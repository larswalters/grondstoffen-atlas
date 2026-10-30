# Routebrief (licht) · Uranium · Port Hope → Montréal → Hamburg → Gronau (Canada → Duitsland)

**stroom-id:** `uranium-porthope-gronau` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** UF6 uit de Port Hope Conversion Facility (Cameco, Ontario) gaat per **truck** over Hwy 401, A-20 en A-40 naar de Montréal-haven, per **containerschip** (Hapag-Lloyd/OOCL, Montréal–Southampton–Antwerpen–Hamburg) naar HHLA Container Terminal Altenwerder in Hamburg en per **goederentrein** via Buchholz, Rotenburg, Bohmte, Osnabrück en Münster naar Urenco Gronau — **aannemelijk: één bron (urantransport.de, stand 2017/2018), spoorroute en Port Hope–Montréal vermoed**.
**Welke as van het verhaal:** de reserve-as Canada → tweede Urenco-fabriek: Port Hope is de Canadese UF6-leverancier van Gronau [1][2], naast Metropolis (VS). Volume: >20 treinen met >6.000 t UF6 uit Canada en VS samen in 2016 (≈ 4.060 t U, eigen omrekening ×0,676), >4.000 t UF6 in 2017; gebruikelijk 6.000–8.000 t UF6/j [2]. Geen aparte Canada-splitsing gepubliceerd. Gronau verrijkt ≈ 4.550 t U feed-eq./j (sitelaag, schatting).

## 1 · Ketenkaart
```
Port Hope `u-porthope-conversie` ──(b1 truck · Hwy 401 → A-20 → A-40 · hemelsbreed 420 km, geen wegkm)──► Montréal Viau `u-montreal-kade` (onzeker)
  ──(b2 zee · St.-Laurent → Atlantisch → Noordzee → Elbe · MARNET 6.046 km)──► Altenwerder `u-hamburg-altenwerder`
  ──(b3 spoor · Buchholz–Rotenburg–Bohmte–Osnabrück–Münster–Burgsteinfurt · hemelsbreed 240 km, 3 runs)──► Urenco Gronau `u-gronau` ── stoppunt
```
**Afwijking t.o.v. het ontwerp:** geen. Het ontwerp-stuk Hamburg→Gronau is, conform de haalbaarheidstoets, geen kopie van Steinweg-spoor maar nieuwe runs vanaf Altenwerder (Steinweg ligt ca. 5 km noordoostelijker, ander emplacement).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | truck | Port Hope → Montréal Viau (aannemelijk: bron noemt dit stuk niet) | Hwy 401 → A-20 (grens) → A-40 Félix-Leclerc/Métropolitaine → Notre-Dame Est | hemelsbreed 420 km, geen wegkm; OSRM-indicatie 454 km; Hwy 401 is 828 km lang [7] | `maak_stroombeen_weg` (extract canada) | nee |
| b2 | B | zee | Montréal Viau → Altenwerder (Hapag-Lloyd/OOCL-weekdienst, ~1 week [1]) | St.-Laurent, Atlantische Oceaan, Kanaal, Noordzee, Elbe | hemelsbreed 5.732; MARNET getest 6.046,1 | MARNET (`--been zee`) | nee: kade-snap 3,38 km (zeeknoop 6358) en 4,49 km (zeeknoop 3944), beide < 5 km |
| b3a | C | spoor (aannemelijk: bron zegt "vermutlich") | Altenwerder → Rotenburg (Wümme) | Hafenbahn → Hamburg-Harburg → Buchholz | 79,6 gemeten, geen gepubliceerde spoorkm | `toets_spoorroute` | nee |
| b3b | C | spoor | Rotenburg → Bohmte | Rollbahn-corridor naar Osnabrück | 122,4 gemeten | `toets_spoorroute` | nee |
| b3c | C | spoor | Bohmte → Gronau | Osnabrück Hbf → Münster (omkering) → Burgsteinfurt → Gronau | 123,6 gemeten, 2 omkeringen | `toets_spoorroute` | nee |
Spoor totaal 325,6 km gemeten tegen hemelsbreed 240 (+36%, omweg via Rotenburg/Osnabrück/Münster); geen spoorkm gepubliceerd, ±15% is indicatie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-porthope-conversie` | conversie (kop) | Port Hope Conversion Facility (Cameco), 1 Eldorado Place | 43.9437, -78.2955 | letterlijk uit `uranium-mcarthurriver-porthope` §3 [4] | bron-gelegd (daar z15 gezien; OSRM-snap 13 m, Eldorado Place) |
| `u-montreal-kade` | overslag truck → zee | Port of Montréal, containerterminal Viau-zijde | 45.5900, -73.5065 | letterlijk uit `uranium-poti-blindriver` §3 [5] | onzeker: terminal niet gepubliceerd (z15 gezien: containerstapels en kranen langs een kadewand aan de Saint-Laurent; welk lijnbedrijf hier laadt is niet bevestigd) |
| `u-hamburg-altenwerder` | overslag zee → spoor | HHLA Container Terminal Altenwerder (CTA), Hamburg | 53.5050, 9.9358 | [3] (53.50389, 9.93417) + haalbaarheidstoets | bron-gelegd (z15 gezien: kruis op de kadewand, schepen aan de kade, containerstapels en spoorterminal direct westelijk) |
| `u-gronau` | verrijking (staart, stoppunt) | Urenco Deutschland, Gronau | 52.2154, 7.0739 | letterlijk uit `uranium-gronau-novouralsk` §3 [6] | bron-gelegd (daar z15 gezien: scheidingshallen en tailsopslag) |

## 4 · Via-punten (landbenen met een corridorkeuze; punten OP de doorgaande weg/lijn, nooit in een stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Hwy 401 oost van Gananoque | 44.3498, -76.1089 | 401 i.p.v. Hwy 2 / Thousand Islands Parkway langs de rivier [8] |
| b1 | 2 | Hwy 401 bij de 416-knoop (Johnstown) | 44.7427, -75.4956 | 401 oostwaarts i.p.v. Hwy 416 naar Ottawa [8] |
| b1 | 3 | grens Ontario–Québec (401 wordt A-20) | 45.2086, -74.3477 | grensovergang; Wikipedia: 401 loopt tot de Québec-grens [7][8] |
| b1 | 4 | A-40 Félix-Leclerc, West-Island | 45.4573, -73.8391 | A-40 over het eiland i.p.v. A-20 via Dorval/Turcot [8] |
| b1 | 5 | A-40 Métropolitaine, noord-Montréal | 45.5521, -73.6263 | houdt A-40 tot de Viau-afrit; vermijdt de binnenstad [8] |
| b3a | 1 | Rotenburg (Wümme) station | 53.1122, 9.3900 | dwingt Rollbahn via Rotenburg i.p.v. een Soltau-omweg (zie walvisbay-malvesi); ligt op de bron-corridor Buchholz [9] |
| b3b | 1 | Bohmte station | 52.3608, 8.3075 | letterlijk uit `uranium-walvisbay-malvesi` §4; pint Bremen–Osnabrück-corridor (daar BBU-waarneming) [9] |
Router raakt zonder extra via: Hamburg-Harburg (<0,1 km), Rangierbahnhof Maschen (0,05 km van 53.4091, 10.0504), Buchholz-station (0,14 km), Osnabrück Hbf (0,13 km), Münster-omkering (0,0 km), Burgsteinfurt (0,22 km) [9][10] — dus de corridor Maschen–Buchholz–Osnabrück–Münster uit [1] én de 17-uur-blokkade tussen Steinfurt en Gronau (2017, [2]) worden gevolgd.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Port Hope Conversion Facility | Cameco | UO3 → UF6 | vergund 12,5 Mkg U als UF6/j | [4] (via `uranium-porthope-almelo` §5) |
| CTA Altenwerder | HHLA (74,9%) / Hapag-Lloyd (25,1%) | container zee → spoor | ≈ 3 mln TEU/j, geen uraniumcijfer | [3] |
| Urenco Gronau | Urenco | natuurlijk UF6 → verrijkt UF6 + tails | ≈ 4.550 t U feed-eq./j (sitelaag, schatting) | [6] |

## 6 · Stoppunt
De brief stopt bij Urenco Gronau: de verrijkingsfabriek uit het ontwerp; geen bron noemt een vervolgbestemming van deze lading (fase D en E vervallen).

## 7 · Open punten
- **Eén bron, activistisch:** urantransport.de (stand okt 2017 / juni 2018) noemt Port Hope als leverancier en de Montréal–Hamburg-dienst, maar geeft geen volume per route en markeert de spoorroute als "vermutlich" [1][2]. Herkomst Canada of VS niet per zending te scheiden; Halifax (ACL, Unikai Hamburg) is een alternatieve laadhaven in de bron en wordt niet getekend.
- **Port Hope → Montréal niet gebronnd** (truck is aanname); er is geen gepubliceerde wegkm: hemelsbreed 420 km, geen wegkm (OSRM 454 km is OSM-afgeleid) — ±15% is indicatie.
- **Montréal-terminal onzeker** (Viau; terminal niet gepubliceerd, hergebruikt anker).
- **Altenwerder-anker op de kade**: het ruwe OSM-polygoon (53.5046, 9.9328) ligt midden op de stapelplaats; de kademarker staat 0,2 km van Wikipedia [3]. MARNET-zeeknoop 3944 (53.5451, 9.9273) ligt 4,49 km noordelijk: geen haven-aanloop (< 5 km), naad zee → spoor 4,09 km (norm < 5).
- **Twee router-omkeringen b3c:** Münster Hbf (51.9624, 7.6392, 176,9°; Kopfmachen is hier plausibel) en bij de Gronau-aftakking (52.2101, 7.0749, 171,5°; bekend uit `uranium-gronau-novouralsk`); niet weggeschoven.
- **Peiljaar 2016–17.** In 2017 gingen VS- en deels Canada-zendingen per truck [2]; of Port Hope-UF6 nog per trein rijdt is niet gepubliceerd.
- **Sitelaag-hergebruik:** `w-porthope` (43.9576, -78.2942) ligt 1,5 km van het bron-gelegde `u-porthope-conversie`; centraal gelijktrekken.

## 8 · Bronnen
[1] urantransport.de, "Transporte aus USA/Kanada nach Gronau" (Port Hope; Montréal–Hapag-Lloyd/OOCL; CTA Hamburg; "vermutlich Maschen–Buchholz–Osnabrück–Münster"; stand okt 2017) https://urantransport.de/hintergrund/transportrouten/transporte-aus-usakanada-nach-gronau/
[2] urantransport.de, "Transporte zur und von der Urananreicherungsanlage in Gronau" (>20 treinen/>6.000 t UF6 in 2016, >4.000 t in 2017, 6.000–8.000 t/j; blokkade Steinfurt–Gronau; stand juni 2018) https://urantransport.de/hintergrund/transporte-zur-und-von-der-urananreicherungsanlage-in-gronau/
[3] Wikipedia (en), "Container Terminal Altenwerder" (53.50389, 9.93417; HHLA 74,9%, Hapag-Lloyd 25,1%; ≈ 3 mln TEU) https://en.wikipedia.org/wiki/Container_Terminal_Altenwerder
[4] `v2/design/routebrieven/uranium-mcarthurriver-porthope.md` §3/§5 en `uranium-porthope-almelo.md` §5 (Port Hope-anker, Cameco jaarverslag 2015, 12,5 Mkg U)
[5] `v2/design/routebrieven/uranium-poti-blindriver.md` §3 en `uranium-langerheinrich-metropolis.md` §3 (u-montreal-kade, onzeker)
[6] `v2/design/routebrieven/uranium-gronau-novouralsk.md` §3 (u-gronau, DE-Wikipedia 52.21538, 7.07391); `v2/design/uranium-sitelaag.json` `w-urenco-gronau`
[7] Wikipedia (en), "Ontario Highway 401" (828 km, eindigt bij de Québec-grens, A-20 vervolgt) https://en.wikipedia.org/wiki/Ontario_Highway_401
[8] OSRM-demoserver (project-osrm.org, OSM): Port Hope → Montréal Viau 453,95 km; manoeuvrelocaties op Hwy 401, A-20, A-40; via-punten gekozen als wegvertex op de mainline
[9] Wikipedia (de) MediaWiki-API `prop=coordinates`: Bahnhof Bohmte 52.360833, 8.3075; Buchholz (Nordheide) 53.324515, 9.876302; Rotenburg (Wümme) 53.112222, 9.39
[10] OSM via Photon: Rangierbahnhof Maschen 53.4091, 10.0504; Bahnhof Burgsteinfurt 52.1482, 7.3297
[11] Haalbaarheidstoets `uranium-porthope-gronau` (bindend): kade-marker 53.5050, 9.9358, snap 4,5 km, spoor via Rotenburg
[sat] Esri World Imagery (`v2/tools/sat_check.py`): `v2/build-cache/satcheck/sat-uranium-porthope-gronau-{altenwerder,altenwerder-z14,montreal-viau}.png`

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
`bash v2/tools/bak_stromen.sh uranium-porthope-gronau` → `v2/data/stroomroute-uranium-porthope-gronau.json` (96,7 KB, versie 2, lonlat). **5 benen · 6.833,4 km · 4.933 punten · 4 markers · 0 stippel.**

| # | modaliteit | km gebakken | km brief | naad naar vorige | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 454,1 | hemelsbreed 420 / OSRM 454 (geen wegkm) | 0 | wegscan canada 575 s; alle via-snaps 0,00–0,01 km; kade-snap 0,21 km |
| b2 | zee | 6.046,1 | MARNET getest 6.046,1 | 3,38 | 70 MARNET-edges, 642 punten; snaps 3,377 en 4,494 km → geen haven-aanloop |
| b3a | spoor | 82,9 | gemeten 79,6 | 4,09 | altenwerder → rotenburg, 296 punten |
| b3b | spoor | 124,3 | gemeten 122,4 | 0 | rotenburg → bohmte, 254 punten |
| b3c | spoor | 126,0 | gemeten 123,6 | 0 | bohmte → gronau, 411 punten; 2 omkeringen |

**Recept.** b1: profiel `uranium-porthope-gronau-porthope-montreal` in `maak_stroombeen_weg.py` (extract canada, refs 401 / Highway 401 / 20 / 40, vensterKm 50, zeven punten uit §4), gescand met `wegscan_puur.py`; b2: `--been zee` kade → kade; b3: de drie bestaande `toets_spoorroute.mjs`-runs (`BAKE_SUFFIX=-raw`, `--max-snap=60`) als `--been-geojson`. Geen letterlijke kopieën, geen stippel, geen aanloop, geen lucht, geen leiding.

**Toets.** Spoor-km liggen 1,5–4,0% boven de gemeten routeKm van de run (de bake telt de getekende lijn, de run telt alleen edges): binnen ±15%. b1 454,1 km valt op de OSRM-indicatie (geen wegkm, dus geen norm). Naden 0 / 3,38 / 4,09 / 0 / 0 km (alle < 5). Markers: Port Hope 0,00 · Montréal 0,00 · Gronau 0,28 · Altenwerder 0,63 km van hun lijn (de spoor-snap van 0,63 km is het emplacement; marker ligt op de kade). `toets_knikken`: truck 19 knikken (afritspikes en kruispunten, 0 omkeringen), zee 2, spoor b3c 2 omkeringen (Münster 51,9624 / 7,6392, Kopfmachen plausibel, en de Gronau-aftakking 52,2101 / 7,0749). `toets_rechte_benen`: geen regel voor deze stroom.

**Bevindingen / afwijkingen.** Het id noemt Gronau en dat is ook het eindpunt; geen afwijking van het ontwerp. Montréal Viau-anker blijft onzeker en b1 is aanname (geen bron voor Port Hope → Montréal). Het zeebeen begint 3,38 km van de kademarker (zeeknoop 6358) en eindigt 4,49 km van Altenwerder (zeeknoop 3944): beide onder de aanloopgrens van 5 km, maar zichtbaar als naad. Sitelaag `w-porthope` ligt 1,5 km van het anker (centraal gelijktrekken).

**Lessen.** `wegscan_puur.py` op canada (6,4 GB) duurde 575 s op één kern en draait prima op de achtergrond met een logbestand; via-punten uit OSRM-mainline-vertices snapten allemaal binnen 0,01 km, dus de OSRM-via-methode werkt voor Hwy 401/A-20/A-40.
