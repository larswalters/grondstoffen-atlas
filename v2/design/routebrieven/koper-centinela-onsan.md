# Routebrief (licht) · koper — Centinela → Michilla → Onsan-haven (Zuid-Korea)

**stroom-id:** `koper-centinela-onsan` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) · **status:** gebakken
**Titel (bol):** Koper · Centinela (Chili) → Michilla → Onsan-haven (Zuid-Korea) — afnemer LS MnM aannemelijk: één bron
**Keten in één zin:** Cu-concentraat uit de Esperanza-concentrator van Minera Centinela (Sierra Gorda) per **slurryleiding**
(~145 km, eigen verbinding) naar de pier van Michilla, per **bulkschip** de Stille Oceaan over (MARNET ~18.003 km) naar de
Onsan-haven bij Ulsan. **Stoppunt = Onsan-haven**: het terrein van LS MnM is niet gevonden, dus geen kade-naar-smelterbeen.
**Welke as van het verhaal:** *Chileens concentraat naar Korea* — Centinela 2023: 162,7 kt Cu in concentraat + 79,3 kt kathode [1];
2025 totaal 240,4 kt Cu [2]. LS MnM tekende in april 2024 een 10-jarig contract met Centinela [5]. Aandeel Onsan niet gepubliceerd.

## 1 · Ketenkaart
```
Esperanza-concentrator `cu-centinela-laad` ──(b1 leiding · concentraat-slurryleiding, STIPPEL · ~145 km [3], hemelsbreed 125,6)──►
  Michilla-pierkop `cu-michilla-kade` ──(b2 zee · haven-aanloop, STIPPEL · 158,0 km)──► MARNET-zeeknoop 4664 (-23.8000,-71.3000)
  ──(b3 zee · MARNET, Chili-kust → Stille Oceaan → Korea-Straat · 18.003,4 km)──► zeeknoop 5629 bij Onsan (35.4618,129.3908)
  ──(b4 zee · haven-aanloop Onsan, STIPPEL · 5,6 km, KOPIE zilver-greenscreek-onsan b4)──► Onsan-haven `cu-onsan-kade` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | Esperanza-concentrator → Michilla-pierkop | concentraatleiding (slurry) Esperanza-Michilla; de zeewaterleiding Michilla-Centinela ligt op dezelfde lijn [3][4][7] | 145 [3]; hemelsbreed 125,6 (gemeten, -13,4%) | OSM-fragmenten onbruikbaar: ongetagd, 2-18 km, geen substance (way 1360445780 e.a.) | ja, eigen verbinding zonder net — schematisch, geen OSM-tracé |
| b2 | B | zee (haven-aanloop) | Michilla-pierkop → zeeknoop 4664 | schematisch over water; pier ligt 158,0 km van de dichtstbijzijnde zeeknoop (> 5 km) | 158,0 (rechte lijn, gemeten) | maak_havenaanloop.py liep vast op timeout 300 s in de haalbaarheidstoets: rechte stippel, geen tweede poging; NE-landtoets 0,0 km land | ja, net reikt niet |
| b3 | B | zee | zeeknoop 4664 → zeeknoop 5629 (Onsan) | Chili-kust, Stille Oceaan, Korea-Straat; "aannemelijk: één bron" staat in de beennaam | 18.003,4 (MARNET-droogloop 2026-10-29; edge-som 18.003,8); hemelsbreed kade-kade ~17.650 | MARNET | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop 5629 → Onsan-haven | LETTERLIJKE KOPIE van b4 uit `bak_zilver_greenscreek_onsan` (= penasquito b4) | 5,6 [8][9] | stippel-kopie | ja, net reikt niet (> 5 km) |

Vervallen t.o.v. het ontwerp (bindende toets): been C kade → LS MnM-smelter 0,9 km; het smelterpunt 35.4234,129.3525 is volgens de toets de Korea Zinc Onsan power station.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-centinela-laad` | concentrator (laadplek leiding) | Planta Concentradora Esperanza, Minera Centinela | -22.9998, -69.1031 | [1][4] + OSM landuse | bron-gelegd (z15 gezien: concentratorblok met indikkers en twee tailings-/waterbekkens op het kruis, open pit 2 km oostelijk, woonkamp zuidwestelijk; `sat-koper-centinela-onsan-laad.png`) |
| `cu-michilla-kade` | overslag leiding → zee (pierkop) | Esperanza-pier, Caleta Michilla | -22.7227, -70.2918 | [3][4] + OSM works | bron-gelegd (z15 gezien: smalle pier loopt vanaf het fabrieksterrein aan de kust NW de zee in, het kruis ligt op de pierkop; `sat-koper-centinela-onsan-kade.png`) |
| `cu-onsan-kade` | losplek (haven) | Onsan-haven bij Ulsan | 35.4180, 129.3600 | hergebruik letterlijk uit `zilver-penasquito-onsan` / `zilver-greenscreek-onsan` [8][9] | aannemelijk (daar z16: stacking yard aan kademuur; ligt bij Korea Zinc 4e fabriek 35.4191,129.3613, niet aantoonbaar bij LS MnM) |

Zeeknopen (geen ankers): Michilla-kust 4664 = -23.8000, -71.3000; Onsan 5629 = 35.4618, 129.3908.

## 4 · Via-punten
Geen: geen landbeen over het net. De leiding is een stippel tussen twee ankers; zee loopt via de MARNET-router.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Esperanza-concentrator | Minera Centinela (Antofagasta plc 70%, Marubeni 30%) | erts → Cu-/Mo-concentraat met goud | 2023: 162,7 kt Cu in concentraat; 2025 totaal 240,4 kt Cu | [1][2] |
| Onsan-smelter (LS MnM) | LS MnM | concentraat → kathode, zwavelzuur | 680 kt geraffineerd Cu/j (terrein niet bewezen in OSM) | [6] + sitelaag `w-onsan` |

## 6 · Stoppunt
Stop bij de Onsan-haven: het contract noemt de afnemer (LS MnM) maar geen locatie; het smelterterrein is niet gevonden en het sitelaagpunt ligt bij Korea Zinc, dus geen kade-naar-smelterbeen (geen fase D/E).

## 7 · Open punten
- **Afnemer = één Koreaanse persbron** [5]: "1 Mt concentraat per jaar" past niet bij 163 kt Cu in concentraat (~0,6 Mt concentraat) [1]; hooguit door groei (tweede concentrator [2]). Beennaam draagt "aannemelijk: één bron". Het JoongAng-artikel (okt 2026) noemt Centinela niet [6].
- **LS MnM-terrein onbekend**: OSM kent geen LS MnM-object; het sitelaagpunt `w-onsan` (35.4234,129.3525) is de Korea Zinc power station. Sitelaag centraal corrigeren; de Onsan-kade deelt dit voorbehoud.
- **Leiding volledig stippel**: de 145 km komt uit een bron van 2008 [3] (e-mj.com gaf 403, niet gelezen); OSM-fragmenten zijn ongetagd en niet als concentraatleiding te bewijzen. De zeewaterleiding Michilla-Centinela (144 km, SIAM I/II) ligt op dezelfde lijn [4][7] maar is een ander product.
- **Michilla-zeeknoop 158 km uit de kust** (MARNET kent het kustwater hier niet): aanloop is een rechte stippel; maak_havenaanloop time-out, geen tweede poging.
- **Sitelaag mist Centinela en Michilla** (koper-sitelaag.json): centraal toevoegen met de ankers hierboven.
- Aandeel Onsan niet gepubliceerd; kathode (79,3 kt Cu, 2023) gaat niet via deze route.

## 8 · Bronnen
[1] Wikipedia, Centinela mine: Antofagasta 70% / Marubeni 30%; 2023: 162.700 t Cu in concentraat, 79.300 t kathode, 165.800 oz goud. https://en.wikipedia.org/wiki/Centinela_mine
[2] Antofagasta plc, Centinela: 2025 Cu 240,4 kt (+7%), 2026 195-215 kt; tweede concentrator als project. https://www.antofagasta.co.uk/our-business/mining-division/centinela/
[3] Industrial Info, 9 juli 2008: 145 km slurryleiding van Esperanza naar Michilla, waar haven en voorzieningen komen; zeewater via aparte leiding ernaast. https://www.industrialinfo.com/news/article/antofagasta-minerals-to-select-construction-firm-by-august-for-copper-and-gold-project-in-chile--135202
[4] Business Excellence, Minera Esperanza: zeewaterleiding 145 km volgt dezelfde lijn als de concentraatleiding; pompstation bij de Esperanza Pier in Caleta Michilla. https://www.bus-ex.com/article/minera-esperanza
[5] Daum (Koreaanse pers), 18 juni 2024: LS MnM en Centinela, 10 jaar, 1 Mt concentraat per jaar, april 2024; geen locatie. https://v.daum.net/v/20240618091200778
[6] Korea JoongAng Daily, okt 2026: Onsan-smelter 680 kt geraffineerd Cu/j, LS MnM weegt kortere concentraatinkoop; noemt Centinela niet. https://www.koreajoongangdaily.com/business/ls-mnm-weighs-copper-concentrate-cuts-as-shortages-squeeze-smelter-profits/12928685
[7] MCH.cl, Aguas Esperanza (Almar/Transelec): zeewaterleiding Michilla-Centinela 144 km, SIAM II in dienst april 2026. https://www.mch.cl/aguas-esperanza-comienza-a-entregar-agua-a-distrito-minero-centinela-a-traves-de-siam-ii/
[8] Brief `zilver-penasquito-onsan.md` (+ `bak_zilver_penasquito_onsan`): Onsan-ankers, zeeknoop 5629, b4 5,6 km.
[9] Brief `zilver-greenscreek-onsan.md` (+ `bak_zilver_greenscreek_onsan`): letterlijke kopie b4.
[10] Esri World Imagery via `sat_check.py` (z15): `v2/build-cache/satcheck/sat-koper-centinela-onsan-laad.png`, `-kade.png`; hecht_marnet droogloop 2026-10-29 (b3 18.003,4 km, b2 158,0 km, NE-landtoets b2 0,0 km land).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
**Bestand:** `v2/data/stroomroute-koper-centinela-onsan.json` (36,3 KB) · functie `bak_koper_centinela_onsan` in `v2/tools/bak_stromen.sh` · geen profiel in `maak_stroombeen_weg.py` (geen weg of spoor) · geen tussenbestanden.
**Recept:** `bash v2/tools/bak_stromen.sh koper-centinela-onsan` (een run, zwaar-slot). Vier benen, drie markers, 18.292,6 km, 1.850 punten, versie 2, lonlat.

| # | modaliteit | km | punten | stijl | naad naar vorige |
|---|---|---|---|---|---|
| b1 | leiding | 125,6 | 2 | stippel (eigen verbinding zonder net) | 0 |
| b2 | zee (haven-aanloop Michilla) | 158,0 | 2 | stippel (net reikt niet) | 0,00 |
| b3 | zee (MARNET 4664 → 5629) | 18.003,4 | 1.844 | doorgetrokken | 0,00 |
| b4 | zee (haven-aanloop Onsan) | 5,6 | 2 | stippel, letterlijke kopie uit `bak_zilver_greenscreek_onsan` | 0,00 |

**Markers:** Esperanza-concentrator (-22,9998, -69,1031), Esperanza-pier Michilla (-22,7227, -70,2918), Onsan-haven (35,4180, 129,3600); alle drie 0,0 km van hun lijn.
**Toets:** km conform brief (b3 18.003,4 tegen MARNET-droogloop 18.003,4; b1 125,6 hemelsbreed tegen 145 gepubliceerd = -13,4%, binnen 15% maar het is geen wegkm, dus alleen indicatie). Geen naad > 5 km. `toets_knikken`: 0 knikken, 0 omkeringen. `toets_rechte_benen`: b1, b2 en b4 omwegfactor 1,000, alle drie bewust stippel met reden.

**Toelichting per stippel:**
- **b1 leiding:** volledig schematisch. Gepubliceerd 145 km (2008-bron), hemelsbreed 125,6 km; OSM-fragmenten zijn ongetagd en zonder substance, dus niet als concentraatleiding te bewijzen. De zeewaterleiding Michilla-Centinela ligt op dezelfde lijn maar is een ander product.
- **b2 aanloop Michilla:** pierkop 158,0 km van de dichtstbijzijnde zeeknoop 4664; `maak_havenaanloop.py` liep vast op timeout 300 s, rechte stippel, geen tweede poging; NE-landtoets 0,0 km land.
- **b4 aanloop Onsan:** letterlijke kopie van de regel in `bak_zilver_greenscreek_onsan` (kade 5,6 km van zeeknoop 5629).

**Lessen:**
- Een keten zonder wegbeen heeft geen profiel of scan nodig: een functie met drie stippels en een MARNET-been is genoeg.
- Het stroom-id noemt Onsan en de lijn eindigt in de Onsan-haven; geen afwijking tussen id en eindpunt.
- De sitelaag mist Centinela en Michilla en `w-onsan` ligt bij Korea Zinc: centraal corrigeren (zie §7).
- Tijdens de bake bewerkte een andere agent `bak_stromen.sh`; bash meldde een syntaxfout achter het gebakken resultaat (bestand verschoof tijdens het lezen), `bash -n` daarna schoon en LF-teller 0.
