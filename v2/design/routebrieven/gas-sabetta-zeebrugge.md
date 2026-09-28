# Gas · Sabetta (Rusland) → Zeebrugge (België)

**stroom-id:** `gas-sabetta-zeebrugge` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) ·
**status:** gebakken
**Keten in één zin:** Arctisch LNG van het Novatek-complex Yamal LNG in Sabetta, per ijsklasse-tanker de
westelijke, jaarrond-ijsvrije route langs de Barentszzee en Noorwegen naar de Fluxys LNG-terminal in
Zeebrugge, waar het losgelost/hervergast het Belgisch/NW-Europese gasnet in gaat.
**Welke as van het verhaal:** de reserve-as van het Arctische, seizoensgebonden verhaal — Yamal LNG is
al jaren écht gecontracteerd naar Zeebrugge (20-jarig transshipment-contract, tot 8 Mt/j) en Zeebrugge was
in 2025 de drukste Europese haven voor Russisch Arctisch LNG (58 schepen); tegelijk de kwetsbaarste as van
de zeven — sancties, ijsklasse-afhankelijkheid en sinds 27-3-2025 een EU-verbod op doorvoer (transshipment)
van Russische LNG bij Zeebrugge naar niet-EU-markten.

## 1 · Ketenkaart
```
Yamal LNG-complex Sabetta `gas-sabetta-lng` ──(b1 zee · haven-aanloop → Karische Zee/Barentszzee-kust
   (69-73°N) → Noorse kust zuidwaarts (66°N→54°N) → Noordzee → haven-aanloop · ~4.879,8 km, MARNET)──►
   Fluxys LNG-terminal Zeebrugge `gas-zeebrugge-lng`
   ──(b2 leiding · korte terreinleiding · 4,98 km, stippel — letterlijke kopie uit
      `gas-bonny-zeebrugge.md`)──►
   netinvoedingspunt `gas-zeebrugge-iuk` (Fluxys/Interconnector-zone) ── stoppunt
```
Fase A (South Tambey-gasveld → Sabetta, onshore trunkline) vervalt — zie §7.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | B | zee | Sabetta-kade → zeeknoop 4711 (71,34710/72,40350) | haven-aanloop, Ob-baai/Kara-kust | 14,4 [lokale zeeknoop-meting] | stippel — Esri/MARNET kent de Sabetta-kade niet | ja |
| b1 | B | zee | zeeknoop 4711 → zeeknoop 1629 (51,50000/3,40000) | Karische Zee → Barentszzee-kust → Noorse kust → Noordzee (westelijke, niet-Arctische route) | 4.844,9 [lokale MARNET-testroute, haalbaarheidstoets] | MARNET (kade→kade) | nee |
| b1b | B | zee | zeeknoop 1629 → Zeebrugge-kade | haven-aanloop | 20,5 [lokale zeeknoop-meting] | stippel — zelfde grensgeval als `gas-bonny-zeebrugge` b1b | ja |
| b2 | C | leiding | Fluxys-terminal Zeebrugge → netinvoedingspunt IUK | korte terreinleiding, Zeebrugge-industriezone | 4,98 [eigen meting, letterlijk hergebruikt uit `gas-bonny-zeebrugge.md`] | stippel — OSM-pijpleidingnet daar al getoetst: LNG-terminal en IUK-poort liggen op twee NIET-verbonden componenten | ja |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-sabetta-lng` | productie + laadkade (Yamal LNG-complex) | Yamal LNG, Sabetta (Novatek) | 71.2733, 72.0725 | [1][2][3][9] | bron-gelegd (z14 gezien: liquefactiecomplex met tankenpark, twee grote opslagtanks en twee steigers de baai in, met een tanker aangemeerd aan de oostelijke steiger — jetty-structuur duidelijk zichtbaar) |
| `gas-zeebrugge-lng` | losplek + regasterminal + transshipment-hub (Fluxys) | Fluxys LNG Zeebrugge | 51.3537, 3.2200 | [4][5][8] | bron-gelegd — anker LETTERLIJK hergebruikt uit `gas-bonny-zeebrugge.md` (z15/z16 gezien: 4 bolvormige LNG-tanks, tankenpark, twee steigers met laadarmen het LNG-dok in) |
| `gas-zeebrugge-iuk` | netinvoedingspunt (fase C-eind) | terrein "UK Gas Interconnector Terminal" (Fluxys-gaszone), Zeebrugge | 51.3156, 3.1822 | [8] | aannemelijk — anker letterlijk hergebruikt uit `gas-bonny-zeebrugge.md` |

## 4 · Via-punten
Niet van toepassing: b1 routeert via MARNET (geen corridorkeuze door ons te leggen, en de haalbaarheidstoets
bevestigt lokaal dat de router de Barentszzee-kust volgt in plaats van over de pool/land te snijden) en b2
is te kort (< 5 km) voor een corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Yamal LNG-complex Sabetta | Novatek 50,1% · Total 20% · CNPC 20% · Silk Road Fund 9,9% | pijpgas (South Tambey-veld) → LNG | 3 trains, 16,5 Mtpa nominaal + kleine Train 4 ≈ 17,4 Mtpa (peiljaar 2025) — ≈ 22,4-23,7 bcm/j (1 Mt≈1,36 bcm) | [2][3] |
| Fluxys LNG-terminal Zeebrugge | Fluxys | LNG (tanker) → hervergast pijpleidinggas + ship-to-ship-transshipment | 9 bcm/j nominale terminalcapaciteit; opslag 5 tanks (incl. nieuwe 180.000 m³-tank); Yamal-Fluxys-transshipmentcontract tot **8 Mt/j** (20-jarig, 2021) | [4][5] |

## 6 · Stoppunt
De brief stopt bij het netinvoedingspunt in de Zeebrugge-gaszone: net als bij `gas-bonny-zeebrugge` verdwijnt
de LNG-herkomst hier in het gemengde Belgisch/NW-Europese pijpleidingnet (of gaat als transshipment-cargo
verder de wereld op) — er is geen enkelvoudige "fabriek" die dit gas als eindproduct ontvangt, dus fase D/E
vervallen.

## 7 · Open punten
- **Fase A vervallen**: geen coördinaat gevonden voor het South Tambey-gasveld (Wikipedia/Nominatim geven
  geen puntlocatie op — het veld bestaat uit verspreide putlocaties, geen enkelvoudig traceerbaar tracé naar
  Sabetta). Conform "geen coördinaat verzinnen" blijft dit been ongetekend; de brief begint bij het
  liquefactiecomplex.
- **Zeebrugge-kade-grensgeval, zelfde als as 5** (haalbaarheidstoets-punt): b2 is een letterlijke kopie van
  de eerder gebakken `gas-bonny-zeebrugge`-leiding (4,98 km, stippel) — daar bleek het OSM-pijpleidingnet
  tussen LNG-terminal en IUK-poort uit twee NIET-verbonden componenten te bestaan.
- **Sabetta-haven-aanloop nieuw, nog niet gebakken**: bij `gas-bonny-zeebrugge` liepen beide haven-aanlopen
  (Bonny én Zeebrugge) vast op `timeout 300` (exit 124) en viel de bake terug op een rechte stippel; gezien de
  vergelijkbare afstand (14,4 km) en complexere kustlijn (baai, zandbanken) is bij Sabetta hetzelfde patroon
  aannemelijk — niet vooraf getest binnen deze brief.
- **Jaarvolume Sabetta→Zeebrugge specifiek niet los gebrond**: bekend zijn het totale nominale
  Yamal-exportvolume (17,4 Mtpa), het gecontracteerde Zeebrugge-transshipmentplafond (8 Mt/j) en het
  feitelijke 2025-verkeer (58 Yamal-cargo's bij Zeebrugge — meer dan alle Chinese havens samen; EU-breed
  15,1 Mt Yamal-import, ~76% van Yamal's wereldexport) — geen bron geeft een los Sabetta→Zeebrugge-tonnage.
- **Transshipmentban sinds 27-3-2025**: Russische LNG mag bij Zeebrugge niet meer worden doorgevoerd
  (ship-to-ship-transshipment) naar niet-EU-markten; rechtstreekse invoer in het Belgische/NW-Europese net
  (waar déze as over gaat) blijft toegestaan en ging door — H1-2025 al 3,3 bcm geïmporteerd, 61% ná de
  banddatum. Risico voor toekomstig volume, geen wijziging van de fysieke route.
- **Grote cirkel Sabetta–Zeebrugge is ~3.560 km**; de gemeten vaarbare MARNET-route (4.844,9 km) volgt
  bewust de kust in plaats van over de Noordpool, en ligt daarmee ruim onder de eerdere ontwerpschatting van
  6.000–6.500 km — bevestigd door de lokale haalbaarheidstoets (503 punten, 0 van 54 geteste edges
  afgekeurd wegens landkruising).

## 8 · Bronnen
[1] Wikipedia, "Sabetta" — locatie op het Jamal-schiereiland, coördinaat 71,2733/72,0725, poort + LNG-fabriek
Yamal LNG. https://en.wikipedia.org/wiki/Sabetta
[2] Wikipedia, "Yamal LNG" — eigendom Novatek 50,1%/Total 20%/CNPC 20%/Silk Road Fund 9,9%; 3 trains, 16,5
Mtpa nominaal; gevoed door het South (Yuzhno-)Tambeyskoye-gasveld; 180 km spoorlijn Bovanenkovo–Sabetta;
Zeebrugge als route wanneer ijs de Northern Sea Route blokkeert; 2025 EU-import 15,1 Mt (~76% van Yamal's
wereldexport); 2026 Hormuz-crisispiek jan–apr: 91 ladingen, 98% van exportvolume naar de EU.
https://en.wikipedia.org/wiki/Yamal_LNG
[3] `v2/design/gas-sitelaag.md` (anker `w-yamal-sabetta`, [B8]) — 17,4 Mtpa (3 trains + Train 4), coördinaat
Wikipedia-geohack, status was "aannemelijk" (nu opgewaardeerd naar bron-gelegd via eigen `sat_check.py`
in deze brief).
[4] Global Energy Monitor, "Zeebrugge LNG Terminal" — coördinaat 51,353/3,22241; terminalcapaciteit 9
bcm/j; opslag 5 tanks incl. nieuwe 180.000 m³-tank; Yamal-Fluxys-contract tot 8 Mt/j transshipment; 2022:
~90% van Yamal-transshipment ging naar niet-Europese markten. https://www.gem.wiki/Zeebrugge_LNG_Terminal
[5] Natural Gas World / Gasworld, "Yamal LNG and Fluxys sign long-term contract for LNG transhipment at
Zeebrugge Terminal" — 20-jarig contract, tot 8 Mt/j, voor jaarrond-levering vanaf het Jamal-schiereiland
naar Azië-Pacific wanneer ijs de Northern Sea Route blokkeert.
https://www.naturalgasworld.com/yamal-fluxys-zeebrugge-terminal-contract-for-lng-transhipment-22566
[6] FPS Economy (Belgische federale overheid), "Sanctions on the reloading of Russian LNG in Belgium" —
vanaf 27-3-2025 geen doorvoer/reload van Russische LNG meer toegestaan bij Zeebrugge; H1-2025 al 3,3 bcm
geïmporteerd, 61% ná de banddatum.
https://economie.fgov.be/en/themes/energy/sources-and-carriers-energy/natural-gas/sanctions-reloading-russian
[7] discoveryalert.com, "LNG terminals Europe 2026: energy infrastructure" — 58 Yamal-schepen bij Zeebrugge
in 2025 (meer dan alle Chinese havens samen, 51 schepen); EU-breed 15,1 Mt Yamal-import in 2025.
https://discoveryalert.com/lng-terminals-europe-2026-energy-infrastructure/
[8] `v2/design/routebrieven/gas-bonny-zeebrugge.md` — bron van de letterlijk hergebruikte ankers
`gas-zeebrugge-lng` en `gas-zeebrugge-iuk`, en van de leiding-stippel b2 (4,98 km, OSM-topologie getoetst:
twee gescheiden componenten).
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14) —
`v2/build-cache/satcheck/sat-gas-sabetta-zeebrugge-sabetta-lng.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Stroom `gas-sabetta-zeebrugge`** → `v2/data/stroomroute-gas-sabetta-zeebrugge.json` — 4 benen,
**4.889,0 km**, 587 punten, 3 markers. zee 17,7 (stippel) + 4.844,9 + 21,4 (stippel) = 4.884,0 km ·
leiding 5,0 km (stippel). Recept: `bak_stromen.sh` (functie `bak_gas_sabetta_zeebrugge`).
Bestand 11,5 KB.

**b1a (zee, stippel-geojson, haven-aanloop Sabetta):** anders dan verwacht (bij `gas-bonny-zeebrugge`
liepen beide aanlopen vast op `timeout 300`) SLAAGDE `maak_havenaanloop.py --van 71.2733,72.0725 --naar
71.34710,72.40350` hier gewoon, op de trap cel 0,005° kaal (minste land midden op de lijn): **17,7 km
over water, 63 punten**, tegen 14,4 km hemelsbreed (omwegfactor 1,234). 2,43 km van de lijn ligt op land,
maar uitsluitend aan het kade-uiteinde (0,00 km MIDDEN op de lijn) — dat is de 1:10M-kustkorrel (een kade
ligt per definitie óp de kustlijn), geen landkruising. `--stippel-geojson` i.p.v. de geplande rechte
terugval: betere geometrie, dezelfde kennisclaim (stippel blijft, "we weten dát het water is, niet waar
het schip vaart").

**b1 (zee, MARNET, kade→kade wordt knoop→knoop):** zeeknoop 4711 (71,34710/72,40350) → zeeknoop 1629
(51,50000/3,40000, identiek aan de knoop die `gas-bonny-zeebrugge` al gebruikt voor Zeebrugge) — snap
0,000 km aan beide zijden (de knopen zelf zijn het beginpunt). Resultaat **4.844,9 km over 36
MARNET-edges, 503 punten**, tegen de lokale haalbaarheidstoets van 4.844,9 km uit de bak-aanwijzing —
**exact gelijk**. De route volgt de Barentszzee-kust (69-73°N) en daalt zuidwaarts langs Noorwegen
(66°N→54°N) naar de Noordzee, precies zoals vooraf getoetst; geen doorsteek over de pool of over land.
Lengte-invariant: getekende lijn 4.844,927 km vs som edge-km 4.845,000 km = −0,073 km (de naden).

**b1b (zee, stippel-geojson, haven-aanloop Zeebrugge):** óók geslaagd — anders dan de twee mislukte
Zeebrugge-aanlopen bij `gas-bonny-zeebrugge` (beide `timeout 300`, exit 124) liep deze door op de trap
cel 0,01° kaal: **21,4 km over water, 19 punten**, tegen 20,5 km hemelsbreed (omwegfactor 1,044), **0,00
km over land** — geen enkele landkruising, ook niet aan het kade-uiteinde.
⚠️ **Gereedschapsles (eigen fout, gecorrigeerd vóór het eindrapport):** `maak_havenaanloop.py --van
<kade> --naar <zeeknoop>` schrijft het GeoJSON altijd in de volgorde kade→zeeknoop, en
`hecht_marnet.py --stippel-geojson` leest die punten LETTERLIJK in bestandsvolgorde in, zonder de
richting aan de reisvolgorde aan te passen (anders dan `--stippel`, dat de volgorde uit `--van`/`--naar`
opbouwt). Omdat b1b ná b1 komt (dat al op de zeeknoop eindigt) moest dit been in zeeknoop→kade-volgorde
staan; de eerste bake gaf daardoor een naad van 20,503 km tussen been 2 en been 3 (en dezelfde 20,503 km
tussen been 3 en been 4, want been 3's opgeslagen "laatste" punt was feitelijk de zeeknoop, niet de
kade). Gefixt door de punten-array van het eigen geojson-bestand
(`gas-sabetta-zeebrugge-aanloop-zeebrugge.geojson`) om te draaien vóór het herbakken — geen nieuwe
`maak_havenaanloop.py`-run nodig, dezelfde meting, alleen de opslagvolgorde. Ná de fix: naad 0,000 km
overal. **Zoek deze klasse bij elke toekomstige `--stippel-geojson`/`--been-geojson` die ná een ander
been in de keten komt** — de volgorde waarin `--van`/`--naar` aan `maak_havenaanloop.py` is gegeven
bepaalt de opslagvolgorde, niet de plek in de reisvolgorde.

**b2 (leiding, Zeebrugge-terrein, stippel, LETTERLIJKE KOPIE):** exact het been uit `gas-bonny-zeebrugge`
b2 hergebruikt (zelfde coördinaten, zelfde tekst) — **4,984 km, 2 punten**. Niet opnieuw getoetst: het
OSM-pijpleidingnet is daar al topologisch gecontroleerd (LNG-terminal en IUK-poort op twee NIET-verbonden
componenten).

**Toets naden:** alle vier de overgangen **0,000 km** (na de b1b-punten-fix hierboven).

**`toets_knikken.py`:** 3 knikken ≥60° (80,0° / 74,9° / 64,9°, allemaal "krappe bocht" op de MARNET-kust
langs Rusland/Noorwegen/België), **0 omkeringen, 0 terugloop**. Geen bevinding.

**`toets_rechte_benen.py --min-km 5`:** alleen b2 (de leiding-stippel, 5,0 km) komt naar voren als
"rechte lijn" — **verwacht en correct**, een gedocumenteerde letterlijke kopie zonder eigen meting. b1a
en b1b verschijnen NIET meer als rechte lijn (in tegenstelling tot de gebakken verwachting in de
bak-aanwijzing): omdat `maak_havenaanloop.py` hier een echt gekromd pad over water vond in plaats van een
rechte terugval, zijn het geen rechte benen meer — dat is een verbetering t.o.v. de aanname, geen
afwijking om te melden.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {zee, leiding} (binnen de
toegestane set), elk been ≥2 punten (minimum 2, het gemeten zeebeen 503), bestandsgrootte **11,5 KB**
(ruim < 300 KB).

**Markers:** alle drie op **0,0 km** van de lijn (het zijn de been-eindpunten zelf: gas-sabetta-lng,
gas-zeebrugge-lng, gas-zeebrugge-iuk).

**Gereedschapslessen:**
- De zeeknoop-lookup uit de brief (`bak_aanwijzingen`) kwam bij het bakken exact terug: Sabetta-kade
  14,4 km / zeeknoop 4711, Zeebrugge-terminal 20,5 km / zeeknoop 1629 (identiek aan `gas-bonny-zeebrugge`)
  — beide onafhankelijk herrekend vóór het bakken en identiek aan de brief.
- Twee haven-aanlopen die bij `gas-bonny-zeebrugge` allebei op `timeout 300` vastliepen, slaagden hier
  allebei — geen tegenspraak met die eerdere observatie, gewoon een andere kustgeometrie (Sabetta/
  Zeebrugge zijn andere coördinaten dan Bonny Island/Zeebrugge, en zelfs "dezelfde" Zeebrugge-kant kan
  op een andere trap slagen). **"Eerder mislukt" is geen voorspelling voor een volgende poging** — het
  blijft nodig om `maak_havenaanloop.py` gewoon te draaien in plaats van meteen op de rechte terugval te
  gokken.
- `--stippel-geojson` neemt de punten van het bestand LETTERLIJK over, zonder de richting te controleren
  tegen de rest van de keten — zie de b1b-les hierboven. Dit is geen bug in `hecht_marnet.py` (de tool
  documenteert "niet over deze graaf geroutet"), maar een aandachtspunt voor elke bak-agent die
  `maak_havenaanloop.py` ná een eerder been in de keten aanroept.
