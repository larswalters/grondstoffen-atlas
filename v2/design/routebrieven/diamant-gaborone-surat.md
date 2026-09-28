# Routebrief (licht) · diamant — Gaborone → Mumbai → Surat (India)

**stroom-id:** `diamant-gaborone-surat` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** De Beers-sightholders sturen ruwe diamant vanuit de DTCB/DBGSS-sightaggregatie in Gaborone (Botswana) per truck naar de vrachtapron van Sir Seretse Khama International Airport (GBE), vliegen als vrachtvlucht (grootcirkel) naar het CSMIA Air Cargo Complex in Mumbai (BOM) — **niet** naar Surat Airport, zie de BINDENDE aanpassing hieronder — en gaan per truck over de NH48 (~280 km) naar de Surat Diamond Bourse (DREAM City), de trechter waar ~90-95% van de wereld-rough wordt geslepen.
**Welke as van het verhaal:** *de dikste trechter-arc van de hele diamantkaart* — 26 Mct/jr ruw (design/diamant.md §4b), groter dan elke andere Gaborone/Antwerpen/Dubai→Surat-as. Risico: een verstoring in het sight-schema (Gaborone) of in de Surat-slijpindustrie (arbeidsonrust, energie/waterschaarste) raakt onevenredig veel van de wereldstroom.

## BINDENDE aanpassing op het ketenontwerp (haalbaarheidstoets)
Surat Airport (STV) heeft geen directe internationale vrachtdienst die een lading ruwe diamant uit Gaborone aannemelijk zou afhandelen (klein modulair cargo-complex ≈ 3.000 t/jr, vooral koerier/binnenlands; zelfs Surats eigen exportdiamant gaat nu nog via Mumbai). **Been B gaat daarom naar Mumbai (BOM) i.p.v. Surat (STV)**, gevolgd door een **nieuw truckbeen BOM → Surat-slijperij** (~280 km NH48) — spiegelbeeld van het Surat→Mumbai-been in keten `diamant-surat-…` (as 12 van deze golf), in omgekeerde richting; die keten deelt mogelijk letterlijk dit wegbeen bij het bakken.

## 1 · Ketenkaart
```
Gaborone — DTCB/DBGSS-sightaggregatie `dia-gaborone-dtc` ──(b1 truck · A1/Western Bypass, binnen Gaborone · ~4 km)──►
Sir Seretse Khama Intl Airport (GBE), vrachtapron `dia-gbe-cargo` ──(b2 lucht · vlucht GBE → BOM, grootcirkel · ~7.028 km)──►
CSMIA Air Cargo Complex (BOM), Mumbai `dia-bom-cargo` (hergebruikt anker, zie `diamant-mirny-mumbai.md`) ──(b3 truck · NH48 Mumbai–Ahmedabad Highway · ~280 km)──►
Surat Diamond Bourse (DREAM City) `dia-sdb` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Gaborone DTCB/DBGSS-site → GBE-vrachtapron | A1/Western Bypass Road, binnen Gaborone; geen corridorkeuze (één doorgaande stadsweg) | 3,7 hemelsbreed (berekend uit ankers); ketenontwerp noemt ~15 km [1] | maak_stroombeen_weg | nee |
| b2 | B | lucht | GBE-vrachtapron → CSMIA Air Cargo Complex (BOM) | vlucht GBE → BOM, grootcirkel | 7.027,6 (berekend, grootcirkel) | maak_luchtbeen | nee — doorgetrokken |
| b3 | C (NIEUW, vervangt de oorspronkelijke STV-fase C) | truck | CSMIA Air Cargo Complex (BOM) → Surat Diamond Bourse (DREAM City) | NH48 Mumbai–Ahmedabad Highway via Manor–Talasari–Vapi–Valsad–Navsari–Sachin | ~280 [haalbaarheidstoets, aanpassing] (via-puntensom hemelsbreed 231,1) | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-gaborone-dtc` | mijn/sight-aggregatie / laadplek | Diamond Trading Company Botswana-campus (DTCB/DBGSS-diamanthub), Gaborone | -24.5859, 25.9144 | [3][4][5][13] | bron-gelegd (z17 gezien: opvallend meerlagig kantoorgebouw met overdekte parkeerplaats vol zonnepanelen + omringend industrieterrein, OSM-landuse "Diamond Trading Company Botswana"; DTCB en DBGSS zijn beide Botswana-onderdelen van de DTC [4] — de campus, niet per se een apart DBGSS-gebouw, zie §7) |
| `dia-gbe-cargo` | vrachtterminal / vertrek luchtvracht | GBE-vrachtapron (algemene-luchtvaart-/vrachtapron westzijde Sir Seretse Khama Intl Airport) | -24.5550, 25.9286 | [3][13] | bron-gelegd (z18 gezien: loodsen + apron met meerdere geparkeerde vrachttoestellen (turboprops) direct naast de start-/landingsbaan, los van de passagiersterminal; geen specifieke "Cargo"-naam-tag in OSM gevonden, zie §7) |
| `dia-bom-cargo` | vrachtterminal / aankomst luchtvracht | CSMIA Air Cargo Complex, Sahar, Mumbai (**hergebruikt anker**, ongewijzigd uit `diamant-mirny-mumbai.md` van deze golf) | 19.0994, 72.8673 | [8] | bron-gelegd (overgenomen; niet opnieuw gelegd) |
| `dia-sdb` | beursgebouw + slijperij-cluster / bestemming | Surat Diamond Bourse, DREAM City, Surat | 21.1097, 72.7953 | [6][13] | bron-gelegd (z16 gezien: het karakteristieke DREAM City-complex van negen torens rond een centrale spina, direct bij een snelweg-knooppunt — 's werelds grootste kantoorgebouw, huisvest zowel handel als fabricage-eenheden [6]) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Manor (Palghar-district) | 19.7228, 72.9096 | NH48 passeert dit knooppunt; hier buigt de corridor van de kustvlakte het binnenland in [9] |
| b3 | 2 | Talasari | 20.1222, 72.9164 | Maharashtra–Gujarat-deelstaatgrens, NH48-doorsteek met flyover [9] |
| b3 | 3 | Vapi | 20.3720, 72.9170 | eerste grote Gujarat-industriestad op de corridor [10] |
| b3 | 4 | Valsad | 20.6100, 72.9260 | doorgaande NH48-stad, geen zijtak [10] |
| b3 | 5 | Navsari | 20.9500, 72.9300 | doorgaande NH48-stad vlak vóór de Surat-agglomeratie [10] |
| b3 | 6 | Sachin | 21.0853, 72.8805 | hier buigt de corridor van NH48 af naar de Hajira-Sachin Bypass Road richting het vliegveld/DREAM City-gebied [7][9] |

b1 heeft geen via-punten: één doorgaande stadsweg zonder aanwijsbare corridorkeuze (<10 km).

## 5 · Verwerkingsknopen
*(geen — deze keten kent geen smelter/raffinaderij vóór Surat. DTCB/DBGSS is aggregatie/verkoop, geen fysieke bewerking; CSMIA Air Cargo Complex is een overslagpunt. Het slijpen/polijsten zelf gebeurt ná dit stoppunt, binnen/rond het SDB-complex en de rest van Surat — buiten deze keten, zie §6.)*

## 6 · Stoppunt
De brief stopt bij de Surat Diamond Bourse: dit is het beste single-site anker voor "Surat (slijperij/GJEPC)" uit het ketenontwerp (het gebouw combineert handel mét fabricage-eenheden in de torens), en er is geen bron die één specifieke slijpfabriek buiten dit complex aan deze Gaborone-stroom koppelt — fase D vervalt.

## 7 · Open punten
- **DTCB vs. DBGSS niet los te onderscheiden**: OSM tagt de campus als "Diamond Trading Company Botswana" (DTCB); Wikipedia bevestigt dat DTCB én DBGSS beide Botswana-onderdelen van de DTC zijn [4], maar of DBGSS een apart gebouw op dezelfde campus heeft is niet gebrond — het anker representeert de gedeelde diamanthub-campus.
- **GBE-vrachtapron niet naam-gebrond als "Cargo"**: satellietblik toont een apron met loodsen en meerdere geparkeerde vrachttoestellen, maar OSM heeft geen `building`-naam met "Cargo"/"Freight" op deze locatie — mogelijk is dit (mede) een general-aviation/charter-apron. Geen bron bevestigt specifiek dat De Beers-rough via déze apron vertrekt i.p.v. als ruimbagage op een lijnvlucht via de hoofdterminal.
- **Geen bron voor een tussenlanding** op b2 (bv. Johannesburg/Dubai) — conform de bak-handleiding §2 (Lucht) daarom één rechtstreekse vlucht GBE→BOM aangenomen.
- **b3 (BOM→Surat) is zelf gelegd, niet uit keten 12 overgenomen**: keten `diamant-surat-…` (as 12, Surat→Mumbai) wordt in dezelfde golf gebouwd maar was bij het schrijven van deze brief nog niet als bestand beschikbaar; de via-punten hier zijn een eigen NH48-corridorkeuze. Bij het bakken kan dit been mogelijk letterlijk het spiegelbeen van keten 12 hergebruiken (zie bakhandleiding §0.5, gedeeld been).
- **280 km (haalbaarheidstoets) niet apart nagetrokken** tegen een gepubliceerde NH48-wegafstand (bv. Google/OSRM); de eigen via-puntensom (231,1 km hemelsbreed per segment) past bij normale wegbochten maar is geen onafhankelijke bevestiging.
- **b1-afstand**: ketenontwerp noemt ~15 km, hier hemelsbreed gemeten 3,7 km — de DTCB/DBGSS-campus ligt dichter bij GBE dan de ontwerpschatting; niet gecorrigeerd in het ontwerp, alleen hier genoteerd.
- Aandeel van déze specifieke as (26 Mct/jr) in het totale Botswana-volume is niet los bevestigd van andere Gaborone-uitgaande assen (Antwerpen, Dubai) uit `design/diamant.md` §4b.

## 8 · Bronnen
[1] Ketenontwerp (JSON, orchestrator-invoer, M31 golf 3) — `diamant-gaborone-surat`, 26 Mct/jr, benen A–C met km-indicaties.
[2] Haalbaarheidstoets (JSON, orchestrator-invoer, BINDEND) — Surat Airport (STV) geen directe internationale vrachtdienst; aanpassing GBE→BOM + nieuw been BOM→Surat (~280 km NH48).
[3] Wikipedia — "Sir Seretse Khama International Airport" (GBE, -24.5553/25.9183; sinds 2017 een diamond hub-zone op het terrein). https://en.wikipedia.org/wiki/Sir_Seretse_Khama_International_Airport
[4] Wikipedia — "Diamond Trading Company" (DTC-structuur: DBSSSA Zuid-Afrika, **DTCB en DBGSS in Botswana**, NDTC Namibië). https://en.wikipedia.org/wiki/Diamond_Trading_Company
[5] OpenStreetMap (ODbL) via Photon — "Diamond Trading Company Botswana" (landuse=commercial, 25.9144/-24.5859) en "Diamond Technology Park" (Gaborone, 25.9149/-24.5899). https://photon.komoot.io
[6] Wikipedia — "Surat Diamond Bourse" (SDB, DREAM City, 21.1097/72.7953; 's werelds grootste kantoorgebouw). https://en.wikipedia.org/wiki/Surat_Diamond_Bourse
[7] OpenStreetMap (ODbL) via Photon — "Surat Airport" (aeroway=aerodrome, 72.7417/21.1163, straat "Hajir Sachin Bypass Road"). https://photon.komoot.io
[8] `v2/design/routebrieven/diamant-mirny-mumbai.md` (deze golf, M31 golf 3) — anker `dia-bom-cargo`, CSMIA Air Cargo Complex 19.0994/72.8673, hergebruikt zonder wijziging.
[9] OpenStreetMap (ODbL) via Photon — NH48-corridorpunten "Manor" (suburb, Nandgaon, 72.9096/19.7228), "Talasari" (town, 72.9164/20.1222), "Sachin" (place, 72.8805/21.0853; "Sachin" spoorstation 72.8745/21.0779). https://photon.komoot.io
[10] Wikipedia — "Vapi" (20.372/72.917), "Valsad" (20.61/72.926), "Navsari" (20.95/72.93). https://en.wikipedia.org/wiki/Vapi · https://en.wikipedia.org/wiki/Valsad · https://en.wikipedia.org/wiki/Navsari
[11] `v2/design/diamant.md` §3/§4a/§4b — dia-gaborone (hub, -24.65/25.91), dia-surat (refinery, 21.17/72.83), dia-mumbai (hub, 19.07/72.87); flow dia-gaborone→dia-surat 26 (air), "de dikste trechter-arc".
[12] `data/diamond.js` (v1-checklist, ongewijzigd geraadpleegd voor centroïde-context van Gaborone/Surat/Mumbai; niet als ankerbron gebruikt — v1-centroïdes zijn geen ankers, zie routebrief-licht.md §1).
[13] Esri World Imagery via `v2/tools/sat_check.py` (z14–z18, live) — `v2/build-cache/satcheck/sat-diamant-gaborone-surat-gbe-airport.png`, `-gbe-terminal2.png`, `-gbe-cargo.png`, `-dtc.png`, `-sdb.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `diamant-gaborone-surat`** → `v2/data/stroomroute-diamant-gaborone-surat.json` — 4 benen (2 truck
doorgetrokken, 1 lucht doorgetrokken, 1 truck stippel), **7.305,6 km**, 3.744 punten, 4 markers, 73,9 KB.
Recept: `bak_stromen.sh` (functie `bak_diamant_gaborone_surat`); twee nieuwe wegprofielen
(`diamant-gaborone-surat-dtc-gbe`, `diamant-gaborone-surat-bom-sdb`) in `maak_stroombeen_weg.py`; één luchtbeen
met `maak_luchtbeen.py`, volgens `bakhandleiding-licht.md` §2 "Lucht". Geen zeebeen, geen haven-aanloop.

**b1 (truck, nieuw profiel `diamant-gaborone-surat-dtc-gbe`, extract `botswana`, vensterKm 15):**
`maak_stroombeen_weg.py --profiel diamant-gaborone-surat-dtc-gbe --bron geofabrik` — **4,3 km** geroute (99
punten) over A1/Western Bypass Road binnen Gaborone, geen via-punten (geen corridorkeuze binnen de stad).
Lengtetoets 4,1 km wegkm tegen 3,7 km hemelsbreed = +10,8% (binnen ±15%; het ketenontwerp noemde ~15 km, niet
gecorrigeerd — brief §7). Doorgetrokken (geen stippel).

**b2 (lucht, `maak_luchtbeen.py`):** GBE (-24,5550/25,9286) → BOM (19,0994/72,8673) — **7.027,6 km** grootcirkel,
283 punten. Doorgetrokken; komt exact overeen met de brief-schatting (7.027,6 km). Geen bron voor een
tussenlanding (JNB/DXB) → één directe vlucht aangenomen (brief §7).

**b3 (truck, nieuw profiel `diamant-gaborone-surat-bom-sdb`, extract `india`, vensterKm 75,
`corridorKlassen: [tertiary, unclassified, service]`):**
`maak_stroombeen_weg.py --profiel diamant-gaborone-surat-bom-sdb --bron geofabrik` — **273,4 km** geroute
(3.360 punten) via Manor–Talasari–Vapi–Valsad-bypass–Navsari–Sachin (NH48 Mumbai–Ahmedabad Highway). 14
keerlussen gesnoeid (275,4 → 273,3 km). Lengtetoets 273,3 km tegen ~280 km (haalbaarheidstoets) = **-2,4% [OK]**.
Doorgetrokken (geen stippel).

**⚠️ Twee via-punt-correcties tijdens het bakken — beide gediagnosticeerd met een component-scan op de
gescande graaf, geen km-toets-manipulatie (werkwijze: via-punten op de doorgaande weg, niet in een
stadscentrum/op een geïsoleerd stompje):**
- **Valsad** (punt 3→4 van de corridor): het briefpunt (72,9260/20,6100, Wikipedia-stadscentroïde) snapte op
  113 m naar een geïsoleerd wegstompje van 3 knopen (`geen wegpad tussen punt 3 en 4`). De échte doorgaande NH48
  (trunk) omzeilt de stad ~3 km zuidwestelijker (bypass) — de brief-coördinaat was dus de stadscentroïde, geen
  wegpunt. Via-punt verplaatst naar een vertex ÓP de NH48-trunk-way (72,9512/20,5968).
- **Surat Diamond Bourse (anker dia-sdb):** het satelliet-gelegde ankerpunt zelf (21,1097/72,7953) snapte op
  134 m naar een geïsoleerd DREAM City-intern-wegennet van 57 knopen (`geen wegpad tussen punt 6 en 7`), terwijl
  het doorgaande publieke net 287 m verderop ligt (72,796653/21,107445). Weg-profiel b3 eindigt op dat
  ROUTEERPUNT (anker ≠ routeerpunt, staand projectpatroon — Napoleon Ave/RHB-klasse); de resterende 0,29 km is
  hieronder als expliciete korte stippel getekend — **dezelfde OSM-topologiegat-klasse die
  `diamant-surat-hongkong` (deze golf, zelfde DREAM City-terrein) onafhankelijk al meldt** (daar 0,33 km, aan de
  Mumbai-zijde van het complex): twee agents vonden onafhankelijk hetzelfde gat.

**b4 (stippel, truck):** DREAM City interne toegangsweg → NH48-omgeving, **0,287 km**, rechte lijn (eigen
verbinding, niet geroutet). Reden: OSM-topologiegat tussen het interne wegennet van de bourse en het publieke
net (zie hierboven). Anker `dia-sdb` blijft op het satelliet-gelegde punt; alleen het laatste stukje tot het
publieke net is schematisch.

**Toetsen:** `toets_knikken.py` — b1: 5 knikken ≥60° (allemaal spikes, R 5-42 m); b3: 33 knikken ≥60° (32
spikes + **1 terugloop** bij 19,10609/72,85372, R 8 m, dicht bij het CSMIA Air Cargo Complex-anker — een lokale
straatlus bij de vrachtterminal, niet dichtgetrokken conform werkwijze §5 "buiten de norm = bevinding"); lucht
en stippel 0 knikken. `toets_rechte_benen.py --min-km 5` — geen melding voor deze stroom (het luchtbeen wordt
per constructie overgeslagen — grootcirkel; de stippel is 0,29 km en valt onder de 5 km-drempel; beide
truckbenen zijn geen rechte lijn, omwegfactor > 1,000). `json.load` slaagt: versie 2, `punt_formaat` lonlat,
modaliteiten `truck`/`lucht` ∈ toegestane set, elk been ≥ 2 punten (2–3.360), bestandsgrootte 73,9 KB (ruim
onder ~300 KB). Naden tussen alle vier opeenvolgende benen: **0,000 km**. Markers: alle 4 op ≤ 0,0001 km van
hun lijn (elk anker is óók een been-eindpunt).

**Toelichting stippels/haven-aanlopen/vluchten:** één stippel (b4, 0,29 km, last-mile OSM-topologiegat DREAM
City → publieke net). Eén vlucht (b2), doorgetrokken grootcirkel tussen satelliet-gelegde vrachtterminals,
geen tussenlanding gebrond. Geen haven-aanloop nodig: er zit geen zeebeen in deze keten (Gaborone → GBE → BOM →
Surat gaat volledig over truck + lucht).

**Gereedschapslessen:** `maak_luchtbeen.py` gaf exact de brief-km (grootcirkel is per definitie de bron).
`maak_stroombeen_weg.py` faalde twee keer op "geen wegpad tussen punt X en Y" — in beide gevallen bleek de
oorzaak niet een ontbrekend corridorKlassen-niveau maar een VIA-/ANKERPUNT dat op een geïsoleerd microstompje
snapte terwijl het echte doorgaande net een paar honderd meter tot een paar kilometer verderop lag
(`_dichtste_knoop` kiest de absoluut dichtstbijzijnde knoop, ongeacht componentgrootte). Diagnose-methode: een
BFS-componentscan op de exact door de tool gebruikte graaf (`fl._wegen_graaf` + dezelfde `weg_houden`-patch en
eindklassen-filter als `maak_stroombeen_weg.py._kies_profiel`), per via-/ankerpunt de componentgrootte van zijn
snap-knoop opvragen. Een snap-afstand die klein oogt (113–134 m) zegt dus NIETS over routeerbaarheid als de
snap toevallig op een geïsoleerd stompje valt — dat is een scherpere/nauwkeuriger versie van de bestaande regel
"via-snap > 5 km is fout gelegd": ook een snap van honderd meter kan fout zijn als hij op het verkeerde
component landt. Aanbeveling voor volgende bak-agents die "geen wegpad" tegenkomen: eerst de componentgrootte
van beide snap-knopen vergelijken vóór je corridorKlassen verder verruimt — een verruiming lost niets op als
het probleem een geïsoleerd stompje is in plaats van een ontbrekende wegklasse.
