# De overslag — ontwerpbesluit na het vierpanel (LAR-518)

*Vastgelegd 2026-07-20/21. Bron: vier onafhankelijk uitgewerkte architecturen, elk aangevallen
door drie skeptici met eigen lens (invarianten · M25 · werkelijkheid), alle met eigen metingen
op de echte bake (73.941 knopen / 69.855 edges / `?v=039`). De ruwe ontwerpen en aanvallen
staan in de workflow-journals van 2026-07-20; dit document is de synthese.*

---

## 1 · De belangrijkste uitkomst is geen routeerontwerp

**Het riviernet is geen net maar 10.670 losse fragmenten (mediaan 4,8 km), en dáár sterft elke
overslag — welk mechanisme je ook kiest.** Vier ontwerpen, twaalf aanvalsronden, en elke meting
komt op hetzelfde uit:

- New Orleans hangt aan een fragment van 222 km, Cincinnati aan één van 16 km, Baton Rouge aan
  een derde van 1.148 km **dat geen van beide bevat**. De vlaggenschip-acceptatie
  (R'dam→Cincinnati = zeeschip + duwkonvooi) bestaat in deze bake niet.
- R'dam→Duisburg — de drukste binnenvaartrelatie ter wereld — is onbouwbaar: Duisburgs fragment
  is 2 knopen / 1,5 km groot.
- **2.149 van de 3.962 havens (54%) kunnen nooit een route krijgen**, welke lijst je ook aanwijst.
  Van de 21 grootste riviercomponenten hebben er 14 geen enkele haven binnen 25 km; twee derde
  van de 374.342 km raakt geen haven, hoe dan ook.
- Zelfs met álle 572 mechanische kandidaten aangewezen ontsluit een overslag 9,4% van het
  riviernet, mediaan 9,2 km achter de haven.

**→ HET STITCHEN VAN HET RIVIERNET IS EEN HARDE VOORWAARDE VÓÓR DE OVERSLAG, GEEN VERVOLGSTAP.**
Wie de overslag eerst bouwt, levert een mechanisme dat overwegend "geen pad" zegt (eerlijk maar
onbruikbaar) of — erger — zelfverzekerd verkeerde plaatsnamen toont: één panel-prototype gaf
R'dam→Nijmegen als *"overslag bij Willemstad, 205 km"* — een verzonnen tweede schip in een
vestingdorp met een jachthaven, voor een route die in werkelijkheid één Rijnschip is (~172 km).
Meetbare stitch-doelen staan in §6.

## 2 · Wat de aanvallen definitief hebben beslist (met bewijs, niet mening)

1. **Een overslag is geen edge — nu gemeten, geen aanname meer.** Nul-kost-edges op de 572
   kandidaten breken twee invarianten onmiddellijk: R'dam→Shanghai 19.610 → 19.604 (−5,2) en
   Duluth→R'dam 8.031 → 7.998 (−33,2). Na stitchen wordt dat erger, niet beter.
2. **Geen enkele afstandsdrempel kan havens classificeren.** Manaus is een échte oceaanhaven
   (Panamaxen, 1.500 km de Amazone op) met zee-snap **1.084 km**; Duisburg wordt door geen
   zeeschip aangelopen op **152 km**; Port Hedland (80,8) en Nijmegen (79,1) verschillen 1,7 km
   in snap en zijn elkaars tegendeel. **Het interval is leeg.** Elke guard, trap of zaaidrempel
   die van de snap-afstand afhangt erft de al bewezen straf-onmogelijkheid in een nieuw kostuum.
   → De modaliteit van een punt is een **aangewezen eigenschap**, precies Lars' besluit,
   consequent doorgetrokken.
3. **De aangewezen lijst mag niet op `ports.json` gesleuteld zijn.** Kasumbalesa, Khorgos,
   Alashankou, Malaszewicze, Erenhot, mijn-railheads (Carajás, Kiruna) — géén staat in
   ports.json, en drie ervan leven al als knelpunt in `_chokepoints.js`. LOCODE alleen is
   bovendien geen sleutel: 38 duplicaten, waaronder USPWM = Portland Oregon **én** Portland
   Maine (4.083 km uit elkaar — één aanwijzing zou per ongeluk de complete VS-landbrug openen).
4. **Knoop-identiteit kan haven-identiteit niet dragen.** 3.962 havens delen 1.854 zeeknopen;
   knoop 6811 draagt 22 havens van Antwerpen (18 km) tot Straatsburg (394 km); knoop 6781
   draagt Amsterdam, Nijmegen, Duisburg én Krefeld. Elke overstap die op "een aangewezen haven
   raakt deze knoop" triggert, is een gratis teleport voor alle 22. → De overstap springt over
   een **expliciet knopenpaar dat in de aangewezen entry zelf staat**.
5. **Eén `opties.schip` over alle benen is de oorspronkelijke bug in nieuwe kleren.** Het issue
   heet "3 schepen, niet 1" — dus **scheepsklasse per been**, anders vaart de Vb-duwbak alsnog
   19.610 km over de Indische Oceaan (gemeten: het zeenet heeft 12 gabariet-edges op 15.933,
   het filter houdt daar niets tegen).
6. **"Geen pad" moet een reden dragen.** Drie oorzaken geven nu hetzelfde antwoord (netten niet
   verbonden · geen aangewezen punt · maat past niet) en zijn voor de gebruiker niet te
   onderscheiden van een kapotte feature.

## 3 · Het gekozen mechanisme

**Kern = het "Overslaglagen"-motorontwerp** (gelaagde A* met toestand *(knoop, aantal
overstappen)*, één heap, lexicografische sleutel *(laag, g+h)*) — het enige van de vier waarvan
de motor **exact gemeten klopte**: R'dam→Shanghai bit-identiek aan de huidige router (19.609,7,
zelfde 4.670 bezochte knopen), multi-source Dijkstra gratis ingevouwen (géén paren-probleem,
kosten onafhankelijk van de lijstgrootte), heuristiek toelaatbaar per laag, geen strafgetal,
geen rebake. **Plus de identiteits-analyse uit het "Havenknoop"-ontwerp** (bevinding 4
hierboven), maar zónder hubs in de bake te bakken: dat kostte een rebake, 42% dode knopen en
een ports.json-gebonden identiteit. Het expliciete knopenpaar verhuist naar de data.

### 3a · Het aangewezen register: `v2/data/knooppunten.json`

Een **eigen entiteit met een eigen stabiele id** — geen afgeleide van ports.json:

```json
{ "versie": 1, "punten": [
  { "id": "rotterdam", "naam": "Rotterdam", "locode": "NLRTM",
    "aanhechting": { "zee": [4.05, 51.99], "binnen": [4.32, 51.90] },
    "overslag": [["zee", "binnen"]],
    "bron": "aangewezen 2026-07-21" }
] }
```

- `aanhechting` = per modaliteit een **coördinaat**; de lader snapt elk op zijn eigen net en
  **rapporteert de snap-afstand** — de machine meet, de redacteur oordeelt (geen drempel,
  besluit 2). Een punt zónder `zee` biedt nooit een zee-aanhechting aan, hoe dichtbij MARNET
  ook ligt — dat is de Duisburg-fix, redactioneel in plaats van mechanisch.
- `overslag` = welke paren hier mogen wisselen. Leeg = wel adresseerbaar, geen overslagpunt.
- M25 schuift erin zonder breuk: `"spoor": [lon,lat]` erbij, en Kasumbalesa krijgt gewoon een
  entry — het is geen haven en dat hoeft niet meer.
- Lader faalt **hard** op een onoplosbare of dubbelzinnige entry (nooit stil overslaan).

### 3b · De router: `zoekKeten(van, naar, opties)`

- **Een been mengt nooit netten** — structureel waar (0 kruisende edges, blijft toetsbare
  invariant) — en draagt de modus van zijn net: een been over het riviernet ís een binnenschip
  en wordt zo gerapporteerd en gekleurd.
- **Uiteinden zaaien per net, mét hun aanloopkosten in `g`** (gemeten noodzakelijk: zonder
  zaaikosten wint een onzinroute naar een knoop 304 km naast Cincinnati). Geen zaaidrempel —
  een aanloop van 79 km is gewoon 79 km die eerlijk meetelt en verliest vanzelf van 2 km.
- **Overstappen alleen op een aangewezen punt**, over het expliciete knopenpaar uit de entry,
  +1 laag; de fysieke sprongafstand telt mee in de kilometers (geen wormgat).
- **Lexicografisch: minste overslagen wint, daarbinnen minste km.** Dát is het structurele slot
  op de Donau-ring: R'dam→Shanghai slaagt met 0 overslagen op zee en een keten door Europa
  (2 overslagen) wordt **nooit in kilometers vergeleken** — er is geen getal om verkeerd te
  kiezen. `maxOverstap = 2` (Lars' "3 schepen"), heap gedimensioneerd op toestanden **mét
  bounds-assert** (de huidige `n*8` zonder check is bij overloop een stille no-op op een typed
  array — gemeten faalgedrag: verkeerde routes zonder foutmelding).
- **Scheepsklasse per been**: zee-been → zeeschipkeuze, binnen-been → CEMT/VS-tow-keuze.
- **"Geen pad" geeft de reden terug** (besluit 6).
- `zoekRoute()` blijft ongewijzigd als eenlaags-primitief; `zoekRouteRealistisch()` en het
  `binnenvaart`-groepslabel blijven staan (gemeten no-op, maar twee sloten weggooien in
  dezelfde sessie waarin je de deur verbouwt is precies hoe het misgaat) — opruimen mag pas
  als `toets_routes.py` groen is op het nieuwe pad.

### 3c · Waarom dit de bekende gevallen goed doet (na het stitchen)

| route | uitkomst | waarom |
|---|---|---|
| R'dam→Shanghai | zeeschip 19.610, 0 overslagen | 0-overslag zee wint lexicografisch; keten wordt nooit geënumereerd |
| R'dam→Nijmegen | **binnenschip ~172, 0 overslagen** | rivier-zaad→rivier-zaad op één component; aanloop 0,6+2,0 verslaat zee-aanloop 1,1+79,1 — **géén verzonnen Willemstad-overslag** |
| R'dam→Cincinnati | zeeschip → **overslag New Orleans** → duwkonvooi | geen 0-overslagpad; New Orleans is aangewezen én raakt beide netten (3,3/3,3 km) |
| R'dam→Duisburg | binnenschip over de Rijn | zelfde patroon als Nijmegen |
| haven zonder verbinding | geen pad + reden | valkuil 4, nu diagnosticeerbaar |

## 4 · Verworpen, met de doodsoorzaak erbij (niet opnieuw onderzoeken)

- **Trap-/laddersjablonen met afstandsguards** — de guard is de vaste straf in vermomming
  (leeg interval, besluit 2), en de H-keuze "beste som wint" bouwde de Donau-ring opnieuw:
  gemeten Bremen→Shanghai via **Sète** (binnenschip dwars door Frankrijk), 1.921 km "winst" —
  tweemaal de oorspronkelijke ringfout.
- **λ/τ-kostmodel per laag** — de ketenautomaat vuurde op de echte data letterlijk nooit
  (["zee"] slaagt voor élk havenpaar), en zodra spoor op laag 0 meedoet is λ precies de
  eendimensionale afweging waarvan al bewezen is dat geen getal haar oplost.
- **Hubs in `marnet.bin` bakken** — rebake, +42% dode knopen, identiteit aan ports.json
  geklonken; het waardevolle deel (expliciet knopenpaar) is overgenomen in de datalaag.
- **Vaste straf per overslag** — al eerder bewezen onmogelijk; nu drie keer onafhankelijk
  herbevestigd met verse getallen.

## 5 · Wat dit bewust NIET oplost (opgeschreven zodat niemand denkt van wel)

1. **Modale economie.** Bij twee 0-overslagroutes wint de kortste in km; of lading per
   binnenschip of zeeschip gaat is economie die de graaf niet kent. Het antwoord draagt nu wél
   een eerlijk modus-label, en de maten (LAR-519) knijpen het verder per klasse.
2. **M25's landbrug-vraag.** Een zuivere spoorroute heeft 0 overslagen en concurreert dan in
   dezelfde laag op km met zee — 7 van de 11 invarianten zouden naar een trein kantelen. De
   uitweg is genoteerd en is géén kostmodel: **de atlas hoeft de modal split niet te raden — de
   flows-data draagt al `mode` per been** (ship/rail/road/pipeline, 275 landstromen). De
   simulator routeert bekende stromen langs hun opgegeven ketens; hij verzint geen vervoerskeuze.
   Dat besluit hoort bij de start van M25, niet nu.
3. **Intramodale overslag** (spoorwijdte-breuken Malaszewicze/Alashankou). Vereist "hier MOET
   je wisselen" naast "hier mag je wisselen" — M25-ontwerpvraag, het register kan het dragen.

## 6 · Volgorde en meetpunten

**Stap 0 — riviernet stitchen (eigen issue, eerst, dit is het echte werk).**
Acceptatie meetbaar: R'dam- en Nijmegen-rivierknoop één component · New Orleans, Baton Rouge,
Memphis en Cincinnati één component · componenten 10.670 → orde honderden · lengtetoets per
corridor tegen ijkpunten (de bestaande methode; let op de 19e-eeuwse-voorganger-val en de
Mosel-signatuur — een naad die twee meanders kortsluit is een sluipweg).

**Stap 1 — `v2/tools/toets_routes.py`** (vóór het routerwerk): de elf invarianten headless
narekenbaar (panel-prototypes bewezen 19.609,7 en 8.030,9 exact reproduceerbaar zonder
browser), plus anti-ring-toetsen en de geen-pad-redenen. De repo heeft nu nul uitvoerbare
tests; dit werk introduceert ze.

**Stap 2 — `knooppunten.json` + lader** (~20–40 aangewezen havens om te beginnen; Rotterdam,
Antwerpen, Hamburg, New Orleans, Shanghai, Manaus, …).

**Stap 3 — `zoekKeten` + HUD** (benen met eigen kleur/klasse, overslagpunt benoemd, reden bij
geen pad).

**Acceptatie van het geheel** = de tabel in §3c, plus: zeeroutes exact (19.610 / 8.031), geen
enkele bestaande zeeroute korter, en de anti-ring-toets bewijst dat voor R'dam→Shanghai nooit
een keten wordt geënumereerd.

**Bijvangst die sowieso moet** (drie aanvallers onafhankelijk): bounds-assert op de heap ·
`dichtstbijzijndeKnoop()` krijgt een netfilter (geeft sinds het riviernet vaak een rivierknoop
op een kaartklik) · noot: `passages` telt 53.989 entries waarvan 52 echte zeestraten — wie
erover itereert toont het halve riviernet.
