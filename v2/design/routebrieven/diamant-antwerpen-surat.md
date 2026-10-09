# Routebrief (licht) · diamant — Antwerpen (AWDC) → Brussels Airport → Mumbai (BOM) → Surat (India)

**stroom-id:** `diamant-antwerpen-surat` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** gecertificeerde ruwe diamant (rough) van het AWDC/Diamond Office in Antwerpen per truck over de E19
naar Brucargo (Brussels Airport), als vrachtvlucht (grootcirkel BRU → BOM, **aannemelijk: één bron**) naar het CSMIA Air Cargo
Complex in Mumbai, en per truck over de NH48 (~273 km) naar de Surat Diamond Bourse (DREAM City) — de Antwerpse G7-poort naar de Indiase slijpers.
**Welke as van het verhaal:** *Antwerpen als G7-poort → Surat*, indicatie ~28 Mct/j ruw (v1-checklist `design/diamant.md` §4b / `data/diamond.js`
flow dia-antwerp → dia-surat, natte vinger, peiljaar 2023-24, geen waarheid; eenheid Mct/j = miljoen karaat per jaar) [1]. Geen Antwerpen-India-cijfer
in Mct gevonden; vindbare getallen zijn ongedateerd of onderling strijdig. Context: Antwerpen telde H1 2026 38,9 Mct in+uit, alle bestemmingen [5].
Waarde per karaat laag tot middel (kleine stenen die in Surat geslepen worden) — hier niet in het gewicht.

## 1 · Ketenkaart
```
AWDC/Diamond Office, Antwerpen `dia-awdc` ──(b1 truck · E19 via Mechelen · omgekeerde kopie · 37,4 km)──►
Brucargo, Brussels Airport `dia-brucargo` ──(b2 lucht · vlucht BRU → BOM, grootcirkel, aannemelijk · 6.867 km)──►
CSMIA Air Cargo Complex, Mumbai `dia-bom-cargo` ──(b3 truck · NH48 via Manor–Talasari–Vapi–Valsad–Navsari–Sachin · kopie · 273,4 km)──►
Surat Diamond Bourse `dia-sdb` ──(b4 truck · stippel · 0,29 km kopie)──► stoppunt (anker)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | AWDC Antwerpen → Brucargo | E19 via Mechelen; **omgekeerde letterlijke kopie** van `diamant-jwaneng-antwerpen` b4 (`…-weg-brucargo-antwerpen.geojson`) | hemelsbreed 34,4 km, geen wegkm (kopie 37,4 km; OSRM-webcheck 37,7 km is OSM-afgeleid) [11] | kopie (omgekeerd) | nee |
| b2 | B | lucht | Brucargo (BRU) → CSMIA Air Cargo Complex (BOM) | vlucht BRU → BOM, grootcirkel (aannemelijk: één bron) | 6.867,2 grootcirkel [berekend] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | CSMIA Air Cargo Complex → Surat Diamond Bourse | NH48 Mumbai–Ahmedabad; **letterlijke kopie** van `diamant-gaborone-surat` b3 (= `diamant-dubai-surat` b3) | 289 km stad-tot-stad Mumbai–Surat [9]; kopie 273,4 = −5,4% | kopie | nee |
| b4 | C | truck | DREAM City interne toegangsweg → `dia-sdb` | OSM-topologiegat DREAM City | 0,29 [kopie] | kopie (stippel) | ja — eigen verbinding zonder net (letterlijk uit `diamant-gaborone-surat` b4) |

Geen zeebeen (dus geen haven-aanloop). Brucargo ligt airside, maar het wegbeen eindigt 0,14 km van het anker op de openbare weg en het BOM-wegbeen
0,03 km van het BOM-anker — geen last-mile-stippel nodig (patroon `goud-loulo-ticino` niet van toepassing).

## 3 · Ankers (één per site en per overslag — alle vier HERGEBRUIKT, niet opnieuw gelegd)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-awdc` | handels-/certificeringshub / vertrek | AWDC/Diamond Office, Hoveniersstraat, Antwerpen | 51.2152, 4.4187 | [4][11] (`diamant-ekati-antwerpen` §3) | bron-gelegd (z15 gezien: dicht stedelijk bouwblok in de Diamantwijk, kruis ~0,3 km ten noordwesten van het stationsgebouw Antwerpen-Centraal; geen eigen terrein te onderscheiden) |
| `dia-brucargo` | overslag truck → lucht | Brucargo, Brussels Airport | 50.90628, 4.45584 | [7][11] (`diamant-ekati-antwerpen` §3) | bron-gelegd (z15 gezien: kruis tussen vrachtloodsen en verhard platform met geparkeerde toestellen, noordrand van de cargozone ten noorden van de landingsbaan) |
| `dia-bom-cargo` | overslag lucht → truck | CSMIA Air Cargo Complex, Sahar, Mumbai | 19.0994, 72.8673 | [11] (`diamant-dubai-surat` §3) | bron-gelegd op site-niveau (z15 gezien: kruis net N van het luchthavenhek bij de vrachtloodsen, tussen de Terminal-2-boog en de oude baan; zelfde punt als in zes zusterbrieven, niet verschoven) |
| `dia-sdb` | beurs + slijperijcluster / bestemming | Surat Diamond Bourse, DREAM City | 21.1097, 72.7953 | [8][11] (`diamant-gaborone-surat`) | bron-gelegd (z15 gezien: negen torens op een eigen as midden in vlak land buiten de stad; routeerpunt 21.107445, 72.796653 ligt 0,29 km ervandaan) |

## 4 · Via-punten (alleen b3; b1 is één doorgaande snelweg, kopie; b2 lucht)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Manor (NH48-knooppunt) | 19.7228, 72.9096 | NH48 buigt hier van de kustvlakte het binnenland in |
| b3 | 2 | Talasari | 20.1222, 72.9164 | deelstaatgrens Maharashtra–Gujarat, NH48-flyover |
| b3 | 3 | Vapi | 20.3720, 72.9170 | eerste grote Gujarat-industriestad op de corridor |
| b3 | 4 | Valsad-bypass (NH48-trunk) | 20.5968, 72.9512 | trunk omzeilt Valsad ~3 km zuidwestelijk; de stadscentroïde snapte op een stompje |
| b3 | 5 | Navsari | 20.9500, 72.9300 | doorgaande NH48-stad vlak vóór Surat |
| b3 | 6 | Sachin | 21.0853, 72.8805 | corridor buigt af naar de Hajira–Sachin Bypass richting DREAM City |
(Uit `diamant-dubai-surat` §4; het b3-geojson is gekopieerd, dus geen nieuwe wegscan. b1 draagt via-punten E19 Mechelen 51.0213, 4.4481 en Antwerpen-Zuid 51.1103, 4.4319 in zijn bronbestand.)
Geofabrik-regio's: b1 `belgie`; b3 `india` (geen scan nodig: kopieën).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| AWDC/Diamond Office | AWDC | rough/polished → import-/exportklaring + Kimberley-Process-certificering; G7-certificaat voor niet-Russische natuurlijke rough ≥ 0,5 ct | geen capaciteit per ketenbron | [4] |
| CSMIA Air Cargo Complex | Mumbai International Airport | luchtvracht → douane (Air Special Cargo) → truck | geen cijfer gevonden | [11] |

Het slijpen gebeurt ná het stoppunt in Surat.

## 6 · Stoppunt
De brief stopt bij de Surat Diamond Bourse: handel, douane-afhandeling en fabricage-units in één complex [8]; geen bron koppelt déze Antwerpse
lading aan één slijperij — fase D vervalt, fase E vervalt.

## 7 · Open punten
- **De vlucht BRU → BOM is een aanname (één bron) en geen directe lijndienst bestaat nu.** Jet Airways vloog Brussel–Mumbai tot 22-03-2016, Brussels Airlines tot 2018;
  in 2025 onderhandelt Brussels Airport met Air India en IndiGo over een herstart [2][3]. Geen bron noemt een directe BRU-BOM-vrachtvlucht, vluchtnummer of tussenlanding;
  de lading kan in werkelijkheid via een hub gaan (Dubai, Zürich — de roof van 2013 betrof Antwerpse diamant in een Brink's-wagen naar Brussels Airport voor een vlucht naar Zürich [7]).
  Eén directe grootcirkel is dus schematisch: "van deze terminal naar die", niet "langs deze lijn". Dat Antwerpse rough naar India vliegt is wél gebrond (diamanten "heen en weer vliegen", >8 op de 10 ruwe stenen via Antwerpen [2]).
- **Volume is een natte vinger (28 Mct/j)**; getallen als "75 procent van Antwerps rough naar India" (JCK, ongedateerd) en 85 Mct zijn onderling strijdig en niet geverifieerd. Antwerp rough-export Q1 +40% naar $ 2,58 mld [10]: jaar niet bevestigd, geen India-vermelding.
- **Russische rough** loopt hier niet door (G7-importverbod; Antwerpen is G7-authority [4]): de Dubai-omweg staat in `diamant-dubai-surat`.
- **b1 en b3: geen echte wegkm** (alleen hemelsbreed 34,4 km en stad-tot-stad 289 km); de ±15%-toets is voor deze kopieën een indicatie.
- b1 eindigt 0,14 km van `dia-brucargo` (jwaneng-anker 50.9056, 4.4576 ligt 0,14 km ten ZO): naad b1→b2 blijft binnen de 5 km-norm; niet verschoven.
- **Mumbai-freighters gepauzeerd** aug 2026 t/m mei 2027 (Apron G) [11]: geldt vrachtvliegtuigen, niet beveiligde koerierlading in passagiersvluchten; de kaart toont de vaste vorm.
- AWDC-jaarcijfers 2025 en het GJEPC-artikel (tekst ontbrak in de fetch) niet verder geraadpleegd; Brussels Airport-persbericht (403) alleen via zoekresultaat gezien — niet geciteerd.

## 8 · Bronnen
[1] Ketenontwerp M31 golf 8 + `design/diamant.md` §4b / `data/diamond.js` (flow dia-antwerp → dia-surat, 28, air) — intern.
[2] La Libre, 2017-04-28, "Brussels Airlines rouvre la route du diamant" (Jet Airways laatste BRU–BOM 2016-03-22; diamant 83% van Belgische export naar India; >8 op 10 ruwe stenen via Antwerpen). https://www.lalibre.be/economie/entreprises-startup/2017/04/28/brussels-airlines-rouvre-la-route-du-diamant-ZG4JR3SBOBE4NBZUVV6Z6TOZY4/
[3] Brussels Times, 2025-03-05, "Brussels Airport looks into relaunching direct flights to Delhi and Mumbai" (Brussels Airlines t/m 2018, onderhandelingen Air India/IndiGo). https://www.brusselstimes.com/business/1472207/brussels-airport-looks-into-relaunching-direct-flights-to-delhi-and-mumbai
[4] AWDC, G7/EU-sancties-FAQ (Antwerpen = designated G7 authority; G7-certificaat voor niet-Russische natuurlijke rough ≥ 0,5 ct; export van Russische goederen toegestaan). https://www.awdc.be/g7eu-sanctions-faq
[5] Rapaport, 2026-07-12, "Antwerp's diamond trade sees positive momentum" (H1 2026: 38,9 Mct, $ 10,6 mld). https://rapaport.com/news/antwerps-diamond-trade-sees-positive-momentum/
[6] VRT NWS, 2015-08-27 (Kimberley Process: Antwerpen 234,7 Mct in+uit; India importeert meer rough dan Antwerpen, exporteert nauwelijks). https://www.vrt.be/vrtnws/p.wZbbMOyko
[7] Wikipedia, "Brussels Airport diamond heist" (Brink's-wagen uit Antwerpen, Brussels Airport, vlucht naar Zürich, 2013). https://en.wikipedia.org/wiki/Brussels_Airport_diamond_heist
[8] Wikipedia, "Surat Diamond Bourse" (DREAM City, grootste kantoorgebouw ter wereld). https://en.wikipedia.org/wiki/Surat_Diamond_Bourse
[9] Wikipedia, "Surat" (289 km ten noorden van Mumbai) — via brief `diamant-dubai-surat` [6]. https://en.wikipedia.org/wiki/Surat
[10] GJEPC Solitaire, "Antwerp Q1 rough diamond exports +40% to $2.58 billion" (alleen titel gelezen; jaar niet bevestigd). https://gjepc.org/solitaire/antwerp-q1-rough-diamond-exports-40-to-2-58-billion/
[11] Brieven `diamant-jwaneng-antwerpen`, `-ekati-antwerpen`, `-gaborone-surat`, `-dubai-surat` (ankers + kopieerbare benen; STAT Times Mumbai-freighterpauze via dubai-surat [10]).
[12] Esri World Imagery via `sat_check.py` (z15): `v2/build-cache/satcheck/sat-diamant-antwerpen-surat-{awdc,brucargo,bom-cargo,sdb}.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
Recept: `bash v2/tools/bak_stromen.sh diamant-antwerpen-surat` (functie `bak_diamant_antwerpen_surat`, patroon `bak_diamant_dubai_surat`).
Uitvoer `v2/data/stroomroute-diamant-antwerpen-surat.json` (versie 2, lonlat, 79,9 KB): **4 benen · 7.178,3 km · 4.073 punten · 4 markers**.
Geen wegscan, geen profiel, geen zee: alle benen zijn een kopie of een luchtbeen.

| # | modaliteit | km | naad naar vorig | geometrie |
|---|---|---|---|---|
| b1 | truck | 37,4 | – | omgekeerde kopie `diamant-jwaneng-antwerpen` b4 (E19 via Mechelen), 435 pt |
| b2 | lucht | 6.867,2 | 0,14 | `maak_luchtbeen.py` BRU → BOM grootcirkel, 276 pt, doorgetrokken |
| b3 | truck | 273,4 | 0,00 | letterlijke kopie `diamant-gaborone-surat` b3 (NH48), 3.360 pt |
| b4 | truck, stippel | 0,29 | 0,00 | letterlijke kopie stippel `diamant-gaborone-surat` b4 (DREAM City) |

Markers (afstand tot de lijn): dia-awdc 26 m · dia-brucargo 0 m · dia-bom-cargo 0 m · dia-sdb 0 m. Grootste naad 0,14 km (b1 naar b2).

**Toets.** b1: geen echte wegkm, hemelsbreed 34,4 km tegen 37,4 gebakken = +8,7% (indicatie, geen norm). b3: 273,4 tegen 289 km stad-tot-stad = -5,4% (indicatie).
`toets_knikken`: 39 knikken, 1 omkering die een terugloop is (153,4 graden, 8 m, 19.10609,72.85372, vlak bij het BOM-uiteinde van b3): geerfd uit de gekopieerde NH48-lijn
(`diamant-gaborone-surat` toont dezelfde terugloop), niet hier aangeraakt. `toets_rechte_benen --min-km 5`: geen melding voor deze stroom. json.load, versie 2, punt_formaat lonlat, modaliteiten {truck, lucht}, elk been >= 2 punten.

**Toelichting.**
- **Vlucht (b2):** doorgetrokken, geen stippel; "aannemelijk: één bron" en "geen directe lijndienst sinds 2018" staan in de beennaam. Grootcirkel tussen twee satelliet-gelegde vrachtterminals (BRU Brucargo, BOM CSMIA Air Cargo Complex); de claim is "van deze terminal naar die", niet "langs deze lijn". De werkelijke lading kan via een hub (Zürich, Dubai) gaan (§7).
- **Stippel (b4):** eigen verbinding zonder net (OSM-topologiegat DREAM City, 0,29 km), overgenomen uit `diamant-gaborone-surat`; niet dichtgetrokken.
- **Geen airside-stippel:** het wegbeen eindigt 0,14 km van het Brucargo-anker en 0,00 km van het BOM-anker, onder de norm.
- **Geen haven-aanloop, geen leiding, geen zee.** Fase D en E vervallen (§6).

**Lessen.** (1) Een keten uit alleen kopieën en een luchtbeen bakt in één run van ~1 minuut (alleen de 12 s MARNET/graaf-inladen als overhead); het risico zit in de richting van een gekopieerd been, niet in de router: b1 moest omgedraaid zijn (kop AWDC) zodat de naad b1 naar b2 klopt.
(2) Meet de naad nadat je een kopie omdraait: de jwaneng-uiteinden liggen 0,14 km van dia-brucargo, niet op het anker; dat is binnen de norm en is niet verschoven.
(3) De terugloop bij het BOM-uiteinde van de NH48-kopie is een bestaande bevinding van de gedeelde geometrie; wie die repareert moet alle stromen met dit been meenemen (o.a. `diamant-gaborone-surat`, `-dubai-surat`, deze), niet één.
