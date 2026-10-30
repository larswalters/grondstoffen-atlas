# Routebrief (licht) · diamant — Lomonosov → Arkhangelsk (ARH) → Moskou (Rusland)

**stroom-id:** `diamant-lomonosov-moskou` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** Ruwe diamant uit de Lomonosov-mijn (Arkhangelskaya-pijp, Severalmaz, Alrosa-dochter) gaat per truck over een secondary-weg en de M-8 naar Talagi Airport (ARH) bij Arkhangelsk en vliegt als vrachtvlucht (grootcirkel) naar Sheremetyevo-Cargo (SVO, Moskou), de verkoopkant van Alrosa (aannemelijk: één bron voor de bestemming, geen bron voor de vlucht).
**Welke as van het verhaal:** *De tweede Russische diamantprovincie — Arkhangelsk naast Jakoetië.* Volume **3,5 Mct/j** (2024 en 2025, Wikipedia [1]; ca. 12% van Alrosa-totaal [6]; vermelde capaciteit 2 Mct staat in strijd met de 3,5 en is niet verklaard [1]). Sitelaag `w-lomonosov` staat op 0,6 Mct en op een verkeerde plek (64.6833, 39.9333, bij Arkhangelsk zelf): centraal corrigeren. Waarde per karaat: niet gevonden. ⚠️ Alrosa stopte Severalmaz van 1 juli 2026 voor 3 maanden [6]; hervatting niet bevestigd.

## BINDENDE aanpassing (haalbaarheidstoets)
b1 eindigt op de laatste openbare weg (M-8-vertex bij Talagi), niet op het airside vrachtplatform; een korte stippel sluit af. Geen via nodig voor de corridor in de toets; de 3 via-punten hieronder houden de corridor vast. b2 is "aannemelijk: geen bron voor de vlucht". Lomonosov-pit-anker (sat bevestigd) hergebruikt als site-anker.

## 1 · Ketenkaart
```
Lomonosov-mijn, Arkhangelskaya-pijp `dia-lomonosov-mijn` ──(b1 truck · GOK-weg → secondary → 11К-723 → 11ПК-744 → М-8 · 101,4 km gemeten)──►
Talagi Airport (ARH), vrachtplatform `dia-arh-vrachtplatform` (b1b stippel: last mile airside, 0,4 km)
──(b2 lucht · vlucht ARH → SVO, grootcirkel, aannemelijk · 975,8 km)──►
Sheremetyevo-Cargo (SVO), Moskou `dia-svo-cargo` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Lomonosov-mijn → M-8 bij Talagi (ARH) | mijnweg (service/unclassified, 5,7 km) → ongenummerde secondary (77 km) → 11К-723 → 11ПК-744 → М-8 [5] | hemelsbreed 79 km, geen wegkm; gemeten 101,4 (indicatie; GIA noemt ca. 110 km mijn–stad Arkhangelsk, geen wegkm naar Talagi [4]) | maak_stroombeen_weg (profiel `diamant-lomonosov-moskou-mijn-arh`, extract rusland-noordwest) | nee |
| b1b | A | truck | M-8-vertex → ARH-vrachtplatform | airside, geen wegpad | 0,38 (hemelsbreed) | `--stippel` | **ja** — airside/privéterrein zonder aansluiting op het openbare net |
| b2 | B | lucht | ARH vrachtplatform → SVO-Cargo | vlucht ARH → SVO (vrachtvlucht, grootcirkel); aannemelijk: geen bron voor de vlucht | 975,8 (berekend, grootcirkel) | maak_luchtbeen | nee — doorgetrokken |

Fase C vervalt (sorteerplek Arkhangelsk niet gevonden, zie §7); D vervalt (Alrosa USO Moskou is de verkoopkant, geen fabriek met adres); E vervalt.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-lomonosov-mijn` | mijn / laadplek | Lomonosov-mijn, Arkhangelskaya-pijp (Severalmaz) | 65.2924, 41.0208 | [1][7][8] | bron-gelegd (z15 gezien: terrasvormige open pit, het kruis ligt in het midden van de put; haulroads en depots rondom; Wikipedia 65.2911, 41.0181 ligt 0,2 km ernaast) |
| `dia-arh-vrachtplatform` | vrachtterminal / vertrek lucht | Talagi Airport (ARH), platform voor het terminalgebouw | 64.5970, 40.7090 | [3][9] | **onzeker** (z15 gezien: verhard platform met ca. 12 toestellen, een lang terminalgebouw aan de zuidrand; een apart vrachtgebouw is niet te onderscheiden; Wikipedia 64.60, 40.717 ligt op de baan) |
| `dia-svo-cargo` | vrachtterminal / aankomst lucht | Sheremetyevo-Cargo, Moskou (**hergebruikt**) | 55.9696, 37.4362 | `diamant-mirny-mumbai.md` [10] | bron-gelegd (overgenomen, niet opnieuw gelegd) |

## 4 · Via-punten (b1, reisvolgorde, vertices OP de doorgaande weg, snap 0 km [7])
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | secondary Lomonosov–Arkhangelsk, midden (km 51) | 64.9112, 41.0312 | houdt de route op de doorgaande secondary (77 km, zonder ref) i.p.v. een zijweg |
| b1 | 2 | begin 11К-723 (km 83) | 64.7159, 40.7631 | overgang naar de genummerde regionale weg vóór de stad |
| b1 | 3 | 11ПК-744 × М-8 (km 98) | 64.6020, 40.6292 | knoop waar de rondweg de M-8 bereikt; Arkhangelsk-centrum blijft ongemoeid |

Segmenten (km): pit → 1 50,2 · → 2 32,7 · → 3 14,4 · → M-8 Talagi 3,6 (som 100,9; plus 0,5 km pit-stub, totaal 101,4). Zonder via-punten gaf de toets dezelfde 100,9 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Lomonosov-mijn (pijpen Arkhangelskaya, Karpinskogo-1) | Severalmaz (Alrosa 99,6%) | erts → ruw; voorsortering in Arkhangelsk tweewekelijks (65–70 kct per partij) | 3,5 Mct/j (2024–2025) | [1][2][4][6] |
| Alrosa USO, Moskou | Alrosa | ruw → verkoop (sanctielijst EU 3-01-2024, VS 24-02-2022) | niet gevonden | [4][5] |

## 6 · Stoppunt
De brief stopt bij Sheremetyevo-Cargo: GIA noemt alleen voorsortering in de stad Arkhangelsk en verzending naar Alrosa USO in Moskou [4]; geen bron noemt een vervolgbeen vanaf SVO (fase D en E vervallen).

## 7 · Open punten
- **Geen bron voor de vervoerswijze Arkhangelsk → Moskou:** GIA noemt alleen verzending [4]; ARH–SVO wordt wel bevlogen door Aeroflot, Rossiya en Smartavia [3], dus een vlucht is mogelijk, maar vracht per weg of per trein is niet uitgesloten. Het been is aannemelijk, niet gebrond.
- **Sorteerlocatie in Arkhangelsk niet gevonden** (Severalmaz-hoofdkantoor ul. Karla Marksa 15 is geen sorteerplek; Kuznechikha-punt ongeverifieerd): de truck eindigt bij de luchthaven, niet bij een sorteerfaciliteit.
- **Vrachtplatform ARH niet te onderscheiden** van het passagiersplatform: anker onzeker, airside-stippel 0,38 km.
- **Wegkm niet gebrond:** alleen hemelsbreed 79 km en GIA ca. 110 km mijn–stad; gemeten 101,4 km is een indicatie (de ±15%-toets geldt niet als norm). Ontwerpref 11K-722 niet teruggevonden; OSM heeft M-8, 11ПК-744 en 11К-723.
- **Mijn tijdelijk stilgelegd** 1 juli 2026 voor 3 maanden [6]; of de productie is hervat staat niet in de bronnen. Een peiljaar-2025-volume geldt als beschrijving van de normale as.
- **Sitelaag `w-lomonosov`:** 0,6 Mct en coördinaat 64.6833, 39.9333 kloppen niet (3,5 Mct; pit 65.2924, 41.0208): centraal corrigeren.
- Alrosa onder sancties (EU, VS) [5]; weinig zendingsdata publiek.

## 8 · Bronnen
[1] en.wikipedia — "Lomonosov diamond mine": 3,5 Mct in 2024 en 2025, capaciteit 2 Mct, reserves 220 Mct, 65.29111/41.01806. https://en.wikipedia.org/wiki/Lomonosov_diamond_mine
[2] en.wikipedia — "Severalmaz": Alrosa 99,6%, Lomonosov-licentie. https://en.wikipedia.org/wiki/Severalmaz
[3] en.wikipedia — "Talagi Airport": 64.60/40.717, baan 2.500 m, vluchten naar SVO (Aeroflot, Rossiya, Smartavia). https://en.wikipedia.org/wiki/Talagi_Airport
[4] GIA Gems and Gemology, zomer 2017 — "Lomonosov deposit": mijn ca. 110 km van Arkhangelsk, tweewekelijkse voorsortering in de stad (65–70 kct), verzending naar Alrosa USO Moskou. https://my.gia.edu/summer-2017-lomonosov-deposit
[5] en.wikipedia — "Alrosa": VS-sancties 24-02-2022, EU 3-01-2024. https://en.wikipedia.org/wiki/Alrosa
[6] The Moscow Times (ru), 2026-06-26 — Alrosa stopt Severalmaz 3 maanden vanaf 1 juli; 3,5 Mct (ca. 12% van Alrosa), pijpen Arkhangelskaya en Karpinskogo-1. https://ru.themoscowtimes.com/2026/06/26/rossiya-ostanavlivaet-krupneishee-mestorozhdenie-almazov-varhangelskoi-oblasti-iz-za-finansovih-problem-alrosi-a199347
[7] OSM (ODbL), Geofabrik `rusland-noordwest`, eigen PBF-scan (`wegscan_puur.py`, profiel `diamant-lomonosov-moskou-mijn-arh`): 101,4 km via secondary, 11К-723, 11ПК-744 en М-8.
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-diamant-lomonosov-moskou-mijn.png`.
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15): `v2/build-cache/satcheck/sat-diamant-lomonosov-moskou-arh-vracht.png`.
[10] `v2/design/routebrieven/diamant-mirny-mumbai.md` (anker `dia-svo-cargo`, Sheremetyevo-Cargo 55.9696/37.4362).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)

**Stroom:** `diamant-lomonosov-moskou` · **bestand:** `v2/data/stroomroute-diamant-lomonosov-moskou.json` (22,8 KB) ·
**recept:** `bak_diamant_lomonosov_moskou()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh diamant-lomonosov-moskou`).

**3 benen · 1.077,6 km · 1.123 punten · 3 markers** — twee doorgetrokken, één stippel:

| # | fase | modaliteit | km | naad met vorig been | stippel? |
|---|---|---|---|---|---|
| b1 | A | truck | 101,4 | (start) | nee |
| b1b | A | truck | 0,4 | 0,000 km | **ja** — ARH-vrachtplatform last mile (airside) |
| b2 | B | lucht | 975,8 | 0,000 km | nee (doorgetrokken; "grootcirkel" en "aannemelijk" in de beennaam) |

**Markers (afstand tot de eigen lijn 0,000 km):** `dia-lomonosov-mijn` 65.2924, 41.0208 (bron-gelegd) · `dia-arh-vrachtplatform` 64.5970, 40.7090 (onzeker) · `dia-svo-cargo` 55.9696, 37.4362 (bron-gelegd, hergebruikt uit diamant-mirny-mumbai).

**Recept b1:** profiel `diamant-lomonosov-moskou-mijn-arh` in `maak_stroombeen_weg.py` (extract rusland-noordwest, 3 via-punten op de doorgaande weg: secondary midden, begin 11K-723, 11PK-744 x M-8), gescand met `wegscan_puur.py`; segmenten 50,2 + 32,7 + 14,4 + 3,6 km, plus 0,5 km pit-stub. Geen via-punt in Arkhangelsk-centrum. Geen omweg-segment.
**b1b stippel:** het vrachtplatform van ARH heeft geen wegpad; b1 eindigt op de laatste openbare weg (M-8, 64.5951, 40.7024), de stippel van 0,379 km sluit af (patroon goud-loulo-ticino).
**b2 vlucht:** `maak_luchtbeen.py`, grootcirkel 975,8 km, 41 punten, doorgetrokken. Aannemelijk: geen bron voor de vervoerswijze Arkhangelsk naar Moskou (zie §7); de aanname staat in de beennaam. Geen km-toets (grootcirkel is de km per definitie).
**Geen** zeebeen, haven-aanloop, leiding, spoor of letterlijke kopie.

**Toets:** b1 101,4 km tegen hemelsbreed 79 km (+28%): buiten de ±15%, maar er is geen gepubliceerde wegkm (GIA noemt ca. 110 km mijn-stad, geen route naar Talagi); gemeten ligt tussen hemelsbreed en de GIA-opgave, dus een indicatie, geen afwijking. Naden 0,000 km (max < 5 km). Markers 0,000 km van hun lijn. `toets_knikken.py`: 8 knikken >= 60 graden (alle R < 70 m, spikes op pit-haulroads, de M-8-knoop en het eindpunt), 0 omkeringen, 0 terugloop. `toets_rechte_benen.py --min-km 5`: de stroom komt er niet in voor. json: versie 2, punt_formaat lonlat, modaliteiten truck/lucht, elk been >= 2 punten.

**Open / bevindingen voor centraal:** sitelaag `w-lomonosov` corrigeren naar 3,5 Mct en 65.2924, 41.0208 (nu 0,6 Mct en 64.6833, 39.9333); mijn tijdelijk stilgelegd 1 juli 2026; ARH-anker onzeker.

**Lessen:** een vooraf gescand wegprofiel plus een vooraf gebakken luchtbeen maakt de bak-functie een kopie-en-plak van drie geojson-regels; de airside-stippel volgt het goud-loulo-ticino-patroon zonder aanpassing.
