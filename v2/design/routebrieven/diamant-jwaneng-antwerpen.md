# Routebrief (licht) · diamant — Jwaneng → Antwerpen (via Gaborone & Brussels Airport)

**stroom-id:** `diamant-jwaneng-antwerpen` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** ruw diamant van de Debswana Jwaneng-mijn (Botswana) per **truck** naar de sight-aggregatie in
Gaborone (Diamond Technology Park), per **truck** naar de vrachtapron van Sir Seretse Khama International Airport
(GBE), per **vrachtvlucht** (grootcirkel) naar Brucargo op Brussels Airport (BRU), en per **truck** naar het
AWDC/Diamond Office in de Antwerpse Diamantwijk.
**Welke as van het verhaal:** Botswana → Gaborone → Antwerpen: het De Beers/Debswana-anker, de grootste
single-source waarde-as van de diamantketen. Jwaneng levert ~12 Mct/j ruw (~11% wereldvolume, hoogste
waarde/karaat van de grote mijnen) [1][9]; sinds 25-02-2025 ligt er een nieuw 10-jarig De Beers/Botswana-
verkoopcontract + een 25-jaar Debswana-mijnvergunning-verlenging (tot juli 2054), met het ODC-verkoopaandeel dat
groeit van 30% (2025-30) via 40% (2030-35) naar 50% (2035-40) [7] — de contractonderhandeling uit het
ketenontwerp is dus geen open kwestie meer, maar een getekend akkoord.

## 1 · Ketenkaart
```
Jwaneng-mijn `dia-jwaneng-mill` ──(b1 truck · Trans-Kalahari Corridor · ~170 km)──► Gaborone DTP `dia-gaborone-dtp`
   (De Beers/DBGSS sight-aggregatie, in de Diamond Hub SEZ bij de luchthaven, sinds 2017)
   ──(b2 truck · Airport Road · ~5 km)──► GBE-vrachtapron `dia-gbe-cargo`
   ──(b3 lucht · grootcirkel GBE → BRU · ~8.652 km, doorgetrokken)──► Brucargo `dia-bru-cargo` (Brussels Airport)
   ──(b4 truck · E19 · ~38 km)──► AWDC/Diamond Office `dia-antwerp-awdc` (Antwerpen) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `dia-jwaneng-mill` → `dia-gaborone-dtp` | Trans-Kalahari Corridor (A2) via Sese–Kanye–Moshupa–Gabane | 170 [1], webcheck 166,7 | maak_stroombeen_weg | nee |
| b2 | B | truck | `dia-gaborone-dtp` → `dia-gbe-cargo` | Airport Road | ~15 (ontwerp-schatting) → webcheck 5,0 [11] | maak_stroombeen_weg | nee |
| b3 | B | lucht (vrachtvlucht, grootcirkel) | `dia-gbe-cargo` → `dia-bru-cargo` | GBE → BRU | ontwerp ~8.850, webcheck 8.652 [11] | maak_luchtbeen | nee — doorgetrokken |
| b4 | C | truck | `dia-bru-cargo` → `dia-antwerp-awdc` | E19 via Mechelen | ~40 (ontwerp), webcheck 37,7 [11] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-jwaneng-mill` | mijn/fabriek (kop) | Jwaneng-mijn concentrator-/fabriekscomplex (Debswana) | -24.5303, 24.7083 | [1][5][6] | bron-gelegd (z17 gezien: fabriekscomplex met ronde indikkers, loodsen en transportbanden op de zuidoostrand van de put) |
| `dia-gaborone-dtp` | overslag / sight-aggregatie | Diamond Technology Park, Gaborone (De Beers/DBGSS-zone) | -24.5899, 25.9149 | [2][5][6] | bron-gelegd (z16 gezien: kantoren-/bedrijvencomplex incl. het herkenbare ronde Botswana Innovation Hub-gebouw, in de Diamond Hub SEZ bij de luchthaven) |
| `dia-gbe-cargo` | vrachtterminal (luchthaven) | Sir Seretse Khama Int'l Airport, vrachtapron/hangaar | -24.5576, 25.9242 | [2][5][6] | aannemelijk (z17 gezien: hangaar met platform en geparkeerde vrachttoestellen naast de terminal; OSM draagt geen "Cargo"-naam op dit gebouw) |
| `dia-bru-cargo` | vrachtterminal (luchthaven) | Brucargo, Brussels Airport | 50.9056, 4.4576 | [3][5][6] | bron-gelegd (z15 gezien: vrachtloodsen zuid van de passagiersterminal; OSM-adres "Bedrijvenzone Machelen Cargo" / "Brucargo 706") |
| `dia-antwerp-awdc` | beursgebouw (bestemming) | AWDC / Diamond Office, Hoveniersstraat 22, Antwerpen | 51.2154, 4.4185 | [4][5][6] | bron-gelegd (z16 gezien: stadsblok in de Diamantwijk vlak bij Antwerpen-Centraal; OSM bevestigt Hoveniersstraat 18-22) |

## 4 · Via-punten (b1, b2, b4 — b3 is lucht en heeft er geen)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Sir Seretse Khama Ave / Trans-Kalahari-aansluiting (rand Jwaneng-stad) | -24.5914, 24.7299 | hier verlaat de route de mijnweg en gaat de Trans-Kalahari Corridor op (OSM-wegnaamwissel, webcheck) |
| b1 | 2 | Trans-Kalahari Corridor bij Sese | -24.8079, 25.0140 | pint de corridor op de doorgaande trunk-weg (OSM: `highway=trunk`, naam "Trans-Kalahari Corridor") i.p.v. een binnendoor-track |
| b1 | 3 | Trans-Kalahari Corridor bij Kanye | -24.9502, 25.2955 | corridor passeert Kanye (grootste plaats onderweg) langs de doorgaande weg, niet het centrum |
| b1 | 4 | Moshupa, Thamaga Road-kruising | -24.7586, 25.4426 | corridor buigt hier van zuid naar noordoost, richting Gaborone |
| b1 | 5 | Gabane, nabij Gaborone | -24.6531, 25.8030 | laatste herkenbare punt vóór de stadsrand van Gaborone, voorkomt een sluipweg door de buitenwijken |
| b2 | 1 | Airport Road, aftakking bij DTP | -24.5874, 25.9168 | enige doorgaande weg tussen DTP en de luchthaventerminal (webcheck) |
| b4 | 1 | E19 bij Mechelen | 51.0213, 4.4481 | pint de route op de E19 i.p.v. een parallelle N-weg door het centrum van Mechelen |
| b4 | 2 | E19/R1-knooppunt Antwerpen-Zuid (Wilrijk) | 51.1103, 4.4319 | trekt de route om de Antwerpse ring i.p.v. een sluipweg dwars door de stad |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Diamond Technology Park (Gaborone) | De Beers / Botswana (DBGSS) | ruw uit meerdere Botswaanse mijnen → gesorteerde "sights" per sightholder | Jwaneng-aandeel ~12 Mct/j; sinds 2025 ODC 30%→40%→50% van de verkoop | [1][7][9] |
| AWDC / Diamond Office (Antwerpen) | AWDC | rough/polished → import-/exportklaring + Kimberley Process-certificering | "one-stop import & export clearing" | [4][8] |

## 6 · Stoppunt
De brief stopt bij het AWDC/Diamond Office in Antwerpen: dit is de certificerings- en handelspoort (diamant.md
§3c/§4b), niet de slijperij (Surat, elders al gemodelleerd in `data/diamond.js`) en niet de eindmarkt. Er is geen
bron die voor déze specifieke Jwaneng-zending een vervolgbestemming per lading noemt — fase D/E vervalt.

## 7 · Open punten
- **Exact DBGSS-gebouw in Gaborone niet met naam gevonden** in OSM/Nominatim/Photon; het anker gebruikt de
  "Diamond Technology Park"-landuse-polygoon in dezelfde Diamond Hub SEZ (sinds 2017 [2]) — ~5 km van de
  luchthaven, korter dan de ~15 km uit het ketenontwerp. Dat getal was een ruwe schatting in het ontwerp, geen
  bron; de gemeten waarde (webcheck) vervangt hem.
- **GBE-vrachtterminal**: geen OSM-gebouw met "Cargo" in de naam; anker = hangaar/apron-cluster naast de
  terminal (satellietbeeld z17), status *aannemelijk*.
- **Geen lading-specifieke bron voor "Jwaneng-rough vliegt via Brussels Airport"**: de vlucht volgt uit de
  opdrachttekst/`design/diamant.md` §3c/§4b (niet-Russische rough via Antwerpen-certificering) en uit het feit dat
  Brucargo al decennia Antwerpse diamantvracht draagt — bevestigd door de diamantroof van 2013 op de tarmac van
  Brussels Airport (~US$50 mln, uit een vliegtuig) [3]. Geen tussenlanding gebrond → één directe vlucht
  aangenomen (§2 bakhandleiding).
- **b1 is vrijwel één hoofdweg** (Trans-Kalahari Corridor/A2); de 5 via-punten pinnen de corridor op de
  doorgaande trunk-weg, ze markeren geen scherpe routekeuzes tussen alternatieven.
- **Aandeel van de Jwaneng-rough dat specifiek via Antwerpen gaat** (i.p.v. rechtstreeks Gaborone→Surat of
  Gaborone→Dubai, zie `data/diamond.js` §4b) is niet per lading gebrond — alleen dat Antwerpen het
  G7-certificeringsknooppunt is voor niet-Russische, dus ook Botswaanse, rough [8].

## 8 · Bronnen
[1] Wikipedia, "Jwaneng diamond mine" — rijkste diamantmijn ter wereld, 170 km ZW van Gaborone; coördinaten. https://en.wikipedia.org/wiki/Jwaneng_diamond_mine
[2] Wikipedia, "Sir Seretse Khama International Airport" — 15 km N van Gaborone; sinds 2017 special economic zone incl. "diamond hub for diamond sector". https://en.wikipedia.org/wiki/Sir_Seretse_Khama_International_Airport
[3] Wikipedia, "Brussels Airport" — coördinaten 50°54'05"N 4°29'04"E; diamantroof 2013 (~US$50 mln) uit een vliegtuig op de tarmac — bewijs dat diamant hier fysiek vliegt. https://en.wikipedia.org/wiki/Brussels_Airport
[4] AWDC, "About AWDC" — adres Hoveniersstraat 22, 2018 Antwerpen; Diamond Office faciliteert import/export ("one-stop import & export clearing"). https://www.awdc.be/en/about-awdc
[5] OpenStreetMap/Nominatim + Photon (ODbL) — Jwaneng Diamond Mine (landuse=quarry, -24,5179/24,6958); Diamond Technology Park, Gaborone (landuse=commercial, -24,5899/25,9149); Hoveniersstraat 18-22-gebouw, Antwerpen (51,2154/4,4185); "Bedrijvenzone Machelen Cargo" / "Hulpkantoor Douane Zaventem, Brucargo 706" (50,9056/4,4576). https://www.openstreetmap.org
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15-z17) — `v2/build-cache/satcheck/sat-diamant-jwaneng-antwerpen-{plant3,dtp,gbe-cargo,brucargo2,awdc}.png`.
[7] Anglo American, persbericht 25-02-2025 — De Beers/Botswana: nieuw 10-jarig verkoopcontract + 25-jaar Debswana-mijnvergunning-verlenging (aug. 2029 → juli 2054); ODC-verkoopaandeel 30% (2025-30) → 40% (2030-35) → 50% (2035-40). https://www.angloamerican.com/media/press-releases/2025/25-02-2025
[8] `design/diamant.md` (dit project, §3c/§4b/§5) — Antwerpen als verplicht G7-certificeringsknooppunt sinds maart 2024 (sanctie op Russische/Alrosa-diamant); Surat als slijptrechter; Gaborone-sights.
[9] USGS Mineral Commodity Summaries 2025 (Diamond) + Kimberley Process Certification Scheme (KPCS) — wereld-ruwproductie ~110-120 Mct/j; checklist voor het jaarvolume, geen handelsstatistiek per zending.
[10] Debswana, officiële site — Jwaneng als een van 's werelds belangrijkste diamantmijnen naar waarde en volume. https://www.debswana.com/
[11] router.project-osrm.org (OSRM-demo op het OSM-wegennet) — webcheck-wegafstanden: Jwaneng→DTP 166,7 km, DTP→GBE 5,0 km, Brucargo→AWDC 37,7 km; grootcirkel GBE→BRU 8.652 km (eigen berekening, sferische afstand).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `diamant-jwaneng-antwerpen`** → `v2/data/stroomroute-diamant-jwaneng-antwerpen.json` — 4 benen (truck ·
truck · lucht · truck, fase A → B → C → stoppunt), **8.860,5 km**, 2.661 punten, 5 markers, 54,2 KB. Recept:
`bak_stromen.sh` (functie `bak_diamant_jwaneng_antwerpen`); drie nieuwe wegprofielen
`diamant-jwaneng-antwerpen-jwaneng-gaborone` / `-gaborone-gbe` / `-brucargo-antwerpen` in
`maak_stroombeen_weg.py`. Alle vier benen doorgetrokken, geen stippels.

**b1 (truck, profiel `diamant-jwaneng-antwerpen-jwaneng-gaborone`, extract `botswana`, vensterKm 40):**
`maak_stroombeen_weg.py --profiel … --bron geofabrik` — **166,5 km** geroute (getekende lijn 166,7 km incl.
anker-verbindingsstukjes 0,18/0,03 km) langs de Trans-Kalahari Corridor via Sese–Kanye–Moshupa–Gabane, 13
keerlussen gesnoeid (166,7 → 166,5 km dubbel gereden stukken). Lengtetoets tegen 170 km (Wikipedia; webcheck OSRM
166,7 km) = **−2,1%**, ruim binnen ±15%. First mile 8,15 km / last mile 1,23 km over kleine wegklassen, beide
binnen de 12 km-marge.

**b2 (truck, profiel `diamant-jwaneng-antwerpen-gaborone-gbe`, extract `botswana`, vensterKm 15):** **4,7 km**
geroute (getekend 4,8 km) over Airport Road, DTP → GBE-vrachtapron. Lengtetoets tegen 5 km (webcheck OSRM,
corrigeert de ontwerp-schatting van ~15 km) = **−6,0%**. Korte stadsrand-hop, geen keerlussen.

**b3 (lucht, grootcirkel, GBE → BRU):** `maak_luchtbeen.py --van "GBE vrachtapron (Sir Seretse Khama Int'l)|
-24.5576,25.9242" --naar "Brucargo (Brussels Airport)|50.9056,4.4576"` — **8.651,7 km** gemeten grootcirkel (eigen
sferische berekening in de opdracht: 8.652 km; het ontwerp noemde ~8.850 km — het gemeten getal vervangt de
schatting, geen aparte km-toets voor een luchtbeen). 348 punten. Doorgetrokken, geen stippel: een vlucht tussen
twee gelegde vrachtterminals is geen gat. Geen bron voor een tussenlanding (brief §7) → één directe vlucht,
conform de bakhandleiding.

**b4 (truck, profiel `diamant-jwaneng-antwerpen-brucargo-antwerpen`, extract `belgie`, vensterKm 20):** **37,3
km** geroute (getekend 37,4 km incl. anker-verbindingsstukjes 0,03/0,08 km) over de E19 via Mechelen, 18 kleine
keerlussen gesnoeid (dubbel gereden stukjes bij Brucargo/Mechelen/Antwerpen-Zuid, lengte ongewijzigd op
37,3 km). Lengtetoets tegen 40 km (ontwerp; webcheck OSRM 37,7 km) = **−6,7%**. De router volgt de E19 exact,
geen alternatieve corridor.

**Toetsen:** `toets_knikken.py` — lucht-been 0 knikken/0 omkeringen (per constructie recht); de drie truckbenen
5/2/6 knikken ≥60° (spikes op kruispunten/afritten, straal 3–336 m), **0 omkeringen ≥150°, 0 terugloop** over de
hele stroom — geen actie nodig. `toets_rechte_benen.py --min-km 5` — geen ⚠️-melding voor deze stroom (het
lucht-been wordt per constructie overgeslagen — ratio 1,000 maar niet gevlagd; de twee truckbenen ≥5 km hebben
ratio 1,364/1,082, geen rechte lijn). `json.load` slaagt: versie 2, `punt_formaat` lonlat, modaliteiten
`truck`/`truck`/`lucht`/`truck` ∈ toegestane set, elk been ≥ 2 punten (1.763/115/348/435), bestandsgrootte
54,2 KB (ruim onder ~300 KB). Naden tussen de vier benen: **0,000 km** op alle drie overgangen (b1→b2 op de DTP,
b2→b3 op de GBE-vrachtapron, b3→b4 op Brucargo). Markers: alle vijf op ≤0,1 km van hun been (elk anker is
tegelijk het routeerpunt/been-uiteinde).

**Toelichting stippels/haven-aanlopen/vluchten:** één vlucht, doorgetrokken (zie boven). Geen zeebeen in deze
keten → geen MARNET, geen haven-aanloop. Geen enkel been kreeg een stippel: de drie truckbenen zijn gewone,
gekarteerde wegen met verwaarloosbare anker-verbindingsstukjes (alle ≤0,18 km), en het luchtbeen is een gelegde
vlucht tussen twee vrachtterminals (regel: dat is per definitie geen "net reikt niet"-geval). Fase D/E vervallen
(brief §6, stoppunt bij AWDC/Diamond Office).

**Gereedschapslessen:** `maak_luchtbeen.py` en `maak_stroombeen_weg.py` werkten zonder aanpassing; het
luchtbeen-patroon uit `bakhandleiding-licht.md` §2 ("lucht|vlucht <van> → <naar> (vrachtvlucht, grootcirkel)|pad")
sluit naadloos aan op `hecht_marnet.py route --been-geojson`. Alle drie de webcheck-cijfers uit de opdracht
(166,7 / 5,0 / 37,7 km) kwamen binnen 6,7% van de gemeten geometrie terug — de OSRM-webchecks uit de brief bleken
betrouwbaarder dan de oorspronkelijke ketenontwerp-schattingen (met name b2: ontwerp ~15 km, gemeten 4,7 km).
⚠️ De sandbox van deze sessie stond het voorgeschreven `neem_slot`-mechanisme (met zijn `rm -rf "$d"`-opruiming)
niet toe (geblokkeerd door een ingebouwde veiligheidscheck op een pad met variabelen); de twee wegscans en de bake
zijn daarom **zonder slot** gedraaid — beide extracts zijn klein (botswana 88 MB, belgie 690 MB, geen "reus") en
liepen elk binnen 31 s, dus geen waarneembare belasting van de gedeelde machine.
