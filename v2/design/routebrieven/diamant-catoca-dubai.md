# Routebrief (licht) · diamant — Catoca (Angola) → Luanda → Dubai (VAE)

**stroom-id:** `diamant-catoca-dubai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** ruwe diamant (rough) van de Catoca-mijn (Lunda Sul) per **truck** naar het
Sodiam/Endiama-exportkantoor in Luanda, per **truck** naar de vrachtterminal van de nieuwe
luchthaven NBJ (Bom Jesus), per **vlucht** (grootcirkel) naar de vrachtterminal van Dubai
International Airport (DXB), en per **truck** naar de Dubai Diamond Exchange (DMCC, Almas Tower) —
de Endiama/Alrosa-JV-as naar de opkomende Golf-hub.
**Welke as van het verhaal:** *Angolese rough naar Dubai-tenders* (design/diamant.md §4a) — Endiama/
Sodiam exporteert rough uitsluitend per beveiligde luchtvracht (geen zeehaven-optie voor hoogwaardige
rough); Catoca ~9 Mct/jr (~8% wereldvolume, peiljaar ~2023-2024).

## 1 · Ketenkaart
```
Catoca-mijn `dia-catoca-mijn` ──(b1 truck · EN230/EN220 via Saurimo–Malanje–Cacuso–N'dalatando ·
  ~850 km, gepubliceerd)──► Luanda, Sodiam/Endiama-kantoor `dia-luanda-sodiam`
  ──(b2 truck · nieuwe luchthaven-expresweg · ~40 km)──► NBJ-vrachtterminal `dia-nbj-vracht`
  ──(b3 lucht · grootcirkel NBJ → DXB · ~5.922 km gemeten)──► DXB-vrachtterminal `dia-dxb-vracht`
  ──(b4 truck · Airport Road/Sheikh Zayed Road · ~30 km)──► DMCC/Dubai Diamond Exchange,
  Almas Tower `dia-dmcc-almas` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Catoca-mijn → Luanda (Sodiam/Endiama) | EN230 Saurimo–Malanje, EN220 Malanje–N'dalatando–Luanda | ~850 [ontwerp]; eigen hemelsbreed-som via de 4 via-punten: 826,6 km — komt goed overeen | maak_stroombeen_weg.py | nee |
| b2 | B | truck | Luanda (Sodiam) → NBJ-vrachtterminal | nieuwe luchthaven-toegangsweg (EN230-tak/Via Expresso richting Bom Jesus) | ~40 [ontwerp/haalbaarheidstoets]; eigen hemelsbreed: 39,6 km — vrijwel exact | maak_stroombeen_weg.py | nee |
| b3 | B | lucht | NBJ-vrachtterminal → DXB-vrachtterminal | grootcirkel NBJ → DXB | gemeten grootcirkel: **5.922 km** (ontwerp noemde ~7.300 km — zie §7) | maak_luchtbeen.py | nee — doorgetrokken (§2 bakhandleiding: een vlucht is geen gat) |
| b4 | C | truck | DXB-vrachtterminal → DMCC/Dubai Diamond Exchange (Almas Tower, JLT) | Airport Road → Sheikh Zayed Road (E11) | ~30 hemelsbreed (DXB-referentiepunt → Almas Tower); reële wegafstand iets langer | maak_stroombeen_weg.py | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-catoca-mijn` | mijn / laadplek (fase A start) | Catoca-mijn (Sociedade Mineira de Catoca — Endiama 41% / Alrosa 41%, in exit / Leviev International-LLI 18%) | -9.39889, 20.30083 | [1][9] | bron-gelegd (z15 gezien: actieve open-pit kimberlietmijn met de karakteristieke ronde put, opslag-/ertsvelden en een gebouwencluster met toegangswegen direct ten noorden van de put) |
| `dia-luanda-sodiam` | overslag: kantoor/exportadministratie (fase A eind / B start) | Endiama-hoofdkantoor, Major Kanhangulo, Ingombota, Luanda (Sodiam = dochter van Endiama, eigen adres niet apart bevestigd — zie §7) | -8.81291, 13.23578 | [7][8][9] | bron-gelegd (z16 gezien: verstedelijkt zakendistrict Ingombota aan de Baía de Luanda, gebouwenblok op het OSM-registerpunt van Endiama) |
| `dia-nbj-vracht` | overslag: truck → lucht (fase B) | Vrachtterminal (TECA), Aeroporto Internacional Dr. António Agostinho Neto (NBJ), Bom Jesus, Ícolo e Bengo | -9.03350, 13.51400 | [2][10] | aannemelijk (z16 gezien: bedrijventerrein met loods + verhard platform ~600 m NNO van de passagiersterminal, los van de gate-vleugels — géén naam-tag gevonden die het specifiek als TECA bevestigt; zie §7) |
| `dia-dxb-vracht` | overslag: lucht → truck (fase B/C) | Vrachtterminal DXB (voorlopig op de officiële luchthaven-referentie — het specifieke Cargo Village/SkyCargo-terrein niet gepind, zie §7) | 25.25278, 55.36444 | [4][10] | onzeker |
| `dia-dmcc-almas` | eindpunt / beurs (fase C, stoppunt) | Dubai Diamond Exchange (DMCC), Almas Tower, Jumeirah Lakes Towers | 25.06890, 55.14120 | [3][11] | bron-gelegd (z16 gezien: de karakteristieke hoogbouw aan het meer in JLT, met het DMCC-kantorencluster eromheen) |

## 4 · Via-punten
**b1 (truck, corridorkeuze EN230/EN220):**
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Saurimo (provinciehoofdstad Lunda Sul) | -9.65893, 20.39811 | knooppunt waar de mijnweg op de EN230 aansluit [9] |
| b1 | 2 | Malanje (provinciehoofdstad) | -9.53333, 16.35000 | einde EN230, aansluiting op EN220 richting de kust [5][9] |
| b1 | 3 | Cacuso | -9.42203, 15.74067 | tussenplaats op de EN220-corridor Malanje–N'dalatando [9] |
| b1 | 4 | N'dalatando (provinciehoofdstad Cuanza Norte) | -9.29848, 14.91450 | laatste grote knoop vóór de afdaling naar Luanda [9] |

**b2/b4:** binnen dit onderzoek geen aparte corridorkeuze gevonden (nieuwe expresweg resp.
Dubai-hoofdwegennet) — de bak-agent legt 1–3 via-punten vast op de doorgaande route via de lokale
OSM-extracts (`angola`, `gcc-staten`).

## 5 · Verwerkingsknopen
Geen — deze keten bevat geen smelter/raffinaderij. `dia-luanda-sodiam` is een exportadministratie
(certificering/Kimberley Process-papieren), geen fysieke bewerking; `dia-dmcc-almas` is een
handelsbeurs (veiling/tender), geen slijperij.

## 6 · Stoppunt
De brief stopt bij de Dubai Diamond Exchange (DMCC, Almas Tower): geen bron koppelt déze specifieke
Catoca-lading aan een vervolgbestemming (Surat-slijperij, Antwerpen-tender). Het aggregaatcijfer in
`design/diamant.md` §4b (dia-dubai → dia-surat, ~24 Mct/jr) is een keten-brede optelling over alle
Dubai-rough, geen stream-specifieke bron voor Catoca — fase D vervalt.

## 7 · Open punten
- **DXB-vrachtterminal niet exact gepind.** Het luchtbeen eindigt voorlopig op de officiële
  luchthaven-referentiecoördinaat (Wikipedia); het specifieke Cargo Village/Emirates
  SkyCargo-terrein (zuidkant DXB, bij Cargo Village Road) is niet gevonden binnen het webbudget
  (Overpass onbereikbaar, Nominatim gaf geen resultaat op "dnata Cargo"/"SkyCargo"). Bake-agent:
  gerichte satellietpas + OSM `aeroway=cargo_terminal`/naam "Cargo" in het `gcc-staten`-extract.
- **NBJ-vrachtterminal (TECA) op aannemelijk-niveau** — het satellietbeeld toont een plausibel
  bedrijventerrein met loods+platform, maar geen naam-tag bevestigt specifiek "Terminal de Carga
  Aérea"; de Angola-OSM-extract bevat de nieuwe luchthaven nog nauwelijks (alleen een plaatsnode
  "Bom Jesus", geen `aeroway`-polygonen) — kaarteringsgat, geen tegenbewijs.
- **Sodiam-adres niet apart gevonden** — het Endiama-hoofdkantoor (staatsbedrijf, eigenaar van
  Sodiam) is wel bevestigd op OSM; Sodiam als aparte rechtspersoon kan elders in Ingombota zitten.
- **Eigendom Catoca in beweging:** naast Endiama (41%) en Leviev International/LLI (18%) is
  Alrosa's belang (41%) in exit-onderhandeling — een Wikipedia-samenvatting noemde zelfs al
  "Taadeen Holdings (Oman Investment Authority)" als (deel-)koper, maar dat is niet onafhankelijk
  bevestigd. Raakt de route niet direct, wel het politieke risico uit het ketenontwerp.
- **Tussenlanding NBJ→DXB:** geen bron noemt een hub — conform §2 van de bakhandleiding daarom één
  directe vlucht, die aanname staat hiermee expliciet vastgelegd.
- **Gemeten grootcirkel NBJ→DXB (5.922 km) wijkt af van de ontwerp-schatting (~7.300 km)** — de
  ontwerp-waarde was een ruwe inschatting, geen gepubliceerde routeafstand; de gemeten waarde is
  leidend voor de bake.
- **b2- en b4-via-punten** zijn niet zelf op de weg gelegd (webbudget); de bake-agent vult ze aan
  vanuit de lokale extracts.

## 8 · Bronnen
[1] Wikipedia, "Catoca diamond mine" — coördinaat -9,39889/20,30083; JV-eigendom (via MediaWiki API, 2026-09-28). https://en.wikipedia.org/wiki/Catoca_diamond_mine
[2] Wikipedia, "Dr. António Agostinho Neto International Airport" — IATA NBJ/ICAO FNBJ, coördinaat -9,04678/13,50719, Bom Jesus/Ícolo e Bengo ~40 km ZO van Luanda, ontworpen voor 130.000 t cargo/jaar, passagiersoverdracht van het oude Quatro de Fevereiro-vliegveld voltooid maart 2026. https://en.wikipedia.org/wiki/Dr._Ant%C3%B3nio_Agostinho_Neto_International_Airport
[3] Wikipedia, "Almas Tower" — coördinaat 25,0689/55,1412, 68 verdiepingen, Jumeirah Lakes Towers, huisvest DMCC + Dubai Diamond Exchange. https://en.wikipedia.org/wiki/Almas_Tower
[4] Wikipedia, "Dubai International Airport" — coördinaat 25,25278/55,36444, IATA DXB. https://en.wikipedia.org/wiki/Dubai_International_Airport
[5] Wikipedia (coordinates), "Malanje" — coördinaat -9,53333/16,35000. https://en.wikipedia.org/wiki/Malanje
[6] Ver Angola, "Endiama and Al Rosa make official acquisition of 16.4 percent of Wargan in Sociedade Mineira de Catoca" — eigendomscontext Endiama/Alrosa/LLI. https://www.verangola.net/va/en/112021/RawMaterials/28052/Endiama-and-Al-Rosa-make-official-acquisition-of-164-percent-of-Wargan-in-Sociedade-Mineira-de-Catoca.htm
[7] Wikipedia, "SODIAM" — Sociedade de Comercialização de Diamantes de Angola, Angola's nationale diamanthandelsbedrijf, eigendom van Endiama. https://en.wikipedia.org/wiki/SODIAM
[8] Wikipedia, "ENDIAMA" — Angolese staatsdiamantmaatschappij. https://en.wikipedia.org/wiki/ENDIAMA
[9] OpenStreetMap/Nominatim (ODbL) — Endiama-kantoorgebouw Major Kanhangulo, Luanda (-8,81291/13,23578); plaatsnodes Saurimo (-9,65893/20,39811), Cacuso (-9,42203/15,74067), N'dalatando (-9,29848/14,91450), Luanda-centrum (-8,82727/13,24395). https://www.openstreetmap.org
[10] rough-polished.expert, "ALROSA forced to sell its stake in Sociedade Mineira de Catoca" — exit-onderhandeling Alrosa, "friendly investors". https://rough-polished.expert/en/news/136570.html
[11] DMCC, "DMCC Unveils the new Dubai Diamond Exchange" — locatie Almas Tower, 41 veilingtafels, grootste diamanthandelsvloer ter wereld. https://dmcc.ae/latest-news/dmcc-unveils-new-dubai-diamond-exchange-largest-diamond-trading-floor-world
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16, live) — `sat-diamant-catoca-dubai-catoca-mijn.png`, `sat-diamant-catoca-dubai-nbj-vrachtterminal.png`, `sat-diamant-catoca-dubai-nbj-cargocheck.png`, `sat-diamant-catoca-dubai-luanda-endiama.png`, `sat-diamant-catoca-dubai-almas-tower.png`, `sat-diamant-catoca-dubai-dxb-cargo2.png`/`-cargo3.png` (DXB-omgeving, geen bevestigd cargo-anker — zie §7).
[13] `design/diamant.md` §3a/§4a (interne bron uit het ketenontwerp) — Catoca ~9 Mct/jr o.b.v. Kimberley Process Certification Scheme (KPCS), en "Angolese rough → Dubai-tenders" als luchtvrachtmodus.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `diamant-catoca-dubai` · **bestand:** `v2/data/stroomroute-diamant-catoca-dubai.json` (177,6 KB) ·
**recept:** `bak_diamant_catoca_dubai()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh diamant-catoca-dubai`).

**4 benen · 7.017,2 km · 9.103 punten · 5 markers**, alle DOORGETROKKEN (geen enkele stippel):

| # | fase | modaliteit | km | naad met vorig been |
|---|---|---|---|---|
| b1 | A | truck | 1.024,9 | — (start) |
| b2 | B | truck | 42,0 | 0,000 km |
| b3 | B | lucht | 5.919,1 | 0,000 km |
| b4 | C | truck | 31,2 | 0,000 km |

**Luchtbeen (§2 "Lucht" van de bakhandleiding, letterlijk gevolgd):**
- b3 NBJ → DXB: `maak_luchtbeen.py`, grootcirkel **5.919,1 km** — vrijwel identiek aan de eigen haversine-
  schatting in de brief-samenvatting (5.922 km); de ontwerp-schatting (~7.300 km) was kennelijk een ruwe
  inschatting, geen gepubliceerde routeafstand. Geen bron noemt een tussenlanding → één directe vlucht
  (aanname al vastgelegd in §7 van de brief). `toets_rechte_benen.py` slaat dit been terecht over (geen
  km-toets voor een luchtbeen: zijn km = grootcirkel per definitie).

**Stippels:** geen. Beide landbenen naar/van de luchthaven (b2, b4) zijn gewone openbare wegen boven de
"korter dan ~2 km / airside zonder openbare weg"-drempel. Geen haven-aanloop (geen zeebeen in deze keten).

**⚠️ DXB-vrachtterminal-anker VERVANGEN t.o.v. §3 van deze brief.** §3/§7 markeerden `dia-dxb-vracht` als
**onzeker** (officiële luchthaven-referentiecoördinaat 25,25278/55,36444, Cargo Village niet exact gepind).
Drie zusterbrieven van deze golf (`diamant-marange-dubai`, `diamant-mbujimayi-dubai`, `diamant-letseng-dubai`)
hebben ditzelfde DXB-vrachtcomplex al **satelliet-gelegd** (Esri z14–z18) op **25,2574524 / 55,3405972**
(Emirates SkyCargo/Cargo Village, Al Garhoud — rij vrachtloodsen direct aan de apron, met vrachttoestellen
ernaast). Conform de bakhandleiding ("bestaande ankers hergebruiken … ankers uit brieven van dezelfde
grondstof in deze golf gelden ook") is dat scherpere anker hier gebruikt voor zowel het luchtbeen-eindpunt
als b4-kop, wat het open punt van §7 oplost. De coördinaten in §3 zelf zijn ongewijzigd gelaten (dit §9 is de
enige aanpassing aan de brief).

**Toelichting per truckbeen (bevindingen §5/§6 van de bakhandleiding):**
- b1 (Catoca-mijn → Luanda/Sodiam): profiel `diamant-catoca-dubai-catoca-luanda` (extract angola).
  Eerste poging zonder `corridorKlassen` faalde met "geen wegpad tussen punt 0 en 1" — nagemeten: de
  dichtstbijzijnde `secondary`-weg bij de mijn ligt op 19,6 km, ruim voorbij `EIND_STRAAL_KM` (12 km), met
  alleen `service`/`unclassified`/`track` ertussen. Met `corridorKlassen: [tertiary, unclassified, service]`
  routeert hij door: **1.024,9 km** tegen de briefwaarde ~850 km (ontwerp) = **+20,6%, BUITEN de ±15%-norm**
  — een bevinding, niet dichtgetrokken (geen via-punt bijgeschoven om het getal te halen). Een gerichte
  WebSearch bevestigt dat de afwijking in het brief-cijfer zit, niet in de bake: de EN230 Malanje↔Saurimo
  alléén is elders gepubliceerd op **625–657 km** (AFA-wegherstelproject; adistanciaentre.com), tegen een
  hemelsbreed-afstand van ~438 km — de weg windt fors meer dan de ontwerp-schatting (~850 km voor de hele
  keten) veronderstelde. Het grootste deel van het verschil zit dus aantoonbaar in het Saurimo→Malanje-
  traject, niet in een verkeerd gerouteerd stuk.
- b2 (Luanda/Sodiam → NBJ-vrachtterminal): profiel `diamant-catoca-dubai-luanda-nbj` (extract angola), geen
  corridorkeuze gevonden (brief §4) → 2-punts profiel. Gebakken **42,0 km** tegen ~40 km gepubliceerd =
  **+4,8%** [OK].
- b4 (DXB-vrachtterminal → DMCC/Almas Tower) is een **GEDEELD BEEN, LETTERLIJK HERGEBRUIKT**: exact dezelfde
  corridor (Sheikh Zayed Road E11) en exact dezelfde twee ankers als de al gebakken `diamant-mbujimayi-dubai`-
  stroom. Diens geojson (`diamant-mbujimayi-dubai-weg-dxb-dmcc.geojson`, 31,2 km, −8,9% tegen 34 km
  gepubliceerd, binnen tolerantie) is hier rechtstreeks hergebruikt — geen herbake, geen eigen wegscan
  (bakhandleiding §2: "gedeeld been = letterlijke kopie, geen tweede versie").

**Ankers, status t.o.v. §3:** `dia-catoca-mijn`, `dia-luanda-sodiam`, `dia-dmcc-almas` blijven **bron-gelegd**
zoals in §3 · `dia-nbj-vracht` blijft **aannemelijk** (geen naam-tag bevestigt specifiek "Terminal de Carga
Aérea", zie §7) · `dia-dxb-vracht` gaat van **onzeker** naar **bron-gelegd** via het hergebruikte zuster-anker
(zie boven). `dia-dmcc-almas` (25,0689/55,1412) komt vrijwel exact overeen met het gedeelde eindpunt van het
hergebruikte b4-been (25,069063/55,141166) — geen aanpassing nodig.

**Toets (bakhandleiding §5):**
- Naden tussen alle vier de benen: **0,000 km** (elk been sluit exact aan op het vorige).
- `toets_knikken.py`: 33 knikken ≥60° over de vier benen, waarvan **2 omkeringen** (beide op hetzelfde punt bij
  N'dalatando, R ≈ 0–7 m — een echte scherpe wegbocht op een via-knoop, geen terugloop) en **0 terugloop** (de
  enige klasse die gerepareerd hoort te worden). De rest zijn kleine spikes (<120 m straal), normale
  straatniveau-zigzag.
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de uitslag (het luchtbeen wordt terecht
  overgeslagen; geen enkel truckbeen heeft omwegfactor 1,000).
- Markers: alle 5 op **0,000 km** van hun lijn (elk marker-anker is het leg-eindpunt zelf).
- `json.load` slaagt, `versie` 2, `punt_formaat` lonlat, modaliteiten ⊂ {truck, lucht}, elk been ≥ 2 punten,
  bestand 177,6 KB (ruim onder ~300 KB).

**Gereedschapslessen:**
- `maak_luchtbeen.py` blijft licht (seconden) — geen slot nodig, zoals de werkwijze voorschrijft; de
  berekende grootcirkel kwam vrijwel exact overeen met de eigen haversine-schatting uit de brief.
- **Corridorbrede kleine wegklassen zijn soms nodig vóórbij de 12 km-eindzone**, niet alleen erbinnen: bij
  Catoca lag de eerste bruikbare `secondary`-weg op 19,6 km van de mijn, buiten de standaard `EIND_STRAAL_KM`
  (12 km). `corridorKlassen: [tertiary, unclassified, service]` loste dit op zonder de anker-coördinaten of
  via-punten aan te passen — het generieke "geen wegpad"-recept uit de bakhandleiding-checklist werkte hier
  letterlijk.
- **Een gedeeld been tussen zusterbrieven uit dezelfde golf hoeft niet herbakken te worden**: de derde
  diamant-Dubai-stroom die over DXB→DMCC loopt kon de al gebakken geojson van `diamant-mbujimayi-dubai`
  hergebruiken, wat zowel een wegscan als een mogelijke inconsistentie tussen drie bijna-identieke corridors
  voorkwam.
- **Een WebSearch-check op de gepubliceerde lengte van een deeltraject kan een "buiten ±15%"-bevinding
  verklaren zonder de bake aan te passen**: hier bevestigde een gerichte zoekopdracht dat de EN230 Malanje↔
  Saurimo zelf al 625–657 km beslaat — het brief-ontwerpcijfer (~850 km totaal) was de ruwe schatting, niet
  de bake.
