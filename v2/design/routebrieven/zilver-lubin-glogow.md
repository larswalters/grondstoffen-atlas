# Routebrief (licht) · Zilver · Polkowice-Sieroszowice → Głogów (land)

**stroom-id:** `zilver-lubin-glogow` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** koperconcentraat (met het zilver erin) van KGHM's Zakład Wzbogacania Rud "Polkowice" (de
verwerkingsfabriek van de Polkowice-Sieroszowice-mijn, Neder-Silezië) per **spoor** — KGHM's eigen "Główny Ciąg
Technologiczny" — naar de Głogów-kopersmelter, waar het via de Kaldo-oven ook het zilver oplevert: KGHM is
daarmee 's werelds grootste bijproduct-zilverbron van één onderneming — stoppunt bij de Głogów-smelter/
raffinaderij.
**Welke as van het verhaal:** *binnenlandse mijn-tot-smelter-as* — geen zee, geen grens, één bedrijf (KGHM) dat
erts wint, verrijkt en tot metaal (incl. zilver en goud) verwerkt binnen ~25 km in Neder-Silezië.

## 1 · Ketenkaart
```
ZWR "Polkowice" (concentrator, KGHM) `ag-polkowice-concentrator`
   ──(b1 spoor · KGHM's Główny Ciąg Technologiczny · gemeten door de spoorrouter)──►
Głogów-smelter + Precious Metals Plant (KGHM) `ag-glogow-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `ag-polkowice-concentrator` → `ag-glogow-smelter` | KGHM interne aanduiding "Główny Ciąg Technologiczny"; KGHM's eigen corporate site bevestigt expliciet railvervoer concentraat → Głogów-smelter [1] | geen gepubliceerde lengte; hemelsbreed ≈ 23,2 km — de spoorrouter meet de werkelijke afstand | `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` (extract polen, `v2/build-cache/raw1op1/polen.geojson`) | nee — spoornet dekt Neder-Silezië dicht; alleen stippel als de router "geen pad" geeft |

Modaliteit gecorrigeerd t.o.v. het ketenontwerp: de haalbaarheidstoets wees op KGHM's eigen tekst — *"The final
product resulting from the work of the concentration plants is the concentrate that is transported by rail to
the 'Głogów' Smelter and the 'Legnica' Smelter"* [1] — dus geen weg-scan-profiel maar de spoorrouter.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-polkowice-concentrator` | concentrator (kop van het spoor) | Zakład Wzbogacania Rud "Polkowice" (KGHM), ul. Jana Wyżykowskiego, Polkowice | 51.4863, 16.0655 | [2][3] | bron-gelegd (z15 gezien: industrieel complex met verwerkingshallen, silo's en een rangeerspoor direct zuidoostelijk van het terrein; OSM-gebouw "Zakład Wzbogacania Rud 'Polkowice'" 100 m van het punt) |
| `ag-glogow-smelter` | smelter + zilver-/goudraffinaderij (stoppunt) | Huta Miedzi "Głogów" (KGHM), Żukowice, powiat głogowski | 51.6872, 15.9778 | [1][4][5] | bron-gelegd (z14 gezien: groot smeltercomplex met schoorstenen, ertsopslag en tailingsbekken aan de Odra, spoorbundel het terrein op; OSM-object "man_made=works, Huta Miedzi 'Głogów'" 0 m van het punt) |

## 4 · Via-punten
Geen — geen bron of kaart toont een corridorkeuze op dit ~23 km-traject; de spoorrouter legt de werkelijke lijn
tussen kop en staart vast. Blijkt bij het bakken een keuze te bestaan (bijv. via Rudna-emplacement), dan komt
die als via-punt terug in een revisie van deze brief.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| ZWR "Polkowice" (concentrator, bij de Polkowice-Sieroszowice-mijn) | KGHM | ruw erts → koperconcentraat (23 % Cu) | Polkowice-gebied ≈ 9,1 Mt erts/jaar verwerkt [1]; keten-breed (3 concentratorfabrieken) ≈ 33 Mt erts/j → ≈ 2 Mt concentraat/j | [1] |
| Głogów-smelter + Precious Metals Plant (Kaldo-oven) | KGHM | concentraat → koperkathode + ruwlood + H₂SO₄ + zilver/goud-baren | Głogów I+II ≈ 150.000 t elektrolytisch koper/j; 2023: ≈ 1.400 t geraffineerd zilver + ≈ 3 t goud [4]; 2025 KGHM-groep-totaal 1.347 t zilver [5] | [4][5] |

## 6 · Stoppunt
De brief stopt bij de Głogów-smelter: dit ís het eindpunt van de zilverketen bij KGHM (Precious Metals Plant,
Kaldo-oven → zilverbaren) — geen bron noemt een vervolgzending van de baren (bv. naar een LBMA-kluis); fase E
vervalt.

## 7 · Open punten
- **Exacte spoorlijn niet bij naam bekend in Engelstalige bronnen** — "Główny Ciąg Technologiczny" is KGHM's
  interne aanduiding, geen gepubliceerde lijnnaam/-lengte. De spoorrouter (§2) moet de werkelijke tracé op het
  1-op-1-net vinden; of dat via een aparte rangeerknoop bij Rudna loopt is niet gebrond en blijft een aandachtspunt
  bij het bakken.
- **Mijnspecifiek zilveraandeel niet gepubliceerd** — Polkowice-Sieroszowice, Lubin en Rudna leveren samen het
  erts voor Głogów (+ Legnica); welk deel van de ≈1.400 t zilver/jaar specifiek uit Polkowice-Sieroszowice komt
  is niet apart gebrond (bevestigt het risico uit het ketenontwerp).
- **Legnica-smelter (tweede bestemming van hetzelfde concentraatstroom) niet getekend** — de brief volgt alleen
  de Głogów-tak; een deel van het Polkowice-concentraat gaat mogelijk ook naar Legnica, niet gekwantificeerd.
- **Ertsherkomst binnen het Polkowice-gebied** (Polkowice-Sieroszowice-mijn specifiek vs. gemengd met Lubin-erts
  op dezelfde concentrator) niet apart gebrond — de concentrator verwerkt "Polkowice area"-erts als geheel [1].

## 8 · Bronnen
[1] KGHM Polska Miedź, "Ore enrichment" — Concentration Plants-capaciteit per mijngebied (Lubin ≈8 / Polkowice
≈9,1 / Rudna ≈16 Mt erts/j) + expliciete railtransport concentraat → Głogów- en Legnica-smelter.
https://kghm.com/en/our-business/processes/ore-enrichment
[2] OpenStreetMap (ODbL) via Photon — gebouw "Zakład Wzbogacania Rud 'Polkowice'", ul. Jana Wyżykowskiego,
Polkowice Dolne, 51,48627/16,06550. https://www.openstreetmap.org
[3] Esri World Imagery via `v2/tools/sat_check.py` (z15) — `v2/build-cache/satcheck/sat-zilver-lubin-glogow-concentrator.png`.
[4] KGHM Polska Miedź, "Głogów" (smelting & refining) — geschiedenis, capaciteit (Głogów I 80 kt → 160 kt Cu;
Głogów II 150 kt Cu), sulfuric acid, Precious Metals Plant/Kaldo-oven; 2023-productie ≈1.400 t zilver + ≈3 t goud.
https://kghm.com/en/our-business/smelting-and-refining/glogow
[5] KGHM Polska Miedź, "Silver market" — ≈75% van wereldwijde zilverproductie is bijproduct; KGHM Group
2025-productie 1.347 t zilver, geraffineerd bij Głogów als baren/korrels.
https://kghm.com/en/about-us/our-industry/silver-market
[6] OpenStreetMap (ODbL) via Photon — object "Huta Miedzi 'Głogów'" (man_made=works), Żukowice, 51,68717/15,97784.
https://www.openstreetmap.org
[7] Esri World Imagery via `v2/tools/sat_check.py` (z14) — `v2/build-cache/satcheck/sat-zilver-lubin-glogow-smelter.png`.
[8] Wikipedia (Wikimedia API) — Rudna mine (KGHM), 51,50154/16,10731; context voor de drie KGHM-mijnen in
Neder-Silezië (Lubin/Polkowice-Sieroszowice/Rudna) die gezamenlijk de concentratorfabrieken voeden.
https://en.wikipedia.org/wiki/Rudna_mine
[9] Ketenontwerp + haalbaarheidstoets (workflow-invoer, M31 golf 2) — jaarvolume-kader, bronnen_start
(kghm.com smelting-and-refining/glogow, silver-market, csr2022.kghm.com) en de gecorrigeerde modaliteit spoor.
[10] Webzoekopdracht "linia kolejowa Polkowice Głogów KGHM Główny Ciąg Technologiczny" (netTG.pl,
Rynek Kolejowy, Envirail, 28-09-2026) — bevestigt dat het huidige KGHM-treinverkeer Polkowice → Głogów
alleen over de bestaande, omslachtige route via Lubin en Rudna Gwizdanów loopt; een nieuwe rechtstreekse
lijn (Lubin-Polkowice-Głogów, incl. uitbreiding van lijn 289 Legnica-Lubin-Rudna Gwizdanów) is nog in
planfase, niet aangelegd.
[11] Nominatim/OpenStreetMap (ODbL) — station "Rudna Gwizdanów", 51,52910/16,28097; gebruikt om te
bevestigen dat de gebakken spoorlijn de echte omweg via Rudna Gwizdanów volgt (zie §9).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom:** `zilver-lubin-glogow` · **bestand:** `v2/data/stroomroute-zilver-lubin-glogow.json` (3,8 KB) ·
**recept:** `bak_zilver_lubin_glogow()` in `v2/tools/bak_stromen.sh`

**Benen (1, in reisvolgorde):**
| # | modaliteit | km gebakken | km hemelsbreed (brief) | afwijking | stippel? |
|---|---|---|---|---|---|
| b1 | spoor | 61,0 km (175 punten) | 23,1–23,2 km | +163–164% | nee |

**Totaal:** 61,0 km · 175 punten · 2 markers (beide op 0,0 km van de lijn — exacte ankers). Naden: geen (één
been, geen vertakking). `toets_knikken.py`: 2 knikken ≥60°, waarvan 1 "scherpe bocht, echt" (Lubin) en 1
TERUGLOOP (Głogów-nadering) — zie hieronder. `toets_rechte_benen.py --min-km 5`: geen regel voor deze stroom
(been is geen rechte lijn, omwegfactor 2,57 ≠ 1,000). JSON: `versie 2`, `punt_formaat lonlat`, modaliteit
`spoor` ∈ de toegestane set, 175 ≥ 2 punten — laadt schoon.

**Toelichting per stippel/haven-aanloop:** geen — het ene been is volledig doorgetrokken (`--been-geojson`,
geroutet door de spoorrouter op het 1-op-1-net). Geen zeebeen, dus geen haven-aanloop nodig.

**Grootste bevinding — de brief's hemelsbreed-schatting was niet de echte corridor.** De brief noemde
"geen gepubliceerde lengte; hemelsbreed ≈23,2 km" voor KGHM's interne "Główny Ciąg Technologiczny" en
verwachtte een gemeten lijn dicht bij die 23 km. De spoorrouter (1-op-1-OSM-net, `BAKE_SUFFIX=-raw`) vindt
in plaats daarvan een reële route van 59,5–61,0 km (verhouding 2,57–2,6×) via Lubin (172,4°-bocht bij
51,4006/16,1955 ligt vrijwel exact op Lubin-station) en Rudna Gwizdanów (het pad snijdt 51,5291/16,2810,
het Rudna Gwizdanów-spoorstation, Nominatim-gelegd). Dat is GEEN routerfout: een onafhankelijke webbron
(netTG.pl/Rynek Kolejowy/Envirail, bron [10]) bevestigt expliciet dat het huidige KGHM-treinverkeer
Polkowice → Głogów alleen over "de bestaande, tamelijk omslachtige route via Lubin en Rudna Gwizdanów"
loopt, en dat een geplande rechtstreekse nieuwe lijn (Lubin-Polkowice-Głogów) nog niet is aangelegd. De
23,2 km uit de brief was dus de hemelsbrede afstand tussen concentrator en smelter, niet de echte
spoorcorridor — precies het open punt dat de brief zelf al aankondigde ("de spoorrouter moet het
werkelijke tracé vinden, mogelijk via een rangeerknoop bij Rudna", §7). Buiten ±15% en buiten de eigen
130%-alarmgrens van de bak-aanwijzing — **bevinding, niet dichtgetrokken.**

**Tweede bevinding — één kleine, niet-gerepareerde terugloop vlak vóór de smelter.** Met de default
`--keerstraf` (25) koos de vrije Dijkstra een 14 km-omweg voorbij Głogów naar een doodlopende spoorstomp
bij Bytom Odrzański (51,7253/15,8257) en terug over dezelfde punten (`toets_knikken.py`: R≈0 m, v=99 —
een onmiskenbare terugloop, en Bytom Odrzański ligt ver buiten elke KGHM-bron). Getest op
`--keerstraf` 1/2/3/5/10/15/20: allemaal identiek 59,5 km/115 edges; pas bij 25 springt de route naar de
81,6 km-omweg. De bake gebruikt daarom `--keerstraf=5` (ruim onder die drempel, geen coördinaat- of
via-punt-ingreep). Dat elimineert de Bytom Odrzański-omweg, maar laat één kleine terugloop staan vlak vóór
de Głogów-smelter (51,6837/15,9694, R≈24–34 m, `toets_knikken` v=2,2) — op elke geteste keerstraf 1–20
blijft precies dit punt over. Aannemelijke verklaring: de smelter heeft een eigen spoorbundel op het
terrein (brief §1) en het 1-op-1-net dwingt hier een korte kopmaakbeweging af om die site-aansluiting
vanuit de juiste richting te bereiken — niet apart geverifieerd binnen het WEBBUDGET van deze bake. Niet
dichtgetrokken met een verzonnen via-punt of coördinaat; blijft staan als open punt.

**Gereedschapslessen:**
- `--keerstraf` is geen straf-toeval maar kan een echte binaire wissel in de kortste-padkeuze zijn: op dit
  net springt de route pas bij keerstraf ≥25 van 59,5 naar 81,6 km. Bij een verdachte grote omweg (>130%
  van de brief-schatting) loont het om een klein bereik (1–20) te testen vóór je een via-punt verzint.
- Een "TERUGLOOP" (`toets_knikken.py`, R≈0, v hoog) op de KOP/STAART van een been kan wijzen op een reëel
  kopmaakpunt bij het binnenrijden van een site-spoorbundel, niet per se een routerfout — maar een
  terugloop MIDDEN in het traject naar een OSM-stomp zonder enige bronvermelding (hier: Bytom Odrzański)
  is wél een sterk signaal van een vermijdbare omweg.
- Een hemelsbreed-schatting in een lichte brief is een ondergrens voor de omwegfactor-toets, geen
  voorspelling van de echte corridor — een webzoekopdracht op de bedrijfsinterne lijnnaam (hier: "Główny
  Ciąg Technologiczny") kan de echte, gepubliceerde route bevestigen vóórdat je de meting als "buiten de
  norm, dus fout" afdoet.

**Open punten (naar de brief, niet dichtgetrokken):**
- De kleine terugloop vlak vóór de Głogów-smelter (zie boven) is niet onafhankelijk bevestigd als een echt
  site-kopmaakpunt.
- De exacte spoorlijn-naam/-nummers (lijn 971/971a/289 volgens bron [10]) zijn niet één-op-één aan de
  gebakken geometrie gekoppeld — de webbron bevestigt de corridor (via Lubin/Rudna Gwizdanów), niet elk
  wisselpunt.
- De overige open punten uit de brief (§7: mijnspecifiek zilveraandeel, Legnica-smelter, ertsherkomst)
  blijven ongewijzigd — dit bakwerk raakt alleen de geometrie van been b1.
