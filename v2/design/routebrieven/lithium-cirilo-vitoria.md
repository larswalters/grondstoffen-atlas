# Routebrief (licht) · lithium — Grota do Cirilo (Araçuaí) → Porto de Vitória (→ China)

**stroom-id:** `lithium-cirilo-vitoria` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat (SC5,5%) van Sigma Lithium's DMS/flotatie-complex Grota do Cirilo (Jequitinhonha-vallei, Araçuaí, Minas Gerais) gaat volledig per **truck** — geen spoor — over BR-367/BR-116/BR-259/BR-101 naar de exporthaven van **Vitória** (Espírito Santo), en per **bulkschip** over de Zuid-Atlantische Oceaan naar China — getekend tot de Yangtze-monding (aannemelijk, hergebruikt anker); de enige Zuid-Amerikaanse Atlantische ertsroute van de atlas.
**Welke as van het verhaal:** as 1 — Braziliaans hardrock-concentraat naar Chinese raffinage, over de Atlantische Oceaan i.p.v. de Stille (Chili/Argentinië). Peiljaar 2025: Plant 1 nameplate ≈240–270 kt SC5,5%/j ≈ 35–39 kt LCE-indicatie (omrekenfactor uit `lithium-greenbushes-zhangjiagang.md`); Plant 2 in opbouw. Bronnen: sigmalithiumresources.com (investor updates), USGS Mineral Commodity Summaries 2026 — Lithium (Brazil-cijfer).

## 1 · Ketenkaart
```
Grota do Cirilo `li-cirilo-plant` ──(b1 truck · BR-367→Itaobim→BR-116→Gov. Valadares→BR-259→Colatina→João Neiva→BR-101 · ~650–700 km, schatting)──► Porto de Vitória `li-vitoria-kade`
   ──(b2 zee · haven-aanloop 95,5 km, stippel, zeeknoop 900 -20,00/-39,50)──► 
   ──(b3 zee · Zuid-Atlantische Oceaan, Kaap de Goede Hoop of Panama — MARNET beslist · ~19.500–20.000 km, schatting)──► Yangtze-monding `li-yangtze-monding` ⏹ stoppunt (aannemelijk, hergebruikt anker)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A/C | truck (spodumeenconcentraat SC5,5%, géén spoor — zie §7) | `li-cirilo-plant` → `li-vitoria-kade` | erftoegang → BR-367 → Itaobim → BR-116 → Governador Valadares → BR-259 → Colatina → João Neiva → BR-101 → havenwegen Vitória | ~650–700 (ontwerpschatting: via-keten hemelsbreed 558,6 km × 1,15–1,25 routefactor; geen gepubliceerd truck-km gevonden) | maak_stroombeen_weg, extract `brazilie`, refs BR-367/BR-116/BR-259/BR-101 | nee |
| b2 | B | zee (haven-aanloop, kortste pad over water) | `li-vitoria-kade` → zeeknoop 900 (-20,00000,-39,50000) | Baía de Vitória → open Atlantische kust | 95,5 (gemeten, `hecht_marnet.marnet_zee`) | maak_havenaanloop.py, terugval: rechte stippel | ja — haven-aanloop (kade > 5 km én > 25 km van de zeeknoop, bakhandleiding §2) |
| b3 | B | zee (bulkschip) | zeeknoop 900 → `li-yangtze-monding` | Zuid-Atlantische Oceaan, om Kaap de Goede Hoop of via Panama — MARNET beslist | ~19.500–20.000; hemelsbreed ~19.000 (ontwerpschatting) | MARNET | nee; *aannemelijk: één bron* in de beennaam van b3/marker |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-cirilo-plant` | mijn / verwerkingsknoop (DMS/flotatie Plant 1+2) | Sigma Lithium, Grota do Cirilo-complex, Araçuaí (MG) | -16.7328, -41.8878 | [1][9][11] | bron-gelegd (z16 gezien: fabrieksgebouwen + silo's/tanks direct naast open pits met laterietgroeve-kleuren en een toegangsweg vanaf het noorden; **vervangt** het bestaande sitelaag-anker `w-li-sigma` -16.7002/-41.8927, dat 4,6 km NNO op een klein gebouwencluster aan de oever van de Rio Jequitinhonha bleek te staan — vermoedelijk een pompstation, niet de hoofdconcentrator; zie §7) |
| `li-vitoria-kade` | overslag truck → zee | Porto de Vitória, Vila Rubim / Cais Comercial (bij Codesa-kantoor en Vports-kantoor) | -20.3238, -40.3477 | [4][5][10][11] | bron-gelegd (z15 gezien: pier/kade met aangrenzende loods- en tankopslag in de historische havenbuurt Vila Rubim, aan de vaargeul tegenover het centrum van Vitória; welk exact sitio/berth Sigma's concentraat + tailings laadt is niet per lading gebrond — zie §7) |
| `li-yangtze-monding` | aanlanding China (zeeknoop, stoppunt) | Yangtze-monding (bestaand anker) | 31.42704, 121.47618 | [8] = hergebruik uit `lithium-atacama-antofagasta.md` §3 | aannemelijk (zelfde rol; geen Chinese fabriek/haven per lading gebrond) |

## 4 · Via-punten (b1 — corridorkeuzes op de doorgaande weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Itaobim (kruising BR-367 × BR-116) | -16.5619, -41.5025 | pint de noordelijke aftakking naar BR-116 i.p.v. BR-367 verder oost naar Salto da Divisa |
| b1 | 2 | Governador Valadares (kruising BR-116 × BR-259) | -18.8574, -41.9439 | pint de afslag oostwaarts op BR-259 i.p.v. BR-116 door naar Belo Horizonte |
| b1 | 3 | Colatina (BR-259, ES) | -19.4720, -40.7193 | pint de doorgaande BR-259-corridor door Espírito Santo |
| b1 | 4 | João Neiva (kruising BR-259 × BR-101) | -19.7272, -40.4338 | pint de afslag zuidwaarts op BR-101 naar Vitória i.p.v. noordwaarts |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Grota do Cirilo, DMS/flotatie-complex (Plant 1+2) | Sigma Lithium (Sigma Mineração S.A.) | ROM-spodumeenerts → spodumeenconcentraat SC5,5% + tailings | Plant 1 ≈240–270 kt SC/j (2024→2025-doel); Plant 2 in opbouw | [1][2][9] |
| Porto de Vitória, Vila Rubim | Codesa / private terminaloperator Vports | truck (big bags/bulk concentraat + tailings) → bulkschip | niet gepubliceerd per lading; eerste ladingen 2023 telkens ~15.000 t concentraat + ~15.000–30.000 t tailings | [3][4] |

## 6 · Stoppunt
De brief stopt op de Yangtze-monding: geen bron noemt de Chinese raffinaderij of aanlandingshaven per lading (Yahua/Sichuan is aannemelijk, niet bevestigd) — fase D/E vervallen en de lijn eindigt waar het bewijs eindigt.

## 7 · Open punten
- **Kernclaim van het ontwerp vervalt (haalbaarheidstoets, bindend):** géén spoorcorridor via FCA/VLI naar Porto Sul/Ilhéus (Bahia) — Sigma Lithium vervoert 100% per truck naar Vitória (Espírito Santo), bevestigd door meerdere persberichten 2023–2025 [2][3][6][7]. Stroom-id daarom hernoemd van het oorspronkelijke ontwerp `lithium-cirilo-ilheus` naar **`lithium-cirilo-vitoria`**; de "eigen groene spoorcorridor"-frase uit de as-omschrijving is geschrapt. Het originele NI 43-101-technisch rapport noemde wél Porto Sul/Ilhéus als geplande exporthaven (~500 km) [9] — dat was het toen geplande, niet het uitgevoerde tracé.
- **Truck-km niet gepubliceerd:** geen bron geeft een exacte wegkilometrage Araçuaí→Vitória; §2/b1 is een ontwerpschatting op de via-keten (558,6 km hemelsbreed × 1,15–1,25). Wordt bij het bakken vervangen door de gemeten weggeometrie.
- **Exacte laadkade/berth Vitória onbekend:** "Vports – Porto de Vitória" wordt in persberichten genoemd als locatie van de eerste ladingen [3], maar geen bron geeft de precieze pier/berth; het site-anker in §3 is het best gevonden punt (Vila Rubim, bij het Vports- en Codesa-kantoor).
- **Grota do Cirilo-anker gecorrigeerd:** het bestaande sitelaag-anker `w-li-sigma` (status "onzeker") bleek 4,6 km van het echte DMS/flotatie-complex te liggen; §3 hierboven draagt de correctie. Aan te passen in `v2/design/lithium-sitelaag.json` bij de volgende sitelaag-ronde.
- **Chinese eindbestemming** blijft aannemelijk/niet bevestigd (Yahua-groep/Sichuan) — ongewijzigd t.o.v. het ontwerp.
- **Productiestatus peiljaar:** 2025 kende een tijdelijke productiestop/-hervatting (Sigma 3Q25 MD&A, niet apart geverifieerd in deze ronde); het hier genoemde volume is nameplate-capaciteit, geen gemeten 2025-uitvoer.
- **Geen wegextract China nodig** voor deze brief (stopt op de Yangtze-monding, geen fase D).

## 8 · Bronnen
[1] Sigma Lithium Corp, persbericht 27-04-2023 — trucks van Grota do Cirilo (Araçuaí-fabriek) naar Vitória Port; laadtijd ~5 min/truck. https://sigmalithiumcorp.com/sigma-lithium-trucks-green-lithium-and-tailings-to-vitoria-port-in-preparation-of-15000-tonne-shipment-of-each-product-in-may/
[2] Sigma Lithium Corp, persbericht Q2 2023 — tweede ladingdoel 15.000 t Triple Zero Green Lithium bereikt bij Vitória Port. https://sigmalithiumcorp.com/sigma-lithium-reaches-second-shipment-target-of-15000-tonnes-of-triple-zero-green-lithium-at-port-closes-export-revolver-credit-line-with-santander-for-us10m-reports-second-quarter-2023-results/
[3] Revista Mineração, 27-07-2023 — eerste verscheping "lítio verde" bij "Vports – Porto de Vitória (ES)", 15.000 t lithium + 15.000 t bijproducten. https://revistamineracao.com.br/2023/07/27/sigma-lithium-realiza-primeiro-embarque-de-litio-verde-no-porto-de-vitoria-es/
[4] PR Newswire, 27-04-2023 — herpublicatie van [1], zelfde tekst en cijfers. https://www.prnewswire.com/news-releases/sigma-lithium-trucks-green-lithium-and-tailings-to-vitoria-port-in-preparation-of-15-000-tonne-shipment-of-each-product-in-may-301810234.html
[5] MarketScreener, 27-04-2023 — herpublicatie van [1]. https://www.marketscreener.com/quote/stock/SIGMA-LITHIUM-CORPORATION-44561341/news/SIGMA-LITHIUM-TRUCKS-GREEN-LITHIUM-AND-TAILINGS-TO-VITORIA-PORT-IN-PREPARATION-OF-15-000-TONNE-SHIPM-43668718/
[6] Batteries News, 27-04-2023 — herpublicatie van [1]. https://batteriesnews.com/sigma-lithium-trucks-green-lithium-tailings-vitoria-port-preparation-15000-tonne-shipment-of-each-product-in-may/
[7] Seeking Alpha / The Fly, oktober 2023 — derde verscheping 20.000 t Triple Zero Green Lithium klaar bij de haven op 20 oktober. https://seekingalpha.com/pr/19498456-sigma-lithium-readies-third-shipment-of-20000-tonnes-of-triple-zero-green-lithium-at-port-by
[8] `v2/design/routebrieven/lithium-atacama-antofagasta.md` §3 — anker `li-yangtze-monding` 31.42704,121.47618, hergebruikt.
[9] SEC EDGAR, NI 43-101 Technical Report Grota do Cirilo Lithium Project — locatie "25 km oost van Araçuaí, 450–600 km NO van Belo Horizonte", toegang via BR-367; UTM-referentiepunt 190615 mE/8146788 mN (zone 24S) ≈ -16,74/-41,90, 4,6 km van het satelliet-gelegde plant-anker; vermeldt Porto Sul/Ilhéus (~500 km) als het destijds geplande exportkanaal. https://sigmalithiumresources.com/wp-content/uploads/2023/05/2023-01-SGML-Updated-Technical-Report-1.pdf ; SEC-exhibit https://www.sec.gov/Archives/edgar/data/1848309/000117184325001837/ex_796089.htm
[10] OpenStreetMap/Nominatim (ODbL) — "Vports" kantoren -20.32212,-40.33784 en -20.32116,-40.34717; "Companhia Docas do Espírito Santo" -20.32384,-40.34765; gemeente-centroïdes Itaobim, Governador Valadares, Colatina, João Neiva, Araçuaí. https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z14–z16, live): `v2/build-cache/satcheck/sat-lithium-cirilo-vitoria-{sigma-plant,sigma-plant-z14,sigma-plant-main,sigma-plant-close,vports-office,codesa-cais,vitoria-overview}.png`.
[12] Wikipedia (pt), BR-259 — Governador Valadares–Colatina–João Neiva (begint op BR-101), 711,7 km totaal. https://pt.wikipedia.org/wiki/BR-259
[13] v2/design/lithium-sitelaag.json — bestaand anker `w-li-sigma` (status "onzeker", coördinaat -16.7002,-41.8927), hier gecorrigeerd op basis van [11].

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

⚠️ **Stroom-id-correctie ten opzichte van de opdracht:** de bak-opdracht noemde nog het
oorspronkelijke ontwerp-id `lithium-cirilo-ilheus`. Deze brief (§7, haalbaarheidstoets,
bindend) had dat id vóór het bakken al vervangen door **`lithium-cirilo-vitoria`**, omdat
er géén spoorcorridor via FCA/VLI naar Porto Sul/Ilhéus (Bahia) bestaat — Sigma Lithium
vervoert 100% per truck naar Vitória (Espírito Santo). Gebakken is dus `lithium-cirilo-vitoria`,
zoals de bak-aanwijzingen in de opdracht zelf ook al voorschreven (functie
`bak_lithium_cirilo_vitoria`). Vóór het bakken gecontroleerd: geen restanten van
`lithium-cirilo-ilheus` op schijf (geen functie, geen profiel, geen data-bestand).

**Stroom `lithium-cirilo-vitoria`** → `v2/data/stroomroute-lithium-cirilo-vitoria.json` — 3 benen,
**20.951,0 km**, 13.862 punten, 3 markers. truck 712,4 km · zee 102,7 (stippel) + 20.135,9 =
20.238,6 km. Recept: `bak_stromen.sh` (functie `bak_lithium_cirilo_vitoria`).

**b1 (truck, `maak_stroombeen_weg.py --profiel lithium-cirilo-vitoria-plant-kade --bron geofabrik`,
extract `brazilie`):** Grota do Cirilo → Itaobim → Governador Valadares → Colatina → João Neiva →
Porto de Vitória, **712,4 km** (11.717 punten, na 57 gesnoeide keerlussen van 756,5 → 712,3 km
ruw). Tegen de ontwerpschatting van ~675 km (via-keten hemelsbreed 558,6 km) = **+5,5%** — ruim
binnen een venster, en er is geen gepubliceerd cijfer om een harde ±15%-toets tegen af te dwingen
(§2/§7 van de brief). `corridorKlassen: ["tertiary"]` toegevoegd omdat de BR-367 direct bij het
complex een tertiary-klasse had; eindklassen (residential/service/tertiary/unclassified) namen
33.444 van 145.898 kleine-klasse-ways binnen 12 km van plant/kade mee. Anker-verbindingen (buiten
de lengtetoets): plant → weg 0,09 km, weg → kade 0,01 km — beide ruim binnen de eindzone.

**b2 (zee, stippel, haven-aanloop Vitória):** `maak_havenaanloop.py --van -20.3238,-40.3477
--naar -20.00000,-39.50000` (Vitória-kade → zeeknoop 900) — pad over water gevonden op trap
"cel 0,005° kaal" (de eerste drie trappen faalden of gaven "geen pad"): **102,7 km · 87 punten ·
0,00 km over land**, omwegfactor 1,075 tegen de rechte lijn (95,5 km). Geen terugval nodig — het
tool hing niet vast op `timeout 300`.

**b3 (zee, MARNET, geen stippel):** `--been "zee|...|-20.00000,-39.50000|31.42704,121.47618"`,
startend op de zeeknoop van b2 (niet op de kade — die aanloop levert b2). Snap zeeknoop 0,000 km,
snap Yangtze-monding 10,715 km (ruim onder `--max-snap` 25 km). Resultaat **20.135,9 km over
93 MARNET-edges** (2.058 punten) tegen de ontwerpschatting ~19.500–20.000 km uit de brief = net
erboven (+0,7% tot +3,3% afhankelijk van welk uiteinde van de bandbreedte je pakt) — binnen het
venster, geen harde bron om tegen te toetsen. Lengte-invariant: getekende lijn 20.135,914 km vs
som edge-km 20.135,300 km = +0,614 km (de naden).

**Toets naden:** alle drie de overgangen **0,000 km** — b1→b2 (plant-tot-kade eindigt exact op de
haven-aanloop-start) en b2→b3 (haven-aanloop eindigt exact op de zeeknoop waar het bulkschip
begint). Geen zee-snap boven de 5 km-norm, dus geen tweede haven-aanloop nodig.

**`toets_knikken.py`:** 21 knikken ≥60°, **0 omkeringen ≥150°, 0 terugloop** (dus niets dat volgens
de norm gerepareerd hoort te worden). De 20 spikes op b1 (truck) zijn allemaal kleine-straal
(1–138 m) OSM-zigzag op via-punten/kruisingen — geen van alle is een omkering. Het zeebeen b3 heeft
1 krappe bocht (81,9°, straal 5.448 m bij 30,90190/122,89110) — een normale MARNET-routeknik bij de
nadering van de Yangtze-monding, geen fout.

**`toets_rechte_benen.py --min-km 5`:** geen been van deze stroom in de uitslag — ook b2 (de
stippel, omwegfactor 1,075) wordt niet als verdachte rechte lijn aangemerkt.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee} (binnen de
toegestane set), elk been ≥2 punten (minimum 87), bestandsgrootte **289,8 KB** (< 300 KB-richtwaarde,
net onder de rand — dit is met 13.862 punten de grootste lichte-lithiumstroom tot nu toe, vooral
door de 11.717 punten van het ongesnoeide truckbeen).

**Markers:** Grota do Cirilo 0,0 m · Porto de Vitória 0,0 m · Yangtze-monding **4.448,8 m**
(anker ≠ routeerpunt — bestaand, hergebruikt anker uit `lithium-atacama-antofagasta.md`, dezelfde
afstand-klasse als eerder gerapporteerd voor ditzelfde punt in andere lithiumstromen; niet
bijgeschoven om de afstand te halen, werkwijze §3).

**Gereedschapslessen:** de coördinaat-volgorde voor `maak_havenaanloop.py --van/--naar` moet met
`=` doorgegeven worden (`--van=-20.3238,-40.3477`) zodra de eerste waarde met een `-` begint —
zonder `=` leest argparse het minteken als een optievlag en faalt de aanroep met "expected one
argument". Verder geen bijzonderheden: dit was de eerste keer dat een lichte lithiumbake zonder
enige terugval (geen mislukte haven-aanloop, geen "geen wegpad", geen tweede spoorrun) in één keer
door alle drie de benen liep.
