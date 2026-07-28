# Routebrief · grafiet (vlokconcentraat → AAM → cel) — Balama → Vidalia → De Soto / Casa Grande (VS)

**stroom-id:** `grafiet-balama-vidalia`  ·  **geschreven:** 2026-07-28 · **omgezet naar het
mijn-tot-eindproduct-sjabloon + fase D/E:** 2026-07-29  ·  **status brief:** fase A–C in toets
(de keten staat op de bol, `?v=099`) · fase D–E concept (prospectief — de uitstroom bestaat
fysiek nog nauwelijks, zie kernfeit 4)

**Keten in één zin:** vlokconcentraat in 1-t-zakken per **truck** van de Balama-plant over de
N380/N1 naar Nacala (containerisering bij Grindrod), per **containerschip** om de Kaap (hub
Durban aannemelijk) naar de Port of New Orleans, per **rivierbarge** (belading Port Allen,
SEACOR-train) naar de Port of Vidalia op rivier-mijl 359, per **short-haul truck** de
Syrah-fabriek in; het **AAM** gaat per **long-haul truck** (EA: 45–55 ritten/maand) naar
celfabrieken — gedocumenteerd: Panasonic Energy Kansas (De Soto) voor Lucid, waarna de
**2170-cellen** naar Lucid AMP-1 in Casa Grande (AZ) gaan; de **Tesla-streng** (8 kt/j) stopt
beargumenteerd aan de fabriekspoort, omdat de leverlocatie nooit publiek is gemaakt.

*Volgens `../routebrief-werkwijze.md` (§1a: de brief loopt door tot het eindproduct). Eerste
versie 2026-07-28 uit bronnenonderzoek (4 parallelle research-agents, 2026-07-27/28): benen
1–3 uitgezocht, het uitgaande been bewust dun — er wás t/m Q2 2026 geen structurele
commerciële uitstroom. Herschreven 2026-07-29 naar het sjabloon, fase D/E toegevoegd
(webresearch 2026-07-29), benen doorlopend hernummerd b1–b8. Doel: **zelfverificatie** —
alleen §5 (openstaande punten) komt bij Lars terug.*

**Notatie (hard):** coördinaten altijd **lat, lon** met **decimale punt**; ankers op 5
decimalen, passages 2–4. Alle regels uit de eerste versie zijn bij deze omzetting
gecontroleerd op lat,lon-volgorde en op plausibiliteit tegen de werkelijke plaats: **geen
lon,lat-swaps aangetroffen** (de Tongling-klasse fout uit andere brieven komt in deze brief
niet voor). Ankers waarvan de **ligplaats nog open** staat, staan bewust op minder decimalen
(terrein-niveau) — daar wordt geen decimaal verzonnen. Elk been draagt een been-id
`grafiet-balama-vidalia-b<n>`. `aansluitingen.json` bevat nog **géén** grafiet-aansluitingen
(zie §6); ankers verwijzen daarom naar de node-ids in `data/graphite.js` waar die bestaan.

**Toets-doel (historisch, 2026-07-28):** de stroom-preview op `?v=091` tekende deze keten als
zee → overslag bij **Leeville (Bayou Lafourche)** → barge vanaf dáár → los op het
**fleeting-punt** boven de Natchez–Vidalia-brug → **spoor** naar een battery-belt-centroïde.
Deze brief weerlegt alle vier die keuzes: de overslag zee→barge ligt (in het gedocumenteerde
eindbeeld) bij **Port Allen**, de losplek is de **Port of Vidalia (mijl 359)**, en het
uitgaande been is **truck** — er bestaat geen spoor in Concordia Parish en geen spoorbrug bij
Natchez–Vidalia. *Stand 2026-07-29: die vier correcties zijn per `?v=092`–`?v=099`
doorgevoerd (§6).*

---

## 1 · Ketenkaart

```
Balama-plant ──(b1 · truck N380/N1, ~485 km)──► Nacala
 gr-mozambique                                   O1: Grindrod Cross Dock (zak → container; plek open)
  ├─ vertakking A (fase A): Pemba-variant —          + containerterminal oostoever  gr-port-nacala
  │  breakbulk, derde partijen (alternatief)         (satelliet-gelegd)
                    ──(b2 · zee, ~17.162 km; hub Durban aannemelijk)──► Port of New Orleans
                                                 O2: Durban DCT (aannemelijk; ligplaatsen open)
                                                 O3: Napoleon Ave containerterminal  gr-port-neworleans
                    ──(b3 · rivier mijl 100 → 228, modus onzeker)──► Port Allen
                                                 O4: IRMT / SEACOR AMH (kade open)
                    ──(b4 · barge mijl 228 → 359, SEACOR-train)──► Port of Vidalia (mijl 359; kade open)
                                                 O5: haven → short-haul truck
                    ──(b5 · last mile, ~1–4 km, stippel)──► Syrah Vidalia AAM-fabriek  gr-ref-vidalia
                    ──(b6 · last mile uitgaand: dock → poort → US-84)──►
  ├─ vertakking B (na b6): Tesla-streng, 8 kt/j — leverlocatie nooit publiek → STOPPUNT
  ├─ vertakking C (na b6): Panasonic-Japan-substrand (eerste Lucid-cellen) → STOPPUNT
                    ──(b7 · long-haul truck ~1.100 km, corridor n.t.b.)──► Panasonic Energy Kansas, De Soto
                    ──(b8 · modaliteit n.t.b., ~1.660 km hemelsbreed)──► Lucid AMP-1, Casa Grande — keten-eind
```

| | |
|---|---|
| **Fasen** | A Balama → Nacala · B zee → New Orleans · C aanlanding → Syrah Vidalia (AAM-fabriek) · D AAM → celfabriek (De Soto) · E cel → voertuigfabriek (Casa Grande) |
| **Benen** | 8, doorlopend genummerd (`grafiet-balama-vidalia-b1` … `-b8`) |
| **Overslagen** | 5 (Nacala · Durban [aannemelijk] · New Orleans · Port Allen · Vidalia-haven) — elk 2 ankers; **6 ligplaats-ankers staan nog open** (§5), er is er geen verzonnen |
| **Gedeelde benen** | geen |
| **Vertakkingen** | fase A: **Pemba-breakbulk** (derde-partij-klanten, ~10-kt-parcels [Z5][Z7]) — geen eigen brief · na been 6: **Tesla-streng** (offtake 8 kt/j [S9]) — beargumenteerd stoppunt, geen eigen brief · na been 6: **Panasonic-Japan-substrand** (eerste Lucid-cellen uit Japan [S14][P5]) — stoppunt (§5) |
| **Reële alternatieven** | fase A: **Porto de Pemba** (punt-type *alternatief*; aandeel wisselend — 2025 o.a. één 10-kt-parcel VS, derde partijen) · fase B/C: **praktijk t/m okt 2024 = truck** Port NOLA → Vidalia over de US-84-corridor (aandeel toen 100% [Z10]); het barge-eindbeeld is gedocumenteerd, maar de slip is pas sinds Q1 2025 in aanbouw [B4] |

## 2 · Productvormen per fase — wat beweegt er fysiek

| fase | product | vorm / verpakking | gehalte of specificatie | omzetting in de volgende stap | jaarvolume |
|---|---|---|---|---|---|
| A | vlokconcentraat | 1-t-zakken, op de site verpakt; gedekte multi-axle trucks ~37 t [M1][M9] | — (gehalte niet in de gebruikte bronnen) | zak → 20-ft-container (Grindrod Cross Dock) | EA-regime ≈ 20,5 kt/j; feitelijk 2023 / 2024 / 2025 t-m Q3: 6 / 2,1 / 0 kt [B27][Z3] |
| B | vlokconcentraat | zakken ín containers — ~85 oceaancontainers/maand bij vol bedrijf [Z3] | — | container → rivierbarge (of truck, §been 3) | idem |
| C | vlokconcentraat | containers op barge, ≤78 per train [B1] | — | vlok → gezuiverd, bolvormig, gecoat **AAM** | in ≈ 20,5 kt/j → uit 11,25 kt/j AAM [B1][B27] |
| D | AAM (natural graphite active anode material) | verpakt stukgoed per gesloten long-haul trailer; emballage niet gedocumenteerd [S1] | batterijkwaliteit; kwalificatie Tesla/Lucid loopt (vergevorderd) [P6][P8] | AAM → anode in 2170-cel | contracten: Tesla 8 kt/j [S9] · Lucid ~7 kt / 3 jaar [P3]; feitelijk t/m Q2 2026: 150 t monsters [S13] |
| E | 2170-cel | cellen, gepalletiseerd (vorm niet gedocumenteerd) | doel De Soto ± 32 GWh/j [P1] | cel → pack/voertuig (Lucid Air/Gravity [P5]) | leveringen aan Lucid vanaf "2026" [P2] |

### 2a · De productvraag — van product naar kade

De ladder (6 stappen) is **per laad-, overslag- en losplek ingevuld bij het blok van die
plek** (fase-secties hieronder), telkens inclusief wat de productvorm **uitsluit**. De twee
scherpste uitsluitingen van deze keten: **containervormig product lost niet aan een bulk-
t-dock met transportband** (de Vidalia-spanning, §overslag O5), en **een offshore-supply-pas
van 23–27 ft is geen containerhaven** (de Leeville-fout van `?v=091`). De uitsluiting is hier
telkens sterker bewijs dan de bevestiging: zij leverde de negatieve ankers.

### 2b · De overslagregel

Een overslag is **nooit één punt** en **elke drager-wissel telt** — óók zak→container
(Nacala Cross Dock) en container-transshipment deepsea→deepsea (Durban). Elke overslag
hieronder heeft twee ankers (aankomst been N, vertrek been N+1) plus de terreinstappen;
waar het tweede anker niet bekend is, staat het als **openstaand punt in §5** en is er géén
coördinaat verzonnen. **Anker ≠ routeerpunt:** het schip vaart in de geul (Napoleon Ave:
anker schoof 490 m, het routeerpunt maar 154 m — gemeten, `?v=099`).

## 3 · Kernfeiten die de vorm van de keten bepalen

1. **Twee exportkanalen in Mozambique** (Syrah zelf): **Nacala = containers**
   (Grindrod Cross Dock Facility, sinds 2018; lijnen ex-Nacala bedienen o.a. de VS)
   en **Pemba = breakbulk** (sinds maart 2022, 10-kt-parcels). Kwartaalrapporten
   prijzen "FOB Nacala/Pemba". Het **Vidalia-been is containervormig** (DOE-EA:
   ~85 oceaancontainers/maand bij vol bedrijf) → vertrek voor deze stroom = Nacala
   [M2][M4][Z1][Z3]. De 10-kt US-breakbulk ex-Pemba (2025) was voor
   dérde-partij-klanten, niet Vidalia [Z5][Z7].
2. **Het kerndocument voor de VS-kant is DOE/EA-2181** (Final EA + FONSI, april
   2022): containers arriveren in de **Port of New Orleans**, gaan in **Port
   Allen** (Baton Rouge, westoever) op een rivierbarge (≤78 containers) mee in de
   bestaande **Port Allen ↔ Memphis containerbarge-train** (SEACOR AMH), lossen in
   de **Port of Vidalia**, laatste stuk per **short-haul truck** naar de fabriek;
   uitgaand AAM per **long-haul tractor trailer** [B1][Z3].
3. **Gedocumenteerde praktijk t/m okt 2024 was truck** Port NOLA → Vidalia
   (US-84-corridor); de barge is het geplande eindbeeld zodra het havenproject van
   Vidalia klaar is (slack-water slip in aanbouw sinds Q1 2025) [Z9][Z10][B4].
4. **Volumes zijn (nog) klein**: "Graphite Shipped to Vidalia" 2023 = 6 kt, 2024 =
   2,1 kt, 2025 t/m Q3 = 0; Vidalia produceerde t/m Q2 2026 alleen
   kwalificatiemonsters (150 t YTD), Balama zelf staat op een laag pitje
   ("curtailed") en commerciële AAM-verkoop is beoogd na afronding van de
   kwalificaties in H2 2026 [B27][S13][P8]. EA-regime bij 11,25 kt/j AAM ≈ ~20,5 kt
   vlok/jaar. De flow-waarde 60 in `data/graphite.js` is een fase-3-orde [B27][S13].
5. **Uitgaand AAM gaat per long-haul truck** (EA: 45–55 ritten/maand bij vol
   bedrijf) — **er is geen spoor**: Concordia Parish heeft geen actieve lijn
   (Louisiana Midland opgeheven 1985), er is **geen spoorbrug** over de Mississippi
   tussen Baton Rouge en Vicksburg, en de Natchez Railway (oostoever) is aan geen
   enkele Syrah-bron te koppelen [S1][S3][S5][S20].
6. **Twee gecontracteerde afnemers, één gedocumenteerde leverlocatie.** Tesla
   (offtake dec 2021, 8 kt/j over 4 jaar) heeft de leverlocatie nooit publiek
   gemaakt; het leveringsdispuut (default-notice juli 2025, deadline verlengd tot
   16-03-2026 o.v.v. DOE) is in juni 2026 opgelost, finale kwalificatie loopt nog
   [S9][S11][P6][P7]. Lucid (feb 2025, ~7 kt / 3 jaar, start 2026) neemt af via
   zijn celleverancier **Panasonic** — eerst Japan, vanaf 2026 **De Soto, Kansas**,
   met de cellen daarna naar Lucids fabriek in **Arizona** [S14][P2][P3][P5].

---

# FASE A · Balama-plant → Porto de Nacala

## Been 1 · truck — Balama-plant → Porto de Nacala (containerkanaal)

**been-id:** `grafiet-balama-vidalia-b1`
**Modaliteit:** truck — 100% wegtransport (Grindrod pit-to-port-contract 2017, gedekte
multi-axle trucks ~37 t; grafiet wordt óp de site in 1-tons zakken gedaan) [M1][M6][M9][M10]
**Lengte:** gemeten 494,7 km over het OSM-wegnet (`?v=093`, +2,0% t.o.v. de ESIA-som ≈ 485);
keten-stand `?v=099`: 504 km (na de last-mile-verfijning) / gepubliceerd ~490–515 km [M9][M10]
**Net / bron geometrie:** OSM-wegcorridor (N380 → N1 → EN8/N12), incl. kleine wegklassen
binnen 12 km van plant en kade (ankerstukjes 3,8 / 2,6 → 0,39 / 0,12 km, `?v=094`)
**Stippel:** nee (het been zelf ligt op echt wegnet; het stippel-stuk van deze keten is de
zee-aanloop van b2 en de last mile b5)
**Corridor bij naam:** N380 (ex-EN242) oost via Montepuez naar Metoro, daar de N1 zuid naar
Namialo, de EN8/N12 oost naar Nacala [M1]
**Routeerpunt kop / staart:** ≈ anker — wegnet gevolgd tot 0,39 km van de plant en 0,12 km
van de kade (meting `?v=094`); max snap 0,5 km
**Toets-marge:** default (2 km passages · 100 m kop/staart)

**Pemba-variant** (breakbulk, ander kanaal): Metoro rechtdoor oost over de N1/EN106,
~250–265 km totaal [M1][M9] — zie de vertakkingsregels onderin de tabel en §4.

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Balama-plant** — bagging on-site, truckbelading (Twigg/Syrah) | laadplek | -13.31000, 38.66000 | [M1][M9][M16] | bevestigd · ankercheck 2026-07-28 doorstaan |
| 2 | — | **Balama-dorp** ligt ~9 km WZW van de plant — route start op de site, NIET door het dorp | referentie (niet aan lijn) | -13.349, 38.574 | [M1][M16] | bevestigd |
| 3 | ~5–10 | Maputo-dorp + brug 1 (wetland-bruggen) | passage | — | [M1] | aannemelijk |
| 4 | ~15–30 | Nacole en Mapupulo (brug 2 ertussen) | passage | — | [M1] | aannemelijk |
| 5 | ~50 | **Montepuez** — drie 90°-bochten dwars door het centrum; markt aan de westrand | passage | -13.125, 39.002 | [M1][M16] | bevestigd |
| 6 | ~70–90 | Namanhumbir + Nanhupo (robijnmarkten aan de N380) | passage | — | [M1] | aannemelijk |
| 7 | ~160 | **Metoro** — T-kruising N380 × N1: dé splitsing Nacala (zuid) / Pemba (oost); het eerstvolgende bevestigde punt op de gekozen tak is Ocua (punt 9) | kruising | -13.104, 39.873 | [M1][M16] | bevestigd |
| 8 | ~180–360 | Chiúre, Namapa, Nacaroa, Netia (N1 zuidwaarts) | passage | — | [M1] | aannemelijk |
| 9 | ~234 | Ocua + **Lúrio-brug** (provinciegrens Cabo Delgado/Nampula) | rivierkruising | -13.645, 39.793 | [M1][M16] | bevestigd |
| 10 | ~383 | **Namialo** — kruising N1 × EN8/N12: afslag oost naar Nacala; de N1 rechtdoor gaat naar Nampula-stad, dáár gaat de stroom NIET heen (negatief anker onderaan) | kruising | -14.923, 39.988 | [M1][M16] | bevestigd |
| 11 | ~418 | Monapo | passage | -14.916, 40.297 | [M16] | bevestigd |
| 12 | ~480 | Nacala buitenwijk-vork — linker tak direct omlaag naar de haven (vermijdt het centrum) | passage | — | [M1] | aannemelijk |
| 13 | ~480 | **Grindrod Cross Dock Facility** — zak → container (60.000 m², 3.500 TEU-yard); einde been 1 = aankomstanker overslag O1 | overslag | — | [M4][M5] | bevestigd — **coördinaat onbekend, §5** |
| 14 | ~485 | **Porto de Nacala** — containerterminal, oostoever van de baai; vertrek-anker been 2 | overslag | -14.53830, 40.66730 | [M16] + satelliet | **satelliet-gelegd** (Esri z16, 0,01°-grid, 2026-07-28) |
| 15 | — | **Nacala-a-Velha kolenterminal** (wéstoever, Vale) hoort NIET bij deze stroom (ook negatief anker onderaan) | referentie (niet aan lijn) | -14.533, 40.624 | [M16] | bevestigd |
| 16 | — | **Nacala-spoorlijn** (Moatize–Nampula–Nacala) wordt NIET gebruikt — Grindrod-contract is expliciet wegtransport; geen bron noemt spoor voor het vlok | referentie (niet aan lijn) | — | [M1][M6] | bevestigd |
| 17 | ~160→250 | *Pemba-variant:* Metoro → Pemba (N1/EN106 via Mieze; stadsroute Av. do Chai → Av. da Marginal) | passage (variant) | — | [M1] | bevestigd |
| 18 | ~250 | *Pemba-variant:* **Porto de Pemba** — breakbulk-kade (183 m, ~9 m diepte; Grindrod/CFM) | **alternatief (aandeel wisselend; 2025 o.a. één 10-kt-parcel VS, derde partijen)** | -12.96800, 40.48600 | [M16][Z1][Z5][Z7] | bevestigd |

**Opmerkingen been 1.** De mijn-coördinaat die in `data/graphite.js` stond (-13.29, 38.53)
lag **~13 km te ver west** (bij Balama-dorp); de echte site ligt op ~38.66 O (OSM:
industrieterrein, pits, Syrah's zonnepark) — doorgevoerd per `?v=093` (§6). De
haven-coördinaat (-14.54, 40.67) was een **stadscentroïde**. ⚠️ Correctie 2026-07-28
(visuele check Lars + satelliet-grid): het onderzoekspunt -14.531, 40.652 bleek óók fout —
dat is open water bij de kolen-jetty op de wéstoever (precies het terminal dat als "niet aan
lijn" in deze brief staat). De containerterminal waar de trucks aankomen ligt op de oostoever
bij de stad: **-14.53830, 40.66730** (satelliet-gelegd, Esri z16 met 0,01°-grid — de
Tongling-werkwijze). De corridor was 2024-2025 verstoord bij de **mijnpoort**
(boerenprotesten, stilstand dec 2024 → medio juni 2025), niet op de weg; de Cabo
Delgado-insurgentie raakte deze route niet aantoonbaar [M14].

**Negatieve ankers been 1:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Nampula-stad | -15.12, 39.27 | 10 km | de N1 rechtdoor voorbij Namialo leidt naar Nampula; de stroom slaat bij Namialo (punt 10) af naar de EN8/N12 oost [M1][M16] |
| Nacala-a-Velha kolenterminal (westoever, Vale) | -14.533, 40.624 | 2 km | kolen-jetty, geen containers (= punt 15); het verworpen onderzoekspunt -14.531, 40.652 lag hier vlakbij in het water [M16] + satelliet |

### Productvraag · laadplek Balama-plant (been 1, punt 1)

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | vlokconcentraat in 1-t-zakken (bagging on-site) [M1][M9] |
| 2 | Soort faciliteit | bagging-installatie + gedekte truckbelading op het fabrieksterrein — geen bulk-verlading |
| 3 | Partijen op deze plek | Twigg Graphite Mining/Syrah (site); Grindrod (pit-to-port-wegcontract 2017) [M6] |
| 4 | Welke hoort bij déze stroom | Grindrod — contract is expliciet wegtransport [M1][M6] |
| 5 | Welke plek op het terrein | laadplek op de plant aan de toegangsweg; route start op de site, niet in Balama-dorp [M1][M16] |
| 6 | Coördinaat + satelliet | -13.31000, 38.66000 — ankercheck 2026-07-28 (z16-stitch) doorstaan; zichtbaar: industrieterrein, pits, zonnepark [M16] |

**Wat de productvorm uitsluit:** bulk-kippers (het product zit in zakken), de Nacala-spoorlijn
(geen aansluiting op de site, contract is weg), en een start bij Balama-dorp (9 km WZW).

## Overslag O1 (been 1 → been 2) — Nacala

**Productvraag (ladder):**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | 1-t-zakken, gestuffd in 20-ft-containers (~85 oceaancontainers/maand bij vol bedrijf) [Z3] |
| 2 | Soort faciliteit | cross-dock-loods met containeryard + containerterminal met kadekranen |
| 3 | Partijen op deze plek | Grindrod Cross Dock Facility (60.000 m², 3.500 TEU-yard, sinds 2018) [M4][M5]; containerterminal oostoever |
| 4 | Welke hoort bij déze stroom | Grindrod = Syrahs logistieke keten [M4][M6]; de terminal-operator staat niet in de gebruikte bronnen |
| 5 | Welke kade | Cross Dock: exacte plek onbekend (§5) · terminal: oostoever bij de stad |
| 6 | Coördinaat + satelliet | terminal -14.53830, 40.66730 **satelliet-gelegd** (z16, 2026-07-28); Cross Dock: géén coördinaat — niet verzonnen |

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 1 | Grindrod Cross Dock — truck-los, zak → container | losplek | — | [M4][M5] | bevestigd — coördinaat open (§5) |
| 2 | terrein | containeryard (3.500 TEU) + voordracht naar de terminal | verwerkingsstap | — | [M4] | bevestigd |
| 3 | vertrek been 2 | containerterminal oostoever — ligplaats zeeschip | laadplek | -14.53830, 40.66730 | [M16] + satelliet | **satelliet-gelegd** |

**Routeerpunt ≠ anker.** Het zeeschip vaart in de baai-geul; MARNET reikt hier niet — de
eerste ~122 km zee-aanloop is een **gestippelde haven-aanloop** (MARNET-knopen dun bij
Mozambique, geen AIS-tracks) en per werkwijze §7 de **eindvorm**, geen tussenstand.

**Wat de productvorm uitsluit:** de kolen-jetty op de westoever (Vale — bulk), de
breakbulk-kade (dat is het Pemba-kanaal), spoor.

---

# FASE B · zee — Nacala → Port of New Orleans

## Been 2 · zee — Nacala → Port of New Orleans (router)

**been-id:** `grafiet-balama-vidalia-b2`
**Modaliteit:** containerschip  ·  **Router:** zee = vrij geroutet (werkwijze §6) — in de
brief alleen kade→kade + sanity-ankers
**Lengte:** gemeten ~17.162 km (`?v=099`; incl. de zeeschip-opvaart Southwest Pass → Napoleon
Ave, 191,1 km — die rivierkilometers horen bij het zeebeen, §7)
**Stippel:** alleen de eerste ~122 km (haven-aanloop Nacala, geen MARNET/AIS — eindvorm)
**Direct of transshipment-hub?** **Hub, aannemelijk:** geen bron toont een directe dienst
Nacala → US Gulf; de MSC-rotatie Durban–…–Nacala–Durban maakt **Durban** de
transshipment-hub van het containerbeen [Z18]. Ligplaatsen in Durban onbekend → §5.
**Routeerpunt kop / staart:** kop = eerste MARNET-knoop, ~122 km uit de kust (stippel-
aanloop, exacte knoop in de bake); staart = geroutet overslagpunt in de rivier, 154 m van het
kade-anker (gemeten `?v=099`) — max snap 0,2 km
**Toets-marge:** default; zee-sanity-ankers ruim (±25 km)

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Nacala containerterminal** (vertrek, oostoever) | laadplek | -14.53830, 40.66730 | [M16] + satelliet | **satelliet-gelegd** |
| 2 | — | **Durban** — transshipment-hub van het containerbeen (MSC-rotatie Durban–…–Nacala–Durban); eigen overslag-blok hieronder | overslag | -29.87, 31.02 | [Z18] | aannemelijk |
| 3 | ~2.500 | **Kaap de Goede Hoop / Agulhas-ronding** — vanaf Durban per definitie om de Kaap, NIET Suez | passage | -34.83, 20.0 | [Z18] | aannemelijk |
| 4 | — | **Golf-toegang: Yucatánkanaal óf Straat Florida** — hangt af van de rederijrotatie; ONS `wp-florida` IS EEN GOK | passage | — | [Z-analyse] | onzeker (§5) |
| 5 | mijl −20 | **Southwest Pass** — jetty-einde; dé deep-draft-aanloop (50 ft Ship Channel sinds 2022) | passage | 28.91, -89.43 | [Z13][Z14] | bevestigd |
| 6 | mijl 0 | Head of Passes (referentie rivier-mijl 0 AHP) | referentie (niet aan lijn) | 29.15, -89.25 | [Z13] | bevestigd |
| 7 | ±mijl 100 | **Port of New Orleans — Napoleon Avenue Container Terminal** (enige containerterminal; 45 ft) — de containerkade met de portaalkranen aan de rivier; aankomstanker overslag O3 | losplek / eindpunt zeebeen | 29.91230, -90.11200 | [Z19][B25] + satelliet z16 | **satelliet-gelegd** |

**Negatieve ankers been 2** — mét coördinaat + verbodsstraal (nieuw t.o.v. de eerste versie;
de verboden zelf stonden er al):

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Suezkanaal | 30.45, 32.35 | 500 km | vanaf Durban per definitie om de Kaap [Z18 + routelogica] |
| South Pass (delta) | 28.99, -89.14 | 8 km | de deep-draft-aanloop is de Southwest Pass; de verklikker ving live dat MARNET via South Pass binnenkwam → gefixt met een SWP-via-punt (`?v=092`: South Pass-venster 0 · SWP 67 punten) [Z13] |
| Pass a Loutre (delta) | 29.17, -89.03 | 8 km | idem — geen aanloop [Z13] |
| Leeville / Belle Pass (Bayou Lafourche) | 29.25, -90.21 | 15 km | Belle Pass is 23–27 ft, gebouwd voor offshore-supplyvaart naar Port Fourchon; daar komt geen containerschip voor NOLA doorheen. Precies waar `?v=091` de overslag tekende — een graaf-raakpunt, geen haven [Z15] |

## Overslag O2 (onderweg, been 2) — Durban (aannemelijk)

**Productvraag (ladder):**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | zeecontainers (transshipment deepsea ↔ deepsea) |
| 2 | Soort faciliteit | containerterminal |
| 3 | Partijen op deze plek | Durban Container Terminal (operator Transnet) |
| 4 | Welke hoort bij déze stroom | MSC — de rotatie Durban–…–Nacala–Durban eindigt/keert bij Durban en maakt de hub aannemelijk [Z18] |
| 5 | Welke kade | onbekend — geen bron noemt de DCT-ligplaatsen voor deze rotatie |
| 6 | Coördinaat + satelliet | géén — beide ankers open (§5), geen coördinaat verzonnen; havenpunt -29.87, 31.02 is een haven-centroïde, geen anker |

**Wat de productvorm uitsluit:** bulk-/autoterminals; een direct-call Nacala → US Gulf is in
geen bron aangetroffen.

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst (ex Nacala) | DCT — ligplaats onbekend | losplek | — | [Z18] | onzeker (§5) |
| 2 | terrein | containeryard-transshipment | verwerkingsstap | — | [Z18] | aannemelijk |
| 3 | vertrek (naar US Gulf) | DCT — ligplaats onbekend | laadplek | — | [Z18] | onzeker (§5) |

## Overslag O3 (been 2 → been 3) — New Orleans, Napoleon Avenue

**Productvraag (ladder):**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | zeecontainers met 1-t-zakken vlok |
| 2 | Soort faciliteit | containerterminal met portaalkranen aan de rivier |
| 3 | Partijen op deze plek | Port of New Orleans — **Napoleon Avenue Container Terminal is de enige containerterminal** (45 ft) [Z19][B25] |
| 4 | Welke hoort bij déze stroom | idem — alle containers voor NOLA komen hier binnen |
| 5 | Welke kade | de containerkade aan de rivier, ±mijl 100 |
| 6 | Coördinaat + satelliet | 29.91230, -90.11200 — **satelliet-gelegd** (z16, 2026-07-28); de eerdere kandidaat 29.9165, -90.1105 lag 489 m landinwaarts vóór het rangeerterrein |

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 2 | Napoleon Ave — ligplaats zeeschip | losplek | 29.91230, -90.11200 | [B25][B26] + satelliet z16 | **satelliet-gelegd** |
| 2 | terrein | containeryard | verwerkingsstap | — | [Z19] | bevestigd |
| 3 | vertrek been 3 | shuttle-barge-ligplaats óf truckgate — **onbekend** (modus been 3 is niet hard) | laadplek | — | [B15][Z10] | **open (§5)** — de eerste versie had hier maar één anker; het tweede is niet verzonnen |

**Routeerpunt ≠ anker.** Het geroutete overslagpunt ligt in de geul, 154 m van het kade-anker;
de overslagmarker ligt 56 m van het geroutete punt (gemeten, `?v=099`).

**Wat de productvorm uitsluit:** een stadscentroïde is geen kade (0 van 510.752 AIS-tracks
kwam binnen 0,5 km van het oude punt); bulkterminals; Leeville/Belle Pass (offshore-supply).

---

# FASE C · aanlanding → Syrah Vidalia (AAM-fabriek)

## Been 3 · rivier — Napoleon Ave → Port Allen (IRMT), modus onzeker

**been-id:** `grafiet-balama-vidalia-b3`
**Modaliteit:** containerbarge (COB-shuttle NOLA ↔ Baton Rouge bestaat [B15]) — **de modus
NOLA → Port Allen is niet hard: truck is niet uitgesloten** (zelfde corridor); praktijk t/m
okt 2024 was sowieso truck de hele weg [Z10] → openstaand punt §5
**Brief-gestuurd** (werkwijze §6) · **km-kolom = officiële USACE-rivier-mijlen (AHP)**
**Lengte:** mijl ±100 → 228,4 ≈ 207 km; samen met been 4 gemeten 404 km over echte
AIS-tracks (`?v=099`)
**Stippel:** nee (echte tracks)
**Routeerpunt kop / staart:** kop = geul bij Napoleon Ave (snap 154 m, zie O3); staart =
**nog te bepalen** (IRMT-ligplaats open)
**Toets-marge:** default (2 km passages); kop/staart-marge pas toetsbaar als de
IRMT-ligplaats vaststaat

| # | mijl | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | ±100 | **Napoleon Avenue Container Terminal** — vertrek rivierbeen (zie overslag O3) | laadplek | 29.91230, -90.11200 | [B25][B26] + satelliet z16 | **satelliet-gelegd** |
| 2 | 102,8 | Carrollton-gage (New Orleans) | referentie | 29.945, -90.135 | [B7] | bevestigd |
| 3 | 121,6 | Hale Boggs Memorial Bridge (Luling–Destrehan) | passage | 29.937, -90.377 | [B22] | bevestigd |
| 4 | 138,7 | Reserve | passage | 30.052, -90.552 | [B8] | bevestigd |
| 5 | ±160,8 | Gramercy — Veterans Memorial Bridge | passage | 30.058, -90.698 | [B-afgeleid] | aannemelijk |
| 6 | 173,6 | Donaldsonville | passage | 30.101, -90.985 | [B9] | bevestigd |
| 7 | ±208,5 | Plaquemine | passage | 30.288, -91.233 | [B28] | aannemelijk |
| 8 | 228,3–228,4 | **Port Allen Lock** + Baton Rouge-gage — afslag GIWW; de ENIGE sluis in de keten (GIWW-zijde, niet de rivier) | kruising / sluis | 30.4415, -91.2075 | [B10][B12] | bevestigd |
| 9 | — | **IRMT Port Allen** — losplek been 3 = beladingspunt been 4 (container-op-barge); GIWW-kanaalzijde direct west van de Port Allen Lock | overslag | 30.432, -91.222 | [B13][B14] | terminal bevestigd, **kade nog niet (§5)** |

**Negatieve ankers been 3** (gelden ook voor been 4):

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Atchafalaya bij Krotz Springs | 30.54, -91.75 | 20 km | géén Atchafalaya-kortsluiting — de barge blijft op de mainstem [B18][B19] |
| Atchafalaya-monding, Morgan City | 29.70, -91.21 | 25 km | idem — de Atchafalaya is geen route van deze keten [B18][B19] |

**Verboden zonder plaats-anker (feiten, geen punt):** géén sluis op de Mississippi-mainstem
(vrijstromend tot boven St. Louis) [B20][B21] · géén zeeschepen boven mijl 232,4 [B16] · het
grafiet reist als **containers**, geen bulktransload [B1] · de fabriek ligt NIET aan de
rivier [B1].

## Overslag O4 (been 3 → been 4) — Port Allen, Inland Rivers Marine Terminal

*De productvraag is hier gesteld nadat het punt bij de anker-check als "onbepaald" zakte
(de ligplaats was op de tegels niet aan te wijzen): wie doet dit product hier, en waar?*

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | zeecontainers op een rivierbarge (container-op-barge), ≤78 per train [B1] |
| 2 | Soort faciliteit | barge-terminal met containeryard aan een bargekanaal |
| 3 | Partijen op deze plek | **SEACOR AMH**, gevestigd op de **Inland Rivers Marine Terminal** van de Port of Greater Baton Rouge: 84 acre aan een bargekanaal langs de GIWW bij de kruising met de Mississippi, **bargekade van 200 ft**, containeryard van 9 acre, ro/ro-ramp, spooraansluiting [B13][B14] |
| 4 | Welke hoort bij déze stroom | SEACOR AMH — de barge-train Port Allen ↔ Memphis rijdt er al; EA-2181 wijst dit beladingspunt aan [B1][B14] |
| 5 | Welke kade | **de terminal staat vast, de meter kade niet** — de port-eigen pagina geeft geen adres of coördinaat |
| 6 | Coördinaat + satelliet | 30.432, -91.222 (terrein-niveau). Het punt ligt bínnen de bbox van de AIS-track-graaf [29.4, -92.2, 32.2, -89.4] → volgende stap is het **dok-bewijs uit trackuiteinden** (dezelfde toets die bij de Syrah-kade 55 eindigende tracks vond), níet een nieuwe z16-ronde. Tot die er is: **open ligplaats** op de bol (`v2/data/ankercheck.json`) |

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 3 | IRMT — kade (shuttle-barge of truckgate) | losplek | 30.432, -91.222 | [B13][B14] | terminal bevestigd, kade open (§5) |
| 2 | terrein | containeryard 9 acre + ro/ro-ramp | verwerkingsstap | — | [B13] | bevestigd |
| 3 | vertrek been 4 | IRMT — bargekade 200 ft (SEACOR-train) | laadplek | 30.432, -91.222 | [B13][B14] | terminal bevestigd, kade open (§5) |

**Wat de productvorm uitsluit:** deepsea-kades (boven mijl 232,4 komt geen zeeschip [B16]);
de graanelevators van Baton Rouge (bulk).

## Been 4 · barge — Port Allen (IRMT) → Port of Vidalia (rivier-mijl 359)

**been-id:** `grafiet-balama-vidalia-b4`
**Modaliteit:** containerbarge in de bestaande **SEACOR AMH-train Port Allen ↔ Memphis** [B1][B13][B14]
**Brief-gestuurd** · **km-kolom = officiële USACE-rivier-mijlen (AHP)**
**Lengte:** mijl 228,4 → 359 ≈ 210 km (met been 3 samen gemeten 404 km, `?v=099`)
**Stippel:** nee (echte tracks)
**Routeerpunt kop / staart:** kop = **nog te bepalen** (IRMT-ligplaats open); staart =
rivier-routeerpunt bij mijl 359, snap ~0,40 km (meting `hecht_marnet`: Vidalia 177,5 → 0,400 km)
**Toets-marge:** default; staart pas op 100 m toetsbaar als de kade vaststaat

| # | mijl | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | — | **IRMT Port Allen** — vertrek barge-train (zie overslag O4) | laadplek | 30.432, -91.222 | [B13][B14] | terminal bevestigd, kade open |
| 2 | 228,3–228,4 | **Port Allen Lock** — terug de rivier op (zelfde, enige sluis) | sluis | 30.4415, -91.2075 | [B10][B12] | bevestigd |
| 3 | 232,4 | Deep-draft-grens (einde 50-ft Ship Channel; daarboven 12-ft duwvaart) | referentie | 30.46, -91.19 | [B16][B17] | bevestigd |
| 4 | ±265,5 | St. Francisville / Bayou Sara | passage | 30.776, -91.375 | [B28] | aannemelijk |
| 5 | 302,4 | Red River Landing | referentie | 30.96, -91.66 | [B11] | bevestigd |
| 6 | 304 | **Old River Lock** — ingang zijkanaal Atchafalaya/Red; wordt GEPASSEERD, niet geschut | passage | 31.077, -91.668 | [B18] | bevestigd |
| 7 | 311–319 | Old River Control-complex (rechteroever) | passage | 31.076, -91.599 | [B19] | bevestigd |
| 8 | **359** | **Port of Vidalia** — gedocumenteerde losplek (cargo ramp + t-dock; slack-water slip 31.53788, -91.48535 in aanbouw sinds Q1 2025) | losplek | 31.538, -91.485 | [B1][B3][B4] | haven bevestigd, **kade nog niet (§5)** |
| 9 | ±363–364 | **Terral RiverService-fleeting** (ex-Vidalia Dock & Storage), boven de brug — het punt waar onze AIS-toets en `?v=091` eindigden; barge-activiteit reëel, maar NIET de gedocumenteerde Syrah-losplek | referentie (niet aan lijn) | 31.568, -91.416 | [B23][B24] | aannemelijk |
| 10 | ±363 | Natchez–Vidalia Bridge / Natchez-gage 363,3 — ligt BOVEN de losplek (mijl 359): de gedocumenteerde route passeert de brug niet, alleen de (afgewezen) fleeting-variant komt erlangs | referentie (niet aan lijn) | 31.559, -91.413 | [B28] | bevestigd |

## Overslag O5 (been 4 → been 5) — Port of Vidalia, mijl 359

*Ook hier is de productvraag gesteld nadat de ligplaats op de tegels niet aan te wijzen was.*

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | containers van de barge |
| 2 | Soort faciliteit | container-/ro-ro-afhandeling (kraan of ramp) |
| 3 | Partijen op deze plek | **Port of Vidalia**: aan LA-131, ~2,5 mijl ten zuiden van de stad, mijl 359 AHP, vaardiepte 12 ft, 75 acre binnen een industriepark van 275 acre. De **bestaande** eerste fase is een **cargo ramp voor aggregaat** plus een **t-dock met transportband voor droge bulk** [B1][B3] |
| 4 | Welke hoort bij déze stroom | de haven zelf; EA-2181 wijst hem aan als losplek [B1] |
| 5 | Welke kade | ⚠️ **Dat is een spanning die de productvraag zichtbaar maakt, geen detail:** deze stroom is containervormig [B1], en een t-dock met transportband voor droge bulk lost geen containers. Ofwel de containers gaan over de cargo ramp/ro-ro, ofwel de werkelijke losplek is een andere kade aan die oever (de slip in aanbouw [B4]). Dat is een vraag aan de brief, niet aan de satelliet |
| 6 | Coördinaat + satelliet | 31.538, -91.485 (haven-niveau) — kade open; binnen de AIS-bbox → **dok-bewijs uit trackuiteinden** (§5); tot dan open ligplaats op de bol (`v2/data/ankercheck.json`) |

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 4 | Port of Vidalia — loskade (cargo ramp / ro-ro / slip) | losplek | 31.538, -91.485 | [B1][B3][B4] | haven bevestigd, kade open (§5) |
| 2 | terrein | laydown/omslag containers → chassis | verwerkingsstap | — | [B1] | aannemelijk |
| 3 | vertrek been 5 | truckbelading haventerrein | laadplek | 31.538, -91.485 | [B1] | terrein-niveau, exacte plek open (§5) |

**Wat de productvorm uitsluit:** het t-dock met transportband (droge bulk) voor déze
containervormige stroom; het Terral-fleeting-punt boven de brug is barge-activiteit maar
niet de gedocumenteerde Syrah-losplek [B23][B24].

## Been 5 · last mile — Port of Vidalia → fabriekspoort → losplek Syrah

**been-id:** `grafiet-balama-vidalia-b5`
**Modaliteit:** short-haul truck [B1]  ·  **Stippel:** **ja — geen net** (werkwijze §7:
eindvorm; zo getekend sinds `?v=092`)
**Lengte:** EA/eerste versie ~4 km; hemelsbreed kade→fabriek 1,0 km; werkwijze §7 noemt ~1 km
— vermoedelijk is ~4 km de rijafstand vanaf de bestaande cargo ramp; meten zodra de
ligplaats vaststaat (§5)
**Routeerpunt kop / staart:** n.v.t. (geen net — eigen verbinding, gestippeld mét reden)

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | Port of Vidalia — truckbelading (zie overslag O5) | losplek/laadplek | 31.538, -91.485 | [B1][B3] | kade open (§5) |
| 2 | — | LA-131 (havenuitrit → noord) | passage | — | [B1] | aannemelijk |
| 3 | — | fabriekspoort — omgeving D.A. Biglane Rd × LA-131 (exact punt: z16-pass, §5) | poort | — | [B1] | aannemelijk |
| 4 | ~1–4 | **Syrah-fabriek Vidalia** — losplek op het terrein; de fabriek ligt ~4 km landinwaarts van de rivier (NW-hoek D.A. Biglane Rd × LA-131) | losplek | 31.54660, -91.48870 | [B1] | bevestigd · ankercheck 2026-07-28 doorstaan |

### Productvraag · losplek Syrah-fabriek (been 5, punt 4)

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | containers/zakken vlokconcentraat per short-haul truck |
| 2 | Soort faciliteit | fabrieks-losdock op het terrein |
| 3 | Partijen op deze plek | Syrah Technologies LLC (Syrah Resources) [B1] |
| 4 | Welke hoort bij déze stroom | de enige AAM-fabriek van Syrah in de VS |
| 5 | Welke plek | losplek op het terrein; poort aan LA-131 (exact punt: z16-pass §5) |
| 6 | Coördinaat + satelliet | 31.54660, -91.48870 — ankercheck 2026-07-28 doorstaan |

**Wat de productvorm uitsluit:** de fabriek ligt NIET aan de rivier [B1] — een losplek op de
oever is fout; spoor bestaat niet in Concordia Parish [S20].

## Verwerkingsknoop · Syrah Vidalia AAM-fabriek

| | |
|---|---|
| **anker-id** | node `gr-ref-vidalia` (`data/graphite.js`); nog géén `aansluitingen.json`-entry (§6) |
| **eigenaar van dit anker** | deze brief |
| **in** | vlokconcentraat Balama (containers) — EA-regime ≈ 20,5 kt/j; feitelijk 2023 / 2024 / 2025 t-m Q3: 6 / 2,1 / 0 kt [B1][B27] |
| **andere ingaande strengen** | geen — Vidalia draait op Balama-vlok [B1][Z3] |
| **uit** | AAM — 11,25 kt/j (EA-regime); t/m Q2 2026 alleen kwalificatiemonsters (150 t YTD) [B27][S13] |
| **uitgaande strengen** | Tesla-offtake 8 kt/j → **stoppunt** (leverlocatie nooit publiek, fase D) [S9] · Lucid via Panasonic ~7 kt / 3 jaar → **been 7–8, deze brief** [P3] · Panasonic-Japan-substrand (eerste Lucid-cellen) → stoppunt (§5) [S14][P5] |
| **verlies / bijproduct** | purificatie-reststromen — niet gedocumenteerd in de gebruikte bronnen |

---

# FASE D · AAM → celfabriek

## Been 6 · last mile uitgaand — laaddock Syrah → poort → US-84

**been-id:** `grafiet-balama-vidalia-b6`
**Modaliteit:** long-haul tractor trailer, gesloten; 45–55 ritten/maand bij vol bedrijf [S1]
**Stippel:** terreindeel ja (eigen verbinding); vanaf LA-131 openbaar wegnet
**Routeerpunt kop / staart:** kop = laaddock — **nog te bepalen** (z16-pass §5); staart =
aansluiting US-84 in Vidalia — **nog te bepalen**

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Syrah-fabriek Vidalia** — AAM-laaddock (vertrek uitgaand been) | laadplek | 31.54660, -91.48870 | [S1] | bevestigd (dock zelf open, §5) |
| 2 | — | fabriekspoort → LA-131 | poort | — | [B1] | aannemelijk |
| 3 | ~3 | aansluiting US-84 (Vidalia) — de enige uitvalsweg west; de brug oost is Natchez (MS) en deze streng kruist de Mississippi niet | kruising | — | [P9-wegennet] | aannemelijk |

### Productvraag · laadplek AAM uitgaand (been 6, punt 1)

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | AAM — gezuiverd, bolvormig, gecoat grafietpoeder; emballage niet gedocumenteerd (verpakt stukgoed) |
| 2 | Soort faciliteit | docklaad voor gesloten long-haul trailers, 45–55 ritten/maand bij vol bedrijf [S1] |
| 3 | Partijen op deze plek | Syrah Technologies (zelfde terrein als been 5) |
| 4 | Welke hoort bij déze stroom | idem |
| 5 | Welke plek | exact laaddock onbekend — z16-pass (§5) |
| 6 | Coördinaat + satelliet | 31.54660, -91.48870 (terrein-niveau); geen satellietpass op het dock |

**Wat de productvorm uitsluit:** bulk (kipper/silowagen is in geen bron genoemd), spoor
(bestaat niet [S3][S5][S20]), barge uitgaand (geen bron — de EA zegt truck [S1]). Containers
alleen voor de export-substrand (Japan).

## Vertakking na been 6 · de Tesla-streng — beargumenteerd stoppunt

- **Contract:** dec 2021 (ASX), 8 kt/j over 4 jaar — op papier de grootste afnemer [S9].
- **Verloop:** eerste default-notice juli 2025 (niet-conforme monsters); deadlines meermaals
  verlengd, laatst tot 16-03-2026 (o.v.v. het DOE); **juni 2026 opgelost** — Tesla accepteert
  dat Syrah conforme AAM-monsters produceert en trekt de beëindiging in; de finale
  kwalificatie loopt nog en blijft een beëindigingsgrond [S11][P6][P7].
- **Wat gezocht is en niet gevonden (2026-07-27/28 + 2026-07-29):** een leverlocatie. Geen
  ASX-melding, geen EA-/DOE-stuk en geen persbericht noemt wáár Tesla het AAM afneemt.
  Kandidaten uit de cellenfabriek-logica: Gigafactory Nevada (2170, met Panasonic),
  Gigafactory Texas (4680), Fremont/Kato Rd (4680-pilot, CA) — alle drie zonder bron voor
  déze stroom.
- **Daarom stopt de Tesla-streng aan de fabriekspoort van Vidalia** (werkwijze §1a: het
  stoppunt wordt beargumenteerd, niet stilzwijgend gekozen). Geen lijn tekenen; de
  kandidaten hieronder zijn referenties, geen ankers.

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | Tesla Gigafactory Nevada (Sparks) — mogelijke Tesla-leverlocatie | referentie (niet aan lijn) | 39.540, -119.439 | [S9] | onzeker |
| 2 | Tesla Gigafactory Texas (Austin) — mogelijke Tesla-leverlocatie | referentie (niet aan lijn) | 30.222, -97.619 | [S9] | onzeker |

*Substrand Panasonic-Japan (vertakking C):* de eerste Lucid-cellen komen uit
Panasonic-fabrieken in Japan [S14][P5]; áls Vidalia-AAM daarheen gaat is dat een tweede
export-substrand (containers, haven en fabriek onbekend) — geen bron → stoppunt + §5.

## Been 7 · long-haul truck — Vidalia → Panasonic Energy Kansas (De Soto)

**been-id:** `grafiet-balama-vidalia-b7`
**Modaliteit:** long-haul truck (EA: 45–55 ritten/maand bij vol bedrijf) [S1]; **direct of
via een hub?** — direct FTL aannemelijk (dedicated ladingen), een LTL-hub is nergens
gedocumenteerd en niet uitgesloten → §5
**Lengte:** ~1.100 km over de weg (eerste versie); hemelsbreed ≈ 880 km
**Stippel:** n.v.t. — dit been wordt pas getekend bij fysieke stroom (§7)
**Corridor bij naam:** **nog te bepalen** — geen bron documenteert de route; plausibele
varianten via US-65 noord (Tallulah–Pine Bluff) dan wel I-20/I-30/I-40/I-49; de streng
blijft op de westoever van de Mississippi (geen brug nodig)
**Routeerpunt kop / staart:** nog te bepalen
**Toets-marge:** dekkings-/verklikkertoets pas mogelijk ná corridorkeuze (§5)

**Status van de stroom:** prospectief — leveringen aan Lucid("s celleveranciers") verwacht
vanaf jan 2026, o.v.v. kwalificatie; commerciële AAM-verkoop beoogd na kwalificatie H2 2026;
t/m Q2 2026 alleen monsters [P3][P8][S13].

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Syrah-fabriek Vidalia** — vertrek (zie been 6) | laadplek | 31.54660, -91.48870 | [S1] | bevestigd |
| 2 | ~10 | **Ferriday** — US-84 west uit Vidalia, kruising US-84 × US-65/US-425: dé uitvalsweg west | kruising | 31.63, -91.55 | [P9-wegennet] | aannemelijk |
| 3 | — | corridor Ferriday → regio Kansas City: **nog te bepalen** (geen bron) | passage | — | — | onzeker (§5) |
| 4 | ~1.100 | **Panasonic Energy Kansas** — De Soto, Astra Enterprise Park (ex-Sunflower Army Ammunition Plant), 10301 Astra Parkway; losdock onbekend | losplek | 38.93815, -95.00240 | [P2][P9][P11] | **bevestigd** (OSM + adres) — géén z16-pass (§5) |

**Negatieve ankers been 7** (beide punten komen uit de eerste versie; straal nieuw):

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Jackson (MS) | 32.30, -90.19 | 25 km | het spoorpad door Jackson was een artefact van onze eigen router — de echte CN-lijn buigt er NW (Yazoo Sub) en maakt geen kop; maar deze stroom rijdt daar überhaupt niet: uitgaand is truck en blijft op de westoever [S16] |
| Battery-belt-centroïde TN/KY | 36.50, -86.60 | 150 km | géén gecontracteerde afnemer zit daar; Novonix Chattanooga is een concurrent, geen afnemer; `?v=091` tekende hierheen een spoorbeen dat niet bestaat [S9][S14] |

### Productvraag · losplek Panasonic De Soto (been 7, punt 4)

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | AAM, verpakt stukgoed per gesloten trailer |
| 2 | Soort faciliteit | inbound materiaal-docks van een li-ion-celfabriek (2170) |
| 3 | Partijen op deze plek | **Panasonic Energy Kansas**: 4,7 mln sq ft, massaproductie 2170-cellen sinds 14-07-2025, doel ±32 GWh/j; klanten bij de opening: Lucid, Toyota, Harbinger, Tesla; gebouwd om "batteries to Tesla" te leveren [P1][P2][P11][P12] |
| 4 | Welke hoort bij déze stroom | het Syrah–Lucid-contract levert aan "Lucid en/of zijn celleveranciers" = Panasonic; Panasonic levert Lucid vanaf 2026 uit De Soto [P2][P3][P4] |
| 5 | Welke plek | fabriekspolygoon bekend (OSM-works, bbox 38.93574–38.94048 / -95.00418 – -94.99667); wélk dock: onbekend (§5) |
| 6 | Coördinaat + satelliet | 38.93815, -95.00240 (OSM-centroïde van het fabrieksgebouw) — **geen satellietpass gedaan** (§5); de benadering uit de eerste versie (38.96, -94.97, adres-niveau De Soto-stad) lag ~3,4 km te ver NO |

**Wat de productvorm uitsluit:** geen haven- of spooraanvoer voor AAM gedocumenteerd
(aanvoer per truck aannemelijk conform de EA-uitgaande modus); geen bulk-installaties.

## Verwerkingsknoop · Panasonic Energy Kansas (De Soto)

| | |
|---|---|
| **anker-id** | geen — kandidaat `gr-fab-desoto` (nog niet in projectdata; §6) |
| **eigenaar van dit anker** | deze brief |
| **in** | AAM van Syrah Vidalia (Lucid-contract, ~7 kt / 3 jaar vanaf 2026) [P3] · anodemateriaal van andere leveranciers — niet gedocumenteerd welke (samenvloeiing in de knoop) |
| **andere ingaande strengen** | kathode-/elektrolyt-/foliestromen buiten scope van deze brief |
| **uit** | 2170-cellen, doel ±32 GWh/j [P1] |
| **uitgaande strengen** | **Lucid → AMP-1 Casa Grande (been 8, deze brief)** [P2] · Tesla (hoofdklant van de fabriek — eigen streng, niet deze brief) [P11][P12] · Toyota, Harbinger (genoemd bij de opening) [P2] |
| **verlies / bijproduct** | — (niet gedocumenteerd) |
| **let op** | zodra ook ander anodemateriaal binnenkomt is binnen de knoop niet te scheiden welke cel Syrah-grafiet draagt — de streng volgt het contractuele pad naar Lucid |

---

# FASE E · cel → voertuigfabriek

## Been 8 · modaliteit n.t.b. — De Soto → Lucid AMP-1, Casa Grande (AZ)

**been-id:** `grafiet-balama-vidalia-b8`
**Modaliteit:** **nog te bepalen** — truck aannemelijk, intermodaal spoor niet uitgesloten;
geen bron noemt de vervoerswijze (§5). Gedocumenteerd is de relatie zelf: Panasonic levert
Lucid vanaf 2026 uit De Soto, "batteries to ship to their factory in Arizona" [P2][P5]
**Lengte:** hemelsbreed ≈ 1.660 km; wegcorridor **nog te bepalen**
**Routeerpunt kop / staart:** nog te bepalen
**Toets-marge:** pas na corridorkeuze

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Panasonic Energy Kansas** — cel-uitslag (dock onbekend) | laadplek | 38.93815, -95.00240 | [P2][P9] | bevestigd — dock open (§5) |
| 2 | — | corridor: **nog te bepalen** (geen bron) | passage | — | — | onzeker (§5) |
| 3 | ~1.900 (indicatief) | **Lucid AMP-1** — Casa Grande (AZ), 317 W Selma Highway; voertuig- en packfabriek (Lucid Air/Gravity) | losplek (keten-eind) | 32.85685, -111.77844 | [P5][P9][P10] | **bevestigd** (OSM + AZ Commerce) — géén z16-pass (§5) |

### Productvraag · laadplek cel-uitslag Panasonic De Soto (been 8, punt 1)

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | 2170-cellen, gepalletiseerd (vorm niet gedocumenteerd) — §2 fase E |
| 2 | Soort faciliteit | uitgaand verzenddock voor gepalletiseerd stukgoed; het docktype is niet verder te versmallen zolang de modaliteit open is (truck aannemelijk, intermodaal spoor niet uitgesloten — §5.15) |
| 3 | Partijen op deze plek | Panasonic Energy Kansas — dezelfde faciliteit als de losplek (been 7, punt 4) [P1][P2] |
| 4 | Welke hoort bij déze stroom | Panasonic levert Lucid vanaf 2026 uit De Soto — "batteries to ship to their factory in Arizona" [P2][P5] |
| 5 | Welke plek | fabriekspolygoon bekend (zie been 7, punt 4); wélk uitslag-dock: onbekend (§5.12) |
| 6 | Coördinaat + satelliet | 38.93815, -95.00240 (OSM-centroïde, terrein-niveau) — **geen satellietpass gedaan** (§5.12) |

**Wat de productvorm uitsluit:** bulk-verlading (cellen zijn verpakt stukgoed) en een haven
(binnenland). Meer valt er zonder gedocumenteerde modaliteit niet uit te sluiten — de
modaliteitsvraag zelf is §5.15.

### Productvraag · losplek Lucid AMP-1 (been 8, punt 3)

| stap | vraag | antwoord |
|---|---|---|
| 1 | Product, fysieke vorm | 2170-cellen, gepalletiseerd (vorm niet gedocumenteerd) |
| 2 | Soort faciliteit | inbound docks van een voertuig-/packfabriek |
| 3 | Partijen op deze plek | Lucid Motors AMP-1 (Advanced Manufacturing Plant), Casa Grande — productie Lucid Air sinds 2021, Gravity sinds 2024/25 [P5][P10] |
| 4 | Welke hoort bij déze stroom | Lucid gebruikt Panasonic-2170-cellen (Gravity); Panasonic levert vanaf 2026 uit De Soto [P2][P5] |
| 5 | Welke plek | 317 W Selma Highway; wélk dock: onbekend (§5) |
| 6 | Coördinaat + satelliet | 32.85685, -111.77844 (OSM-works-centroïde) — **geen satellietpass gedaan** (§5) |

**Wat de productvorm uitsluit:** geen haven (binnenland); bulk n.v.t.

**Waar de keten eindigt, en waarom daar.** Bij **Lucid AMP-1 Casa Grande**: daar gaat de cel
de pack en het voertuig in — het voertuig is het eindproduct en gaat als zodanig de markt op;
er is geen gedocumenteerde vaste volgende locatie meer (distributie/dealers = markt, geen
anker). De **Tesla-streng** stopt eerder, aan de fabriekspoort van Vidalia, omdat geen enkele
bron de leverlocatie noemt — dat stoppunt is een bevinding, geen gat in het zoekwerk (zie de
vertakking in fase D). Een markt-centroïde zoals `gr-mkt-us` is expliciet een centroïde en
dus géén anker.

---

## 4 · Samenvloeiingen en vertakkingen (overzicht)

| # | been | soort | met welke brief | wat gedeeld wordt | eigenaar anker |
|---|---|---|---|---|---|
| 1 | 1 | vertakking (Pemba-variant, breakbulk derde partijen) | geen eigen brief | N380-corridor t/m Metoro + de variantpunten 17–18 | deze brief |
| 2 | na 6 | vertakking (Tesla-streng, 8 kt/j) — **stoppunt** | geen eigen brief (geen gedocumenteerde bestemming) | benen 1–6 volledig + laadplek b6 | deze brief |
| 3 | na 6 | vertakking (Panasonic-Japan-substrand, eerste Lucid-cellen) — **stoppunt** | geen eigen brief | benen 1–6 | deze brief |
| 4 | 7 | samenvloeiing ín de knoop De Soto (ander anodemateriaal, leveranciers onbekend) | — | alleen de verwerkingsknoop, geen been | deze brief |

**Regel:** één brief = één streng. Zodra de Tesla-leverlocatie of de Japan-haven ooit
gedocumenteerd raakt, wordt die vertakking een eigen brief met een eigen `stroom-id`; tot
die tijd zijn het stoppunten in deze brief.

## 5 · Openstaande punten

| # | been | wat | waarom onzeker | wat het zou oplossen |
|---|---|---|---|---|
| 1 | 1/O1 | coördinaat Grindrod Cross Dock Facility (aankomstanker overslag O1) | bron noemt terminal + oppervlak, geen plek; niet verzonnen | OSM/haventekening of z16-pass Nacala-havengebied |
| 2 | 2/O2 | Durban-transshipment: terminal + beide ligplaatsen | rotatie [Z18] maakt de hub aannemelijk, maar geen bron noemt DCT-ligplaatsen | MSC-vaarschema of AIS-call-bewijs van een werkelijke rotatie |
| 3 | 2 | Golf-toegang: Yucatánkanaal óf Straat Florida (`wp-florida` is een gok) | hangt af van de rederijrotatie [Z-analyse] | AIS-track van een werkelijke Nacala/Durban → NOLA-aanloop |
| 4 | O3 | vertrek-anker been 3 in New Orleans (shuttle-barge-ligplaats of truckgate) | de eerste versie had één anker; modus been 3 niet hard | bevestiging modus (punt 5) + terminalinfo Port NOLA |
| 5 | 3 | modus NOLA → Port Allen: COB-shuttle of truck | EA beschrijft het eindbeeld; shuttle bestaat [B15], praktijk was truck [Z10] | Syrah-/SEACOR-uitspraak of waarneming (AIS/foto) van een werkelijke verplaatsing |
| 6 | 3–4/O4 | meter kade IRMT Port Allen | port-pagina geeft geen adres/coördinaat | **dok-bewijs uit AIS-trackuiteinden** (punt ligt binnen de track-bbox) — geen nieuwe z16-ronde |
| 7 | 4/O5 | wélke kade in de Port of Vidalia lost containers (cargo ramp/ro-ro vs t-dock-bulk-spanning; slip in aanbouw) | productvorm sluit het t-dock uit; geen bron wijst de kade aan | dok-bewijs uit trackuiteinden + voortgang havenproject [B4] |
| 8 | 5 | lengte + poortpunt last mile (EA ~4 km vs ~1 km hemelsbreed) | rijafstand hangt af van welke kade; poort niet gelegd | meting over de echte weg zodra de kade vaststaat; z16-pass poort |
| 9 | 6 | exact AAM-laaddock + aansluitpunt US-84 | terrein-niveau bekend, dock niet | z16-pass fabrieksterrein |
| 10 | 7 | wegcorridor Vidalia → De Soto (US-65/I-20/I-30/I-40/I-49-varianten) | geen bron documenteert de route; alleen Ferriday is als uitvalsweg hard te maken | vrachtdocumentatie, vergunningen of carrier-informatie; daarna routeerpunten + marges invullen |
| 11 | 7 | direct FTL of via een LTL-hub | EA noemt alleen "long-haul tractor trailer" [S1] | carrier-/contractinformatie |
| 12 | 7–8 | Panasonic De Soto: losdock (b7) én cel-uitslagdock (b8) + z16-pass (nieuw anker, nu OSM-centroïde) | research 2026-07-29; hoogstens "bevestigd" — satellietpass (Esri z16) moet nog; ook het vertrek-dock van been 8 is niet aangewezen | z16-pass De Soto (beide docks aanwijzen) |
| 13 | D | Tesla-leverlocatie (8 kt/j-offtake) | nooit publiek gemaakt; kandidaten NV/TX/CA zonder bron | elke bron die de leverlocatie noemt (contract, DOE-stuk, vrachtdata) — heft het stoppunt op |
| 14 | D | Panasonic-Japan-substrand: haven + fabriek | "Japan, later De Soto" [S14][P5] — verder niets | Syrah-/Panasonic-bron over de eerste leveringsbestemming |
| 15 | 8 | modaliteit + corridor De Soto → Casa Grande; AMP-1-dock + z16-pass (nieuw anker) | relatie gedocumenteerd [P2], vervoerswijze niet; satellietpass moet nog | bron over de celtransporten; z16-pass AMP-1 |

## 6 · Conflicten met de projectdata (afwerklijst)

| # | wat | was (2026-07-28) | hoort te zijn | bron | stand 2026-07-29 |
|---|---|---|---|---|---|
| 1 | `gr-mozambique` (mijn) | -13.29, 38.53 (bij het dorp) | **-13.31000, 38.66000** (de plant) | [M16] | doorgevoerd (`?v=093`) |
| 2 | `gr-port-nacala` | -14.54, 40.67 (stadscentroïde) | **-14.53830, 40.66730** (containerterminal oostoever, satelliet-gelegd; het onderzoekspunt -14.531, 40.652 lag in het water bij de west-jetty) | [M16] + satelliet | doorgevoerd (`?v=094`) |
| 3 | `gr-port-neworleans` | 29.95, -90.07 (stadscentroïde; bekende M28-vondst) | **29.91230, -90.11200** (Napoleon Ave, containerkade — satelliet-gelegd 2026-07-28; de eerste correctie naar 29.9165, -90.1105 lag nog 489 m landinwaarts vóór het rangeerterrein) | [B25] + satelliet z16 | doorgevoerd (`?v=099`) |
| 4 | `gr-ref-vidalia` | 31.57, -91.42 (fleeting-punt/stad) | **31.54660, -91.48870** (fabriek) | [B1] | doorgevoerd (`?v=092`) |
| 5 | flow `gr-mozambique → gr-ref-vidalia`, note "per barge vanuit New Orleans" | barge vanaf NOLA | barge wordt in **Port Allen** beladen; praktijk t/m 2024 was truck | [B1][Z10] | doorgevoerd (`?v=092`) |
| 6 | flow `gr-ref-vidalia → gr-mkt-us` | mode **rail**, 45 kt/j, naar TN/KY | mode **road**, prospectief; gedocumenteerde bestemming nu: De Soto (KS); Tesla onbekend | [S1][S9][S14][P2][P3] | doorgevoerd (`?v=092`: road, spoorbeen weg); bestemming actualiseren zodra fase D getekend wordt |
| 7 | flow-waarde Balama→Vidalia 60 kt/j | 60 | EA-regime ≈ **20,5 kt/j** (fase 1); feitelijk 2023–2025: 6 / 2,1 / 0 kt | [B27][Z3] | doorgevoerd (`?v=092`, volumes EA-regime) |
| 8 | via-keten `wp-florida` in graphite.js | Straat Florida als feit | **onzeker** (Yucatán even plausibel) | [Z-analyse] | **open** (§5.3) |
| 9 | stroom-preview `?v=091`: overslag Leeville · barge vanaf zee-raakpunt · eind op fleeting-punt · spoorbeen | — | overslag **NOLA (zeeschip-eind)** en **Port Allen (barge-belading)** · los **mijl 359** · last-mile truck · **géén spoorbeen** | deze brief | doorgevoerd (`?v=092`–`?v=099`) |
| 10 | `aansluitingen.json` | bevat géén grafiet-aansluitingen | entries voor Nacala-terminal, Napoleon Ave, IRMT, Vidalia-kade, Syrah-fabriek (en later De Soto/AMP-1) zodra de ligplaatsen vaststaan | deze brief | open |
| 11 | fase-D/E-ankers in projectdata | bestaan niet (`gr-mkt-us` = markt-centroïde) | De Soto **38.93815, -95.00240** en AMP-1 **32.85685, -111.77844** als echte bestemmingsankers zodra fase D/E getekend wordt; de eerste-versie-benadering De Soto 38.96, -94.97 lag ~3,4 km te ver NO | [P9] | open (pas tekenen bij fysieke stroom, §7) |

## 7 · Wat de kaart moet tekenen

1. **Zeebeen** (zeeschip): Nacala-kade → Southwest Pass → Napoleon Ave — óók het
   stuk rivier tot mijl 100: dat vaart het zééschip (50-ft channel), dus die
   kilometers horen bij het blauwe been, niet bij de barge. De eerste ~122 km bij
   Nacala gestippeld (haven-aanloop, geen net — eindvorm).
2. **Barge-been**: Napoleon Ave → Port Allen (IRMT-marker) → Port of Vidalia
   (mijl 359). Modus-nuance NOLA→Port Allen in de noot.
3. **Last mile** (short-haul truck): kade → fabriek, gestippeld — "eigen
   verbinding", geen net.
4. **Géén spoorbeen.** Het uitgaande been (truck, prospectief) voorlopig niet
   tekenen; desgewenst later dun/gestippeld naar **De Soto KS** (enige
   gedocumenteerde bestemming — eerst corridor bepalen, §5.10) — maar niet naar
   TN/KY, en **geen Tesla-lijn** (stoppunt).
5. Mozambique-kant: het truckbeen Balama→Nacala is een landcorridor over echte
   N380/N1-geometrie (staat er sinds `?v=093`; truck = amber).
6. **Fase E** (De Soto → Casa Grande): pas tekenen bij fysieke celleveringen
   (vanaf 2026 [P2]) en na corridorkeuze; tot dan alleen de verwerkingsknoop
   De Soto als bestemmingsanker in de fase-D-nota.
7. Keten-stand `?v=099`: 18.070 km (truck 504 · zee 17.162 · barge 404 · last
   mile); de fase-D/E-benen komen daar te zijner tijd bovenop.

## 8 · Toets-checklist (invullen bij de controle)

- [ ] **Notatie:** alle coördinaten lat, lon met decimale punt; ankers op 5 decimalen
      (open ligplaatsen bewust op terrein-precisie, §notatie)
- [ ] Elk been heeft een **been-id**; ankers dragen het `data/graphite.js`-id waar dat
      bestaat (`aansluitingen.json`-entries: §6.10)
- [ ] Elke laadplek, overslag en losplek heeft status **satelliet-gelegd** (z16) — door de
      maker zelf gelegd; nieuwe fase-D/E-ankers nog niet (§5.12/§5.15)
- [ ] Elke laad-/los-/overslagplek heeft een ingevulde **productvraag** (§2a), inclusief de
      uitsluitingen
- [ ] Elke overslag (óók transshipment) heeft **twee** ankers + de terreinstappen ertussen —
      open ankers staan in §5, er is er geen verzonnen
- [ ] **Routeerpunt + max snap** genoteerd bij elk been-uiteinde op water; "nog te bepalen"
      waar de ligplaats open is
- [ ] **Dekking:** de gerouteerde lijn raakt alle *bevestigde* punten in volgorde
      (default-marge 2 km passages / 100 m kop en staart; afwijkingen per been-kop)
- [ ] **Verklikker:** geen enkele plaats geraakt die niet in de brief staat
- [ ] Geen enkel **negatief anker** binnen zijn verbodsstraal geraakt
- [ ] Lengte per been binnen de tolerantie t.o.v. de gepubliceerde waarde — mét gereedschap,
      beide eindpunten en netstadium (b1: 494,7 km · `maak_stroombeen_weg.py` · plant→kade ·
      `?v=093`-net)
- [ ] Volumes sluiten aan over de verwerkingsknopen heen (§2: 20,5 kt vlok → 11,25 kt AAM →
      contracten 8 + ~2,3 kt/j)
- [ ] Elke stippellijn draagt een **reden**; elk reëel **alternatief** heeft een aandeel of
      een openstaand punt
- [ ] De keten loopt door tot het eindproduct (AMP-1) — de stoppunten (Tesla, Japan) zijn
      beargumenteerd (fase D/E)

## 9 · Bronnen

**Mozambique [M..]:** M1 ESIA Balama Traffic & Transport Assessment (CES/EOH 2014,
via DFC) · M2 Syrah "Sales, Marketing and Logistics" · M4 Grindrod persbericht
Cross Dock · M5 Freight News Cross Dock · M6 Mining Review Grindrod-contract 2017 ·
M9 NS Energy Balama · M10 Mining Technology Balama · M14 Ecofin hervatting na
protesten · M16 OSM/Overpass (ODbL, 2026-07-28). *(Volledige lijst: research-run
wf_5829e3b8, journal.)*

**Zee [Z..]:** Z1 Africa Outlook (twee kanalen) · Z3 DOE/EA-2181 · Z5 Syrah
breakbulk-VS · Z7 Syrah Q3-2025 · Z9 nola.com 2018 · Z10 nola.com okt 2024 ·
Z13 Port NOLA 50-ft Ship Channel · Z14 Waterways Journal 2022 · Z15 Greater
Lafourche Port Commission · Z18 MSC Mozambique-rotatie · Z19 Port NOLA terminals.

**Barge [B..]:** B1 DOE/EA-2181 §2.2 · B3 Town of Vidalia (Port, mijl 359) ·
B4 LA Site Selection (slip-coördinaat) · B7–B11 USACE rivergages (mijlen) ·
B12 USACE GIWW Port Allen-route · B13 Port of Greater Baton Rouge IRMT ·
B14 The Advocate IRMT/SEACOR · B15 10/12 Industry Report COB-shuttle ·
B16 LA Maritime Assoc (RM 232,4) · B18 USACE Old River Lock · B19 Old River
Control · B20/B21 locks alleen boven St. Louis · B22 Hale Boggs Bridge ·
B23/B24 Terral-fleeting Vidalia · B25/B26 Port NOLA terminals/mijlen ·
B27 Syrah Q2-2026 · B28 Rivergator.

**Uitgaand [S..]:** S1 DOE/EA-2181 (truck, 45–55/mnd) · S3 Natchez–Vidalia Bridge ·
S5 Natchez Railway (NTZR) · S9 Syrah-Tesla offtake (ASX dec 2021) · S11 electrive
Tesla-dispuut opgelost (zie ook P6) · S13 Syrah Q2-2026 (150 t YTD) · S14 electrive
Syrah–Lucid/Panasonic De Soto (zie ook P4) · S16 Mississippi State Rail Plan (CN
Yazoo Sub) · S20 Louisiana Midland opgeheven 1985.

**Fase D/E — AAM-afnemers & cellen [P..] (research 2026-07-29):**
P1 Panasonic Energy persbericht 14-07-2025 "Begins Mass Production … Kansas"
(2170-massaproductie gestart; doel ±32 GWh/j) · P2 opening-verslagen De Soto
(WardsAuto · Manufacturing Dive · Kansas Reflector, juli 2025 — klanten bij de
opening: Lucid, Toyota, Harbinger, Tesla; Lucid: levering start "volgend jaar"
[2026], "batteries to ship to their factory in Arizona") · P3 Syrah ASX-melding
25-02-2025 "Vidalia AAM Supply Agreement with Lucid" (~7 kt / 3 jaar, start 2026;
leveringen verwacht vanaf jan 2026 na kwalificatie door Lucids celleveranciers;
prijs per kwartaal aan een vlok-index) · P4 electrive 25-02-2025 "Lucid orders
battery graphite from Syrah" · P5 electrive 08-01-2025 "Lucid Gravity uses 2170
cells from Panasonic" (cellen nu uit Japan; vanaf medio 2025 óók uit de VS) ·
P6 electrive 01-06-2026 "Graphite deal with Tesla: Syrah reports resolution in
delivery dispute" (default-notice juli 2025; deadline-verlengingen tot 16-03-2026
o.v.v. DOE; opgelost, finale kwalificatie blijft beëindigingsgrond) · P7 Benchmark
Source "Tesla reinstates graphite supply agreement" + Investing News "Tesla
withdraws Syrah termination notice" (tweede bron resolutie) · P8 Investing.com
"Syrah Q2 2026 slides" (Balama curtailed; commerciële AAM-verkoop na kwalificatie
H2 2026; positieve operationele kasstroom verwacht vanaf H2 2027) · P9
OSM/Nominatim-geocodering 2026-07-29 (ODbL): way 1201758396 "Panasonic EV Battery
Factory", 10301 Astra Parkway, De Soto KS 66018 → 38.93815, -95.00240; way
1254715766 "Lucid Motors", 317 W Selma Highway, Casa Grande AZ 85193 →
32.85685, -111.77844; relatie 14122951 "Astra Enterprise Park"; [P9-wegennet] =
OSM-wegnet VS · P10 Arizona Commerce Authority 28-09-2021 (productiestart Lucid
Air, AMP-1 Casa Grande) · P11 fox4kc / OLDCC ($4 mrd; Astra Enterprise Park =
ex-Sunflower Army Ammunition Plant; "supply batteries to Tesla when operational") ·
P12 desotoks.us (Astra Enterprise Park + Panasonic-facility-pagina's).

**Eigen metingen:** satelliet-overlay Esri z16 2026-07-28 (Nacala oostoever ·
Napoleon Ave) · ankercheck 2026-07-28 (Balama-plant, Nacala en Syrah-fabriek
doorstaan; Port Allen en Vidalia open — `v2/design/ankercheck-2026-07-28.json`) ·
lengte-metingen `?v=093`/`?v=094`/`?v=099` (`maak_stroombeen_weg.py` ·
`hecht_marnet route` · AIS-track-graaf) · Nominatim/Overpass-geocodering 2026-07-29
(De Soto, Casa Grande) · **géén z16-pass op de nieuwe fase-D/E-ankers** (§5.12/§5.15).
