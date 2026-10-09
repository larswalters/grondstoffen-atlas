# Routebrief (licht) · Grafiet · Molo (Madagaskar) → Toliara → Khalifa Port (VAE)

**stroom-id:** `grafiet-molo-abudhabi` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** SuperFlake-vlokconcentraat van de NextSource Molo-mijn (Zuid-Madagaskar) gaat per **truck** over RN10/RN7 naar de
Toliara-kade, per **zeeschip** (haven-aanloop + MARNET, Indische Oceaan, Arabische Zee, Hormuz) naar de Golf en via een tweede aanloop naar
de containerterminal van Khalifa Port bij Abu Dhabi, voor de nog te bouwen NextSource-anodefabriek in ICAD (aannemelijk: één bron voor de
bestemming, haven niet in een bron genoemd).
**Welke as van het verhaal:** Madagaskar-vlok naar een Golf-anodefabriek voor Mitsubishi Chemical. Volume: 0 kt vandaag (fabriek niet gebouwd);
kader: offtake ca. 9 kt AAM/j, fabriek 30 kt AAM/j (fase 1 14 kt/j) [1][2], Molo nameplate 17 kt/j, feitelijk ca. 11 kt/j (2025) [8].
Peiljaar plan 2025/26; eenheid kt grafiet per jaar.

## 1 · Ketenkaart
```
Molo-mijn `gr-molo-mijn` ──(b1 truck · RN10/RN7, LETTERLIJKE KOPIE grafiet-molo-duisburg · 378,5 km gebakken)──► Toliara-kade `gr-toliara-kade`
  ──(b2 zee · haven-aanloop Toliara, STIPPEL, KOPIE · 111,2 km)──► zeeknoop 5303 (-22.8572, 42.7368)
  ──(b3 zee · MARNET, Mozambiquekanaal → Indische Oceaan → Arabische Zee → Hormuz · router kiest, 5.414 km hemelsbreed)──►
  zeeknoop 8065 (24.5196, 54.3123)
  ──(b4 zee · haven-aanloop Khalifa, STIPPEL · 46,8 km hemelsbreed)──► Khalifa Port-containerkade `gr-khalifa-kade` ⏹ stoppunt
  (ICAD-fabriek ligt ± 50 km landinwaarts bij Mussafah, niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-molo-mijn` → `gr-toliara-kade` | Fotadrevo → Ampanihy → RN10 → Betioky Atsimo → Andranovory → RN7 (kopie `grafiet-molo-duisburg` b1) | hemelsbreed 164 km, geen wegkm; gebakken 378,5 | kopie `$BEEN/grafiet-molo-duisburg-weg-molo-toliara.geojson` (`--been-geojson`) | nee |
| b2 | A/B | zee | `gr-toliara-kade` → zeeknoop 5303 | haven-aanloop Toliara (kopie van b2 `grafiet-molo-duisburg`) | 111,2 | `--stippel` recht, zoals `bak_grafiet_molo_duisburg` | ja: 1:10M-kust kent de haven niet |
| b3 | B | zee | zeeknoop 5303 → zeeknoop 8065 | MARNET kiest (Hormuz) | 6.549,8 (haalbaarheidstoets), nog te bakken | `--been "zee|…|-22.8572,42.7368|24.5196,54.3123"` | nee |
| b4 | B | zee | zeeknoop 8065 → `gr-khalifa-kade` | haven-aanloop Khalifa (kade 46,8 km van de knoop, > 25 km: router snapt niet) | 46,8 hemelsbreed; 48,3 over water (getest) | `--stippel-geojson` met `$BEEN/grafiet-molo-abudhabi-aanloop-khalifa.geojson` (al gebakken) | ja: aanloop |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-molo-mijn` | mijn (kop) | NextSource Molo-mijn, Fotadrevo/Ampanihy — hergebruikt uit `grafiet-molo-duisburg` en sitelaag `w-nextsource-molo` | -24.0045, 45.1244 | [3][9] | bron-gelegd (letterlijk hergebruikt: z14 kruis op kleine gebouwen in droog savannegebied) |
| `gr-toliara-kade` | overslag (zeekade) | Port de Tuléar, Toliara — hergebruikt uit `grafiet-molo-duisburg` | -23.3778, 43.6648 | [3][9] | bron-gelegd (letterlijk hergebruikt: smalle pier met T-steiger, kade bevestigd, geen kranen) |
| `gr-khalifa-kade` | overslag/losplek (containerkade) | Khalifa Port, container terminal (OSM-operator Abu Dhabi Terminals), zuidoostkade | 24.8077, 54.6499 | [4][5][6] | aannemelijk (z16 gezien: kranenrij en stapels op de kade, een MSC-containerschip langszij; kade en terminal bevestigd, dat deze lading hier aankomt staat in geen bron) |

Zeeknopen (MARNET, gemeten met `marnet_zee`): 5303 op 111,2 km van Toliara (hergebruikt); 8065 op 46,8 km van `gr-khalifa-kade`.
Beeld: `v2/build-cache/satcheck/sat-grafiet-molo-abudhabi-khalifa-kade.png`, `-khalifa.png`, `-khalifa-z16.png`.

## 4 · Via-punten (alleen b1, kopie; de bak gebruikt het bestaande profiel, geen nieuwe punten)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ampanihy (RN10-aansluiting) | -24.6927, 44.7464 | regionale weg van de mijn komt hier op de RN10 |
| b1 | 2 | Betioky Atsimo (RN10) | -23.6897, 44.4212 | doorgaande RN10, geen zijtak |
| b1 | 3 | Andranovory (RN10 → RN7) | -23.5420, 44.8053 | enige corridorkeuze naar de kade |
b2 t/m b4 hebben geen via-punten (zee/aanloop).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Molo-mijn (vlotatie) | NextSource Materials | erts → SuperFlake-vlokconcentraat | nameplate 17 kt/j; feitelijk ca. 11 kt/j, voorraad opgebouwd tot ver in 2028 | [2][8] |
| Battery Anode Facility, ICAD Abu Dhabi (niet gebouwd) | NextSource Materials | vlok (+ Syrah-fines) → gecoat sferisch gezuiverd grafiet (AAM) | 30 kt/j, fase 1 14 kt/j, start gepland Q4 2026, vol begin 2028 | [1][2][7] |

## 6 · Stoppunt
De lijn stopt bij de containerkade van Khalifa Port: de fabriek ligt in een bestaande hal in ICAD (Mussafah) zonder perceelnummer, dus een fase-D-anker
zou een verzonnen coördinaat zijn; Khalifa is de aangewezen containerhaven van Abu Dhabi [4], maar geen bron noemt hem voor deze lading. Fase D vervalt, E vervalt.

## 7 · Open punten
- **Haven niet gebrond:** geen bron noemt Khalifa Port of Mussafah; Khalifa is een aanname op grond van [4] (alle containerverkeer van Abu Dhabi). Alternatief Mussafah Port (24.3860, 54.5075, OSM-locality), 24,7 km van zeeknoop 8065, kleinere haven.
- **Hormuz (hoog):** de Straat is sinds 28 feb 2026 grotendeels geblokkeerd, met wisselende wapenstilstanden en heropeningen tot minstens juli 2026 [10]; de lijn is de structurele route, geen waarneming. Gevolg voor de levering aan de fabriek niet onderzocht.
- **Volume nul:** fabriek niet gebouwd; FID fase 1 (mei 2026) is voorwaardelijk, alleen pre-EPC, geen bouwstart [7]. Molo ligt in "campaign production"; de voorraad dekt Mitsubishi tot 2028 [2].
- **Mitsubishi-AAM** gaat volgens het ontwerp naar Noord-Amerika, niet Japan; niet getekend. Syrah-fines uit Balama [2] zijn een tweede voeding en niet getekend.
- **Weg-km:** b1 is een kopie met 378,5 km gebakken tegen hemelsbreed 164 km, geen wegkm; de ±15%-toets geldt niet als norm.
- **Aanloop Khalifa** is al gerekend (48,3 km, 35 punten, 0 km over land, omwegfactor 1,03, cel 0,01° gebufferd, ca. 4 min); herberekenen is niet nodig.
- Satellietblik van de kade is één opname; welke terminal (AD Terminals, CSP, MSC) de lading afhandelt is niet bepaald.

## 8 · Bronnen
[1] NextSource Materials, TEA battery anode facility UAE, okt 2025 (30 kt/j, fase 1 14 kt/j, Mitsubishi 9 kt/j, ICAD, start Q4 2026). https://investingnews.com/nextsource-materials-announces-positive-results-of-technical-economic-study-for-proposed-battery-anode-facility-in-the-uae-and-secures-industrial-site-with-building-in-abu-dhabi/
[2] NextSource / Syrah, 2 mrt 2026 (Syrah-fines 34-68 kt; Molo primary and preferred; voorraad Molo tot 2028). https://www.investingnews.com/nextsource-materials-signs-agreement-for-the-supply-of-graphite-fines-as-additional-source-of-feedstock-for-its-battery-anode-facility-in-abu-dhabi/
[3] Routebrief `grafiet-molo-duisburg` (2026-09-28): ankers Molo-mijn en Toliara-kade, b1/b2, bronnen [1]-[7] daarin. v2/design/routebrieven/grafiet-molo-duisburg.md
[4] Wikipedia, "Khalifa Port" — handelt al het containerverkeer van Abu Dhabi, Zayed Port overgedragen 2012; 24.8333, 54.6667. https://en.wikipedia.org/wiki/Khalifa_Port
[5] OpenStreetMap (ODbL), way 243045263 "Khalifa Port Container Terminal" (cargo=container, operator Abu Dhabi Terminals; bbox 24.802-24.817 / 54.639-54.658) en way 1303931592 "Khalifa Port". https://www.openstreetmap.org/way/243045263
[6] Esri World Imagery via `v2/tools/sat_check.py` — bestanden `sat-grafiet-molo-abudhabi-khalifa*.png`.
[7] African Mining Market, "NextSource advances with final investment in Abu Dhabi anode facility", 12 mei 2026 (FID fase 1, pre-EPC, voorwaardelijk). https://africanminingmarket.com/nextsource-advances-with-final-investment-in-abu-dhabi-anode-facility/
[8] Zie `grafiet-molo-duisburg` [3]: campaign production, ca. 11 kt/j (NextSource Q3-update 2025). https://www.accessnewswire.com/newsroom/en/metals-and-mining/nextsource-materials-provides-quarterly-update-and-announces-progress-on-molo-min-1028248
[9] v2/design/grafiet-sitelaag.json — `w-nextsource-molo`.
[10] Wikipedia, "2026 Strait of Hormuz crisis" (sluiting vanaf 28 feb 2026, wapenstilstanden, heropeningen). https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis
[11] Club of Mozambique, Syrah levert graphite uit Balama aan de Abu Dhabi-fabriek en daarna aan een Japanse klant. https://clubofmozambique.com/news/mozambique-syrah-resources-to-supply-graphite-to-japan-aim-report/
[12] Wikipedia, "Mussafah" (industriegebied ten zuidwesten van Abu Dhabi, haven). https://en.wikipedia.org/wiki/Mussafah

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)

**Stroom `grafiet-molo-abudhabi`** → `v2/data/stroomroute-grafiet-molo-abudhabi.json` — 4 benen, **7.087,8 km**,
3 markers: truck 378,5 km · zee 111,2 (stippel) + 6.549,8 + 48,3 (stippel) km. Bestand 105,7 KB, 5.250 punten.
Recept: `bak_stromen.sh` (functie `bak_grafiet_molo_abudhabi`); geen nieuw wegprofiel en geen extract nodig (b1 is een kopie).

Toelichting per leg:
- **b1 (truck, doorgetrokken):** LETTERLIJKE KOPIE van `grafiet-molo-duisburg-weg-molo-toliara.geojson` via `--been-geojson`
  (4.542 punten, 378,5 km, naam noemt de kopie). Hemelsbreed 164 km, geen wegkm: de ±15%-toets is hier indicatie, geen norm.
- **b2 (zee, stippel, haven-aanloop Toliara):** kopie van b2 in `bak_grafiet_molo_duisburg`: rechte stippel kade -> zeeknoop 5303,
  111,2 km (1:10M-kust kent de haven niet; `maak_havenaanloop.py` liep daar op de time-out, geen tweede poging).
- **b3 (zee, MARNET, doorgetrokken):** zeeknoop 5303 -> 8065, snap 0,000 km aan beide kanten, **6.549,8 km** (671 punten); de brief
  noemde 6.549,8 uit de haalbaarheidstoets: identiek. Route via de Indische Oceaan en de Straat van Hormuz (Arabische Zee, Golf van Oman).
- **b4 (zee, stippel, haven-aanloop Khalifa):** `--stippel-geojson` met de al gebakken aanloop (48,3 km, 35 punten, 0 km land). ⚠️ Dat
  bestand liep van kade naar knoop (tegen de reisvolgorde in): de eerste bake gaf een naad van 46,8 km. Opgelost met een punt voor punt
  omgekeerde kopie `grafiet-molo-abudhabi-aanloop-khalifa-rev.geojson` (geen nieuwe geometrie, geen herberekening); de functie wijst daarheen.
- Alle 3 markers uit §3 zijn meegenomen; fase D en E vervallen (ICAD-perceel niet te leggen).

**Toets-bevindingen (bakhandleiding §5):**
- **Naden:** alle 3 naden 0,00 km (max 0,00 km) na de omkering van de Khalifa-aanloop.
- **Markers:** alle drie 0,0 km van hun lijn (anker = eindpunt van het been).
- **`toets_knikken.py`:** 38 knikken >= 60 gr, 0 omkeringen, 0 teruglopen. De spikes op b1 zijn OSM-zigzag op kleine wegklassen in de
  gekopieerde Molo-weg (dezelfde geometrie als `grafiet-molo-duisburg`); op de zee-leg twee krappe bochten: 110 gr bij 24,799 N / 53,953 E
  (5,8 km, Golfroute) en 70 gr bij 22,70 N / 60,40 E (8,4 km, Arabische Zee), beide zeerouter-uitvoer, geen terugloop.
- **`toets_rechte_benen.py --min-km 5`:** alleen b2 (haven-aanloop-stippel, omwegfactor 1,000): verwacht, een rechte stippel met reden.
- **Contract:** versie 2, punt_formaat lonlat, modaliteiten {truck, zee}, elk been >= 2 punten.

**Lessen:**
- Een haven-aanloop die met `maak_havenaanloop.py --van kade --naar knoop` is gebakken loopt kade -> knoop; staat de kade aan het EIND
  van de keten, dan moet het geojson omgekeerd worden vóór `--stippel-geojson` (anders een naad ter grootte van de aanloop).
- Open punten blijven die van §7 (Khalifa als aanname, Hormuz-blokkade, volume nul, terminal onbepaald).
