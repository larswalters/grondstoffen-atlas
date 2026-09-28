# Routebrief (licht) · diamant — Gahcho Kué (Canada) → Yellowknife → Gaborone (Botswana)

**stroom-id:** `diamant-gahchokue-gaborone` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 4) ·
**status:** gebakken
**Keten in één zin:** ruwe diamant van de Gahcho Kué-mijn (De Beers Canada 51% / Mountain Province Diamonds
49%-JV, Northwest Territories, geen permanente weg) vliegt van de eigen mijnstrip naar Yellowknife Airport en
vandaar met één zeer lange interncontinentale vlucht naar Gaborone, waar De Beers zijn wereldwijde
sight-aggregatie/verkoop houdt (DTCB/DBGSS-campus, hergebruikt uit `diamant-gaborone-surat.md`).
**Welke as van het verhaal:** *reserve-as uit golf 3, hier alsnog gebouwd voor bredere Canadese dekking naast
het kwetsbare `diamant-ekati-antwerpen` (Ekati zelf zit sinds juli 2026 in receivership, zie die brief §7)* —
Canada ~14% wereldvolume (~16 Mct/jr Diavik+Ekati+Gahcho Kué samen, design/diamant.md §3a); Gahcho Kué's eigen
ontwerpcapaciteit ~4,5 Mct/jr over een geplande 11-jaar mijnlevensduur vanaf 2016 [3].

## BINDENDE aanpassing op het ketenontwerp (haalbaarheidstoets)
De toets stond activering afhankelijk van het sneuvelen van keten `diamant-ekati-antwerpen` — die keten is in
golf 3 wél gebakken, maar draagt een eigen zwaar risico (Ekati-receivership). Gahcho Kué is een **andere, nog
actieve mijn** (JV-partner De Beers Canada) en dekt daarmee een reëel deel van de Canadese productie dat de
Ekati-keten niet dekt; de as wordt daarom alsnog gebouwd voor bredere dekking, niet omdat keten 2 zelf faalde.
Conform de toets is **fase C toegevoegd** (GBE → DTCB/DBGSS, het ontbrekende laatste been) en is de aanname
"één directe vlucht" voor het zeer lange been B expliciet gedocumenteerd (zie §7) — beide zoals de toets eist.

## 1 · Ketenkaart
```
Gahcho Kué Aerodrome `dia-gahchokue-strip` ──(b1 lucht · grootcirkel · 287,7 km)──►
Yellowknife Airport (YZF), vrachtapron `dia-yzf-splitsing` (hergebruikt anker) ──(b2 lucht · grootcirkel ·
14.878,7 km, zeer lang — zie §7) ──► Sir Seretse Khama Intl Airport (GBE), vrachtapron `dia-gbe-cargo`
(hergebruikt anker) ──(b3 truck · A1/Western Bypass Gaborone · ~4 km, letterlijke kopie van
`diamant-gaborone-surat` b1, omgekeerde richting) ──► DTCB/DBGSS-campus `dia-gaborone-dtc` (hergebruikt anker)
── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | lucht | Gahcho Kué Aerodrome → Yellowknife Airport (YZF) | grootcirkel | 287,7 (gemeten); Wikipedia "approximately 280 km" [3] | maak_luchtbeen.py | nee — doorgetrokken |
| b2 | B | lucht | Yellowknife Airport (YZF) → Sir Seretse Khama Intl Airport (GBE) | grootcirkel, geen tussenlanding gebrond | 14.878,7 (gemeten grootcirkel); ontwerp noemde ~14.500 [1] | maak_luchtbeen.py | nee — doorgetrokken, zie §7 voor de aanname |
| b3 | C (nieuw, per aanpassing) | truck | GBE-vrachtapron → DTCB/DBGSS-campus, Gaborone | A1/Western Bypass Road, Gaborone — letterlijke kopie van `diamant-gaborone-surat-weg-dtc-gbe.geojson`, omgekeerde richting | 3,7 hemelsbreed (gemeten); zusterbeen mat 4,1–4,3 km wegkm [9] | letterlijke kopie (`voeg_been_toe.py`/hergebruikt geojson) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-gahchokue-strip` | mijnvliegveld (vertrekpunt lucht) | Gahcho Kué Aerodrome (grind-/ijsbaan naast het mijncomplex, Kennady Lake) | 63.43534, -109.14478 | [3][4][10] | bron-gelegd (z14 gezien: duidelijke rechte grindlandingsbaan direct ten oosten van het mijncomplex/de tailings aan Kennady Lake, exact zoals Wikipedia beschrijft; OSM-node `aeroway=aerodrome` "Gahcho Kue Aerodrome" 63.4353409/-109.1447850) |
| `dia-yzf-splitsing` | overslag lucht→lucht (sorteer-/splitsingsfaciliteit) | vrachtapron/GA-terrein oostzijde Yellowknife Airport (**hergebruikt anker**, `diamant-ekati-antwerpen.md`) | 62.46850, -114.42500 | [5][8] | bron-gelegd (hergebruikt; z15 in de zusterbrief gezien: hangaars + kleine vrachttoestellen op het GA-platform oostzijde). ⚠️ Een CBC-bron in de zusterbrief zegt dat Diavik/Gahcho Kué in één gebouw en Ekati in een ánder gebouw op hetzelfde terrein sorteren [8] — het exacte Gahcho Kué-gebouw is niet apart geadresseerd, zie §7 |
| `dia-gbe-cargo` | vrachtterminal (aankomst lucht, vertrek truck) | GBE-vrachtapron, Sir Seretse Khama Intl Airport (**hergebruikt anker**, `diamant-gaborone-surat.md`) | -24.5550, 25.9286 | [6][9] | bron-gelegd (hergebruikt; z18 in de zusterbrief gezien: loodsen + geparkeerde vrachttoestellen naast de start-/landingsbaan) |
| `dia-gaborone-dtc` | handels-/aggregatiehub (eindpunt) | DTCB/DBGSS-campus, Gaborone (**hergebruikt anker**, `diamant-gaborone-surat.md`) | -24.5859, 25.9144 | [7][9] | bron-gelegd (hergebruikt; z17 in de zusterbrief gezien: meerlagig kantoorgebouw + industrieterrein, OSM-landuse "Diamond Trading Company Botswana") |

## 4 · Via-punten
Geen — b1/b2 zijn luchtbenen (per constructie recht, geen via-punten); b3 is een letterlijke kopie van een
reeds gebakken stadsweg zonder corridorkeuze (`diamant-gaborone-surat.md` §4: "b1 heeft geen via-punten").

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| DTCB/DBGSS-campus, Gaborone | De Beers (DTC Botswana) | ruwe diamant van De Beers-JV-mijnen wereldwijd → gesorteerd/gewaardeerd, sight-allocaties aan sightholders | onbekend per mijn; hub sinds 2013 (verplaatst van Londen) [7] | [7][9] |

## 6 · Stoppunt
De brief stopt bij de DTCB/DBGSS-campus in Gaborone: dat is het opgegeven eindpunt van de reserve-as en het
punt waar de al bestaande keten `diamant-gaborone-surat` verder gaat naar de Surat-slijperij (26 Mct/jr,
gedeeld trechterverhaal) — die aansluiting is al getekend in een andere stroom, dus fase D vervalt hier om
dubbeling te vermijden.

## 7 · Open punten
- **⚠️ b2 is het zwakst gebronde been van deze keten, zoals de haalbaarheidstoets al voorspelde.** De gemeten
  grootcirkel YZF→GBE is **14.878,7 km** — ruim voorbij het realistische bereik van een vrachtvliegtuig zonder
  tussenstop (747-8F/777F ≈ 9.000-9.200 km). Geen bron noemt een specifieke hub (Amsterdam/Londen/
  Johannesburg/Dubai zijn allemaal plausibel); conform `bakhandleiding-licht.md` §2 ("Lucht": alleen een
  tussenlanding tekenen als een bron de hub noemt) is dit **één directe vlucht met die aanname expliciet
  hier vastgelegd** — in werkelijkheid gaat dit vrijwel zeker via minstens één tussenstop. Dit is een
  schematische claim ("van hier naar daar"), geen beweerde vliegroute.
- **De routering Gahcho Kué → Gaborone zelf is aannemelijk, niet per zending gebrond.** Geen bron zegt
  letterlijk "Gahcho Kué-rough gaat naar Gaborone". De aanname steunt op twee feiten: (1) De Beers Canada
  bezit 51% van de Gahcho Kué-JV [3], en (2) De Beers verplaatste zijn wereldwijde aggregatie/verkoop
  ("sights") in 2013 van Londen naar Gaborone (design/diamant.md §3c/§8) — sindsdien is Gaborone de
  standaardhub voor De Beers-eigen productie. Een andere bestemming (Antwerpen, zoals bij Namdeb toen
  Gaborone niet gebrond kon worden — zie `diamant-namdeb-gaborone.md`) is niet uit te sluiten.
- **`dia-yzf-splitsing` is een hergebruikt anker voor het verkeerde gebouw, mogelijk.** De CBC-bron in
  `diamant-ekati-antwerpen.md` zegt dat Diavik/Gahcho Kué in één sorteergebouw zitten en Ekati in een ander —
  het hergebruikte anker (uit de Ekati-brief) is dus zelf al alleen "aannemelijk" voor het algemene
  GA-vrachtplatform, niet voor een specifiek pand. Binnen het webbudget niet los te adresseren.
- **Gahcho Kué's mijnlevensduur:** de 2010-feasibility study projecteerde ~4,5 Mct/jr over 11 jaar vanaf de
  opening in 2016 — dat horizont loopt rond 2027 af [3]. Geen recentere bron (2025/2026) gevonden binnen het
  webbudget die bevestigt of de mijn nog in normale productie is of al richting sluiting gaat, zoals bij
  Ekati wél expliciet gevonden werd. Dit is dus een open risico, geen bevestigd feit zoals bij Ekati.
- **Jaarvolume:** geen Gahcho Kué-specifiek actueel productiecijfer gevonden; gebruikt is de
  ontwerpcapaciteit ~4,5 Mct/jr uit de 2010-feasibility study [3]. Canada-totaal (Diavik+Ekati+Gahcho Kué)
  ~16 Mct/jr, 14% wereldvolume, design/diamant.md §3a — met Diavik gesloten en Ekati in receivership ligt het
  actuele totaal waarschijnlijk fors lager (zelfde kanttekening als in de Ekati-brief).
- b3-km is een hemelsbrede meting van het hergebruikte ankerpaar, geen nieuwe wegscan; de bak-agent kan het
  bestaande geojson (`diamant-gaborone-surat-weg-dtc-gbe.geojson`) letterlijk in omgekeerde richting gebruiken
  in plaats van opnieuw te routeren.

## 8 · Bronnen
[1] Ketenontwerp (JSON, orchestrator-invoer, M31 golf 4, veld `as`) — `diamant-gahchokue-gaborone`, benen A/B met km-indicaties (~280 km, ~14.500 km).
[2] Haalbaarheidstoets (JSON, orchestrator-invoer, BINDEND, veld `toets`) — haalbaar: true; aanpassing: fase C toevoegen (GBE→DBGSS) + de "één directe vlucht"-aanname expliciet documenteren.
[3] Wikipedia, "Gahcho Kué Diamond Mine" — locatie (Kennady Lake, 63°26′04″N 109°11′10″W), "approximately 280 km east northeast of Yellowknife", De Beers Canada 51% / Mountain Province Diamonds 49%-JV, geopend 20-09-2016, ontwerpcapaciteit ~4.500.000 karaat/jr over 11 jaar, "served by Gahcho Kue Aerodrome". https://en.wikipedia.org/wiki/Gahcho_Ku%C3%A9_Diamond_Mine
[4] OpenStreetMap (ODbL) via Photon/Nominatim — node `aeroway=aerodrome` "Gahcho Kue Aerodrome", 63.4353409/-109.1447850. https://www.openstreetmap.org
[5] Wikipedia, "Yellowknife Airport" — coördinaten 62.46306/-114.44028 (kruiscontrole op het hergebruikte anker, dat op het oostelijke GA-vrachtplatform ligt, niet op het hoofdgebouw). https://en.wikipedia.org/wiki/Yellowknife_Airport
[6] Wikipedia, "Sir Seretse Khama International Airport" — coördinaten -24.55528/25.91833 (kruiscontrole op het hergebruikte anker `dia-gbe-cargo`). https://en.wikipedia.org/wiki/Sir_Seretse_Khama_International_Airport
[7] design/diamant.md §3c/§8 — Gaborone/DTCB/DBGSS als De Beers-aggregatie/verkoophub sinds de beneficiation-verplaatsing van Londen naar Botswana (2013); intern ontwerpdocument.
[8] `v2/design/routebrieven/diamant-ekati-antwerpen.md` — hergebruikt anker `dia-yzf-splitsing` (62.46850/-114.42500) + de CBC-bron over gescheiden sorteergebouwen Diavik/Gahcho Kué vs. Ekati bij Yellowknife Airport.
[9] `v2/design/routebrieven/diamant-gaborone-surat.md` — hergebruikte ankers `dia-gbe-cargo` (-24.5550/25.9286) en `dia-gaborone-dtc` (-24.5859/25.9144); het gebakken wegbeen-geojson `diamant-gaborone-surat-weg-dtc-gbe.geojson` (4,3 km) voor letterlijk hergebruik in b3.
[10] Esri World Imagery via `v2/tools/sat_check.py` (z14, live) — `v2/build-cache/satcheck/sat-diamant-gahchokue-gaborone-strip.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 4)

**Stroom `diamant-gahchokue-gaborone`** → `v2/data/stroomroute-diamant-gahchokue-gaborone.json` — 3 benen (2
lucht doorgetrokken, 1 truck doorgetrokken), **15.170,7 km**, 709 punten, 4 markers, 15,4 KB. Recept:
`bak_stromen.sh` (functie `bak_diamant_gahchokue_gaborone`); geen nieuw wegprofiel (b3 is een letterlijke
kopie); twee luchtbenen met `maak_luchtbeen.py`, volgens `bakhandleiding-licht.md` §2 "Lucht". Geen zeebeen,
geen haven-aanloop.

**b1 (lucht, `maak_luchtbeen.py`):** Gahcho Kué Aerodrome (63,43534/-109,14478) → YZF (62,46850/-114,42500) —
**287,7 km** grootcirkel, 13 punten. Doorgetrokken; exact de gemeten waarde uit de brief, tegen Wikipedia
"approximately 280 km" (brief §2/§8[3]) — geen km-toets voor een luchtbeen (bakhandleiding §5).

**b2 (lucht, `maak_luchtbeen.py`):** YZF (62,46850/-114,42500) → GBE (-24,55500/25,92860) — **14.878,7 km**
grootcirkel, 597 punten. Doorgetrokken; ZEER LANG, ver voorbij het realistische bereik van een vrachtvliegtuig
zonder tussenstop (747-8F/777F ≈ 9.000-9.200 km). Geen bron noemt een specifieke tussenlandingshub → ÉÉN
DIRECTE VLUCHT aangenomen conform bakhandleiding §2, aanname expliciet gedocumenteerd in brief §7.

**b3 (truck, LETTERLIJKE KOPIE, omgekeerde richting):** GBE-vrachtapron (-24,5550/25,9286) →
DTCB/DBGSS-campus (-24,5859/25,9144) — **4,3 km** (99 punten), gekopieerd uit
`diamant-gaborone-surat-weg-dtc-gbe.geojson` (stroom `diamant-gaborone-surat`, been b1, functie
`bak_diamant_gaborone_surat`) met de puntenvolgorde omgedraaid, geen nieuwe wegscan. Doorgetrokken, geen
via-punten (zelfde stadsweg zonder corridorkeuze als het origineel). Het origineel toetste zichzelf al:
4,1 km wegkm tegen 3,7 km hemelsbreed = +10,8% (binnen ±15%, zie `diamant-gaborone-surat.md` §9).

**Toetsen:** `toets_knikken.py` — b1/b2 (lucht) 0 knikken; b3 (truck) **5 knikken ≥60°, alle spikes (R 5-42 m),
0 omkeringen, 0 terugloop** — identiek aan de 5 spikes die het origineel `diamant-gaborone-surat` b1 al droeg
(zelfde geometrie, alleen de puntenvolgorde is omgedraaid); geen nieuwe bevinding, bestaand kenmerk van het
gekopieerde been. `toets_rechte_benen.py --min-km 5` — geen melding voor deze stroom (beide luchtbenen worden
per constructie overgeslagen — grootcirkel; het truckbeen is 4,3 km, onder de 5 km-drempel). `json.load`
slaagt: versie 2, `punt_formaat` lonlat, modaliteiten `lucht`/`truck` ∈ toegestane set, elk been ≥ 2 punten
(13–597), bestandsgrootte 15,4 KB (ruim onder ~300 KB). Naden tussen alle drie opeenvolgende benen: **0,000
km**. Markers: alle 4 op 0,000 km van hun lijn (elk anker is óók een been-eindpunt).

**Toelichting stippels/haven-aanlopen/vluchten:** geen stippels in deze keten. Twee vluchten (b1, b2), beide
doorgetrokken grootcirkels tussen satelliet-gelegde/hergebruikte vrachtterminals; b2 draagt de zwaarste
aanname van de keten (één directe vlucht over 14.878,7 km, zie brief §7) — dat blijft zo staan, want geen bron
noemt een tussenlandingshub. Geen haven-aanloop nodig: geen zeebeen in deze keten.

**Lessen/open punten:** (1) de literal-copy-werkwijze uit `bakhandleiding-licht.md` werkt zonder aanpassing
ook in omgekeerde richting — reverse van `geometry.coordinates` plus het omdraaien van `van`/`naar` en
`snapVanKm`/`snapNaarKm` in de properties volstaat, geen nieuwe scan nodig; (2) een gekopieerd been erft de
knikken van zijn origineel — die horen niet apart gerepareerd te worden, ze zijn al bevinding in de
brontstroom; (3) b2 blijft het risicovolste been van de hele M31-golf-4-reserve-as (zie brief §7, open punt
over de ontbrekende tussenlandingshub).
