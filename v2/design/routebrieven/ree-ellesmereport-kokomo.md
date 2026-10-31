# Routebrief (licht) · Zeldzame aardmetalen — Less Common Metals Ellesmere Port → Felixstowe → Port Newark → Haynes Kokomo (VS)

**stroom-id:** `ree-ellesmereport-kokomo` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · Less Common Metals Ellesmere Port → Felixstowe → Port Newark → Haynes Kokomo (VS) (lanthaan-nikkellegering, aannemelijk: VK-haven en Kokomo-vestiging zijn aannames)
**Keten in één zin:** Lanthaan-nikkellegeringspoeder (HS 7502.20) van Less Common Metals (LCM, Ellesmere Port, VK) gaat per **truck** (M56, M6, A14) naar Felixstowe, per containerschip over de Noord-Atlantische Oceaan naar Port Newark (NJ) en per **truck** (I-80, I-76, I-71, US-30, I-75, US-33, SR-18) naar de superlegeringsmaker Haynes International in Kokomo (Indiana). Stoppunt aan de fabriekspoort.
**Welke as van het verhaal:** Eindgebruik buiten de magneet: een REE-legering (lanthaan) als legeringstoevoeging voor nikkel-superlegeringen. Volume: **onbekend als jaarcijfer**; ImportGenius telt 9 containers en **42,9 t** legeringspoeder van LCM naar Haynes (lopend totaal, periode niet genoemd), laatste zending 30-07-2026 5,4 t in 56 vaten [1]. Dat is **0,043 kt legering, geen REO**: het lanthaangehalte is onbekend. Ter vergelijking: LCM-groep ca. 2,5 kt metaal/legering per jaar (kt metaal, geen REO) [3].
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** anker = Haynes **Kokomo Manufacturing Facility**, 2000 W Defenbaugh St (40.4691, -86.1594), niet het hoofdkantoor 1020 W Park Ave (2,3 km verder, klein terrein) [2][5]; extract us-west-virginia vervalt; corridor is I-80/I-76/I-71/US-30/I-75/US-33/SR-18 (kortste weg), niet I-70 via Wheeling; ontwerp-schatting 1.250 km vervalt (OSRM 1.145 km). Eindpunt zoals het id belooft (Kokomo).

## 1 · Ketenkaart
```
LCM-legeringsfabriek `ree-lcm-ellesmere` (Ellesmere Port)
  ──(b1 truck · M56 → M6 → A14 · hemelsbreed 324 km, gemeten 412,8 km, LETTERLIJKE KOPIE ree-ellesmereport-sumter b1, aannemelijk)──► Trinity Terminal Felixstowe `ree-felixstowe-trinity`
  ──(b2 zee · Noordzee, Kanaal, Noord-Atlantische Oceaan, The Narrows · 6.028,6 km, aannemelijk)──► Port Newark Container Terminal `ree-newark-ct`
  ──(b3 truck · I-80 → I-76 → I-71 → US-30 → I-75 → US-33 → SR-18 · hemelsbreed 1.014 km, OSRM 1.145 km, gemeten 1.128 km, aannemelijk)──► Haynes Kokomo `ree-haynes-kokomo` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `ree-lcm-ellesmere` → `ree-felixstowe-trinity` | M56, M6, A14 | hemelsbreed 324 km, geen wegkm; kopie gemeten 412,8 (OSRM 414,6) [9] | LETTERLIJKE KOPIE `$BEEN/ree-ellesmereport-sumter-weg-lcm-felixstowe.geojson` (bak_ree_ellesmereport_sumter b1) | nee — *aannemelijk: één bron* (haven) |
| b2 | C | zee | `ree-felixstowe-trinity` → `ree-newark-ct` | Noordzee, Engels Kanaal, Noord-Atlantische Oceaan, The Narrows | 6.028,6 (eigen MARNET-dry-run [11]; snap Felixstowe 4,70 km, Newark 3,58 km) | MARNET | aanloop: nee (beide < 5 km) |
| b3 | D | truck | `ree-newark-ct` → `ree-haynes-kokomo` | I-80 (NJ, PA, OH), I-76, I-71, US-30, I-75, US-33, SR-29, SR-18 | hemelsbreed 1.014 km, geen wegkm; OSRM 1.145 km (indicatie); wegscan 1.128,1 km (-1,5%) [9][10] | maak_stroombeen_weg (profiel `ree-ellesmereport-kokomo-newark-kokomo`; extracts us-new-jersey, us-pennsylvania, us-ohio, us-indiana) | nee — *aannemelijk: Kokomo-vestiging* |

Fase A/E bestaan niet: LCM is de herkomst (geen mijn), E vervalt. D is gebronnen: de importerspagina noemt Haynes als consignee [1]. Letterlijke kopie alleen b1 (zelfde LCM-fabriek en Felixstowe-aanname als `ree-ellesmereport-sumter`); b2 en b3 zijn nieuw (Newark en Kokomo niet eerder gedeeld).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-lcm-ellesmere` | legeringsfabriek (laadplek) | Less Common Metals, North Road, Ellesmere Port | 53.3055, -2.9334 | hergebruik letterlijk uit `ree-ellesmereport-sumter.md` §3 [9] | bron-gelegd (daar z15 gezien: wit-gedekte industriehal aan de Mersey-oever) |
| `ree-felixstowe-trinity` | overslag land → zee (containerterminal) | Trinity Terminal, Port of Felixstowe | 51.9639, 1.2926 | hergebruik letterlijk uit `ree-ellesmereport-sumter.md` §3 [9] | bron-gelegd (daar z15 gezien: containerstapels en portaalkranen; haven voor deze lading = aanname) |
| `ree-newark-ct` | overslag zee → land (containerterminal) | Port Newark Container Terminal, Newark NJ | 40.6873, -74.1499 | hergebruik letterlijk uit `ree-sillamae-newark.md` §3 [12] | bron-gelegd (daar z15 gezien: containerterminal met stapels en kranen op de kadevinger); haven Newark volgens importerspagina [1] |
| `ree-haynes-kokomo` | afnemer / superlegeringsmaker (losplek, stoppunt) | Haynes International, Kokomo Manufacturing Facility, 2000 W Defenbaugh St | 40.4691, -86.1594 | [2][5] adres + Nominatim (huisnummerpunt) | aannemelijk (z15 gezien: industrieel hallencluster met parkeerterreinen direct noord van het punt, ook hallen ten zuiden; geen naam leesbaar, welke hal smelt is onbekend) [14] |

Zeeknopen: Felixstowe snapt op MARNET-knoop 4306 (51.9217, 1.2966, 4,70 km), Newark op 3,58 km (eind 40.7029, -74.1127). Dat zijn knopen, geen ankers. Het hoofdkantoor (OSM-industrieterrein 40.4815, -86.1436) is op z15 bekeken: klein terrein tussen woonwijk en spoor, geen fabriekshallen; daarom NIET gekozen [14].

## 4 · Via-punten (alleen b3; b1 is een kopie, b2 is zee; profiel-coördinaten zijn (lon, lat))
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | I-80/I-280-overgang, Parsippany-regio NJ | 40.8592, -74.3745 | pint de uitgang uit NJ via I-280/I-80 i.p.v. NJ Turnpike/I-78 (OSRM nearest 5,2 m) |
| b3 | 2 | I-80 midden Pennsylvania (Clearfield-regio) | 40.9760, -78.0533 | pint I-80 door centraal PA i.p.v. PA Turnpike I-76 of I-70 (OSRM nearest 2,6 m) |
| b3 | 3 | I-80/I-76-overgang, Youngstown-regio OH | 41.1100, -80.8384 | pint de overstap op I-76 (Ohio Turnpike) i.p.v. I-80 verder (nearest 3,8 m) |
| b3 | 4 | I-76/I-71-overgang, Medina OH | 41.0240, -81.9077 | pint I-71 zuidwaarts richting Mansfield i.p.v. Turnpike-door naar Toledo (nearest 4,4 m) |
| b3 | 5 | US-30 bij Mansfield OH | 40.7739, -82.5610 | pint US-30 westwaarts i.p.v. I-71 naar Columbus/Indianapolis (nearest 2,1 m) |
| b3 | 6 | I-75 tussen Lima en Wapakoneta OH | 40.6771, -84.1304 | pint de overstap op I-75 en US-33 naar Indiana i.p.v. US-30 naar Fort Wayne (nearest 3,1 m) |
| b3 | 7 | SR-18 ten oosten van Kokomo IN | 40.5517, -85.3275 | pint de laatste 77 km op SR-18/US-35 vanuit het oosten (nearest 0,3 m) |
Alle punten liggen buiten stadscentra, op de doorgaande weg. Refs b3: `["I-80","I-76","I-71","US-30","I-75","US-33","SR-29","SR-18"]`. OSRM met alle via-punten 1.159,8 km (direct 1.145,2). Wegscan: ankers 0,05 en 0,02 km van de weg, first mile 2,65 km (service/unclassified), last mile 0,64 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| LCM Ellesmere Port | Less Common Metals (USA Rare Earth) | REE-metalen/legeringen → La-Ni-legeringspoeder (HS 7502.20) | ca. 2.500 t/j totaal alle metalen en legeringen (groepscijfer, geen REO) | [3] |
| Haynes Kokomo | Haynes International (Acerinox) | La-Ni-legering → nikkel-superlegeringsplaat (o.a. alloy 230, nominaal 0,02% lanthaan) | niet gevonden | [2][6][7] |

## 6 · Stoppunt
Fabriekspoort van Haynes in Kokomo: de importerspagina noemt Haynes als consignee [1]; wat er met de legeringen daarna gebeurt valt buiten deze keten (fase E vervalt).

## 7 · Open punten
- **Lanthaangehalte onbekend**: "lanthanum nickel alloy powder" (HS 7502.20) is een nikkellegering; de REE-inhoud is een fractie, geen REO. Marginale REE-lading, daarom geen kt REO opgegeven [1].
- **VK-haven is aanname.** De Haynes-zending noemt geen buitenlandse haven; Felixstowe is overgenomen uit `ree-ellesmereport-sumter`, waar een LCM-B/L Antwerpen noemt. Reserve: Seaforth (26 km van LCM). Newark is wel gebronnen (importerspagina: New York/Newark Area) [1], terminal niet bevestigd.
- **Kokomo is aanname**: Haynes heeft ook Arcadia LA (buis) en Mountain Home NC (draad) [2][6]; de locatiepagina zegt niet welke site smelt; Wikipedia en een Haynes-sheet plaatsen vlakke producten in Kokomo [6][7]. Welke hal de poeder ontvangt is niet gezien.
- **Modaliteit Newark → Kokomo (truck) is afgeleid**; geen bron noemt trein of weg. Geen jaarvolume en geen containerwaarde; 42,9 t is een lopend totaal zonder periode.
- **Wegkilometers zijn indicaties**: hemelsbreed 1.014 km en OSRM 1.145 km; geen operator- of overheidsopgave; de ±15%-toets is indicatie.
- Felixstowe-anker staat 190 m achter de kadekant (site-niveau); airside is niet van toepassing.

## 8 · Bronnen
[1] ImportGenius, Less Common Metals Ltd (supplier) — Haynes International: lanthanum nickel alloy powder HS 7502.20.00, B/L PCXS3EM26070115, aankomst 30-07-2026, 5.395 kg, 56 DRM, herkomst VK; totaal 9 containers 42.859 kg; Haynes-haven New York/Newark Area. https://www.importgenius.com/suppliers/less-common-metals-ltd
[2] Haynes International, Locations — Kokomo Manufacturing Facility 2000 W. Defenbaugh St 46902; hoofdkantoor 1020 W. Park Ave; Wire (Hendersonville NC), Tubular (Arcadia LA). https://www.haynesintl.com/en/about/locations
[3] InvestorNews, "Rare earth metal and alloy capability outside of China in September 2026" — USA Rare Earth: ca. 2.500 t/j metaal-/legeringscapaciteit (groep). https://investornews.com/critical-minerals-rare-earths/rare-earth-metal-and-alloy-capability-outside-of-china-in-september-2026/
[4] USA Rare Earth, bedrijfssite (LCM-overname, Ellesmere Port). https://www.usare.com/
[5] OpenStreetMap (ODbL) via Nominatim — Haynes International landuse=industrial 40.48151, -86.14360 (hoofdkantoor, way 772000390); 2000 W Defenbaugh St 40.46908, -86.15937. https://nominatim.openstreetmap.org
[6] Wikipedia, "Haynes International" — Acerinox-dochter, Kokomo: flat products; Arcadia: tubular; Mountain Home: wire. https://en.wikipedia.org/wiki/Haynes_International
[7] Haynes International, "230 brochure" — alloy 230 nominaal 0,02% lanthaan (via zoekresultaat). https://haynesintl.com/wp-content/uploads/2025/08/230-brochure.pdf
[8] USA Rare Earth / LCM context: zie `ree-ellesmereport-sumter.md` §8 [7][8][10] (10-K, LCM-artikel, OSM-fabriekspunt).
[9] `v2/design/routebrieven/ree-ellesmereport-sumter.md` — b1-kopie (412,8 km), ankers LCM en Felixstowe, OSRM-indicaties.
[10] OSRM (router.project-osrm.org) — Newark → Kokomo 1.145,2 km (I-280, I-80, I-76, I-71, US-30, I-75, US-33, SR-29, SR-67, SR-18); met 7 via-punten 1.159,8 km; alle via-punten binnen 5,2 m van de weg. Wegscan `maak_stroombeen_weg.py`: 1.128,1 km (-1,5%).
[11] Eigen MARNET-dry-run (`hecht_marnet.py route`, scratch): Felixstowe → Newark 6.028,6 km, 78 MARNET-edges, snaps 4,70 en 3,58 km.
[12] `v2/design/routebrieven/ree-sillamae-newark.md` §3 — Newark-anker, z15 gezien.
[13] Haynes alloy-sheets: zoekresultaat "Alloy at Glance 230" — Haynes Kokomo als adres. https://haynesintl.com/wp-content/uploads/2025/08/Alloy-at-Glance-230.pdf
[14] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-ree-ellesmereport-kokomo-haynes.png` (Defenbaugh) en `-haynes-hq.png` (hoofdkantoor), z15, 2026-10-31.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Uitvoer:** `v2/data/stroomroute-ree-ellesmereport-kokomo.json` (342,3 KB, versie 2, punt_formaat lonlat), functie `bak_ree_ellesmereport_kokomo` in `v2/tools/bak_stromen.sh`, profiel `ree-ellesmereport-kokomo-newark-kokomo` in `maak_stroombeen_weg.py`. Totaal **7.569,6 km**, 17.109 punten, 4 markers, 3 benen, geen stippel.

| been | modaliteit | km gebakken | punten | brief | afwijking |
|---|---|---|---|---|---|
| b1 LCM → Felixstowe | truck | 412,8 | 4.142 | hemelsbreed 324, geen wegkm; kopie 412,8 | LETTERLIJKE KOPIE sumter b1 (0,0) |
| b2 Felixstowe → Newark | zee | 6.028,6 | 645 | 6.028,6 (dry-run) | 0,0 |
| b3 Newark → Kokomo | truck | 1.128,2 | 12.322 | hemelsbreed 1.014, OSRM 1.145 | -1,5% (indicatie, geen wegkm) |

**Recept:** b1 = `--been-geojson` op het sumter-bestand; b2 = `--been "zee|…"` kade naar kade (MARNET, 78 edges, snaps 4,70 en 3,58 km, beide onder 5 km dus geen haven-aanloop); b3 = vooraf gescand met `wegscan_puur.py` (profiel hierboven, 4 extracts, 7 via-punten op de doorgaande weg, snaps 0,00-0,21 km) en als `--been-geojson` gebakken. Draaien: `bash v2/tools/bak_stromen.sh ree-ellesmereport-kokomo`.

**Toets:** naden 4,70 km (Felixstowe-zeeknoop 4306) en 3,58 km (Newark-zeeknoop), geen naad > 5 km; b1-b2 en b2-b3 zijn zeesnaps, b1 eindigt op het Felixstowe-anker, b3 begint op het Newark-anker (0,0 km). Alle 4 markers 0,0 km van de lijn. `toets_knikken.py`: 49 knikken >= 60 graden (klaverbladen en afritten, spikes van 6-15 m straal), 0 omkeringen, 0 terugloop; een krappe bocht (R 401 m) bij 40,4804 / -85,6938 (SR-18 oost van Kokomo). Geen stippel, geen aanloop, geen vlucht, geen leiding.

**Lessen / noten:** (1) De wegkm van b3 is een OSRM-indicatie, geen operatoropgave: de -1,5% is geen norm. (2) Haven Felixstowe, Newark-terminal en Kokomo-hal blijven aannames (zie §7), staan in de beennamen. (3) Bij het bakken gaf `bak_stromen.sh` een regel "rokken.: command not found" uit een andere (parallelle) functie rond regel 15110: niet van deze stroom, vermoedelijk een tijdelijk onvolledige edit van een andere agent.
