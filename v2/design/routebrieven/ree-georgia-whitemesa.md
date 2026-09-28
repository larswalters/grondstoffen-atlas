# Routebrief (licht) · Zeldzame aardmetalen · Van → Via → Naar (land)

**stroom-id:** `ree-georgia-whitemesa` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** monazietzand (bijproduct van de titaandioxide-mineraalzandwinning) van Chemours'
Mission Mine (Charlton County, Georgia) gaat per truck ~2.620 km hemelsbreed (geen wegkm gevonden) dwars
door het zuidoosten van de VS naar de White Mesa Mill (Energy Fuels) in Blanding, Utah, die het erts tot
een REE-carbonaat/-oxide verwerkt.
**Welke as van het verhaal:** VS mineraalzand-bijproduct → VS REE-scheiding — de enige binnenlandse
Amerikaanse monaziet-toeleveringsketen van de atlas. Chemours en Energy Fuels tekenden op 2020-12-14 een
driejarig contract voor minimaal 2.500 t/j natuurlijk monazietzand vanaf Chemours' **Offerman Mineral Sand
Plant** in Georgia [1]; recentere berichtgeving (in het ketenontwerp aangeleverd, binnen budget niet
zelfstandig geverifieerd) noemt een lager huidig volume van ~500 t/j en een doel van ≥10.000–15.000 t/j
doorvoer op de langere termijn [8].

## 1 · Ketenkaart
```
Chemours Mission Mine (heavy-mineral-sand mijn) `ree-ga-mijn`
  ──(b1 truck, aannemelijk: één keten-been voor een meerstaps proces · corridor TN–AR–OK–TX–NM–AZ→UT,
     I-40 → US-491 → US-160/163/191, vermijdt Colorado · hemelsbreed ~2.620 km, geen wegkm)──►
White Mesa Mill, Blanding (Utah) `w-whitemesa` (hergebruikt uit ree-sitelaag.json) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (aannemelijk: niet bronbevestigd voor déze rit, enige redelijke aanname over 2.600+ km binnenland) | `ree-ga-mijn` → `w-whitemesa` | Chattanooga→Nashville→Memphis→Little Rock→OKC→Amarillo→Albuquerque→Gallup (I-40), dan US-491→US-160/163→US-191 naar Blanding | hemelsbreed 2.620,4 km, geen wegkm gevonden binnen budget | maak_stroombeen_weg (extracts us-georgia/tennessee/arkansas/oklahoma/texas/new-mexico/arizona/utah) | mogelijk last-mile bij `ree-ga-mijn` (zie §7) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-ga-mijn` | mijn / laadplek | Chemours Mission Mine (heavy-mineral-sand surface mine; erts gaat naar het Offerman-scheidingsproces) | 31.0276, -81.9772 | [2][3] NPDES-permit GA0050275, Wastewater Regulatory Program-memo, outfall 001 lat/long | bron-gelegd (z15 gezien: waterbekken/bezinkvijver direct aan het punt, met ~1,5 km noordelijker een uitgestrekt lichtgekleurd, kaalgemaakt mijnterrein met meerdere rechthoekige bekkens — consistent met de "floating wet mill"-verwerking die het permit beschrijft [3]; geen exact ankerpunt op de put zelf, want die "beweegt continu mee met het ertslichaam" [3]) |
| `w-whitemesa` | losplek / raffinaderij | White Mesa Mill (Energy Fuels), Blanding, Utah | 37.5323, -109.5098 | hergebruikt letterlijk uit `v2/design/ree-sitelaag.json` (id `w-whitemesa`) en `ree-mountainpass-fortworth.md`-patroon | bron-gelegd (overgenomen, niet opnieuw gecheckt) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Chattanooga, TN (I-75/I-24-knoop) | 35.0456, -85.3097 | pint de noordelijke I-24-corridor i.p.v. een rechtstreekse route door Alabama/Mississippi |
| b1 | 2 | Nashville, TN (I-24/I-40-knoop) | 36.1627, -86.7816 | overstap I-24 → I-40 westwaarts |
| b1 | 3 | Memphis, TN (I-40, Mississippi-oversteek) | 35.1495, -90.0490 | pint de doorgaande I-40-corridor over de rivier |
| b1 | 4 | Little Rock, AR (op I-40) | 34.7465, -92.2896 | doorgaande I-40-corridor door Arkansas |
| b1 | 5 | Oklahoma City, OK (op I-40) | 35.4676, -97.5164 | doorgaande I-40-corridor, sluit een zuidelijkere I-20/I-30-route uit |
| b1 | 6 | Amarillo, TX (op I-40) | 35.2220, -101.8313 | doorgaande I-40-corridor door de Texas Panhandle |
| b1 | 7 | Albuquerque, NM (op I-40) | 35.0844, -106.6504 | pint I-40 door New Mexico i.p.v. afbuigen via I-25 noordwaarts (Colorado) |
| b1 | 8 | Gallup, NM (I-40/US-491-knoop) | 35.5281, -108.7426 | overstap I-40 → US-491 noordwaarts; vanaf hier via Shiprock (US-64) → Kayenta AZ (US-160/163) → Bluff/Blanding UT (US-191) — deze laatste ~400 km liggen buiten het 8-punten-budget en zijn geen eigen via-punt geworden (open punt, zie §7) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| White Mesa Mill | Energy Fuels | monazietzand → REE-carbonaat (~71% TREO droge basis), uranium als bijproduct | contract-minimum 2.500 t/j monaziet (2021); doel ≥10.000–15.000 t/j doorvoer op termijn (recentere, binnen budget niet geverifieerde cijfers uit het ketenontwerp) | [1][8] |

## 6 · Stoppunt
De brief stopt bij White Mesa Mill: dat is de enige gedocumenteerde bestemming in het ketenontwerp. Fase D
(scheiding van het REE-carbonaat tot losse oxiden/metalen, of een magneetfabriek als afnemer) is in geen van
de beschikbare bronnen met naam en adres genoemd — Energy Fuels' eigen 2025-berichtgeving over terbiumoxide
suggereert dat verdere scheiding **op dezelfde site** gebeurt (geen apart been nodig), maar dat is binnen dit
budget niet onafhankelijk bevestigd. Fase E vervalt.

## 7 · Open punten
- **Exacte scheidingsfabriek (Offerman Mineral Sand Plant, Pierce County GA) niet gevonden binnen budget.**
  De SEC 8-K van 2020-12-14 noemt expliciet dat het monaziet fysiek gescheiden wordt bij Chemours' **Offerman
  Mineral Sand Plant** [1] — dát is strikt genomen het echte verladingspunt, niet de mijn zelf. Drie
  WebSearch-pogingen en Nominatim/Photon/Overpass leverden geen bedrijfsadres of coördinaat op (Overpass was
  onbereikbaar vanaf deze machine); Nominatim gaf alleen de hamlet-centroïde van Offerman (31.4097,-82.1118),
  die uitdrukkelijk **geen anker** mag zijn. Deze brief gebruikt daarom Chemours' **Mission Mine**
  (Charlton County) als site-niveau-anker voor de oorsprong — een echte, satelliet-bevestigde Chemours
  mijnlocatie in dezelfde regio die volgens haar eigen NPDES-vergunning erts levert voor "off-haul to offsite
  dry mill (mineral sand plant)" [3], maar niet per se de exacte plek waar het monaziet zelf de weg op gaat.
- **Welke vestiging(en) precies leveren blijft open.** Chemours heeft in de regio meerdere actieve
  mijnen (Mission Mine, Charlton County [2][3]; Amelia A&B Mine, Wayne County, met eigen outfall op
  31.6403,-81.9587 [4][5]) plus de Trail Ridge South-mijn in Clay County, Florida [6]; geen bron koppelt
  het Energy Fuels-contract aan één specifieke mijn.
- **Jaarvolume-discrepantie (haalbaarheidstoets, bindend als open punt, niet als tooling-probleem):** het
  2020-contract noemt een minimum van 2.500 t/j [1]; het ketenontwerp geeft daarnaast een recenter, binnen dit
  budget niet zelfstandig geverifieerd cijfer van ~500 t/j actueel en een langetermijndoel van ≥10.000 t/j
  doorvoer [8] — de twee zijn niet met elkaar verzoend.
- **Geen gepubliceerde wegkilometer gevonden**; §2 gebruikt de hemelsbrede afstand (2.620,4 km) tussen de
  gekozen ankers, met de indicatie dat de ±15%-toets hier niet als norm geldt.
- **Mogelijke last-mile-stippel bij `ree-ga-mijn`:** een heavy-mineral-sand-mijn verplaatst zich continu
  langs het ertslichaam [3] en ligt op een groot, deels onverhard mijnterrein; of het ankerpunt binnen ~2 km
  van het OSM-wegnet ligt is niet gecontroleerd (geen geometrie-bake in deze opdracht) — de bak-agent moet dit
  bij `maak_stroombeen_weg.py` checken en zo nodig een korte stippel "last mile (geen net op deze korrel)"
  toevoegen.
- **Modaliteit b1 (truck) is een aanname**, niet in een bron bevestigd voor déze specifieke 2.600+ km-rit.

## 8 · Bronnen
[1] Energy Fuels Inc., Form 8-K (SEC, item 8.01), 2020-12-14: driejarig contract met Chemours, minimum
2.500 t/j natuurlijk monazietzand uit Chemours' Offerman Mineral Sand Plant (Georgia), verwerking bij White
Mesa Mill vanaf Q1-2021 — https://www.sec.gov/Archives/edgar/data/1385849/000106299320006295/form8k.htm
[2] Georgia EPD, NPDES-vergunning GA0050275 (The Chemours Company FC, LLC – Mission Mine), draft-permit
cover letter 2026-02-13: faciliteitsadres 1682 South Tyler Field Road, Nahunta, Georgia 31553, Charlton
County, Satilla River Basin — https://geos.epd.georgia.gov/GA/GEOS/Public/EnSuite/Shared/pages/util/StreamDoc.ashx?id=1092188&type=PERMIT_FILLED_OBJECT
[3] Georgia EPD, Wastewater Regulatory Program — Waste Load Allocation-memo voor Mission Mine (NPDES
GA0050275): outfall 001 lat/long 31°1'39,48"N / 81°58'37,81"W, procesomschrijving "floating wet mill" en
"off-haul to offsite dry mill (mineral sand plant)" — zelfde document als [2]
[4] Georgia EPD, NPDES-vergunning GA0050250 (The Chemours Company FC, LLC – Amelia A & B Mine), draft-permit
cover letter 2023-12-13: faciliteitsadres 892 Power Line Road, Jesup, Georgia 31545, Wayne County, Altamaha
River Basin; outfall 0011 op 31,617631 / -81,941978 — https://geos.epd.georgia.gov/GA/GEOS/Public/EnSuite/Shared/pages/util/StreamDoc.ashx?id=1098407&type=PERMIT_FILLED_OBJECT
[5] Georgia.org / kantoor gouverneur Kemp, persbericht 2020-09-22: Chemours breidt uit in Wayne County
(Georgia), $86 mln investering — https://georgia.org/press-release/kemp-welcomes-chemours-wayne-county-86-million-investment-creates-78-new-jobs
[6] Chemours, persbericht 2022: start van de Trail Ridge South mineral sand mine, Clay County, Florida
(~$93 mln investering) — https://www.chemours.com/en/news-media-center/all-news/press-releases/2022/chemours-begins-operation-of-trail-ridge-south-mineral-sand-mine-in-florida
[7] SEC EDGAR, bedrijfsdossier Energy Fuels Inc. (CIK 0001385849) — gebruikt om de 8-K van 2020-12-14 te
lokaliseren en te dateren — https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001385849&type=8-K&owner=include&count=100
[8] Ketenontwerp (aangeleverde jaarvolume-noot, binnen dit budget niet zelfstandig geverifieerd): Energy
Fuels investor-nieuws 2025-07-17 en 2025-09-09 over eerste terbiumoxide-productie en een doorvoerdoel van
~10.000 t/j monaziet bij White Mesa Mill — algemene bron: https://www.energyfuels.com/investors
[9] OpenStreetMap/Nominatim, geocode "Offerman, Georgia" → hamlet-centroïde 31,40966 / -82,11179 (Pierce
County) — uitsluitend gebruikt om de regio te bevestigen, NIET als anker —
https://nominatim.openstreetmap.org/

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Stroom:** `ree-georgia-whitemesa` · **bestand:** `v2/data/stroomroute-ree-georgia-whitemesa.json` (578,4 KB) ·
**functie:** `bak_ree_georgia_whitemesa()` in `v2/tools/bak_stromen.sh` · **registerregel:** `{ sleutel: "ree-gw", bestand: "stroomroute-ree-georgia-whitemesa.json", grondstof: "ree", aan: true }`

| # | modaliteit | km | punten | naad met vorige been | stippel? |
|---|---|---|---|---|---|
| b1 | truck | 3.518,5 | 28.111 | — (1e/enige been) | nee |
| **totaal** | | **3.518,5** | **28.111** | | 2 markers |

Eén been (b1, truck), gebakken met `python v2/tools/maak_stroombeen_weg.py --profiel ree-georgia-whitemesa-ga-utah
--bron geofabrik` over 8 extracts (us-georgia/tennessee/arkansas/oklahoma/texas/new-mexico/arizona/utah, 2,1 GB,
536 s scan) en als `--been-geojson` in `hecht_marnet.py route` opgenomen (geen routering over de zee-/spoorgraaf —
de geometrie komt letterlijk uit het gescande wegbestand). Geen zeebenen, dus geen haven-aanloop; geen spoornet;
geen fase D/E (brief §6: stoppunt bij White Mesa Mill).

**Km-toets (brief §2/§7: geen gepubliceerde wegkm, referentie geen norm):**
- Gemeten weggeometrie **3.518,5 km** tegen hemelsbreed **2.620,4 km** = **+34,3%**. Dit is GEEN afwijking van een
  norm (de brief geeft zelf al aan dat de ±15%-toets hier niet geldt): een 2.600+ km I-40/US-491/160/163/191-corridor
  die bewust om Colorado heen buigt volgt per definitie geen grootcirkel, en +34% weg-t.o.v.-hemelsbreed is normaal
  voor zo'n lange, bochtige binnenlandse rit (vergelijkbaar met `ree-mountainpass-fortworth`, dat ~2.250 km weg
  tegen een kortere hemelsbrede referentie legde).

**Twee open bake-vragen uit `bak_aanwijzingen` opgelost:**
1. **Corridorstuk Gallup → White Mesa (~400 km, buiten het 8-punten-budget van de brief-§4-tabel):** opgelost door
   TWEE extra via-punten toe te voegen aan het `PROFIELEN`-recept (niet aan de brief zelf) — Shiprock NM
   (36,7856/-108,6871, US 491/US 64-knoop) en Kayenta AZ (36,7278/-110,2568, US 160/163-knoop) — met `vensterKm: 60`.
   Beide pinnen het US 491 → US 160/163 → US 191-tracé; geen omweg gemeten (snap 0,02→0,36 km op alle vier de
   nieuwe/bestaande knopen in dat stuk).
2. **Ankersnap Mission Mine (mogelijke last-mile, mijn "beweegt continu mee met het ertslichaam"):** GEEN
   last-mile-stippel nodig. Gemeten snap plant → weg **0,07 km**, weg → kade (White Mesa) **0,36 km** — beide ruim
   binnen de 0,5 km-marker-norm. `eindKlassen` incl. `track` + `eindToegangPrivaat: True` in het profiel volstonden:
   first mile 6,95 km over kleine wegklassen (service/tertiary/track), last mile 1,67 km (service).

**Markers (2, beide op het beenuiteinde, snap ≈ 0 km):**
- `ree-ga-mijn` (31,0276 / -81,9772) — kop, snap 0,07 km.
- `w-whitemesa` (37,5323 / -109,5098) — staart, snap 0,36 km (hergebruikt anker uit `ree-sitelaag.json`, niet
  opnieuw satelliet-gecheckt, conform de bak-aanwijzing).

**Toets (bakhandleiding-licht §5):**
- `toets_knikken.py --bestand stroomroute-ree-georgia-whitemesa.json` — 62 knikken ≥ 60° (vrijwel allemaal
  OSM-spikes/krappe bochten op een normale wegkartering over 3.518 km), **3 omkeringen ≥ 150°**, waarvan **1
  TERUGLOOP**: bij 35,15203/-90,04510 (vlak bij de Memphis-Mississippi-oversteek, exact op het via-punt "Memphis
  TN, I-40, Mississippi-oversteek"), verhouding pad/hemelsbreed lokaal 2,6 — een OSM-interchange/brugoprit-lus op
  de I-40-kruising, geen via-punt-fout (het via-punt zelf ligt correct op de doorgaande weg, snap 0,02→0,23 km).
  **Bevinding, niet gerepareerd** (§bakhandleiding: "buiten de norm = bevinding, geen via-punt bijschuiven").
- `toets_rechte_benen.py --min-km 5` — `ree-georgia-whitemesa` verschijnt NIET in de lijst van verdachte rechte
  stukken (het enige been heeft 28.111 punten en een omwegfactor ver van 1,000).
- `json.load` slaagt, `versie` 2, `punt_formaat` `lonlat`, modaliteit `truck` (bekende set), been ≥ 2 punten.
  **Bestandsgrootte 578,4 KB — BOVEN de ~300 KB-indicatie** uit de handleiding (§5). Bevinding: `maak_stroombeen_weg.py`
  kent geen simplify-stap voor `--been-geojson`-benen (de geometrie komt 1-op-1 uit de gescande OSM-ways); een
  vergelijkbaar lang wegbeen (`ree-mountainpass-fortworth`, ~2.250 km) is met 267,7 KB wel kleiner — mogelijk meer
  kruispunt-dichte stadstrajecten (Nashville/Chattanooga/Little Rock/OKC/Amarillo binnenstad-interchanges) in deze
  corridor. Niet gefixt (gedeeld tool, geen simplify-vlag beschikbaar); gemeld als bevinding, geen fout.

**Gereedschapslessen:**
- Geen "geen wegpad"-fout op de volledige 2.600+ km-corridor over 8 staten in één `--profiel`-run; het ruime
  venster (60 km) en de twee extra via-punten (Shiprock/Kayenta) vingen het laatste, budget-overschrijdende
  brief-stuk zonder tweede poging.
- De 8-extracts-scan (2,1 GB, us-texas als "reus"-extract) nam 536 s in beslag onder het weg+reus-slotsysteem
  (gedeeld met ~14 parallelle agenten) — ruim binnen de 600.000 ms-Bash-timeout, geen achtergrondrun nodig.
- 43 keerlussen (dubbel-gereden stukken) automatisch gesnoeid door `snoei_keerlussen` (3.533,8 → 3.518,0 km vóór
  de anker-verbindingsstukjes); de grootste bij Little Rock AR (7,61 km) — normaal gedrag van het wegtool, geen
  aparte actie nodig.

**Open punten (ongewijzigd t.o.v. §7, bevestigd/aangevuld bij het bakken):** de exacte Offerman Mineral Sand
Plant-coördinaat blijft ongevonden (Mission Mine blijft het site-anker); welke Chemours-vestiging(en) precies
leveren blijft open; de jaarvolume-discrepantie (2.500 t/j contractminimum vs ~500 t/j actueel vs ≥10.000-15.000 t/j
langetermijndoel) is niet verzoend; geen gepubliceerde wegkilometer gevonden (§2 gebruikt hemelsbreed 2.620,4 km,
nu bevestigd tegen een gemeten wegtracé van 3.518,5 km); modaliteit truck blijft een aanname; fase D/E blijft
vervallen (brief §6). Nieuw uit het bakken: één OSM-interchange-terugloop bij de Memphis-oversteek (zie toets
hierboven) en het bestandsgroottepunt (578,4 KB, boven de ~300 KB-indicatie).
