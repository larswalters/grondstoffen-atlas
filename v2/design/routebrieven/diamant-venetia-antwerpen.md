# Routebrief (licht) · diamant — Venetia → Antwerpen (via O.R. Tambo & Brussels Airport)

**stroom-id:** `diamant-venetia-antwerpen` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** ruwe diamant van De Beers' Venetia-mijn (Limpopo, Zuid-Afrika, sinds 2021-2023 ondergronds)
gaat per **truck** naar de vrachtterminal van O.R. Tambo International Airport (JNB), per **vrachtvlucht**
(grootcirkel) naar Brucargo op Brussels Airport (BRU), en per **truck** naar het AWDC/Diamond Office in de
Antwerpse Diamantwijk voor handel en G7-certificering.
**Welke as van het verhaal:** Zuid-Afrika (Venetia) → OR Tambo → Antwerpen: het laatste grote De Beers-eigen
ZA-anker — de mijn is nu ondergronds. Venetia levert ~5 Mct/j ruw (~5% wereldvolume, grootste ZA-mijn) [1][9].
⚠️ **Twee lopende onzekerheden uit het ketenontwerp**, niet apart weerlegd binnen het webbudget (haalbaarheids-
toets: geen tegenspraak gevonden): de omschakeling naar ondergrondse mijnbouw (2021-2023) geeft een hogere
kostprijs en een langzamere ramp-up, en De Beers zelf staat ter discussie binnen Anglo American (mogelijke
afsplitsing/verkoop, aangekondigd 2024-2026) [9][10].

## 1 · Ketenkaart
```
Venetia-mijn (De Beers) `dia-venetia-mijn` ──(b1 truck · N1/R572 via Polokwane · ~440-491 km)──►
O.R. Tambo vrachtterminal `dia-jnb-cargo` (JNB, Kempton Park)
   ──(b2 lucht · vlucht JNB → BRU, grootcirkel · ~8.880 km, doorgetrokken)──►
Brucargo `dia-brucargo` (Brussels Airport)
   ──(b3 truck · E19 via Mechelen · ~38-40 km)──►
AWDC/Diamond Office `dia-awdc` (Antwerpen) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `dia-venetia-mijn` → `dia-jnb-cargo` | N1/R572 via Polokwane, Mokopane, Bela-Bela, Pretoria | ~440 [ontwerp]; webcheck (OSRM) 491,1 [8] | maak_stroombeen_weg | nee |
| b2 | B | lucht (vrachtvlucht, grootcirkel) | `dia-jnb-cargo` → `dia-brucargo` | JNB → BRU | ~9.150 [ontwerp]; grootcirkel 8.879,6 (eigen berekening) [8] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | `dia-brucargo` → `dia-awdc` | E19 via Mechelen | ~40 [ontwerp]; webcheck (OSRM) 37,7 [8] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-venetia-mijn` | mijn / laadplek | Venetia-mijn (De Beers), open put + verwerkingsfabriek, Limpopo | -22.4362, 29.3175 | [1][2][6][7] | bron-gelegd (z15 gezien: rand van de open put, direct ten zuiden een industrieel fabriekscomplex met gebouwen, opslagbekkens en toegangswegen — geen apart sorteergebouw op deze resolutie te onderscheiden) |
| `dia-jnb-cargo` | vrachtterminal (luchthaven, vertrek lucht) | O.R. Tambo Int'l Airport, vrachtloodsen/-apron, Kempton Park | -26.1400, 28.2300 | [3][6][7] | bron-gelegd (z16 gezien: cluster vrachtloodsen met open apron waarop meerdere widebody-vrachttoestellen geparkeerd staan, direct zuid van de passagiersterminal; zelfde anker als `pgm-jnb-vracht` in `pgm-rustenburg-tokio.md`, deze golf) |
| `dia-brucargo` | vrachtterminal (luchthaven, aankomst lucht/vertrek truck) | Brucargo, Brussels Airport | 50.90628, 4.45584 | [4][6][7] | bron-gelegd (z15 gezien: vrachtloodsen + geparkeerde vrachttoestellen op het platform, ten zuiden van de passagiersterminal; hergebruikt anker uit `diamant-ekati-antwerpen.md`, deze golf) |
| `dia-awdc` | beursgebouw / certificeringshub (bestemming) | AWDC / Diamond Office, Hoveniersstraat, Antwerpen | 51.21520, 4.41870 | [5][6][7] | bron-gelegd (z16 gezien: dicht stedelijk bouwblok in de Diamantwijk vlak bij Antwerpen-Centraal, op Hoveniersstraat; hergebruikt anker uit `diamant-ekati-antwerpen.md`, deze golf) |

## 4 · Via-punten (b1 en b3 — b2 is lucht en heeft er geen)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Louis Trichardt/Makhado, N1/R572-knoop | -23.0500, 29.9000 | hier komt de R572 vanaf de mijn uit op de doorgaande N1 zuidwaarts |
| b1 | 2 | Polokwane (N1) | -23.9000, 29.4500 | grootste stad onderweg, N1 passeert via de ring, geen alternatieve hoofdcorridor |
| b1 | 3 | Mokopane (N1) | -24.1833, 29.0167 | pint de route op de N1 i.p.v. een parallelle R-weg |
| b1 | 4 | Bela-Bela (N1) | -24.8833, 28.2833 | N1 loopt hier direct langs de stad, geen omweg via Modimolle |
| b1 | 5 | Pretoria, N1-ring | -25.7461, 28.1881 | N1 buigt hier om Pretoria heen richting Midrand/Kempton Park |
| b1 | 6 | Kempton Park, N1/R21-knoop | -26.1000, 28.2333 | hier verlaat de route de N1 op de R21 naar O.R. Tambo (zelfde punt als `pgm-jnb-cargo` in `pgm-rustenburg-shanghai.md`) |
| b3 | 1 | E19 bij Mechelen | 51.0213, 4.4481 | pint de route op de doorgaande E19 i.p.v. een parallelle N-weg door Mechelen-centrum (hergebruikt uit `diamant-jwaneng-antwerpen.md`) |
| b3 | 2 | E19/R1-knoop Antwerpen-Zuid (Wilrijk) | 51.1103, 4.4319 | trekt de route om de Antwerpse ring i.p.v. een sluipweg dwars door de stad (hergebruikt) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| AWDC / Diamond Office (Antwerpen) | AWDC | rough → import-/exportklaring + Kimberley Process-/G7-certificering | "one-stop import & export clearing" | [5][9] |

## 6 · Stoppunt
De brief stopt bij het AWDC/Diamond Office in Antwerpen: dit is de certificerings- en handelspoort (`design/
diamant.md` §3c/§4a), niet de slijperij (Surat, elders al gemodelleerd in `data/diamond.js`) en niet de
eindmarkt. Er is geen bron die voor déze specifieke Venetia-zending een vervolgbestemming per lading noemt —
fase D/E vervalt.

## 7 · Open punten
- **Geen lading-specifieke bron voor "Venetia-rough vliegt via O.R. Tambo → Brussels Airport"**: de vlucht volgt
  uit `design/diamant.md` §3c/§4a ("De Beers-rough uit Zuid-Afrika vliegt naar Antwerpen voor certificering +
  handel — géén zeeroute voor rough diamant") en uit het feit dat Brucargo al decennia Antwerpse diamantvracht
  draagt. Geen tussenlanding gebrond → één directe vlucht aangenomen (bakhandleiding §2).
- **JNB-vrachtterminalanker draagt geen "Cargo"-naam in OSM**: het punt is hergebruikt van `pgm-jnb-vracht`
  (`pgm-rustenburg-tokio.md`, deze golf), waar het satellietbeeld cargo-apronclusters met widebody-vrachttoestellen
  toont en Wikipedia "cargo aircraft park at aprons Golf/Whiskey/Delta/Foxtrot" noemt — géén apart pand met
  "Cargo" in de OSM-naam gevonden binnen budget.
- **Wegafstand b1 wijkt af**: het ketenontwerp noemt ~440 km, de OSRM-webcheck geeft 491,1 km (N1/R572 via
  Polokwane is een reële maar niet de kortste denkbare corridor). De via-punten volgen de N1 letterlijk; het
  verschil is corridorkeuze, geen foute route.
- **Venetia-specifiek volume niet los bevestigd**: het cijfer ~5 Mct/j / ~5% wereldvolume komt uit
  `design/diamant.md` §3a (KPCS/USGS), niet per bron voor het peiljaar 2026 herbevestigd binnen het webbudget.
- **De Beers/Anglo American-afsplitsing en de ondergrondse omschakeling** (uit de risico-tekst van het
  ketenontwerp) zijn niet apart geverifieerd — de haalbaarheidstoets vond binnen budget geen tegenspraak en
  kwalificeerde dit als "geen recent nieuws meer, geen aparte check nodig".

## 8 · Bronnen
[1] `v2/design/diamant.md` (projectbrief, dit project) §3a (jaarvolume Venetia ~5 Mct/j, ~5% wereldvolume,
    o.b.v. KPCS/USGS) + §4a (luchtvracht-bron: De Beers-rough uit Zuid-Afrika vliegt naar Antwerpen).
[2] Wikipedia, "Venetia Limpopo Nature Reserve" — omgeeft de Venetia-diamantmijn, eigendom De Beers Diamond
    Mining Company; coördinaten uit MediaWiki prop=coordinates. https://en.wikipedia.org/wiki/Venetia_Limpopo_Nature_Reserve
[3] Wikipedia, "O. R. Tambo International Airport" — IATA JNB, Kempton Park; coördinaten -26,13333/28,25000
    uit MediaWiki prop=coordinates. https://en.wikipedia.org/wiki/O._R._Tambo_International_Airport
[4] Wikipedia, "Brussels Airport" — IATA BRU, Zaventem; coördinaten 50,90139/4,48444 uit MediaWiki
    prop=coordinates. https://en.wikipedia.org/wiki/Brussels_Airport
[5] AWDC, "About AWDC" — adres Hoveniersstraat 22, 2018 Antwerpen; Diamond Office faciliteert import/export
    ("one-stop import & export clearing"). https://www.awdc.be/en/about-awdc
[6] OpenStreetMap/Nominatim + Photon (ODbL) — Venetia Diamond Mine (landuse=quarry, -22,43621/29,31745);
    O.R. Tambo Freight Terminal-cluster (aeroway=terminal, -26,11158/28,24051, ter oriëntatie — het gebruikte
    anker is het cargo-apron op -26,1400/28,2300, hergebruikt uit `pgm-rustenburg-tokio.md`); Brucargo
    (landuse=industrial, "Bedrijvenzone Machelen Cargo", 50,90628/4,45584); Hoveniersstraat, Antwerpen
    (highway=pedestrian, 51,21521/4,41873). https://www.openstreetmap.org
[7] Esri World Imagery via `v2/tools/sat_check.py` (z13-z16) —
    `v2/build-cache/satcheck/sat-diamant-venetia-antwerpen-{venetia-mijn,jnb-cargo,jnb-cargo-v2,jnb-overzicht,jnb-airport-full,bru-cargo,awdc}.png`.
[8] router.project-osrm.org (OSRM-demo op het OSM-wegennet) — webcheck-wegafstanden: Venetia-mijn →
    JNB-vrachtterminal 491,1 km, Brucargo → AWDC 37,7 km; grootcirkel JNB→BRU 8.879,6 km (eigen sferische
    berekening op de twee vrachtterminal-ankers).
[9] Ketenontwerp + haalbaarheidstoets (workflow-invoer, dit project, M31 golf 3) — jaarvolume, risico-tekst
    (Venetia ondergrondse omschakeling 2021-2023; De Beers/Anglo American mogelijke afsplitsing 2024-2026),
    bronnen_start (debeersgroup.com, debswana.com, awdc.be); haalbaarheidstoets: haalbaar, geen aanpassing.
[10] Anglo American, publieke berichtgeving 2024-2026 — voorgenomen afsplitsing/verkoop van De Beers binnen
    het Anglo American-portfolio (niet apart bevestigd binnen webbudget; zie risico-tekst in [9]).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `diamant-venetia-antwerpen` · **bestand:** `v2/data/stroomroute-diamant-venetia-antwerpen.json`
(117,9 KB) · **recept:** `bak_diamant_venetia_antwerpen()` in `v2/tools/bak_stromen.sh` (draai:
`bash v2/tools/bak_stromen.sh diamant-venetia-antwerpen`).

**Benen (3), totaal 9.582,2 km · 5.807 punten · 4 markers:**

| # | modaliteit | km | punten | naad | toelichting |
|---|---|---|---|---|---|
| b1 | truck | 665,2 | 5.015 | — | Venetia-mijn → O.R. Tambo vrachtterminal, N1/R572 via Louis Trichardt/Makhado, Polokwane, Mokopane, Bela-Bela, Pretoria, Kempton Park. `maak_stroombeen_weg.py`, profiel `diamant-venetia-antwerpen-venetia-jnb` (`eindToegangPrivaat: True`, `corridorKlassen: [tertiary, unclassified]`). |
| b2 | lucht | 8.879,6 | 357 | 0,00 km | vlucht JNB → BRU, grootcirkel, `maak_luchtbeen.py`. Doorgetrokken (geen stippel — bakhandleiding §2). |
| b3 | truck | 37,4 | 435 | 0,14 km | Brucargo → AWDC/Diamond Office, E19 via Mechelen/Wilrijk. **Letterlijke kopie** van het reeds gebakken been uit `diamant-jwaneng-antwerpen` (identieke via-punten, vrijwel identieke ankers) — geen nieuwe wegscan. |

**Toelichting per stippel:** geen — alle drie de benen zijn doorgetrokken (geen stippel in deze keten,
zoals de opdracht al verwachtte: beide truckbenen zijn substantiële hoofdwegverbindingen en het luchtbeen
loopt tussen twee gelegde vrachtterminals).

**Toelichting per haven-aanloop:** geen — geen kade/zeebeen in deze keten (alleen truck en lucht).

**Toelichting per vlucht:** b2, JNB → BRU. Anker = vrachtterminal/vrachtplatform aan beide kanten
(O.R. Tambo cargo-apron, satelliet-gelegd; Brucargo, satelliet-gelegd, hergebruikt anker uit
`diamant-ekati-antwerpen.md`/`diamant-namdeb-gaborone.md`). Grootcirkel 8.879,6 km tegen het
ontwerpcijfer ~9.150 km — binnen de marge die bij een vlucht hoort (geen km-toets voor luchtbenen,
bakhandleiding §5). Geen tussenlanding gebrond → één directe vlucht, zoals de brief al aannam (§7).

**Gereedschapslessen:**
- **b1 kwam ver buiten de ±15%-norm uit: 665,2 km tegen de gepubliceerde/webcheck 491,1 km (+35,4%).**
  Eerst geprobeerd: `eindToegangPrivaat: True` (222,4 km voor het eerste deelbeen Venetia → Louis
  Trichardt/Makhado, tegen ~90 km hemelsbreed) en daarna óók `corridorKlassen: [tertiary, unclassified]`
  + `vensterKm` 40 → 75 (222,6 km, vrijwel ongewijzigd). Omdat het getal onder twee verschillende
  wegklasse-instellingen nagenoeg identiek blijft, is dit **geen wegklasse-filterprobleem maar een
  genuine detour in het OSM-wegennet** tussen de mijn en de N1-knoop bij Louis Trichardt/Makhado
  (mogelijk via Alldays/Vivo, een dun wegennet door het Soutpansberg-gebied). Via-punten zijn **niet**
  bijgeschoven om het getal te forceren (routebrief-licht §1, bakhandleiding §5) — dit blijft een
  bevinding, geen fix. Vergelijkbaar met de eveneens buiten-tolerantie bevinding bij `pgm-rustenburg-
  shanghai` b1 (+48,4% op een verwant N1/N4-traject).
- **`toets_knikken.py` vond 2 echte TERUGLOOP-punten** (niet alleen spikes) op b1, beide vlak bij het
  O.R. Tambo vrachtterminal-anker (-26,10025/28,23322, R=1 m · -26,13446/28,22503, R=7 m) — submeter-
  tot-enkele-meter straal, niet zichtbaar op wereldschaal. Niet gerepareerd binnen deze bake (zou een
  aparte via-puntenronde op het lokale straatnet bij de terminal vragen); overige 48 knikken zijn
  spikes/krappe bochten, geen terugloop.
- **`toets_rechte_benen.py --min-km 5`**: geen enkel been van deze stroom verschijnt in de uitslag —
  b1 en b3 zijn echte gerouteerde lijnen (5.015 resp. 435 punten), b2 (lucht) wordt door het tool
  bewust overgeslagen.
- **b3 als letterlijke kopie werkte zonder aanpassing** — de via-punten in mijn brief (E19 bij Mechelen
  51,0213/4,4481 · E19/R1-knoop Antwerpen-Zuid/Wilrijk 51,1103/4,4319) matchen exact het reeds gebakken
  profiel `diamant-jwaneng-antwerpen-brucargo-antwerpen`; scheelde een volledige wegscan.

**Toets (samenvatting):** `json.load` slaagt, `versie: 2`, `punt_formaat: lonlat`, alle modaliteiten in
{truck, lucht}, elk been ≥ 2 punten, bestandsgrootte 117,9 KB (< 300 KB-norm). Geen naad > 5 km (max
0,14 km, b3). Markers alle op hun anker (routeerpunt = anker voor alle vier).
