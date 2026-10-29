# Routebrief (licht) · Uranium · Pinyon Plain Mine → Flagstaff, Kayenta → White Mesa Mill (VS)

**stroom-id:** `uranium-pinyonplain-whitemesa` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) ·
**status:** gebakken (2026-10-29)
**Keten in één zin:** uraniumerts (hoog-grade ondergrondse breccia-pipe, ~1,6% U3O8) van de Pinyon Plain Mine (Energy
Fuels, Kaibab National Forest bij Grand Canyon South Rim) per **truck** over SR-64 zuid, Williams, I-40 naar Flagstaff,
US-89 noord (Cameron, Tuba City), US-160 oost door de Navajo Nation (Kayenta) en US-191 noord (Bluff) naar de White Mesa
Mill bij Blanding, Utah — de enige actieve uraniummolen van de VS; stoppunt.
**Welke as van het verhaal:** Reserve: Colorado Plateau — de Amerikaanse mijnproductie die weer op gang komt, een
ertshaul van ~515 km door Navajo-land. **Jaarvolume: ~590 t U gemijnd in 2025** (1.534.000 lb contained U3O8 uit 47.200
short tons erts, alleen Pinyon Plain; peiljaar 2025) [1]. Eenheid t U/j (1 lb U3O8 = 0,3847 kg U).

## 1 · Ketenkaart
```
Pinyon Plain Mine `u-pinyonplain-mijn` ──(b0 last mile · STIPPEL · 1,35 km bosweg niet in OSM)──►
──(b1 A truck · SR-64 → Williams → I-40 → Flagstaff → US-89 → US-160 → US-191 · 315 mi verhard + 5 mi onverhard
= ~515 km)──► White Mesa Mill `u-whitemesa-molen` (Blanding, UT) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b0 | A | truck | mijn → eerste OSM-wegvertex (35.8913, -112.0853) | bosweg/mijnpad | 1,35 hemelsbreed (gemeten, geen bron) | `--stippel` | ja — last mile (geen net op deze korrel) |
| b1 | A | truck | eerste wegvertex → White Mesa Mill | SR-64 zuid → Williams → I-40 oost → Flagstaff-oost → US-89 noord → US-160 oost → US-191 noord | 515 [1: "315 miles on paved roads and 5 miles on dirt roads" = 320 mi; 4: ~320 mi; 3: ~300 mi] | maak_stroombeen_weg (us-arizona, us-utah) | nee |

Gemeten (profiel uitgevoerd): weggeometrie **528,3 km = +2,6%** op 515 km; eerste 11,8 km over `unclassified` boswegklasse, laatste 1,7 km `service`; plant → weg 1,35 km, weg → kade 0,36 km.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-pinyonplain-mijn` | mijn / laadplek (kop) | Pinyon Plain Mine (voorheen Canyon Mine), Energy Fuels, Coconino County AZ | 35.8831, -112.0963 | [1][8] | bron-gelegd (z15 gezien: kaal geveegd mijnerf van ~14-17 acres met gebouwen, schachtpad en een groene waterpoel in dicht pinyon-jeneverbos; een onverharde weg loopt zuidoostwaarts). 10-K geeft 35°52'58,65" N 112°5'47,05" W = 35.8830, -112.0964, binnen 0,02 km. |
| `u-whitemesa-molen` | uraniummolen (U3O8), stoppunt | White Mesa Mill, Energy Fuels, Blanding UT | 37.5323, -109.5098 | [9][10] | bron-gelegd (letterlijk hergebruikt uit `ree-georgia-whitemesa` / `w-whitemesa`; z15 gezien: molengebouwen NO, twee gelijnde tailingcellen, groot ontruimd erts-/stapelterrein, US-191 op ~1,4 km oost) |

## 4 · Via-punten (b1)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Williams, AZ (SR-64/I-40) | 35.2430, -112.1925 | pint de westelijke keuze: SR-64 zuid naar I-40 (KNAU [5] noemt Williams) i.p.v. US-180 via Valle direct naar Flagstaff; snap 0,64 km |
| b1 | 2 | Flagstaff-oost (I-40/US-89) | 35.2158, -111.5391 | I-40 door/langs Flagstaff [4], daarna US-89 noord; snap 0,19 km |
| b1 | 3 | Tuba City, AZ (US-89/US-160) | 36.1190, -111.2410 | US-89 over Cameron naar US-160 oost [3][4]; snap 0,79 km |
| b1 | 4 | Kayenta, AZ (US-160) | 36.7116, -110.2536 | US-160 door de Navajo Nation [3]; snap 0,31 km |
| b1 | 5 | Mexican Water, AZ (US-160/US-191) | 36.9520, -109.5300 | knoop waar US-191 noordwaarts Utah in gaat [4]; snap 0,58 km |
| b1 | 6 | Bluff, UT (US-191) | 37.2840, -109.5520 | US-191 noord naar Blanding; snap 0,11 km |
Refs: AZ-64, I-40, US-89, US-160, US-191. Extracts: us-arizona, us-utah. Alle snaps < 1 km, nergens > 5 km.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Pinyon Plain Mine | Energy Fuels | ondergronds erts → ertsstapel → trucks | 2025: 47.200 short ton, 1.534.000 lb contained U3O8 (~590 t U); reserve 1,6 Mlb [2]; 60 man [2] | [1][2] |
| White Mesa Mill | Energy Fuels | erts → U3O8 (yellowcake); ook V2O5 en REE | vergund 2.000 short ton erts/dag en >8 Mlb U3O8/j; 2025 geproduceerd ~1.015.000 lb finished U3O8 | [1][3] |

## 6 · Stoppunt
De brief stopt bij White Mesa Mill: Energy Fuels noemt zes langlopende contracten met Amerikaanse utilities [1], maar geen bron
legt de yellowcake van déze mijn bij een benoemde conversiefabriek; fase D en E vervallen.

## 7 · Open punten
- **Pinyon Plain is geen sitelaag-site:** `uranium-sitelaag.json` heeft noch Pinyon Plain noch White Mesa (alleen `w-whitemesa` in `ree-sitelaag.json`, REE-rol). Voorstel centraal: mijn (~590 t U, 2025) en molen (vergund >8 Mlb U3O8/j) toevoegen; niet door mij gewijzigd.
- **Eerste 1,35 km (mijn → OSM-weg) is stippel:** de bosweg staat niet als gekarteerde weg (`track` komt niet door de scanner); de 10-K noemt ~5 mi onverharde weg, de scan 11,8 km unclassified.
- **Ertshaul in 2024 gepauzeerd, sinds feb 2025 hervat** (afspraak met Navajo Nation 29 jan 2025; 2 trucks/dag, verwacht 10/dag) [4][5]; trucks/dag lopen uiteen (6–8 [3], tot 10 [4]) — niet getekend, geen volume op de lijn.
- **Gedeelde corridor:** `ree-georgia-whitemesa` rijdt dezelfde US-160/US-191-stukken (Kayenta, Mexican Water, Bluff delen dezelfde via-punten); eigen been, geen letterlijke kopie omdat de uiteinden verschillen.
- **Pinyon-only 2025-cijfer komt uit één tabel van de 10-K [1];** 2026-cijfers (guidance 2,0–2,5 Mlb voor drie mijnen) niet per mijn gesplitst. Peil 2025.
- **Vervolgleg niet getekend** (Colorado-extract ontbreekt, afnemer onbekend).

## 8 · Bronnen
[1] Energy Fuels Inc., Form 10-K FY2025 (SEC): mijncoördinaat, "315 miles on paved roads and 5 miles on dirt roads", Pinyon Plain extractie 2025, molencapaciteit. https://www.sec.gov/Archives/edgar/data/1385849/000138584926000009/efr-20251231.htm
[2] Energy Fuels, Pinyon Plain Mine (fully permitted, operating, ore shipping to White Mesa; reserve 1,6 Mlb; 60 man). https://www.energyfuels.com/pinyon-plain
[3] KJZZ, "Along a 300-mile hauling route, Navajo uranium concerns collide with U.S. clean energy agenda", 2024-06-28. https://www.kjzz.org/news/2024-06-28/along-a-300-mile-hauling-route-navajo-uranium-concerns-collide-with-u-s-clean-energy-agenda
[4] High Country News, ertshaul-route SR-64, I-40 Flagstaff, US-89, US-160, US-191, ~320 mi, tot 10 trucks/dag, 2025. https://www.hcn.org/?p=331435
[5] KNAU, "Uranium ore hauling resumes in northern Arizona", 2025-02-12. https://www.knau.org/knau-and-arizona-news/2025-02-12/uranium-ore-hauling-resumes-in-northern-arizona
[6] Wikipedia, "Energy Fuels Inc." (Pinyon Plain, Navajo-afspraak jan 2025, White Mesa Mill Blanding). https://en.wikipedia.org/wiki/Energy_Fuels_Inc.
[7] Zoekresultaat (niet gelezen): Environment America, "Where does the uranium from Pinyon Plain mine get hauled?" — 300-320 mi, 6-10 trucks/dag. https://environmentamerica.org/arizona/articles/where-does-the-uranium-from-pinyon-plain-mine-get-hauled/
[8] Esri World Imagery z15 via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-uranium-pinyonplain-whitemesa-mijn.png`.
[9] Esri World Imagery z15 via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-uranium-pinyonplain-whitemesa-molen.png`.
[10] `v2/design/routebrieven/ree-georgia-whitemesa.md` §3 en `v2/design/ree-sitelaag.json` (`w-whitemesa`, 37.5323, -109.5098).
[11] Console `maak_stroombeen_weg.py --profiel uranium-pinyonplain-whitemesa` (2026-10-29): 528,3 km, snaps, first/last mile.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
**Bestand:** `v2/data/stroomroute-uranium-pinyonplain-whitemesa.json` (71,4 KB, versie 2, punt_formaat lonlat), 2 benen, 2 markers, totaal 530,0 km.
**Recept:** functie `bak_uranium_pinyonplain_whitemesa()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh uranium-pinyonplain-whitemesa`); weggeometrie uit profiel `uranium-pinyonplain-whitemesa` in `maak_stroombeen_weg.py` (wegscan, extracts us-arizona + us-utah), ankerpunt afgeknipt tot `uranium-pinyonplain-whitemesa-weg-net.geojson`.

| # | modaliteit | been | km gemeten | km brief | stijl |
|---|---|---|---|---|---|
| b0 | truck | last mile mijn Pinyon Plain, 35.8831,-112.0963 naar 35.8913,-112.0853 | 1,3 | 1,35 hemelsbreed | STIPPEL (geen net op deze korrel, bosweg niet in OSM) |
| b1 | truck | SR-64, Williams, I-40, Flagstaff, US-89, US-160, US-191 naar White Mesa Mill | 528,7 (3.314 punten) | 515 (10-K, 320 mi) | doorgetrokken |

**Toets:** b1 528,7 km tegen 515 = +2,7% (binnen ±15%, echte wegkm uit de 10-K). Naad b0 naar b1 0,006 km. Beide markers liggen op de lijn (0,0 km). `toets_knikken`: 0 omkeringen, 0 terugloop; 13 spikes en enkele krappe bochten van 60 gr of meer, vrijwel allemaal OSM-geometrie in de molenzone (service-wegen) en bij Flagstaff, geen reparatie nodig. Geen zee, haven-aanloop, lucht, leiding of letterlijke kopie.
**Toelichting stippel:** alleen b0 (eerste 1,35 km bosweg van mijn naar de eerste OSM-wegvertex); `track` komt de scanner niet door. Het wegbeen levert zelf nog 11,8 km `unclassified` boswegklasse aan het begin.
**Lessen:** (1) een anker dat 1,35 km van het net ligt: het eerste punt van het wegbeen afknippen en als stippel last mile tekenen, zodat de naad klopt en de doorgetrokken lijn alleen gemeten OSM is; (2) bash v2/tools/bak_stromen.sh kan een syntaxfout melden als een andere agent tegelijk een functie in hetzelfde bestand schrijft; de eigen bake loopt dan al door, controleer met `bash -n`.
