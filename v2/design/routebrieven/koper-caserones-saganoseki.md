# Routebrief (licht) · koper — Caserones (Chili) → Totoralillo → Saganoseki (Japan)

**stroom-id:** `koper-caserones-saganoseki` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Titel (bol):** Koper · Caserones → Totoralillo → Saganoseki (Japan) — afnemer Saganoseki aannemelijk: één bron
**Keten in één zin:** Cu-concentraat uit de concentrator van Caserones (SCM Minera Lumina Copper Chile, Tierra Amarilla, Atacama; Lundin 70 %, JX 30 %) per **truck** (mijnweg, C-535/C-345, Ruta 30, Ruta 5-bypass om Copiapo, afslag) naar Puerto Punta Totoralillo (CAP), per **bulkschip** over de Stille Oceaan naar de kade van de **Saganoseki-smelter** (JX Nippon Mining & Metals, Oita). Stoppunt = die kade.
**Welke as van het verhaal:** *Chileens eigen-mijnconcentraat naar de Japanse eigenaar-smelter.* Caserones FY2023: 120,6 kt Cu in concentraat + 18,9 kt kathode (en-Wikipedia, ambigu of 120,6 beide vormen omvat) [1]; Lundin 2025: 132,9 kt Cu totaal [2]; 2014-plan 150 kt Cu/j in concentraat [3]. Aandeel dat Saganoseki haalt niet gepubliceerd: JX-offtake sinds 2023 maximaal 30 % van de output [5] (eigen rekensom ≈ 36-40 kt Cu, geen bron).

## 1 · Ketenkaart
```
Caserones-concentrator `cu-caserones-laad` ──(b1 stippel · mijnweg-track ~9,2 km hemelsbreed)──► C-535-wegpunt
  ──(b2 truck · C-535/C-345 → Tierra Amarilla → Ruta 30 → Ruta 5 Norte-bypass · 271,5 km gemeten)──► ertsveld Totoralillo
  ──(b3 stippel · band/shiploader 0,7 km)──► pierkop `cu-totoralillo-kade` ──(b4 stippel · haven-aanloop 122,1 km, rechte lijn)──►
  zeeknoop 4668 (-26.6229,-72.0205) ──(b5 zee · MARNET · ~18.440 km, aannemelijk: één bron)──► zeeknoop 5812 (33.4176,131.9947)
  ──(b6 stippel · haven-aanloop 21,5 km, rechte lijn)──► Saganoseki-kade `cu-saganoseki-kade` ⏹ stoppunt (smelter 0,4 km verder)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | concentrator → eerste openbare wegpunt (-28.1468,-69.6226) | mijnweg, OSM-track (scanner slikt geen track) | hemelsbreed 9,2 km, geen wegkm (OSM-track ~16 km) | rechte stippel | **ja** — mijnterrein/track, geen net |
| b2 | A | truck | wegpunt → Totoralillo-ertsveld | C-535/C-345, Tierra Amarilla, Ruta 30, **Ruta 5 Norte-bypass west van Copiapo**, afslag Totoralillo | hemelsbreed 194 km, geen wegkm; JX: mijn-Copiapo 162 km [3]; gemeten OSM 271,5 (+ b1 ≈ 281) | `maak_stroombeen_weg` profiel `koper-caserones-saganoseki-caserones-totoralillo` (extract chili), lokaal getest | nee |
| b3 | A | leiding (band) | ertsveld → pierkop | CAP-terrein: ingekapselde band naar de pier [6] | 0,7 (hemelsbreed) | rechte stippel | **ja** — eigen terrein |
| b4 | B | zee (aanloop) | pierkop → zeeknoop 4668 | schematisch over water; kade 122,1 km van de zeeknoop (> 5 km) | 122,1 (rechte lijn, NE-landtoets 0,0 km land; `maak_havenaanloop` liep vast op timeout 300 s, geen tweede poging) | `--stippel` (rechte stippel) | **ja** — MARNET reikt niet |
| b5 | B | zee | zeeknoop 4668 → zeeknoop 5812 | Stille Oceaan → Bungo-kanaal; *aannemelijk: één bron (2014, via Coquimbo)* | grootcirkel 17.724; test 18.439,5 [haalbaarheidstoets] | MARNET (`--been zee`) | nee |
| b6 | B | zee (aanloop) | zeeknoop 5812 → Saganoseki-kade | Beppu-baai / kust Oita; kade 21,5 km van de zeeknoop (> 5 km) | 21,5 (rechte lijn; `maak_havenaanloop` timeout 300 s; NE-landtoets 2,4 km over land, kaap Saganoseki) | `--stippel` (rechte stippel) | **ja** — 1:10M-kust kent de haven niet |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-caserones-laad` | mijn / concentrator (laadplek) | Caserones, concentrator | -28.1835, -69.5390 | [1][3] | bron-gelegd (z15 gezien: verwerkingsblok met groene hallen, indikker-tanks en tailingleiding onder de dagbouw; het kruis ligt op het concentratorcomplex; wiki-punt -28.1690,-69.5336 ligt in de put en is verlaten; `sat-koper-caserones-saganoseki-laad.png`) |
| `cu-totoralillo-kade` | overslag truck → zee | Puerto Punta Totoralillo (CAP), pierkop / ertsveld | -26.8543, -70.8161 (ertsveld) · -26.8480, -70.8167 (pierkop) | [2][6] + OSM way 1126714951 | bron-gelegd (z15 gezien: pier met bulkschip, ommuurd ertsveld/loods en bandtracé langs de kust; geen openbaar spoor; `-totoralillo.png`) |
| `cu-saganoseki-kade` | losplek (kade) | Saganoseki, concentraatkade bij de smelter | 33.2527, 131.8735 | [3][7] | bron-gelegd (z15 gezien: lange witte concentraatloods aan de kade van de westelijke baai, smelterterrein met schoorstenen direct oostelijk; `-kade.png`) |
| `w-saganoseki` | smelter (geen been, hergebruik sitelaag) | Saganoseki Smelter & Refinery | 33.2523, 131.8784 | `koper-sitelaag.json` | aannemelijk (OSM-centroïde 33.2562, 131.8762; ~0,4 km van de kade) |

Zeeknopen (geen ankers): 4668 = -26.6229, -72.0205 (122,1 km van Totoralillo) · 5812 = 33.4176, 131.9947 (21,5 km van de Saganoseki-kade).

## 4 · Via-punten (alleen b2; eerste punt = einde b1, laatste = anker; extract chili)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | C-535, eerste openbare weg | -28.1468, -69.6226 | einde mijnstippel; satelliet: wegen naast de tailingdam |
| b2 | 2 | C-535/C-345 | -28.1538, -69.7879 | dwingt de talweg af (refs C-535/C-345) |
| b2 | 3 | C-345 | -27.9123, -70.0220 | idem; richting Tierra Amarilla |
| b2 | 4 | Ruta 30 west van Tierra Amarilla | -27.5015, -70.4088 | kiest Ruta 30 naar Ruta 5, **niet** door Copiapo-centrum (scan zonder via: 0,2 km van het centrum) |
| b2 | 5 | Ruta 5 Norte, zuidkop van de bypass | -27.5060, -70.4491 | begin van de bypass west van Copiapo (OSM way 188007167) |
| b2 | 6 | Ruta 5 Norte, bypass west van de stad | -27.3524, -70.4393 | houdt de lijn 9,7 km uit het stadscentrum (OSM way 390155589) |
| b2 | 7 | Ruta 5 Norte richting Caldera | -27.3526, -70.6531 | pint Ruta 5 (motorway) in plaats van C-35-kustweg |
| b2 | 8 | afslag Totoralillo | -26.8647, -70.7947 | afslag naar de haven; Caldera blijft 2,3 km ernaast |
Recept-profiel (lon, lat), `refs ["C-535","C-345","5"]`, `corridorKlassen ["tertiary","unclassified","service"]`, `eindToegangPrivaat True`, `gepubliceerdKm 262`, `vensterKm 40`: staat al in `maak_stroombeen_weg.py` (eigen profiel, laatste run: 271,5 km, +3,6 % op 262, 4.676 punten, last mile 2,75 km service/unclassified, plant→weg 0,00, weg→kade 0,09 km).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Caserones-concentrator | SCM Minera Lumina Copper Chile (Lundin 70 %, JX 30 %) | erts → Cu-/Mo-concentraat (+ SX-EW-kathode) | 120,6 kt Cu in concentraat (FY2023); totaal 132,9 kt Cu (2025) | [1][2] |
| Puerto Punta Totoralillo | Compañía Minera del Pacífico (CAP) | concentraat: loods 50 kt → shiploader | uitbreiding 2017 voor 500 kt mineraal/j (concentraat) [6] | [6] |
| Saganoseki Smelter & Refinery | JX Nippon Mining & Metals (sinds 2020-04; daarvoor Pan Pacific Copper) | concentraat → anode/kathode | 450 kt Cu/j (sitelaag `w-saganoseki`) | [3][8] |

## 6 · Stoppunt
Bij de Saganoseki-kade: de smelter ligt ~0,4 km van de kade (geen eigen been). Geen bron noemt een afnemer van Saganoseki-kathode; fase D/E vervallen.

## 7 · Open punten
- **Afnemer Saganoseki = één bron uit 2014** [3]: de eerste lading (Koryu, ~5.000 t, 6 weken Pacific) liep Coquimbo → Saganoseki; JX/PPC: het grootste deel naar PPC-smelters. Sinds 2023 is Lundin meerderheid en JX-offtake maximaal 30 % [5]; geen bron koppelt een Totoralillo-lading aan Saganoseki. Beennaam b5 draagt "aannemelijk: één bron".
- **Havenkeuze:** 2014 Coquimbo, Totoralillo sinds het 2017-akkoord [6]; geen bron bevestigt dat de concentraatlading nu nog uit Totoralillo naar Japan gaat.
- **Mijn → haven per truck niet gebrond:** alleen Coquimbo-camions in 2014; Totoralillo-transport (truck of anders) volgt uit geen bron; de wegkm is een eigen OSM-meting, geen gepubliceerde wegkm.
- **Haven-aanloop b6 schematisch:** de rechte lijn zeeknoop 5812 → kade snijdt 2,4 km NE-land (kaap); `maak_havenaanloop` gaf in de eerste trappen 22,8-24,1 km over water maar eindigde op timeout, dus geen pad opgeslagen. De bak-agent mag niet opnieuw proberen maar kan de stippel desnoods in twee rechte stukken om de kaap leggen.
- **b1 is track:** de eerste ~16 km zijn OSM-track (bak: stippel van 9,2 km hemelsbreed); de echte mijnweg ligt anders.
- **Eigenaar:** de smelter staat sinds 2020 onder JX, niet meer onder Pan Pacific Copper (ja-Wikipedia) [8]; sitelaagnaam `Pan Pacific Copper/JX` is verouderd (centraal).
- **Jaarvolume ambigu:** 120,6 kt Cu "fines" kan concentraat of totaal zijn; Saganoseki-aandeel onbekend.

## 8 · Bronnen
[1] en-Wikipedia, Caserones (infobox FY2023: 120.600 t Cu, 18.900 t kathode, 4.600 t Mo; coördinaat -28.1690/-69.5336; Totoralillo-akkoord feb 2017; Lundin 70 / JX 30). https://en.wikipedia.org/wiki/Caserones
[2] Lundin Mining, Caserones: concentraat via Totoralillo, kathode via Antofagasta; 2025 productie 132.881 t Cu. https://lundinmining.com/operations/caserones-project/
[3] JX/Mitsui Mining/Pan Pacific Copper, 24-09-2014: Koryu met eerste Caserones-concentraat aangekomen bij Saganoseki na zes weken Pacific; 150 kt Cu/j in concentraat, merendeel naar PPC-smelters; mijn 162 km ZO van Copiapo. https://www.hd.eneos.co.jp/english/newsrelease/jx/pdf/20140924_02_02_1050061.pdf
[4] Mitsui Mining & Smelting, aug 2014: Koryu vertrekt 29 juli uit Coquimbo, ~5.000 t concentraat, naar Saganoseki. https://www.mitsui-kinzoku.com/Portals/0/resource/uploads/topics_140801e.pdf
[5] Argus, 2024: JX blijft Caserones-koper afnemen, maximaal 30 % van de output. https://www.argusmedia.com/pt/news-and-insights/latest-market-news/2581609-japan-s-jx-to-sell-further-stake-in-chilean-copper-firm
[6] en-Wikipedia, Punta Totoralillo (CAP-haven 25 km ten noorden van Caldera; Caserones-akkoord 2017); MCH/Mundo Marítimo: galpón 50.000 t concentraat, ingekapselde band. https://en.wikipedia.org/wiki/Punta_Totoralillo · https://www.mch.cl/negocios-industria/se-firma-contrato-caserones/
[7] OSM/Nominatim: landuse Saganoseki (centroïde 33.2562, 131.8762); sitelaag `w-saganoseki` (ja-Wikipedia-geohack 33.2523, 131.8784).
[8] ja-Wikipedia, パンパシフィック・カッパー: per 2020-04 Saganoseki overgedragen aan JX Metals; Caserones naar JX/Mitsui-joint venture. https://ja.wikipedia.org
[9] Haalbaarheidstoets 2026-10-29 (hecht_marnet): zeeknoop 4668 → Saganoseki 18.439,5 km; zeeknopen 4668/5812; OSM-weg 261,6 km via Copiapo.
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14-z15): `v2/build-cache/satcheck/sat-koper-caserones-saganoseki-laad.png`, `-totoralillo.png`, `-kade.png`, `-mijnweg.png`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`v2/data/stroomroute-koper-caserones-saganoseki.json` · 136,9 KB · contract versie 2 · 6 benen · 3 markers · totaal 18.864,6 km · naden alle 0,00 km (markers 0,0 km van hun lijn).

| # | modaliteit | km | geometrie | stippel |
|---|---|---|---|---|
| b1 | truck | 9,2 (hemelsbreed, geen wegkm) | rechte lijn concentrator -> C-535-wegpunt | ja, mijnterrein/OSM-track |
| b2 | truck | 271,6 | wegscan profiel koper-caserones-saganoseki-caserones-totoralillo (chili), 4.676 punten | nee |
| b3 | leiding (band) | 0,7 | rechte lijn ertsveld -> pierkop | ja, eigen CAP-terrein, geen OSM-way |
| b4 | zee (aanloop) | 122,1 | rechte lijn pierkop -> zeeknoop 4668 | ja, MARNET reikt niet |
| b5 | zee | 18.439,5 | MARNET zeeknoop 4668 -> 5812, 75 edges, 1.886 punten, snap 0,0 km | nee (aannemelijk: één bron in de naam) |
| b6 | zee (aanloop) | 21,5 | rechte lijn zeeknoop 5812 -> Saganoseki-kade | ja, 1:10M-kust kent de haven niet |

**Markers:** Caserones-concentrator (-28.1835, -69.5390), Totoralillo-pierkop (-26.8480, -70.8167), Saganoseki-kade (33.2527, 131.8735). Het ertsveld (-26.8543, -70.8161) is geen eigen marker; het is het begin van b3 en het eind van b2.

**Recept:** functie `bak_koper_caserones_saganoseki` in `v2/tools/bak_stromen.sh`; het wegprofiel stond al in `maak_stroombeen_weg.py` en het geojson `koper-caserones-saganoseki-weg-caserones-totoralillo.geojson` (uit de ontwerpfase, 271,6 km) is letterlijk hergebruikt, geen nieuwe wegscan. Zonder `--been-geojson` voor lucht of leiding.

**Toets:** b2 271,6 km tegen de eigen indicatie 262 km = +3,6 % (geen gepubliceerde wegkm; JX geeft alleen mijn-Copiapo 162 km); b5 18.439,5 km gelijk aan de haalbaarheidstoets (18.439,5). `toets_knikken`: 17 knikken >= 60 gr over de hele stroom (alle in b2), 1 omkering, 0 terugloop; de scherpe spikes (1-31 m) liggen op via-punt-snaps langs C-535/C-345 en bij de afslag Totoralillo, de krappe bocht van 185 m bij -27.4955, -70.2690 (Ruta 30). `toets_rechte_benen`: alleen de vier stippels (b1, b3, b4, b6) staan als recht, elk met reden.

**Toelichting stippels:** b1 mijnweg is OSM-track die de scanner niet doorlaat, de echte mijnweg ligt anders. b3 is de ingekapselde band van CAP. b4 en b6: `maak_havenaanloop` is in de ontwerpfase op timeout 300 s gelopen en niet opnieuw geprobeerd; b4 snijdt 0,0 km land, b6 snijdt 2,4 km NE-land (kaap Saganoseki) en is niet in stukken om de kaap gelegd omdat daar geen bewezen coördinaat voor is.

**Lessen:** (1) het id noemt Saganoseki en de lijn eindigt ook in Saganoseki: geen afwijking. (2) Het gedeelde wegbeen uit de ontwerpfase is zonder slot hergebruikt (alle weg-slots bezet, geen herscan nodig). (3) Beide havens liggen buiten het MARNET-zeenet; de twee aanlopen (143,6 km) plus mijnweg en band (9,9 km) maken 153,5 km stippel van 18.864,6 km (0,8 %).
