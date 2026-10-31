# Routebrief (licht) · Uranium · Springfields → Hull → Zeebrugge → Gronau (Verenigd Koninkrijk → Duitsland)

**stroom-id:** `uranium-springfields-gronau` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** UF6 uit de Springfields-conversie (Westinghouse/Cameco-tolconversie, Salwick bij Preston) gaat per **truck** over M55, M6, M61, M60 en M62 naar de veerterminal van Hull, per **veerboot** over de Noordzee naar Zeebrugge en per **truck** over E34, A67, A57/A42 en A31 naar Urenco Gronau. **Aannemelijk: één bron (urantransport.de) noemt alleen "per LKW ... auf einer Fähre über Belgien"; havens, veerlijn en route zijn afleiding.** Peiljaar 2012-2014: de UK-levering stopt eind 2014, daarna rijdt UF6 uit Frankrijk [1][2].
**Welke as van het verhaal:** de VK-schakel van de Gronau-voeding: Springfields staat in de leverancierslijst van Gronau [1]. Volume: 2012 19 leveringen van 50-100 t, 2013 nul, 2014 bijna 20 van bijna 100 t UF6 [1] = **ca. 650-1.350 t U/j** (UF6 × 0,676, eigen omrekening, indicatie; peiljaar 2012/2014). Springfields-UF6-fabriek: 6.000 t/j, Cameco-tolconversie 5.000 t U/j tot aug 2014 [2].

## 1 · Ketenkaart
```
Springfields `u-springfields` ──(b1 truck · M55 → M6 → M61 → M60 → M62 → A63 · hemelsbreed 166 km, geen wegkm; OSRM 212 · aannemelijk)──► Hull veerterminal `u-hull-veer`
  ──(b2 zee · veer Hull–Zeebrugge, Humber → Noordzee · MARNET 360,9 km tegen hemelsbreed 355 · aannemelijk)──► Zeebrugge veerterminal `u-zeebrugge-veer`
  ──(b3 truck · N34/N49 → R1 Antwerpen → E34 → A67 Eindhoven → A57/A42 → A31 · hemelsbreed 284 km, geen wegkm; OSRM 385 · aannemelijk)──► Urenco Gronau `u-gronau` ── stoppunt
```
**Afwijkingen t.o.v. het ontwerp:** (1) de ontwerp-corridor "E40/E34 Gent, A1/A35 Enschede" vervalt: OSRM rijdt Zeebrugge → Gronau via E34, A67 en A42/A31 en niet via Enschede (385 km, niet de ontwerp-indicatie 430) [8]; (2) Hull "King George Dock" wordt het OSM-terminalpunt "Hull Ferry Terminal" aan de Humber [5].

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | Springfields → Hull veerterminal (aannemelijk: haven niet genoemd) | M55 → M6 → M61 → M60 → M62 → A63 (Clive Sullivan Way) → Hedon Road | hemelsbreed 166 km, geen wegkm; OSRM-indicatie 212 km [7] | maak_stroombeen_weg (groot-brittannie) | nee |
| b2 | C | zee | Hull veerterminal → Zeebrugge veerterminal (aannemelijk: bron noemt alleen veer via België) | Humber → Noordzee, veerlijn Hull–Zeebrugge [4][6] | hemelsbreed 355 km; MARNET 360,9 km (geen gepubliceerde zeemijl gevonden) | MARNET kade → zeeknoop 1629 + haven-aanloop | aanloop Zeebrugge: ja (22,9 km); Hull: nee (1,8 km) |
| b2a | C | zee (stippel) | zeeknoop 1629 → Zeebrugge veerterminal | haven-aanloop, schematisch | 22,9 km hemelsbreed | rechte stippel (maak_havenaanloop gaf na 300 s geen pad) | ja: 1:10M-kust kent de haven niet |
| b3 | C | truck | Zeebrugge → Urenco Gronau (aannemelijk) | N34/N49 → R1 Antwerpen → E34 → A67 → A57 → A42 → A3 → A2 → A31 | hemelsbreed 284 km, geen wegkm; OSRM-indicatie 385 km [8] | maak_stroombeen_weg (belgie, nederland, de-nrw) | nee |
De ±15%-toets is voor b1 en b3 alleen indicatie (geen gepubliceerde wegkm); b2 gemeten tegen hemelsbreed (+1,6%).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-springfields` | conversie (kop) | Springfields nuclear site, Salwick (Westinghouse) | 53.7775, -2.8081 | [3] Wikipedia-coördinaat (53.7775, -2.80806) | bron-gelegd (z15 gezien: ommuurd complex van hallen en schoorstenen met spoorlijn en solarveld ernaast; kruis ligt op het noordelijk deel van het terrein; OSRM-snap 0,22 km op Lea Lane) |
| `u-hull-veer` | overslag truck → veer | Hull Ferry Terminal (Hedon Road, King George Dock-zijde) | 53.7419, -0.2788 | OSM-node "Hull Ferry Terminal" 53.74189, -0.27914 [5]; ontwerp [12] | bron-gelegd (z15 gezien: ro-ro-pier aan de Humber met een veerboot aan de kade, trailerrijen en poortgebouwen; OSRM rijdt tot "Rotterdam ferry car check") |
| `u-zeebrugge-veer` | overslag veer → truck | Zeebrugge, P&O-terminal Leopold II-dam | 51.3410, 3.1897 | OSM-checkpoint "P&O Zeebrugge - Hull" 51.3399, 3.1868 [6] (0,24 km ZW); ontwerp [12] | aannemelijk (z15 gezien: kadekop van de Leopold II-dam bij containerstapels en kranen; geen veerboot aan deze kade, de bron noemt geen terminal; Zeebrugge-LNG-anker `gas-zeebrugge-lng` is geen veerterminal en wordt niet hergebruikt) |
| `u-gronau` | verrijking (staart, stoppunt) | Urenco Deutschland, Gronau | 52.2154, 7.0739 (routeanker 52.2184, 7.0723) | letterlijk uit `uranium-gronau-vasteras` §3 [10][11] | bron-gelegd (daar z15 gezien: scheidingshallen met schakelstation) |

## 4 · Via-punten (alleen waar een corridorkeuze bestaat; punten OP de doorgaande weg, nooit in een stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | M55/M6 bij de Preston-bypass | 53.8037, -2.6938 | M55 naar de M6 i.p.v. A59 door Preston [7] |
| b1 | 2 | M6/M61-knoop (Bamber Bridge) | 53.7378, -2.6499 | M61 naar Manchester i.p.v. M6 door naar M62 bij Warrington [7] |
| b1 | 3 | M61/M60 (Worsley, ten NW van Manchester) | 53.5277, -2.3632 | M60-ring noordzijde, niet door het centrum [7] |
| b1 | 4 | M60/M62 (Simister) | 53.5468, -2.2698 | M62 oostwaarts over de Pennines [7] |
| b1 | 5 | M62 bij Brighouse | 53.7296, -1.7324 | M62 houden (niet M606/Bradford) [7] |
| b1 | 6 | M62 bij Birstall (M621, ten westen van Leeds) | 53.7464, -1.6495 | houdt de M62 richting Goole/Humber i.p.v. M621 naar Leeds [7] |
| b1 | 7 | A63 Clive Sullivan Way (eind M62, westrand Hull) | 53.7223, -0.4742 | A63 Hull in langs de Humber i.p.v. een A15-omweg [7] |
| b3 | 1 | A11 bij Zeebrugge-Brugge | 51.2950, 3.2549 | A11 naar Brugge i.p.v. de kustweg N34 oostwaarts [8] |
| b3 | 2 | N49 Expresweg (Maldegem) | 51.2211, 3.4109 | N49/E34-corridor naar Antwerpen i.p.v. A10/E40 via Gent [8] |
| b3 | 3 | R1 Antwerpen (ring, zuidwest) | 51.2226, 4.3518 | ring, niet het centrum [8] |
| b3 | 4 | E34 na de ring (Zandhoven) | 51.2030, 4.5702 | E34 naar Eindhoven i.p.v. E313 naar Hasselt [8] |
| b3 | 5 | A67 bij de Eindhoven-ring | 51.4049, 5.4906 | A67 oostwaarts i.p.v. A2/A73 [8] |
| b3 | 6 | A57 bij Duitse grens/Moers | 51.4398, 6.6032 | Ruhr-doorsteek A57 i.p.v. A3 via Emmerich [8] |
| b3 | 7 | A3/A2 bij Oberhausen | 51.4918, 6.8172 | A3 → A2 naar het noorden [8] |
| b3 | 8 | A31 begin (Bottrop) | 51.5555, 6.9262 | A31 noord naar Gronau i.p.v. A1 via Münster [8] |
Het snappen van de via-punten op de OSM-scan is niet getest in deze brief (alleen OSRM-manoeuvrelocaties, wegvertices); een snap > 5 km is een fout (bakhandleiding §2). b1 begint en b3 eindigt op het routeanker; b3 begint op de kademarker.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Springfields-conversie | Westinghouse (NDA-lease); Cameco-tolconversie 2006-2014 | UO3 → UF6 | 6.000 t/j; Cameco 5.000 t U/j tot aug 2014; sloot daarna | [2][3] |
| Urenco Gronau | Urenco | natuurlijk UF6 → verrijkt UF6 + tails | ≈ 4.550 t U feed-eq./j (sitelaag, schatting) | [10][11] |

## 6 · Stoppunt
De brief stopt bij Urenco Gronau: de verrijkingsfabriek die [1] als ontvanger van de UK-trucks noemt; vervolgbestemmingen van deze lading zijn niet gebronnd (fase D en E vervallen).

## 7 · Open punten
- **Eén bron, en die zegt alleen "per Fähre über Belgien":** urantransport.de noemt UK-trucks tot 2014 en Springfields in de leverancierslijst, niet Hull, Zeebrugge, een veerlijn of een route [1]. Het Landtag-document (16-5733) zegt volgens de haalbaarheidstoets "vermutlich Springfields" [12]; zelf niet gelezen.
- **Veerlijn en havens zijn afleiding:** Hull–Zeebrugge volgt uit OSM ("P&O Zeebrugge - Hull") en Wikipedia ("Former P&O Ferries service to Hull") [4][6]; dat de lijn in 2012-14 voer en welke terminal gebruikt werd is niet gebronnd. OSM-relaties kennen de lijn niet meer (alleen Teesport en Tilbury) [12].
- **Zeebrugge-anker aannemelijk, geen bron-gelegd:** de P&O-checkpoint ligt 0,24 km ZW van het anker; de veerkade zelf is niet gezien.
- **Haven-aanloop Zeebrugge:** de terminal ligt 22,9 km van MARNET-zeeknoop 1629 (51.5000, 3.4000): rechte stippel (400 m op de kadekop valt in het 1:10M-landpolygoon; de rest is water). Hull ligt 1,8 km van knoop 7014 (53.7308, -0.2994): geen aanloop; naden zee → truck 1,8 km en 0 km.
- **Geen wegkm gepubliceerd** voor b1 en b3; OSRM 211,9 en 385,3 km zijn OSM-afgeleid. Het MARNET-getal 360,9 km is een lokale routering [9].
- **Eindjaar 2014:** de Springfields-UF6-fabriek sloot na aug 2014 [2]; sinds 2015 levert Frankrijk [1]. 2013 had geen UK-leveringen [1]. "2012: 19 mit jeweils 50-100 Tonnen auf 4-8 LKW" is onduidelijk geformuleerd; de volumeband is daarom een indicatie.
- **Sitelaag:** `w-westinghouse-springfields` (53.75, -2.80, onzeker) ligt 3,1 km naast het bron-gelegde `u-springfields`; centraal gelijktrekken.

## 8 · Bronnen
[1] urantransport.de, "Transporte zur und von der Urananreicherungsanlage in Gronau" (2011 222 LKW Feed; 2012 19 leveringen 50-100 t; 2013 geen; 2014 bijna 20 van bijna 100 t; UK-trucks per veer via België; vanaf 2015 Frankrijk; Springfields in de leverancierslijst) https://urantransport.de/hintergrund/transporte-zur-und-von-der-urananreicherungsanlage-in-gronau/
[2] World Nuclear Association, "Nuclear Power in the United Kingdom" (Springfields 6.000 t/j conversie; Cameco-tolconversie 5.000 t U/j 2006-aug 2014, daarna sluiting) https://world-nuclear.org/information-library/country-profiles/countries-t-z/united-kingdom
[3] Wikipedia (en), "Springfields" (53.7775, -2.80806; Salwick bij Preston; Westinghouse, NDA-lease) https://en.wikipedia.org/wiki/Springfields
[4] Wikipedia (en), "Zeebrugge" ("Former P&O Ferries service to Hull") https://en.wikipedia.org/wiki/Zeebrugge
[5] OSM via Nominatim: "Hull Ferry Terminal, Hedon Road" 53.74189, -0.27914; "King George Dock" 53.74279, -0.26715
[6] OSM via Nominatim: "Checkpoint P&O Zeebrugge - Hull, Leopold II-dam" 51.33988, 3.18684
[7] OSRM-demoserver (OSM): Springfields → Hull 211,85 km; manoeuvrelocaties op M55, M6, M61, M60, M62, A63
[8] OSRM-demoserver (OSM): Zeebrugge → Gronau routeanker 385,3 km; manoeuvrelocaties op A11, N49, R1, E34, A67, A57, A3, A2, A31
[9] Lokale MARNET-routering (`hecht_marnet.py route`, Hull → zeeknoop 1629): 360,9 km, 6 edges; zeeknopen 7014 (1,83 km) en 1629 (22,92 km)
[10] `v2/design/routebrieven/uranium-gronau-vasteras.md` §3/§7 (u-gronau 52.2154, 7.0739; routeanker 52.2184, 7.0723)
[11] `v2/design/routebrieven/uranium-gronau-novouralsk.md` §3 (DE-Wikipedia 52.21538, 7.07391); `v2/design/uranium-sitelaag.json` (`w-urenco-gronau`, `w-westinghouse-springfields`)
[12] Haalbaarheidstoets `uranium-springfields-gronau` (bindend): Hull 53.7419, -0.2788, Zeebrugge 51.3410, 3.1897, aanloop als stippel, Landtag NRW "vermutlich Springfields"
[sat] Esri World Imagery (`v2/tools/sat_check.py`): `v2/build-cache/satcheck/sat-uranium-springfields-gronau-{springfields,hull,zeebrugge}.png`

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-uranium-springfields-gronau.json` (120,2 KB, versie 2, lonlat, 4 markers) · **functie:** `bak_uranium_springfields_gronau` in `v2/tools/bak_stromen.sh` · **profielen:** `uranium-springfields-gronau-springfields-hull` en `uranium-springfields-gronau-zeebrugge-gronau` in `v2/tools/maak_stroombeen_weg.py` · **titel:** Uranium · Springfields (VK) → Hull → Zeebrugge → Urenco Gronau (Duitsland).

| # | modaliteit | km (gebakken) | tegen brief | naad voor | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 211,6 | OSRM-indicatie 212 km (hemelsbreed 166, geen wegkm): -0,2% | 0 | doorgetrokken, 2.276 punten |
| b2 | zee | 360,9 | MARNET 360,9; hemelsbreed 355: +1,7% | 1,83 km (Hull-kade → zeeknoop 7014) | doorgetrokken, 41 punten |
| b2a | zee (stippel) | 22,9 | 22,9 km hemelsbreed | 0 | rechte stippel zeeknoop 1629 → Zeebrugge |
| b3 | truck | 379,2 | OSRM-indicatie 385 km (hemelsbreed 284, geen wegkm): -1,5% | 0 | doorgetrokken, 4.037 punten |
Totaal 974,6 km, 6.356 punten. De ±15%-toets is voor b1 en b3 alleen indicatie (geen gepubliceerde wegkm). Grootste naad 1,83 km (zee → truck bij Hull, geen aanloop nodig: kade 1,8 km van knoop 7014, onder de 5 km-grens). Markers 0,0 km van de lijn (Hull, Zeebrugge) en 0,38 resp. 0,35 km (Springfields, Gronau: routeanker op het verbonden net, zie hieronder).

**Recept.** b1 en b3: wegscan (`wegscan_puur.py`) met de via-punten uit §4; b2: MARNET Hull-kade → zeeknoop 1629; b2a: rechte stippel. Dispatch: `bash v2/tools/bak_stromen.sh uranium-springfields-gronau`.

**Toelichting per stippel/aanloop.** (1) **Zeebrugge-aanloop (b2a), 22,9 km:** `maak_havenaanloop.py` gaf opnieuw na 300 s geen pad (exit 124, trappen 0,0025° gebufferd en kaal: geen pad); rechte stippel zeeknoop 1629 → kade, geen tweede poging. De stippel betekent "hier reikt het net niet" (1:10M-kust kent de haven niet), niet onzekerheid. (2) Hull: geen aanloop (1,8 km). Geen luchtbeen, geen leiding, geen gedeeld been.

**Afwijkingen t.o.v. de brief.** (a) **b1 routeanker:** de dichtstbijzijnde OSM-knoop bij het siteanker (53.7775, -2.8081) is een los plantwegje van één way (eigen component) en gaf "geen wegpad tussen punt 0 en 1"; b1 start daarom op een knoop van het verbonden net (53.7764, -2.8136, OSM service-weg, 0,38 km van het siteanker; zelfde patroon als Gronau). Het siteanker blijft de marker `u-springfields`. (b) **b3 via-punt A57 Moers:** (51.4398, 6.6032) snapte op een zijweg 0,4 km ten noorden van de A57 en gaf een keerlus (TERUGLOOP 170 gr, `toets_knikken`); verplaatst naar de A57-hoofdbaan (51.4363, 6.6035), daarna 0 terugloop. (c) b3 eindigt op het Gronau-routeanker (52.2184, 7.0723) en niet op het plantanker (zelfde reden als uranium-gronau-vasteras).

**Toetsen.** `toets_knikken`: b1 9 knikken (1 omkering, een echte bocht bij de Hull-pier), b3 21 knikken (4 omkeringen: Maldegem N49-stub 0 m, afritten bij Moers en Bottrop; geen terugloop). `toets_rechte_benen`: alleen de Zeebrugge-stippel (omwegfactor 0,999, bedoeld). Geen via-snap > 0,01 km. Geen naad > 5 km.

**Lessen.** (1) Een plantanker op een los OSM-plantwegje (Springfields, Gronau) vraagt een routeanker op het verbonden net: zoek de dichtstbijzijnde knoop in de grootste component uit de `-pbfways-`-cache. (2) Een via-punt uit OSRM-manoeuvrelocaties kan op een toe-/afrit of zijweg vallen (Moers): `toets_knikken` ziet dat als TERUGLOOP; verplaats het naar een punt dat al op de hoofdbaan van de eigen route ligt. (3) Veerterminal-ankers (Hull, Zeebrugge) werken als gewone kade-ankers voor het zeebeen; alleen Zeebrugge heeft een haven-aanloop nodig.
