# Routebrief (licht) · zilver — Greens Creek → Hawk Inlet → Onsan (Zuid-Korea)

**stroom-id:** `zilver-greenscreek-onsan` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** Zn/Pb-concentraat met zilver van Hecla's Greens Creek (Admiralty Island, Alaska) per **truck** over de
privé-haulroad (~14,5 km) naar de Hawk Inlet-terminal, per **bulkschip** de Noord-Pacific over (MARNET ~7.800 km, hemelsbreed
~7.050 km) naar de Onsan-kade bij Ulsan en over eigen terrein naar de Korea Zinc-smelter — **stoppunt** (smelter = bestemming).
**Welke as van het verhaal:** *Alaska-concentraat naar Zuid-Korea* — Greens Creek 8,725 Moz Ag = ~271 t Ag/j (Hecla 10-K FY2025 [1]);
Korea Zinc was sinds 2018 de grootste concentraatklant met 39,3% [2]; Korea-omzet van Hecla 611 van 1.414 mln USD in 2025 [1].
Aandeel Onsan/tonnage per jaar niet gepubliceerd; deel van het zilver gaat als doré naar anderen.

## 1 · Ketenkaart
```
Greens Creek-molen `ag-greenscreek-molen` ──(b1 truck · Greens Creek-haulroad, OSM tertiary · ~14,5 km)──► Hawk Inlet-terminal `ag-hawkinlet-kade`
  ──(b2 zee · haven-aanloop Hawk Inlet, stippel · ~12 km)──► zeeknoop 2974 (58.0857,-134.9142)
  ──(b3 zee · MARNET Icy Strait/Golf van Alaska/Noord-Pacific · ~7.820 km)──► zeeknoop 5629 bij Onsan (35.4618,129.3908)
  ──(b4 zee · haven-aanloop Onsan, stippel · 5,6 km, KOPIE penasquito b4)──► Onsan-kade `ag-onsan-kade`
  ──(b5 truck · eigen terrein, stippel · 0,9 km, KOPIE penasquito b5)──► Korea Zinc Onsan-smelter `ag-onsan-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | molen → Hawk Inlet-kade | Greens Creek-haulroad (OSM `highway=tertiary`, way 1096871176 + 1096871177, privé) | **14,5** (10-K: terminal "about nine miles" van de molen) [1]; TRS 8,5 mi weg molen–kamp Hawk Inlet [2]; OSM-ways 10,3 + 4,1 = 14,4 | maak_stroombeen_weg (`us-alaska`, `corridorKlassen: tertiary`) | nee |
| b2 | B | zee (haven-aanloop) | Hawk Inlet-kade → zeeknoop 2974 | schematisch over water; kade ligt 10,4 km van de zeeknoop (> 5 km-regel) | ~12,0 (maak_havenaanloop, 213 s bij haalbaarheidstoets; limiet 300 s) | maak_havenaanloop.py; terugval rechte stippel | ja — net reikt niet |
| b3 | B | zee | zeeknoop 2974 → zeeknoop 5629 (Onsan) | Icy Strait, Golf van Alaska, Aleoeten, Noord-Pacific, Korea-Straat | MARNET 7.820,3 (hemelsbreed kade–kade 7.048; "aannemelijk: één bron" voor Onsan — in de beennaam) | MARNET | nee |
| b4 | B | zee (haven-aanloop) | zeeknoop 5629 → Onsan-kade | LETTERLIJKE KOPIE van `bak_zilver_penasquito_onsan` b4 | 5,6 (gemeten in die stroom) | stippel-kopie | ja — net reikt niet (> 5 km) |
| b5 | C | truck | Onsan-kade → Korea Zinc-smelter | LETTERLIJKE KOPIE van penasquito b5, eigen terrein | 0,9 (hemelsbreed) | stippel-kopie | ja — eigen terrein / geen net op deze korrel |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-greenscreek-molen` | mijn + molen (laad) | Greens Creek-molencomplex (920-area), Hecla | 58.0826, -134.6391 | [1][2][5] | bron-gelegd (z16 gezien: molengebouwen met groot dak + procesinstallaties langs de bergweg, droge-tailingspad 0,5 km WSW; OSM service-way-punt 58.0813,-134.6458 ligt op dat pad = routeerpunt-alternatief) |
| `ag-hawkinlet-kade` | overslag (terminal) | Hawk Inlet Dock / marine terminal, Hecla | 58.1261, -134.7550 | [1][3][5] | bron-gelegd (z15 gezien: bulker aan een pier, grote loods + opslagyard; het punt ligt op de yard, de pier ~0,2 km westelijker) |
| `ag-onsan-kade` | losplek (haven) | Onsan-havenkade nabij Korea Zinc, Ulsan | 35.4180, 129.3600 | hergebruik letterlijk uit `zilver-penasquito-onsan` [4] | bron-gelegd (daar z16) |
| `ag-onsan-smelter` | smelter (stoppunt) | Korea Zinc Onsan-smelter | 35.4234, 129.3525 | hergebruik letterlijk uit `zilver-penasquito-onsan` [4] | bron-gelegd (daar z14) |
Zeeknopen (geen ankers): Hawk Inlet 58.0857, -134.9142 (id 2974, MARNET-zeeknoop 10,4 km van de kade); Onsan 35.4618, 129.3908 (id 5629).

## 4 · Via-punten
Geen. De haulroad is de enige weg op het eiland tussen molen en terminal: geen corridorkeuze (haalbaarheidstoets: "geen via-punten nodig").
Fallback voor de bak-agent: valt de weg-scan weg, zet dan één stippel ("eigen verbinding zonder net, privé-haulroad") molen → kade.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Greens Creek-molen | Hecla Greens Creek Mining | erts → Zn-, Pb-concentraat + doré/gravity-concentraat | 8,725 Moz Ag in 2025 (~271 t) | [1] |
| Korea Zinc Onsan-smelter | Korea Zinc | Zn/Pb-concentraat → raffinaat + teruggewonnen zilver | grootste base-metaalcomplex ter wereld (zie penasquito-brief) | [2][4] |

## 6 · Stoppunt
Stop bij de Korea Zinc Onsan-smelter: het ontwerp noemt geen vervolgstap en zilver wordt daar als bijproduct teruggewonnen; geen fase D/E.

## 7 · Open punten
- **Onsan-aandeel rust op één bron** (TRS 2021: Korea Zinc 39,3% sinds 2018 [2]); 10-K FY2025 noemt klanten alleen Customer A–K. Korea-omzet 611 mln USD (2025) tegen 181 (2024) is consistent met een groeiend Koreaans aandeel [1]. Concentraat gaat ook naar Teck, Mitsui, Cliveden; doré apart. Beennaam: "(aannemelijk: één bron)". Tonnage naar Onsan onbekend.
- **Geen bron noemt een specifieke Hawk Inlet → Onsan-zending** (zoekopdracht gaf alleen losse delen [6]); route is as-niveau.
- Hawk Inlet-pier ligt ~0,2 km westelijk van het ankerpunt (yard); op site-niveau aanvaard.
- Molen-anker wijkt 0,42 km af van het OSM-punt uit de haalbaarheidstoets (op het tailingspad); de weg-scan moet de haulroad tot de molengebouwen volgen (trimStaart, vensterKm ~15); anders routeerpunt 58.0813,-134.6458.
- Sitelaag `w-greens-creek` (58.07, -134.63) is v1-centroïde; centraal gelijktrekken met `ag-greenscreek-molen`.
- Weg 14,5 km is 10-K "nine miles"; TRS noemt 8 mi (10 km, mijn → Hawk Inlet) en 8,5 mi (weg tussen de kampen): ±15%-toets tegen 14,5.

## 8 · Bronnen
[1] Hecla Mining, Form 10-K FY2025 — 8.725 koz Ag Greens Creek 2025; "Hawk Inlet marine terminal about nine miles from the mill"; Korea-omzet 611/181 mln USD; Customer A–K. https://www.sec.gov/Archives/edgar/data/719413/000119312526055059/hl-20251231.htm
[2] SLR/Hecla, Technical Report Summary Greens Creek (feb 2022), §16.2.1 — Korea Zinc 39,3%, Cliveden 13,6%, Mitsui 11,8%, Teck 14,7% sinds 2018; §1.3.9 storage-loadout Hawk Inlet. https://www.sec.gov/Archives/edgar/data/719413/000143774922004164/ex_338347.htm
[3] Wikipedia, Greens Creek mine — terminal 8 mi/13 km, concentraat wereldwijd. https://en.wikipedia.org/wiki/Greens_Creek_mine
[4] Brief `zilver-penasquito-onsan.md` (+ functie `bak_zilver_penasquito_onsan`) — Onsan-ankers, b4/b5, zeeknoop 5629.
[5] OpenStreetMap/Nominatim (Hawk Inlet, node 150919736, 58.1258,-134.7531; haulroad-ways 1096871176/1096871177) en Esri World Imagery via `sat_check.py`: `v2/build-cache/satcheck/sat-zilver-greenscreek-onsan-molen.png`, `-molen-z16.png`, `-hawkinlet-kade.png`.
[6] Zoeksessie 2026-10-09 (Admiralty mining district, Wikipedia; Korea Zinc, Wikipedia) — geen zendingsbewijs Hawk Inlet → Onsan.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
`v2/data/stroomroute-zilver-greenscreek-onsan.json` · 23,3 KB · contract versie 2 · totaal 7.852,0 km · 1.118 punten · 4 markers · naden 0,00 km.

| # | modaliteit | km | geometrie | stippel |
|---|---|---|---|---|
| b1 | truck | 13,2 (brief 14,5; -9,3%, binnen ±15%) | haulroad, OSM tertiary, wegscan_puur us-alaska, 283 punten | nee |
| b2 | zee | 12,0 | haven-aanloop Hawk Inlet, maak_havenaanloop geslaagd (cel 0,01 kaal, 0,00 km over land) | ja, net reikt niet |
| b3 | zee | 7.820,3 (MARNET, brief 7.820,3) | zeeknoop 2974 naar 5629, 814 punten | nee |
| b4 | zee | 5,6 | letterlijke kopie stippel b4 van `bak_zilver_penasquito_onsan` | ja, net reikt niet |
| b5 | truck | 0,9 | letterlijke kopie stippel b5 van penasquito, eigen terrein | ja, eigen terrein |

**Recept:** profiel `zilver-greenscreek-onsan-molen-hawkinlet` in `maak_stroombeen_weg.py` (via alleen de twee ankers, vensterKm 15, corridorKlassen tertiary, trimStaart); scan met `python v2/tools/wegscan_puur.py --profiel zilver-greenscreek-onsan-molen-hawkinlet` (11 s, 13 ways in het venster); aanloop met `timeout 300 python v2/tools/maak_havenaanloop.py` (zie hieronder); functie `bak_zilver_greenscreek_onsan` in `bak_stromen.sh`, `bash v2/tools/bak_stromen.sh zilver-greenscreek-onsan`.

**Toelichting.**
- b1: de scan volgde de haulroad van molen tot kade zonder stub aan de molenkant (snaps 0,03 en 0,01 km), dus het routeerpunt-alternatief was niet nodig. 13,2 km tegen de 10-K-opgave van "about nine miles" (14,5 km): -9,3%; de OSM-ways zelf geven 10,3 + 4,1 = 14,4 km, het verschil zit in de ankerprojectie (trimStaart knipte 0,05 km). Toets_knikken meldt één spike van 120 graden (R 3 m) bij 58.1273,-134.7518, vlak vóór het kade-anker: de weg draait het yard in; geen terugloop.
- b2: eerste trappen gaven geen pad of 1,44 km over land; de gekozen trap (cel 0,01 graden, kaal) levert 12,0 km (omwegfactor 1,160) zonder landkruising. Eindigt exact op zeeknoop 2974. Stippel omdat het net hier niet reikt (kade 10,4 km van de zeeknoop).
- b3: aannemelijk (één bron voor Onsan als bestemming, TRS 2021) staat in de beennaam; doorgetrokken. Toets_knikken: drie bochten (krapste 107,7 graden, R 5,1 km bij 54.06,-164.26 in de Aleoeten) zijn echte doorvaarten, geen fout.
- b4/b5: letterlijke kopie van de twee stippel-regels uit penasquito (5,613 en 0,907 km); toets_rechte_benen meldt alleen b4 (omwegfactor 0,998) als stippel met reden.

**Lessen.** (1) De haven-aanloop van Hawk Inlet had ~3,5 min nodig (limiet 300 s, klaar in tijd); de brief gaf 213 s. (2) Weg-slots waren de hele tijd bezet; de aanloop (geen slot) kon al parallel lopen. (3) Open punten uit §7 blijven staan: sitelaag `w-greens-creek` centraal gelijktrekken, Onsan-aandeel één bron, Hawk Inlet-pier 0,2 km westelijker dan het anker.
