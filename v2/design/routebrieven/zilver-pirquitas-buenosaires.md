# Zilver · Pirquitas → Jujuy → Buenos Aires (land)

**stroom-id:** `zilver-pirquitas-buenosaires` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** zilver-loodconcentraat (en zinkconcentraat) van de Pirquitas-verwerkingsfabriek van Puna Operations (SSR Mining, Jujuy; erts van Chinchillas ~42 km per truck) gaat in 1 t big bags op platte trucks via Susques, RN 52 en RN 9 door heel Argentinië naar de exporthaven Buenos Aires (containerkade TRP, aannemelijk) — stoppunt aan de kade, want de smelterklanten zijn niet met naam gepubliceerd.
**Welke as van het verhaal:** de grootste zilvermijn van Argentinië, op 4.100 m in de Puna, exporteert via de Atlantische kant en niet via Chili. Peiljaar 2025: 9.814 koz Ag = 305 t Ag/j (SSR 10-K 2025 [2]); 2024: 10.500 koz = 327 t Ag/j (idem). Eenheid t Ag/j (1 Moz = 31,1 t); dit is zilver in concentraat, verkocht 9.663 koz.

## 1 · Ketenkaart
```
Pirquitas-fabriek `ag-pirquitas-plant`
  ──(b1 truck · RP/Susques → RN 52 → RN 9 (Purmamarca, S.S. de Jujuy, Tucumán, Rosario) → Buenos Aires · ~1.906 km gemeten, geen gepubliceerde totaalkm)──►
Buenos Aires containerkade TRP, Puerto Nuevo `ag-baires-kade` ── stoppunt
(zee, smelter en vervolg: niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (1 t big bags, platte trucks) | `ag-pirquitas-plant` → `ag-baires-kade` (aannemelijk: één bron) | Susques → RN 52 → RN 9 → RN 34/RN 9 zuidwaarts → Rosario → Buenos Aires | gepubliceerd alleen tot Jujuy: 335 km (TRS, vanaf het mijngebied; gemeten 318,5, -4,9%) [1]; totaal Buenos Aires: hemelsbreed 1.540 km, geen wegkm; gemeten 1.906 km | maak_stroombeen_weg (extract argentina), nieuw profiel | nee |

Geen zeebeen (haven aannemelijk in de beennaam). **Cross-grondstof bewust dubbel:** ~94% van de lijn (1.821 van 1.940 km volgens de haalbaarheidstoets) ligt binnen 150 m van `lithium-olaroz-naraha` b1; nieuw is alleen de eerste ~120 km Pirquitas → Susques/RN 52. Geen letterlijke kopie van dat bestand, omdat die lijn de Olaroz-omweg bevat [5].

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-pirquitas-plant` | fabriek / laadplek | Pirquitas-verwerkingsfabriek, Puna Operations, Rinconada, Jujuy (~4.100 m) | -22.6925, -66.4830 | [1] (fabriek in het oostelijk derde van het terrein, centrum -22.70/-66.50) + [4] | bron-gelegd (z17 gezien: brekergebouw en transportbanden naar een koepel- en bolvormige tank, bekken met zwarte vloeistof en groot tailingsveld in het noordoosten; punt staat op het fabrieksplatform. Eerste blik op z16 op -22.6937/-66.4841 ligt 170 m ZW op dezelfde pad) |
| `ag-baires-kade` | overslag (export) | TRP — Terminales Río de la Plata (DP World), Puerto Nuevo, Buenos Aires | -34.5847, -58.3631 | letterlijk hergebruikt uit `lithium-olaroz-naraha` (`li-baires-kade`) [5] | aannemelijk (bron noemt "Rosario of Buenos Aires" en het kostenmodel 100% Buenos Aires, geen terminal; punt zelf bron-gelegd in de lithiumbrief: containerstapels en twee portaalkranen) |

## 4 · Via-punten (b1; letterlijk de vier van `lithium-olaroz-naraha` b1, gecontroleerd op de doorgaande weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Purmamarca (RN 52 → RN 9-knoop) | -23.7466, -65.4992 | de afdaling van de Puna naar de Quebrada; pint RN 52 → RN 9 in plaats van de noordroute via Abra Pampa/RN 9 noord [1][3] |
| b1 | 2 | San Salvador de Jujuy | -24.1853, -65.2995 | RN 9 passeert de provinciehoofdstad; pint de doorgaande route, geen stadsomleiding |
| b1 | 3 | Tucumán (RN 34/RN 9-splitsing) | -26.8241, -65.2226 | corridorkeuze RN 9 of RN 34 zuidwaarts; pint de zuidelijke keuze |
| b1 | 4 | Rosario | -32.9442, -60.6505 | laatste grote knoop vóór Buenos Aires; TRS noemt Rosario als alternatieve haven [1] |

Susques (-23.4167, -66.4833) is bewust geen via-punt: Pirquitas → RN 52 loopt er per constructie langs en het is geen corridorkeuze. Tussen plant en Purmamarca bepaalt de router het pad.

## 5 · Verwerkingsknopen
(geen — de fabriek is zelf het beginpunt; er is geen smelter of fabriek in de keten, zie §6.)

## 6 · Stoppunt
De brief stopt aan de kade van Buenos Aires: de TRS zegt alleen dat de concentraten aan de kade rechtstreeks naar de kopers gaan, met 50% naar China en de rest naar Latijns-Amerika, Europa en Oost-Azië, zonder smelter bij naam [1]. Fase B en verder vervallen daarom, in één zin beargumenteerd.

## 7 · Open punten
- **Haven niet bij naam gebrond:** TRS noemt "Rosario of Buenos Aires", het kostenmodel 100% Buenos Aires [1]; de 10-K zegt alleen "a port" [2]. De terminal TRP is een aanname uit de lithiumketen. Oudere bronnen (Wood Mackenzie, tot ~2018) noemden Antofagasta; de TRS van 2024 is nieuwer en bepaalt de keten.
- **Gepubliceerde totaal-wegkm ontbreekt:** alleen Pirquitas-Jujuy 335 km (TRS) en 293 km Jujuy-Pirquitas via de noordroute RN 9 / RP 7 / RP 70 (CFI) [3]; totaal Buenos Aires is gemeten (1.906 km), niet gepubliceerd, dus de ±15%-toets geldt als indicatie.
- **Twee corridors uit de Puna:** Susques-RN 52 (TRS, zwaar transport) en de noordroute via Abra Pampa/RN 9. We tekenen de eerste; de TRS noemt "Route No. 77", een label dat we in OSM niet kunnen thuisbrengen (de toegangsbeschrijving in [1] noemt voor Susques-Chinchillas RN 40 en RP 70).
- **Levensduur:** met reserves van 4,7 Mt (incl. stockpile) en 5.000 t/d is de fabriek nog ~2,6 jaar vol (eigen berekening op [2]); de lijn blijft hetzelfde getekend zolang Puna draait.
- **Zilverinhoud per concentraat en afnemers niet gepubliceerd** (Ag-gehaltes 4,7–10,8 kg/t volgens CFI) [3].
- **Bestandsgrootte:** het been is ~362 KB (boven de 300 KB-vlag), bekend en niet te verhelpen zonder punten te schrappen.

## 8 · Bronnen
[1] SLR/SSR Mining, Puna Operations S-K 1300 Technical Report Summary (12 feb 2024) — concentraat per truck naar Susques ("Route No. 77"), dan Route 9 naar Rosario of Buenos Aires; Jujuy 335 km; fabriek in oostelijk derde, centrum 22°42'S 66°30'W; trucking 100% naar Buenos Aires, 50% export naar China. https://www.sec.gov/Archives/edgar/data/921638/000094787124000126/ss2975198_ex9604.htm
[2] SSR Mining, Form 10-K FY2025 — Puna: 9.814 koz (2025), 10.500 koz (2024) Ag; 5.000 t/d; concentraten in 1 t bags per truck naar een haven; reserves per 31-12-2025. https://www.sec.gov/Archives/edgar/data/921638/000092163826000035/ssrm-20251231.htm
[3] Consejo Federal de Inversiones, Plan de Logística Minera Oro y Plata, informe final — Pirquitas/Chinchillas 293 km vanaf Jujuy (RN 9, RP 7, RP 70), 315 km elders, 10,5 Moz in 2024, ~42 km Chinchillas-Pirquitas. https://cfi.org.ar/uploads/2026/09/Plan-Logistica-Minera-Oro-y-Plata-Informe-final_252_0.pdf
[4] Esri World Imagery via `v2/tools/sat_check.py` (z16/z17) — `v2/build-cache/satcheck/sat-zilver-pirquitas-buenosaires-planta-z16.png` en `sat-zilver-pirquitas-buenosaires-planta-aanbev.png`.
[5] Eigen routebrief `v2/design/routebrieven/lithium-olaroz-naraha.md` — TRP-kade (bron DP World / OSM), vier via-punten, b1-profiel `lithium-olaroz-naraha-baires`; satellietbeeld `sat-li-olaroz-naraha-baires-trp.png`.
[6] SSR Mining, Our Operations (Pirquitas): erts 40 km per truck naar de verwerking, zilverlood- en zinkconcentraat naar internationale smelters. https://www.ssrmining.com/projects/pirquitas/
[7] Wood Mackenzie, Pirquitas asset report (oudere logistiek via Antofagasta, tot ~2018). https://www.woodmac.com/reports/metals-pirquitas-zinc-mine-16173121/
[8] Haalbaarheidstoets M31 golf 19 (orkestrator) — 1.821 van 1.940 km binnen 150 m van lithium-olaroz-naraha b1; gemeten 1.906 km.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-zilver-pirquitas-buenosaires.json` (305,2 KB, boven de vlag van 300 KB; versie 2, lonlat, 14.319 punten) · functie `bak_zilver_pirquitas_buenosaires` in `bak_stromen.sh` · profiel `zilver-pirquitas-buenosaires-planta-baires` in `maak_stroombeen_weg.py` · tussenuitvoer `v2/build-cache/ais/graaf/zilver-pirquitas-buenosaires-weg-pirquitas-baires.geojson`.

| # | modaliteit | km (gemeten) | brief | stippel |
|---|---|---|---|---|
| b1 | truck, Pirquitas-fabriek → Buenos Aires TRP | 1.906,2 | geen gepubliceerde totaalkm; hemelsbreed 1.540 (+23,8%, indicatie); Jujuy-deel 318,2 tegen 335 (TRS), -5,0% | nee |

Totaal 1.906,2 km, één been, dus geen naden. Markers (2): Pirquitas-fabriek en TRP, allebei 0,0 km van de lijn (plant-snap 0,16 km, kade-snap 0,03 km; weg-kade 0,70 km last mile over een service-weg). Knikken: 102 >= 60 graden, 1 omkering (170,7 graden bij de kade, 16 m, echt), 0 terugloop; toets_rechte_benen: geen treffer.

**Recept.** `wegscan_puur.py --profiel zilver-pirquitas-buenosaires-planta-baires` (extract argentina, corridorKlassen tertiary/unclassified/residential, eindKlassen incl. track, vensterKm 75, 119,4 km first mile over kleine klassen) en daarna `bash v2/tools/bak_stromen.sh zilver-pirquitas-buenosaires`. Via-punten: Susques, Purmamarca, S.S. de Jujuy, Tucuman, Rosario. Geen zeebeen, geen haven-aanloop, geen stippel, geen vlucht, geen leiding.

**⚠ Afwijking van de brief: Susques is WEL een via-punt.** De brief (§4) liet Susques weg met het argument dat Pirquitas → RN 52 er per constructie langs loopt. De eerste scan zonder Susques koos echter de noordroute via Abra Pampa/RN 9 (254,6 km tot Purmamarca, de lijn 59 km van Susques en 8,6 km van Abra Pampa), terwijl de TRS de vrachtwagens expliciet via Susques ("Route No. 77") en daarna Route 9 laat rijden. Purmamarca kan niet onderscheiden tussen aankomst vanuit het westen (RN 52) of het noorden (RN 9), dus Susques is hier een echte corridorkeuze. Met Susques: 119,1 + 134,0 + 65,1 = 318,2 km tot Jujuy (TRS 335 km, -5,0%; zelfde getal als de 318,5 uit de haalbaarheidstoets), totaal 1.906,2 km, bestand 305 KB: dat is ook wat de brief voorspelde.

**⚠ Briefcoordinaat Susques ligt ~12 km te ver westelijk.** Wikipedia geeft -23.4167, -66.4833 (het getal in §4), maar het dorp ligt volgens OSM-Nominatim op -23.3992, -66.3676 (de lijn passeert er op 0,0 km). Met het Wikipedia-punt maakte de router een wegzijtak van 27 km heen en terug die de snoei kapte; het profiel gebruikt nu de OSM-coordinaat (snap 0,00 km). De coordinaat in §4 blijft staan als bron-citaat, niet als routeerpunt.

**Open punten blijven:** haven niet bij naam gebrond (Rosario of Buenos Aires, TRP is aanname), geen gepubliceerde totaalkm, tweede Puna-corridor (noordroute via Abra Pampa, 293 km Jujuy-Chinchillas volgens CFI) niet getekend, afnemers niet gepubliceerd.

**Lessen.** (1) Een via-punt dat alleen een knoop pint kan de corridor aan de bronzijde niet vastleggen: Purmamarca ligt op het kruispunt van twee aanvoerroutes, en zonder Susques gaf de router een plausibele maar andere route. Controleer na elke scan bij een bron-genoemde plaats (hier Susques) hoe ver de lijn er van af ligt. (2) Een Wikipedia-coordinaat voor een dorp kan kilometers afwijken; vergelijk met OSM-Nominatim voordat het een via-punt wordt. (3) 94% overlap met lithium-olaroz-naraha b1 blijft bewust dubbel (Olaroz-omweg).
