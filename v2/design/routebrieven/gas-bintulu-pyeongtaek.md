# Routebrief (licht) · gas — Bintulu (Maleisië) → Pyeongtaek (Zuid-Korea)

**stroom-id:** `gas-bintulu-pyeongtaek` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** Sarawak-aardgas, vloeibaar gemaakt bij het Petronas LNG-complex (Malaysia LNG,
Bintulu) — een van 's werelds oudste LNG-exportcomplexen (1983) — per **LNG-tanker** over de Zuid-Chinese
Zee → Straat Luzon/Bashi-kanaal → Oost-Chinese Zee → Gele Zee naar de KOGAS-regasterminal Pyeongtaek,
Zuid-Korea's oudste importterminal (1986).
**Welke as van het verhaal:** *Zuidoost-Azië als LNG-producent (Malaysia LNG/Bintulu) naar Zuid-Korea
(KOGAS)* — vult het ontbrekende derde "founding"-LNG-blok (naast Qatar/VS/Australië) aan in dit project.
Vast ondergrenscontract MLNG Tiga ↔ KOGAS: max. 2,0 Mtpa ≈ 2,7 bcm/j, 2008–2028, DES-basis [2]; Korea nam
in 2005 al 26% van de totale Malaysische LNG-export af, naast Japan (65%) en Taiwan (9%) [1] — dit
contract is dus een deelcontract/ondergrens, geen totaalcijfer voor de hele stroom (zie §7).

## 1 · Ketenkaart
```
Petronas LNG-complex / Malaysia LNG, Bintulu `gas-bintulu-kade`
   ──(b1 zee · haven-aanloop, stippel · ≈21,5 km)──► zeeknoop 5430 (Zuid-Chinese Zee)
   ──(b2 zee · Zuid-Chinese Zee → Straat Luzon/Bashi-kanaal → Oost-Chinese Zee → Gele Zee ·
       ~4.300–4.600 km, MARNET)──► zeeknoop 5632 (bij Pyeongtaek)
   ──(b3 zee · haven-aanloop, stippel · ≈5,4 km)──►
   Pyeongtaek LNG Terminal (KOGAS) `gas-pyeongtaek-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Bintulu-kade (MLNG-jettycomplex) → zeeknoop 5430 | haven-aanloop, MLNG-jettycomplex → Zuid-Chinese Zee | ≈21,5 [gemeten, hecht_marnet-zeeknoopcheck op de sitelaag-anker: 21,479 km, zie §9-voorbereiding] | `maak_havenaanloop.py` | ja — kade ligt 21,5 km van de zeeknoop (> 5 km, LAR-586) |
| b2 | B | zee | zeeknoop 5430 → zeeknoop 5632 | Zuid-Chinese Zee → Straat Luzon/Bashi-kanaal → Oost-Chinese Zee → Gele Zee | 4.234,4 [gemeten via `hecht_marnet.py route` in de haalbaarheidstoets — binnen de ontwerpbandbreedte 4.300–4.600 km*, omwegfactor 1,02 tegen de grootcirkel 4.157 km, dus een reële MARNET-uitkomst] | MARNET | nee |
| b3 | B | zee | zeeknoop 5632 → Pyeongtaek-kade | haven-aanloop, Gele Zee → KOGAS-jetty | ≈5,4 [gemeten, hecht_marnet-zeeknoopcheck: 5,405 km, zie §9-voorbereiding] | `maak_havenaanloop.py` | ja — kade ligt net over de 5 km-grens van de zeeknoop (LAR-586) |

\* 4.234,4 km ligt net onder de ondergrens van de ontwerpbandbreedte (4.300–4.600) — plausibele
MARNET-uitkomst, zie §7.

Fase A (offshore Sarawak/Sabah/Miri-gasvelden → Bintulu, via pijpleiding [1]) **vervalt**: diffuus
offshore-brongebied zonder enkelvoudig anker, zelfde situatie als bij eerdere VS-Golfkust-ketens in dit
project. Fase C (Pyeongtaek-regasterminal → KOGAS-nationale net) wordt niet als aparte lijn getekend: de
regasterminal is zelf het knooppunt waar LNG weer pijpleidinggas wordt (zie §6). Fase D vervalt: geen bron
noemt een specifieke fabriek of afnemer stroomafwaarts van Pyeongtaek.

## 3 · Ankers (één per site en per overslag — beide hergebruikt, letterlijk)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-bintulu-kade` (= `w-malaysialng`) | overslag leiding/LNG → zee (liquefactieterminal, MLNG-jettycomplex) | Petronas LNG-complex (Malaysia LNG), Bintulu, Sarawak | 3.2822, 113.0882 | [4][5], hergebruikt uit `v2/design/gas-sitelaag.md`/`.json` ([B10]) | bron-gelegd (satelliet z17, al vastgelegd in de sitelaag: kruis op het procesterrein tussen de bolvormige LNG-tanks; exacte MLNG-jetty binnen het complex nog te preciseren bij de bake) |
| `gas-pyeongtaek-kade` (= `w-pyeongtaek`) | overslag zee → leiding (regasterminal, KOGAS-terrein) | Pyeongtaek LNG Terminal (KOGAS) | 37.00242, 126.78434 | [4][5], hergebruikt uit `v2/design/gas-sitelaag.md`/`.json` ([B30]), al eerder gebruikt als OSM-anker | bron-gelegd (satelliet z14, al vastgelegd in de sitelaag: kruis midden op het tankpark, meerdere ronde LNG-tanks zichtbaar) |

## 4 · Via-punten
Niet van toepassing: alle drie benen zijn `zee`, geen landbeen met een corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Petronas LNG-complex (Malaysia LNG) | Petronas (+ Shell, Mitsubishi, Nippon Oil, Sarawak State Government) | offshore pijpleidinggas (Sarawak/Sabah/Miri) → LNG | 9 trains (Satu/Dua/Tiga + Train 9), ~29,3 Mtpa ≈ 39,8 bcm/j gecombineerd (algemeen bekend, sitelaag [B10]); installed capacity 21,85 Mtpa in 2005 vóór Train 9 (+3,6 Mtpa, 2016) [1] | [1][4] |
| Pyeongtaek LNG Terminal | KOGAS | LNG → pijpleidinggas | regasificatiecapaciteit 1.721,81 bcf/j ≈ 48,8 bcm/j (sitelaag [B30]); ontvangstcapaciteit 30,1 Mt/j, operationeel sinds 1986 — KOGAS' oudste terminal, eerste gas naar de Pyeongtaek-energiecentrale [2][3] | [2][3][4] |

## 6 · Stoppunt
De brief stopt bij Pyeongtaek: hier wordt LNG weer pijpleidinggas en gaat het het Zuid-Koreaanse
nationale net in (KOGAS, 5.346 km pijpleiding, 216 steden/gemeenten [3]). Geen bron koppelt een specifieke
lading aan één eindgebruiker of fabriek — fase D/E vervallen.

## 7 · Open punten
- Het ontwerp-JSON claimt `regios_extracts: maleisie aanwezig=true`, maar er staat **geen**
  Maleisië-Geofabrik-extract in `v2/build-cache/geofabrik/` (187 extracts gecontroleerd, bevestigd door de
  haalbaarheidstoets). Blokkeert deze keten niet (geen land-been), maar niet overnemen in een latere
  Maleisië-keten die wél een wegbeen nodig heeft.
- Het enige harde contractcijfer (2,0 Mtpa, MLNG Tiga ↔ KOGAS, 2008–2028, DES [2]) is expliciet een
  deelcontract/ondergrens — gecorroboreerd als "breder dan dit ene contract" door Wikipedia "Malaysia LNG"
  (Korea 26% van de totale Malaysische export, peiljaar 2005 [1]), maar er is geen actueel (2020s)
  totaalcijfer voor de volledige Bintulu→Korea-stroom gevonden binnen het webbudget.
- b2's km (4.234,4, uit de haalbaarheidstoets) is een MARNET-routeruitkomst, geen gepubliceerde
  end-to-end ladingroute-lengte — zwakke meetlat voor een been van deze lengte, zelfde klasse als
  gas-corpuschristi-incheon §7 en olie-habshan-chiba §9.
- Exacte MLNG-jetty binnen het Bintulu-complex (drie LNG/LPG-jetties in het MLNG Jetty Terminal [1]) niet
  gepreciseerd — de hergebruikte sitelaag-coördinaat ligt op het procesterrein, niet op één specifieke
  steiger; eventueel te verfijnen bij de bake, geen blokkade voor deze lichte brief.
- Zeeknoop-afstanden zijn vooraf gemeten met het script uit de bakhandleiding §2 (21,479 km / 5,405 km,
  bevestigd door de haalbaarheidstoets) — nog niet bevestigd door een echte bake; de exacte snap kan een
  fractie afwijken.

## 8 · Bronnen
[1] Wikipedia, "Malaysia LNG" — 9 liquefactietrains (MLNG Satu/Dua/Tiga + Train 9, 1983–2016), installed
capacity 21,85 Mtpa in 2005 (+3,6 Mtpa Train 9 in 2016); markten (2005): Japan 65%, Korea 26%, Taiwan 9%;
drie LNG-jetties + één LPG-jetty in het MLNG Jetty Terminal; gas via pijpleiding vanaf offshore
Bintulu/Miri/Sabah (Petronas Carigali, Shell). https://en.wikipedia.org/wiki/Malaysia_LNG (pageid 14469097)
[2] JOGMEC, "36. KOGAS" (oil & gas info journal, 2023) — KOGAS-LNG-contractentabel: Malaysia/MLNG III
(Tiga), contractperiode 2008–2028 (20 jaar), max. 2,0 Mt/j, levering DES; KOGAS-ontvangstterminals: Pyeong­
taek 30,1 Mt/j sinds 1986 (oudste), Incheon 40,0 Mt/j sinds 1996. https://journal.jogmec.go.jp/content/300513859.pdf
(omgeleid vanaf de door het ketenontwerp opgegeven url oilgas-info.jogmec.go.jp/…/4_36_kogas_2023_en.pdf)
[3] Wikipedia, "Korea Gas Corporation" — staatsbedrijf sinds 1983, een van 's werelds grootste LNG-kopers,
vijf regasterminals + 5.346 km pijpleidingnet, bevoorraadt 216 steden/gemeenten; LNG-import sinds 1986,
eerste levering aan de Pyeongtaek-energiecentrale. https://en.wikipedia.org/wiki/Korea_Gas_Corporation
[4] `v2/design/gas-sitelaag.md` / `gas-sitelaag.json` — anker `w-malaysialng` (3,2822/113,0882,
bron-gelegd, satelliet z17, [B10]) en `w-pyeongtaek` (37,00242/126,78434, bron-gelegd, satelliet z14,
[B30]), beide letterlijk hergebruikt.
[5] Ketenontwerp + haalbaarheidstoets van deze golf (orkestrator-JSON, M31 golf 6, 2026-09-28) —
webcheck met de exacte sitelaag-ankers (21,479 km / 5,405 km) en volledige MARNET-route zeeknoop→zeeknoop
(4.234,4 km, omwegfactor 1,02 tegen de grootcirkel 4.157 km).
[6] `v2/tools/hecht_marnet.py` (eigen herberekening, bakhandleiding §2, 2026-09-28) — zeeknoop 5430 op
3,29960/112,89550 (21,479 km van `w-malaysialng`); zeeknoop 5632 op 37,01130/126,72450 (5,405 km van
`w-pyeongtaek`) — bevestigt de haalbaarheidstoets exact.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Recept:** `bash v2/tools/bak_stromen.sh gas-bintulu-pyeongtaek` (functie `bak_gas_bintulu_pyeongtaek()`
in `v2/tools/bak_stromen.sh`, vlak vóór de dispatch-ankerregel). Drie benen, alle `zee`, in reisvolgorde.

| # | modaliteit | km | punten | stippel | naam |
|---|---|---|---|---|---|
| 1 | zee | 22,1 | 37 | ja (over water, geojson) | haven-aanloop Bintulu (schematisch, over water — kade 21,5 km van de MARNET-zeeknoop, LAR-586) |
| 2 | zee | 4.234,4 | 439 | nee | LNG-tanker Bintulu (MLNG-jettycomplex) → Pyeongtaek (Zuid-Chinese Zee → Straat Luzon/Bashi-kanaal → Oost-Chinese Zee → Gele Zee) |
| 3 | zee | 5,4 | 2 | ja (rechte lijn) | haven-aanloop Pyeongtaek (schematisch — 1:10M-kust kent de haven niet) |
| **totaal** | | **4.261,9** | **478** | | 2 markers, 0 naden > 0 m |

**Markers (2, beide reeds bron-gelegd, geen nieuwe satellietpas):**
- `gas-bintulu-kade` — Petronas LNG-complex (Malaysia LNG), Bintulu, Sarawak (3,2822/113,0882) — 0,0 km van de lijn.
- `gas-pyeongtaek-kade` — Pyeongtaek LNG Terminal (KOGAS) (37,00242/126,78434) — 0,0 km van de lijn.

**Toelichting per stippel/aanloop:**
- **b1 (haven-aanloop Bintulu, stippel-geojson):** `maak_havenaanloop.py` is GELUKT — kortste pad over
  water, 22,1 km / 37 punten, omwegfactor 1,027 (tegen de rechte lijn van 21,5 km). De 1,29 km die als
  "over land" resteert grenst aan het kade-uiteinde zelf (een kade ligt op de 1:10M-kustlijn per
  definitie óp land — dat is de korrel van die kustlijn, geen routeerfout); geen landkruising midden op
  de lijn. Reden voor de stippel blijft staan ondanks de betere geometrie: een kortste-pad-over-water is
  géén waargenomen vaargeul (bakhandleiding §2), en de kade ligt > 5 km van de MARNET-zeeknoop (LAR-586).
- **b3 (haven-aanloop Pyeongtaek, rechte stippel):** `maak_havenaanloop.py` liep vast op `timeout 300`
  (exit 124) — géén tweede poging (bakhandleiding §2), terugval op de rechte stippellijn tussen zeeknoop
  5632 (37,01130/126,72450) en de kade (37,00242/126,78434), 5,4 km. Reden: kade net over de 5 km-grens
  van haar zeeknoop (LAR-586).
- **b2 (MARNET, geen stippel):** volledig geroutet over de bestaande MARNET-zeegraaf, 4.234,4 km over
  29 zee-edges — exact de haalbaarheidstoets-uitkomst (4.234,4 km) van vóór de bake, en binnen de
  omschreven bandbreedte-context (§2/§7 van de brief; de meting bevestigt dat 4.234,4 km een reële
  MARNET-uitkomst is, geen wilde route). De router bevestigt zelf de gerapporteerde reisweg (Zuid-
  Chinese Zee → Straat Luzon/Bashi-kanaal → Oost-Chinese Zee → Gele Zee), geen Panama/Suez-omweg.
- **Vluchten/leiding:** niet van toepassing — alle drie benen zijn zee, geen luchtbeen en geen
  leidingbeen in deze keten (§1/§4/§6 van de brief).
- **Gedeelde benen:** geen — nieuwe stroom zonder gedeeld been met een bestaande gas-stroom.

**Toets (bakhandleiding §5):**
- Km per been: b1 22,1 tegen brief-indicatie ≈21,5 (+2,8%, haven-aanloop over water — geen harde norm
  voor een stippel-aanloop); b2 4.234,4 km EXACT gelijk aan de brief-verwachting 4.234,4 km; b3 5,4 km
  EXACT gelijk aan de brief-indicatie ≈5,4 km (5,405).
- Naden tussen opeenvolgende benen: 0,000 km op beide overgangen (geen haven-aanloop-herstel nodig).
- Markers: beide op 0,000 km van de lijn (anker = routeerpunt, kade-coördinaat viel exact op het
  been-uiteinde).
- `toets_knikken.py`: 1 knik ≥60° (65,9°, R≈7.475 m, bij 37,16690/126,41420, vlak vóór de Koreaanse
  kust) — een echte bocht in de MARNET-geometrie, 0 omkeringen, 0 terugloop. Geen bevinding.
- `toets_rechte_benen.py --min-km 5`: been 3 (5,4 km, stippel) verschijnt als "MIDDEL" — verwacht en
  correct, want het IS een niet-onderzochte rechte lijn (de reden staat in de beennaam); been 1 is geen
  rechte lijn (37 punten, geojson) en verschijnt niet in de lijst. Been 2 is doorgetrokken en niet recht
  (omwegfactor 1,02 t.o.v. de grootcirkel) — geen bevinding.
- JSON-contract: `versie: 2`, `punt_formaat: lonlat`, alle modaliteiten `zee` (in de toegestane set),
  elk been ≥ 2 punten, bestand 9,6 KB (ruim onder de ~300 KB-norm).

**Lessen / open punten voor een volgende bake:**
- Een geslaagde `maak_havenaanloop.py`-pas kan een klein stukje "over land" laten staan wanneer het
  precies op het kade-uiteinde ligt — dat is de korrel van de 1:10M-kustlijn zelf, geen fout in de
  aanloop-geometrie, en de bakhandleiding zegt terecht dat de stippel-status dan toch blijft staan
  (geometrie ≠ kennisclaim).
- De twee eerder vooraf gemeten zeeknoop-afstanden (21,479 km / 5,405 km, brief §9-voorbereiding) zijn nu
  bevestigd door de echte bake: b3's rechte stippel (5,4 km) komt er nagenoeg identiek uit, en b1's
  geroutete aanloop (22,1 km) ligt er dicht tegenaan (+0,6 km voor de omweg over water).
- De overige open punten uit §7 van de brief (Maleisië-extract ontbreekt, het 2,0 Mtpa-contractcijfer is
  een deelcontract, b2's km is een routeruitkomst en geen gepubliceerde end-to-end ladingroute-lengte,
  exacte MLNG-jetty niet gepreciseerd) blijven ongewijzigd staan — deze bake voegt er geen nieuwe aan toe
  en lost er geen van op.
