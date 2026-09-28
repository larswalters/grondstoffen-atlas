# Zilver · Van → Via → Naar (land)

**stroom-id:** `zilver-uchucchacua-callao` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** lood/zink-zilverconcentraat van de Uchucchacua-mijn (Buenaventura, Oyón, Lima-regio) per
**truck** over de Andes-vallei-corridor Oyón–Churín–Sayán–Huacho–Chancay naar de mineraalterminal van
Transportadora Callao S.A. in de haven van Callao — bewust **stoppunt** bij het exportpunt, geen gedocumenteerde
overzeese smelter-bestemming binnen budget.
**Welke as van het verhaal:** Peru — primaire zilvermijn Uchucchacua naar Callao (haven). Uchucchacua produceert
≈400 t Ag/j (Buenaventura jaarverslag 2024, primair zilver + lood/zink-bijproduct; zie `v2/design/zilver-sitelaag.json`
id `w-uchucchacua` / `data/silver.js` id `ag-uchucchacua`). Prioriteit 5 van M31 golf 5.

## 1 · Ketenkaart
```
Uchucchacua-mijnkamp `ag-uchucchacua-mijn` ──(b1 truck · Oyón–Churín–Sayán–Huacho–Chancay ·
   hemelsbreed via-som 243,2 km, geen wegkm)──► Transportadora Callao-mineraalterminal `ag-callao-tcsa`
   (muelle centro, Callao-haven) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Uchucchacua-mijnkamp → Transportadora Callao-mineraalterminal | Oyón → San Juan de Churín → Sayán → Huacho → Chancay (Andes-vallei naar de kust, dan Panamericana Norte zuidwaarts) [1][2][3] | hemelsbreed 243,2 km (via-punten-som), geen wegkm [berekend; geen gepubliceerde wegkm gevonden binnen budget] | maak_stroombeen_weg (extract `peru`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-uchucchacua-mijn` | mijn / laadplek | Uchucchacua-mijnkamp (Buenaventura), Oyón, Lima-regio | -10.6335, -76.6895 | [4][8] | bron-gelegd (z17 gezien: mijnwerkerskamp met dormitory-clusters, industriële loodsen, een tailings-/afvalgebied met omgeleide toegangsweg en waterzuiveringsbekkens direct N ervan, verbonden met switchback-wegen — zie §7 voor de afwijking t.o.v. de sitelaag-centroïde) |
| `ag-callao-tcsa` | overslag / exportpunt (stoppunt) | Transportadora Callao S.A. — Terminal de Embarque de Concentrado de Minerales ("muelle centro"), Callao-haven | -12.0499, -77.1446 | [5][6][7][9] | bron-gelegd (z18 gezien: vier bulkcarriers met open laadluiken side-by-side aan een eigen kade tussen de APM-containerterminal in het noorden en de DP World-containerterminal in het zuiden — exact het "muelle centro"-patroon uit Wikipedia; geen containerkranen, wel bulk-laadgerei) |

## 4 · Via-punten (b1 — de enige landbeen, geen corridorkeuze maar bekende doorgaande-wegplaatsen)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Oyón (provinciehoofdstad) | -10.6684, -76.7702 | eerste doorgaande-wegplaats vanaf het mijnkamp, waar de mijnweg op de Carretera Huaura–Oyón–Ambo aansluit [2][3] |
| b1 | 2 | San Juan de Churín | -10.8113, -76.8750 | de weg volgt hier de Huaura-riviervallei verder omlaag; sluit een noordelijkere route via Cajatambo uit [2][3] |
| b1 | 3 | Sayán | -11.1335, -77.1934 | corridorknoop waar de vallei-weg de kustvlakte nadert, laatste punt vóór Huacho [2] |
| b1 | 4 | Huacho | -11.1085, -77.6103 | aansluiting op de Panamericana Norte (kustcorridor); hier buigt de route zuidwaarts naar Lima/Callao [2] |
| b1 | 5 | Chancay | -11.5628, -77.2700 | laatste kustplaats op de Panamericana Norte vóór de Callao-metropoolregio [2] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| — | — | — | — | geen tussenliggende verwerkingsknoop getekend: het erts wordt al op de mijn (Uchucchacua) tot lood/zink-zilverconcentraat verwerkt; geen smelter/raffinaderij in deze keten |

## 6 · Stoppunt
De brief stopt bij de Transportadora Callao-mineraalterminal: geen bron bevestigt dat Uchucchacua-concentraat
specifiek naar déze kade gaat versus een eigen Buenaventura-verwerkingsfabriek elders in Peru, en geen bron noemt
een overzeese smelter-bestemming — de haven-exportkade is daarmee het eerlijke, zij het zwakke, eindpunt
(vergelijkbaar met het Cannington-precedent, `zilver-cannington-townsville.md`).

## 7 · Open punten
- **BINDEND UIT DE HAALBAARHEIDSTOETS — onopgelost binnen budget:** geen bevestiging dat Uchucchacua-concentraat
  specifiek naar Callao/Transportadora Callao gaat versus een eigen Buenaventura-verwerkingsfabriek elders in Peru
  (Buenaventura heeft ook eigen plants, o.a. bij Julcani/Mallay). Wel een indirecte aanwijzing: Transportadora Callao
  concentreert vracht uit "Junín, Pasco, Ayacucho, Huancavelica en de noordelijke zone van Lima" [7] — Oyón ligt in
  die noordelijke Lima-zone, wat de aanname ondersteunt zonder ze te bevestigen.
- **Geen gepubliceerde wegkilometer gevonden binnen budget** — alleen de via-punten-som hemelsbreed (243,2 km);
  het ontwerp schatte zelf al 2-3× de hemelsbrede 160 km door het Andes-gebergte. De ±15%-toets geldt hier niet als
  norm, alleen als indicatie; het wegtool meet de echte wegkm bij het bakken.
- **Mijn-anker gecorrigeerd t.o.v. de sitelaag-v1-centroïde.** `w-uchucchacua` in `v2/design/zilver-sitelaag.json`
  (-10.6200,-76.9200) bleek bij een satellietblik op leeg Andes-terrein te liggen, zonder enige mijninfrastructuur
  (25 km WNW van de echte site). Het hier gebruikte anker (-10.6335,-76.6895) ligt wél op een satelliet-bevestigd
  mijnkamp (dormitories, tailings-gebied, waterzuivering). **Sitelaag zelf niet gewijzigd — alleen gemeld** (raakt
  alleen eigen bestanden, zie werkwijze).
- **Callao-anker verscherpt van generieke havencentroïde naar een specifieke terminal.** `ag-port-callao` in
  `data/silver.js` (-12.05,-77.15) is een generieke centroïde; hier vervangen door de satelliet-bevestigde
  Transportadora Callao-mineraalterminal. De exacte individuele berth binnen dat complex (er liggen 4 bulkcarrier-
  ligplaatsen naast elkaar) is niet apart gepind — één representatief punt voor het hele terminal-complex.
- **Geen fase B/C/D/E getekend** — de keten stopt bewust bij het exportpunt; er is geen bron voor een vervolgtraject.
- **Afstand tot de MARNET-zeeknoop is 60,7 km** (zeeknoop 394, -12.00000,-77.70000) — ruim boven de 5 km-drempel
  voor een haven-aanloop (bakhandleiding §2). Niet van toepassing in déze brief (geen zeebeen getekend), maar
  relevant mocht een latere fase B alsnog worden toegevoegd.

## 8 · Bronnen
[1] Ketenontwerp (workflow-invoer) — jaarvolume, van/naar-sites, oorspronkelijke corridor-aanname en risico-inschatting.
[2] OpenStreetMap (ODbL) via Nominatim — Oyón -76,7702/-10,6684 · San Juan de Churín -76,8750/-10,8113 · Sayán
    -77,1934/-11,1335 · Huacho -77,6103/-11,1085 · Chancay -77,2700/-11,5628; Churín-node draagt de straatnaam
    "Carretera Huaura - Ambo". https://www.openstreetmap.org
[3] Wikipedia (Spaans), "Provincia de Oyón" — grenst aan Huaura (zuid/west) en Pasco (oost); bevestigt de
    vallei-ligging richting de kust. https://es.wikipedia.org/wiki/Provincia_de_Oy%C3%B3n
[4] OpenStreetMap (ODbL) via Photon — plaatsnaam "Uchuc Chacua", village, Oyón, -76,6890/-10,6352 (mijnkamp-
    nabije nederzetting, niet de mijn zelf); satellietblik bevestigt mijninfrastructuur op deze locatie.
    https://www.openstreetmap.org
[5] Wikipedia (Engels), "Port of Callao" — drie terminals: North Multipurpose (APM Terminals), Terminal de
    Embarque de Concentrado de Minerales (Transportadora Callao S.A.), New Container Terminal South Zone
    (DP World Callao). https://en.wikipedia.org/wiki/Port_of_Callao
[6] Wikipedia (Spaans), "Puerto del Callao" — "muelle centro" geconcedeerd aan Consorcio Transportadora Callao;
    mineralenkade/transportband geopend mei 2014. https://es.wikipedia.org/wiki/Puerto_del_Callao
[7] PortalPortuario, "En Puerto de El Callao se construye el mayor depósito de minerales del mundo" — Transportadora
    Callao concentreert vracht uit Junín, Pasco, Ayacucho, Huancavelica en de noordelijke zone van Lima (Oyón valt
    binnen die laatste zone). https://portalportuario.cl/en-puerto-de-el-callao-se-construye-el-mayor-deposito-de-minerales-del-mundo/
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16/z17/z18, live) —
    `v2/build-cache/satcheck/sat-zilver-uchucchacua-callao-mijnkamp.png`,
    `sat-zilver-uchucchacua-callao-osmpunt.png`, `sat-zilver-uchucchacua-callao-mijn-z16.png` (mijnkamp);
    `sat-zilver-uchucchacua-callao-port-close.png`, `sat-zilver-uchucchacua-callao-muelle-centro.png`,
    `sat-zilver-uchucchacua-callao-mineralterminal.png` (Callao-terminal).
[9] Rumbo Minero, "Muelle de Minerales del Callao alcanza récord histórico con 2 mil naves atendidas" — bevestigt
    de operationele mineraalkade bij Callao (Transportadora Callao / TCSA).
    https://www.rumbominero.com/peru/noticias/economia/muelle-de-minerales-del-callao-record-historico/
[10] Energiminas, "Transportadora Callao contrata a Metso Outotec…terminal de minerales" — bevestigt naam en rol
    van Transportadora Callao als exploitant van de mineraalterminal.
    https://energiminas.com/2023/03/06/transportadora-callao-contrata-a-metso-outotec-para-desarrollar-proyectos-de-infraestructura-y-mantenimiento-en-su-terminal-de-minerales/
[11] Wikipedia (Engels/Spaans), "Compañía de Minas Buenaventura" — bevestigt Uchucchacua als zilvermijn van
    Buenaventura (Oyón); geen operationele/logistieke details op zendingsniveau (bevestigt het budget-risico uit
    het ontwerp). https://en.wikipedia.org/wiki/Compa%C3%B1%C3%ADa_de_Minas_Buenaventura
[v1] `data/silver.js` (ag-uchucchacua, ag-port-callao) en `v2/design/zilver-sitelaag.json` (w-uchucchacua) —
    v1-register en sitelaag als checklist/bronnenstartpunt (niet gewijzigd).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Eén been (b1, truck), 305,5 km, 4.788 punten, 2 markers, 102,6 KB.**

| # | modaliteit | km gemeten | naad | stippel? | recept |
|---|---|---|---|---|---|
| b1 | truck | 305,5 | 0,00 km (eerste been) | nee | `maak_stroombeen_weg.py --profiel zilver-uchucchacua-callao-mijn-tcsa --bron geofabrik` (extract `peru`) → `bak_zilver_uchucchacua_callao()` in `v2/tools/bak_stromen.sh` |

**Markers (2, uit §3 van de brief):**
- `ag-uchucchacua-mijn` — Uchucchacua-mijnkamp (Buenaventura), Oyón, Lima-regio — -10.6335, -76.6895 (snap 0,04 km op de weglijn)
- `ag-callao-tcsa` — Transportadora Callao S.A. mineraalterminal (muelle centro), Callao-haven — -12.0499, -77.1446 (snap 0,05 km)

**Km-toets (§7 van de brief, expliciet géén harde ±15%-norm):** de brief geeft alleen een hemelsbreed
via-punten-som (243,2 km) als indicatie, met de eigen waarschuwing dat het Andes-traject Oyón→Sayán
2-3× de directe hemelsbrede afstand (160 km) kan bedragen. De gemeten wegkm is **305,5 km** — een
afwijking van **+25,6%** t.o.v. de indicatie. Buiten de gebruikelijke ±15%-band, maar dit is de
**gebrieft-verwachte** uitkomst en geen bevinding in de zin van de handleiding: de brief zelf zegt dat
de ±15%-toets hier niet als norm geldt. Het gemeten getal (305,5 km) vervangt de indicatie als beste
schatting van de echte reisafstand.

**Toelichting per been:**
- b1 is volledig doorgetrokken, geen stippel. De weg volgt de Huaura-riviervallei (Oyón → San Juan de
  Churín → Sayán) en daarna de Panamericana Norte-kuststrook (Huacho → Chancay → Callao), zoals de
  brief beschrijft. Geen via-punt gaf een snap > 5 km (max. snap 0,46 km bij Chancay).
- Mijnkamp-uiteinde: `eindKlassen` verruimd met `track` + `eindToegangPrivaat: True` (kamptoegangsweg
  is deels unclassified/track tot Oyón) — de scan liep hierdoor door zonder "geen wegpad".
- Callao-uiteinde: dezelfde `eindToegangPrivaat: True` bleek ook hier nodig te zijn (containerterminal-
  achtige toegang/poortcontrole rond de mineraalterminal); zonder deze sleutel zou het laatste stukje
  binnen de afgesloten havenzone niet routeerbaar zijn geweest.
- Geen haven-aanloop en geen zeebeen: de brief tekent bewust geen fase B (geen bron voor een overzeese
  bestemming). Ter info blijft staan dat de TCSA-kade 60,7 km van de dichtstbijzijnde MARNET-zeeknoop
  ligt (ver boven de 5 km-drempel) — relevant bij een eventuele latere fase B, niet bij deze bake.
- Geen fase D/E getekend, conform brief §6 (bewust stoppunt bij het exportpunt).

**Lessen / bevindingen:**
- `toets_knikken.py`: 0 omkeringen, 0 terugloop over 50 knikken ≥ 60°, allemaal haarspeldbochten met
  kleine straal (3–80 m) — verwacht op een Andes-bergweg (switchbacks bij Oyón/Churín), geen fout.
- `toets_rechte_benen.py --min-km 5`: geen vlag voor dit been (geen verdachte omwegfactor 1,000).
- Contract-toets: `versie 2`, `punt_formaat lonlat`, modaliteit `truck` (geldig), 1 been met 4.788
  punten (≥ 2), bestandsgrootte 102,6 KB (ruim onder de norm).
- Open punt blijft staan zoals in §7 van de brief: geen bevestiging dat het Uchucchacua-concentraat
  specifiek naar Callao/Transportadora Callao gaat versus een eigen Buenaventura-verwerkingsfabriek
  elders in Peru — dit is een aanname uit het ketenontwerp, niet iets wat de bake kan toetsen.
- Mijn-anker en Callao-anker wijken af van de v1-sitelaag/-registerpunten (zie brief §7); beide
  sitelaag-/registerbestanden zelf zijn niet aangeraakt, alleen gemeld (buiten scope van deze agent).

**Registerregel (centraal, niet door deze agent):**
`{ sleutel: "uchucchacua-callao", bestand: "stroomroute-zilver-uchucchacua-callao.json", aan: true }`
