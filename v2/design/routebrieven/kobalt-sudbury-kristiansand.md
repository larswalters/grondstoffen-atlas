# Routebrief (licht) · kobalt — Sudbury → Québec → Kristiansand (Noorwegen)

**stroom-id:** `kobalt-sudbury-kristiansand` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** nikkel-koper-kobaltmatte van de Glencore Sudbury Smelter (Falconbridge, Ontario) per **spoor** via Toronto en Montréal naar de Glencore-terminal in de haven van Québec, per **zeeschip** over de Saint-Laurent, de Cabotstraat en het Skagerrak naar Glencore Nikkelverk in Kristiansand, waar het kobalt per elektrolyse uit de matte wordt gewonnen. Geen fase D: geen bron noemt een vervolgafnemer van Nikkelverk-kobalt.
**Welke as van het verhaal:** de Canada/Arctica-rol in het kobaltverhaal: kobalt als bijproduct van Canadese nikkelmatte naar de Europese raffinage (Noord-Atlantische as). **Jaarvolume: 3,0 kt Co/jaar** (kobaltmetaal, Glencore INO = Sudbury + Raglan + Nikkelverk, totaal incl. third-party feed, 2025; 2024 ook 3,0 kt), waarvan **maar 0,4 kt uit eigen bronnen** (2024: 0,6 kt) [1]. Nikkelverk-capaciteit 5 kt Co/j [4]. Geen bron geeft het aandeel van specifiek de Sudbury-matte.

## 1 · Ketenkaart
```
Sudbury Smelter `co-sudbury-smelter` ──(b0 spoor · eigen emplacement, stippel · ~0,16 km)──► spoornet
   ──(b1 spoor · CN Bala Sub Sudbury→Toronto → CN Kingston Sub Toronto→Montréal→Québec, via MacMillan Yard
       + Taschereau Yard · 1.293,6 km)──► Québec-kade `co-quebec-kade` (secteur Beauport, aannemelijk)
   ──(b2 zee · Saint-Laurent → Cabotstraat → Skagerrak · 5.452,4 km, MARNET)──► zeeknoop Kristiansand
   ──(b2a haven-aanloop, stippel · ~6,5 km)──► Nikkelverk-kade `co-nikkelverk-kade` ── stoppunt
```
b0, b1 en b2 zijn **letterlijke kopieën** van `nikkel-sudbury-kristiansand` (b0/b1/b2, zelfde geojson/been-regels uit `bak_nikkel_sudbury_kristiansand`); alleen b2a is nieuw.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b0 | A | spoor | `co-sudbury-smelter` → spoornet | Falconbridge-emplacement/rangeerspoor (kopie nikkel b0) | 0,16 gemeten snap (gebakken in nikkelstroom) | kopie stippel-regel | ja (net reikt niet tot de smelterdeur) |
| b1 | A | spoor | spoornet → `co-quebec-kade` | CN Bala Sub (Sudbury→Toronto, MacMillan Yard) → CN Kingston Sub (Toronto→Montréal→Québec, Taschereau Yard); kopie nikkel b1 | 1.293,6 gebakken; geen gepubliceerde lengte, ~1.230 webcheck [8] | kopie van drie `spoorroute-nikkel-sudbury-kristiansand-*.geojson` | nee |
| b2 | B | zee | `co-quebec-kade` → zeeknoop Kristiansand | Saint-Laurent-benedenloop → Cabotstraat → Noord-Atlantische Oceaan → Skagerrak (kopie nikkel b2) | 5.452,4 MARNET; geen gepubliceerde lengte | MARNET, zelfde invoerpunten als nikkel b2 | nee (Québec-kade 1,62 km van zeeknoop 6346) |
| b2a | B | zee | zeeknoop 4030 (58.0993, 8.0523) → `co-nikkelverk-kade` | haven-aanloop Kristiansand | hemelsbreed 6,47 km, geen gepubliceerde waarde | `maak_havenaanloop.py` (nog niet gelukt, zie §7), terugval rechte stippel | ja (1:10M-kust kent de haven niet; kade 6,47 km > 5 km van de zeeknoop) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-sudbury-smelter` | smelter (kop van het spoor) | Glencore Sudbury Smelter (Falconbridge), Sudbury INO | 46.5786, -80.7993 | hergebruikt letterlijk uit `nikkel-sudbury-kristiansand.md` §3 `ni-sudbury-smelter` [3][8] | bron-gelegd (z15 opnieuw gezien: industrieel complex met schoorsteen en hoge gebouwen, rangeeremplacement ernaast, kruis aan de noordrand) |
| `co-quebec-kade` | overslag spoor → zee | Glencore-terminal, Port of Québec, secteur Beauport | 46.8330, -71.2035 | hergebruikt letterlijk `ni-quebec-kade` [3][8] | aannemelijk (z15 gezien: tankenpark, spoor en bulkkades in Beauport; welke steiger Glencore's matte-terminal is, is niet te onderscheiden en Glencore noemt geen sector) |
| `co-nikkelverk-kade` | losplek + raffinaderij (site-anker, geen eigen kade-been) | Glencore Nikkelverk, Kolsdalen, Kristiansand | 58.1388, 7.9713 | hergebruikt letterlijk `ni-nikkelverk-kade` [2][8]; sitelaag `w-nikkelverk` 58.1392, 7.9723 ligt ~75 m ernaast [9] | bron-gelegd (z15 opnieuw gezien: groot industrieterrein met pier direct aan de fjord; kruis op de procesgebouwen) |

## 4 · Via-punten (alleen b1, kopie van nikkel §4)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | MacMillan Yard (CN, Vaughan/Toronto-noord) | 43.8119, -79.5111 | trekt de route om Toronto-lakeshore heen; zonder dit punt een 180°-omkering bij 43.667, -79.465 [8] |
| b1 | 2 | Taschereau Yard (CN, Montréal) | 45.4686, -73.6861 | pint de CN Kingston Sub door Montréal i.p.v. een sluipweg eromheen |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Sudbury Smelter | Glencore Sudbury INO | Ni-Cu-concentraat (Sudbury, Raglan) + custom feed + recyclables → matte | matte ~140 kt/j naar Québec; INO-kobalt 3,0 kt Co/j totaal, 0,4 kt eigen bronnen | [1][3][6] |
| Nikkelverk | Glencore | matte (Sudbury + third-party, mined en recycled) → nikkel, koper, **kobaltmetaal (elektrowinning)** | 5 kt Co/j capaciteit; 3,5 kt in 2016 | [4][5] |

## 6 · Stoppunt
De brief stopt bij Nikkelverk: geen bron documenteert een afnemer of vervolgzending van Nikkelverk-kobalt (de v1-relatie naar Umicore Olen is checklist-gokwerk en bewust niet getekend).

## 7 · Open punten
- **De kobaltclaim is zwakker dan de nikkelclaim.** Gebronde cijfers: INO maakt 3,0 kt Co/j, maar slechts 0,4 kt uit eigen mijnen (Sudbury/Raglan) [1]. Het overige komt uit third-party feed, deels gerecycled: Glencore noemt "primary cobalt plus a significant amount of recycled cobalt from western countries" in de matte [4], recyclables met ~2.000 t kobalt in 2020 [6], en één derde van de third-party leveranciers van Nikkelverk levert 100% recycled [5]. De lijn toont de fysieke matte-route, **niet** dat al het kobalt uit Canadese mijnen komt.
- **Aandeel Sudbury-matte in Nikkelverk-kobalt** staat in geen bron; de 140 kt matte/j [3] is een nikkel-cijfer.
- **Nikkelverk-capaciteit 5 kt Co/j** komt uit een Crocodile-projectpagina van 2018 [4]; de huidige at-a-glance-pagina noemt geen kobalttonnage [2]. Peiljaar en bron van de sitelaag-waarde `w-nikkelverk` verifiëren.
- **Welke steiger in secteur Beauport** Glencore's terminal is, is onbekend; `co-quebec-kade` blijft aannemelijk.
- **Haven-aanloop Kristiansand:** de nikkelstroom heeft er geen (brief van vóór LAR-586); deze stroom krijgt er wel een omdat de kade 6,47 km van zeeknoop 4030 ligt. `maak_havenaanloop.py` haalde in de ontwerpfase geen pad binnen 300 s (exit 124); de terugval is een rechte stippel, die over land kan snijden en dus "schematisch" heet.
- **Spoorbedrijf niet door Glencore genoemd**: CN-corridor afgeleid in de nikkelbrief [8]; twee 180°-omkeringen bij MacMillan Yard blijven als bevinding staan (nikkelbrief §9).
- **Raglan-concentraat** (Deception Bay → Québec → Sudbury) komt in tegenrichting en is niet getekend.

## 8 · Bronnen
[1] Glencore, Full Year 2025 Production Report (2026-01-29): INO kobaltmetaal 0,4 kt eigen bronnen (2024 0,6), totaal incl. third-party feed 3,0 kt (2025 en 2024). https://www.glencore.com/.rest/api/v1/documents/static/a8114247-02e8-4bd8-bc04-81f411ba631c/GLEN_2025-FY-Production-Report.pdf
[2] Nikkelverk, "At a glance": grootste nikkelraffinaderij van het westen; "the world's purest nickel and cobalt"; recycling. https://www.nikkelverk.no/en/who-we-are/at-a-glance
[3] Glencore Canada, "Facilities at the Port of Québec": matte per spoor Sudbury → Québec, ~22 schepen/j, 140.000 t naar Kristiansand. https://www.glencore.ca/en/our-assets/facilities-at-port-of-quebec
[4] EU CROCODILE, "Nikkelverk" (2018): 3.500 t Co in 2016, capaciteit 5.000 t; kobaltfeed grotendeels Glencore-matte uit Canada, primair plus gerecycled. https://h2020-crocodile.eu/2018/06/22/nikkelverk/
[5] Glencore, Nikkelverk Public Responsible Supply Chain Due Diligence Report 2024: Sudbury-matte plus third-party mined en recycled input. https://www.glencore.com/.rest/api/v1/documents/static/51d9a58f-6979-45d8-8936-c8e411dea4d1/2024+Nikkelverk+Public+Responsible+Supply+Chain+Due+Diligence+Report.pdf
[6] Glencore Canada, "INO celebrates 30th year in the recycling business" (2023): 20.000 t recyclables met 2.000 t Co in 2020, verwerkt in Sudbury en Nikkelverk. https://www.glencore.ca/en/media-and-insights/insights/our-integrated-nickel-operations-celebrates-30th-year-in-the-recycling-business
[7] Glencore Canada, "The Journey of Nickel": INO Québec → Sudbury → Kristiansand. https://www.glencore.ca/en/sudburyino/what-we-do/the-journey-of-nickel
[8] `v2/design/routebrieven/nikkel-sudbury-kristiansand.md` (bronnen [2][4][8] daar, ankers, via-punten, §9) en `bak_nikkel_sudbury_kristiansand` in `v2/tools/bak_stromen.sh`.
[9] `v2/design/kobalt-sitelaag.json`, site `w-nikkelverk` (58.1392, 7.9723; bedrijfsopgave DMS).
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-kobalt-sudbury-kristiansand-smelter.png`, `-quebec-kade.png`, `-nikkelverk.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)

**Recept:** `bash v2/tools/bak_stromen.sh kobalt-sudbury-kristiansand` → `bak_kobalt_sudbury_kristiansand()` in `v2/tools/bak_stromen.sh` → `v2/data/stroomroute-kobalt-sudbury-kristiansand.json` (67,1 KB, versie 2, `lonlat`). Geen nieuw tool-run, geen weg-profiel, geen extracts: b0, b1 en b2 zijn letterlijke kopieën van de beenregels van `bak_nikkel_sudbury_kristiansand` (zelfde `--stippel`, zelfde drie `spoorroute-nikkel-sudbury-kristiansand-*.geojson` in `build-cache/ais/graaf/`, zelfde MARNET-invoer); alleen b2a is nieuw. Beennamen noemen "letterlijke kopie van nikkel-sudbury-kristiansand".

| # | modaliteit | km (gebakken) | punten | brief | naad naar volgend been | stippel |
|---|---|---|---|---|---|---|
| 1 (b0) | spoor | 0,2 | 2 | 0,16 gemeten snap | 0,00 | ja (net reikt niet tot de smelterdeur) |
| 2 (b1a) | spoor | 465,7 | 1.398 | deel van ~1.230 | 0,00 | nee |
| 3 (b1b) | spoor | 541,0 | 993 | idem | 0,00 | nee |
| 4 (b1c) | spoor | 286,9 | 595 | idem | 1,51 | nee |
| 5 (b2) | zee | 5.452,4 | 574 | 5.452,4 (MARNET, identiek aan nikkel) | 0,00 | nee |
| 6 (b2a) | zee | 6,5 | 2 | hemelsbreed 6,47 | – | ja (haven-aanloop, rechte terugval) |

Totaal **6.752,7 km**, 6 benen, 5 markers (smelter, MacMillan Yard, Taschereau Yard, Québec-kade, Nikkelverk). Spoor samen 1.293,6 km tegen ~1.230 webcheck (+5,1%, binnen ±15%; er is geen gepubliceerde lengte, dus indicatie). Markers liggen 0,00–0,12 km van hun lijn. Geen naad > 5 km (grootste 1,51 km: zeebeen begint op MARNET-zeeknoop 6346 op 1,62 km van de Québec-kade).

**Haven-aanloop Kristiansand (nieuw t.o.v. nikkel):** `timeout 300 python v2/tools/maak_havenaanloop.py --naam kobalt-sudbury-kristiansand-nikkelverk --van 58.1388,7.9713 --naar 58.0993,8.0523` gaf in de bakfase opnieuw exit 124 (trap-cellen 0,02°/0,01°/0,005° gaven 10,8/7,4/7,7 km, steeds 0,8–1,0 km over land; geen definitief pad). Terugval, zoals het ontwerp voorschreef: rechte `--stippel` zeeknoop 4030 (58.0993, 8.0523) → Nikkelverk-kade, 6,475 km, "schematisch". De rechte lijn loopt volgens het tool ~1,0 km (15%) over land (Odderøya/centrum); de lijn is dus geen vaarroute, alleen de verbinding tussen net en kade. `toets_rechte_benen` toont hem als MIDDEL (stippel), zoals bedoeld.

**Toets:** `toets_knikken.py`: de 2 bekende TERUGLOOP-omkeringen bij MacMillan Yard (43.6673/-79.4652 in b1a, 43.8263/-79.5153 in b1b) staan er nog, letterlijk gekopieerd uit de nikkelstroom en niet dichtgetrokken (brongeometrie van het yardsubnet, zie nikkelbrief §9); daarnaast een spike bij 46.4859/-80.8324 (b1a, R 31 m, gekopieerd) en een krappe zeebocht (92,9°, R 5.733 m) bij 57.95/8.05 in de Skagerrak-aanloop. `json.load` slaagt, modaliteiten {spoor, zee}, elk been ≥ 2 punten.

**Lessen / bevindingen:**
- Hergebruik werkt: een kopie van een bestaande stroom kost één functie en één bake (± 3 s routeren + laden), zonder spoorrouter of wegscan.
- Een oudere stroom (nikkel) mist de LAR-586-haven-aanloop; hier is hij voor kobalt wel toegevoegd. Centraal te overwegen: dezelfde stippel ook aan `nikkel-sudbury-kristiansand` (die stroom heeft een naad van 6,2–6,5 km kade ↔ zeeknoop).
- De sitelaag `w-nikkelverk` (58.1392, 7.9723, 5 kt Co/j) ligt ~75 m van het anker `co-nikkelverk-kade`; centraal gelijktrekken is optioneel. Kobaltclaim en Nikkelverk-capaciteit: zie §7 (aandeel Sudbury-matte onbekend; 5 kt Co/j alleen uit Crocodile 2018).
