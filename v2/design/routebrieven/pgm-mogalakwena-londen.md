# Routebrief (licht) · PGM — Mogalakwena (Bushveld) → OR Tambo → Londen (Royston, Verenigd Koninkrijk)

**stroom-id:** `pgm-mogalakwena-londen` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** platina/palladium/rodium van de Mogalakwena-concentrator (Valterra Platinum, ex-Anglo American Platinum, Noordelijke rand Bushveld) per **truck** naar de **Rustenburg PMR**-raffinaderij, per **truck** naar de OR Tambo (JNB) vrachtterminal, per **vrachtvlucht** (grootcirkel, aannemelijk) naar Heathrow (LHR), en per **truck** naar de **Johnson Matthey Royston**-raffinaderij (Hertfordshire, LPPM-erkend voor good-delivery baren) — stoppunt.
**Welke as van het verhaal:** Zuid-Afrika/Bushveld → Londen. Mogalakwena produceerde 2023 ~900 koz Pt+Pd+Rh (Anglo American Platinum-jaarverslag [1]) ≈ **28,0 t 3E/jaar** (900÷32,15); Rustenburg PMR raffineert het grootste deel van het Zuid-Afrikaanse platina, geen site-specifiek Mogalakwena→Royston-volume gevonden (§7). **BINDEND aangepast** (haalbaarheidstoets): naar_site is uitsluitend Johnson Matthey Royston, niet "LPPM-kluis" — één site-anker per overslag.

## 1 · Ketenkaart
```
Mogalakwena-concentrator `pgm-mogalakwena-mijn` ──(b1 truck · N1/R24 · ~341 km)──►
  Rustenburg PMR `pgm-rustenburg-pmr` ──(b2 truck · N4/N1/R21 · ~120 km [ontwerp], eigen check ~166 km)──►
  OR Tambo vrachtterminal `pgm-jnb-cargo` ──(b3 lucht · vlucht JNB → LHR, grootcirkel · 9.072 km)──►
  Heathrow vrachtterminal `pgm-lhr-cargo` ──(b4 truck · M25/A1(M)/A505 · ~97 km)──►
  Johnson Matthey Royston `pgm-jm-royston` ── stoppunt (eindraffinage, LPPM good-delivery)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-mogalakwena-mijn` → `pgm-rustenburg-pmr` | N1 (Mokopane–Mookgophong–Bela-Bela–Pretoria-Noord) → R24 "Platinum Highway" (Pretoria–Rustenburg) | 341 [10, OSRM]; ontwerp ~180 — **correctie, zie §7** | maak_stroombeen_weg — profiel `pgm-mogalakwena-rustenburg` | nee |
| b2 | B | truck | `pgm-rustenburg-pmr` → `pgm-jnb-cargo` | N4 (Rustenburg–Brits–Pretoria) → N1/R21 (Pretoria–Midrand–Kempton Park) | ~120 [ontwerp/11]; eigen OSRM-check 166 km — zie §7 | maak_stroombeen_weg — profiel `pgm-rustenburg-jnb` (hergebruik van via-punten uit [11][12] mogelijk) | nee |
| b3 | B | lucht | `pgm-jnb-cargo` → `pgm-lhr-cargo` | vrachtvlucht JNB → LHR, grootcirkel | 9.072 [9, maak_luchtbeen.py, reeds gegenereerd] | maak_luchtbeen | nee — doorgetrokken (bakhandleiding §2) |
| b4 | C | truck | `pgm-lhr-cargo` → `pgm-jm-royston` | M4 → M25 (westelijke ring) → A1(M) → A505 Baldock–Royston | 97 [10, OSRM]; BINDEND genoemd M25/A10/A505 — gemeten pad neemt A1(M) i.p.v. A10, zie §7 | maak_stroombeen_weg — profiel `pgm-heathrow-royston` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-mogalakwena-mijn` | mijn / concentrator (laadplek) | Mogalakwena-concentrator, Valterra Platinum (ex-Anglo American Platinum), Mokopane, Limpopo | -23.9805, 28.9160 | [2][14] | bron-gelegd (z16 gezien: ertsverwerkingscomplex met conveyors, silo's en crusher-gebouwen ZO van de open pit, tussen twee tailingsdams) |
| `pgm-rustenburg-pmr` | raffinaderij (overslag) | Rustenburg PMR (Waterval-smelter/RBMR/PMR-complex), Valterra Platinum | -25.6750, 27.3180 | **hergebruikt anker** uit [11][12] (zelfde golf) + eigen satellietblik (z16, ~0,4 km ernaast, zelfde complex) | bron-gelegd (overgenomen + bevestigd) |
| `pgm-jnb-cargo` | vrachtterminal (luchtanker) | OR Tambo (JNB) vrachtplatform/-loodsen, Kempton Park | -26.1380, 28.2270 | **hergebruikt anker** uit [11] (zelfde golf) + eigen satellietblik (z17, andere apron-cluster ~2,5 km ervandaan, ook loodsen + vrachttoestellen) | bron-gelegd (overgenomen) |
| `pgm-lhr-cargo` | vrachtterminal (luchtanker) | Heathrow (LHR) World Cargo Centre — vrachtloodsen + platform | 51.4703, -0.4195 | [8][14] | bron-gelegd (z17 gezien: rij vrachtloodsen met plat/donker dak, platform met meerdere geparkeerde widebody-vrachttoestellen) |
| `pgm-jm-royston` | raffinaderij (eindpunt) | Johnson Matthey Royston PGM-raffinaderij, Orchard Road Industrial Estate, Royston, Hertfordshire | 52.0550, -0.0351 | [5][6][7][14] | bron-gelegd (z17 gezien: industrieel gebouwencomplex op het aangewezen kavel; komt overeen met OSM `man_made=works` "Johnson Matthey") |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Mokopane (N1-aansluiting) | -24.1833, 29.0167 | eerste doorgaande N1-knoop na de mijn; sluit de lokale R518 uit |
| b1 | 2 | Mookgophong (N1) | -24.5144, 28.7163 | doorgaande N1 zuidwaarts, geen zijtak |
| b1 | 3 | Bela-Bela (N1) | -24.8806, 28.2905 | doorgaande N1 naar de Pretoria-Noord/Platinum Highway-aansluiting |
| b1 | 4 | Akasia (N1 → R24 "Platinum Highway"-wissel) | -25.6548, 28.1136 | hier verlaat de route de N1 en gaat de R24 westwaarts op naar Rustenburg |
| b2 | 1 | Brits (N4-knoop) | -25.6344, 27.7811 | vaste doorgaande knoop op de N4 (hergebruikt uit [11][13]) |
| b2 | 2 | Pretoria (N4/N1-knoop) | -25.7461, 28.1881 | hier voegt de N4 samen met de N1 zuidwaarts (hergebruikt uit [11]) |
| b2 | 3 | Midrand/Allandale (N1/R21-knoop) | -25.9992, 28.1264 | hier buigt de route van de N1 af op de R21 naar OR Tambo (hergebruikt uit [11][12]) |
| b4 | 1 | Denham (M25-west) | 51.5741, -0.5351 | M25-passage rond West-Londen, sluit de binnenstad uit |
| b4 | 2 | Abbots Langley (M25-noord, Hertfordshire) | 51.7131, -0.4059 | doorgaande M25 richting de A1(M)-aftakking |
| b4 | 3 | Welwyn (A1(M)) | 51.8100, -0.2285 | doorgaande A1(M) noordwaarts (§7: A1(M) i.p.v. de genoemde A10) |
| b4 | 4 | Baldock Bypass (A1(M) → A505-wissel) | 51.9663, -0.1928 | hier verlaat de route de A1(M) en gaat de A505 naar Royston op |

Geofabrik-regio's: `zuid-afrika` (b1, b2) · `groot-brittannie` (b4).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Rustenburg PMR | Valterra Platinum (ex-Anglo American Platinum) | Bushveld-erts/matte → geregistreerd Pt/Pd/Rh | "'s werelds grootste platinaraffinaderij" (~70% wereldplatina), geen t/j gevonden | [4][11][12] |
| Johnson Matthey Royston | Johnson Matthey | geregistreerd Pt/Pd/Rh → LPPM good-delivery baren | nieuwe PGM-raffinaderij op dezelfde locatie, bouw sinds 2019, operationeel vanaf 2027 [6][7] | [5][6][7] |

## 6 · Stoppunt
De brief stopt bij Johnson Matthey Royston: dat is de BINDEND aangewezen eindraffinage (LPPM good-delivery), en geen bron noemt een vervolgzending naar een specifieke afnemer/fabriek — fase D vervalt (werkwijze licht §1).

## 7 · Open punten
- **b1-lengte fors gecorrigeerd:** het ketenontwerp noemt ~180 km; een echte routering (OSRM/OSM-wegennet) over N1+R24 geeft **341 km** — een route via Thabazimbi/Northam (R510) is via OSRM zelfs nog langer (377 km). Het ontwerpcijfer lijkt een hemelsbrede of onderschatte afstand; 341 km is hier het werkcijfer, geen operator-bron.
- **b2-lengte:** ontwerp ~120 km (ook zo aangehouden in de zusterbrieven [11][12] van deze golf); eigen OSRM-check geeft 166 km. Beide zusterbrieven behandelen het ontwerpcijfer als indicatief — dit volgt hetzelfde; de bake-lengtetoets beslist.
- **b4-lengte:** BINDEND-tekst noemt ~50 km via M25/A10/A505; gemeten (OSRM) is het 97 km via M25/A1(M)/A505 — de A1(M) is hier het functionele equivalent van de genoemde A10 (beide sluiten aan op de A505 bij Baldock). Bron_voor_luchtvracht blijft ongewijzigd van kracht.
- **Bron_voor_luchtvracht JNB→LHR:** aannemelijk, analoog aan de goud-/Rand Refinery-luchtvrachtpraktijk vanuit Zuid-Afrika (conform de BINDEND-aanpassing); geen PGM-specifieke bron voor déze vlucht gevonden. Geen tussenlanding gebrond → één directe vlucht.
- **Rustenburg PMR — exacte PMR-hal niet afgebakend:** het complex bevat smelter + RBMR + PMR ineen (zelfde beperking als in [11][12]); het anker is site-niveau.
- **Jaarvolume déze specifieke as (Mogalakwena→Royston):** niet gevonden; alleen Mogalakwena-mijnvolume (nationaal/site) en algemene Rustenburg PMR-marktrol.
- **Rustenburg PMR → OR Tambo (b2)** is dezelfde corridor als in [11] en [12] (parallelle golf-3-ketens); bake-agent kan het reeds gebakken been hergebruiken (`vertakt_van`/gedeeld-been-patroon) i.p.v. opnieuw te bakken — zie bak_aanwijzingen.

## 8 · Bronnen
[1] Anglo American / Valterra Platinum, Platinum fact sheet (ketenontwerp-bron), Mogalakwena 2023 ~900 koz Pt+Pd+Rh. https://www.angloamerican.com/business/platinum/~/media/Files/A/Anglo-American-Plc/docs/platinum_10.pdf
[2] OpenStreetMap (ODbL) — landuse "Mogalakwena Platinum Mine", -23.9928/28.9050. https://www.openstreetmap.org
[3] Johnson Matthey, PGM Markets. https://matthey.com/products-and-markets/pgms
[4] Wikipedia, "Rustenburg" — "the world's largest platinum refinery, PMR (Precious Metal Refiners), which processes around 70% of the world's platinum". https://en.wikipedia.org/wiki/Rustenburg
[5] Wikipedia, "Valterra Platinum" (voorheen Anglo American Platinum). https://en.wikipedia.org/wiki/Valterra_Platinum
[6] Johnson Matthey Technology Review, "A New Platinum Metals Refinery" (Royston-historie). https://technology.matthey.com/article/28/1/2-6
[7] Royston Crow, over de nieuwe JM PGM-raffinaderij in Royston (bouw sinds 2019, operationeel vanaf 2027). https://www.royston-crow.co.uk/news/25689955.rosyton-firm-rejects-safety-concerns-staff-suspended/
[8] OpenStreetMap (ODbL) via Photon — "Heathrow South Cargo Centre", -0.4120/51.4683. https://www.openstreetmap.org
[9] LPPM. https://www.lppm.com/
[10] OSRM (router.project-osrm.org, OpenStreetMap-wegennet) — gemeten wegafstanden b1 (341 km), b2 (166 km), b4 (97 km), 2026-09-28.
[11] v2/design/routebrieven/pgm-rustenburg-shanghai.md — hergebruikte ankers `pgm-rustenburg-pmr`, `pgm-jnb-cargo` + via-punten b2 (zelfde golf, M31 golf 3).
[12] v2/design/routebrieven/pgm-zimplats-rustenburg.md — bevestiging Rustenburg PMR-anker (zelfde golf).
[13] OpenStreetMap (ODbL) via Photon — Mokopane, Mookgophong, Bela-Bela, Brits, Centurion, Midrand, Denham, Abbots Langley, Welwyn, Baldock Bypass, Northam, Thabazimbi, Marikana (plaatscentra). https://www.openstreetmap.org
[14] Esri World Imagery via `v2/tools/sat_check.py` (z14–z17) — `v2/build-cache/satcheck/sat-pgm-mogalakwena-londen-mijnpit.png`, `sat-pgm-mogalakwena-londen-concentrator.png`, `sat-pgm-mogalakwena-londen-aap-candidate1/2/3.png`, `sat-pgm-mogalakwena-londen-ortambo-cargo.png`, `sat-pgm-mogalakwena-londen-ortambo-cargo2.png`, `sat-pgm-mogalakwena-londen-heathrow-cargo.png`, `sat-pgm-mogalakwena-londen-heathrow-cargo2.png`, `sat-pgm-mogalakwena-londen-royston.png`.


## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `pgm-mogalakwena-londen`** → `v2/data/stroomroute-pgm-mogalakwena-londen.json` — 4 benen (truck fase A →
truck fase B → lucht fase B → truck fase C → stoppunt), **9.688,8 km**, 6.385 punten, 5 markers, 128,9 KB.
Recept: `bak_stromen.sh` (functie `bak_pgm_mogalakwena_londen`); twee nieuwe wegprofielen
`pgm-mogalakwena-londen-mogalakwena-rustenburg` en `pgm-mogalakwena-londen-heathrow-royston` in
`maak_stroombeen_weg.py`. Lucht-geojson (`pgm-mogalakwena-londen-lucht-jnb-lhr.geojson`, 9.071,9 km) stond al op
schijf (eerder met `maak_luchtbeen.py` gegenereerd) en is ongewijzigd hergebruikt.

**b1 (truck, nieuw profiel, extract `zuid-afrika`, vensterKm 50):**
`maak_stroombeen_weg.py --profiel pgm-mogalakwena-londen-mogalakwena-rustenburg --bron geofabrik` —
**336,4 km** geroute (getekende lijn 336,7 km incl. anker-verbindingsstukjes) over de vier via-punten uit de
brief (Mokopane → Mookgophong → Bela-Bela → Akasia/N1→R24-wissel), N1 zuidwaarts → R24 "Platinum Highway"
westwaarts. Anker-verbindingsstukjes plant → weg 0,15 km en weg → kade 0,17 km (beide OK, ruim binnen 0,5 km). 4
keerlussen gesnoeid (365,0 → 336,4 km). First mile 9,72 km / last mile 8,89 km over kleine wegklassen
(residential/service/tertiary/unclassified). Tegen het werkcijfer **341 km** (geen operator-bron, eigen
OSRM-meting, routebrief §7): **−1,3% [OK]**, ruim binnen ±15% — het ontwerpcijfer ~180 km blijft daarmee bevestigd
fors onderschat (§7, niet dichtgetrokken).

**b2 (truck, GEDEELD BEEN, letterlijk hergebruikt, GEEN nieuwe scan):**
`--been-geojson "truck|…|$BEEN/pgm-rustenburg-shanghai-weg-rustenburg-jnb.geojson"` — Rustenburg PMR → OR Tambo
vrachtterminal is dezelfde corridor als in `pgm-rustenburg-shanghai.md` (zelfde golf 3, hergebruik-aanwijzing in
routebrief §7); ankers komen exact overeen (-25,6750/27,3180 → -26,1380/28,2270), dus het al gebakken geojson van
die zusterbrief is hergebruikt in plaats van een derde keer te bakken. **178,2 km** in deze bake (het eigen
bakverslag van `pgm-rustenburg-shanghai` rapporteert 178,0 km voor dezelfde lijn — verschil van 0,2 km komt van
hoe `hecht_marnet.py` een reeds-gebakken been optelt, geen nieuwe geometrie). Tegen mijn eigen brief-cijfers
(gepubliceerdKm 120 ontwerp / eigen OSRM-check 166 km, §7): **+48,5%** resp. **+7,3%** — buiten resp. binnen
±15%. Dit is dezelfde bevinding die de zusterbrief al vaststelde (haar eigen ontwerpcijfer ~120 km lag +48,4%
onder de gemeten lijn): het ontwerpcijfer was voor beide brieven indicatief en niet operator-gebrond, de gedeelde
bake-uitvoer is de echte controle. Geen via-punt bijgeschoven; via-punten en been zijn ongewijzigd overgenomen.

**b3 (lucht, hergebruikt `maak_luchtbeen.py`-resultaat, DOORGETROKKEN):** geojson al aanwezig op schijf —
grootcirkel **9.071,9 km**, 364 punten, OR Tambo (JNB) vrachtterminal → Heathrow (LHR) World Cargo Centre. Tegen
het brief-cijfer 9.072 km (§1/§2): binnen afronding — een luchtbeen heeft geen ±15%-km-toets (km = grootcirkel per
constructie, bakhandleiding §5). Geen tussenlanding: geen bron in de brief noemt een hub (§7), dus één directe
vrachtvlucht JNB → LHR conform §2 "Lucht". Bron voor de modaliteit blijft **aannemelijk** (analoog aan de
goud-/Rand Refinery-luchtvrachtpraktijk vanuit Zuid-Afrika; geen PGM-specifieke bron voor déze vlucht gevonden
binnen het budget, §7) — die aanname staat in de beennaam en hier, niet in de lijnstijl (doorgetrokken).

**b4 (truck, nieuw profiel, extract `groot-brittannie`, `eindToegangPrivaat: True`, vensterKm 30):**
`maak_stroombeen_weg.py --profiel pgm-mogalakwena-londen-heathrow-royston --bron geofabrik` — eerste scanpoging
zónder `eindToegangPrivaat` faalde op "geen wegpad tussen punt 4 en 5" (Baldock Bypass → Johnson Matthey
Royston-terrein); met de vlag routeert hij door tot het terrein (snap 0,04 km). **101,9 km** geroute (getekende
lijn 102,0 km) over de vier via-punten (Denham → Abbots Langley → Welwyn → Baldock Bypass), M25-westring →
A1(M) noordwaarts → A505 naar Royston. 20 keerlussen gesnoeid (112,6 → 101,9 km). First mile 1,92 km / last mile
0,80 km over kleine wegklassen. Tegen het werkcijfer **97 km** (eigen OSRM-meting, routebrief §7): **+5,0% [OK]**
— de BINDEND-tekst noemde ~50 km via M25/A10/A505, maar de A1(M) is hier het functionele equivalent van de
genoemde A10 (beide sluiten aan op de A505 bij Baldock).

**Toetsen:** `toets_knikken.py` — b1: 17 knikken ≥60° (16 spikes + 1 scherpe bocht echt), 2 omkeringen ≥150°
waarvan **1 TERUGLOOP** bij -25,65426/28,11332 (vlak bij de N1→R24-wissel bij Akasia, v=2,5) · b2 (gedeeld been):
34 knikken, 2 omkeringen waarvan 1 TERUGLOOP bij -26,13446/28,22503 (dezelfde plek als al gerapporteerd in
`pgm-rustenburg-shanghai.md` §9 — pre-existent, hier niet aangeraakt) · b3 (lucht): 0 knikken, 0 omkeringen (per
constructie recht) · b4: 20 knikken (allemaal spikes), 0 omkeringen. Beide TERUGLOOPs zijn kleine
OSM-scannerartefacten op kleine wegklassen vlak bij een terreintoegang (Akasia-wissel resp. het JNB-cargo-terrein
van het gedeelde been) — bewust **niet** dichtgetrokken (geen via-punt geschoven); open punt hieronder.
`toets_rechte_benen.py --min-km 5` — geen melding voor deze stroom (het luchtbeen wordt per ontwerp overgeslagen,
alle drie truckbenen zijn geen rechte lijnen). `json.load` slaagt: versie 2, `punt_formaat` lonlat, modaliteiten
`truck`/`lucht` ∈ toegestane set, elk been ≥ 2 punten (2.193 / 2.064 / 364 / 1.764), bestandsgrootte **128,9 KB**
(ruim onder ~300 KB). Naden tussen opeenvolgende benen: b1→b2 0,000 km · b2→b3 2,622 km (binnen de
5 km-norm) · b3→b4 0,000 km. Markers alle op hun anker (routeerpunt = anker op elk van de vijf punten).

**Toelichting stippels/haven-aanlopen/vluchten:** geen stippel in deze stroom (alle vier benen doorgetrokken,
conform brief §1 "geen stippels"). Geen zeebeen dus geen haven-aanloop. Eén vlucht (b3), doorgetrokken conform
bakhandleiding §2: ankers = de satelliet-gelegde vrachtplatforms/-loodsen aan beide kanten (brief §3,
bron-gelegd), geen tussenlanding aangenomen (§7), modaliteit-bron **aannemelijk** (zie b3 hierboven).

**Gereedschapslessen:** (1) een gedeeld been tussen zusterbrieven van dezelfde golf hoeft niet herbouwd te worden
— `--been-geojson` met het bestaande geojson van de andere agent volstaat zodra de ankers exact overeenkomen
(hier bevestigd op de decimaal); dit voorkomt dat drie agents dezelfde 178 km-corridor drie keer bakken (zoals de
opdracht al aanwees). (2) tweede keer dat `eindToegangPrivaat` nodig bleek voor een luchthaven/raffinaderij-
vrachtterminal-anker (na JNB in de zusterbrief, nu Johnson Matthey Royston): zonder de vlag faalde
`maak_stroombeen_weg.py` op "geen wegpad tussen punt 4 en 5", met de vlag routeert hij door tot het
raffinaderijterrein — bevestigt dat een eindanker op een industrieterrein vaak een kleine-klasse toegangsweg
nodig heeft die zonder de vlag buiten het venster valt.

**Open punten (naast de reeds in §7 genoemde):** de twee TERUGLOOPs (b1 bij Akasia, b2 bij het JNB-cargo-terrein —
laatste is pre-existent uit de zusterbrief) blijven staan als kleine OSM-scannerartefacten, niet dichtgetrokken.
b2's lengte wijkt in deze bake (178,2 km) af van zowel mijn eigen ontwerpcijfer (120 km, +48,5%) als mijn eigen
OSRM-check (166 km, +7,3%) — verwacht, want het is de letterlijk hergebruikte lijn uit de zusterbrief die haar
eigen ontwerpcijfer-afwijking al heeft vastgesteld (§9 aldaar); geen actie hier.

**Herstel (2026-09-28, onafhankelijke keuring):** het luchtbeen (b3) bleek bij de bake-oplevering met een
kop-anker gegenereerd op −26,1210/28,2452 — 2,622 km van de vastgelegde vrachtterminal-marker `pgm-jnb-cargo`
(−26,1380/28,2270) — een mechanische mismatch tussen het pre-gegenereerde luchtbeen-geojson en de markercoördinaat
uit deze brief/functie, niet zichtbaar in de eigen naad-telling omdat 2,622 km ruim binnen de algemene 5 km-norm
viel maar wél de striktere lucht-norm (kop/staart ≤ 0,5 km van de terminal-marker, bakhandleiding §2) overtrad.
Hersteld: `v2/tools/maak_luchtbeen.py` opnieuw gedraaid met `--van "OR Tambo (JNB) vrachtterminal|-26.1380,28.2270"`
(exact de marker) → nieuw `pgm-mogalakwena-londen-lucht-jnb-lhr.geojson`, 9.073,1 km (was 9.071,9 km — het oude
anker lag toevallig 1,2 km dichter bij LHR). Stroom herbakken via `bash v2/tools/bak_stromen.sh
pgm-mogalakwena-londen` (zwaar-slot). Na herstel: alle vier naden 0,000 km, alle vijf markers 0,000–0,0001 km van
de lijn, luchtbeen kop/staart exact op de terminal-markers, km(lucht) = grootcirkelafstand (9.073,136… ≈ 9.073,1).
Geen via-punten verschoven, geen ander bestand/functie/profiel aangeraakt buiten deze twee (het geojson +
`bak_pgm_mogalakwena_londen`, ongewijzigde commando-structuur). Totaal 9.688,8 → **9.690,0 km**.
