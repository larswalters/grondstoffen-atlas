# Routebrief · kolen (cokes-/stoomkool) — Cerrejón → staal thyssenkrupp Duisburg (Colombia → Duitsland)

**stroom-id:** `kolen-cerrejon-ruhr`  ·  **geschreven:** 2026-07-24 (fase A–C)  ·  **herschreven naar het mijn-tot-eindproduct-format + fase D/E toegevoegd:** 2026-07-29  ·  **status brief:** in toets
**Keten in één zin:** steenkool uit de Cerrejón-dagbouw (La Guajira), per eigen normaalspoor 150 km naar Puerto Bolívar, per capesize over de Atlantische Oceaan naar de EMO-terminal op de Maasvlakte, per duwstel 240 km sluisvrij over Hartelkanaal–Oude Maas–Merwede–Waal–Rijn naar het Werkshafen Schwelgern (Duisburg), daar per transportband naar de Kokerei Schwelgern (kolen → cokes), per band naar de hoogovens Schwelgern 1/2 (cokes + erts → ruwijzer), en per torpedowagen over het werkspoor naar het Oxygenstahlwerk (ruwijzer → staal) — waar de kolen als grondstof ophouden te bestaan.

*Volgens `../routebrief-werkwijze.md`. De brief loopt door tot het EINDPRODUCT — hij stopt niet
bij de loskade. Elk been draagt dezelfde bewijslast, ook het laatste.*

*Doel: **zelfverificatie** — brief + eigen satellietpass maken de keten controleerbaar; alleen §5
(openstaande punten) komt bij Lars terug. **Notatie (hard):** coördinaten altijd **lat, lon** met
**decimale punt**; ankers 5 decimalen, passages 2–4. Elk been draagt een **been-id**
`kolen-cerrejon-ruhr-b<n>`; ankers dragen waar mogelijk het id uit `aansluitingen.json`.*

*Toets-doel (uit de oorspronkelijke brief, 2026-07-24): de atlas routeerde deze stroom toen als
trein 146 km → zee 8.231 km → binnenschip 254 km via EMO → Beerkanaal → Hartelkanaal → Oude Maas →
Rijn (`?v=071`, 0 gaten). Deze brief is de onafhankelijke controle van die corridor. ⚠️ Die
getallen horen bij het netstadium van `?v=071` (24 juli) — bij hermeten altijd gereedschap, beide
eindpunten en netstadium noemen.*

---

## 1 · Ketenkaart

```
laadlus Cerrejón ──(b1 spoor 150 km)──► Puerto Bolívar ──(b2 zee ±8.231 km)──► EMO Maasvlakte
 `coal-cerrejon-laad`⚠️§6              `coal-bolivar-kade`                     `coal-rotterdam-kade`
                                                                                │ alternatief: EECV Dintelhaven
                                                                                │ (tk-eigen kolenterminal, aandeel onbekend →§5)
                          ──(b3 Rijn 240 km, sluisvrij)──► Werkshafen Schwelgern  `coal-duisburg-kade`
                          ──(b4 band ±0,8 km)──► Kokerei Schwelgern (kolen → cokes)
                          ──(b5 band ±1,0 km)──► Hochofens Schwelgern 1/2 (cokes+erts → ruwijzer)
                                                  │ vertakking: deel v/d cokes per wagon → Hochofen 8 Hamborn (→§5)
                          ──(b6 werkspoor ±1,3 km, torpedowagens)──► Oxygenstahlwerk 1 Bruckhausen
                                                  │ tweede afnemer: Oxygenstahlwerk 2 Beeckerwerth (±3,4 km)
                                                  ▼
                                        KETEN-EIND: ruwstaal (brammen/warmband = stáálstroom, eigen brief)
  ◄── samenvloeiing op het complex: ijzererts + PCI-injectiekolen komen over dezelfde kade binnen — geen eigen brief (nog)
```

| | |
|---|---|
| **Fasen** | A mijn → zeehaven (b1) · B zee (b2) · C aanlanding → verwerker/kokerei (b3+b4) · D cokes → hoogovens (b5) · E ruwijzer → staal (b6) |
| **Benen** | 6 (doorlopend genummerd) |
| **Overslagen** | 3 grote met elk een eigen blok (Puerto Bolívar · EMO · Schwelgern-kade); de drager-wissels op het tk-terrein (band → oven, torpedowagen) staan als terreinstappen in b4–b6 |
| **Gedeelde benen** | geen (geen andere brief gebruikt deze corridor; de kóper-stroom `koper-lobito-duisburg` eindigt 7 km zuidelijker in Ruhrort — bewust een ánder anker) |
| **Vertakkingen** | na been 5 gaat een deel van de cokes per wagon naar Hochofen 8 (Hamborn/Bruckhausen) — zelfde eigenaar, geen eigen stroom-id; aandeel onbekend (§5) |
| **Reële alternatieven** | laadzijde been 3: het maatgevende thyssenkrupp-duwverkeer laadt primair bij **EECV Dintelhaven** (±7 Mt kolen/j), niet bij EMO — zie het alternatief-blok bij de EMO-overslag; aandeel onbekend (§5) |

## 2 · Productvormen per fase — wat beweegt er fysiek

| fase | product | vorm / verpakking | gehalte of specificatie | omzetting in de volgende stap | jaarvolume |
|---|---|---|---|---|---|
| A | steenkool (hoogcalorische bitumineuze kool; thermische + PCI-kwaliteiten) | bulk; treinen 100–150 wagons à 110 t [A9][A10] | exacte spec niet vastgesteld (§5) | → zeebulk | mijnexport: niet vastgesteld in deze brief (§5); ±7 treinen/dag [A9] |
| B | idem | capesize-bulk, schepen tot 180.000 t [A3][A5] | idem | → duwbak-bulk | deel van A |
| C | idem | duwstellen: 4-baks 193 m / ±11.000 t, 6-baks 269,5 m / ±16.000 t [C4] | idem | → kokskolenblend (kokerei) + PCI-injectie (hoogoven) | Schwelgern-kade totaal erts+kolen ±23 Mt/j, ±10.000 duwbakken/j [C3][C22] |
| D | hoogovencokes | stukbulk (gezeefd/geclassificeerd), per band of wagon [D1] | uit ±3,8 Mt kolen → ±2,5 Mt cokes [D1] | → reductiemiddel in de hoogoven | ±2,5 Mt/j [D1]; bijproduct koksgas ±155.000 m³/u, teer, benzol, zwavel [D1] |
| E | ruwijzer → ruwstaal | vloeibaar: torpedopfannen (werkspoor), converter-charges ±265 t [D4] | converter: ±20 min bij 1.650–1.720 °C [D3] | brammen (stranggiet) of warmband (gietwals) [D3] — stáálstroom, eigen brief | Schwelgern-ovens ±10.000 + ±12.000 t ruwijzer/dag [D2] ≈ orde 8 Mt/j (afgeleid); OSW Bruckhausen 5,2 Mt [D3], OSW Beeckerwerth 5,9 Mt ruwstaal/j [D4] |

### 2a · De productvraag — van product naar kade

*Ingevuld voor elke laad-, overslag- en losplek. De ladders van fase D/E zijn kort: één eigenaar,
één terrein.*

**Ladder 1 — laadplek mijn (b1-kop).**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm? | gebroken/gewassen steenkool, bulk |
| 2 | Soort faciliteit? | treinbeladingsstation: silo boven een keerlus, beladen op rijdende trein |
| 3 | Partijen op deze plek? | alleen Carbones del Cerrejón Limited (100% Glencore, sinds jan 2022) [A13] |
| 4 | Welke hoort bij déze stroom? | idem — eigen mijnspoor, één operator |
| 5 | Welke laadplek? | keerlus met laadsilo's, 12.800 t buffer, laden 9.500 t/h [A1][A6][A9] |
| 6 | Coördinaat + satelliet | 11.12600, -72.63500 — **satellietpass (z16) nog niet gedaan → §5** |

*Uitsluiting:* de dagbouw-put zelf is geen laadplek (de Escondida-regel); de quarry-centroïde
waar `coal-cerrejon-laad` nu op staat is dus de verkeerde plek → §6.

**Ladder 2 — overslag Puerto Bolívar (b1 → b2).**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm? | steenkool in treinladingen (100–150 wagons à 110 t) |
| 2 | Soort faciliteit? | kiplos-/ontlaadstation met bodemlossing + stockyard + shiploader aan een diepzeepier |
| 3 | Partijen op deze plek? | alleen Cerrejón — eigen haven (enige gebruiker van Bahía Portete-terminal) |
| 4 | Welke hoort bij déze stroom? | idem |
| 5 | Welke kade? | Muelle Carbonífero 1 (schepen tot 180.000 t) + Muelle 2 (2014); vaargeul 19 m × 225 m × 4 km [A1][A3][A4][A5] |
| 6 | Coördinaat + satelliet | 12.26000, -71.96300 (Muelle 1) — **satellietpass nog niet gedaan → §5** |

*Uitsluiting:* capesize-belading sluit kleinschalige kades uit; geen containers, geen stukgoed —
alles wat geen bulk-pier met shiploader is valt af.

**Ladder 3 — overslag EMO Maasvlakte (b2 → b3).**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm? | steenkool, capesize-bulk in; duwbak-bulk uit |
| 2 | Soort faciliteit? | droge-bulk importterminal: brugkranen (lossen), stockyard, duwbak-belader |
| 3 | Partijen die dat op de Maasvlakte/Europoort doen? | **EMO** (Mississippihaven, HES International) en **EECV** (Calandkanaal/Dintelhaven — eigendom thyssenkrupp Steel + HKM) [C15][D6] |
| 4 | Welke hoort bij déze stroom? | de projectdata kiest **EMO** (aansluiting `coal-rotterdam-kade`; ±80% van de EMO-overslag gaat naar het Duitse achterland [C14][C15][C24]); het maatgevende tk-duwverkeer laadt primair bij **EECV** → reëel alternatief (blok hieronder, §5) |
| 5 | Welke kade? | kolenkade noordzijde Mississippihaven; duwbak-belader "kade 2013", ±5.000 t/u [C14][C15] |
| 6 | Coördinaat + satelliet | 51.94109, 4.05354 (anker) — **satellietpass nog niet gedaan; zeekade en binnenvaartkade zijn nog niet als twee ankers gescheiden → §5** |

*Uitsluiting:* container-/LNG-/stukgoedkades uitgesloten; het **Beerkanaal** is de zeevaart-kant
van de Mississippihaven — de duwvaart verlaat de haven oostwaarts (negatief anker been 3).

**Ladder 4 — overslag Werkshafen Schwelgern (b3 → b4).**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm? | cokes-/injectiekool per duwstel (±11.000–16.000 t) |
| 2 | Soort faciliteit? | werkshaven van een geïntegreerd hoogovenbedrijf: losbruggen op een erts-/kolenkade, bandtransport het werk op |
| 3 | Partijen op deze plek? | beheer Eisenbahn und Häfen GmbH (thyssenkrupp-dochter); enige klant is thyssenkrupp Steel [C3][C22][C23] |
| 4 | Welke hoort bij déze stroom? | idem — Kokerei Schwelgern ligt op ±0,8 km, het Erzlager op ±1,2 km, de hoogovens op ±1 km |
| 5 | Welke kade? | loskade Werkshafen Schwelgern, rechteroever Rijn-km 790,20; ±10.000 duwbakken/j, ±23 Mt/j erts+kolen [C3][C22][C23] |
| 6 | Coördinaat + satelliet | loskade (brief) 51.50900, 6.73000 · anker `coal-duisburg-kade` (OSM-pier met moorings) 51.51321, 6.72347 — **discrepantie ±0,5 km, satellietpass beslist → §5/§6** |

*Uitsluiting:* cokeskool voor een hoogoven lost bij het staalbedrijf, niet in een publiek
stukgoedbekken — Ruhrort/Becken A (de kóperkade, 7 km bovenstrooms) is een negatief anker.

**Ladder 5 — losplek Kokerei Schwelgern (b4-staart, kort).** Kolen → kolentoren/batterijen.
Faciliteit: kooksfabriek met 2 batterijen × 70 ovens (grootste ovens ter wereld, 8,32 × 0,59 ×
20,8 m), twee kolenopslagen die per **schip of wagon** gevuld worden [D1]. Partij: thyssenkrupp
Steel Europe (KBS in mei 2020 versmolten) [D1]. Coördinaat: 51.50193, 6.72713 (OSM way/228035059
[D8]; Wikipedia 51.50172, 6.72794 [D1] — consistent). *Uitsluiting:* de vroegere Kokerei August
Thyssen (51.48934, 6.73534) is brownfield [D8] — daar lost niets meer.

**Ladder 6 — losplek hoogovens Schwelgern (b5-staart, kort).** Cokes → hoogovenbunker.
Faciliteit: twee hoogovens naast de sinteranlage; aanvoer per band vanaf de kokerei-classificatie
[D1][D2]. Partij: thyssenkrupp Steel. Coördinaten: Hochofen Schwelgern 1 = 51.50492, 6.73965 ·
Schwelgern 2 = 51.50672, 6.73969 (OSM [D8]). *Uitsluiting:* de "Hochofen"-treffers op
51.480, 6.781 zijn de múseumhoogovens van het Landschaftspark Duisburg-Nord (Meiderich) —
negatief anker.

**Ladder 7 — losplek Oxygenstahlwerk (b6-staart, kort).** Vloeibaar ruwijzer → converter.
Faciliteit: BOF-staalwerk; aanvoer per torpedopfannen over het werkspoor vanaf de Hamborn- en
Schwelgern-ovens [D3][D4]. Partij: thyssenkrupp Steel. Coördinaten: OSW 1 Bruckhausen =
51.49351, 6.74222 · OSW 2 Beeckerwerth = 51.48370, 6.70705 (OSM [D8]). *Uitsluiting:* het
OSM-object "Oxygenstahlwerk (OX)" op 51.46225, 6.74756 hoort bij het Ruhrort/ArcelorMittal-terrein
— verkeerde staalfabriek, negatief anker.

### 2b · De overslagregel, hier toegepast

Een overslag is nooit één punt en elke drager-wissel telt. In deze keten: Puerto Bolívar
(ontlaadstation → stockyard/band → shiploader: 3 punten), EMO (zeekade → stockyard → duwbak-belader:
**nog maar 1 anker** — openstaand punt §5, geen coördinaat verzonnen) en Schwelgern (loskade →
band; het band-vertrekpunt/kolenlager is niet benoemd in OSM → §5). Op het tk-terrein wisselt de
drager nog twee keer (band → hoogovenbunker; abstich → torpedowagen) — genoteerd als terreinstappen
in b5/b6. **Anker ≠ routeerpunt:** gemeten snap-afstanden per been-uiteinde staan in de
been-koppen (bron: `aansluitingen.json`, netstadium 2026-07-23/28).

## 3 · Kernfeiten die de vorm van de keten bepalen

1. **De natte corridor is operator-gedocumenteerd en volledig sluisvrij** — thyssenkrupp Veerhaven:
   Hartelkanaal → Oude Maas → Beneden-Merwede → Waal → Rijn, 240 km, 26 uur geladen bergwaarts;
   enige beweegbare kunstwerk is de Hartelkering (normaal open) [C4][C12]. Dat pint het hele been 3.
2. **De Ferrocarril del Cerrejón is de enige normaalspoor-goederenlijn van Colombia** (1.435 mm,
   150 km, enkelsporig, mijn → eigen diepzeehaven) [A2][A3][A4][A7] — fase A ligt volledig op
   privé-infrastructuur van de mijn; er is geen alternatieve route.
3. **Fase D speelt op één terrein:** de Kokerei Schwelgern ligt ±0,8 km achter de loskade, verwerkt
   ±3,8 Mt kolen tot ±2,5 Mt cokes per jaar, en de hoofdafnemer is het naastgelegen
   hoogovenwerk [D1][D5]. Geen openbaar net — band en werkspoor → stippellijnen mét reden.
4. **Fase E is werkspoor:** ruwijzer van de ovens Schwelgern 1/2 (±10.000 + ±12.000 t/dag [D2])
   gaat per torpedopfannen naar de Oxygenstahlwerke Bruckhausen (5,2 Mt/j, 2 converters [D3]) en
   Beeckerwerth (5,9 Mt/j, charges ±265 t [D4]).
5. **⚠️ De gedocumenteerde Cerrejón→Duitsland-stroom is overwegend krachtwerkkool** — kopers RWE,
   STEAG (tot 20% van zijn behoefte), EnBW, E.ON; Colombia leverde ±31% van de Duitse
   steenkoolimport en verving na 2022 Russische kolen [E1][E2][E3]. Een bron die specifiek
   Cerrejón-kool in de Schwelgern-kokskolenblend legt is **niet gevonden** (§5) — de brief volgt
   de corridor van de projectstroom (`data/coal.js` + `aansluitingen.json`: losplek Schwelgern).
6. **De D/E-staart is in transitie:** Hochofen 9 (Hamborn, 1962) is in oktober 2025 stilgelegd;
   capaciteit gaat van 11,5 naar 8,7–9,0 Mt ruwijzer; een DRI-anlage (2,3 Mt, gepland eind 2027)
   vervangt Hamborn 8/9 richting 2030 [E4][E5]. Deze brief beschrijft de stand van 2026-07.

---

# FASE A · Mina Cerrejón → Puerto Bolívar

## Been 1 · spoor — laadstation mijn → ontlaadstation Puerto Bolívar

**been-id:** `kolen-cerrejon-ruhr-b1`
**Modaliteit:** spoor (eigen lijn) — Ferrocarril del Cerrejón (OSM: "Vía Ferroviaria Albania –
Puerto Bolívar"). Officieel **150 km** [A2][A3][A5][A6][A7]; langs de OSM-geometrie 153,8 km incl.
emplacementen (IRJ: 145 km excl. [A14]). **Normaalspoor 1.435 mm** — de enige
normaalspoor-goederenlijn van Colombia [A3][A4][A7] — niet geëlektrificeerd, alleen vracht,
**enkelsporig** met een passeerspoor van 3,1 km op km 110–113 [A1]. Aangelegd 1983–84 (27 bruggen,
samen 2.300 m) [A7]; sinds jan 2022 100% Glencore (Carbones del Cerrejón Limited) [A13].
±7 treinen/dag, 100–150 wagons à 110 t [A9][A10].
**Lengte:** gepubliceerd 150 km · OSM-geometrie 153,8 km (+2,5%, incl. emplacementen)
**Net / bron geometrie:** OSM-spoorlijn way/31148047 (mijn en pier aantoonbaar op dezelfde
component van 158 km — `aansluitingen.json`-meting)
**Stippel:** nee (echte OSM-geometrie)
**Corridor bij naam:** Vía Ferroviaria Albania – Puerto Bolívar
**Routeerpunt kop / staart:** kop **nog te bepalen** (de gemeten spoor-snap 5,95 km bij
11.1741, -72.5562 hoort bij de quarry-centroïde, niet bij de laadlus — §6) · staart
12.2387, -71.9831 — max snap ±0,7 km (gemeten 0,67 km, `coal-bolivar-kade`)
**Toets-marge:** default (2 km passages · 100 m kop/staart); Wayuu-rancherías zijn OSM-only
(spelling wisselt per bron) — passagemarge daar 2 km aanhouden
**anker-ids:** kop `coal-cerrejon-laad` (⚠️ ligt nu ±8 km oost van de laadlus — §6) · staart
`coal-bolivar-kade`

km = afstand langs het spoor vanaf de laadlus (OSM-chainage; gevalideerd tegen journalistieke
km-aanduidingen, zie opmerkingen).

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0,0 | **Laadstation mijn** — keerlus met laadsilo's (12.800 t; laden 9.500 t/h op rijdende trein) | laadplek | 11.12600, -72.63500 | [A1][A6][A9] | bevestigd |
| 2 | 0–3 | Emplacement **La Mina** (yard-waaier) | emplacement | 11.135, -72.622 | [A1] | aannemelijk |
| 3 | 3,8 | **Mushaisa** (Cerrejón-woonkamp), W van het spoor | passage | 11.152, -72.608 | [A1] | aannemelijk |
| 4 | 4,8 | **Albania** — lijn schampt de NW-rand, dorp direct ZO | passage | 11.158, -72.599 | [A1][A3] | bevestigd |
| 5 | 6,0 | Viaduct (55 m) over de weg Cuestecitas–Albania (ruta 88) | kruising | 11.165, -72.591 | [A1] | aannemelijk |
| 6 | — | **Cuestecitas** ligt 3,2 km W van de lijn — route loopt er NIET doorheen | referentie (niet aan lijn) | 11.181, -72.618 | [A1] | bevestigd |
| 7 | 9,5 | **Brug Río Ranchería** (229–270 m) | rivierkruising | 11.174, -72.560 | [A1][A7] | bevestigd |
| 8 | 14,5 | Ranchería **La Hoguera** (300 m W) | passage | 11.167, -72.516 | [A1] | aannemelijk |
| 9 | 19,1 | Kruising weg Albania–Uribia + 2 arroyo-bruggen (106/105 m) | kruising | 11.197, -72.506 | [A1] | aannemelijk |
| 10 | 21,6 | **Brug 236 m** over tweede rivierarm (naam onbevestigd) | rivierkruising | 11.219, -72.509 | [A1] | aannemelijk |
| 11 | 23,6 | Overweg bij rancherías Los Playones / Garcibón | kruising | 11.235, -72.503 | [A1] | aannemelijk |
| 12 | 40,3 | Rancherías Curarir & Masamana (~2 km W) | passage | 11.376, -72.448 | [A1] | aannemelijk |
| 13 | 46,1 | **Viaduct over Ruta 90 Riohacha–Maicao**; knooppunt Cuatro Vías ±3 km WZW | kruising | 11.414, -72.406 | [A1][A7][A19][A20] | bevestigd |
| 14 | 46–48 | Nueva Cuasin (O) en Yamahain (W) | passage | 11.412, -72.401 | [A1] | aannemelijk |
| 15 | 58–61 | Rancherías Guaitequi / Aguafachon / Sarahu (W), Cousharain / Marirau (O) | passage | 11.534, -72.350 | [A1] | aannemelijk |
| 16 | 63,8 | Overweg (omgeving "km 61" — aanslag jan 2026) | kruising | 11.560, -72.342 | [A1][A12] | aannemelijk |
| 17 | 66,5 | Rancherías Rivira / Garcia / Jotomana (1,2–1,5 km W) | passage | 11.587, -72.343 | [A1] | aannemelijk |
| 18 | 73,2 | **San Miguel** (1,1 km W) | passage | 11.642, -72.316 | [A1] | aannemelijk |
| 19 | 76,4 | Comunidad Parajain–Parlain (210 m W) | passage | 11.665, -72.297 | [A1] | aannemelijk |
| 20 | 79,8–80,2 | Overwegen ZW-toegang Uribia — het "km 80, sector Cuatro Vías–Uribia" uit blokkade-berichten | kruising | 11.694, -72.283 | [A1][A11] | bevestigd |
| 21 | 82,7 | Overweg Calle 12 / Avenida Fundador (hoofdtoegang Uribia) | kruising | 11.716, -72.273 | [A1] | aannemelijk |
| 22 | 82,9 | **Uribia** — lijn passeert de NW-rand; centrum 800 m ZO | passage | 11.716, -72.271 | [A1][A2][A11] | bevestigd |
| 23 | 83,0–83,6 | 2 bruggen (80/151 m) over de arroyo's van Uribia (Kutanamana/Chemerrain) | rivierkruising | 11.719, -72.271 | [A1][A15][A16] | bruggen bevestigd, namen onzeker |
| 24 | 90,0 | Janurerao (420 m O) | passage | 11.775, -72.243 | [A1] | aannemelijk |
| 25 | 100–106 | Jaraurain (W), Kusinalima (W); bruggen 74 m en 144 m | passage | 11.905, -72.188 | [A1] | aannemelijk |
| 26 | 110,2–113,3 | **Passeerspoor** (3,1 km, wissels aan beide einden) | passeerspoor | 11.951, -72.160 | [A1] | aannemelijk |
| 27 | 121,4 | Arroyo-brug 88 m | rivierkruising | 12.030, -72.119 | [A1] | aannemelijk |
| 28 | 131,1 | Gelijkvloerse kruising "Vía Uribia – Puerto Bolívar" | kruising | 12.106, -72.074 | [A1] | aannemelijk |
| 29 | 137,1 | Arroyo-brug 66 m | rivierkruising | 12.155, -72.052 | [A1] | aannemelijk |
| 30 | 139,8 | Overweg weg naar Punta Gallinas | kruising | 12.178, -72.044 | [A1] | aannemelijk |
| 31 | 141,1–141,5 | 2 kleine arroyo-bruggen (28/25 m) | rivierkruising | 12.190, -72.039 | [A1] | aannemelijk |
| 32 | 146,5 | Overweg "Vía Cabo de la Vela" (jeeproute kruist het spoor) | kruising | 12.222, -72.004 | [A1] | aannemelijk |
| 33 | 147,0 | **Media Luna** (Wayuu-gemeenschap, 950 m W; invloedszone haven per uitspraak T-704/16) | passage | 12.231, -72.006 | [A1][A17][A18] | bevestigd |
| 34 | 149,2 | Piyohureka (440 m Z); airstrip Puerto Bolívar Z van de lijn | passage | 12.234, -71.983 | [A1] | aannemelijk |

*De punten 35–37 van de oorspronkelijke brief (ontlaadstation, transportbanden, muelles) staan
hieronder in het overslag-blok — geen punt is vervallen.*

**Opmerkingen been 1**

- **Chainage gevalideerd:** "km 80, sector Cuatro Vías–Uribia" (blokkades [A11]) = OSM km
  79,8–80,2; de aanslag bij "km 61" (jan 2026 [A12]) valt tussen punt 15 en 16.
- **⚠️ Voor het spoornet:** op het terminalterrein zit in OSM een niet-doorverbonden stuk van
  ~1 km tussen einde hoofdspoor (12.239, -71.983) en het pier-toeloopspoor; de echte verbinding
  loopt via de terminal-lus. Zelfde klasse als het last-mile-heal-werk.
- Naast de tabel: ±25 naamloze veld-/gemeenschapsoverwegen (OSM), niet apart gelijst.
- Wayuu-plaatsnamen zijn OSM-only; spelling kan per bron verschillen. Treinsamenstelling
  verschilt per bron (109/120/150 wagons).

**Negatieve ankers been 1** — mét coördinaat + verbodsstraal:

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Cuestecitas | 11.181, -72.618 | 2 km | ligt 3,2 km W van de lijn; wegbeschrijvingen noemen het dorp als knooppunt, het spoor komt er niet [A1] |
| Riohacha | 11.544, -72.907 | 10 km | het spoor raakt Riohacha nergens; OSM-signal-ruis bij Riohacha is bekend en fout [A1] |
| Maicao | 11.378, -72.239 | 5 km | het spoor raakt Maicao nergens (Ruta 90-kruising ligt 20+ km westelijker, punt 13) [A1] |

## Overslag been 1 → been 2 — Puerto Bolívar

**Productvraag:** ladder 2 in §2a — kiplosstation + stockyard + shiploader aan de eigen
diepzeepier; enige partij is Cerrejón zelf.
**anker-id:** `coal-bolivar-kade` (12.23912, -71.97693 — centroïde van de OSM-terminal-way
"Terminal de Carbones del Cerrejón"; ligt tussen aankomst- en vertrekanker in, consistent).

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 1 *(was punt 35)* | **Terminal Puerto Bolívar** — ontlaadstation (4 stortbunkers, bodemlossing 5 s/wagon), emplacement + lus, stockyard | losplek | 12.24000, -71.96800 | [A1][A9][A10] | bevestigd — **satellietpass open (§5)** |
| 2 | terrein *(was punt 36)* | Overdekte transportbanden (6.400 t/h) stockyard → pier | verwerkingsstap | 12.24900, -71.96400 | [A1][A5][A9] | bevestigd |
| 3 | vertrek been 2 *(was punt 37)* | **Muelle Carbonífero 1** (shiploader, schepen tot 180.000 t) + **Muelle 2** (2014; 12.25700, -71.96100), monding Bahía Portete; vaargeul 19 m × 225 m × 4 km | laadplek | 12.26000, -71.96300 | [A1][A3][A4][A5] | bevestigd — **satellietpass open (§5)** |

**Routeerpunt ≠ anker.** Spoor-routeerpunt 12.2387, -71.9831 (snap 0,67 km);
zee-routeerpunt 12.447, -72.2363 (snap **36,44 km** — MARNET-korrel bij Colombia; de
haven-aanloop wordt vermoedelijk een stippellijn mét reden, zie §7 en werkwijze §7: Colombia
heeft geen havens met varend AIS-verkeer in de wereldscan).

---

# FASE B · zee

## Been 2 · zee — Puerto Bolívar → Rotterdam EMO

**been-id:** `kolen-cerrejon-ruhr-b2`
**Modaliteit:** zeeschip (capesize, tot 180.000 t) · **Router:** zee = vrij geroutet
(werkwijze §6) — alleen eindpunten vastgelegd, geen brief-ankers op open zee
**Lengte:** huidige atlas 8.231 km (`?v=071`-meting, netstadium 24 juli — bij hermeten
gereedschap + eindpunten + netstadium noemen)
**Overslagen onderweg:** geen (rechtstreeks; bulk kent hier geen transshipment-hub — de
direct-vs-hub-vraag speelt bij containers, niet bij deze capesize-stroom)
**Routeerpunt kop / staart:** 12.447, -72.2363 (snap 36,44 km — MARNET-korrel, zie
overslag-blok) · 51.9876, 4.0697 (snap 5,29 km, gemeten `coal-rotterdam-kade`)

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | **Muelle Carbonífero 1/2, Bahía Portete** | laadplek | 12.26000, -71.96300 | [A1][A3][A5] | bevestigd — satellietpass open (§5) |
| 2 | Nauw van Calais / Straat van Dover (sanity-anker) | passage | 51.03, 1.55 | geografie Kanaal-aanloop Rotterdam; router | aannemelijk |
| 3 | **EMO-terminal, kolenkade noordzijde Mississippihaven, Maasvlakte** | overslag | 51.94109, 4.05354 | [C14][C15] + `aansluitingen.json` | bevestigd — satellietpass open (§5) |

**Negatieve ankers been 2:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Panamakanaal (Atlantische ingang, Cristóbal) | 9.35, -79.92 | 100 km | de route is trans-Atlantisch; via Panama is een omweg van vele duizenden km — een router die hier komt zit fout |

---

# FASE C · aanlanding → verwerker (Kokerei Schwelgern)

## Overslag been 2 → been 3 — EMO, Maasvlakte

**Productvraag:** ladder 3 in §2a — droge-bulk importterminal; op de Maasvlakte doen EMO en EECV
dit werk; de projectdata kiest EMO.
**anker-id:** `coal-rotterdam-kade` (51.94109, 4.05354).

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 2 | EMO-zeekade (brugkranen, lossen capesize) — **exacte losligplaats nog niet als eigen anker gelegd** | losplek | 51.94109, 4.05354 *(zelfde anker als rij 3 — §5)* | [C14][C15] | aannemelijk |
| 2 | terrein | EMO-stockyard (opslag; ±80% van de overslag naar het Duitse achterland) | opslag/stockpile | 51.94109, 4.05354 *(terminal-centroïde)* | [C14][C15][C24] | bevestigd |
| 3 | vertrek been 3 | EMO binnenvaart-/kolenkade noordzijde Mississippihaven (kade 2013, belader ±5.000 t/u) — brief-punt (2026-07-24): 51.940, 4.055 | laadplek | 51.94109, 4.05354 | [C14][C15][C24] | bevestigd — **satellietpass open (§5)** |

**⚠️ Overslag = twee ankers, en die zijn hier nog niet gescheiden.** De oude brief had één
EMO-punt; zeeschip-losligplaats en duwbak-belaadkade zijn fysiek verschillende kades aan
hetzelfde bekken. Er is **geen** coördinaat verzonnen: één anker dekt nu beide rollen →
openstaand punt §5 (z16-pass moet de twee kades scheiden).

**Routeerpunt ≠ anker.** Zee 51.9876, 4.0697 (snap 5,29 km) · binnenvaart 51.9452, 4.0394
(snap 1,07 km) — gemeten in `aansluitingen.json`.

**Reëel alternatief (laadzijde):**

| punt | type | lat, lon | bron | status |
|---|---|---|---|---|
| **EECV-terminal** (zeekade 1.100 m aan het Calandkanaal — 1 kolenschip + 2 ertsschepen, diepgang tot 23 m; binnenvaartkade 900 m met 3 beladers in de **Dintelhaven**; ±20 Mt erts + ±7 Mt kolen/j; eigendom thyssenkrupp Steel + HKM; belading duwbakken door zusterbedrijf thyssenkrupp Veerhaven) | alternatief (aandeel onbekend — vermoedelijk het merendeel van het tk-duwverkeer; §5) | 51.941, 4.122 *(monding Dintelhaven = punt 4 been 3; exacte kades §5)* | [C16][D6][D7] | bevestigd (faciliteit) · onzeker (ligplaats) |

Vanaf de Dintelhaven-monding (punt 4 van been 3) zijn de EMO- en EECV-route identiek — voor deze
stroom is EMO het gekozen laadpunt (aansluiting `knooppunten`/`aansluitingen.json`).

## Been 3 · binnenvaart (Rijn) — EMO Maasvlakte → Werkshafen Schwelgern

**been-id:** `kolen-cerrejon-ruhr-b3`
**Modaliteit:** duwvaart (thyssenkrupp Veerhaven: 4-baks duwstel 193 m / ±11.000 t, 6-baks
269,5 m / ±16.000 t, ±22 Mt/jaar [C4]) · **Brief-gestuurd** (werkwijze §6: geen vrije Dijkstra)
**Lengte:** operator 240 km enkele reis (26 uur geladen bergwaarts) [C4] · gerouteerd 254 km
(`?v=071`, netstadium 24 juli; verschil zit vermoedelijk deels in de Beerkanaal-lus en de
eindpunt-keuze — na de correctie opnieuw meten, mét gereedschap/eindpunten/netstadium)
**km-kolom =** officiële **Rijn-km** (loopt afwaarts op; alleen ingevuld op het Duitse deel en
bij de grens, waar de raai bekend is — de NL-vaarwegen dragen elk een eigen kilometrering)
**Stippel:** nee (Rijn/vaarwegen = echt net)
**Corridor bij naam** (officiële namen, in volgorde): Mississippihaven → **Hartelkanaal**
(overgang bij de Suurhoffbrug; CEMT VIc, 21 km) → **Oude Maas** (monding tussen Spijkenisserbrug
en Botlekbrug, stroomopwaarts) → **Beneden-Merwede** (drierivierenpunt Groothoofd, Dordrecht — de
Noord wordt NIET genomen) → **Boven-Merwede** (splitsing Werkendam — de Nieuwe Merwede wordt NIET
genomen) → **Waal** (vanaf de monding van de Afgedamde Maas bij Woudrichem/Loevestein; sluisvrij,
65% van de Rijnafvoer) → **Boven-Rijn** (Pannerdensche Kop — het Pannerdensch Kanaal wordt NIET
genomen) → **Rijn/Niederrhein** (grens bij Spijk, ±km 857,4) → **Werkshafen Schwelgern**
(rechteroever, **Rijn-km 790,20**, Duisburg-Hamborn/Marxloh)
**Routeerpunt kop / staart:** 51.9452, 4.0394 (snap 1,07 km) · 51.5059, 6.7248 (snap 0,82 km) —
gemeten in `aansluitingen.json`
**Toets-marge:** default (2 km passages · 100 m kop/staart); afwijkend: plaats-coördinaten zijn
OSM-kernen en sommige kernen liggen 1–2 km van de geul (Barendrecht, Beuningen, Xanten, Lobith,
Rheinberg, Voerde) → daar 3 km aanhouden
**anker-ids:** kop `coal-rotterdam-kade` · staart `coal-duisburg-kade`

**Bron van de corridor is de operator zelf** — thyssenkrupp Veerhaven: *"De vaarroute vanuit
Europoort gaat via het Hartelkanaal, Oude Maas, Beneden Merwede, Waal en bij de Duitse grens de
Rijn op naar Duisburg"* [C4]. Schwelgern ontvangt ±10.000 duwbakken per jaar [C3]. **De route is
volledig sluisvrij**; enige beweegbare kunstwerk is de Hartelkering (stormvloedkering, staat
normaal open) [C12]. Afgewezen alternatieven mét reden: Nederrijn–Lek is gestuwd
(Driel/Amerongen/Hagestein — geen zware duwvaart) [C13]; Dordtsche Kil → Hollandsch Diep is de
corridor naar Moerdijk/Antwerpen, niet naar de Rijn [C5].

| # | km (Rijn) | punt | type | vaarweg | lat, lon | bron | status |
|---|---|---|---|---|---|---|---|
| 1 | — | **EMO-terminal**, binnenvaart-/kolenkade noordzijde Mississippihaven (kade 2013, belader ±5.000 t/u; ±80% van de overslag naar het Duitse achterland) | laadplek | Mississippihaven | 51.94109, 4.05354 | [C14][C15][C24] | bevestigd — satellietpass open (§5) |
| 2 | — | Mississippihaven oostwaarts uitvaren (open verbinding met het Hartelkanaal sinds doorsteek Beerdam, eind 1997) | vaarweg | Mississippihaven | 51.937, 4.060 | [C1][C2][C24] | bevestigd |
| 3 | — | **Suurhoffbrug** (A15/N15) = overgang naar het Hartelkanaal | vaarweg-overgang | → Hartelkanaal | 51.938, 4.107 | [C1][C24] | bevestigd |
| 4 | — | Monding **Dintelhaven** (EECV erts-/kolenterminal — laadpunt van de Veerhaven-duwstellen; zie het alternatief-blok) | knooppunt | Hartelkanaal | 51.941, 4.122 | [C1][C16][C24] | bevestigd |
| 5 | — | Harmsenbrug (N57) | passage | Hartelkanaal | 51.902, 4.212 | [C1][C24] | bevestigd |
| 6 | — | Heenvliet (Z-oever) | passage | Hartelkanaal | 51.864, 4.245 | [C24] | aannemelijk |
| 7 | — | Geervliet (Z-oever) | passage | Hartelkanaal | 51.860, 4.259 | [C24] | aannemelijk |
| 8 | — | Hartelbrug (N218) | passage | Hartelkanaal | 51.864, 4.308 | [C1][C24] | bevestigd |
| 9 | — | **Hartelkering** (normaal open) + locatie vml. Hartelsluizen | sluis/kering (open) | Hartelkanaal | 51.866, 4.308 | [C12][C24] | bevestigd |
| 10 | — | Spijkenisse | passage | Hartelkanaal/Oude Maas | 51.846, 4.331 | [C5][C24] | bevestigd |
| 11 | — | **Monding Hartelkanaal in de Oude Maas** (tussen Spijkenisserbrug en Botlekbrug); stroomopwaarts = ZO | vaarweg-overgang | → Oude Maas | 51.867, 4.334 | [C1][C5][C24] | bevestigd |
| 12 | — | Spijkenisserbrug | passage | Oude Maas | 51.860, 4.340 | [C5][C24] | bevestigd |
| 13 | — | Hoogvliet (N-oever) | passage | Oude Maas | 51.865, 4.364 | [C5][C24] | bevestigd |
| 14 | — | Poortugaal (N-oever) | passage | Oude Maas | 51.858, 4.391 | [C5][C24] | bevestigd |
| 15 | — | Rhoon (N-oever) | passage | Oude Maas | 51.857, 4.424 | [C5][C24] | bevestigd |
| 16 | — | Afsplitsing **Spui** (Z — NIET nemen) | knooppunt | Oude Maas | 51.837, 4.433 | [C5][C24] | bevestigd |
| 17 | — | Oud-Beijerland (Z-oever) | passage | Oude Maas | 51.821, 4.417 | [C5][C24] | bevestigd |
| 18 | — | Heinenoord (Z-oever) | passage | Oude Maas | 51.827, 4.480 | [C5][C24] | bevestigd |
| 19 | — | Heinenoordtunnel (A29) | passage | Oude Maas | 51.834, 4.513 | [C5][C24] | bevestigd |
| 20 | — | Barendrecht (N-oever, kern ±2 km) | passage | Oude Maas | 51.857, 4.537 | [C5][C24] | bevestigd |
| 21 | — | Heerjansdam (N-oever) | passage | Oude Maas | 51.835, 4.562 | [C5][C24] | bevestigd |
| 22 | — | Puttershoek (Z-oever) | passage | Oude Maas | 51.805, 4.568 | [C5][C24] | bevestigd |
| 23 | — | Afsplitsing **Dordtsche Kil** (Z, richting Moerdijk/Antwerpen — NIET nemen) | knooppunt | Oude Maas | 51.801, 4.621 | [C5][C24] | bevestigd |
| 24 | — | Zwijndrecht (N-oever) | passage | Oude Maas | 51.816, 4.641 | [C5][C24] | bevestigd |
| 25 | — | Dordrecht (Z-oever; spoorbrug + Drechttunnel) | passage | Oude Maas | 51.814, 4.669 | [C5][C24] | bevestigd |
| 26 | — | **Drierivierenpunt Groothoofd** — de Noord mondt links uit (NIET nemen) | vaarweg-overgang | → Beneden-Merwede | 51.820, 4.670 | [C5][C6][C24] | bevestigd |
| 27 | — | Papendrecht (N-oever) | passage | Beneden-Merwede | 51.835, 4.694 | [C6][C24] | bevestigd |
| 28 | — | Sliedrecht (N-oever) | passage | Beneden-Merwede | 51.831, 4.770 | [C6][C24] | bevestigd |
| 29 | — | Hardinxveld-Giessendam (N-oever) | passage | Beneden-Merwede | 51.839, 4.825 | [C6][C24] | bevestigd |
| 30 | — | Boven-Hardinxveld (N-oever) | passage | Beneden-Merwede | 51.832, 4.879 | [C6][C24] | bevestigd |
| 31 | — | **Splitsing Werkendam** — de Nieuwe Merwede takt ZW af (NIET nemen) | vaarweg-overgang | → Boven-Merwede | 51.821, 4.894 | [C6][C7][C24] | bevestigd |
| 32 | — | Werkendam (Z-oever) | passage | Boven-Merwede | 51.808, 4.899 | [C7][C24] | bevestigd |
| 33 | — | Merwedebrug (A27) | passage | Boven-Merwede | 51.830, 4.944 | [C7][C24] | bevestigd |
| 34 | — | Gorinchem (N-oever; mondingen Linge + Merwedekanaal) | passage | Boven-Merwede | 51.830, 4.974 | [C7][C8][C24] | bevestigd |
| 35 | — | Woudrichem (Z-oever) | passage | Boven-Merwede | 51.817, 5.003 | [C7][C24] | bevestigd |
| 36 | — | **Monding Afgedamde Maas** bij Slot Loevestein | vaarweg-overgang | → Waal | 51.821, 5.002 | [C7][C8][C11][C24] | bevestigd |
| 37 | — | Vuren (N-oever) | passage | Waal | 51.825, 5.048 | [C24] | aannemelijk |
| 38 | — | Brakel (Z-oever) | passage | Waal | 51.817, 5.091 | [C24] | aannemelijk |
| 39 | — | Herwijnen (N-oever) | passage | Waal | 51.827, 5.130 | [C24] | aannemelijk |
| 40 | — | Haaften (N-oever) | passage | Waal | 51.818, 5.213 | [C24] | aannemelijk |
| 41 | — | Zaltbommel (Z-oever) | passage | Waal | 51.811, 5.245 | [C8][C11][C24] | bevestigd |
| 42 | — | Martinus Nijhoffbrug (A2) + spoorbrug | passage | Waal | 51.821, 5.260 | [C8][C24] | bevestigd |
| 43 | — | Waardenburg (N-oever) | passage | Waal | 51.831, 5.258 | [C24] | aannemelijk |
| 44 | — | Varik (N-oever) | passage | Waal | 51.824, 5.368 | [C24] | aannemelijk |
| 45 | — | Heerewaarden (Z-oever) + afsplitsing **Kanaal van Sint Andries** (NIET nemen) | knooppunt | Waal | 51.818, 5.389 | [C24] | aannemelijk |
| 46 | — | Ophemert (N-oever) | passage | Waal | 51.845, 5.387 | [C24] | aannemelijk |
| 47 | — | Dreumel (Z-oever) | passage | Waal | 51.848, 5.430 | [C24] | aannemelijk |
| 48 | — | Tiel (N-oever) | passage | Waal | 51.887, 5.437 | [C8][C11][C24] | bevestigd |
| 49 | — | Monding **Amsterdam-Rijnkanaal** (Prins Bernhardsluizen, N — NIET nemen) | knooppunt | Waal | 51.901, 5.454 | [C8][C24] | bevestigd |
| 50 | — | Wamel (Z-oever) | passage | Waal | 51.881, 5.467 | [C24] | aannemelijk |
| 51 | — | Prins Willem-Alexanderbrug (N323) bij Echteld | passage | Waal | 51.899, 5.496 | [C24] | aannemelijk |
| 52 | — | Beneden-Leeuwen (Z-oever) | passage | Waal | 51.881, 5.510 | [C24] | aannemelijk |
| 53 | — | Ochten (N-oever) | passage | Waal | 51.908, 5.567 | [C24] | aannemelijk |
| 54 | — | Druten (Z-oever) | passage | Waal | 51.889, 5.605 | [C24] | aannemelijk |
| 55 | — | Dodewaard (N-oever) | passage | Waal | 51.914, 5.657 | [C24] | aannemelijk |
| 56 | — | Deest (Z-oever) | passage | Waal | 51.890, 5.666 | [C24] | aannemelijk |
| 57 | — | Winssen (Z-oever) | passage | Waal | 51.882, 5.707 | [C24] | aannemelijk |
| 58 | — | Tacitusbrug (A50) bij Ewijk | passage | Waal | 51.886, 5.738 | [C8][C24] | bevestigd |
| 59 | — | Beuningen (Z-oever) | passage | Waal | 51.859, 5.767 | [C24] | aannemelijk |
| 60 | — | Weurt (Z-oever) | passage | Waal | 51.858, 5.815 | [C24] | aannemelijk |
| 61 | — | Monding **Maas-Waalkanaal** (Sluis Weurt, Z — NIET nemen) | knooppunt | Waal | 51.855, 5.823 | [C8][C24] | bevestigd |
| 62 | — | Oosterhout (N-oever) | passage | Waal | 51.880, 5.827 | [C24] | aannemelijk |
| 63 | — | **Nijmegen** (Z-oever; De Oversteek, spoorbrug, Waalbrug) | passage | Waal | 51.852, 5.871 | [C8][C11][C24] | bevestigd |
| 64 | — | Lent (N-oever) | passage | Waal | 51.866, 5.865 | [C24] | aannemelijk |
| 65 | — | Erlecom (Z-oever, Ooijpolder) | passage | Waal | 51.845, 5.959 | [C24] | aannemelijk |
| 66 | — | Gendt (N-oever) | passage | Waal | 51.880, 5.971 | [C24] | aannemelijk |
| 67 | — | Kekerdom (Z-oever) | passage | Waal | 51.865, 6.009 | [C24] | aannemelijk |
| 68 | — | Doornenburg (N-oever) | passage | Waal | 51.890, 6.002 | [C24] | aannemelijk |
| 69 | — | Millingen aan de Rijn (Z-oever) | passage | Waal | 51.864, 6.046 | [C24] | aannemelijk |
| 70 | ±867,5 | **Pannerdensche Kop** — Pannerdensch Kanaal links (Nederrijn/IJssel, NIET nemen); Pannerden zelf ligt aan het Kanaal en wordt NIET gepasseerd | vaarweg-overgang | → Boven-Rijn | 51.874, 6.038 | [C9][C10][C24] | bevestigd |
| 71 | — | Tolkamer (linkeroever) | passage | Boven-Rijn | 51.853, 6.103 | [C9][C24] | bevestigd |
| 72 | — | Lobith (linkeroever, ±1,5 km landinwaarts) | passage (referentie) | Boven-Rijn | 51.862, 6.118 | [C24][C25][C26] | bevestigd |
| 73 | ±857,4 | **Spijk + Duitse grens** (scheepvaartgrens Spijkse Veer) | vaarweg-overgang (grens) | → Rijn (Niederrhein) | 51.849, 6.153 | [C9][C10][C25][C26] | bevestigd (km: aannemelijk) |
| 74 | — | Griethausen (linkeroever, oude Rijnarm) | passage (referentie) | Rijn | 51.823, 6.166 | [C24] | aannemelijk |
| 75 | 853,2 | Rheinbrücke Emmerich (B220) | passage | Rijn | 51.828, 6.226 | [C18][C24] | bevestigd |
| 76 | ±852 | **Emmerich am Rhein** (rechteroever) | passage | Rijn | 51.833, 6.244 | [C18][C24] | bevestigd |
| 77 | — | Grieth (linkeroever; Kalkar ±3 km landinwaarts) | passage | Rijn | 51.787, 6.314 | [C24] | aannemelijk |
| 78 | — | Niedermörmter (linkeroever) | passage | Rijn | 51.745, 6.379 | [C24] | aannemelijk |
| 79 | — | Rees (rechteroever) | passage | Rijn | 51.758, 6.396 | [C24] | aannemelijk |
| 80 | — | Xanten (linkeroever, ±2 km landinwaarts; oeverdorp Wardt) | passage (referentie) | Rijn | 51.689, 6.437 | [C24] | aannemelijk |
| 81 | — | Bislich (rechteroever) | passage | Rijn | 51.679, 6.493 | [C24] | aannemelijk |
| 82 | — | **Wesel** (rechteroever) | passage | Rijn | 51.658, 6.617 | [C19][C24] | bevestigd |
| 83 | — | Lippemonding (rechteroever) | knooppunt | Rijn | 51.653, 6.600 | [C20][C24] | bevestigd |
| 84 | 814 | Niederrheinbrücke Wesel (B58) | passage | Rijn | 51.645, 6.602 | [C19][C24] | bevestigd |
| 85 | 813 | Monding **Wesel-Datteln-Kanal** + Schleuse Friedrichsfeld (NIET nemen) | knooppunt | Rijn | 51.644, 6.605 | [C20][C24] | bevestigd |
| 86 | — | Büderich (linkeroever) | passage | Rijn | 51.629, 6.579 | [C24] | aannemelijk |
| 87 | — | Götterswickerhamm (rechteroever, Voerde) | passage | Rijn | 51.581, 6.661 | [C24] | aannemelijk |
| 88 | — | Mehrum (rechteroever, Voerde) | passage | Rijn | 51.576, 6.625 | [C24] | aannemelijk |
| 89 | — | Ossenberg (linkeroever; Rheinberg ±2 km landinwaarts) | passage | Rijn | 51.571, 6.584 | [C24] | aannemelijk |
| 90 | 793,8–794,5 | Orsoy (linkeroever) + NIAG-kolenhaven | passage + referentie | Rijn | 51.524, 6.687 | [C21][C24] | bevestigd |
| 91 | — | Duisburg-Walsum (rechteroever) | passage | Rijn | 51.535, 6.717 | [C24] | aannemelijk |
| 92 | 790,20 | **Ingang Werkshafen Schwelgern** (rechteroever) | vaarweg-overgang | → Werkshafen Schwelgern | 51.512, 6.723 | [C3][C24] | bevestigd |
| 93 | — | **Loskade Werkshafen Schwelgern** — erts + cokeskool voor Kokerei Schwelgern en de hoogovens; beheer Eisenbahn und Häfen (thyssenkrupp); ±10.000 duwbakken/jr, 23 Mt/jr | losplek | Werkshafen Schwelgern | 51.50900, 6.73000 | [C3][C22][C23][C24] | bevestigd — **satellietpass open; ⚠️ anker `coal-duisburg-kade` ligt op 51.51321, 6.72347 (§5/§6)** |

**Opmerkingen been 3**

- **Rijn-km Schwelgern = 790,20, niet ~796** (eerdere aanname gecorrigeerd; consistent: NIAG
  Orsoy op km 793,8–794,5 benedenstrooms). De Haus-Knipp-spoorbrug (51.479, 6.681) ligt
  bóvenstrooms van de haveningang en wordt dus NIET gepasseerd [C27].
- **Verkeerd-tekenen-vallen:** de Botlekbrug/Botlektunnel liggen benedenstrooms van de
  Hartelkanaalmonding en worden NIET gepasseerd; idem de Maeslantkering (Nieuwe Waterweg).
  Duisburg-Baerl (51.493, 6.676) ligt bovenstrooms en wordt net niet bereikt.
- **EMO vs. EECV:** het maatgevende thyssenkrupp-duwverkeer laadt primair bij EECV in de
  Dintelhaven (punt 4); EMO belaadt eveneens duwbakken (kade 2013). Vanaf punt 4 zijn beide
  routes identiek — voor deze stroom is EMO het gekozen laadpunt (aansluiting
  `knooppunten`/`aansluitingen.json`). Zie het alternatief-blok bij de EMO-overslag.
- **Kleine dijkdorpen direct aan de vaarweg, niet als eigen rij:** Zuilichem, Nieuwaal, Gameren,
  Hurwenen (Z-oever Waal), IJzendoorn (N-oever), Hulhuizen; Duits: Dornick, Praest, Vrasselt,
  Obermörmter, Vynen, Wallach.
- Plaats-coördinaten zijn OSM-kernen; sommige kernen liggen 1–2 km van de geul (Barendrecht,
  Beuningen, Xanten, Lobith, Rheinberg, Voerde) — de route passeert op de genoemde oever ter
  hoogte van de kern. EuRIS/vaarweginformatie.nl bleken niet scrape-baar; de exacte km-raaien
  van de naamovergangen en de grens-km komen uit secundaire bronnen (§5).

**Negatieve ankers been 3** — mét coördinaat + verbodsstraal (de NIET-nemen-knooppunten uit de
tabel krijgen hier hun toetsbare arm-punt; arm-punten zijn centroïden óp de verboden tak):

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Beerkanaal (zeevaart-kant Mississippihaven) | 51.955, 4.035 | 1,0 km | duwvaart verlaat de haven oostwaarts (doorsteek Beerdam 1997); de `?v=071`-route zat hier fout — verklikker uit deze brief [C1][C2] |
| Maeslantkering / Nieuwe Waterweg | 51.954, 4.163 | 2,0 km | corridor loopt via het Hartelkanaal, niet de Nieuwe Waterweg [C12] |
| Botlekbrug (Oude Maas, benedenstrooms Hartelmonding) | 51.871, 4.353 | 0,8 km | ligt benedenstrooms van punt 11 en wordt niet gepasseerd |
| Spui-arm (t.h.v. Nieuw-Beijerland) | 51.803, 4.435 | 1,5 km | afsplitsing (punt 16) wordt voorbijgevaren — arm richting Haringvliet [C5] |
| Dordtsche Kil (midden) | 51.76, 4.62 | 2,0 km | corridor naar Moerdijk/Antwerpen, niet naar de Rijn [C5] |
| De Noord (t.h.v. Alblasserdam) | 51.86, 4.66 | 2,0 km | Groothoofd (punt 26): de Noord niet nemen [C5][C6] |
| Nieuwe Merwede (midden, Biesbosch) | 51.77, 4.83 | 2,0 km | splitsing Werkendam (punt 31): niet nemen [C6][C7] |
| Kanaal van Sint Andries | 51.804, 5.386 | 1,0 km | Waal–Maas-kortsluiting bij Heerewaarden (punt 45): niet nemen [C24] |
| Amsterdam-Rijnkanaal (t.h.v. Ravenswaaij) | 51.925, 5.435 | 1,5 km | noordtak bij Tiel (punt 49): niet nemen [C8] |
| Maas-Waalkanaal (achter Sluis Weurt) | 51.84, 5.83 | 1,5 km | zuidtak bij Weurt (punt 61): niet nemen [C8] |
| Pannerdensch Kanaal (bij Pannerden) | 51.888, 6.041 | 1,2 km | Pannerdensche Kop (punt 70): kanaal = Nederrijn/IJssel-tak; Pannerden wordt NIET gepasseerd [C9][C10] |
| Stuw Driel (Nederrijn) | 51.95, 5.88 | 5,0 km | Nederrijn–Lek is gestuwd (Driel/Amerongen/Hagestein) — geen zware duwvaart [C13] |
| Wesel-Datteln-Kanal (achter Schleuse Friedrichsfeld) | 51.64, 6.63 | 1,5 km | kanaal-tak op km 813 (punt 85): niet nemen [C20] |
| Haus-Knipp-spoorbrug | 51.479, 6.681 | 0,8 km | ligt bóvenstrooms van de haveningang (km 790,20) — wordt niet gepasseerd [C27] |
| Duisburg-Ruhrort, Becken A (koperkade `cu-duisburg-kade`) | 51.4518, 6.7565 | 1,0 km | productvorm: cokeskool lost bij het staalbedrijf (Schwelgern), niet in het stukgoedbekken — dáár lost de kóperstroom [aansluitingen.json] |

**Toets tegen de atlas van 2026-07-24 (`?v=077`, historisch — netstadium van toen):**

1. **⚠️ Verklikker op de haven-uitvaart: het Beerkanaal hoort er niet in.** De werkelijke
   duwvaartroute verlaat de Mississippihaven **oostwaarts** en gaat bij de Suurhoffbrug direct
   het Hartelkanaal in (open verbinding sinds de doorsteek van de Beerdam, eind 1997). Het
   Beerkanaal is de zeevaart-kant. → lijn corrigeren of verklaren (§6).
2. **Oude Maas bevestigd** — de gerouteerde keuze Hartelkanaal → Oude Maas is de echte corridor
   (operator-bron), dus dát deel van de heal-ronde klopte.
3. **Lengte:** gerouteerd 254 km tegen 240 km operator-opgave; verschil vermoedelijk deels
   Beerkanaal-lus + eindpunt-keuze. Na de correctie opnieuw meten.
4. **Nog te toetsen op de bol** (dekking, werkwijze §4): raakt de lijn de vier
   afslag-beslispunten — Groothoofd (26), Werkendam (31), Loevestein (36), Pannerdensche Kop
   (70) — en de bevestigde steden in volgorde, zonder plaatsen te raken die niet in de brief
   staan. Dit zijn meteen de **via-punten** voor het routeren (werkwijze §5).
5. **Eindpunt:** aansluiting hoort op de Schwelgern-haveningang km 790,20 (51.512, 6.723) /
   loskade (51.50900, 6.73000) — zie ook §5/§6 over het anker.

## Overslag been 3 → been 4 — Werkshafen Schwelgern (schip → band)

**Productvraag:** ladder 4 in §2a — werkshaven van het hoogovenbedrijf; beheer Eisenbahn und
Häfen GmbH (thyssenkrupp).
**anker-id:** `coal-duisburg-kade`.

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 3 | Loskade Werkshafen Schwelgern (losbruggen; brief-punt in het bekken 51.50900, 6.73000 · OSM-pier-anker bij de ingang 51.51321, 6.72347) | losplek | 51.50900, 6.73000 | [C3][C22][C23] + `aansluitingen.json` | bevestigd — **satellietpass moet de losligplaats beslissen (§5/§6)** |
| 2 | terrein | kraan/losbrug → bandopvoer richting kolenopslag — **bandvertrekpunt niet benoemd in OSM: géén coördinaat verzonnen** | verwerkingsstap | — | [D1] (twee kolenopslagen, per schip of wagon te vullen) | onzeker (§5) |
| 3 | vertrek been 4 | transportband het werk op (naar kolenopslag/kokerei) | overslag | — | [D1] | onzeker (§5) |

**Routeerpunt ≠ anker.** Binnenvaart-routeerpunt 51.5059, 6.7248 (snap 0,82 km, gemeten
`aansluitingen.json`) — het duwstel ligt aan de kade, de geul ligt in het bekken/de rivier.

## Been 4 · terrein/band — loskade → kolenopslag → Kokerei Schwelgern

**been-id:** `kolen-cerrejon-ruhr-b4`
**Modaliteit:** transportband (+ wagon mogelijk: de kolenopslagen zijn per schip óf wagon te
vullen [D1]) · **Lengte:** ±0,8 km (hemelsbreed kade → kokerei)
**Stippel:** **ja** — eigen tk-terrein, geen openbaar net (werkwijze §7: stippellijn mét reden)
**Routeerpunt kop / staart:** n.v.t. (geen net)

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Loskade Werkshafen Schwelgern | losplek | 51.50900, 6.73000 | [C3][C22][C23] | bevestigd — satellietpass open (§5) |
| 2 | — | Kolenopslag/mengbedden kokerei (2 opslagen, vulbaar per schip of wagon) — coördinaat niet benoemd in OSM | opslag/stockpile | — | [D1] | onzeker (§5) |
| 3 | ±0,8 | **Kokerei Schwelgern** — kolentoren/batterijen (2 × 70 ovens) | losplek | 51.50193, 6.72713 | [D1][D8: way/228035059] | bevestigd — satellietpass open (§5) |

## Verwerkingsknoop · Kokerei Schwelgern

| | |
|---|---|
| **anker-id** | geen in `aansluitingen.json` — kandidaat `coal-schwelgern-kokerei` (51.50193, 6.72713) |
| **eigenaar van dit anker** | deze brief |
| **in** | kokskolen — ±3,8 Mt/j [D1]; aandeel Cerrejón in de blend: **niet gedocumenteerd (§5)** |
| **andere ingaande strengen** | geen (kolen komen via been 3 binnen; wagon-aanvoer mogelijk [D1]) |
| **uit** | hoogovencokes — ±2,5 Mt/j, per band naar classificatie en verder per band of wagon [D1] |
| **uitgaande strengen** | been 5 (band → hoogovens Schwelgern, hoofdafnemer [D1][D5]) · vertakking per wagon → Hochofen 8 Hamborn (aandeel onbekend, §5) |
| **verlies / bijproduct** | koksgas ±155.000 m³/u (werk-energiehuishouding), teer, benzol, zwavel, ammoniumwaterstofcarbonaat [D1] |
| **feiten** | in bedrijf 13-03-2003; grootste kooksovens ter wereld (8,32 × 0,59 × 20,8 m); sinds aug 2019 eigendom thyssenkrupp Steel Europe, KBS in mei 2020 versmolten [D1]; 50-miljoenste ton kokskolen verwerkt (2016) [D5] |

---

# FASE D · cokes → hoogovens (zelfde complex)

## Been 5 · transportband — Kokerei Schwelgern → Hochöfen Schwelgern 1/2

**been-id:** `kolen-cerrejon-ruhr-b5`
**Modaliteit:** transportband (cokes-classificatie → hoogovenbunkers) [D1] · **Lengte:** ±0,9–1,0 km
**Stippel:** **ja** — eigen terrein, geen openbaar net
**Routeerpunt kop / staart:** n.v.t. (geen net)
**Let op (2b):** dit ís een drager-wissel (band), maar binnen één terrein en één eigenaar —
terreinstappen, geen publieke overslag.

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Kokerei Schwelgern — kokszeef/classificatie (vertrek band) | laadplek | 51.50193, 6.72713 | [D1][D8] | bevestigd — satellietpass open (§5) |
| 2 | ±0,9 | **Hochofen Schwelgern 1** (1973; ±10.000 t ruwijzer/dag; deelrenovatie 2021) | losplek | 51.50492, 6.73965 | [D2][D8: way/231185802] | bevestigd — satellietpass open (§5) |
| 3 | ±1,0 | **Hochofen Schwelgern 2** (1993; ±4.800 m³, haarddiameter 14,9 m — grootste van Europa; ±12.000 t/dag) | losplek | 51.50672, 6.73969 | [D2][D8: way/231187655] | bevestigd — satellietpass open (§5) |
| 4 | — | Sinteranlage Schwelgern (erts-voorbereiding; de twee 250 m-schoorstenen) — **andere ingaande stroom**, ter oriëntatie | referentie (niet aan lijn) | 51.50377, 6.73612 | [D2][D8: way/41151954] | bevestigd |
| 5 | — | Erzlager (het ertsveld tussen haven en ovens) — **andere ingaande stroom** | referentie (niet aan lijn) | 51.50658, 6.73437 | [D8: way/41147780] | aannemelijk |

**Vertakking:** een deel van de cokes gaat **per wagon** naar het Hochofenwerk Hamborn [D1] —
Hochofen 8 (nieuwbouw, in bedrijf dec 2007/feb 2008 [E4]); Hochofen 9 (1962) is op
22-10-2025 stilgelegd [E4]. De Hamborn-ovens zijn in OSM niet als benoemd object getagd
(alleen "Erhaltungsbetrieb Hochofen Hamborn", 51.48531, 6.73228 [D8]) → coördinaat HO8 =
openstaand punt (§5). Zelfde eigenaar, geen eigen stroom-id.

**Negatieve ankers fase D/E** (verwarrings-objecten die een geocoder wél vindt):

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Landschaftspark Duisburg-Nord (museumhoogovens Meiderich, "Hochofen 2/5") | 51.4803, 6.7810 | 1,5 km | stilgelegd hoogovenwerk, nu park/uitzichtpunt [D8: tourism=viewpoint] — naïef geocoderen van "Hochofen Duisburg" landt hier |
| "Oxygenstahlwerk (OX)" Ruhrort (ArcelorMittal-terrein) | 51.46225, 6.74756 | 1,0 km | verkeerde staalfabriek — hoort niet bij thyssenkrupp Schwelgern/Bruckhausen [D8] |
| ehemalige Kokerei August Thyssen (brownfield) | 51.48934, 6.73534 | 0,8 km | gesloten kokerij — de actieve kokerij ligt 1,5 km noordelijker [D8] |

## Verwerkingsknoop · Hochofenwerk Schwelgern (thyssenkrupp Steel)

| | |
|---|---|
| **anker-id** | geen — kandidaten `coal-schwelgern-ho1` (51.50492, 6.73965) / `coal-schwelgern-ho2` (51.50672, 6.73969) |
| **eigenaar van dit anker** | deze brief |
| **in** | cokes ±2,5 Mt/j (been 5) [D1] · sinter/erts (eigen sinteranlage + Erzlager; aanvoer over dezelfde kade — geen eigen brief) · PCI-injectiekolen (aandeel onbekend, §5) |
| **andere ingaande strengen** | ijzererts-stroom over Werkshafen Schwelgern (±23 Mt/j erts+kolen totaal op de kade [C3][C22]) — **nog geen eigen routebrief** |
| **uit** | vloeibaar ruwijzer — ±10.000 (S1) + ±12.000 (S2) t/dag [D2] ≈ orde 8 Mt/j (afgeleid uit dagcijfers) |
| **uitgaande strengen** | been 6: torpedowagens over het werkspoor naar OSW 1 Bruckhausen en OSW 2 Beeckerwerth [D3][D4] |
| **verlies / bijproduct** | hoogovenslak (→ cement/wegenbouw), gichtgas (werk-energie) — bestemmingen niet in deze brief |

---

# FASE E · ruwijzer → staal (keten-eind)

## Been 6 · werkspoor (torpedowagens) — Hochöfen Schwelgern → Oxygenstahlwerk

**been-id:** `kolen-cerrejon-ruhr-b6`
**Modaliteit:** werkspoor — torpedopfannenwagens, beheer Eisenbahn und Häfen GmbH
(thyssenkrupp-dochter, beheert ook de haven [C3][C22]) · **Lengte:** ±1,3 km naar OSW 1
(Bruckhausen); ±3,4 km naar OSW 2 (Beeckerwerth) — hemelsbreed
**Stippel:** **ja** — werkspoor, niet in het atlas-spoornet (het M25-filter dropt
`service=`-rail bewust; zie ook de last-mile-heal-klasse)
**Routeerpunt kop / staart:** n.v.t. (geen openbaar net)

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Abstich Hochofen Schwelgern 1/2 → torpedowagen-belading | laadplek | 51.50492, 6.73965 | [D2][D4][D8] | bevestigd — satellietpass open (§5) |
| 2 | ±1,3 | **Oxygenstahlwerk 1, Duisburg-Bruckhausen** — 2 converters, 5,2 Mt ruwstaal/j; in bedrijf 29-09-1969; ruwijzer uit Hamborn én Schwelgern per pfannen aangeleverd | losplek (keten-eind) | 51.49351, 6.74222 | [D3][D8: way/176976194] | bevestigd — satellietpass open (§5) |
| 3 | ±3,4 | **Oxygenstahlwerk 2, Duisburg-Beeckerwerth** — 1962; 5,9 Mt ruwstaal/j, charges ±265 t, ruwijzer per torpedopfannen uit de Hamborner en Schwelgerner ovens | losplek (tweede afnemer; aandeel onbekend, §5) | 51.48370, 6.70705 | [D4][D8: way/96992481] | bevestigd — satellietpass open (§5) |
| 4 | — | Warmbandwerk 1 (Bruckhausen) — eerstvolgende stap ná het keten-eind, ter oriëntatie | referentie (niet aan lijn) | 51.49634, 6.74192 | [D3][D8: way/220625788] | aannemelijk |

**Waar de keten eindigt, en waarom daar.** Bij de converters van de Oxygenstahlwerke. Drie
redenen, in oplopende hardheid: (1) **de grondstof houdt hier op te bestaan** — de koolstof uit
de Cerrejón-kolen is in de hoogoven als cokes verbrand of in het ruwijzer opgelost, en wordt in
de converter (±20 min, 1.650–1.720 °C [D3]) uitgeblazen; wat doorreist is stáál, een andere
grondstofstroom; (2) **na het staalwerk waaiert de stroom** — brammen of warmband [D3], ±400
staalsoorten voor auto- en verpakkingsindustrie, geen enkelvoudige gedocumenteerde volgende
locatie voor "de Cerrejón-kolen"; (3) het vervolg (Warmbandwerk 1 op ±300 m, Beeckerwerth,
koudband, klanten) hoort in een eigen staal-brief met eigen bewijslast. Het stoppunt is dus
beargumenteerd, geen markt-centroïde. ⚠️ Context: dit eindstuk verandert — HO 9 stilgelegd
okt 2025, capaciteit 11,5 → 8,7–9,0 Mt, DRI-anlage gepland eind 2027 [E4][E5]; stand van de
brief = 2026-07.

---

## 4 · Samenvloeiingen en vertakkingen (overzicht)

| # | been | soort | met welke brief | wat gedeeld wordt | eigenaar anker |
|---|---|---|---|---|---|
| 1 | b5/b6 | samenvloeiing (op het complex) | geen — de ijzererts-stroom over dezelfde kade heeft nog geen eigen brief | Werkshafen-kade + hoogovenknoop | deze brief (tot er een erts-brief is) |
| 2 | b5 | vertakking (terrein) | geen eigen stroom-id — cokes per wagon naar Hochofen 8 Hamborn | kokerei-knoop | deze brief |
| 3 | b3 | alternatief laadpunt | geen — EECV Dintelhaven (±7 Mt kolen/j, tk-eigen) | Hartelkanaal-corridor vanaf punt 4 | deze brief |
| 4 | — | bewust gescheiden | `koper-lobito-duisburg` (kathode → Ruhrort, Becken A) | níets — 7 km uit elkaar; kolen ↛ Ruhrort is hier een negatief anker | elk zijn eigen brief |

**Regel:** één brief = één streng. De erts- en PCI-stromen die bij de hoogovenknoop binnenkomen
worden hier alleen als knoop-input geregistreerd, niet uitgeschreven.

## 5 · Openstaande punten

| # | been | wat | waarom onzeker | wat het zou oplossen |
|---|---|---|---|---|
| 1 | alle | **geen enkel punt in deze brief is satelliet-gelegd** — ook de vier bestaande kolen-ankers (`coal-cerrejon-laad`, `coal-bolivar-kade`, `coal-rotterdam-kade`, `coal-duisburg-kade`) niet, en de nieuwe D/E-ankers evenmin | de brief is vóór de satellietpass geschreven; status "satelliet-gelegd" is nergens overgenomen omdat de oude brief hem nergens had | z16-pass (Esri, 0,01°-grid) over alle laad-/overslag-/losplekken — stond al als "→ VOLGENDE" in de projectstand |
| 2 | b2→b3 | EMO-overslag heeft één anker voor twee rollen (zeeschip-losligplaats vs duwbak-belaadkade "kade 2013") | tweede coördinaat niet bekend; niet verzonnen (werkwijze §2b) | z16-pass scheidt de twee kades → tweede aansluiting |
| 3 | b3/b4 | loskade-discrepantie Schwelgern: brief-loskade in het bekken (51.50900, 6.73000) vs anker `coal-duisburg-kade` op de OSM-pier bij de ingang (51.51321, 6.72347) | twee kandidaat-ligplaatsen ±0,5 km uiteen; OSM-pier heeft moorings maar de kolenlosbruggen zijn niet geverifieerd | z16-pass: waar liggen de losbruggen/duwbakken werkelijk |
| 4 | b3 | EECV-aandeel vs EMO-aandeel in de tk-kolenstroom + exacte EECV-kades (Calandkanaal-zeekade, Dintelhaven-binnenvaartkade) | operator-bronnen noemen EECV als primair tk-laadpunt, maar geen verdeling; ligplaatsen niet gelegd | bron met overslagverdeling, of AIS-trackuiteinden in de Dintelhaven; z16 voor de kades |
| 5 | A/C/D | **Cerrejón-aandeel in de Schwelgern-kokskolenblend niet gedocumenteerd** — gezocht (2026-07-29) op Cerrejón×thyssenkrupp/kokskolen: de gedocumenteerde Cerrejón→DE-stroom is krachtwerkkool (RWE, STEAG, EnBW, E.ON; ±31% van de DE-import) [E1][E2][E3] | niets gevonden dat Cerrejón-kool expliciet bij de kokerij legt; Cerrejón levert vooral thermische + PCI-kwaliteiten | leveranciersinformatie tk Steel of haven-manifestdata; tot dan is "cokeskool" hier de projectdata-aanname en het PCI-/blend-aandeel open |
| 6 | b4 | coördinaat kolenopslag/mengbedden op het kokerei-terrein | niet benoemd in OSM; geen coördinaat verzonnen | z16-pass (mengbedden zijn goed zichtbaar) |
| 7 | b5 | vertakkings-aandeel cokes → Hamborn + coördinaat Hochofen 8 | HO8 niet als benoemd OSM-object; aandeel onbekend, en verschuift na de stillegging van HO9 (22-10-2025) | z16-pass + tk-bron over de cokesverdeling |
| 8 | b6 | verdeling ruwijzer OSW 1 Bruckhausen vs OSW 2 Beeckerwerth voor de Schwelgern-ovens | beide gedocumenteerd als afnemers van Hamborn- én Schwelgern-ijzer [D3][D4]; verdeling onbekend | tk-bron; voor de kaart volstaat OSW 1 als hoofdstreng-eind met OSW 2 als tweede afnemer |
| 9 | b3 | exacte Rijn-km-raaien van de naamovergangen + de grens-km (±857,4) | EuRIS/vaarweginformatie.nl niet scrape-baar; secundaire bronnen | EuRIS-raadpleging of RWS-vaarwegenoverzicht met km-raaien |
| 10 | b1 | Wayuu-plaatsnaam-spelling; treinsamenstelling (109/120/150 wagons per bron); ±25 naamloze overwegen niet gelijst | OSM-only namen; bronnen spreken elkaar tegen | lokale bron; voor de toets niet blokkerend (passagemarge 2 km) |
| 11 | A | jaarvolume mijnexport + aandeel naar Rotterdam | niet vastgesteld in deze brief; treinfrequentie (±7/dag) is de enige observabele hier | Glencore/Cerrejón-jaarcijfers + havenstatistiek Rotterdam |
| 12 | b2 | haven-aanloop Puerto Bolívar: zee-snap 36,44 km (MARNET-korrel); Colombia heeft nul havens met varend AIS-verkeer (wereldscan) | geen trackdata te verwachten — stippellijn is hier vermoedelijk de eindvorm (werkwijze §7) | AIS-check bij een latere scan; anders stippel mét reden laten staan |

## 6 · Conflicten met de projectdata (afwerklijst)

| # | wat | nu | hoort te zijn | bron |
|---|---|---|---|---|
| 1 | `coal-cerrejon-laad` in `aansluitingen.json` | 11.12067, -72.55960 (quarry-centroïde; spoor-snap 5,95 km) | laadlus/laadstation 11.12600, -72.63500 (±8 km westelijker) — de laadplek, niet de put (Escondida-regel) | [A1][A6][A9] + deze brief b1-punt 1 |
| 2 | routering haven-uitvaart Rotterdam (`?v=071`-stand) | via het Beerkanaal | oostwaarts de Mississippihaven uit, bij de Suurhoffbrug het Hartelkanaal in | [C1][C2][C24]; negatief anker b3 |
| 3 | `coal-duisburg-kade` | 51.51321, 6.72347 (OSM-pier bij de ingang) | loskade volgens brief 51.50900, 6.73000 — óf de pier is de echte losligplaats; z16 beslist; evt. tweede aansluiting (§2b) | [C3][C22][C23]; §5-punt 3 |
| 4 | `data/coal.js`-stroom eindigt op "Ruhr"-marktniveau | grofkorrelig eindpunt | keten-eind = tk-complex: kokerei (51.50193, 6.72713) → hoogovens → OSW 1 (51.49351, 6.74222); nieuwe aansluiting-kandidaten in §"verwerkingsknopen" | deze brief, fase D/E |
| 5 | lengte been 3 | "254 km" (`?v=071`) circuleert als hét getal | meting hoort mét gereedschap + eindpunten + netstadium; na de Beerkanaal-correctie hermeten tegen operator-240 km | werkregel projectstand 2026-07-28 |

## 7 · Wat de kaart moet tekenen

1. **Been 1** (doorgetrokken, spoorkleur): laadlus → Puerto Bolívar over de echte OSM-geometrie
   (way/31148047), 150 km; terminal-lus op het havende terrein (let op het OSM-gat van ~1 km —
   last-mile-heal-klasse).
2. **Been 2** (zee, router): Muelle Carbonífero → EMO; haven-aanloop Puerto Bolívar vermoedelijk
   **gestippeld** mét reden (geen AIS-dekking Colombia — §5-punt 12).
3. **Been 3** (binnenvaart, brief-gestuurd via-punt → via-punt): de 93 punten, mét de vier
   afslag-beslispunten (26 · 31 · 36 · 70) en zonder één negatief anker te raken; start
   oostwaarts (níet het Beerkanaal).
4. **Benen 4–6** (gestippeld, reden "eigen terrein/werkspoor — geen openbaar net"): kade →
   kokerei → hoogovens → OSW 1; markers op kokerei, HO S1/S2, OSW 1; OSW 2 en Warmbandwerk 1
   als kleinere context.
5. **Referentiemarkers** (niet aan de lijn): Cuestecitas · NIAG-kolenhaven Orsoy · Sinteranlage ·
   Erzlager.
6. **Alternatief-marker:** EECV Dintelhaven (aandeel onbekend).
7. **Kleur / modaliteit per been:** spoor amber · zee blauw · binnenvaart mint (conform de
   bestaande stromenlaag); terrein-benen stippel in de kolen-kleur.

## 8 · Toets-checklist (invullen bij de controle)

- [x] **Notatie:** alle coördinaten lat, lon met decimale punt; ankers op 5 decimalen
- [x] Elk been heeft een **been-id**; ankers dragen waar mogelijk het `aansluitingen.json`-id
- [ ] Elke laadplek, overslag en losplek heeft status **satelliet-gelegd** (z16) — **nee: nul
      punten; bewust niet geclaimd, zie §5-punt 1** (de oude brief had de status ook nergens)
- [x] Elke laad-/los-/overslagplek heeft een ingevulde **productvraag** (§2a), incl. uitsluitingen
- [ ] Elke overslag heeft **twee** ankers + terreinstappen — EMO nog niet (§5-punt 2), Schwelgern-
      bandvertrek open (§5-punt 6); Puerto Bolívar wél compleet
- [x] **Routeerpunt + max snap** genoteerd bij elk been-uiteinde op water en spoor (gemeten
      waarden uit `aansluitingen.json`; b1-kop "nog te bepalen" — §6-punt 1)
- [ ] **Dekking:** de gerouteerde lijn raakt alle *bevestigde* punten in volgorde — nog niet
      gedraaid (stroom staat nog niet gebakken op de bol)
- [ ] **Verklikker:** geen enkele plaats geraakt die niet in de brief staat — nog niet gedraaid
- [ ] Geen enkel **negatief anker** binnen zijn verbodsstraal geraakt — nog niet gedraaid
- [ ] Lengte per been binnen tolerantie — b1: OSM 153,8 vs 150 km (+2,5%, incl. emplacementen) ✓;
      b3: hermeten na Beerkanaal-correctie (§6-punt 5); b4–b6: hemelsbreed, meten bij het leggen
- [ ] Volumes sluiten aan over de verwerkingsknopen (§2) — kokerei sluitend (3,8 → 2,5 Mt [D1]);
      kade-totaal (23 Mt erts+kolen) nog niet uitgesplitst (§5-punt 5/11)
- [x] Elke stippellijn draagt een **reden**; elk reëel **alternatief** heeft een aandeel óf een
      openstaand punt (EECV → §5-punt 4)
- [x] De keten loopt door tot het eindproduct, of het stoppunt is beargumenteerd (fase E: de
      grondstof houdt bij de converter op te bestaan)

## 9 · Bronnen

*Per fase een eigen lijst; tabelverwijzingen [A..] horen bij fase A, [C..] bij fase B/C
(de nummering van de oorspronkelijke brief is behouden), [D..]/[E..] bij fase D/E.*

**Fase A · spoor [A1..A20]:**
A1 OpenStreetMap/Overpass — spoorlijn way/31148047, keerlus way/166491389, passeerspoor
way/648909503, Muelle 1/2 way/700504446 + way/700504445, terminal way/101458541 (ODbL) ·
A2 https://en.wikipedia.org/wiki/Cerrej%C3%B3n ·
A3 https://es.wikipedia.org/wiki/El_Cerrej%C3%B3n ·
A4 https://en.wikipedia.org/wiki/Puerto_Bol%C3%ADvar,_Colombia ·
A5 https://es.wikipedia.org/wiki/Puerto_Bol%C3%ADvar_(La_Guajira) ·
A6 https://www.cerrejon.com/en/que-hacemos/tren ·
A7 https://comarcaliteraria.blogspot.com/2012/03/historia-del-cerrejon-7-asi-se.html ·
A8 https://ferrocarrilescolombianos.blogspot.com/p/ferrocarril-del-cerrejon.html ·
A9 https://www.rocasyminerales.es/rocas-y-minerales/mineria/cerrejon-la-explotacion-de-carbon-mas-grande-de-todo-sudamerica ·
A10 https://www.defencarga.org.co/contenido-sis/as%C3%AD-es-la-gigantesca-operaci%C3%B3n-de-cerrej%C3%B3n-mayor-productor-de-carb%C3%B3n ·
A11 https://www.eltiempo.com/colombia/otras-ciudades/bloqueo-completa-una-semana-en-linea-ferrea-de-cerrejon-y-empresa-advierte-riesgos-para-operacion-empleo-y-exportaciones-3559515 ·
A12 https://www.infobae.com/colombia/2026/01/16/atentado-a-tren-del-cerrejon-expone-riesgos-de-seguridad-en-la-infraestructura-ferrea-clave-para-la-operacion-minera/ ·
A13 https://www.mining.com/glencore-grabs-anglo-american-bhp-stakes-in-cerrejon-coal-mine/ ·
A14 https://www.railjournal.com/in_depth/the-cerrejon-railway-maximising-infrastructure-life-on-the-heavy-haul-line/ ·
A15 https://www.lasillavacia.com/silla-nacional/caribe/cuatro-mil-millones-de-pesos-no-evitaron-que-uribia-se-inundara/ ·
A16 https://laguajirahoy.com/la-guajira/por-falta-de-recursos-paralizan-intervencion-del-arroyo-chemarrain-en-uribia.html ·
A17 https://www.elheraldo.co/la-guajira/diferencias-entre-indigenas-wayuu-y-el-cerrejon-genera-cierre-de-la-ferrea-991295 ·
A18 https://www.corteconstitucional.gov.co/relatoria/2016/t-704-16.htm ·
A19 https://www.calcularruta.com/de-cuatro-vias-a-uribia.html ·
A20 https://www.minube.net/place/four-tracks--a124029

**Fase B/C · zee + Rijn [C1..C27]:**
C1 https://nl.wikipedia.org/wiki/Hartelkanaal ·
C2 https://nl.wikipedia.org/wiki/Mississippihaven ·
C3 https://de.wikipedia.org/wiki/Werkshafen_Schwelgern ·
C4 https://www.thyssenkruppveerhaven.com/ ·
C5 https://nl.wikipedia.org/wiki/Oude_Maas ·
C6 https://nl.wikipedia.org/wiki/Beneden-Merwede ·
C7 https://nl.wikipedia.org/wiki/Boven-Merwede ·
C8 https://nl.wikipedia.org/wiki/Waal_(rivier) ·
C9 https://nl.wikipedia.org/wiki/Boven-Rijn ·
C10 https://www.rijkswaterstaat.nl/water/vaarwegenoverzicht/boven-rijn ·
C11 https://www.rijkswaterstaat.nl/water/vaarwegenoverzicht/waal ·
C12 https://nl.wikipedia.org/wiki/Hartelkering ·
C13 https://nl.wikipedia.org/wiki/Nederrijn ·
C14 https://www.cementonline.nl/artikelen/innovatieve-kadeconstructie-maasvlakte ·
C15 https://www.hesinternational.eu/en/terminals/emo ·
C16 https://www.binnenvaartinbeeld.com/nl/wiki/zesbaksduwvaart_nederlands ·
C17 https://www.binnenvaartinbeeld.com/nl/Scheepspraat/zesbaksduwvaart ·
C18 https://de.wikipedia.org/wiki/Rheinbr%C3%BCcke_Emmerich ·
C19 https://de.wikipedia.org/wiki/Niederrheinbr%C3%BCcke_Wesel ·
C20 https://de.wikipedia.org/wiki/Wesel-Datteln-Kanal ·
C21 https://de.wikipedia.org/wiki/Hafen_Orsoy ·
C22 https://www.thyssenkrupp-steel.com/de/newsroom/pressemitteilungen/hafen-schwelgern.html ·
C23 https://www.deutsche-leuchtfeuer.de/binnen/rhein/haefen/schwelgern-hafen.html ·
C24 OpenStreetMap via Nominatim + Overpass (geraadpleegd 2026-07-24, ODbL) ·
C25 https://grensfietsen.nl/grensfietsen-nl/grensverhalen/gelderland/86-waar-de-rijn-nederland-binnenkomt/ ·
C26 https://reizen-en-recreatie.infonu.nl/steden/131761-spijk-waar-de-rijn-ons-land-binnenkomt.html ·
C27 https://de.wikipedia.org/wiki/Haus-Knipp-Eisenbahnbr%C3%BCcke

**Fase D/E · complex Duisburg + markt [D1..D8, E1..E5]** (research 2026-07-29):
D1 https://de.wikipedia.org/wiki/Kokerei_Schwelgern — bouw 2000–2003, 2×70 ovens, ±3,8 Mt kolen →
±2,5 Mt cokes/j, kolenopslag per schip/wagon, cokes per band naar het naastgelegen werk,
bijproducten; eigendom tk Steel sinds aug 2019, KBS versmolten mei 2020; coörd. 51.50172, 6.72794 ·
D2 https://de.wikipedia.org/wiki/ThyssenKrupp-Hochofenwerk_Schwelgern — Schwelgern 1 (13-02-1973,
±10.000 t/dag; deelrenovatie 2021), Schwelgern 2 (1993, ±4.800 m³, haard 14,9 m, ±12.000 t/dag,
modernisering 2014), sinteranlage met 250 m-schoorstenen; Duisburg-Marxloh ·
D3 https://www.thyssenkrupp-steel.com/de/newsroom/pressemitteilungen/jung-geblieben-oxygenstahlwerk-von-thyssenkrupp-in-duisburg-feiert-50-jaehriges-jubilaeum.html —
OSW Bruckhausen: 29-09-1969, 2 converters, 5,2 Mt/j, pfannen-aanvoer uit Hamborn + Schwelgern,
converter ±20 min / 1.650–1.720 °C, brammen of gietwals-warmband, ±400 staalsoorten ·
D4 https://www.blechnet.com/stahlwerk-beeckerwerth-feiert-50-geburtstag-a-370551/ — Beeckerwerth:
1962, 5,9 Mt/j, charges ±265 t, "über Torpedopfannen angeliefert" uit de Hamborner en
Schwelgerner hoogovens ·
D5 https://www.thyssenkrupp-steel.com/de/newsroom/pressemitteilungen/140-oefen-im-einsatz-fuer-die-stahlproduktion.html —
140 ovens; 50-miljoenste ton kokskolen; hoofdafnemer = naastgelegen tk-werk Schwelgern ·
D6 https://nl.wikipedia.org/wiki/Ertsoverslagbedrijf_Europoort — EECV: eigendom tk Steel + HKM;
±20 Mt erts + ±7 Mt kolen/j; zeekade 1.100 m Calandkanaal (diepgang tot 23 m); Dintelhaven-kade
900 m met 3 beladers; belading duwbakken door thyssenkrupp Veerhaven ·
D7 https://reportersonline.nl/veerhaven-een-transportband-van-240-kilometer-tussen-rotterdam-en-duisburg/ —
Veerhaven als "transportband van 240 km" Rotterdam→Duisburg ·
D8 OpenStreetMap, lokale Geofabrik-extract `de-nrw-latest.osm.pbf` (ODbL, geraadpleegd
2026-07-29) — way/228035059 (Kokerei Schwelgern) · way/231185802 (Hochofen 1) · way/231187655
(Hochofen 2) · way/41151954 (Sinteranlage) · way/41147780 (Erzlager) · way/4088508 (Werkshafen
Schwelgern, operator ThyssenKrupp Steel Europe) · way/176976194 (Oxygenstahlwerk 1) ·
way/96992481 (Oxygenstahlwerk 2) · way/220625788 (Warmbandwerk 1) · way/125809144
(Erhaltungsbetrieb Hochofen Hamborn) · way/228034614 (ehem. Kokerei August Thyssen, brownfield) ·
museumhoogovens Landschaftspark (tourism=viewpoint, 51.4803, 6.7810) ·
E1 https://www.berliner-zeitung.de/politik-gesellschaft/energiewende-im-nordosten-kolumbiens-wird-steinkohle-fuer-deutsche-kraftwerke-abgebaut-li.25371 —
Cerrejón-kool voor Duitse kráchtwerken; kopers o.a. RWE, EnBW, E.ON ·
E2 https://www.wiwo.de/technologie/wirtschaft-von-oben/wirtschaft-von-oben-189-kolumbien-hier-sitzt-deutschlands-neuer-steinkohle-lieferant/28873432.html —
Colombia als vervanger van Russische steenkool na 2022; ±31%-importaandeel ·
E3 https://www.ruhrbarone.de/woher-kommt-die-kraftwerkskohle/88116/ — STEAG dekte tot 20% van
zijn behoefte met Colombiaanse (vrijwel uitsluitend Cerrejón-) kolen ·
E4 https://de.wikipedia.org/wiki/Thyssenkrupp_Steel_Europe — Hochofen 8 nieuwbouw (in bedrijf
dec 2007/feb 2008); Hochofen 9 (1962) stilgelegd oktober 2025 (laatste abstich 22-10-2025);
DRI-anlage gepland eind 2027 ·
E5 https://www.thyssenkrupp.com/de/newsroom/pressemeldungen/pressedetailseite/thyssenkrupp-steel-stellt-wesentliche-eckpunkte-fur-industrielles-zukunftskonzept-vor-290356 —
capaciteitsreductie 11,5 → 8,7–9,0 Mt/j; Hamborn 8/9 vervangen door DR-anlage + smeltunits
richting 2030

**Eigen metingen:** snap-afstanden per anker uit `v2/data/aansluitingen.json`
(`maak_aansluitingen.py`, netstadium 2026-07-23/28) · OSM-scan de-nrw-extract met pyosmium
(2026-07-29, bbox 51.44–51.56 / 6.62–6.82) · satelliet-overlay Esri z16: **nog te draaien** (§5).
