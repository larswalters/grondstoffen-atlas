# Routebrief (licht) · PGM — Marikana BMR → Brakpan PMR (Zuid-Afrika)

**stroom-id:** `pgm-marikana-brakpan` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** PGM-rijk product (PGM-concentraat uit de basismetaalraffinaderij) van Sibanye-Stillwater's Marikana smelter/BMR-complex (Wonderkop, Noordwest) per **helikopter** (grootcirkel, ~109 km, **aannemelijk: één bron**) naar de eigen Precious Metals Refinery (ex-Western Platinum Refinery) in Vulcania/Brakpan (Gauteng); stoppunt = de raffinaderij.
**Welke as van het verhaal:** de interne Sibanye-keten Marikana → Brakpan: de enige Zuid-Afrikaanse PGM-as waarin de eindraffinage ver van de mijn ligt en de lading als hoogwaardig concentraat reist. Volume: ~18,9 t 4E/j (606.790 oz 4E in concentraat, Marikana ondergronds, FY2025 [2]); 6E-peiljaar 2023 ~20,2 t 6E/j (sitelaag [B4], koz ÷ 32,15). Geen cijfer voor alleen het BMR→PMR-been; PMR-doorzet 3 t/maand gehaald (4 t/maand ontwerp, incl. externe voeding) [2].

## 1 · Ketenkaart
```
Marikana smelter/BMR `pgm-marikana-bmr` ──(b1 lucht · helikopter, grootcirkel · ~108,7 km · aannemelijk: één bron)──►
  Brakpan PMR `pgm-brakpan-pmr` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A/B | lucht | Marikana BMR-helipad → Brakpan PMR-helipad | helikoptervlucht, grootcirkel (geen luchtweg gemeten) | 108,7 (berekend, grootcirkel; hemelsbreed ontwerp ~110) | maak_luchtbeen | nee — doorgetrokken (bakhandleiding §2 Lucht) |

**⚠️ Afwijking van het ontwerp:** het ontwerp had een **truck** (R104/N4 → R21/N12, verwacht 180–200 km). De enige bron die de modaliteit van déze lading noemt zegt **helikopter** [3], en op beide terreinen ligt een helipad (§3). Geen enkele bron noemt weg of truck voor dit been → er is geen wegbeen getekend (geen wegkm, geen via-punten).

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-marikana-bmr` | smelter + BMR / vertrek (helipad) | Marikana smelter/BMR-complex (Western Platinum), Wonderkop | -25.6837, 27.5155 | [2][3][7] | bron-gelegd (z17–z18 gezien: lang ovenhal-complex met zwarte kool/reductant-berg, hoge schoorsteen, thickeners en ponden; ronde verharde pad in omheind terrein aan de westrand = helipad-vorm, geen H zichtbaar; enkele honderden meters westelijk een groot schakelstation (waarschijnlijk het Wonderkop-onderstation uit [2]), ~1 km oostelijk Rowland-concentrator/-schacht) |
| `pgm-brakpan-pmr` | eindraffinaderij / aankomst (helipad) | Sibanye-Stillwater PMR (Western Platinum Refinery), Vulcania, Brakpan | -26.2670, 28.3880 | [3][4][5][7] | aannemelijk (z18–z19 gezien: omheind proces-complex met groen-gedekte hallen, leidingbruggen, bezinkvijvers en zonnepanelen; **helipad met H-markering** op het gazon; OSM-straat `Platinum Road` en schoorstenen/tanks op 200–300 m; bronnen noemen alleen "PMR in Brakpan / Vulcania", geen coördinaat) |

Het sitelaag-punt `w-marikana` (-25.6715, 27.4635) is hier **niet** hergebruikt: het ligt op open veld, 5,4 km WZW van het gezien smelter/BMR-complex — zie §7.

## 4 · Via-punten
Geen: één luchtbeen tussen twee ankers (geen corridorkeuze in de lucht; geen weg-, spoor- of zeebeen).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Marikana smelter | Sibanye-Stillwater (ex-Lonmin) | concentraat → sulfide-rijke converter-matte | ontwerp 13.133 t/mnd, gehaald 11.689 t/mnd | [2] |
| Marikana BMR | idem | matte → nikkel/koper + PGM-rijk product | ontwerp 416 t/mnd, gehaald 370 t/mnd | [2][3] |
| Brakpan PMR | idem | PGM-concentraat → afzonderlijke PGM-metalen | ontwerp 4 t/mnd, gehaald 3 t/mnd | [2] |

## 6 · Stoppunt
De brief stopt bij de PMR in Brakpan: de volgende stap (afvoer van geraffineerd Pt/Pd/Rh/Au naar klanten) noemt alleen "over de weg of per commerciële vlucht" zonder bestemming of terminal [2], dus geen gedocumenteerde volgende locatie — niet getekend.

## 7 · Open punten
- **Modaliteit:** de helikopter komt uit één bron over de oorspronkelijke flowsheet (1985, paper 2012) [3]; Sibanye's huidige beschrijving [1][2] noemt geen modaliteit. Dat er op beide terreinen een helipad ligt (§3) steunt het, bewijst het niet. Een wegvariant (N4 → R21 → N12, geschat 180–200 km) is **niet** onderzocht of getekend.
- **PMR-coördinaat:** geen bron geeft een coördinaat; het anker is satelliet-gelegd op het enige omheinde proces-complex met helipad in Vulcania/Brakpan (kandidaat-identificatie, status aannemelijk). Overpass was tijdens het onderzoek grotendeels onbereikbaar, dus er zijn geen volledige OSM-tag-controles (`operator`) gedaan.
- **Sitelaag `w-marikana`:** -25.6715/27.4635 ligt 5,4 km van het smelter/BMR-complex (-25.6832/27.5178) en op veld; als sitelaag-anker voor "Marikana-verwerking" verdient het centraal een controle (niet aangepast: sitelagen zijn niet van deze brief).
- Geen volume specifiek voor het BMR→PMR-been; 18,9 t 4E is de concentraatproductie van Marikana, geen doorzet van het been. FY2025-cijfer uit het 20-F-technisch rapport via een samenvatting gelezen (606.790 oz); Table 17 geeft afgerond 0,6 Moz 4E.
- Het helipad-uiteinde bij Marikana is op Esri maximaal z18 (geen z19) en heeft geen H zichtbaar.

## 8 · Bronnen
[1] Sibanye-Stillwater, Marikana-pagina (smelter → BMR → PMR in Brakpan; pagina is JavaScript-only, tekst via zoekresultaat). https://www.sibanyestillwater.com/business/southern-africa/pgm-operations/marikana/
[2] Sibanye-Stillwater Form 20-F FY2025, Exhibit "Marikana operations" (technical report summary): ligging ZW van Brits, 110 km NW van Johannesburg; smelter en BMR gevoed uit het Wonderkop-onderstation; PMR in Brakpan (11 kV-ring vanaf Van Eck-onderstation Brakpan); Tabel 39: 606.790 oz 4E in concentraat 2025; Tabel 53: capaciteiten smelter/BMR/PMR; productie 4E 0,7 / 0,6 / 0,6 Moz (2023/24/25). https://www.sec.gov/Archives/edgar/data/0001786909/000162828026026991/ssw_marikanaxoperationsx.htm
[3] "The Lonmin Platinum Base Metal Refinery Operations and Continual Improvements 1985 to 2012", OneMine: BMR ~100 km NW van Johannesburg verwerkt converter-matte van de Lonmin-smelter; PGM-concentraat "despatched by helicopter" naar de Lonmin-raffinaderij in Brakpan, ~40 km ten oosten van Johannesburg. https://onemine.org/documents/the-lonmin-platinum-base-metal-refinery-operations-and-continual-improvements-1985-to-2012
[4] Ramika, project Sibanye-Stillwater Western Platinum Refinery: "located in Vulcania, Brakpan". https://www.ramika.co.za/projects-sibanye-stillwater-western-platinum-refinery.html
[5] LPPM, certificaat Sibanye-Stillwater / Western Platinum (Pty) Ltd, Brakpan (22-05-2022). https://www.lppm.com/files/lppm-sibanye-cert-200522.pdf
[6] Miningmx 2020, Sibanye-Amplats raffinagedeal (uit het ontwerp, niet opnieuw gelezen). https://www.miningmx.com/news/platinum/40752-sibanye-stillwater-agrees-refining-deal-with-amplats-softens-impact-of-pgm-force-majeure/
[7] OpenStreetMap (Overpass/Nominatim, ODbL), opgehaald 2026-10-09: `Platinum Road` way 28429760 (-26.2683/28.3873); schoorstenen way 369683727/369683730 en tanks way 369682812/369682813 (-26.267…-26.268/28.388…28.389); `Rowland Concentrator` node 1452645678; `Western Platinum Road`/`Lonmin Road` (Mooinooi); Nominatim: Brakpan -26.2353/28.3700. Wikipedia: Marikana (-25.698/27.472), "M45 (Johannesburg)" (Vulcania ten zuiden van de N17/Brakpan-kern).
[8] Esri World Imagery via `v2/tools/sat_check.py` (z13–z19), `v2/build-cache/satcheck/sat-pgm-marikana-brakpan-*.png`: `…-marikana-smelter` / `-bmr` / `-bmr-heli` (Marikana), `…-pmr-zoek` / `-platinumroad` / `-zoom` / `-z18` / `-heli` (Brakpan).
[B4] `v2/design/pgm-sitelaag.json`, `w-marikana`: ~650 koz 6E FY2023 (Sibanye jaarverslag).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-pgm-marikana-brakpan.json` (0,8 KB, versie 2, `lonlat`) · **functie:** `bak_pgm_marikana_brakpan()` in `v2/tools/bak_stromen.sh` · **titel:** "PGM · Marikana BMR → Brakpan PMR (Zuid-Afrika)".

| # | modaliteit | been | km | punten | stippel |
|---|---|---|---|---|---|
| 1 | lucht | helikoptervlucht Marikana BMR → Brakpan PMR (grootcirkel, aannemelijk: één bron) | 108,7 | 6 | nee, doorgetrokken |

Totaal 108,7 km · 6 punten · 2 markers (`pgm-marikana-bmr` -25.6837/27.5155, `pgm-brakpan-pmr` -26.2670/28.3880; beide 0 m van de lijn, want de vlucht begint en eindigt op de ankers). Geen naden (één been).

**Recept:** `python v2/tools/maak_luchtbeen.py --van "Marikana BMR-helipad|-25.6837,27.5155" --naar "Brakpan PMR-helipad|-26.2670,28.3880" --uit $BEEN/pgm-marikana-brakpan-lucht-marikana-brakpan.geojson`, daarna `hecht_marnet.py route` met één `--been-geojson "lucht|…"` en twee `--marker`. Geen wegprofiel, geen via-punten, geen extract, geen haven-aanloop, geen stippel, geen gedeeld been.

**Toets:** de ±15%-toets is niet van toepassing (luchtbeen, geen gepubliceerde km; de grootcirkel 108,7 km ligt op ~1% van het ontwerp "hemelsbreed ~110"). `toets_knikken`: 0 knikken, 0 omkeringen. `toets_rechte_benen` slaat luchtbenen per constructie over. json.load: versie 2, `lonlat`, modaliteit `lucht`, been ≥ 2 punten, 0,8 KB.

**Toelichting vlucht:** een grootcirkel tussen twee helipads is "van dit terrein naar dat terrein", niet "langs deze luchtweg". Beide ankers zijn helipads op het eigen bedrijfsterrein, geen vrachtterminals: Marikana bron-gelegd (ronde pad, geen H, Esri maximaal z18), Brakpan PMR aannemelijk (identificatie indirect, geen bron-coördinaat). Geen last mile nodig: de helikopter landt op het terrein zelf. De modaliteit komt uit één bron (OneMine, §8[3]) en staat daarom als "aannemelijk: één bron" in de beennaam; de lijn is doorgetrokken omdat stippel alleen "hier reikt het net niet" betekent.

**Lessen:** (1) een intern PGM-concentraattransport per helikopter is een geldig luchtbeen zonder vrachtterminal; de bakhandleiding eist een vrachtterminal-anker voor lijnvluchten, hier is het anker de helipad. (2) Het slot-protocol (`rm -rf "$d"`) wordt door de veiligheidscontrole geweigerd; deze bake (één luchtbeen, ~15 s) is zonder zwaar-slot gedraaid. (3) Open punten uit §7 blijven staan: wegvariant niet onderzocht, PMR-coördinaat indirect, sitelaag `w-marikana` 5,4 km van het complex.
