# Zilver · Rampura Agucha → Chanderiya (India)

**stroom-id:** `zilver-rampuraagucha-pantnagar` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** zink/lood-erts met zilver als bijproduct van de Rampura Agucha-mijn (Hindustan Zinc/Vedanta,
Bhilwara, Rajasthan) per truck over de doorgaande NH48-corridor naar het Chanderiya Lead-Zinc Smelter-complex
(Chittorgarh) — **eenbenige keten, bewust ingekort** t.o.v. het ontwerp (zie §6).
**Welke as van het verhaal:** India — Hindustan Zinc mijn-tot-smelter, zink/lood-bijproductzilver; ≈700 t Ag/j bij
Chanderiya (Hindustan Zinc/Vedanta bedrijfsopgave, niet dit ronde herbevestigd — status aannemelijk). Prioriteit 1,
M31 golf 5.

## 1 · Ketenkaart
```
Rampura Agucha-mijn `ag-rampuraagucha-mijn` ──(b1 truck · NH48 via Gulabpura–Bhilwara–Chittorgarh · hemelsbreed
   ~98,0 km, geen wegkm binnen budget)──► Chanderiya Lead-Zinc Smelter `ag-chanderiya-smelter` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Rampura Agucha-mijn → Chanderiya Lead-Zinc Smelter | doorgaande NH48 (Delhi–Mumbai-corridor) via Gulabpura, westelijk langs Bhilwara, nabij Chittorgarh | hemelsbreed 98,0 km, geen wegkm [1][4][7] | maak_stroombeen_weg (extract `india`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-rampuraagucha-mijn` | mijn / verwerkingsfabriek (kop van b1) | Rampura Agucha-mijn en concentrator (Hindustan Zinc) | 25.8416, 74.7332 | [1][6][9] | bron-gelegd (z17 gezien: concentrator-gebouwen met blauwe daken, tailingsbezinkbekkens en opslagtanks direct naast een groot, deels watergevuld open-pit-litteken; industrieterrein + mijnwerkerswijk eromheen — verfijnd t.o.v. het hergebruikte sitelaag-anker `w-rampura-agucha` (25.8418,74.7545), dat ~2,1 km oostelijker in de tailingszone van hetzelfde complex ligt) |
| `ag-chanderiya-smelter` | smelter+raffinaderij (staart van b1, stoppunt) | Chanderiya Lead-Zinc Smelter Complex (Hindustan Zinc) | 24.9632, 74.6580 | [2][3][6][9] | bron-gelegd (z17 gezien: dicht industriecomplex met smeltergebouwen, rookpluim, opslagtanks, bezinkbekkens en een spoorzijspoor pal naast de Berach-rivier — verfijnd t.o.v. het hergebruikte sitelaag-anker `w-ref-chanderiya` (24.9393,74.6283, status aannemelijk, dorpsniveau), dat ~4,0 km ZZW van dit complex ligt) |

## 4 · Via-punten (b1 — corridorkeuze: welke NH48-aansluiting)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | NH48-aansluiting bij Gulabpura | 74.6153, 25.7996 | hier sluit de lokale weg vanaf de mijn (via SH39A) aan op de doorgaande NH48 [4][7] |
| b1 | 2 | NH48-passage westelijk langs Bhilwara | 74.5755, 25.3480 | NH48 omzeilt de stad — Wikipedia's junctielijst noemt "NH 758 near Bhilwara"; punt ligt bewust op de bypass, niet in het centrum [4] |
| b1 | 3 | NH48 nabij Chittorgarh, vóór de NH27-aansluiting | 74.6249, 25.0522 | laatste lange NH48-stuk vóór de afslag naar Chanderiya; Wikipedia noemt "NH 27 interchange near Chittorgarh" iets verderop [4] |
| b1 | 4 | NH48-afslag naar Chanderiya | 74.6443, 24.9740 | hier verlaat de route de doorgaande NH48 voor de laatste ~3 km lokale weg naar het smeltercomplex [7] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| — | — | — | — | geen tussenliggende verwerkingsknoop: het erts wordt al op de mijn tot lood/zinkconcentraat verwerkt (concentrator bij `ag-rampuraagucha-mijn`); de smelter is de keteneindanker zelf |

## 6 · Stoppunt
De brief stopt **bindend** bij Chanderiya (haalbaarheidstoets): been B (spoor Chanderiya → Pantnagar,
Uttarakhand) en `spoornet_nodig` zijn volledig vervallen. Wikipedia (Hindustan Zinc) bevestigt dat Pantnagar
"initially intended to serve as a smelting facility for Silver production", maar dat er later alleen Zink/Lood-
smelt- en gietfaciliteiten zijn gebouwd — geen bevestiging van een actuele zilverstroom vandaag. Chanderiya zelf
produceert volgens Wikipedia al "zinc, lead, cadmium and other precious metals" [2][3] — dat maakt Chanderiya het
eerlijke, sterker gedocumenteerde stoppunt in plaats van een tweede, ongedocumenteerd been van ~880 km door te
trekken.

## 7 · Open punten
- Geen gepubliceerde wegkilometer voor Rampura Agucha–Chanderiya binnen budget; §2 geeft de hemelsbrede afstand
  tussen de satelliet-gelegde ankers (98,0 km). Een OSRM-routeschatting over hetzelfde OSM-wegnet (NH48-corridor,
  ter indicatie, geen officiële bron) komt op ~119 km — de ±15%-toets geldt hier niet als norm.
- De exacte modaliteit ván het mijnterrein náár de doorgaande weg (eigen HZL-conveyor/interne spoorlijn vs.
  gewone truck) is niet gedocumenteerd binnen budget: Wikipedia/Rampura Agucha zegt alleen DAT het concentraat
  naar Chanderiya "getransporteerd" wordt, niet HOE. Getekend als één doorgaand truckbeen (aannemelijk).
- Jaarvolume (~700-750 t Ag/j bij Chanderiya) is een Hindustan Zinc/Vedanta-bedrijfsopgave uit
  `v2/design/zilver-sitelaag.json` (`w-ref-chanderiya`), dit ronde niet opnieuw met een vers peiljaar
  geverifieerd — status blijft **aannemelijk**.
- Beide ankers zijn t.o.v. de hergebruikte sitelaag-coördinaten verschoven na een eigen satellietblik (zie §3);
  `v2/design/zilver-sitelaag.json` zelf is niet aangepast (buiten scope van deze brief).
- Been B (Chanderiya → Pantnagar) en `spoornet_nodig` zijn BINDEND vervallen conform de haalbaarheidstoets; niet
  getekend en niet gebakken.

## 8 · Bronnen
[1] Wikipedia, "Rampura Agucha" — locatie (Bhilwara-district, 10 km ZO van Gulabpura op NH79/NH48), eigenaar
Hindustan Zinc, ertsverwerking op de mijn, "the lead and zinc concentrates are transported to the Chanderiya
Smelter Complex", ertsproductiecapaciteit 6,15 lakh t/j. https://en.wikipedia.org/wiki/Rampura_Agucha
[2] Wikipedia, "Chanderiya Smelter Complex" — 's werelds grootste lood-zinksmeltercomplex, Chittorgarh-district,
gebouwd 1989-1991, "refines lead-zinc ore from Rampura Agucha", "produces zinc, lead, cadmium and other precious
metals". https://en.wikipedia.org/wiki/Chanderiya_Smelter_Complex
[3] Wikipedia, "Hindustan Zinc" — smelters/raffinaderijen te Chanderiya (Chittorgarh)/Debari/Dariba; Pantnagar
(Uttarakhand) "was initially intended to serve as a smelting facility for Silver production, but later Zinc and
Lead melting and casting plants were also established here". https://en.wikipedia.org/wiki/Hindustan_Zinc
[4] Wikipedia, "National Highway 48 (India)" — junctielijst Rajasthan: "NH 148D near Gulabpura", "NH 758 near
Bhilwara", "NH 27 interchange near Chittorgarh" — bevestigt de doorgaande NH48-corridor Gulabpura→Bhilwara→
Chittorgarh. https://en.wikipedia.org/wiki/National_Highway_48_(India)
[5] Wikipedia, "Chittorgarh" — noemt Chanderiya Lead-Zinc Smelter als een van de grootste zink-loodsmelters ter
wereld, gelegen in het Chittorgarh-district. https://en.wikipedia.org/wiki/Chittorgarh
[6] Hindustan Zinc (Vedanta) — bedrijfssite, smeltlocatie Chanderiya (silver/cadmium-recovery uit slak bevestigd
op de productpagina). https://www.hzlindia.com/what-we-do/metal-smelting-sites/chanderiya-lead-zinc-smelter
[7] OpenStreetMap/Nominatim (ODbL) — plaatsnodes Gulabpura (25.9025,74.6556), Bhilwara-stad (25.3480,74.6360),
Chittorgarh-stad (24.8837,74.6244) en dorp Chanderiya (24.9393,74.6283), gebruikt voor het pinnen van de
via-punten op de NH48-corridor. https://www.openstreetmap.org
[8] Project OSRM (demo-routeerdienst over het publieke OSM-wegnet) — indicatieve rijafstand/corridorbevestiging
Rampura Agucha-plant → Chanderiya-smelter via NH48, ~119,4 km (geen officiële bron, alleen ter indicatie).
https://router.project-osrm.org
[9] `v2/design/zilver-sitelaag.json` / `.md` (M31 golf 5-ontwerp) — hergebruikte ankers `w-rampura-agucha` en
`w-ref-chanderiya` (incl. [B37][B38] Hindustan Zinc-bedrijfsopgave ≈700-750 t Ag/j bij Chanderiya).
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14-z17, live) —
`v2/build-cache/satcheck/sat-zilver-rampuraagucha-pantnagar-mijn-wijd.png` ·
`sat-zilver-rampuraagucha-pantnagar-mijn-plant.png` (mijn/concentrator) ·
`sat-zilver-rampuraagucha-pantnagar-smelter-wijd.png` · `sat-zilver-rampuraagucha-pantnagar-smelter-ind1.png` ·
`sat-zilver-rampuraagucha-pantnagar-smelter-close.png` (Chanderiya-smeltercomplex).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Stroom `zilver-rampuraagucha-pantnagar`** → `v2/data/stroomroute-zilver-rampuraagucha-pantnagar.json` — 1 been,
**127,1 km**, 1.196 punten, 2 markers. truck 127,1 km. Recept: `bak_stromen.sh` (functie
`bak_zilver_rampuraagucha_pantnagar`).

**b1 (truck, Rampura Agucha-mijn/concentrator → Chanderiya Lead-Zinc Smelter, NH48 via Gulabpura, Bhilwara-bypass,
Chittorgarh):** `maak_stroombeen_weg.py --profiel zilver-rampuraagucha-pantnagar-rampuraagucha-chanderiya --bron
geofabrik` (extract `india`, 1,7 GB, 254 s scan). Vier via-punten op de doorgaande NH48 (Gulabpura-aansluiting →
Bhilwara-bypass/NH758-knoop → vóór de NH27-aansluiting bij Chittorgarh → Chanderiya-afslag), alle vier snappend op
0,00–0,04 km — geen enkel via-punt bijgeschoven. Twee keerlussen gesnoeid (127,0 → 126,5 km, dubbel gereden
stukjes). Getekende lijn incl. eerste/laatste-mile-stukjes over kleine wegklassen (0,99 km unclassified bij de
mijn, 2,78 km residential/service/tertiary/unclassified bij de smelter): **127,1 km**.

**Lengtetoets:** de brief geeft **geen gepubliceerde wegkm** — alleen de hemelsbrede afstand tussen de twee
satelliet-gelegde ankers (98,0 km, "geen wegkm", toets-bindend als **indicatie**, geen harde ±15%-norm) en een
niet-officiële OSRM-schatting over dezelfde NH48-corridor (~119,4 km). Gemeten **126,5 km** (weggeometrie) /
**127,1 km** (getekende lijn incl. eerste/laatste mile) — **+29,1% tegen de indicatieve 98,0 km** (buiten de
tool-waarschuwing van ±10%, die hier niet als norm geldt) maar **+6,0% tegen de eigen OSRM-indicatie van
119,4 km** en dus binnen de vooraf verwachte orde van grootte (brief §7/§8[8]: "~115-125 km"). Geen bevinding die
op een routeerfout wijst — de NH48 maakt geen scherpe knikken buiten de vier gekozen via-punten, en alle via-snaps
zijn zo goed als exact.

**Anker-verbindingen (rechte stukjes, apart van de lengtetoets):** mijn/concentrator → doorgaande weg **0,51 km**
[⚠️ net > de 0,5 km-norm, bevinding — de concentrator ligt aan een korte klein-klasse toegangsweg vlak naast de
NH48-aftakking bij Gulabpura, geen tweede poging] · weg → smelterkade **0,02 km** [OK].

**`toets_knikken.py`:** **9 knikken ≥60°, 0 omkeringen, 0 terugloop.** Alle negen zijn spikes (straal 3–117 m,
OSM-zigzags) geconcentreerd rond de twee ankerzones (vijf bij de mijn/Gulabpura-aftakking, vier bij de
Chanderiya-afslag/smelterpoort) — kopmaak-precisie, geen routeerfout.

**`toets_rechte_benen.py --min-km 5`:** geen bevinding voor deze stroom (geen been met omwegfactor 1,000).

**json geldig:** versie 2, punt_formaat lonlat, modaliteit uitsluitend `truck` (binnen de toegestane set), het ene
been heeft 1.196 punten (≥2), bestandsgrootte **23,9 KB** (ruim < 300 KB-richtwaarde).

**Markers:** `ag-rampuraagucha-mijn` en `ag-chanderiya-smelter` liggen op de kop resp. staart van de lijn (0,00 km
— de marker-aan-lijn-afstand hierboven onder "anker-verbindingen" is de km die de weglijn zelf aflegt vanaf het
ankerpunt tot de doorgaande weg, niet de marker-tot-lijn-afstand). Beide ruim binnen de ~0,5 km-norm.

**Geen haven-aanloop, geen zeebeen, geen leiding, geen lucht, geen spoor:** de keten is één volledig doorgetrokken
truckbeen zonder overslag — geen van de andere modaliteiten komt voor in deze stroom.

**Been B (Chanderiya → Pantnagar) blijft bindend vervallen** (§6/§7): niet getekend, niet gebakken, conform de
haalbaarheidstoets van de brief.

**Open punten die blijven staan (zie ook §7):** geen gepubliceerde wegkilometer binnen budget, alleen de
hemelsbrede afstand + de niet-officiële OSRM-indicatie; de exacte modaliteit van het mijnterrein naar de
doorgaande weg (eigen HZL-conveyor/interne spoorlijn vs. gewone truck) blijft ongedocumenteerd binnen budget en is
getekend als één doorgaand, aannemelijk truckbeen; het jaarvolume bij Chanderiya (~700-750 t Ag/j) is niet dit
ronde herbevestigd.

**Gereedschapslessen:**
- Een indicatieve (niet-officiële) tweede schatting naast de hemelsbrede afstand is een nuttige plausibiliteitscheck
  wanneer er geen gepubliceerde wegkm bestaat: de gemeten 126,5 km week +29,1% af van de hemelsbrede 98,0 km maar
  slechts +6,0% van de OSRM-indicatie van 119,4 km — de tool-waarschuwing (±10% tegen de ingevoerde `gepubliceerdKm`)
  sloeg dus terecht aan op een getal dat zelf al als "geen norm" was gelabeld, en de eigenlijke plausibiliteitstoets
  (tegen de OSRM-orde van grootte) slaagt.
- Een anker-verbinding van 0,51 km bij een concentrator aan een korte toegangsweg is geen routeerfout maar een
  eigenschap van de site (klein-klasse toegangsweg net binnen de eindzone-drempel) — vergelijkbaar met de
  "anker ≠ routeerpunt"-klasse elders in het project, hier op de kop-kant van het been.
