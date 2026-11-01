# Routebrief (licht) · gas — Urucu (Amazonas) → Coari → Manaus (Brazilië)

**stroom-id:** `gas-urucu-manaus` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) ·
**status:** gebakken
**Keten in één zin:** Aardgas uit het Urucu-gasveld (Petrobras, gasverwerking UPGN Urucu, Coari) gaat door één doorlopende landleiding van ca. 663 km
(Gasoduto Urucu–Coari–Manaus, TUM/TAG) door regenwoud en over-/onderwaterstukken naar het thermisch complex Mauá in Manaus (Mauazinho, Rio Negro).
**Welke as van het verhaal:** de enige Braziliaanse transportleiding die volledig geïsoleerd van het nationale gasnet werkt [1][2]; het gas voedt het grootste deel van de
gasgestookte opwekking in Manaus. Volume als CAPACITEIT: ship-or-pay 5,5 Mm³/d ≈ 2,0 bcm/j (2026), gemeten jaarvolume niet gevonden (§7).
Let op: Manaus hangt sinds de Tucuruí-lijn aan het nationale stroomnet (zie §7); gas is dus de belangrijkste brandstof, niet de enige energiedrager.

## 1 · Ketenkaart
```
Urucu UPGN `gas-urucu-upgn` ──(b1 leiding · Gasoduto Urucu–Coari–Manaus (Sectie 1 Urucu–Coari, 2 Coari–Anamã, 3 Anamã–Manaus) · ~665 km, 15 OSM-ways)──►
Mauá-complex Manaus `gas-maua-complex` — stoppunt (thermisch complex aan de Rio Negro)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-urucu-upgn` → `gas-maua-complex` | Gasoduto Urucu–Coari–Manaus (Petrobras/TUM): sectie 1 Urucu–Coari, sectie 2 Coari–Anamã, sectie 3 Anamã–Manaus; de Coari- en Anamã-aftakkingen worden niet getekend | 661 [1] / 663,2 [2][3] → gemeten 665,5 (+0,7% t.o.v. 661; incl. twee naden) | 15 OSM-ways (man_made=pipeline, substance=gas), vooraf gestikt met `maak_leidingbeen_gas_urucu_manaus.py` | nee |

Ways in reisvolgorde (volle way-lengte, km): 627453140 (152,1) · 211623377 (76,7) · 310573689 (2,2, onderwater) · 310573683 (47,7) · 272083194 (2,5) · 321589257 (1,3, onderwater) ·
321589244 (65,2) · 180296516 (127,5) · 272968886 (91,9) · 310573679 (5,5, onderwater) · 310573687 (77,8) · 188456610 (10,0, onderwater) · 627636050 (2,2) ·
627636048 (1,6, onderwater) · 627636049 (0,2) = 664,4 km + 1,0 km naden = 665,5 km gestikt. Namen: "Urucu - Manaus Pipeline (Section 1/2/3)"; de drie laatste stukken bij Manaus zijn naamloos met operator Petrobras Transporte SA.
Naden: 0,032 km (272083194) en 1,012 km (tussen 188456610 en 627636050, bij Manaus); beide ruim onder 5 km, doorgetrokken, geen stippel.
Wel meegenomen: de drie korte "underwater"-stukken (rivierkruisingen) als onderdeel van de lijn. Niet meegenomen: Coari Branch (455269995, 354416265, 354416266), Anama Branch (272968884)
en de spurs 627636056, 257502104, 272093923, 627636053, 627636055, 256765517 (hoort niet bij de hoofdlijn naar Mauá).
OSM-richting is per way verschillend; het script oriënteert elke way op gedeelde node-id tot Urucu → Mauá.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-urucu-upgn` | gasverwerking / kop leiding | Polo Industrial de Urucu, UPGN Urucu (Petrobras, Coari) | -4.8661, -65.2964 | [1][3][4][5] | bron-gelegd (z15 gezien: industrieterrein met procesinstallaties, tanks en een luchtstrip-achtig platform midden in bos, ~330 m ten westen van het kruis; OSM-leidingbegin ligt aan de toegangsweg op het kruis; de voedingsleiding "Gasoduto IMT 3 - UPGN Urucu" (OSM 627643354, 33,3 km) eindigt op -4.8673, -65.2985 = op het plantterrein) |
| `gas-maua-complex` | thermisch complex / eind leiding (stoppunt) | Complexo Termelétrico de Mauá, Mauazinho, Manaus (Mauá 3 e.a.) | -3.1216, -59.9320 | [3][6][7] | bron-gelegd (z15 en z17 gezien: industrieel complex aan de Rio Negro met tankpark, turbinehal, leidingrekken en schakelstation; OSM-leidingeinde op het kruis in het oudere Mauazinho-deel; het nieuwe gasturbinegebouw van Mauá 3 ligt ~560 m noordelijker op pt-Wikipedia-coördinaat -3.1172, -59.9297) |

Hergebruik: geen: `gas-sitelaag.json` en eerdere gas-brieven kennen Urucu en Manaus niet. Beelden: `v2/build-cache/satcheck/sat-gas-urucu-manaus-urucu.png`, `-maua.png`, `-maua-z17.png`.

## 4 · Via-punten
Niet van toepassing: één leidingbeen uit aaneengestikte OSM-ways (geen corridorkeuze zoals bij weg/spoor); geen weg-, spoor-, zee- of luchtbeen, geen haven-aanloop.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| UPGN Urucu (Polo Arara/Urucu) | Petrobras | veldgas (o.a. via IMT 3) → verwerkt gas + LPG; ca. de helft van het geproduceerde gas wordt herinjecteerd | marktaanbod ≈ 6 Mm³/d | [4][5] |
| Gasoduto Urucu–Coari–Manaus | Transportadora Urucu–Manaus (TUM), nu TAG (Engie/CDPQ-consortium, Petrobras-klant) | Urucu → Coari → Anamã → Manaus (20 inch tussen Coari en Anamã) | ontwerp 4,1 Mm³/d ≈ 1,5 bcm/j [3]; ship-or-pay 5,5 Mm³/d ≈ 2,0 bcm/j [5] | [3][5] |
| Mauá 3 e.a. thermisch park Manaus (nu Âmbar Energia) | Âmbar Energia (sinds 2024) | gas → elektriciteit; Mauá 3: 591 MW, max. 2,5 Mm³/d | Manaus-thermo 4,4 Mm³/d in 2023 (≈ 1,6 bcm/j); totaal Manaus-vraag 5,5 Mm³/d | [4][7] |

## 6 · Stoppunt
De brief stopt bij het Mauá-complex: dit is het eind van de OSM-hoofdleiding en de grootste gasverbruiker in Manaus; daarna is het gas verdeeld over meerdere centrales
(Mauá, Cristiano Rocha, Ponta Negra, Tambaqui, Jaraqui, Manauara) en het distributienet van Cigás. Geen fase D/E: geen bron die één afnemer voorbij Mauá als eindpunt aanwijst.

## 7 · Open punten
- **Volume**: geen gemeten jaarcijfer. Capaciteit/contract ship-or-pay 5,5 Mm³/d ≈ 2,0 bcm/j (ASDECEN-bijdrage aan ANP-consultatie 03/2026, peiljaar 2026) [5]; ontwerpstroom 4,1 Mm³/d ≈ 1,5 bcm/j [3];
  thermische afname 4,4 Mm³/d in 2023 ≈ 1,6 bcm/j [4]. Etiket in het project: CAPACITEIT, geen gemeten jaarvolume. Wikipedia (EN) noemt 17 bcm/j (initieel) en 20 bcm/j (capaciteit): onwaarschijnlijk (ruim 8x de ship-or-pay), niet gebruikt.
- **Verhaalclaim "enige energiedrager" klopt niet**: Manaus is gekoppeld aan het nationale net via de Tucuruí-Macapá-Manaus-lijn ("Linhão de Tucuruí", [8]; jaartal 2013 komt uit de haalbaarheidstoets, niet zelf bevestigd).
  Aandeel gas in de opwekking: ASDECEN [5] noemt ~85% van de elektriciteit in het geïnterconnecteerde systeem van Amazonas, het zoekresultaat van de toets ca. 65% van de opwekking in Manaus: verschillende maatstaven, geen één cijfer gebruikt.
- **Eigenaar Urucu**: de verkoop van Polo Urucu aan Eneva is niet doorgegaan (toets); leidingeigenaar is TAG (Engie/CDPQ). Bij eigenaarswissel de namen in de bol-noot nalopen.
- **Eindpunt**: pt-Wikipedia [3] noemt als eind de Refinaria Isaac Sabbá (REMAN) in Manaus; de OSM-hoofdleiding eindigt bij Mauá/Mauazinho. Niet getekend verder dan het OSM-eind.
- **Sitelaag mist Urucu en Mauá** (geen gas-site in Brazilië behalve eerdere stromen): centrale aanvulling nodig voor de gloed.
- **Naad 1,012 km** bij Manaus (rivierkruising) wordt rechtgetrokken in de lijn; geen aparte stippel (OSM-gat, onder de 5 km-norm).

## 8 · Bronnen
[1] Wikipedia (EN), "Urucu–Manaus pipeline": 661 km, drie secties, sectie 1 LPG-leiding omgezet, operator TUM (Petrobras); 17/20 bcm/j-claim (niet gebruikt).
    https://en.wikipedia.org/wiki/Urucu%E2%80%93Manaus_pipeline
[2] Wikipedia (PT), "Gasoduto Urucu-Coari-Manaus": 663,2 km, 139,3 km in negen ramalen, secties A/B1/B2, vazão 4,1 milhões m³/d, TUM/TAG (Engie + CDPQ), in dienst 2009.
    https://pt.wikipedia.org/wiki/Gasoduto_Urucu-Coari-Manaus
[3] OpenStreetMap-bijdragers (ODbL), eigen pbf-scan Geofabrik Brazilië (2026-11-01) en OSM-API 0.6: 15 ways "Urucu - Manaus Pipeline", substance=gas, operator Petrobras; way 627643354 "Gasoduto IMT 3 - UPGN Urucu".
    https://www.openstreetmap.org/way/627453140
[4] IEPUC/PUC-Rio, "Gás natural no Amazonas: estudo socioeconômico e ambiental" (EPE-webmap 2024): Manaus-vraag 5,5 Mm³/d, thermo 4,4 Mm³/d in 2023, marktaanbod Urucu ≈ 6 Mm³/d, 663 km, R$ 4,5 mld, 12 gas-UTE's.
    https://www.iepuc.puc-rio.br/arquivos/GN-Amazonas-EstudoSocioeconomico-Ambiental.pdf
[5] ASDECEN, bijdrage aan ANP Consulta Pública nº 03/2026: UCM "único gasoduto de transporte operando em sistema completamente isolado", ~85% van de elektriciteit in het geïnterconnecteerde systeem van Amazonas, ship-or-pay 5,5 Mm³/d, contract tot nov. 2030.
    https://www.gov.br/anp/pt-br/assuntos/consultas-e-audiencias-publicas/consulta-audiencia-publica/2026/arquivos/cp-03-2026/contribuicao_asdecen_cp_anp_ok.pdf
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15, z17; `v2/build-cache/satcheck/sat-gas-urucu-manaus-*.png`).
[7] Wikipedia (PT), "Usina Termelétrica Mauá 3": 591 MW, max. 2,5 Mm³/d, gas uit Urucu via het UCM-leiding, eigenaar Âmbar Energia sinds 2024, coördinaat -3,1172, -59,9297.
    https://pt.wikipedia.org/wiki/Usina_Termel%C3%A9trica_Mau%C3%A1_3
[8] Wikipedia (PT), "Linhão de Tucuruí": Interligação Tucuruí-Macapá-Manaus, westelijke tak naar Manaus.
    https://pt.wikipedia.org/wiki/Linh%C3%A3o_de_Tucuru%C3%AD

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Bestand:** `v2/data/stroomroute-gas-urucu-manaus.json` (versie 2, lonlat, 70,3 KB) · **titel:** Gas · Urucu → Mauá (Manaus) — Brazilië · **recept:** `bak_gas_urucu_manaus()` in `v2/tools/bak_stromen.sh`.
**Benen:**
| # | modaliteit | naam in het bestand | km | punten | stippel |
|---|---|---|---|---|---|
| b1 | leiding | Gasoduto Urucu-Coari-Manaus (OSM-ways, ~663 km) | 665,5 | 3.432 | nee |
Totaal 665,5 km, 2 markers (UPGN Urucu -4.8661,-65.2964 en Mauá -3.1216,-59.9320; beide 0 km van de lijn: de lijn begint en eindigt op de ankers).
**Recept:** `python v2/tools/maak_leidingbeen_gas_urucu_manaus.py --schrijf` (OSM-API, 15 ways, gestikt tot FeatureCollection `gas-urucu-manaus-leiding-ucm.geojson`), daarna `hecht_marnet.py route` met één `--been-geojson "leiding|…"` en twee `--marker`. Geen zee, haven-aanloop, weg, extract, via-punt, kopie of vlucht.
**Toets:** gemeten 665,5 km tegen gepubliceerd 661 [1] / 663,2 [2][3] = +0,7% / +0,3% (binnen ±15%). Naden 0,032 en 1,012 km (< 5 km, gestikt, geen stippel). `toets_knikken.py`: 1 knik van 60 gr (59 m straal, -3.16411,-60.03254), 0 omkeringen, 0 terugloop. `toets_rechte_benen.py --min-km 5` meldt niets voor deze stroom.
**Afwijkingen van het ontwerp:** geen. Eindpunt = Mauá zoals het id belooft (pt-Wikipedia noemt REMAN als eindpunt; niet getekend, zie §7).
**Lessen:** een doorlopende OSM-pipeline van ruim 660 km in 15 ways is in één keer bakbaar zonder stippel; de drie korte onderwaterstukken en de rivierkruising bij Manaus zitten als gestikte naad in de lijn. Registerregel en sitelaag (Urucu, Mauá) volgen centraal.
