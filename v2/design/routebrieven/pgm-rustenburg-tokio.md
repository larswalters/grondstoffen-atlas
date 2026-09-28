# Routebrief (licht) · PGM — Van → Via → Naar (land)

**stroom-id:** `pgm-rustenburg-tokio` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** geraffineerd platina/palladium/rodium van de Rustenburg PMR (Valterra Platinum,
Bushveld) per **truck** naar de OR Tambo-vrachtterminal (JNB), per **vrachtvlucht** (grootcirkel) naar
Narita (NRT), en per **truck** naar Tanaka Kikinzoku Kogyo in Tokio — de langste luchtafstand van de
negen PGM/goud/diamant-ketens van deze golf (~13.600 km).
**Welke as van het verhaal:** Zuid-Afrika/Bushveld → Japan — de Japanse autokat-/industriemarkt
(Toyota-thuismarkt) als PGM-eindafnemer, via een van 's werelds grootste LBMA/LPPM-erkende
edelmetaalhuizen. Geen site-specifiek Rustenburg→Tanaka-jaarvolume gevonden binnen het budget (§7).

## 1 · Ketenkaart
```
Rustenburg PMR `pgm-rustenburg-pmr` ──(b1 truck · N4/N1 Rustenburg–Johannesburg · ~120 km)──►
   OR Tambo vrachtterminal `pgm-jnb-vracht` (JNB)
   ──(b2 lucht · vrachtvlucht JNB → NRT, grootcirkel · ~13.600 km)──►
   Narita vrachtterminal `pgm-nrt-vracht` (NRT)
   ──(b3 truck · Narita Expressway–Tokio · ~65 km)──►
   Tanaka Kikinzoku Kogyo, Tokio `pgm-tanaka-tokio` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | truck | Rustenburg PMR → OR Tambo vrachtterminal | N4 (Platinum Highway) via Brits → N4/N1-knoop Pretoria-West → N1/R21-knoop Allandale → R21 | ~120 [ontwerp] | maak_stroombeen_weg | nee |
| b2 | B | lucht | OR Tambo vrachtterminal (JNB) → Narita vrachtterminal (NRT) | vrachtvlucht, grootcirkel | ~13.600 [ontwerp; grote cirkel JNB–NRT] | maak_luchtbeen | nee — doorgetrokken (§7: geen tussenlanding gebrond, één directe vlucht aangenomen) |
| b3 | C | truck | Narita vrachtterminal → Tanaka Kikinzoku Kogyo, Tokio | Higashi-Kanto Jidoshado → Keiyo-weg → Shuto-Wangan-route, Chuo-ku | ~65 [ontwerp] | maak_stroombeen_weg | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-rustenburg-pmr` | raffinaderij (kop) | Rustenburg PMR (Valterra Platinum, ex-Anglo American Platinum Precious Metals Refinery) | -25.9500, 27.3000 | [3][8] | **onzeker** — coördinaat uit projectregister `data/pgm.js` (v1, niet eerder satelliet-gelegd); z14-blik op dit punt toont landbouwgrond met center-pivot-irrigatie, géén raffinaderij (zie §7) |
| `pgm-jnb-vracht` | vrachtterminal | OR Tambo Cargo Terminal, Kempton Park (JNB) | -26.1400, 28.2300 | [1][9] | bron-gelegd (z16 gezien: cluster vrachtloodsen met platte/blauwe daken + open apron met vrachttoestellen (widebody, geen ramen) direct ten zuiden van de passagiersterminal, tussen de hoofdbaan en de N-toegangsweg — komt overeen met Wikipedia's "cargo aircraft park at aprons Golf/Whiskey/Delta/Foxtrot") |
| `pgm-nrt-vracht` | vrachtterminal | Narita Cargo Area (NRT) | 35.7743, 140.3797 | [2][9] | bron-gelegd (z16 gezien: rij blauw/wit-gedekte vrachtloodsen met meerdere vrachttoestellen op het voorterrein, tussen de A-baan en terminal 1/2, ten zuidwesten van de passagiersterminals) |
| `pgm-tanaka-tokio` | fabriek/afnemer (stoppunt) | Tanaka Kikinzoku Kogyo K.K., hoofdkantoor Nihonbashi-Kayabacho 2-6-6, Chuo-ku, Tokio 103-0025 | 35.6816, 139.7756 | [4][5][6][7] | aannemelijk (z15 gezien: kantoor-/handelsgebouw in het opgegeven Nihonbashi-Kayabacho-blok, dichte zakendistrict-bebouwing; het exacte pand is niet individueel tegen het adres geverifieerd — géén satellietherkenbaar kenmerk voor een raffinagekantoor) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kroondal — R565/N4-oprit | -25.7253, 27.3078 | hier gaat de corridor van de R565 (Rustenburg-stad) over op de N4 oostwaarts (Platinum Highway) [ontwerp] |
| b1 | 2 | Brits — N4-kruispunt | -25.6350, 27.7814 | vaste tussenstop op de N4 tussen Rustenburg en Pretoria, corridor blijft de N4 volgen [ontwerp] |
| b1 | 3 | Pretoria-West — N4/N1-knoop (Proefplaas) | -25.7615, 28.1425 | hier voegt de N4 samen met de N1, corridorkeuze N4→N1-zuid [ontwerp] |
| b1 | 4 | Allandale — N1/R21-knoop | -25.9977, 28.1234 | hier buigt de route van de N1 af op de R21 rechtstreeks naar OR Tambo [ontwerp] |
| b3 | 1 | Narita-IC — Higashi-Kanto Jidoshado | 35.7767, 140.3183 | vertrekpunt van de snelweg vanaf de luchthaven, corridorkeuze richting Chiba/Tokio [ontwerp] |
| b3 | 2 | Chiba-kita IC — overgang naar de Keiyo-weg | 35.6073, 140.1064 | hier wisselt de corridor van de Higashi-Kanto Jidoshado naar de Keiyo-weg richting Tokiobaai [ontwerp] |
| b3 | 3 | Ichikawa/Wangan-knoop | 35.6825, 139.8869 | hier gaat de route de Shuto-Wangan-route op, de laatste corridorkeuze vóór het centrum van Tokio [ontwerp] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Rustenburg PMR | Valterra Platinum (ex-Anglo American Platinum) | Bushveld-erts/matte → geregistreerd Pt/Pd/Rh | "'s werelds grootste PGM-raffinaderij", geen actueel jaarcijfer gebrond in deze brief | [3][8] |
| Tanaka Kikinzoku Kogyo | Tanaka Holdings | geraffineerd Pt/Pd/Rh (baren/sponge) → industriële halffabricaten (autokat, elektronica, sieraad) | LBMA/LPPM good-delivery-erkend refiner; geen sitevolume gebrond | [4][5] |

## 6 · Stoppunt
De brief stopt bij Tanaka Kikinzoku Kogyo's hoofdkantoor in Tokio: dit is de gedocumenteerde
LBMA/LPPM-erkende ontvanger van geraffineerd PGM in Japan, maar er is geen bron die een specifieke
fabriek/afnemer ná Tanaka noemt (autokatalysator-fabricage gebeurt bij derde partijen) — fase D
vervalt, fase E is niet in één zin te geven.

## 7 · Open punten
- **`pgm-rustenburg-pmr` is niet satelliet-bevestigd** — het coördinaat uit `data/pgm.js` (-25.95,
  27.30) bleek op z14 landbouwgrond met center-pivot-irrigatie te zijn, geen raffinaderijcomplex.
  Twee bredere z12/z13-scans rond Rustenburg tonen wél een uitgestrekte mijnbouw-/tailingsgordel
  ten noorden/noordoosten van de stad (o.a. een grote tailingsdam rond -25,50/27,25), maar zonder
  een naam-tag (Nominatim/Overpass waren binnen het webbudget herhaaldelijk 429/rate-limited) is het
  exacte PMR-terrein niet aan te wijzen. **Vraagt een vervolgpas** met een werkende OSM-bron of een
  door Lars aangeleverd adres/coördinaat vóór het bakken van b1.
- **Luchtvracht-bron is aannemelijk, niet apart gebrond voor déze vlucht** (industriestandaard PGM
  vliegt als beveiligde vracht — zie ook `design/pgm.md` §1 "PGM vliegt, net als goud"); geen
  scheepvaart-alternatief gevonden of gezocht.
- **Geen tussenlanding getekend** — geen bron noemt een hub (bv. Hongkong/Golf) voor déze
  Rustenburg→Tanaka-stroom; conform de haalbaarheidstoets blijft dit één directe grootcirkel-vlucht
  JNB→NRT, met deze aanname hier expliciet vastgelegd.
- **Geen site-specifiek jaarvolume gevonden** — alleen nationaal-niveau context (Japan = grote
  PGM-autokat-/industriemarkt, Toyota-thuismarkt); geen Rustenburg→Tanaka-specifiek cijfer binnen
  het budget. Eenheid zou t 3E/jaar zijn (Pt+Pd+Rh, zoals het v1-PGM-register) als een cijfer
  gevonden wordt.
- **Via-punten b1/b3 zijn ontwerp-niveau** (bekende snelwegcorridors/knooppunten uit algemene
  kennis, niet elk apart met een OSM-referentie gecontroleerd) — de bak-agent routeert ze via
  `maak_stroombeen_weg.py` op de echte weggeometrie; afwijkingen >5 km per via-punt zijn dan een
  bevinding, geen automatische correctie.
- **`pgm-tanaka-tokio` is het hoofdkantoor/handelsadres, geen bevestigd fabrieksterrein** — Tanaka's
  fabrieken liggen overwegend in Hiratsuka/Isehara (Kanagawa), niet in Chuo-ku Tokio; de brief houdt
  het Tokio-hoofdkantoor aan omdat het ketenontwerp expliciet "Tanaka Kikinzoku Kogyo, Tokio" als
  `naar_site` opgeeft en de opgegeven corridor-km (~65 km vanaf Narita) bij centraal Tokio past, niet
  bij Hiratsuka (~100+ km). Open punt voor Lars: is het hoofdkantoor het juiste stoppunt, of moet dit
  naar een Kanagawa-fabrieksanker?

## 8 · Bronnen
[1] Wikipedia, "O. R. Tambo International Airport" — coördinaten -26,13333/28,25000; cargo-aprons
    Golf/Whiskey/Delta/Foxtrot; cargo-terminal-uitbreiding aangekondigd maart 2024.
    https://en.wikipedia.org/wiki/O._R._Tambo_International_Airport
[2] Wikipedia, "Narita International Airport" — coördinaten 35,76528/140,38556.
    https://en.wikipedia.org/wiki/Narita_International_Airport
[3] Wikipedia, "Rustenburg" — "Rustenburg is home to ... the world's largest platinum refinery, PMR
    (Precious Metal Refiners), which processes around 70% of the world's platinum."
    https://en.wikipedia.org/wiki/Rustenburg
[4] Wikipedia, "Good Delivery" — Tanaka Kikinzoku Kogyo K.K. (Japan) als erkende raffinaderij.
    https://en.wikipedia.org/wiki/Good_Delivery
[5] Wikipedia, "London Platinum and Palladium Market" — Tanaka Kikinzoku Kogyo als market-maker.
    https://en.wikipedia.org/wiki/London_Platinum_and_Palladium_Market
[6] ja.wikipedia.org, "田中貴金属工業" — hoofdkantoor 東京都中央区日本橋茅場町2-6-6 (〒103-0025);
    fabriekslijst (Iwate/Gunma/Chiba ×2/Kanagawa ×3/Ibaraki). https://ja.wikipedia.org/wiki/田中貴金属工業
[7] Tanaka Precious Metals, bedrijfswebsite — bevestigt Nihonbashi/Kayabacho- en Ginza-historie van
    het hoofdkantoor (geen los adrespunt op deze pagina). https://www.tanaka.co.jp/
[8] `data/pgm.js` / `design/pgm.md` (dit project, v1-PGM-register) — Rustenburg PMR (Anglo American
    Platinum) als grootste PGM-raffinaderij ter wereld, kandidaat-coördinaat -25,95/27,30 (niet
    satelliet-gelegd — zie §7). `v2/design/pgm.md` (lokaal projectbestand).
[9] Esri World Imagery via `v2/tools/sat_check.py` (z12–z16) —
    `v2/build-cache/satcheck/sat-pgm-rustenburg-tokio-jnb-cargo-z16.png`,
    `sat-pgm-rustenburg-tokio-narita-cargo-z16.png`, `sat-pgm-rustenburg-tokio-tanaka-hq.png`,
    `sat-pgm-rustenburg-tokio-rustenburg-pmr.png`, `sat-pgm-rustenburg-tokio-rustenburg-wide.png`,
    `sat-pgm-rustenburg-tokio-rustenburg-ind1.png`, `sat-pgm-rustenburg-tokio-rustenburg-ind2.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `pgm-rustenburg-tokio`** → `v2/data/stroomroute-pgm-rustenburg-tokio.json` — 3 benen (truck fase B → lucht
fase B → truck fase C, stoppunt bij Tanaka), **13.835,3 km**, 4.513 punten, 4 markers, 92,5 KB. Recept:
`bak_stromen.sh` (functie `bak_pgm_rustenburg_tokio`); twee nieuwe wegprofielen
`pgm-rustenburg-tokio-rustenburg-jnb` en `pgm-rustenburg-tokio-narita-tanaka` in `maak_stroombeen_weg.py`; het
luchtbeen via `maak_luchtbeen.py` (geen profiel, geen slot nodig).

**⚠️ Vóóraf gecorrigeerd t.o.v. de eigen brief §7 (blokkade "eerst een betere coördinaat regelen"):** het
v1-registercoördinaat voor `pgm-rustenburg-pmr` (-25,9500, 27,3000) bleek volgens de brief zelf landbouwgrond, geen
raffinaderij. In plaats van een nieuwe satellietronde is het satelliet-gelegde Waterval-smelter/RBMR/PMR-
complex-anker (-25,6750, 27,3180) hergebruikt uit de drie zusterbrieven van dezelfde golf/grondstof
(`pgm-rustenburg-shanghai.md` — bron-gelegd, z16-z17 — plus `pgm-zimplats-rustenburg.md` en
`pgm-mogalakwena-londen.md`, die dat anker op hun beurt al overnamen/bevestigden). Conform de opdracht is de
brieftekst zelf (§1-§8) NIET aangepast; deze correctie staat alleen hier en in de kop van de bak-functie.

**b1 (truck, extract `zuid-afrika`, vensterKm 40, `eindToegangPrivaat`/`eindKlassen` gezet voor het
luchthaventerrein):** `maak_stroombeen_weg.py --profiel pgm-rustenburg-tokio-rustenburg-jnb --bron geofabrik` —
**178,0 km** geroute (getekende lijn 178,2 km incl. anker-verbindingsstukjes) over de vier via-punten uit §4
(Kroondal → Brits → Pretoria-West N4/N1 → Allandale N1/R21), 17 keerlussen gesnoeid (185,6 → 178,0 km).
Anker-verbindingsstukjes plant → weg 0,17 km, weg → kade 0,01 km (beide OK). First mile 6,71 km, last mile 1,64 km
over kleine wegklassen bij de twee uiteinden.

**⚠️ Lengtetoets BUITEN de norm (b1):** 178,0 km tegen ~120 km (ketenontwerp, brief §2) = **+48,3%**, ruim boven
het ±15%-venster. Bevestigt de zustermeting in `pgm-mogalakwena-londen.md` (dezelfde N4/N1/R21-corridor, eigen
OSRM-check 166 km tegen hetzelfde ~120 km-ontwerpcijfer) — de N4/N1/R21-corridor Rustenburg→OR Tambo is
structureel langer dan de gepubliceerde hemelsbreed-achtige schatting. Niet dichtgetrokken; geen via-punt
geschrapt of bijgeschoven.

**b2 (lucht, geen extract, geen slot):** `maak_luchtbeen.py --van "OR Tambo vrachtterminal|-26.1400,28.2300" --naar
"Narita vrachtterminal|35.7743,140.3797"` — **13.582,6 km** grootcirkel, 545 punten. Doorgetrokken, geen stippel
(bakhandleiding §2); `toets_rechte_benen.py` slaat dit been terecht over. Komt overeen met de brief-schatting
~13.600 km en met de claim in §0 dat dit de langste luchtafstand van de negen PGM/goud/diamant-ketens van deze
golf is. Geen tussenlanding getekend (brief §7: geen bron noemt een hub).

**b3 (truck, extract `japan`, reus-slot, vensterKm 40):** `maak_stroombeen_weg.py --profiel
pgm-rustenburg-tokio-narita-tanaka --bron geofabrik` — **74,5 km** geroute (getekende lijn 74,5 km) over de drie
via-punten uit §4 (Narita-IC → Chiba-kita IC → Ichikawa/Wangan-knoop), 22 keerlussen gesnoeid (75,1 → 74,5 km).
Anker-verbindingsstukjes plant → weg 0,02 km, weg → kade 0,00 km (beide OK). First mile 0,28 km, last mile 0,00 km.

**Lengtetoets b3 [OK, net binnen de norm]:** 74,5 km tegen ~65 km (ketenontwerp, brief §2) = **+14,6%** — net
buiten de ±10%-tool-waarschuwing maar binnen de ±15%-norm van de brief.

**Naden tussen de benen: 0,000 km** op beide overslagpunten (OR Tambo-vrachtterminal tussen b1/b2, Narita-
vrachtterminal tussen b2/b3) — de weg- en luchtprofielen delen letterlijk dezelfde ankercoördinaten.

**Toetsen:** `toets_knikken.py` — b1: (meegeteld in de gecombineerde bake, geen terugloop gemeld); b3: 27 knikken
≥60° (26 spikes + 1 echte scherpe bocht bij de Narita-IC-oprit, R 1-48 m), 1 omkering ≥150° en **0 TERUGLOOP**
(de enige klasse die reparatie vraagt). `toets_rechte_benen.py --min-km 5` — geen melding voor
`pgm-rustenburg-tokio` (beide truckbenen hebben een omwegfactor ruim boven 1,000; het luchtbeen wordt per
constructie overgeslagen). `json.load` slaagt: versie 2, `punt_formaat` lonlat, modaliteiten `truck`/`lucht`/
`truck` (alle drie ∈ de toegestane set), elk been ≥ 2 punten (2.064 / 545 / 1.904), bestandsgrootte 92,5 KB (ruim
onder ~300 KB).

**Toelichting stippels/haven-aanlopen/vluchten:** geen stippels — beide truckbenen zijn volledig doorgetrokken
over openbaar wegennet (geen last-mile-gat, geen airside-afsluiting gevonden ondanks `eindToegangPrivaat`). Geen
zeebeen dus geen haven-aanloop. Eén vlucht (b2, zie hierboven), doorgetrokken conform §2 van de bakhandleiding.

**Gereedschapslessen:** de PMR-anker-blokkade uit §7 loste zich op zonder nieuwe satellietronde — drie
zusterbrieven van dezelfde golf/grondstof hadden het Waterval-complex-anker al onafhankelijk satelliet-gelegd
("Bestaande ankers hergebruiken... ankers uit brieven van dezelfde grondstof in deze golf gelden ook" uit de
opdracht, hier letterlijk toegepast). `eindToegangPrivaat`/`eindKlassen` op b1 bleek niet strikt nodig (de scan
vond toch een doorgaand pad naar de vrachtterminal) maar kostte niets en is als voorzorg blijven staan. Beide
lengtetoetsen wijken af in dezelfde richting als de zusterbrief `pgm-mogalakwena-londen.md` op hetzelfde b1-traject
— een aanwijzing dat het ~120 km-ontwerpcijfer voor Rustenburg→OR Tambo structureel te laag is, niet een
incident van deze ene bake.

**Open punt dat blijft staan (ongewijzigd uit de brief):** `pgm-tanaka-tokio` is het Tanaka-hoofdkantoor/
handelsadres in Chuo-ku, geen bevestigd fabrieksterrein (brief §3/§7) — dit been is als stoppunt gebakken zoals de
brief het opgeeft, zonder die aanname te veranderen.
