# Routebrief (licht) · Uranium · Kayelekera → Zambia → Walvis Bay → Hamburg → Orano Malvési (Malawi → Frankrijk)

**stroom-id:** `uranium-kayelekera-malvesi` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) ·
**status:** gebakken
**Keten in één zin:** Malawisch yellowcake (U₃O₈ in 4 containers, eerste zending ≈ 145.000 lb ≈ 56 t U, wegtransport vanaf eind okt 2026, scheepsboeking nov 2026) gaat per **truck** van de Kayelekera-fabriek (Lotus Resources 85%) via Zambia en de Sesheke-brug naar NamPort Walvis Bay, per **zeeschip** naar Europa en per **trein** naar Orano Malvési (Narbonne) — **aannemelijk: bronnen noemen alleen "via Zambia, Walvis Bay, dan Orano CE in Frankrijk"; Hamburg en de spoorroute zijn analogie met `uranium-walvisbay-malvesi`** [1][2][3].
**Welke as van het verhaal:** *Malawi naar de Franse conversie.* Doel 2,4 Mlb U₃O₈/j ≈ **923 t U/j** (steady state, eind 2026, nog niet bereikt) [3]; Q2 2026 155,9 klb (≈ 60 t U), piekmaand mei 73,6 klb [3]; eerste zending 145 klb ≈ 56 t U [1]. Orano CE accepteert het product op zijn Malvési-lijn (1 apr 2026) [2].

## 1 · Ketenkaart
```
Kayelekera-fabriek `u-kayelekera-fabriek` ──(b1 truck · M26 → Chitipa → grens → T2 Isoka/Mpika/Kapiri Mposhi/Lusaka → M10 Livingstone → Sesheke-brug · 1.772,9 km gemeten)──►
  Sesheke-brugkop ──(b2 truck · Katima Mulilo → B8 → Rundu → Otavi → Otjiwarongo → Okahandja → B2 Karibib/Swakopmund · 1.481,3 km)──► NamPort Walvis Bay `u-walvisbay-haven`
  ──(b3a zee haven-aanloop 12,5 km, stippel)──► MARNET-zeeknoop 8084 ──(b3b zee · 10.965,5 km, letterlijke kopie)──► Hamburg Süd-West `u-hamburg-steinweg`
  ──(b4 spoor · 9 geojsons letterlijke kopie · ~1.749 km)──► Orano Malvési `u-malvesi` ── stoppunt
```
**Afwijkingen t.o.v. het ontwerp:** (a) laadanker = de fabriek (-9.9955, 33.7002), niet het Wikipedia-punt (de put, 300 m NW); (b) twee truckprofielen, gesplitst op de brugkop zodat de naad 0 is; (c) de lijn passeert Lusaka-centrum op de T2 (geen via-punt daar, de router kiest de Great North Road); (d) de grens bij Chitipa wordt door de router gekozen, niet via Nakonde (43 km ernaast).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `u-kayelekera-fabriek` → Sesheke-brugkop | mijnweg → M26 → Chitipa → grens → T2 (Isoka, Mpika, Kapiri Mposhi, Lusaka, Kafue) → M10 (Livingstone) → Sesheke — **aannemelijk: bron noemt alleen "via Zambia" [1]** | **geen gepubliceerde wegkm**; hemelsbreed 1.316 km; OSRM-indicatie 1.777; gemeten 1.772,9 (−0,2%, indicatie) | maak_stroombeen_weg, profiel `…-fabriek-sesheke` (malawi + zambia) | nee |
| b2 | A | truck | Sesheke-brugkop → `u-walvisbay-haven` | Katima Mulilo → B8 (Trans-Caprivi) → Rundu → Otavi (B1) → Otjiwarongo → Okahandja → B2 Karibib → Swakopmund → Walvis Bay — **aannemelijk** | **geen gepubliceerde wegkm**; OSRM-indicatie 1.497; gemeten 1.481,3 (−1,1%, indicatie); b1+b2 = 3.254; hemelsbreed fabriek–Walvis Bay 2.499 | profiel `…-sesheke-walvisbay` (namibie + zambia) | nee |
| b3a | B | zee | `u-walvisbay-haven` → zeeknoop 8084 (-22.8344, 14.4759) | haven-aanloop over de baai | 12,5 (MARNET-snap) | rechte stippel, **letterlijke kopie** van `bak_uranium_walvisbay_malvesi` | ja — het net reikt niet tot de kade |
| b3b | B | zee | `u-walvisbay-haven` → `u-hamburg-steinweg` | Atlantisch → Kanaal → Noordzee → Elbe — **aannemelijk: aankomsthaven Lotus niet genoemd, Hamburg is analogie** | 10.965,5 (MARNET, bestaand) | MARNET `--been zee`, **letterlijke kopie** | nee — Hamburg snap 4,14 km (< 5 km) |
| b4 | C | spoor (aannemelijk) | `u-hamburg-steinweg` → `u-malvesi` | Rollbahn Bohmte–Hamm–Köln–Koblenz–Mosel–Metz–Dijon–Miramas–Narbonne | geen spoorkm gepubliceerd; gemeten 1.748,6 | **letterlijke kopie** van de 9 spoorbenen (8 + Malvési-aftakking) uit `uranium-walvisbay-malvesi` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-kayelekera-fabriek` | laadplek (fabriek) | Kayelekera uraniumfabriek, Karonga-district (Lotus 85%, Malawi-overheid 15%) | -9.9955, 33.7002 | [4] (put op -9.9928, 33.6981; fabriek 300 m ZO) [sat] | bron-gelegd (z15 gezien: dagbouw NW, daarnaast verwerkingsterrein met gebouwen en tanks, tailingsdam met groen water direct oost; kruis staat op het fabrieksterrein) |
| `u-walvisbay-haven` | overslag weg → zee | NamPort containerterminal, Walvis Bay | -22.9465, 14.4840 | letterlijk uit `uranium-rossing-walvisbay` §3 / `uranium-walvisbay-malvesi` §3 [8] | bron-gelegd (daar z16 gezien: containerterminal met stapels en kade) |
| `u-hamburg-steinweg` | overslag zee → spoor | C. Steinweg Süd-West-Terminal, Hamburg | 53.5335, 9.9868 | letterlijk uit `uranium-walvisbay-malvesi` §3 [8] | aannemelijk als bestemming voor déze lading (daar z15 gezien; Lotus noemt geen Europese haven) |
| `u-malvesi` | conversie, stoppunt | Orano Malvési (Comurhex I), Narbonne | 43.2074, 2.9812 | [2] (Orano CE-acceptatie op Malvési); letterlijk uit `uranium-walvisbay-malvesi` §3 / `w-malvesi` | bron-gelegd (daar z15 gezien: industrieel complex, verdampingsbekkens NNO) |

## 4 · Via-punten (b1 en b2; allemaal OP de doorgaande weg, geen stadscentrum)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | mijnweg op M26 | -9.9280, 33.6538 | toegang Kayelekera–Karonga–Chitipa-weg, ~8 km N van de fabriek [5] |
| b1 | 2 | M26/M14 bij Chitipa | -9.6927, 33.2303 | corridor noord via Chitipa (niet zuid via Mzuzu–Lilongwe–Chipata) |
| b1 | 3 | aansluiting T2 (Zambia) | -9.8200, 32.7595 | pint de Great North Road T2 na de grens ten westen van Chitipa (grenspost niet gepubliceerd; de router passeert Nakonde niet, 43 km ernaast) |
| b1 | 4 | Mpika (T2) | -11.8299, 31.4482 | houdt de lijn op de T2 zuidwaarts |
| b1 | 5 | Kapiri Mposhi (T2) | -13.9671, 28.6764 | T2-knooppunt Kapiri Mposhi: pint de weg naar Lusaka (niet de Copperbelt) |
| b1 | 6 | Kafue (zuid van Lusaka) | -15.7698, 28.1796 | pint Lusaka-doorgang en de weg naar Livingstone |
| b1 | 7 | M10 oost van Livingstone | -17.8036, 25.7075 | pint de Sesheke-weg (M10) i.p.v. Botswana (Kazungula/A33, de kortste OSRM-route) |
| b1/b2 | 8 | Sesheke-brugkop (B8-vertex, Katima Mulilo-zijde) | -17.4785, 24.2470 | forceert de Zambezi-brug (Zambia/Namibië); naad b1 → b2 = 0 [sat: kruis op de B8 bij de brug] |
| b2 | 9 | Rundu | -17.9323, 19.7732 | B8 Trans-Caprivi i.p.v. Botswana-Ghanzi |
| b2 | 10 | Otavi | -19.6442, 17.3483 | B8/B1 (Grootfontein–Otavi) |
| b2 | 11 | Otjiwarongo | -20.4570, 16.6509 | B1 |
| b2 | 12 | Okahandja | -21.9714, 16.9164 | B1/B2 conform ontwerp; C33 via Omaruru is ~55 km korter, niet gekozen |
| b2 | 13 | Karibib | -21.9389, 15.8494 | B2 |
| b2 | 14 | Swakopmund | -22.6745, 14.5804 | B2 kustweg naar Walvis Bay |
Extracts: b1 `malawi` + `zambia`; b2 `namibie` + `zambia`. Refs: M26, M14, T2, T1, M10 / B8, B1, B2.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kayelekera | Lotus Resources (85%) | erts → U₃O₈ | doel 2,4 Mlb/j ≈ 923 t U/j; Q2 2026 155,9 klb (≈ 60 t U) | [3] |
| Orano Malvési | Orano CE | U₃O₈ → UF4 | nameplate ~15.000 t U/j (indicatief, sitelaag `w-malvesi`) | [2][8] |

## 6 · Stoppunt
De brief stopt bij Orano Malvési: Orano CE heeft het Kayelekera-product daar geaccepteerd [2] en de vervolgstap UF4 → Tricastin staat al in `uranium-malvesi-tricastin`. Fase D/E vervallen.

## 7 · Open punten
- **Corridor door Zambia niet gepubliceerd:** bronnen zeggen "via Zambia, Namibië, Walvis Bay" [1][3]; Chitipa → T2 → Sesheke → B8 is router + via-punten (zuidroute Mzuzu–Lilongwe–Chipata en de Botswana-route via Kazungula zijn niet gekozen). Beennaam: aannemelijk.
- **Aankomsthaven Europa en spoor niet gepubliceerd:** alleen "Orano CE in Frankrijk"; Hamburg en de 9 spoorbenen zijn analogie met `uranium-walvisbay-malvesi` (activistenbronnen). Een ander schip kan Fos, Antwerpen of Dunkerque kiezen.
- **Geen gepubliceerde wegkm:** "hemelsbreed 2.499 km, geen wegkm"; OSRM eigen run 3.274 km (1.777 + 1.497), gemeten 3.254 km: de ±15%-toets is een indicatie.
- **Zending nog onderweg:** wegtransport vanaf ~26 okt 2026, scheepsboeking nov 2026 [1][3]; eerst Dar es Salaam voorkeur, Walvis Bay als alternatief na wegvallen van de Singapore-trans-shipment [2]. Peiljaar 2026, ramp-up (productie gepauzeerd in juni, herstart aug 2026) [3].
- **Lusaka-centrum:** de gemeten lijn gaat door Lusaka (T2); een omleiding rond de stad is niet als via-punt gelegd (geen bron of coördinaat gevonden).
- **Fabriek niet in sitelaag:** `uranium-sitelaag.json` mist Kayelekera (centraal toevoegen, rol mijn+fabriek).
- **Bestandsgrootte:** de bake is 597 KB (23.100 weg-punten); centraal beoordelen (golf 13 vlagde 484 KB).
- **Overlap:** 80% letterlijke kopie (zee + spoor); uniek is het truckbeen door drie landen; het Rossing-profiel deelt alleen de laatste ~100 km B2.

## 8 · Bronnen
[1] Inspenet, "Lotus Resources obtains permit to export uranium" (NRPA, 145.000 lb in 4 containers, via Zambia naar Walvis Bay, Orano CE; weg vanaf week na 26 okt 2026, schip nov) https://inspenet.com/en/news/lotus-resources-obt-permit-export-uranium/
[2] Cruxinvestor/Lotus, "Uranium product acceptance from Orano CE's conversion facility" (Malvési, 1 apr 2026; Dar es Salaam voorkeur, Walvis Bay alternatief, Alistair Group, Orano NPS) https://www.cruxinvestor.com/posts/lotus-resources-secures-uranium-product-acceptance-from-oranos-conversion-facility-ahead-of-first-shipment
[3] Mining Weekly via Oilprice, "Lotus secures final permit for first Kayelekera uranium shipment" (26 okt 2026; 2,4 Mlb/j target, 155,9 klb Q2) https://oilprice.com/Company-News/Lotus-Secures-Final-Permit-for-First-Kayelekera-Uranium-Shipment.amp.html (origineel https://www.miningweekly.com/article/lotus-secures-export-permits-for-malawi-project-2026-10-26, 403)
[4] Wikipedia, "Kayelekera mine" (9°59′34″S 33°41′53″E, Lotus 85%, export via Walvis Bay) https://en.wikipedia.org/wiki/Kayelekera_mine
[5] Mining Technology, Kayelekera project (8 km ten zuiden van de Chitipa–Karonga-weg, onverharde weg vanaf Karonga) https://www.mining-technology.com/projects/kayelekerauraniummin/
[6] WNN, "Paladin cleans up after uranium spill" (2014: convooi vrachtwagens naar Walvis Bay) https://world-nuclear-news.org/articles/paladin-cleans-up-after-uranium-spill
[7] OSRM router.project-osrm.org, eigen runs 2026-10-30 (1.776,6 + 1.497,1 km via de via-punten)
[8] `v2/design/routebrieven/uranium-walvisbay-malvesi.md` (Hamburg, Malvési, 9 spoorbenen, aanloop); `uranium-rossing-walvisbay.md` (Walvis Bay-kade)
[sat] Esri World Imagery (`v2/tools/sat_check.py` z15): `v2/build-cache/satcheck/sat-uranium-kayelekera-malvesi-kayelekera-plant.png`, `…-kayelekera-pit.png`, `…-sesheke-brug.png`
[haalbaarheidstoets] Bindend invoerdocument: fabriekanker -9.9955/33.7002, twee profielen, Okahandja-route, OSRM 3.169/3.240 km.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
**Bestand:** `v2/data/stroomroute-uranium-kayelekera-malvesi.json` · versie 2, `lonlat` · 13 benen (waarvan 1 stippel) · 4 markers · **15.981 km** · 597 KB (23.100 weg-punten). **Niet geregistreerd** (centraal). Recept: `bash v2/tools/bak_stromen.sh uranium-kayelekera-malvesi` (functie `bak_uranium_kayelekera_malvesi`, LF).

| # | modaliteit | been | km (gemeten) | wijze |
|---|---|---|---|---|
| b1 | truck | Kayelekera-fabriek → Sesheke-brugkop | 1.772,9 | wegscan_puur, profiel `…-fabriek-sesheke` (malawi + zambia), 7 via-punten + brugkop |
| b2 | truck | Sesheke-brugkop → Walvis Bay-kade | 1.481,5 | profiel `…-sesheke-walvisbay` (namibie + zambia), 6 via-punten |
| b3a | zee, **stippel** | haven-aanloop Walvis Bay → zeeknoop 8084 | 12,5 | letterlijke kopie uit `bak_uranium_walvisbay_malvesi` |
| b3b | zee | Walvis Bay-kade → Hamburg Steinweg | 10.965,5 | MARNET, letterlijke kopie (zelfde punten als in de Walvis Bay-stroom) |
| b4 | spoor | Hamburg → Malvési (9 geojsons) | 1.748,6 | 9 letterlijke kopieen van `spoorroute-uranium-walvisbay-malvesi-*` (alle 9 punt voor punt gelijk aan de bron-stroom) |

**Toets (handleiding §5):** naden 0 m behalve zee → spoor Hamburg **4,17 km** (Hamburg-snap, < 5 km, geen aanloop nodig) · markers 0,0 / 0,0 / 0,11 / 0,11 km van de lijn · modaliteiten {truck, zee, spoor}, elk been >= 2 punten · `toets_rechte_benen`: alleen de stippel-aanloop van 12,5 km (bedoeld).
**Km-toets weg:** er is GEEN gepubliceerde wegkm. Indicatie: gemeten 3.254,4 km tegen OSRM eigen run 3.274 (−0,6%, b1 −0,2%, b2 −1,1%); hemelsbreed fabriek → Walvis Bay 2.499 km. Dit is geen ±15%-toets tegen een bron maar een router-tegen-router-vergelijking.

**Toelichting stippel:** b3a is de enige stippel, "hier reikt het net niet": de NamPort-kade ligt 12,5 km van MARNET-zeeknoop 8084 (> 5 km); `maak_havenaanloop.py` gaf in de Walvis Bay-brief na 300 s een time-out, dus een rechte stippel (geen tweede poging). Er is geen lucht, geen leiding, geen last-mile-been: de fabriek ligt op het weg-anker (-9.9955, 33.7002) en de Walvis Bay-lading eindigt op de kade.
**Aannemelijk (staat in de beennamen):** de corridor door Zambia (bronnen: alleen "via Zambia"), Hamburg als aankomsthaven en de 9 spoorbenen (analogie met `uranium-walvisbay-malvesi`).

**Bevindingen `toets_knikken`:** geen omkeringen in truck of zee. Truck b1 11 en b2 18 *meter-schaal spikes* (R 3-72 m) bij via-punten en kruispunten: brugkop Sesheke (141 gr, R 3 m), Okahandja, Karibib-kruispunt, last mile Walvis Bay (rechte hoeken); geen terugloop, tekenbaar. Zee 1 krappe bocht (62,5 gr, R 9,5 km, Walvis Bay-baai). Spoor: 3 TERUGLOOP-meldingen (R 0-23 m) bij Narbonne (43.187/3.001, 43.195/3.011) in de overgenomen Malvési-aftakking: pre-existent in `uranium-walvisbay-malvesi`, niet hier geintroduceerd.
**Open punten:** Lusaka-centrum op de T2 (omleiding niet gelegd) · bestandsgrootte 597 KB (centraal beoordelen; golf 13 vlagde 484 KB) · Kayelekera ontbreekt in `uranium-sitelaag.json` · zending nog onderweg, peiljaar 2026.
**Lessen:** (1) een via-punt op een brug (Sesheke) geeft een spike van enkele meters; naad 0 tussen twee profielen is het waard. (2) Het wegbeen van 1.773 km door Malawi + Zambia kostte een scan van 24 MB aan pbf-ways; twee profielen met elk hun eigen extract-paar houden de cache klein. (3) Gedeelde zee- en spoorbenen als letterlijke kopie (80% van de lengte) leveren een volledige keten zonder nieuw zoekwerk; de enige echte inspanning is het wegbeen.
