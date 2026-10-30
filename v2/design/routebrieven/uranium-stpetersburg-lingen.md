# Routebrief (licht) · uranium — Sint-Petersburg (Rusland) → Hamburg → Framatome ANF Lingen (Duitsland)

**stroom-id:** `uranium-stpetersburg-lingen` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** Russische UF6 en uraniumoxide-pellets (fabriek onbekend) gaan per **zeeschip** (NSC en ASPOL: Mikhail Lomonosov, Mikhail Dudin, Kapitan Yakovlev e.a.) van Sint-Petersburg door de Oostzee en het **Nord-Ostsee-Kanal** (Kiel-Holtenau → Brunsbüttel) en de Elbe naar Container Terminal Burchardkai in Hamburg, daarna per **truck** (A7, A1, B72/B213) naar de splijtstoffabriek Framatome ANF in Lingen (Ems) — stoppunt.
**Welke as van het verhaal:** *de Noordroute van Russisch splijtstofmateriaal naar Duitsland.* **Volume:** 68,8 t uranium uit Rusland naar Lingen in 2024, +66% op 2023 (dpa, 03-01-2025) [6]; product niet gespecificeerd, eenheid t U/j (massa), peiljaar 2024. Route-gegevens (Hamburg, A7/A1) zijn peiljaar 2016-17 [1][2]; zending 13-10-2025 liep via Duinkerken, niet Hamburg [7]. Historisch: 12 pelletvrachten uit Rusland in 2017, 13 leveringen UF6 en pellets uit alle herkomsten in 2013 [3].

## 1 · Ketenkaart
```
Russische fabriek (niet genoemd, niet getekend) ──(niet gedocumenteerd)──►
Sint-Petersburg-kade `u-stpetersburg-kade` ──(b1 zee · Finse Golf, Oostzee, Beltzee · MARNET 1.428 km)──► zeeknoop 6862 (Kieler Bucht)
  ──(b2 zee-aanloop, stippel · Kieler Förde · ~16 km)──► Holtenau-sluis `u-holtenau-sluis`
  ──(b3 zee · Nord-Ostsee-Kanal · 96,5 km OSM tegen ~98 km bron)──► Brunsbüttel-sluis `u-brunsbuettel-sluis`
  ──(b4 zee-aanloop, stippel · Elbe · ~6 km)──► zeeknoop 3937 ──(b5 zee · Elbe · MARNET 64 km)──►
Container Terminal Burchardkai `u-hamburg-burchardkai` ──(b6 truck · A7 → A261 → A1 → B72/B213 · hemelsbreed 209 km, geen wegkm; aannemelijk)──►
Framatome ANF Lingen `u-lingen-anf` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | SPb-kade → zeeknoop 6862 (54.4541, 10.3107) | Finse Golf, Oostzee, Beltzee tot de Kieler Bucht (NSC/ASPOL, 3-5 dagen tot Kiel [2]) | MARNET 1.428,2 km (grootcirkel 1.338); geen gepubliceerde zeekm | MARNET | aanloop SPb: nee (kade 4,9 km van zeeknoop 6849) |
| b2 | B | zee | zeeknoop 6862 → Holtenau-sluis | Kieler Förde (Friedrichsort, Möltenort) | 16,4 (handmatig op satelliet) | `--stippel-geojson` (eigen polylijn, 5 punten) | **ja** — haven-aanloop: sluis 13,5 km van de zeeknoop (>5 km); `maak_havenaanloop` gaf exit 124 (300 s) |
| b3 | B | zee | Holtenau-sluis → Brunsbüttel-sluis | Nord-Ostsee-Kanal | **96,5 gemeten** tegen ~98 km [5] (−1,5%); ~12 uur sluis-Hamburg [2] | `maak_rivierbeen` (OSM-bulklaag), **doorgetrokken** | nee |
| b4 | B | zee | Brunsbüttel-sluis → zeeknoop 3937 (53.8771, 9.2273) | Elbe-monding | 6,1 (handmatig op satelliet) | `--stippel-geojson` (eigen polylijn, 3 punten) | **ja** — haven-aanloop: sluis 5,9 km van de zeeknoop (>5 km); `maak_havenaanloop` exit 124 |
| b5 | B | zee | zeeknoop 3937 → Burchardkai (Athabaskakai [2]) | Elbe (Unterelbe → Norderelbe) | MARNET 63,8 km; Burchardkai-snap 1,4 km (<5, geen aanloop) | MARNET | nee |
| b6 | D | truck | Burchardkai → Lingen | A7 → A261 → A1 (Bremen) → afrit B72 → B213 (Cloppenburg–Löningen–Haselünne–Lingen) | **hemelsbreed 209 km, geen wegkm**; OSRM-indicatie 242 km [9] (±15%-toets = indicatie) | maak_stroombeen_weg (3 extracts) | nee — *aannemelijk: één bron noemt A7 en A1 tot Bremen, daarna "nicht bekannt"* [1] |

Totaal zee ≈ 1.611 km (via het kanaal) tegen MARNET direct SPb → Burchardkai via Skagen 2.226 km: het kanaal is de gedocumenteerde keuze [2].

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-stpetersburg-kade` | overslag (kop) | Petrolesport, Gutujevski-eiland, Sint-Petersburg | 59.8909, 30.2376 | letterlijk uit `uranium-inkai-stpetersburg.md` §3 [10] | bron-gelegd (hergebruikt: containerstapels, kranen); bron noemt alleen "St. Petersburg", niet de kade |
| `u-holtenau-sluis` | passage (kanaalingang Oost) | Sluizen Kiel-Holtenau, fjordzijde | 54.3657, 10.1446 | OSM `waterway=lock_gate` ways 451861898/451861900 [8]; [2] noemt de sluis | bron-gelegd (z15 gezien: sluiskamers met schip, Kieler Förde oostelijk) |
| `u-brunsbuettel-sluis` | passage (kanaalingang West) | Sluizen Brunsbüttel (Elbezijde) | 53.8917, 9.1466 | eind van OSM-kanaal (bulk-knoop 31883, 0,00 km); [5] noemt Brunsbüttel | bron-gelegd (z15 gezien: twee lange sluiskamers met pieren aan de Elbe) |
| `u-hamburg-burchardkai` | overslag zee → truck | HHLA Container Terminal Burchardkai (Athabaskakai), Waltershof | 53.5328, 9.9223 | letterlijk uit `grafiet-bogala-hauzenberg.md` §3 (OSM relation 15625871); [1][2] noemen Burchardkai/Athabaskakai | bron-gelegd (z15 eigen blik: kranen en containerstapels aan de Elbekade, spoorbundel) |
| `u-lingen-anf` | fabriek (staart, stoppunt) | Framatome ANF Brennelementfertigungsanlage, Lingen (Ems), naast KKW Emsland | 52.4804, 7.3315 | WP-DE geohack 52.480415 / 7.331507 [4]; [3] "in einem Waldgebiet … nur eine Zufahrtsstraße" | bron-gelegd (z15 gezien: omheind terrein met bedrijfsgebouwen in bos, ~0,8 km NO van de KKW-gebouwen) |

## 4 · Via-punten b6 (op de doorgaande weg; punten uit een OSRM-controle, nearest ≤ 8 m van een weg [9])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b6 | 1 | A7/A261-splitsing (Hamburg-Südwest) | 53.4398, 9.9211 | pint A7 zuidwaarts door de Elbtunnel en daarna A261 naar de A1, i.p.v. A7 naar Hannover |
| b6 | 2 | A261 → A1-samenvoeging (Harburg) | 53.3726, 9.8470 | pint A1 richting Bremen |
| b6 | 3 | Bremer Kreuz (A1/A27) | 53.0413, 8.9830 | A1 langs Bremen, niet A27/A28 door de stad ("Bremer Kreuz" Wikipedia-coördinaat) |
| b6 | 4 | A1-afrit naar de B72 (ten zuiden van Dreieck Ahlhorner Heide) | 52.8139, 8.2092 | de corridorkeuze: A1 verlaten richting B72/B213 i.p.v. door naar Osnabrück (A30/A31, niet gemeten) |
| b6 | 5 | B213 tussen Cloppenburg en Löningen | 52.8008, 7.8496 | houdt de B213 aan, buiten beide stadscentra |
| b6 | 6 | B213 ten zuiden van Haselünne | 52.6344, 7.4498 | houdt de B213 aan richting Lingen-Noord; geen stadscentrum |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Russische fabriek (niet genoemd) | Rosatom/TVEL (niet aangewezen) | UF6 / UO2-pellets → haven | niet gespecificeerd | [3] |
| Framatome ANF Lingen | Framatome (ANF GmbH) | UF6 → UO2-poeder → pellets → splijtstofelementen (per truck, ~10/maand) | 800 t U/j vergund voor droge conversie, 650 t U/j overige delen; exportaandeel 80-90% | [4][3] |

## 6 · Stoppunt
De brief stopt bij de fabriek in Lingen: het opgedragen eindpunt en de enige afnemer die [1][2][3] voor deze Hamburg-lading noemen. Fase E vervalt; de uitgaande splijtstofelementen (naar o.a. Frankrijk, Finland, Zweden) zijn een eigen stroom.

## 7 · Open punten
- **Russische herkomstfabriek onbekend** [1][3]: de lijn begint op de SPb-kade; een pelletfabriek (Elektrostal) of UF6-bron is niet aangewezen en niet getekend.
- **Peiljaar route 2016-17** ("Stand: Juni 2016" [1][2]); pellets uit Rusland nog t/m januari 2022 [3]. De zending van 13-10-2025 (Mikhail Dudin, 12 vaten) werd in Duinkerken gelost, bestemming Romans of Lingen, Hamburg niet genoemd [7]: de Hamburg-route na 2022 is niet bevestigd.
- **Geen wegkm gepubliceerd; wegdeel na Bremen onbekend** ("nicht bekannt" [1]): de A1-afrit richting B72/B213 is een eigen keuze op basis van de OSRM-snelste route [9]; alternatief A1 → Osnabrück → A30 → A31 (langer, niet gemeten).
- **Haven-aanlopen handmatig**: `maak_havenaanloop` gaf bij Kiel-Holtenau en Brunsbüttel exit 124 (300 s); de twee stippels zijn met de hand in de Kieler Förde en langs de Elbe gelegd op Esri z13-z15, niet gemeten.
- **Sitelaag-afwijking (alleen melden):** `w-framatome-lingen` staat op 52.5167, 7.3167 (stadscentrum Lingen, onzeker), 4,3 km van de fabriek 52.4804, 7.3315.
- **Burchardkai-netgat:** het dichtstbijzijnde OSM-punt aan de terminal is een geïsoleerd service-eiland (grafiet-brief); `eindToegangPrivaat` en een anker-verbinding van ~0,6 km zijn te verwachten.
- **Volume is een nationaal jaartotaal** (68,8 t U, 2024 [6]), niet specifiek voor Hamburg; urgewald noemt >82 t Russisch uranium naar Duitsland in 2024 en ≥18 transporten naar ANF sinds 2022 [7b].
- **Sancties:** Russische aanvoer naar Lingen loopt door; de Rosatom-ANF-joint venture is (april 2025) niet vergund [7b].

## 8 · Bronnen
[1] urantransport.de, "Transporte von St. Petersburg über Hamburg nach Lingen" (Stand juni 2016): NSC en ASPOL-schepen, Burchardkai, A7 en A1, na Bremen onbekend. https://urantransport.de/hintergrund/transportrouten/st-petersburg-lingen/
[2] urantransport.de, "Transporte durch den Nord-Ostsee-Kanal" (Stand juni 2016): 3-5 dagen tot Kiel, Holtenau → Hamburg ~12 uur, Athabaskakai. https://urantransport.de/hintergrund/transporte-durch-den-nord-ostsee-kanal/
[3] urantransport.de, "Brennelementefertigung in Lingen und Transporte dort": 2013, 2017 (12 pelletvrachten uit Rusland), 2022; geen spoor, alles per truck. https://urantransport.de/hintergrund/brennelementefertigung-in-lingen-und-transporte-dort/
[4] Wikipedia DE, "Brennelementfertigungsanlage Lingen": coördinaat 52.480415/7.331507, 800 t U/j conversie, 650 t U/j overig. https://de.wikipedia.org/wiki/Brennelementfertigungsanlage_Lingen
[5] Wikipedia EN, "Kiel Canal": 98 km, Brunsbüttel–Holtenau. https://en.wikipedia.org/wiki/Kiel_Canal
[6] Volksstimme/dpa, 03-01-2025, "Deutlich mehr Uran aus Russland nach Lingen geliefert": 68,8 t in 2024. https://www.volksstimme.de/panorama/deutlich-mehr-uran-aus-russland-nach-lingen-geliefert-3976003
[7] Greenpeace France, 14-10-2025: Mikhaïl Dudin, SPb → Duinkerken, 12 vaten, bestemming Romans of Lingen. https://www.greenpeace.fr/espace-presse/nouvelle-livraison-duranium-enrichi-russe-framatome-edf-continuent-de-commercer-avec-la-russie/
[7b] urgewald/AgiEL/Ecodefense-briefing, 25-04-2025: >82 t Russisch uranium naar Duitsland 2024, ≥18 transporten naar ANF sinds 2022. https://www.urgewald.org/sites/default/files/media-files/Lingen-Report.pdf
[8] OpenStreetMap (ODbL), Overpass: `waterway=lock_gate` 451861898/451861900 (Holtenau); NOK-ways 131279453 e.a.; Wikipedia DE Bremer Kreuz 53.0413/8.983. https://www.openstreetmap.org
[9] OSRM (router.project-osrm.org, 2026-10-30): route Burchardkai → Lingen 241,8 km, A7/A261/A1/B72/B213; nearest ≤ 8 m voor de via-punten. http://router.project-osrm.org
[10] Eigen briefs: `uranium-inkai-stpetersburg.md` (SPb-kade), `grafiet-bogala-hauzenberg.md` (Burchardkai), `uranium-stpetersburg-pierrelatte.md` (SPb-zeeknoop 6849, 4,9 km). Eigen MARNET-meting (`hecht_marnet`, knopen 6849/6862/3937/3944). sat_check-beelden in `v2/build-cache/satcheck/`: `sat-uranium-stpetersburg-lingen-fabriek.png`, `-burchardkai.png`, `-holtenau-sluis.png`, `-brunsbuettel-sluis.png`, `-kielerfoerde.png`, `-elbe-brunsbuettel.png`.
[11] Haalbaarheidstoets (bindend, keten-id `uranium-stpetersburg-lingen`): kanaal splitsen, aanloopregel >5 km, Lingen-anker 52.4804/7.3315 — toegepast; sluisanker Holtenau 1,2 km verlegd van 54.3745,10.1535 (bos) naar de OSM-sluispoort.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)
`bash v2/tools/bak_stromen.sh uranium-stpetersburg-lingen` → `v2/data/stroomroute-uranium-stpetersburg-lingen.json` (59,8 KB, versie 2, lonlat, 6 benen, 5 markers, 3.204 punten, totaal 1.852,3 km). Naden 0,000 km behalve de zeesnap bij Burchardkai (1,41 km, < 5 km); markers 0,0 km van de lijn behalve de SPb-kade (4,9 km, zie bevindingen).

| # | modaliteit | km gebakken | km brief | beoordeling |
|---|---|---|---|---|
| b1 | zee (MARNET, doorgetrokken) | 1.428,2 | MARNET 1.428,2 | gelijk; kade snapt op 4,9 km van zeeknoop 6849 (onder de 5 km-aanloopgrens) |
| b2 | zee stippel (haven-aanloop Holtenau) | 16,4 | 16,4 eigen lijn | hier reikt het net niet: sluis 13,5 km van zeeknoop 6862 |
| b3 | zee (Nord-Ostsee-Kanal, OSM, doorgetrokken) | 96,4 | ~98 (Wikipedia) | -1,6%, binnen ±15% |
| b4 | zee stippel (haven-aanloop Brunsbüttel) | 6,1 | 6,1 eigen lijn | hier reikt het net niet: sluis 5,9 km van zeeknoop 3937 |
| b5 | zee (MARNET, doorgetrokken) | 63,8 | MARNET 63,8 | gelijk; Burchardkai-snap 1,41 km |
| b6 | truck (doorgetrokken, aannemelijk: één bron) | 241,4 (wegtool 240,7) | hemelsbreed 209, OSRM-indicatie 242 | geen wegkm gepubliceerd: indicatie, +0,2% tegen OSRM; ±15%-norm niet van toepassing |

**Recept.** b1/b5: `--been` over MARNET (150 resp. 9 punten). b2/b4: de eerder handmatig op Esri z13-z15 gelegde polylijnen `uranium-stpetersburg-lingen-aanloop-holtenau/-brunsbuettel.geojson` (5 resp. 3 punten) als `--stippel-geojson`; geen nieuwe `maak_havenaanloop`-poging (exit 124 in het ontwerp). b3: `uranium-stpetersburg-lingen-rivier-nok.geojson` (maak_rivierbeen, 490 punten) hergebruikt. b6: profiel `uranium-stpetersburg-lingen-hamburg-lingen` (extracts de-hamburg, de-niedersachsen, de-bremen; refs A7/A261/A1/B72/B213; de 6 via-punten uit §4 ongewijzigd; venster 40 km; eindKlassen zonder `service` zoals grafiet-bogala-hauzenberg b3) via `wegscan_puur.py`: via-snaps 0,00-0,03 km, 3 keerlussen van 0,02 km gesnoeid, last mile 1,22 km (tertiary/unclassified), snap Lingen-anker 0,16 km. Slots: weg-slot4, zwaar-slot1.

**Toelichting per stippel/aanloop.** Beide stippels zijn haven-aanlopen tussen een sluis en de dichtstbijzijnde MARNET-zeeknoop (Kieler Förde 16,4 km, Elbe-monding 6,1 km); het kanaal ertussen is gemeten en doorgetrokken. Geen vlucht, geen leiding, geen kopie van een andere stroom. De volgorde van de benen in het json is b1 → b2 → b3 → b4 → b5 → b6.

**Bevindingen (niet dichtgetrokken).**
- SPb-kade-marker staat 4,9 km van de lijn: de kade snapt op 4,9 km van zeeknoop 6849, net onder de aanloopgrens van 5 km (brief: geen aanloop). Zelfde patroon als uranium-stpetersburg-pierrelatte. Centraal te beoordelen of een SPb-aanloop (gedeeld met alle SPb-stromen) gewenst is.
- Naad zee → truck bij Burchardkai 1,41 km (zeesnap); het truckbeen begint op het anker, het anker ligt op een OSM-service-eiland dus de weg snapt 0,62 km verder (anker-verbinding, bekend uit grafiet-bogala-hauzenberg).
- b6 heeft geen gepubliceerde wegkm; 241,4 km komt overeen met de OSRM-indicatie (242), maar de A1-afrit richting B72/B213 is een eigen keuze (bron: na Bremen onbekend).
- toets_knikken: 2 spikes in b6 (88 m bij Burchardkai, 13 m bij Lingen), geen omkeringen of terugloop; toets_rechte_benen meldt niets voor deze stroom.
- Sitelaag `w-framatome-lingen` staat 4,3 km van de fabriek (alleen melden). Routegegevens zijn peiljaar 2016-17; de zending van okt 2025 liep via Duinkerken.

**Lessen.**
- De eerder gelegde tussenbestanden (aanlopen, NOK-lijn) waren compleet en zijn ongewijzigd hergebruikt; alleen profiel, functie en weg-geojson ontbraken.
- Een gelijktijdige edit van een andere agent aan `bak_stromen.sh` gaf aan het eind van de bake een tijdelijke "syntax error near unexpected token" (regel 14356); `bash -n` was daarna schoon en de eigen functie was intact.
