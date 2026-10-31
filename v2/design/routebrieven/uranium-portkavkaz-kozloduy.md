# Routebrief (licht) · uranium — Port Kavkaz → Varna → Kozloduy (Rusland/Bulgarije)

**stroom-id:** `uranium-portkavkaz-kozloduy` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** de laatste Russische (TVEL) splijtstofzending voor Kozloduy (maart 2025) voer per Russisch ro-ro-veer *Slavyanin* naar het Varna Ferry Complex aan het Beloslav-meer [1][4] (vertrekhaven Port Kavkaz is **aannemelijk**, geen bron noemt hem) en ging in vier "railway containers" naar de centrale [1]; omdat Kozloduy geen spoor heeft rijdt het landbeen als **truck** (aannemelijk). Stoppunt: de reactor.
**Welke as van het verhaal:** de Zwarte-Zee-corridor en het einde van de VVER-lock-in in Bulgarije: TVEL-contract vervroegd beëindigd in 2024, blok 5 draait op Westinghouse-brandstof, blok 6 volgt met Framatome [2]. Volume **≈ 40–50 t U/j** (eigen schatting uit het ketenontwerp voor twee VVER-1000-blokken, geen gepubliceerd cijfer; de zending zelf is niet gekwantificeerd [1]); eenheid t U/j, peiljaar 2025.

## 1 · Ketenkaart
```
Port Kavkaz veerterminal (Kertsj-straat) `u-kavkaz-veer`
  ──(b0 zee, haven-aanloop · stippel · 45,2 km over water, 34,4 km van MARNET)──► zeeknoop 2117 (45.0000, 36.4000)
  ──(b1 zee · Zwarte Zee, aannemelijk: vertrekhaven niet genoemd · MARNET 778,4 km, hemelsbreed 737)──► zeeknoop 9443 (Varna)
  ──(b1s zee, haven-aanloop · stippel · 22,9 km OSM-veerlijn door het Varna-kanaal naar het Beloslav-meer)──►
Varna Ferry Complex `u-varna-veer`
  ──(b2 truck · A2 Hemus → 51 → 5 → 3 → 13 → 11 · hemelsbreed 340 km, geen wegkm; gemeten 391,1 · aannemelijk)──►
Kozloduy kerncentrale `u-kozloduy` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b0 | D | zee | Port Kavkaz-kade → zeeknoop 2117 | Kertsj-straat (Zwarte-Zee-kant, niet de Azov-knoop 2144) | 45,2 (eigen meting) | maak_havenaanloop | **ja — MARNET reikt niet (34,4 km > max-snap 25)** |
| b1 | D | zee | zeeknoop 2117 → zeeknoop 9443 (Varna) | Zwarte Zee, Port Kavkaz–Varna (veerlijn sinds 2009 [7][8]; ±36 uur [7]) | hemelsbreed 737; MARNET 778,4 | MARNET | nee — *aannemelijk: vertrekhaven niet genoemd* |
| b1s | D | zee | zeeknoop 9443 → Varna Ferry Complex | OSM-veerlijn way 167786118 (Chornomorsk–Varna) [10], Varna-kanaal en Beloslav-meer | 22,9 (eigen meting) | OSM-geometrie (21 vertices) | **ja — MARNET en de 1:10M-kust kennen het meer niet (22,5 km)** |
| b2 | D | truck | Varna Ferry Complex → Kozloduy | A2 Hemus → 51 → 5 → 3 → 13 → 11 | hemelsbreed 340 km, geen wegkm; gemeten 391,1 (OSRM-indicatie 389 [11]) | maak_stroombeen_weg (extract bulgarije) | nee — *aannemelijk: bron zegt railway containers, vervoermiddel naar de centrale niet genoemd* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-kavkaz-veer` | laadplek (veer) | Port Kavkaz, kade met spoorbundel aan de Chushka-landtong | 45.3408, 36.6737 | [3] wiki 45.3417, 36.6764 | locatie bron-gelegd (z16 gezien: kade met aangemeerd schip aan een rangeerterrein, graansilo's en tankparken N en Z); **rol als vertrekhaven aannemelijk** — welke kade de veerkade is, is niet aan te wijzen |
| `u-varna-veer` | overslag zee → truck | Varna Ferry Complex, W-oever Beloslav-meer | 43.1870, 27.6763 | [6][7][10] OSM-veerlijn eindigt op 43.18709, 27.67626 | bron-gelegd (z16 gezien: lange veersteiger met aangemeerd schip, wortel met rangeerterrein en betonvlakte) |
| `u-kozloduy` | afnemer / reactor | Kozloduy kerncentrale (blokken 5 en 6) | 43.7461, 23.7706 | [5] wiki 43.74611, 23.77056 | bron-gelegd (z15 gezien: twee reactorgebouwen, machinehallen en koelkanaal, koeltorens ontbreken; wegbeen snapt 0,08 km) |

## 4 · Via-punten (alleen b2; op de doorgaande weg, geen stadscentra)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b2 | 0 | weg 9004 bij de afslag van het veercomplex (**routeanker**) | 43.1847, 27.6787 | de terminalstubs zijn access=no en hangen los van het net; veeranker `u-varna-veer` blijft de marker (0,33 km) |
| b2 | 1 | A2 Hemus west van Varna | 43.2542, 27.4484 | pint de A2 i.p.v. de oude weg 2 |
| b2 | 2 | weg 51 tussen Shumen en Targovishte | 43.3976, 26.7773 | corridorkeuze Shumen → Targovishte → Byala (OSRM) i.p.v. Veliko Tarnovo |
| b2 | 3 | weg 51 tussen Targovishte en Popovo | 43.3320, 26.4331 | houdt de noordelijke tak aan |
| b2 | 4 | weg 5 bij Byala (Jantra-oversteek) | 43.4663, 25.7272 | enige oversteek van de Jantra op deze corridor |
| b2 | 5 | weg 3 ten oosten van Pleven | 43.4188, 24.7846 | doorgaande weg 3 naar Pleven |
| b2 | 6 | aansluiting weg 3/13 ten westen van Pleven | 43.4169, 24.4409 | overgang naar weg 13 richting Kozloduy |
| b2 | 7 | weg 13 richting Kozloduy | 43.4888, 24.0911 | houdt weg 13 aan |
| b2 | 8 | weg 11 naderend Kozloduy | 43.6909, 23.8424 | laatste doorgaande weg; eindanker `u-kozloduy` 11,8 km verder (snap 0,08 km) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kozloduy (2 × VVER-1000, blokken 5 en 6) | Kozloduy NPP | verse splijtstof → ≈ 2.000 MWe | 1.003 MWe netto per blok | [2] |

## 6 · Stoppunt
De brief stopt bij de reactor van Kozloduy: de bron noemt de centrale als bestemming [1], maar **de fabriek** en het vertrekpunt van de lading worden niet genoemd, dus fase D begint pas bij de veerhaven. Fase E vervalt (verbruik in de reactor).

## 7 · Open punten
- **Vertrekhaven niet genoemd:** NEI en Ports Europe noemen alleen het veer *Slavyanin* en aankomst in Varna [1][4]. Port Kavkaz is afgeleid uit de bekende veerlijn Kavkaz–Varna [7][8] en uit het feit dat *Slavyanin* een Kavkaz-spoorveer is [3]. Eenbronsketen (NEI); herkomst via Rusland, Oekraïne of Moldavië niet uit te sluiten.
- **Vervoermiddel naar de centrale niet genoemd:** de bron zegt "railway containers" [1]; OSM kent bij Kozloduy geen spoor (bbox-controle 2026-10-31, alleen weg 11) en de dichtstbijzijnde spoorknoop ligt in Roemenië (haalbaarheidstoets). Truck is daarom een aanname; een spoorbeen was niet maakbaar.
- **Peiljaar 2025:** *Slavyanin* werd in juli 2024 beschadigd [9] en volgens Wikipedia in april 2026 vernietigd [3]; de lijn bestaat op deze manier niet meer. De zending van maart 2025 was de laatste; de Russische brandstof dient als reserve [1].
- **Kavkaz-kade:** welke kade de veerkade is, is niet aan te wijzen (rangeerterrein, graan- en olieterminal liggen naast elkaar); anker staat op het veerachtige ligplaatspunt, niet pandniveau.
- **Wegkm:** geen gepubliceerde wegkilometer; de ±15%-toets geldt alleen als indicatie (391,1 gemeten tegen OSRM 389).
- **Volume:** geen gepubliceerde hoeveelheid; 40–50 t U/j is een schatting. Eerste Westinghouse-lading in blok 5: 43 assemblages (mei 2024) [2].

## 8 · Bronnen
[1] NEI Magazine, 2025-04-08 — "Last Russian fuel delivered to Kozloduy": veer *Slavyanin* onder Russische vlag, Ferry Complex Varna, vier railway containers, TVEL-contract vervroegd beëindigd: https://neimagazine.com/?p=94348
[2] WNA, Bulgaria — Westinghouse (blok 5, 10 jaar, 43 assemblages mei 2024), Framatome (blok 6, 2025-2034), VVER V-320, 1003 MWe netto: https://world-nuclear.org/information-library/country-profiles/countries-a-f/bulgaria
[3] Wikipedia, Port Kavkaz — 45°20'30"N 36°40'35"E, oostelijke veerterminal naar Krim, *Slavyanin* laatste spoorveer: https://en.wikipedia.org/wiki/Port_Kavkaz
[4] Ports Europe, 2025-04-22 — laatste Russische nucleaire brandstof voor Kozloduy met ro-ro *Slavyanin* in Varna (paywall, alleen aanhef gelezen): https://www.portseurope.com/last-russian-nuclear-fuel-for-bulgarias-npp-delivered-in-varna-port/
[5] Wikipedia, Kozloduy Nuclear Power Plant — 43°44'46"N 23°46'14"E, blok 5 en 6 VVER-1000: https://en.wikipedia.org/wiki/Kozloduy_Nuclear_Power_Plant
[6] Wikipedia, Port of Varna — Railroad Ferry Terminal aan de zuidoever van het Beloslav-meer: https://en.wikipedia.org/wiki/Port_of_Varna
[7] Chimimport, Varnaferry — terminal W-kust Beloslav-meer, lijn naar Port Kavkaz sinds 3-3-2009, ±36 uur, spoorwijdtewissel: https://www.chimimport.bg/en/sektori/transporten/voden/varnaferi-ood
[8] Kavkaz-Uzel, 2009 — veerlijn Kavkaz–Varna geopend 28-2-2009: https://amp.eng.kavkaz-uzel.eu/articles/9475
[9] Euromaidan Press, 2024-07-23 — *Slavyanin* zwaar beschadigd in Port Kavkaz: https://euromaidanpress.com/2024/07/23/ukrainian-military-severely-damage-russian-ferry-slavyanin-in-kavkaz-port/
[10] OpenStreetMap API — way 167786118 (route=ferry, Chornomorsk – Varna), eindpunt 43.18709, 27.67626 (ODbL): https://www.openstreetmap.org/way/167786118
[11] OSRM publieke demo — route Varna-veer → Kozloduy 388,9 km (indicatie): https://router.project-osrm.org/
[12] Eigen OSM-wegscan Geofabrik bulgarije (maak_stroombeen_weg.py), OSM bbox-controle spoor bij Kozloduy 2026-10-31; haalbaarheidstoets keten-id (Overpass: geen spoor).
Satellietblik (Esri z15–z16, 2026-10-31): `v2/build-cache/satcheck/sat-uranium-portkavkaz-kozloduy-{kavkaz,kavkaz-z16,varna,varna-z16,kozloduy}.png`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
`bash v2/tools/bak_stromen.sh uranium-portkavkaz-kozloduy` → `v2/data/stroomroute-uranium-portkavkaz-kozloduy.json` (65,5 KB, versie 2, lonlat), functie `bak_uranium_portkavkaz_kozloduy`, profiel `uranium-portkavkaz-kozloduy-varna-kozloduy` (extract bulgarije).

| # | modaliteit | km | punten | stippel | naad naar vorig been |
|---|---|---|---|---|---|
| b0 | zee, haven-aanloop Port Kavkaz | 45,2 | 69 | ja | 0 |
| b1 | zee, MARNET 2117 → 9443 | 778,4 | 82 | nee | 0,00 |
| b1s | zee, haven-aanloop Varna (OSM-veerlijn) | 22,9 | 21 | ja | 1,26 |
| b2 | truck, Varna-veer → Kozloduy | 391,2 | 3.175 | nee | 0,33 |

Totaal 1.237,7 km, 3.347 punten, 3 markers (Kavkaz 0,00 · Varna 0,01 · Kozloduy 0,00 km van de lijn).

- **Weg:** 391,2 km tegen OSRM-indicatie 389 (+0,6%); een gepubliceerde wegkm bestaat niet, dus indicatie en geen norm. Routeanker op weg 9004 (0,33 km van het veeranker, de terminalstubs zijn access=no): de naad van 0,33 km is dat procesgat. `toets_knikken`: 23 knikken, 0 omkeringen, 0 terugloop (alle spikes zijn korte rondwegen bij Kozloduy/Varna).
- **Naden:** alle < 5 km. De aanloop Varna begint 1,26 km van zeeknoop 9443 (de OSM-veerlijn vertrekt aan de kanaalmonding, niet op de knoop); blijft staan.
- **Stippels:** b0 (MARNET reikt niet, 34,4 km van knoop 2144 in Azov, aanloop over water door de Kertsj-straat) en b1s (MARNET en 1:10M-kust kennen het Beloslav-meer niet; maak_havenaanloop gaf time-out, terugval op OSM-veerlijn way 167786118).
- **Aannemelijk (beennaam):** b1 (vertrekhaven niet genoemd) en b2 (vervoermiddel naar de centrale niet genoemd). Geen letterlijke kopieen, geen lucht, geen leiding.
- **Lessen:** een ro-ro-veerlijn naar een meerhaven vraagt een OSM-veerlijn als aanloop; `toets_rechte_benen` slaat de stroom niet aan (geen doorgetrokken recht been).
