# Routebrief (licht) · PGM — Van → Via → Naar (land)

**stroom-id:** `pgm-zimplats-rustenburg` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** PGM-matte van de Zimplats Selous Metallurgical Complex (SMC, Great Dyke, Zimbabwe) per
**truck** over de A5/Harare–Masvingo-corridor naar de grensovergang **Beitbridge**, en vandaar per **truck**
over de N1/N4-corridor naar de eindraffinage **Rustenburg PMR** (Valterra Platinum, ex-Anglo American
Platinum) bij Rustenburg, Zuid-Afrika — geen luchtbeen: de matte reist over land, alleen het geraffineerde
metaal vliegt (niet in deze as gemodelleerd).
**Welke as van het verhaal:** de Zimbabwaanse Great Dyke-matte die (nog) niet in eigen land wordt afgeraffineerd
en per truck de grens over gaat naar de Zuid-Afrikaanse eindraffinage — dezelfde Beitbridge-corridor als de
koper-Copperbelt-as (`koper-kolwezi-durban`), nu voor PGM.

## 1 · Ketenkaart
```
Zimplats SMC `pgm-zimplats-smc` ──(b1 truck · A5 Chegutu–Harare → A4 Harare–Masvingo · ~450 km [bron] /
   ~600-650 km eigen via-puntensom, zie §7)──► Beitbridge-grens `pgm-beitbridge-grens`
   ──(b2 truck · N1 Musina–Polokwane–Pretoria → N4 Pretoria–Rustenburg · ~500 km)──► Rustenburg PMR
   `pgm-rustenburg-pmr` (Valterra Platinum) ── stoppunt (eindraffinage)
```
Niet getekend: Unki-mijn en Mimosa-mijn (Great Dyke) leveren vergelijkbare, kleinere matte-volumes naar
Zuid-Afrikaanse raffinage — andere entiteiten/mogelijk andere raffinaderij (Impala Springs), niet gedekt door
deze keten (§7).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-zimplats-smc` → `pgm-beitbridge-grens` | A5 (Chegutu–Harare) → A4/A1 (Harare–Beatrice–Chivhu–Masvingo–Beitbridge) | ~450 [ketenontwerp] — eigen via-puntensom ligt hoger, zie §7 | maak_stroombeen_weg | nee |
| b2 | A | truck | `pgm-beitbridge-grens` → `pgm-rustenburg-pmr` | N1 (Musina–Polokwane–Pretoria) → N4 (Pretoria–Rustenburg) | ~500 [ketenontwerp]; eigen via-puntensom ~526 km, sluit goed aan | maak_stroombeen_weg | nee |

Geen zee-, spoor-, binnenvaart- of luchtbeen; geen fase B/C (geen overslag op een haven); geen fase D/E (geen
bron noemt een vervolgbestemming ná de eindraffinage in déze as — §6).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-zimplats-smc` | mijn/smelter (concentrator + smelter + basismetaal-raffinage) | Zimplats Selous Metallurgical Complex (SMC), Chegutu-district, Mashonaland West, Zimbabwe | -18.0328, 30.4334 | [1][3][4][7] | bron-gelegd (z15 gezien: verwerkingsgebouwen met schoorsteen, een grote zeshoekige lichtgekleurde tailings-opslag direct ernaast, blauwgroene bezinkvijvers, en een tweede tailings-faciliteit ~1 km zuidwestelijk) |
| `pgm-beitbridge-grens` | grensovergang / overslag tussen twee truckcorridors | Beitbridge grensovergang, Limpopo-brug (Zimbabwe ↔ Zuid-Afrika) — hergebruikt uit `koper-kolwezi-durban.md` | -22.2244, 29.9865 | [7][11] | bron-gelegd (z15 gezien: de brug over de Limpopo-rivier, grensfaciliteiten en parkeerterreinen aan de Zimbabwaanse zijde direct ten noorden van de rivier) |
| `pgm-rustenburg-pmr` | losplek / eindraffinaderij | Rustenburg Precious Metals Refinery (Waterval-complex), Valterra Platinum (ex-Anglo American Platinum), Rustenburg, Zuid-Afrika | -25.6838, 27.3272 | [8][9][12] | bron-gelegd (z15 gezien: groot industrieel smelt-/raffinagecomplex met hoge procesgebouwen, tankenpark, bezinkbekkens en een tailings-veld direct noordwestelijk — komt overeen met het Waterval-smelter/PMR-cluster; de exacte PMR-hal binnen het complex is niet apart afgebakend, dus site-niveau) |

## 4 · Via-punten (in reisvolgorde)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Chegutu (A5-knooppunt) | -18.1305, 30.1460 | pint de A5 vanaf de SMC-toegangsweg; sluit een kortere binnenweg naar Kadoma uit |
| b1 | 2 | Harare (A5 → A4-wissel) — hergebruikt uit `koper-kolwezi-durban.md` | -17.8362, 31.0467 | dwingt de route door de hoofdstad; sluit een westelijke omweg via Bulawayo uit |
| b1 | 3 | Beatrice (begin A4 zuidwaarts) | -18.2581, 30.8544 | pint de A4 in zuidelijke richting direct na Harare, sluit de A5 naar Bulawayo/Mutare-richting uit |
| b1 | 4 | Chivhu (A4, tussenstop) | -19.0187, 30.8969 | bevestigt dat de doorgaande A4-corridor gevolgd wordt tot Masvingo |
| b1 | 5 | Masvingo (A4 = R1) — hergebruikt uit `koper-kolwezi-durban.md` | -20.0745, 30.8332 | laatste grote stad vóór de grens; sluit een oostelijke afslag richting Mutare uit |
| b2 | 1 | Musina (eerste stad na de grens) | -22.3454, 30.0269 | bevestigt de N1-richting direct na Beitbridge |
| b2 | 2 | Polokwane (N1) — hergebruikt uit `koper-kolwezi-durban.md` | -23.9218, 29.4803 | grote tussenstop op de N1, sluit binnenwegen door Limpopo-provincie uit |
| b2 | 3 | Pretoria, N1/N4-wissel (N4-afslag richting Rustenburg) | -25.6357, 28.2761 | dwingt de wissel van de N1 naar de N4 af; sluit doorrijden naar Johannesburg/Kaapstad (N1-zuid) uit |
| b2 | 4 | Rustenburg, N4/R24-kruising | -25.7031, 27.2572 | laatste punt vóór het Waterval/PMR-complex; pint de N4 als binnenkomstroute i.p.v. de R24 vanuit het zuiden |

Geofabrik-regio's: `zimbabwe` (b1), `zuid-afrika` (b1-staart + b2).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Zimplats Selous Metallurgical Complex | Zimplats (Implats) | Great Dyke-erts/concentraat (Ngezi-mijn, per interne slurry-leiding ~26 km, niet in deze brief getekend) → PGM-matte | 6E-verkoop FY2024: 641.265 oz (+6% t.o.v. FY2023); expansie-smelter gecommissioneerd okt 2024 | [1][3][4] |
| Rustenburg PMR (Valterra Platinum) | Valterra Platinum (ex-Anglo American Platinum) | matte (Zimbabwaans + eigen Bushveld-concentraat) → geregistreerd Pt/Pd/Rh | grootste PGM-raffinaderij ter wereld (capaciteit niet in t/j gepubliceerd in de geraadpleegde bronnen) | [8][9][12] |

## 6 · Stoppunt
De brief stopt bij Rustenburg PMR: dat is de eindraffinage in deze as (matte → geregistreerd Pt/Pd/Rh) en geen
bron in dit onderzoek noemt een specifieke vervolgzending van het geraffineerde metaal (dat zou een luchtbeen
zijn — bewust niet getekend, `bron_voor_luchtvracht` = n.v.t. voor déze as, ketenontwerp).

## 7 · Open punten
- **Km-mismatch been 1:** de ketenontwerp-indicatie (~450 km) ligt duidelijk onder de som van de gekozen
  via-punten (Chegutu–Harare–Beatrice–Chivhu–Masvingo–Beitbridge, ruwe schatting ~600-650 km). Mogelijk bestaat
  er een kortere ontsluiting die Harare-centrum vermijdt (bv. een link tussen de A5 bij Norton en de A4 bij
  Beatrice) die niet gevonden is — bij het bakken toetsen tegen de ±15%-norm en zo nodig een kortere
  binnenweg zoeken.
- **Interne Zimplats-slurryleiding Ngezi-mijn → SMC** (~26 km, bekend uit algemene bedrijfsinformatie maar niet
  hier gebrond met een URL) is bewust niet als been getekend: dit is bedrijfsinterne infrastructuur vóór het
  gemodelleerde traject, en de brief begint bij de smelter (waar de matte die de weg opgaat ontstaat).
  Beitbridge-lengte b2 kloppen wél goed (eigen som ~526 km tegen ~500 km ketenontwerp).
- **Exacte capaciteit Rustenburg PMR in t/jaar** is in de geraadpleegde bronnen niet gepubliceerd, alleen
  "grootste ter wereld" — kwalitatief, geen kwantitatieve brief-bron gevonden.
- **Unki- en Mimosa-mijn** (Great Dyke, kleinere vergelijkbare volumes naar Zuid-Afrikaanse raffinage) zijn
  bewust niet in déze keten getekend — andere entiteiten, mogelijk andere raffinaderij-bestemming
  (Impala Refineries Springs i.p.v. Rustenburg PMR), niet onderzocht in deze ronde.
- **Grensvertraging/exportverbod-risico Beitbridge:** het ketenontwerp noemt een dreigend Zimbabwaans
  ruw-matte-exportverbod naarmate eigen smeltcapaciteit wordt uitgebreid — dit been kan op termijn wegvallen;
  niet verder onderzocht hier, alleen overgenomen als risiconotitie.
- **Jaarvolume:** 641.265 oz 6E (FY2024, +6% t.o.v. FY2023) ≈ **19,9 t 6E/jaar** (641.265 ÷ 32,15).
  H1 FY2025 daalde tijdelijk −15% naar 280.000 oz door de commissioning van de nieuwe smelter; H2 FY2025
  herstelde +13,2% naar 317.000 oz. Mix = 6E (Pt+Pd+Rh+Au+Ru+Ir), niet nader uitgesplitst in de geraadpleegde
  bronnen.

## 8 · Bronnen
[1] Zimplats, officiële site, https://www.zimplats.com/
[2] Implats (moederbedrijf), officiële site, https://www.implats.co.za/
[3] Zimplats, "Integrated Annual Report FY2024" (PDF; 6E-verkoop 641.265 oz, +6%), 2024-09,
https://www.zimplats.com/data/2024/09/Zimplats-Final-Annual-Integrated-Report-FY2024-1.pdf
[4] Mining Weekly, "Implats commissions 35 MW solar project, expanded smelter at Zimplats", 2024-10-30,
https://www.miningweekly.com/article/implats-commissions-35-mw-solar-project-expanded-smelter-at-zimplats-2024-10-30
[5] Equity Axis, "Zimplats's Production Plummets, but Firm Prices Boost Profitability" (H1 FY2025 6E-matte
-15% naar 280.000 oz door smelter-commissioning), 2025-02,
https://equityaxis.net/post/18287/2025/2/zimplats-s-production-plummets-but-firm-prices-boost-profitability
[6] Wikipedia, "Great Dyke", https://en.wikipedia.org/wiki/Great_Dyke
[7] OpenStreetMap-contributors (ODbL) via Photon/Komoot-geocoder — objecten "Selous Metallurgical Complex"
(landuse=industrial), "Beitbridge Border Post", plaatsen Chegutu/Beatrice/Chivhu/Musina en de N4-kruisingen
bij Pretoria/Rustenburg, https://www.openstreetmap.org
[8] Valterra Platinum (voorheen Anglo American Platinum), officiële site, https://www.valterraplatinum.com/
[9] industryabout.com, "RBMR - Rustenburg Platinum Refinery" (locatie Waterkloof, Rustenburg, coördinaat
-25.683779,27.327233), https://www.industryabout.com/country-territories-3/2049-south-africa/platinum-mining/31210-rbmr-rustenburg-platinum-refinery
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15), `v2/build-cache/satcheck/sat-pgm-zimplats-rustenburg-smc2.png`,
`sat-pgm-zimplats-rustenburg-beitbridge.png`, `sat-pgm-zimplats-rustenburg-pmr.png`
[11] `v2/design/routebrieven/koper-kolwezi-durban.md` — hergebruikte ankers Beitbridge (-22.2244, 29.9865),
Harare (-17.8362, 31.0467), Masvingo (-20.0745, 30.8332), Polokwane (-23.9218, 29.4803)
[12] `v2/data/pgm.js` + `design/pgm.md` — v1-checklist (Rustenburg PMR = Anglo American Platinum Precious
Metals Refinery, "grootste PGM-raffinaderij ter wereld")

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `pgm-zimplats-rustenburg`** → `v2/data/stroomroute-pgm-zimplats-rustenburg.json` — 2 benen (beide truck,
fase A → stoppunt), **1.245,6 km**, 9.677 punten, 3 markers, 197,4 KB. Recept: `bak_stromen.sh` (functie
`bak_pgm_zimplats_rustenburg`); twee nieuwe wegprofielen `pgm-zimplats-rustenburg-smc-beitbridge` en
`pgm-zimplats-rustenburg-beitbridge-rustenburg` in `maak_stroombeen_weg.py`. Geen zee/spoor/binnenvaart/leiding/
lucht — twee doorgetrokken truckbenen over openbaar wegennet, geen stippel.

**b1 (truck, extract `zimbabwe`, vensterKm 90):** `maak_stroombeen_weg.py --profiel
pgm-zimplats-rustenburg-smc-beitbridge --bron geofabrik` — **663,0 km** geroute (getekende lijn 663,2 km incl.
anker-verbindingsstukjes) over de zes via-punten uit §4 (Chegutu → Harare → Beatrice → Chivhu → Masvingo →
Beitbridge), 19 keerlussen gesnoeid (725,4 → 663,0 km). Anker-verbindingsstukjes plant → weg 0,21 km, weg → kade
0,01 km (beide OK). First mile 5,43 km over kleine wegklassen (service/unclassified), last mile 0,00 km.

**⚠️ Lengtetoets BUITEN de norm (b1), verwachte bevinding uit §7:** 663,0 km tegen ~450 km (ketenontwerp) =
**+47,3%**, ruim boven het venster (±15%). De brief signaleerde dit al vooraf: de eigen via-puntensom
(Chegutu–Harare–Beatrice–Chivhu–Masvingo–Beitbridge) werd op ~600-650 km geschat, en de gemeten weggeometrie
(663,0 km) sluit daarbij aan — het is de gepubliceerde ~450 km die vermoedelijk een grove
hemelsbreed-achtige schatting is, niet de gemeten route. Geen via-punt geschrapt of bijgeschoven om het getal te
halen (conform de norm); mogelijk bestaat een kortere Harare-bypass die niet is gevonden (blijft open punt, zie
brief §7).

**b2 (truck, extract `zuid-afrika`, vensterKm 40):** `maak_stroombeen_weg.py --profiel
pgm-zimplats-rustenburg-beitbridge-rustenburg --bron geofabrik` — **582,1 km** geroute (getekende lijn 582,4 km
incl. anker-verbindingsstukjes) over de vier via-punten uit §4 (Musina → Polokwane → Pretoria N1/N4 → Rustenburg
N4/R24), 21 keerlussen gesnoeid (582,3 → 582,1 km, verwaarloosbaar). Anker-verbindingsstukjes plant → weg 0,01 km,
weg → kade 0,20 km (beide OK). First mile 0,00 km, last mile 7,90 km over kleine wegklassen
(residential/service/tertiary/unclassified) bij Rustenburg/het Waterval-complex.

**⚠️ Lengtetoets NET BUITEN de norm (b2):** 582,1 km tegen ~500 km (ketenontwerp) = **+16,4%**; tegen de eigen
via-puntensom uit §7 (~526 km, die "goed aansloot") is het verschil +10,7%. De gemeten weggeometrie (met
keerlussen en first/last-mile over kleine wegklassen) komt net buiten het ±15%-venster op de gepubliceerde 500 km —
bevinding, niet dichtgetrokken; de vier via-punten pinnen de enige bestaande N1→N4-corridorkeuze en zijn niet
aangepast.

**Naad tussen b1 en b2: 0,000 km** — beide benen delen letterlijk hetzelfde Beitbridge-grensanker
(-22.2244, 29.9865) als eindpunt/beginpunt.

**Toetsen:** `toets_knikken.py` — b1: 11 knikken ≥60° (alle spikes, R 3-48 m), 0 omkeringen. b2: 16 knikken ≥60°,
waarvan 2 omkeringen ≥150° en **1 TERUGLOOP** (-25.70456, 27.25575, R=8 m, v=2,9) in het last-mile-stuk bij
Rustenburg PMR — een klein OSM-artefact in het residential/service-wegennet rond het Waterval-complex (18 m lang
op een been van 582 km). Niet gerepareerd: dit vraagt een via-punt-aanpassing in het profiel, wat tegen de norm
"geen via-punt bijschuiven" ingaat voor een verwaarloosbaar stukje geometrie — genoteerd als bevinding.
`toets_rechte_benen.py --min-km 5` — geen melding (b1 omwegfactor 1,416, b2 omwegfactor 1,239; beide ruim boven
1,000, dus geen "recht been zonder stippel"-signaal). `json.load` slaagt: versie 2, `punt_formaat` lonlat, beide
benen modaliteit `truck` ∈ toegestane set, elk been ≥ 2 punten (5.623 / 4.054), bestandsgrootte 197,4 KB (ruim
onder ~300 KB).

**Toelichting stippels/haven-aanlopen/vluchten:** geen. Geen zeebeen dus geen haven-aanloop; geen bron noemt
luchtvracht voor de matte in deze as (brief §6) dus geen luchtbeen — de keten reist volledig over land tot de
eindraffinage.

**Gereedschapslessen:** geen nieuwe tool-issues. Het hergebruikte Beitbridge-grensanker (identiek aan
`koper-kolwezi-durban.md`) gaf een naad van exact 0,000 km tussen de twee benen — bevestigt dat coördinaat-voor-
coördinaat hergebruik van een bestaand anker werkt zoals bedoeld. Beide lengtetoetsen vielen buiten ±15%, wat de
brief zelf al als verwachte bevinding had gemarkeerd voor b1 (§7) en licht onderschat had voor b2 — de
keerlus-snoei en first/last-mile-stukjes tellen op tot enkele procenten extra boven een hemelsbreed-achtige
via-puntenschatting.
