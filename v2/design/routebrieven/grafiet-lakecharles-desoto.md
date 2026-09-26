# Routebrief (licht) · grafiet — Lake Charles → Chattanooga → De Soto (VS)

**stroom-id:** `grafiet-lakecharles-desoto` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** premium petroleum-naaldcokes uit de specialty coker/calciner van de Phillips 66 Lake Charles Manufacturing Complex (Westlake, Louisiana) gaat per **truck** (werkaanname) ~1.086 km over I-10/I-12/I-59/I-24 naar de Novonix Riverside-fabriek in Chattanooga (Tennessee), wordt daar bij ~3.000 °C gegrafitiseerd tot synthetisch anodemateriaal (AAM), en rijdt per **truck** (werkaanname) ~1.152 km over I-24/I-57/I-64/I-70/K-10 naar de celfabriek Panasonic Energy Kansas in De Soto — de eerste grafietketen van de atlas zónder zee, en de synthetische tegenhanger van as 2 (Balama → Vidalia → De Soto).
**Welke as van het verhaal:** *de ex-China buildout, synthetisch*. Tegen een VS-import van AAM van 43,4 kt in jan–aug 2025 (China 55 %, Indonesië 31 %, Korea 14 %) [12] bouwt Novonix Riverside (nameplate 20 kt AAM/j [6][7]) met een bindende offtake van Panasonic Energy: **minimaal 10 kt AAM over 2025–2028** voor Panasonics Noord-Amerikaanse fabrieken [1]; PowerCo is de tweede afnemer [7]. **Jaarvolume vandaag: 0 kt AAM/j** (2026: C-monster en eerste full-scale-monster aan Panasonic [8][10]; massaproductie voor Panasonic H2 2027, volle capaciteit uitgesteld naar september 2031 [10]). Eenheid conform ontwerp: kt AAM/j (verwerker); kop-site in kt naaldcokes/j — Lake Charles publiceert die capaciteit niet [3][4]. Feedstock-koppeling: Phillips 66 is 16 %-aandeelhouder [2] en produceert premium naaldcokes uitsluitend in Humber (VK) en Lake Charles [4][5]; het Novonix 20-F FY2025 zegt echter letterlijk *"we may source specialty petroleum needle coke … from Phillips 66 or a select few other suppliers"* — geen supply-overeenkomst, Lake Charles wordt in geen Novonix-stuk genoemd [6]. Beide benen dragen daarom **(aannemelijk: één bron; volume nul tot H2 2027)** in de naam.

## 1 · Ketenkaart
```
P66 Lake Charles, cokesveld/coker `gr-lakecharles-cokes` ──(b1 truck · I-10 → I-12 → I-59 Hattiesburg–Meridian–Birmingham → I-59 → I-24 · ~1.086 km · aannemelijk: één bron)──►
   ═══ knoop: Novonix Riverside `gr-riverside-fabriek` (naaldcokes → 20 kt AAM/j nameplate; 2026: monsters) ═══
   ──(b2 truck · I-24 → Nashville → I-24 → I-57 → I-64 → I-70 → I-435 → K-10 · ~1.152 km · aannemelijk: één bron)──► Panasonic Energy Kansas, De Soto `gr-desoto-fabriek` (routeerpunt Astra Parkway) ⏹ stoppunt
   ├── vertakking (niet getekend): Panasonic Nevada (Sparks) — contract zegt "Nevada and Kansas", aandeel niet gepubliceerd [1]
   └── fase E bestaat al als been 10 van `grafiet-balama-vs` (De Soto → Lucid AMP-1 Casa Grande); niet opnieuw getekend
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (werkaanname; spoor niet uitgesloten, §7) | `gr-lakecharles-cokes` → `gr-riverside-fabriek` | US-90 → I-10 O → I-12 (Baton Rouge–Slidell) → I-59 N (Hattiesburg, Meridian, Birmingham, Fort Payne) → I-24 O → W 19th St/Riverfront Pkwy | 1.086 (OSRM over OSM [15]; geen gepubliceerde lengte — de lengtetoets loopt tegen dezelfde bron als de extract) | maak_stroombeen_weg (profiel `grafiet-lakecharles-riverside`; kop op privé-terreinwegen → `eindToegangPrivaat`) | nee — *aannemelijk: één bron; volume nul tot H2 2027* |
| b2 | D | truck (werkaanname; contract noemt alleen "Nevada and Kansas") | `gr-riverside-fabriek` → De Soto routeerpunt 38.94196, -95.00748 | I-24 W (Monteagle, Nashville, Clarksville, Paducah) → I-57 N → I-64 W (St. Louis) → I-70 W (Columbia) → I-435 Z → K-10 W | 1.152 (OSRM [15]; geen publicatie) | maak_stroombeen_weg (profiel `grafiet-riverside-desoto`); eindigt op het bestaande routeerpunt, 443 m vóór het terreinanker (procesgat zoals `grafiet-balama-vs` been 9, niet getekend) | nee — *aannemelijk: één bron; volume nul tot H2 2027* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-lakecharles-cokes` | feedstock / laadplek (cokesveld bij de coker) | Phillips 66 Lake Charles Manufacturing Complex, Westlake LA — coker/cokesopslag | 30.2420, -93.2770 | [3][4][13][14] | bron-gelegd (z15/z16 gezien: zwart cokesveld met de coker-installatie midden in het proceseiland, ~250 m ZO van het OSM-landuse-centrum 30.24195/-93.27438; tankparken oost en west, US-90 en I-10 langs de zuidrand; wélke coke (naald- of brandstofcokes) en welke poort de trucks nemen is op het beeld niet te zien) |
| `gr-riverside-fabriek` | verwerkingsknoop (grafitisatie; los- én laadplek op site-niveau) | Novonix Riverside, 1029 West 19th Street / Riverfront Parkway, Chattanooga TN | 35.0388, -85.3243 | [6][7][13][14] | bron-gelegd (z15 gezien: grote witte fabriekshal (ex-Alstom) op de oostoever van de Tennessee-rivierbocht, Riverfront Parkway erlangs, I-24 700 m oostelijk; laaddock niet apart onderscheiden — site-niveau) |
| `gr-desoto-fabriek` | fabriek (fase D, losplek) | Panasonic Energy Kansas, Astra Enterprise Park, De Soto KS | 38.93815, -95.00240 | [16] | hergebruik uit `grafiet-balama-vidalia.md` (terreinanker; docks niet gelegd — opnamedatum; routeerpunt 38.94196, -95.00748 op de rotonde Astra Parkway) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; alle óp de rijbaan, ná de afslag)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | I-12 oost van Baton Rouge (Walker) | 30.4707, -90.8576 | I-12 (noord om Pontchartrain) i.p.v. I-10 door New Orleans |
| b1 | 2 | I-59 noord van Slidell (Pearl River) | 30.4031, -89.7265 | I-59 naar Hattiesburg i.p.v. I-10 oost naar Mobile → I-65 |
| b1 | 3 | I-59 noord van Hattiesburg | 31.3798, -89.3252 | doorrijden op I-59 i.p.v. US-49 naar Jackson |
| b1 | 4 | I-20/59 oost van Meridian | 32.3964, -88.5772 | I-20/59 samen naar Birmingham i.p.v. I-20 W naar Jackson |
| b1 | 5 | I-59 NO van Birmingham (Trussville) | 33.6342, -86.6237 | I-59 rechtstreeks naar Chattanooga i.p.v. I-65 → Nashville → I-24 |
| b1 | 6 | I-24 Chattanooga, Lookout Valley | 35.0188, -85.3830 | I-24 O de stad in (afrit W 19th St/Riverfront) i.p.v. I-59 → I-75 om de stad heen |
| b2 | 1 | I-24 W bij Kimball/Jasper | 35.0424, -85.6740 | I-24 over Monteagle naar Nashville i.p.v. I-75/US-27 |
| b2 | 2 | I-24 NW Nashville, ná I-65/I-40 | 36.2293, -86.7805 | I-24 naar Clarksville/Paducah i.p.v. I-40 W → Memphis → I-55 |
| b2 | 3 | I-57 N ná het einde van I-24 (Pulleys Mill IL) | 37.6474, -88.9763 | I-57 noord i.p.v. zuid |
| b2 | 4 | I-64 W ná I-57 (Mt Vernon IL) | 38.3621, -89.0286 | I-64 naar St. Louis i.p.v. I-57 door naar Effingham → I-70 |
| b2 | 5 | I-70 W Wentzville MO | 38.8102, -90.8696 | I-70 naar Kansas City i.p.v. I-44 → Springfield |
| b2 | 6 | I-435 Z ná I-70 (Kansas City) | 39.0306, -94.5006 | de I-435-ring i.p.v. I-70 door downtown → I-35 |
| b2 | 7 | K-10 Lenexa, ná I-435 | 38.9423, -94.7779 | letterlijke kopie uit profiel `grafiet-vidalia-desoto` (K-10 W naar De Soto) |
| b2 | 8 | K-10 × Lexington Ave, De Soto | 38.9602, -94.9665 | letterlijke kopie uit profiel `grafiet-vidalia-desoto`; daarna het routeerpunt 38.9420, -95.0075 (rotonde Astra Parkway) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Lake Charles Manufacturing Complex (feedstock) | Phillips 66 | ruwe olie → o.a. groene en gecalcineerde specialty/naaldcokes (specialty coker + calciner) | raffinaderij 264.000 b/d; naaldcokes-capaciteit niet gepubliceerd | [3][4][11] |
| Novonix Riverside, Chattanooga | NOVONIX Anode Materials LLC | naaldcokes → synthetisch grafiet AAM (grafitisatie, 4 ovens geïnstalleerd) | nameplate 20 kt AAM/j (doel); Panasonic ≥ 10 kt over 2025–28 + PowerCo; 2026 monsters, massaproductie H2 2027, volle capaciteit sept 2031 | [1][6][8][10] |
| Panasonic Energy Kansas, De Soto | Panasonic Energy | AAM → 2170-cellen (doel ± 32 GWh/j) | zie `grafiet-balama-vidalia.md`, verwerkingsknoop De Soto | [16] |

## 6 · Stoppunt
De brief stopt aan het De Soto-routeerpunt: fase E (cellen → Lucid AMP-1 Casa Grande) is al gemeten en gebakken als been 10 van `grafiet-balama-vs` en wordt niet als tweede versie getekend; de gloednode De Soto wordt door beide stromen gedeeld.

## 7 · Open punten
- **Feedstock-been is niet gedocumenteerd:** geen supply-overeenkomst Novonix–Phillips 66; het 20-F zegt "may source … from Phillips 66 or a select few other suppliers" [6]. Lake Charles is wel de enige Amerikaanse P66-naaldcokesbron [4][5] — en Epsilon (North Carolina, 2027) hééft een expliciete Lake Charles-overeenkomst [11], Novonix niet.
- **Modaliteit beide benen is een werkaanname:** cokes gaat in de VS vaak per spoorhopper; de raffinaderij ligt aan de UP Lafayette Sub en de CPKC Lake Charles Sub (Rosebluff Industrial Lead het terrein in) [13], Riverside ligt aan spoor langs de rivier. Een spoorbeen zou de héle lijn vervangen — niet getekend zolang er geen bron is.
- **Welke Panasonic-fabriek** (De Soto vs Nevada/Sparks) is nergens gepubliceerd [1]; De Soto is gekozen omdat het anker al ligt.
- **Volume nul:** monsters in 2026, massaproductie voor Panasonic pas H2 2027, ramp-up vertraagd tot 2031 en de landaankoop naast Riverside afgeblazen [8][10]; uitbreiding mogelijk óp Riverside i.p.v. Enterprise South [9].
- **Laadplek Lake Charles:** het cokesveld is op z16 zichtbaar, maar of dat de naaldcokes (calciner) of de brandstofcokes is, en welke poort aan US-90 de trucks nemen, is niet gebrond; OSM-terreinwegen zijn `access=private` (71 ways) [13].
- **Riverside:** los-/laaddock niet aangewezen (site-niveau); **De Soto:** beide docks niet gelegd (opnamedatum, uit [16]).
- **Geen gepubliceerde km** voor beide ritten: de lengtetoets loopt tegen OSRM (1.086 / 1.152 km), dezelfde bron als de extracts.
- **Naaldcokes-volume** (kt in) en het rendement cokes → grafiet bij Riverside zijn niet gepubliceerd; de kop-site krijgt in de sitelaag de rol *feedstock* zonder capaciteit.

## 8 · Bronnen
[1] NOVONIX, "Panasonic Energy and NOVONIX Sign Binding Off-Take Agreement", 2024-02-08 — ≥ 10.000 t AAM 2025–2028 uit Riverside voor Panasonics Noord-Amerikaanse fabrieken; kwalificatiemijlpalen vóór Q4 2025. https://ir.novonixgroup.com/news-releases/news-release-details/panasonic-energy-and-novonix-sign-binding-take-agreement
[2] Phillips 66, "Phillips 66 Announces Strategic Investment in NOVONIX", 2021-08-09 — 16 %-belang, $150 mln; "specialty coke, a key precursor". https://investor.phillips66.com/financial-information/news-releases/news-release-details/2021/Phillips-66-Announces-Strategic-Investment-in-NOVONIX/default.aspx
[3] Phillips 66, Lake Charles Manufacturing Complex — Westlake, Louisiana, aan de Calcasieu; "specialty coker and calciner"; specialty petroleum coke. https://www.phillips66.com/refining/lake-charles-refinery/
[4] Phillips 66, Specialties — "leading worldwide producer of premium needle cokes, which are produced at our Humber (UK) and Lake Charles (Louisiana) refineries". https://www.phillips66.com/specialties/
[5] Phillips 66 newsroom, "It's specialty coke…", 2024-09-30 — Humber en Lake Charles maken specialty coke voor synthetische grafietanodes. https://www.phillips66.com/newsroom/specialty-coke-path-toward-cleaner-tomorrow/
[6] NOVONIX Limited, Form 20-F FY2025 (2026) — "we may source specialty petroleum needle coke … from Phillips 66 or a select few other suppliers"; Riverside "up to 20,000 tonnes per annum"; vier grafitisatieovens; Panasonic-update 2026-01-16; hoofdkantoor 1029 W. 19th Street, Chattanooga; Lake Charles en Kansas komen niet voor. https://www.sec.gov/Archives/edgar/data/1859795/000119312526072814/nvx-20251231.htm
[7] NOVONIX, "Our Materials / Contact" — Riverside, 1029 West 19th Street, Chattanooga; 20.000 tpa voor Panasonic en PowerCo. https://www.novonixgroup.com/anode-materials/ · https://www.novonixgroup.com/contact-us/
[8] Chattanooga Times Free Press, 2026-06-12 — eerste mass-produced full-scale-monster synthetisch grafiet naar Panasonic. https://www.timesfreepress.com/news/2026/jun/12/novonix-marks-milestone-in-full-scale-graphite/
[9] Chattanooga Times Free Press, 2026-03-09 — uitbreiding mogelijk naast Riverside (Riverfront Parkway) i.p.v. Enterprise South. https://www.timesfreepress.com/news/2026/mar/09/novonix-may-expand-at-riverside-plant-not/
[10] WTVC NewsChannel 9, 2026-09-01 — halfjaarrapport: 17,5 acre naast Riverside niet gekocht; volle capaciteit sept 2031 (was dec 2027); massaproductie Panasonic H2 2027; C-monster geleverd; going-concern-voorbehoud. https://newschannel9.com/news/local/novonix-backs-off-land-purchase-next-to-chattanooga-plant-slows-production-ramp-up-riverside-synthetic-graphite-panasonic-battery-materials-175-acres
[11] Argus Media, 2025-09-29 — Epsilon Advanced Materials koopt anode-grade groene en gecalcineerde naaldcokes uit P66's 264.000 b/d Lake Charles-raffinaderij voor een 30 kt/j-anodefabriek in North Carolina (2027). https://www.argusmedia.com/en/news-and-insights/latest-market-news/2736976-eam-p66-sign-us-graphite-anode-coke-supply-deal
[12] USGS, Mineral Commodity Summaries 2026 — Graphite: VS-import AAM (natuurlijk + synthetisch) jan–aug 2025 43.400 t (China 55 %, Indonesië 31 %, Korea 14 %); SPG in de VS gemaakt door twee bedrijven in Illinois en Louisiana; wereld 1.800 kt natuurlijk (China 1.400 kt). https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-graphite.pdf
[13] OpenStreetMap (ODbL) via Nominatim/Photon/Overpass, 2026-09-26 — landuse "Lake Charles Refinery" way 510858894 (operator Phillips 66 Company) centrum 30.24195/-93.27438; adrespunt 1029 West 19th Street 35.03879/-85.32427; US-90 "East Napoleon Street" en I-10 langs de zuidrand; 71 `highway=service access=private` binnen het terrein; spoor UP Lafayette Subdivision + CPKC Lake Charles Subdivision + Rosebluff Industrial Lead. https://www.openstreetmap.org
[14] Esri World Imagery via `v2/tools/sat_check.py` (live) — `v2/build-cache/satcheck/sat-grafiet-lakecharles-desoto-lakecharles.png` (z15), `…-lakecharles-west.png` (z16), `…-riverside.png` (z15). (`…-p66noord.png` = tankstation, verworpen.)
[15] OSRM (router.project-osrm.org, OSM-data), 2026-09-26 — cokesveld → Riverside 1.085,7 km / 12,3 u; Riverside → De Soto-routeerpunt 1.151,8 km / 13,4 u; via-punten op de routegeometrie gesnapt.
[16] `v2/design/routebrieven/grafiet-balama-vidalia.md` (been 7–8, §5) — De Soto terreinanker 38.93815/-95.00240, routeerpunt 38.94196/-95.00748, docks niet gelegd; profiel `grafiet-vidalia-desoto` in `v2/tools/maak_stroombeen_weg.py`.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `grafiet-lakecharles-desoto`** → `v2/data/stroomroute-grafiet-lakecharles-desoto.json` — 2 benen. 2.253,3 km. 3 markers: truck 1.108,7 km · truck 1.144,6 km.
Recept: `bak_stromen.sh` (functie `bak_grafiet_lakecharles_desoto`). Toelichting: twee wegscans (profielen `grafiet-lakecharles-desoto-lakecharles-riverside` en `grafiet-lakecharles-desoto-riverside-desoto` in `v2/tools/maak_stroombeen_weg.py`, extracts `us-louisiana`/`us-mississippi`/`us-alabama`/`us-tennessee` resp. `us-tennessee`/`us-kentucky`/`us-illinois`/`us-missouri`/`us-kansas`), geen zeebeen (eerste grafietketen zonder MARNET-been). Been b1 (P66 Lake Charles → Novonix Riverside) 1.108,7 km tegen ~1.086 OSRM (+2,1 %, binnen ±15 %); kop op de privé-terreinwegen van het Lake Charles-complex → `eindToegangPrivaat: True`. Been b2 (Novonix Riverside → De Soto-routeerpunt) 1.144,6 km tegen ~1.152 OSRM (−0,6 %); eindigt op het bestaande De Soto-routeerpunt (rotonde Astra Parkway, 38.94196/-95.00748) — hergebruik van hetzelfde anker/routeerpunt-paar als `grafiet-vidalia-desoto` — dus de De Soto-marker staat 443 m van de lijn op het terreinanker (anker ≠ routeerpunt, zoals bij grafiet-balama-vidalia). Naad tussen b1 en b2 0,00 km (beide scans delen exact de Novonix Riverside-coördinaat). Geen stippelbenen: beide benen zijn doorgetrokken werkaannames ("aannemelijk: één bron; volume nul tot H2 2027" staat in de been- en markernamen, niet in de lijnstijl — werkwijze §7).
Toets: `toets_knikken.py` geeft 0 terugloop op beide benen (63 spike-achtige knikken ≥60° zijn OSM-ruis op wegkruisingen, geen omkeringen die gerepareerd horen te worden); `toets_rechte_benen.py --min-km 5` vindt geen enkel been van deze stroom in de verdachtenlijst (beide benen volgen echte weggeometrie, omwegfactor 1,02 resp. 1,006 — geen rechte lijn). Bestand 422,9 KB, boven de losse ~300 KB-richtwaarde uit de handleiding maar in lijn met andere lange, dicht bemonsterde truckstromen in dit project (koper-tfm-durban 595 KB, koper-lasbambas-tongling 305 KB) — een bevinding, niet dichtgetrokken door punten weg te gooien.
Gereedschapslessen: geen — beide wegscans liepen in één poging binnen tolerantie, `corridorKlassen` was niet nodig (de hele reis loopt over interstates die al in `WEG_HOUD` zitten), alleen `eindToegangPrivaat` voor de Lake Charles-kop.
