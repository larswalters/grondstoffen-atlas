# Routebrief (licht) · diamant — Mbuji-Mayi (DR Congo) → Kinshasa → Dubai (VAE)

**stroom-id:** `diamant-mbujimayi-dubai` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** ruwe diamant van MIBA/artisanale mijnbouw bij Mbuji-Mayi (Kasaï-Oriental) gaat per truck
naar Mbuji-Mayi Airport (MJM), vliegt als binnenlandse verzamelvlucht (grootcirkel) naar N'djili (FIH) in
Kinshasa — waar de CEEC de export certificeert — vliegt door als internationale vrachtvlucht naar Dubai
International Airport (DXB), en gaat per truck naar de vrachtterminal → DMCC/Almas Tower voor handel.
**Welke as van het verhaal:** *de formele MIBA/CEEC-exportstroom via Kinshasa* — DR Congo heeft geen bevaarbare
zeehaven bij Mbuji-Mayi en is voor internationale export van gecertificeerde rough afhankelijk van luchtvracht
via Kinshasa [design/diamant.md §4a]. ⚠️ Dit is de **formele, gecertificeerde** stroom, niet het hele
DRC-volume: een deel ontsnapt aan CEEC-certificering (artisanaal/niet-geregistreerd) en dus aan elke
traceerbare route — zie §7. DR Congo (Mbuji-Mayi) levert ~9 Mct/j ruw, overwegend industrieel/laagwaardig
(~8% wereldvolume) [design/diamant.md §3a, o.b.v. KPCS].

## 1 · Ketenkaart
```
MIBA-terrein/exportkantoor, Mbuji-Mayi `dia-mbm-miba` ──(b1 truck · stadsverbinding · ~3,7 km)──►
Mbuji-Mayi Airport (MJM) `dia-mbm-mjm` ──(b2 lucht · vlucht MJM → FIH, grootcirkel, binnenlandse
   verzamelvlucht · ~919 km)──►
N'djili International Airport (FIH), Kinshasa — CEEC-certificering `dia-fih-term`
   ──(b3 lucht · vlucht FIH → DXB, grootcirkel · ~5.421 km)──►
Dubai International Airport (DXB), vrachtterminal `dia-dxb-cargo`
   ──(b4 truck · Airport Road/Sheikh Zayed Road · ~29 km hemelsbreed)──►
DMCC / Almas Tower, Dubai `dia-dmcc` ── stoppunt
```
Fase C (b4, DXB → DMCC) is toegevoegd op de haalbaarheidstoets: het ontbrekende laatste been.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | MIBA-terrein/exportkantoor → Mbuji-Mayi Airport (MJM) | Avenue Inga, korte stadsverbinding; geen doorgaande corridorkeuze | ~3,7 hemelsbreed (berekend uit ankers); ontwerp noemt ~5 km | maak_stroombeen_weg | nee |
| b2 | A | lucht | Mbuji-Mayi Airport (MJM) → N'djili (FIH), Kinshasa | vlucht MJM → FIH, grootcirkel (binnenlandse verzamelvlucht) | 919,2 (berekend, grootcirkel); ontwerp noemt ~1.070 km | maak_luchtbeen | nee — doorgetrokken |
| b3 | B | lucht | N'djili (FIH), Kinshasa → Dubai Intl (DXB) | vlucht FIH → DXB, grootcirkel | 5.421,3 (berekend, grootcirkel); ontwerp noemt ~6.700 km | maak_luchtbeen | nee — doorgetrokken |
| b4 | C | truck | DXB-vrachtterminal → DMCC/Almas Tower | Airport Road → Sheikh Zayed Road/Al Ittihad Road, binnen Dubai, geen corridorkeuze | ~29,0 hemelsbreed (berekend uit ankers) | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-mbm-miba` | mijn/laadplek (exportkantoor) | MIBA-terrein/exportkantoor, Mbuji-Mayi | -6.1300, 23.6000 | [3][9] | aannemelijk (z14 gezien: stadskern van Mbuji-Mayi met gemengde bebouwing; geen apart MIBA-omheind terrein of pit te onderscheiden op deze resolutie — géén mijnpit zichtbaar binnen budget, zie §7) |
| `dia-mbm-mjm` | vrachtterminal/vertrek luchtvracht | Mbuji-Mayi Airport (MJM), Regideso | -6.1188177, 23.5682265 | [1][9] | bron-gelegd (z14 gezien: duidelijke start-/landingsbaan met apron en gebouwen direct ten oosten van de baan, in de stad Mbuji-Mayi — OSM-aerodrome-node) |
| `dia-fih-term` | vrachtterminal/aankomst+vertrek luchtvracht | N'djili International Airport (FIH), Kinshasa | -4.3840685, 15.4508775 | [2][9] | bron-gelegd (z14 gezien: gebouwencluster en apron direct naast de start-/landingsbaan, ten zuidoosten van de rivierdelta; OSM-aerodrome-node "Aéroport International de Ndjili" — géén apart vrachtgebouw te onderscheiden op deze resolutie, zie §7) |
| `dia-dxb-cargo` | vrachtterminal/aankomst luchtvracht | Dubai Intl Airport (DXB), vrachtcomplex (Emirates SkyCargo/Cargo Village, Al Garhoud) | 25.2574524, 55.3405972 | [4][9] | bron-gelegd (z14 gezien: gebouwencomplex direct ten zuidwesten van de start-/landingsbanen, tussen stad en apron — OSM-building "الإمارات للشحن الجوي" (Emirates SkyCargo), Airport Internal Road) |
| `dia-dmcc` | handels-/beurshub (eindpunt) | DMCC / Almas Tower, Jumeirah Lake Towers, Dubai | 25.0690625, 55.1411656 | [5][9] | bron-gelegd (z15 gezien: herkenbare hoogbouwtoren in het JLT-torencluster bij de marina, matcht de bekende Almas Tower-locatie — DMCC's hoofdkantoor) |

## 4 · Via-punten
*(geen — b1 en b4 zijn beide stadsverbindingen zonder aanwijsbare corridorkeuze; b2/b3 zijn luchtbenen, geen
via-punten. De wegtool routeert zelf over het lokale net.)*

## 5 · Verwerkingsknopen
*(geen fysieke bewerkingsknoop in deze keten — Mbuji-Mayi is winning + sortering/export, N'djili/CEEC is een
certificeringsknoop (administratief, geen fysieke bewerking), DMCC is een handels-/beursgebouw. Het slijpen
(~90-95% van de wereld in Surat, India) valt buiten deze keten — zie §6.)*

## 6 · Stoppunt
De brief stopt bij DMCC/Almas Tower in Dubai: dit is het opgegeven eindpunt van de keten en precies het punt
dat de haalbaarheidstoets vraagt (truckbeen vrachtterminal → beurs/kluis). Geen bron koppelt Mbuji-Mayi-rough
aan een specifieke vervolgbestemming (bv. een slijperij in Surat) — fase D vervalt.

## 7 · Open punten
- **CEEC-locatie niet adresseerbaar binnen budget:** de CEEC (Centre d'Évaluation, d'Expertise et de
  Certification) is een technische overheidsdienst onder het Ministerie van Mijnen (decreet 09/57,
  03-12-2009) die de export van niet-ferro mineralen certificeert [7][8]; geen bron geeft een adres binnen
  N'djili Airport of elders in Kinshasa specifiek — het anker `dia-fih-term` is het luchthaventerrein, niet
  het CEEC-kantoor zelf.
- **`dia-mbm-miba` is een stadscentrum-anker, geen bevestigd MIBA-omheind terrein of exportkantoor:** géén
  mijnpit of apart bedrijfsterrein te onderscheiden op z14; status blijft aannemelijk.
- **De dubbele luchtsprong (MJM→FIH binnenlands, FIH→DXB internationaal) leunt op één zin** in
  design/diamant.md §4a en is niet apart geverifieerd binnen het webbudget (haalbaarheidstoets-risico,
  overgenomen zonder verdere bronbevestiging).
- **Grootste deel van het volume-risico:** DRC/Mbuji-Mayi is overwegend industrieel/laagwaardig en
  gedeeltelijk artisanaal (niet-geregistreerd); een deel van het jaarvolume ontsnapt aan CEEC-certificering
  en dus aan deze getekende, formele MIBA/CEEC-as.
- **km b2/b3 zijn berekende grootcirkels**, geen gepubliceerde vluchtroutelengtes (geen gekarteerd
  luchtwegennet bestaat); werkelijke vluchtroutes kunnen door omvliegen langer zijn.
- **b4 (DXB→DMCC) is hemelsbreed berekend** (29,0 km); de werkelijke wegafstand via Sheikh Zayed Road ligt
  hoger, exacte gepubliceerde km ontbreekt.
- **MIBA-specifiek vs. artisanaal aandeel binnen het DRC-jaarvolume (~9 Mct/j) niet uitgesplitst** —
  bevestigd open punt uit het ketenontwerp.

## 8 · Bronnen
[1] Wikipedia, "Mbuji-Mayi Airport". https://en.wikipedia.org/wiki/Mbuji_Mayi_Airport
[2] Wikipedia, "N'djili Airport". https://en.wikipedia.org/wiki/N%27djili_Airport
[3] Wikipedia, "Mbuji-Mayi" — MIBA, historisch centrum van industriële diamantmijnbouw, alle huidige winning
    artisanaal. https://en.wikipedia.org/wiki/Mbuji-Mayi
[4] Wikipedia / Dubai Airports, "Dubai International Airport" — Cargo Mega Terminal / Dubai Cargo Village,
    Al Garhoud, coördinaat 25°15′10″N 055°21′52″E. https://en.wikipedia.org/wiki/Dubai_International_Airport ·
    https://www.daep.gov.ae/our-airports/dubai-international-dxb/cargo-mega-terminal/
[5] Wikipedia, "Almas Tower" — DMCC-hoofdkantoor, Jumeirah Lake Towers, Dubai. https://en.wikipedia.org/wiki/Almas_Tower
[6] Kimberley Process Certification Scheme — ruwproductiestatistiek DR Congo. https://www.kimberleyprocess.com
[7] CEEC (Centre d'Évaluation, d'Expertise et de Certification) — functie/oprichtingsdecreet, exportcertificering
    niet-ferro mineralen. https://ceecertification.org/index_en.html · https://www.ceecertifications.com/origin_en.html
[8] MIBA (Société Minière de Bakwanga), officiële site. https://www.miba.cd
[9] OpenStreetMap (ODbL) via Photon — "Aéroport de Mbuji-Mayi" (aeroway=aerodrome, 23.5682265/-6.1188177);
    "Aéroport International de Ndjili" (aeroway=aerodrome, 15.4508775/-4.3840685); "الإمارات للشحن الجوي"
    (Emirates SkyCargo, building, DXB Airport Internal Road, 55.3405972/25.2574524); Almas Tower (building,
    JLT, 55.1411656/25.0690625). https://www.openstreetmap.org
[10] design/diamant.md (project-brief) §3a (jaarvolume DR Congo), §4a (luchtvracht-bron Mbuji-Mayi →
     Kinshasa → internationale export), §risico (volume-vs-waarde/artisanaal-vertekening).
[11] Global Witness — achtergrond DRC-diamantsector/traceerbaarheid. https://www.globalwitness.org

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `diamant-mbujimayi-dubai` · **bestand:** `v2/data/stroomroute-diamant-mbujimayi-dubai.json` (15,7 KB) ·
**recept:** `bak_diamant_mbujimayi_dubai()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh diamant-mbujimayi-dubai`).

**4 benen · 6.376,3 km · 736 punten · 5 markers**, alle DOORGETROKKEN (geen enkele stippel):

| # | fase | modaliteit | km | naad met vorig been |
|---|---|---|---|---|
| b1 | A | truck | 4,6 | — (start) |
| b2 | A | lucht | 919,2 | 0,000 km |
| b3 | B | lucht | 5.421,3 | 0,000 km |
| b4 | C | truck | 31,2 | 0,000 km |

**Luchtbenen (§2 "Lucht" van de bakhandleiding, letterlijk gevolgd):**
- b2 MJM → FIH: `maak_luchtbeen.py`, grootcirkel **919,2 km** — sluit vrijwel exact aan op de eigen
  haversine-schatting in de samenvatting (~919 km). Binnenlandse verzamelvlucht (geen internationale grens
  onderweg); geen tussenlanding, want geen bron noemt een hub.
- b3 FIH → DXB: `maak_luchtbeen.py`, grootcirkel **5.421,3 km** — idem exact op de eigen schatting (~5.421 km).
  Internationale vrachtvlucht; géén tussenlanding gebrond (brief §7), aangenomen als één directe vlucht.
- Beide luchtbenen hebben géén km-toets (grootcirkel = de km per definitie); `toets_rechte_benen.py` slaat ze
  terecht over.

**Stippels:** geen. Beide truckbenen (b1 MIBA→MJM, b4 DXB→DMCC) zijn gewone openbare stadswegen boven de
"korter dan ~2 km / airside zonder openbare weg"-drempel, dus geen last-mile-stippel nodig. Geen haven-aanloop
(geen zeebeen in deze keten).

**Toelichting per truckbeen (haalbaarheidstoets §5/§6 van de bakhandleiding, geen dichtgetrokken bevindingen):**
- b1 (MIBA-terrein → MJM): profiel `diamant-mbujimayi-dubai-miba-mjm` (extract congo-drc), gebakken **4,2 km**
  weggeometrie (in de stroom 4,6 km incl. anker-stukjes) tegen het ~5 km-ontwerpcijfer = **-15,7%**, net buiten de
  ±10%-toolwaarschuwing maar binnen de ±15%-norm van de brief. Er is geen betrouwbare gepubliceerde wegreferentie
  om tegen te toetsen (brief §2: "gebruik als gepubliceerdKm ~5 … omdat er geen betrouwbare wegreferentie is") —
  bevinding, niet dichtgetrokken.
- b4 (DXB-vrachtterminal → DMCC): profiel `diamant-mbujimayi-dubai-dxb-dmcc` (extract gcc-staten), gebakken
  **31,0 km** weggeometrie tegen het venstercijfer ~34 km (hemelsbreed 29,0 km + verwachte omweg) = **-8,9%** [OK].

**Ankers, status ongewijzigd t.o.v. §3:** `dia-mbm-miba` blijft **aannemelijk** (stadscentrum-anker, geen apart
MIBA-terrein te onderscheiden op z14) · `dia-fih-term` blijft het luchthaventerrein, niet het CEEC-kantoor zelf
(CEEC-locatie niet adresseerbaar binnen budget) · de overige drie ankers (`dia-mbm-mjm`, `dia-dxb-cargo`,
`dia-dmcc`) zijn **bron-gelegd**.

**Toets (bakhandleiding §5):**
- Naden tussen alle vier de benen: **0,000 km** (elk been sluit exact aan op het vorige).
- `toets_knikken.py`: 0 omkeringen, 0 terugloop over alle vier benen (18 kleine spikes <60 m straal op de
  truckbenen, normale straatniveau-zigzag, geen reparatie nodig).
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de uitslag (luchtbenen worden terecht
  overgeslagen; geen truckbeen heeft omwegfactor 1,000).
- Markers: alle 5 op **0,000 km** van hun lijn (elk marker-anker is het leg-eindpunt zelf).
- `json.load` slaagt, `versie` 2, `punt_formaat` lonlat, modaliteiten ⊂ {truck, lucht}, elk been ≥ 2 punten,
  bestand 15,7 KB (ruim onder ~300 KB).

**Gereedschapslessen:**
- Dit was de derde luchtbeen-bake van deze golf (na de twee PGM-luchtstromen) — het §2-recept
  (`maak_luchtbeen.py` → `--been-geojson "lucht|vlucht <IATA> → <IATA> (vrachtvlucht, grootcirkel)|…"`) werkte
  zonder aanpassing en de berekende grootcirkel-km kwamen vrijwel exact overeen met de eigen haversine-schatting
  uit de brief-samenvatting (919,2 vs ~919 km; 5.421,3 vs ~5.421 km) — een goede kruiscontrole voor toekomstige
  luchtbenen.
- `maak_luchtbeen.py` is inderdaad licht (milliseconden voor beide benen samen) — geen slot nodig, zoals de
  werkwijze voorschrijft.
- Beide wegprofielen liepen in één poging goed door de weg-slot-scan; geen extracts ontbraken (congo-drc en
  gcc-staten stonden al op schijf).
