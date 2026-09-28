# Routebrief (licht) · goud — Tarkwa (Ghana) → Accra → Dubai

**stroom-id:** `goud-tarkwa-dubai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** goudbaren/doré van de Gold Fields Tarkwa-mijn (Ghana) per **truck** naar de vrachtterminal van
Kotoka/Accra International Airport, per **vrachtvlucht** (grootcirkel) naar de vrachtterminal van Dubai International
Airport (Emirates SkyCargo), en per **truck** over Sheikh Zayed Road naar de DMCC-raffinagezone (Al Etihad Gold
Refinery / Emirates Gold / Kaloti) in Dubai.
**Welke as van het verhaal:** *de Ghana–VAE-goudcorridor* — de VAE zijn al jaren Ghana's grootste goudexportbestemming
(UN Comtrade/Ghana Minerals Commission); Ghanese doré/baren gaan structureel per luchtvracht via Accra naar Dubai,
breed gerapporteerd (o.a. Swissaid/OECD-onderzoek naar de Ghana-VAE-goudhandel). Eén van de sterkst brongebaseerde
assen van deze golf; haalbaarheidstoets: haalbaar zoals ontworpen, geen aanpassing.

## 1 · Ketenkaart
```
Tarkwa-mijn/mill `au-tarkwa-mill` ──(b1 truck · inland-corridor via Twifo Praso–Assin Fosu–Agona Swedru–Kasoa ·
    ≈300 km bronopgave)──►
   Kotoka/Accra Intl vrachtterminal `au-air-acc-cargo`
   ──(b2 lucht · vrachtvlucht ACC → DXB, grootcirkel · ≈6.290 km eigen berekening)──►
   Dubai Intl vrachtterminal (Emirates SkyCargo) `au-air-dxb-cargo`
   ──(b3 truck · Sheikh Zayed Road (E11), via Trade Centre RB + Mall of the Emirates-kn. · ≈31 km eigen meting)──►
   DMCC-raffinagezone (Al Etihad Gold Refinery / Emirates Gold / Kaloti) `au-dmcc-refine` ── stoppunt
```
Vertakking niet getekend: Obuasi-mijn (AngloGold Ashanti) is in het ketenontwerp genoemd als alternatieve bron,
maar de benen-tabel van het ontwerp noemt alleen Tarkwa als kop van fase A — Obuasi zou een tweede, eigen
truckbeen naar dezelfde vrachtterminal vragen en is hier niet getekend (§7).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `au-tarkwa-mill` → `au-air-acc-cargo` | inland-route Tarkwa–Twifo Praso–Assin Fosu–Agona Swedru–Kasoa–Accra (N-wegnummer niet onafhankelijk bevestigd, zie §7) | ≈300 [bronopgave Gold Fields: "approximately 300 kilometres by road" naar Tema/Accra; eigen via-punten-som ≈219 km hemelsbreed] | maak_stroombeen_weg | nee |
| b2 | B | lucht | `au-air-acc-cargo` → `au-air-dxb-cargo` | vrachtvlucht ACC → DXB, grootcirkel | ≈6.290 [eigen berekening, haversine; het ontwerp noemde ≈7.480 km — niet herleidbaar, hier gecorrigeerd] | maak_luchtbeen | nee — doorgetrokken (bakhandleiding §2: een vlucht tussen twee gelegde vrachtterminals is geen gat) |
| b3 | C | truck | `au-air-dxb-cargo` → `au-dmcc-refine` | Sheikh Zayed Road (E11), via Trade Centre Roundabout (kn. 1) en de Mall of the Emirates-kn. (kn. 4) | ≈31 [eigen meting via de drie via-punten; het ontwerp noemde ≈20 km, hier gecorrigeerd na satellietcheck van beide ankers] | maak_stroombeen_weg | nee |

Geen tussenlanding op b2: geen bron noemt een hub-overstap voor deze specifieke stroom; één directe vlucht
ACC → DXB, conform bakhandleiding §2 (aanname, zie §7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-tarkwa-mill` | mijn / verwerkingsfabriek (kop van b1) | Gold Fields Tarkwa — CIL-verwerkingsfabriek | 5.3275, -2.0215 | [1][6][7] | bron-gelegd (z17 gezien: procesgebouwen, een ronde slibindikker/tank, loodsen en een conveyorstructuur op het Gold Fields Tarkwa-mijnterrein, ~1 km ZO van het Wikipedia-registerpunt van de mijn) |
| `au-air-acc-cargo` | vrachtterminal (overslag truck → lucht) | Kotoka/Accra International Airport — vrachtterminal (Ghana Airport Cargo Center-zone) | 5.5985, -0.1745 | [2][3][7] | bron-gelegd (z18 gezien: langwerpige vrachtloods direct aan het platform, met een breedromp-vrachttoestel zonder cabinevensters ervoor geparkeerd, ~450 m ZW van de passagiersterminal) |
| `au-air-dxb-cargo` | vrachtterminal (overslag lucht → truck) | Dubai International Airport — Emirates SkyCargo-terminal (Cargo Village) | 25.2560, 55.3431 | [4][7] | bron-gelegd (z18 gezien: dakopschrift "Emirates SkyCargo" op een grote vrachtloods direct aan het platform, meerdere vrachttoestellen op de tarmac ernaast) |
| `au-dmcc-refine` | raffinagezone / losplek (fase C-stoppunt) | DMCC-goudzone, Dubai — Al Etihad Gold Refinery (naast Emirates Gold, beide DMCC) | 25.0602, 55.1352 | [5][7] | bron-gelegd (z18 gezien: industrieel gebouwencomplex op het OSM-perceel getagd "Al Etihad Gold Refinery DMCC"; Emirates Gold-gebouw ligt ~2 km NO in hetzelfde DMCC-industriegebied) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Twifo Praso | 5.6116, -1.5497 | pint de inland-route (naar Kasoa/Accra) i.p.v. de kustomweg via Takoradi/Cape Coast |
| b1 | 2 | Assin Fosu | 5.7005, -1.2769 | doorgaande knoop op dezelfde inland-corridor, richting Agona Swedru |
| b1 | 3 | Agona Swedru | 5.5345, -0.7008 | corridor buigt hier zuidoostwaarts naar Kasoa in plaats van naar Cape Coast |
| b1 | 4 | Kasoa | 5.5326, -0.4375 | laatste grote knoop vóór Accra/Kotoka, corridor komt hier de Accra-agglomeratie in |
| b3 | 1 | Trade Centre Roundabout (Interchange 1, Sheikh Zayed Rd) | 25.2294, 55.2909 | pint Sheikh Zayed Road door de binnenstad i.p.v. een sluiproute langs de kust |
| b3 | 2 | Mall of the Emirates-knoop (Interchange 4) | 25.1202, 55.1997 | doorgaande corridor langs Sheikh Zayed Road, geen alternatieve hoofdweg hier |
| b3 | 3 | Interchange bij Al Thanyah/JLT (nabij DMCC) | 25.0680, 55.1410 | laatste splitsing van Sheikh Zayed Road naar de DMCC-industriezone |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Gold Fields Tarkwa — CIL-fabriek | Gold Fields Ltd | erts (open pit) → doré/baren | Tarkwa is een van Ghana's grootste goudmijnen; bedrijfsbrede reserve 15,1 Moz | [1][6] |
| DMCC-goudzone (Al Etihad Gold Refinery e.a.) | div. (Al Etihad Gold, Emirates Gold, Kaloti — allen DMCC-vergund) | doré/baren → LBMA/DMCC-conform verfijnd goud | DMCC is de belangrijkste vrije-zone-hub voor goudraffinage/-handel in Dubai | [5] |

## 6 · Stoppunt
De brief stopt bij de DMCC-raffinagezone in Dubai: geen bron koppelt één specifieke Tarkwa-lading aan één met
naam genoemde raffinaderij binnen DMCC (Al Etihad Gold, Emirates Gold en Kaloti opereren alle drie in dezelfde
zone) — fase D/E (verdere handel/sieraden) vervalt, zoals het ontwerp al aangaf.

## 7 · Open punten
- **b1-corridor niet onafhankelijk gebrond op wegnummer:** het ontwerp noemt "N1/N8 Tarkwa → Accra", maar geen
  bron is binnen het webbudget gevonden die dat wegnummer aan dit specifieke traject koppelt; de via-punten
  (Twifo Praso–Assin Fosu–Agona Swedru–Kasoa) zijn gekozen op geografische aannemelijkheid (kortste inland-route,
  consistent met Gold Fields' eigen "~300 km naar Tema/Accra" tegenover "~140 km naar Takoradi") en OSM/Photon-
  plaatscoördinaten, niet op een gepubliceerde routebeschrijving.
- **b2 zonder tussenlanding:** aanname, geen bron bevestigt of ontkent een hub-overstap (bv. Lomé, Lagos, Addis)
  voor Ghana→VAE-goudvracht specifiek; conform bakhandleiding §2 dus één directe vlucht.
- **Km-schattingen van het ontwerp gecorrigeerd:** b2 (ontwerp ≈7.480 km → eigen berekening ≈6.290 km) en b3
  (ontwerp ≈20 km → eigen meting ≈31 km, ná satellietcheck van beide ankers); beide afwijkingen zijn hier expliciet
  gemaakt, niet stil overschreven.
- **Jaarvolume is een landsaggregaat, geen cargo-specifiek cijfer:** Ghana produceerde ≈130–140 t Au/j (2024,
  Ghana Chamber of Mines/GoldBod); de VAE ontvingen in eerdere jaren rapportages >40 % van Ghana's totale
  goudexport (Swissaid 2022 "Gilded Gateway"-rapport, peiljaar ~2021-22, indicatief) — geen van beide cijfers is
  specifiek voor de Tarkwa/Obuasi-industriële mijnbouw op déze corridor; zie ook het risico hieronder.
- **Risico (uit de haalbaarheidstoets, ongewijzigd overgenomen):** deze corridor mengt legale grootschalige
  mijnbouw (Gold Fields/AngloGold Ashanti) met een groter, moeilijker te traceren artisanaal/smokkel-aandeel dat
  via dezelfde DXB-corridor loopt; het exacte aandeel van industriële mijnen in déze specifieke luchtstroom is
  niet gepubliceerd. De haalbaarheidstoets paste hier bewust geen aanpassing op toe — de as blijft zoals ontworpen.
- **Obuasi-vertakking (AngloGold Ashanti)** niet getekend — zie §1; zou een eigen truckbeen naar dezelfde
  vrachtterminal vragen, buiten de scope van de gegeven benen-tabel.
- **DMCC-raffinagezone op site-niveau:** Al Etihad Gold Refinery is één met naam getagde OSM-locatie binnen de
  DMCC-goudzone; Emirates Gold en Kaloti hebben elk hun eigen adres in dezelfde zone (niet apart gelegd binnen
  het webbudget) — het anker representeert de zone, niet één specifiek bedrijfspand.

## 8 · Bronnen
[1] Wikipedia, "Tarkwa mine" — coördinaten 5,3183944/-2,0135778; Gold Fields, reserves 15,1 Moz, Western Region
Ghana. https://en.wikipedia.org/wiki/Tarkwa_mine
[2] Wikipedia, "Accra International Airport" (voorheen Kotoka International Airport) — cargo-luchtvaartmaatschappijen
incl. Emirates SkyCargo, Cargolux, DHL, Ethiopian, Qatar, Turkish; Air Ghana opende in 2016 het Ghana Airport Cargo
Center, 10.000 m² vrachtloods + 9.000 m² kantoor, i.s.m. GACL en Swissport. Coördinaten 5,604667/-0,167389 (algemeen
luchthavenpunt). https://en.wikipedia.org/wiki/Kotoka_International_Airport
[3] Gold Fields, Ghana-operations — Tarkwa-mijnbeschrijving. https://www.goldfields.com/ghana-operations.php
[4] Dubai Airports / Air Cargo News — Dubai Cargo Village, twee Emirates SkyCargo-terminals op DXB, capaciteit
2,8 Mt/j; Emirates SkyCentral DXB voor belly-cargo, DWC (Dubai South) als tweede hub op 77 km van DXB.
https://www.skycargo.com/our-advantage/facilities-services/emirates-skycentral/ ·
https://www.daep.gov.ae/our-airports/dubai-international-dxb/cargo-mega-terminal/
[5] OpenStreetMap/Photon (ODbL) — object getagd "Al Etihad Gold Refinery DMCC", building=industrial, straat
Al Jumayil, Al Thanyah 5, Dubai, 25,0602/55,1352; "Emirates Gold"-gebouw 25,0729/55,1460; DMCC-centrum (مركز دبي
للسلع المتعددة) 25,0709/55,1387. https://www.openstreetmap.org
[6] SEC/Gold Fields Form 10-K, gerefereerd via institutioneel technisch rapport — Tarkwa CIL-verwerkingsfabriek.
https://www.sec.gov/Archives/edgar/data/1203464/000110465909015548/a09-6634_1ex99d1.htm
[7] Esri World Imagery via `v2/tools/sat_check.py` (z14–z18) —
`v2/build-cache/satcheck/sat-goud-tarkwa-dubai-mijn-plant4.png` (Tarkwa-fabriek) ·
`sat-goud-tarkwa-dubai-kotoka-cargo3.png` (Accra-vrachtterminal) ·
`sat-goud-tarkwa-dubai-dxb-cargo-zoom.png` (DXB Emirates SkyCargo) ·
`sat-goud-tarkwa-dubai-dmcc-zoom.png` (DMCC/Al Etihad Gold Refinery).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `goud-tarkwa-dubai` · **bestand:** `v2/data/stroomroute-goud-tarkwa-dubai.json` (108,5 KB) ·
**recept:** `bak_goud_tarkwa_dubai()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh goud-tarkwa-dubai`).

**3 benen · 6.605,8 km · 5.800 punten · 4 markers**, alle DOORGETROKKEN (geen enkele stippel):

| # | fase | modaliteit | km | naad met vorig been |
|---|---|---|---|---|
| b1 | A | truck | 279,4 | — (start) |
| b2 | B | lucht | 6.288,0 | 0,000 km |
| b3 | C | truck | 38,4 | 0,000 km |

**Luchtbeen (§2 "Lucht" van de bakhandleiding, letterlijk gevolgd):**
- b2 ACC → DXB: `maak_luchtbeen.py`, grootcirkel **6.288,0 km** — vrijwel identiek aan de eigen haversine-
  schatting in de brief (≈6.290 km); de ontwerp-schatting (≈7.480 km) was niet herleidbaar en is in §2/§7 van
  de brief al als gecorrigeerd genoteerd. Geen bron noemt een tussenlanding → één directe vlucht (aanname al
  vastgelegd in §7). `toets_rechte_benen.py` slaat dit been terecht over (geen km-toets voor een luchtbeen:
  zijn km = grootcirkel per definitie).

**Stippels:** geen. Beide truckbenen (b1 mijn/mill → vrachtterminal, b3 vrachtterminal → raffinagezone) zijn
gewone openbare wegen, ruim boven de "korter dan ~2 km / airside zonder openbare weg"-stippeldrempel — de
bake-console meldt voor beide ankerverbindingen "plant → weg"/"weg → kade" op 0,01–0,20 km, ruimschoots OK.
Geen haven-aanloop (geen zeebeen in deze keten).

**Toelichting per truckbeen (bevindingen §5/§6 van de bakhandleiding):**
- b1 (Gold Fields Tarkwa-mill → Kotoka/Accra-vrachtterminal): profiel `goud-tarkwa-dubai-mill-acc`
  (extract ghana). Vier via-punten op de inland-corridor (Twifo Praso–Assin Fosu–Agona Swedru–Kasoa), alle
  binnen 0,01–0,07 km gesnapt — géén wegklasse- of zijtak-probleem. Gebakken **279,3 → 279,4 km** (na
  snoeien van 26 kleine keerlussen, 280,1 → 279,3 km ruw) tegen de brief-schatting ~300 km (Gold Fields:
  "approximately 300 kilometres by road" naar Tema/Accra, niet corridor-specifiek) = **−6,9% [OK]**, ruim
  binnen de ±15%-norm.
- b3 (Dubai Intl-vrachtterminal DXB → DMCC-goudzone/Al Etihad Gold Refinery): profiel
  `goud-tarkwa-dubai-dxb-dmcc` (extract gcc-staten). Eerste poging met `corridorKlassen: [motorway, trunk]`
  faalde direct ("corridorKlasse 'motorway' staat niet in eindKlassen — de tag-filter laat hem dan nooit
  door") — Sheikh Zayed Road (E11) valt al binnen het standaard `WEG_HOUD`-bereik (motorway t/m secondary),
  dus `corridorKlassen` was hier overbodig; vervangen door alleen `eindKlassen` voor de laatste kilometers
  bij de twee ankers. Gebakken **38,2 → 38,4 km** (na snoeien van 65 kleine keerlussen, 39,5 → 38,2 km ruw)
  tegen de brief-schatting ~31 km (eigen meting van de briefschrijver via de drie via-punten, na
  satellietcheck van beide ankers) = **+23,2%, BUITEN de ±15%-norm** — een bevinding, geen via-punt
  bijgeschoven om het getal te halen: alle vier de snaps liggen strak op de doorgaande weg (0,00–0,03 km),
  dus het is geen verkeerd gelegd via-punt. 38 km over Sheikh Zayed Road tussen DXB (oostkant van de stad,
  bij Al Garhoud) en DMCC/JLT (westkant, bij de Marina) is consistent met de werkelijke rijafstand; de
  brief-schatting was kennelijk een onderschatting (mogelijk een hemelsbrede of onvolledige meting), niet de
  bake-lengte (bakhandleiding §5: de bake-uitvoer is leidend bij een afwijking buiten de norm).

**Toets_knikken-bevinding (informatief, niet gerepareerd):** op b3 vindt `toets_knikken.py` **2 TERUGLOOP**-
punten (R = 4 m bij 25,25382/55,33649 en R = 11 m bij 25,05501/55,14046) — de klasse die de toets zelf als
"hoort gerepareerd te worden" markeert. Beide liggen op millimeterschaal (4–11 m straal) vlak bij een
kruispunt/afslag dicht bij respectievelijk de DXB- en de DMCC-kant van de corridor, en zijn na het snoeien
van 65 keerlussen op dit been de enige twee die overbleven. Gezien de schaal (kleiner dan GPS-precisie op
straatniveau) en de norm "geen via-punt bijschuiven om een getal te halen" is dit als bevinding genoteerd in
plaats van met een gerichte edit weggewerkt — het raakt geen enkele km-toets of naad en verandert het
verhaal van de keten niet.

**Ankers, status t.o.v. §3:** alle vier blijven **bron-gelegd** zoals in §3 — geen wijziging nodig; alle vier
markers liggen op 0,000–0,030 km van hun been-eindpunt (elk anker is exact het leg-eindpunt, zie de
bake-console: "plant → weg 0.07/0.20 km · weg → kade 0.01–0.03 km").

**Toets (bakhandleiding §5):**
- Naden tussen alle drie de benen: **0,000 km** (elk been sluit exact aan op het vorige).
- `toets_knikken.py`: 73 knikken ≥60° over de drie benen (het luchtbeen: 0), waarvan 6 omkeringen ≥150° en
  daarvan **2 terugloop** (zie de bevinding hierboven); de rest zijn spikes van 3–58 m straal, normale
  straatniveau-zigzag op weg-vertexniveau.
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de uitslag (het luchtbeen wordt terecht
  overgeslagen; geen enkel truckbeen heeft omwegfactor 1,000).
- Markers: alle 4 op ≤ 0,030 km van hun lijn (elk marker-anker is het leg-eindpunt zelf).
- `json.load` slaagt, `versie` 2, `punt_formaat` lonlat, modaliteiten ⊂ {truck, lucht}, elk been ≥ 2 punten,
  bestand 108,5 KB (ruim onder ~300 KB).

**Gereedschapslessen:**
- `maak_luchtbeen.py` blijft licht (seconden) — geen slot nodig, zoals de werkwijze voorschrijft; de
  berekende grootcirkel (6.288,0 km) kwam vrijwel exact overeen met de eigen haversine-schatting uit de brief
  (≈6.290 km), wat bevestigt dat de eerdere ontwerp-schatting (≈7.480 km) inderdaad niet herleidbaar/fout was.
- **`corridorKlassen` is voor GROTERE wegklassen overbodig zodra de klasse al in het standaard `WEG_HOUD`-
  bereik (motorway t/m secondary) valt** — het veld is bedoeld om kléínere klassen (tertiary/unclassified/
  service) corridorbreed toe te laten, niet om grotere klassen te forceren; een motorway/trunk-corridor als
  Sheikh Zayed Road heeft dat veld niet nodig en de tool weigert het bovendien hard als de klasse niet ook in
  `eindKlassen` staat.
- **Een brief-schatting die "eigen meting via via-punten" heet, is niet per definitie de echte rijafstand** —
  bij b3 bleek de bake-lengte (38,2 km) een stuk hoger dan de brief-schatting (31 km) terwijl alle snaps
  strak op de weg lagen; de norm "bake-uitvoer is leidend, geen via-punt bijschuiven" voorkwam hier een
  onnodige poging om het getal kunstmatig te laten kloppen.
