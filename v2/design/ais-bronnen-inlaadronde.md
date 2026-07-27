# De inlaadronde — vier AIS-bronsporen, eerlijk afgerekend (fase 1 van M28)

*Uitgevoerd 2026-07-27. Vier bouwers hebben parallel elk één bron ingeladen; vier
sceptische toetsers hebben elk spoor daarna met eigen scripts nagerekend. Dit document is
de overdracht naar fase 2 (de track-graaf, LAR-530).*

*Wat ik voor dít document zélf heb gemeten in plaats van overgenomen: de vijf tracksets in
§6 (tracks/km/punten/MMSI/bytes/tijdspanne, uit de bestanden op schijf), de
punt-tot-punt-tabel in §7 (8.000 tracks per set), het knip-lek in alle vijf de sets, de
Deense Class A/B-verhouding en stilligger-fractie op de ijkdag, de AMSA-stilliggerfractie
over alle vier de maanden, de Noorse ping-cadans, de aanwezigheid van 2026-03-12 in de
Noorse ruwe brokken, de tijdspanne van het VPS-deelbestand, en de twee betwiste
codepaden in `bouw_tracks.py`. Waar bouwer en toetser elkaar tegenspreken staan **beide**
getallen mét een oordeel en de reden.*

## Wat er nu ligt, en wat niet

1. **Vijf tracksets: 768.032 tracks / 55.072.062 km / 119.995.512 punten / 1.046,5 MB** —
   VS, Denemarken, Australië, Noorwegen (3 corridors) en de eigen wereld-collector.
2. **Drie nieuwe converters** (`haal_dma.py`, `haal_amsa.py`, `haal_kystdatahuset.py`) in
   het `haal_marinecadastre.py`-patroon; `bouw_tracks.py` is **byte-voor-byte ongewijzigd**.
3. **Twee sporen zijn volledig geslaagd** (Denemarken 4/4 toetsen, VPS-collector), **twee
   deels**: Australië faalt de lengtetoets (−8,0%) én levert 0 tracks met de ongewijzigde
   `bouw_tracks.py`; Noorwegen leverde 26 van 28 dagen.
4. **Nog niet gedaan:** géén van de vier nieuwe sets staat op de bol of in de graaf; EuRIS
   en GFW wachten op twee accounts (§8); **niets is gecommit** — vier nieuwe/gewijzigde
   bestanden staan als werkkopie klaar.
5. **De harde uitkomst van deze ronde:** vier van de vijf bronnen hebben een korrel van
   0,25-0,45 km en zijn dus edge-geometrie; AMSA is met 20,4 km mediane puntafstand ~80×
   grover en wordt corridor-/dekkingslaag (§7).

---

## 1 · Denemarken — DMA (Danish Maritime Authority)

**Gebouwd:** `v2/tools/haal_dma.py` (nieuw, untracked). Anonieme S3-bucket `aisdata.ais.dk`
→ bucket-listing (welke dagen bestaan écht) → hervatbare download met 0-byte-val op
**grootte** → streamend uitpakken uit de zip (de ~3,5 GB CSV per dag raakt nooit de schijf)
→ collector-JSONL. Dragende ontwerpkeuze: **dunnen naar één positie per MMSI per minuut**,
omdat `bouw_tracks.py` in hele minuten rekent en alles daarbinnen zelf weggooit. Dat
scheelt een factor 5 aan volume zonder informatieverlies stroomafwaarts, en maakte een
aanpassing aan `bouw_tracks.py` overbodig.

**Trackset:** `build-cache/ais/tracks/dk-landelijk.jsonl.gz` — **28 aaneengesloten dagen
(2026-06-27 t/m 2026-07-24), 170.654 tracks / 10.593.105 km / 40.437.626 punten /
23.362 MMSI / 353,1 MB**.
**Ruwe cache:** 28 dagbestanden (4,08 GB) + 28 bronzips (21,78 GB) in
`build-cache/ais/dma/` (gitignored) — de zips blijven staan zodat een rijker recept nooit
een nieuwe download kost.

**Acceptatie — vier van vier GESLAAGD:**

| toets | uitkomst |
|---|---|
| a. Sont (Helsingør–Helsingborg) | **4.420 doorvaarten / 2.457 schepen** over poortlijn 56,03 N; op de oorspronkelijk genoemde 55,70 N: 8.759 / 2.889 (daar telt het Kopenhagen/Malmö-verkeer mee) |
| b. Grote Belt bij de brug | **3.481 doorvaarten / 2.027 schepen** over 55,33 N; bonus Kleine Belt 2.028 / 1.520 |
| c. Kattegat (56,0-57,5 N / 10,5-12,0 O) | **18.374 tracks / 6.218 schepen** |
| d. **LENGTETOETS** Rødby–Puttgarden (gepubliceerd 19 km / 45 min) | mediaan **18,86 km** (bouwer) / **18,89 km** (toetser) = **−0,8 / −0,6%**; tweede as: 43-44 min kruisvaart tegen 45 gepubliceerd |

**Wat de toetser ervan vond: BEVESTIGD.** Hij hergebruikte niets — eigen scripts, eigen
poort-, vak- en veerbootimplementatie — en reproduceert a/b/c **cijfer voor cijfer**. Drie
dingen wegen zwaar:

- Hij bewees de klassieke stille fout **uit** in plaats van hem aan te nemen: alle 28
  bestanden byte-gescand, **105.926.367 regels, waarvan 105.926.367 een `time_utc` dragen in
  precies de vorm die de `strptime` van `bouw_tracks.py` accepteert én met de datum van hun
  eigen dagbestand — 0 uitzonderingen**. Regels min statisch = 105.694.308 posities = exact
  wat pass 1 las. Losse controle: alle 3,6 mln regels van 2026-07-24 écht door `strptime`
  gehaald, 0 onparseerbaar.
- Hij hermat het `km`-veld uit de punten op 17.065 tracks: mediane afwijking 0,025 km, max
  0,107 km.
- **De sterkste validatie zat er al in en was niet opgemerkt:** aan de Grote-Beltpoort
  kruisen COLOR FANTASY, COLOR MAGIC, STENA GERMANICA en STENA SCANDINAVICA elk **exact 28
  keer in exact 28 dagen** — vier dagelijkse lijndiensten. Dat toetst geometrie én kalender
  in één. Tweede ijkpunt op een andere schaal: Helsingør–Helsingborg, 4.232 overtochten,
  mediaan 4,84 km langs de track tegen 4,95 km hemelsbreed, met TYCHO BRAHE 1.251× en
  AURORA AF HELSINGBORG 1.247× = ~45 overtochten per schip per dag (het echte rooster). Eén
  ijkpunt op 19 km kan een proportionele schaalfout verbergen, twee (4 en 19 km) niet.
- Eigen georeferentietoets die de bouwer niet deed: 7,58% van de monsterpunten valt binnen
  NE 1:10M-land; 0,5° noord verschoven wordt dat 38,4% en 0,5° oost 34,7%, en de al
  geaccepteerde VS-set scoort in dezelfde toets 49,9% (binnenrivieren zijn "land" op 1:10M).
  De coördinaten kloppen dus fijnmazig.

**Waar ze elkaar tegenspreken:**

- **Class A/B-verhouding — omgedraaid.** Bouwer: "54,6% Class B, 45,4% Class A". Toetser
  (exacte telling over 28 dagen): **A 55.971.468 = 52,96% · B 49.722.840 = 47,04%**.
  *Zelf geteld op de ijkdag 2026-07-24: 1.817.821 Class B tegen 1.774.753 Class A =
  50,6% / 49,4% van de 3.592.574 posities.* **Geloof de toetser voor de hele set** (hij
  telde alles; mijn dagmeting ligt tussen beide en weerlegt de 54,6% in elk geval). Wat er
  echt staat: **ruwweg half-half, met Class A licht in de meerderheid** — en dat is een
  fase-2-feit, want Class B is pleziervaart en geen vrachtgeometrie (§7.3).
- **Dunningsfactor.** Bouwer 5,8× (uit een monster van 90 minuten), toetser **5,05×**
  (18.128.460 geldige posities → 3.589.174 unieke MMSI-minuten op een volle dag).
  **Geloof de toetser**; een monster van 90 minuten is te klein voor een dagfactor.
- **Stilligger-aandeel — hier heeft de toetser het mis.** Hij verklaart de puntenval
  (105,7 mln posities → 40,4 mln trackpunten = 38,3% retentie) met "46,4% van de posities
  heeft SOG < 0,5". *Zelf gemeten op de ijkdag: 2.262.732 van 3.580.160 posities met een
  SOG-waarde = **63,2%** stilliggend.* Dat sluit rekenkundig veel beter: 36,8% varend tegen
  38,3% retentie. **De conclusie van de toetser (geen stil verlies, de val is ontwerp)
  klopt en wordt hiermee sterker; zijn percentage niet.**
- **Hemelsbrede kade-kade-afstand.** Bouwer 18,85 km (en "+0,0%" daartegen), toetser
  18,33 km uit de werkelijke ligplaatsnaderingen. **Geloof de toetser**, maar de
  vergelijking die telt (18,86-18,89 km tegen 19 km gepubliceerd) houdt in beide gevallen.
- **Afstandsbakken naar Denemarken** (117.947 / 46.456 / 4.901 / 1.225 / 125 tegen
  116.766 / 47.867 / 4.936 / 991 / 94). **Neem geen van beide als feit over:** "afstand van
  Denemarken" is nergens gedefinieerd, dus de bakken zijn maatafhankelijk. Beide
  partitioneren netjes 170.654 en beide geven dezelfde vórm — overweldigend <250 km met een
  staart van ~100 tracks boven 1.000 km. Wat wél exact reproduceert: **95,28% van de tracks
  en 97,76% van de km heeft zijn zwaartepunt in het DK-kernvak** (53-59,5 N / 3-16 O).
- **Eenheden.** "3,8 GB gegzipt" is GiB; decimaal is het 4,08 GB. De 21,78 GB aan zips is
  wél decimaal correct.

**⚠️ Substantiële vondst van de toetser — de bron is groter dan gemeld en de tool kan er
niet bij.** Het rapport zegt "bucket bevat 513 dagbestanden, oudste 2025-02-27"; het
eerdere bronnenonderzoek zei "2006→". De toetser las de hele bucket uit: **1.095 keys** =
513 root-dagbestanden **plus 210 maandarchieven in jaarmappen** (`2006/aisdk-2006-03.zip`
t/m `2024/aisdk-2024-02.zip`, samen ~3.493 GB), plus losse dagen onder `2024/`. *Zelf
nagekeken in de code:* `bucket_dagen()` matcht
`<Key>aisdk-(\d{4}-\d{2}-\d{2})\.zip</Key>` — een key met jaarprefix én maandvorm valt daar
per constructie buiten. **Dus: `--lijst` toont een archief van 17 maanden en de
beschikbaarheidscheck weigert élke dag vóór 2025-02-27 als "niet in de bucket" terwijl de
data er staat.** Een echte beperking van onze tool, gepresenteerd als eigenschap van de
bron. Reparatie = één regex.

**⚠️ Tijdzone is afgeleid, niet gedocumenteerd bevestigd.** De gezaghebbende README uit de
bucket zelf (`!_README_information_CSV_files.txt`) documenteert de kolommen en de
dd/mm/yyyy-vorm maar **zegt niets over de tijdzone**. Kruisverificatie tegen onze eigen
collector is onmogelijk: de datavensters overlappen niet (DMA loopt t/m 07-24, de collector
begint 07-25). Wat er wél is: een diurnale toets die beide partijen onafhankelijk
reproduceren — varende pleziervaart (type 36/37) gaat op zondag 2026-07-19 van 1.008 (uur
00) via 2.669 (03) en 21.037 (06) naar de piek 40.996 (09) en terug naar 1.037 (22), bij
Deense zonsopgang 03:00 UTC en zonsondergang 19:20 UTC; vracht/tankers blijven als controle
vlak over alle 24 uur. Dat past op UTC-labels en niet op CEST. **Alle vier de
acceptatiecijfers zijn invariant onder een constante verschuiving** (drie zijn puur
geometrisch, de vierde is een tijdvérschil), maar een latere tijdgebonden koppeling met de
collector-data is dat niet. De dd/mm/yyyy-omzetting is wél onweerlegbaar: de ruwe rijen van
2026-07-24 lezen `24/07/2026 00:00:00` — dag 24 > 12, dus geen dubbelzinnigheid.

**Overige eerlijkheid uit het bouwersrapport:** één regel van 687,5 mln kreeg
`NavigationalStatus=null` (de schrijfwijze `AIS-SART (active)` stond niet in de tabel; de
meldregel logde hem netjes, effect op de tracks nul). En een **zelf geïntroduceerd
schemadefect dat halverwege is hersteld**: de eerste versie schreef Deense tékst door voor
`NavigationalStatus`/`ShipType` terwijl NOAA en de echte aisstream-collector nummers
leveren — een stroomafwaartse toets `NavigationalStatus == 5` zou voor DK stil False geven.
Gevonden na 3 dagen, run gestopt, mapping toegevoegd, die dagen opnieuw omgezet; de
28-daagse set is volledig met de gecorrigeerde code gemaakt (geverifieerd: int of null).

**Bronvuil dat ongefilterd in de set staat:** 94 (toetser) tot 125 (bouwer) tracks liggen
verder dan 1.000 km van Denemarken, geclusterd op **inlandse Russische coördinaten**
(54,17 N / 33,22 O bij Smolensk; 59,13 N / 34,54 O), alle op MMSI 273xxxxxxx. Dat is de
bekende Baltische GPS-spoofing-signatuur, geen converterfout — maar het staat wel in
`dk-landelijk.jsonl.gz` (§7.3).

---

## 2 · Australië — AMSA (Craft Tracking System)

**Gebouwd:** `v2/tools/haal_amsa.py` (nieuw, untracked). Scrapet de id→maand-mapping van de
échte downloadpagina (163 maanddumps, 2012-09 t/m 2026-06), POST met `TermsAccepted`,
Content-Length-controle + 4 pogingen, geneste zip → punt-shapefile via `pyshp` →
collector-JSONL. Ondersteunt beide AMSA-schema's.

**Trackset:** `build-cache/ais/tracks/au-landelijk.jsonl.gz` — **4 maanden (2026-03-01 t/m
2026-06-30), 42.614 tracks / 15.489.056 km / 853.639 punten / 8.193 MMSI / 10,4 MB**,
gebouwd met **KNIP_MIN=90** (in-memory override vanuit `haal_amsa.py`; `bouw_tracks.py` is
aantoonbaar byte-identiek aan HEAD).
**Ruwe cache:** 382,3 MB zips + 183,7 MB collector-JSONL = 566,0 MB.

**Acceptatie — twee GESLAAGD, één GEFAALD:**

| toets | uitkomst |
|---|---|
| a. Newcastle (kolenhaven, ≤50 km) | **2.162 tracks** — GESLAAGD (toetser reproduceert exact; Brisbane 3.177 · Geelong 2.486 · Melbourne 2.279 · Gladstone 1.481 · Port Kembla 1.122 · Hay Point 849) |
| b. Port Hedland (ijzererts, ≤50 km) | **1.528 tracks** — GESLAAGD (toetser exact; Dampier 1.725, 16 tracks end-to-end tussen beide) |
| c. **LENGTETOETS** Spirit of Tasmania, Devonport↔Geelong (gepubliceerd 242 zeemijl = 448 km) | **412,4 km = −8,0%** (bouwer) / **412,6 km = −7,9%** (toetser) — **GEFAALD** |

**⚠️ De hoofdbevinding, door bouwer én toetser gedraaid en niet beredeneerd: met de
ongewijzigde `bouw_tracks.py` (KNIP_MIN=30) levert deze bron 0 tracks uit 7.746.422
pings.** AMSA dunt zelf naar één positie per schip per uur — hun eigen metadata-PDF in de
zip legt onder *Lineage* vast dat opeenvolgende positierapporten minimaal 60 minuten uit
elkaar liggen. Dat is géén bug in `bouw_tracks.py`; 30 minuten is juist voor VS/EU.
**Het besluit over per-bron KNIP staat in §7.2.**

**Wat de toetser ervan vond: DEELS.** De kern houdt stand: hij las de trackset zelf uit
(42.614 / 853.639 / 15.489.056 km, uit de geometrie herrekend 15.489.054), draaide de
KNIP_MIN=30-run zelf (0 tracks uit 7.746.422 pings in 102 s), haalde alle 7,75 mln
tijdstempels door de letterlijke `strptime` (0 fouten), las de 2 GiB-afkapping uit de
zip-central-directory + DBF-kop (2026-03/04/05 elk exact 2.147.484.154 byte = 2³¹+506),
haalde `--lijst` live tegen AMSA (163 maanddumps) en **verifieerde de referentie
onafhankelijk via het web** (242 zeemijl én vaartijd 9-11 uur staan echt gepubliceerd). Hij
deed er een niet-circulaire geometrietoets bij, want de bbox-toets van de bouwer is bijna
tautologisch: **0 van 853.639 punten in drie dozen midden in de Australische woestijn**,
terwijl Bass Strait 3,90% en de Pilbara-kust 3,13% van alle punten dragen. En de
identiteit van de veerlijn is hard: 4 MMSI, waarvan 2 samen 128 van de 130 oversteken
dragen = ~64 per schip over 122 dagen = een dagelijkse tweeschepen-dienst.

**⚠️ Waar ze elkaar tegenspreken — en hier zit het belangrijkste defect van de hele ronde:**

- **ONVERMELD DEFECT: de knip lekt. 4,94% van de geleverde kilometers overbrugt een gat dat
  geknipt had moeten worden.** *Zelf hermeten op het geleverde bestand en de toetser
  reproduceert tot op de eenheid:* **35.659 van 811.025 segmenten (4,397%) overspannen een
  gat > KNIP_MIN (90 min) en dragen 765.365 km = 4,94% van de 15.489.056 km. 17.402 van de
  42.614 tracks (41%) bevatten er minstens één; 1.391 gaten zijn langer dan 24 uur, 302
  langer dan 7 dagen (36.685 km), het ergste 92,1 dagen — en de langste enkele sprong in de
  set is 7.546,6 km**: een rechte lijn dwars over de Indische Oceaan, getekend alsof hij
  gevaren is.
  *Mechanisme, in de code nagekeken (`bouw_tracks.py`, regels 190-199):* een stilliggende
  ping (`sog < VARE_GRENS`) doet `laatste_ping = t_min` en dan `continue` — hij **ververst
  de gat-referentie maar komt nooit in de track**. Een schip dat 92 dagen uit dekking valt
  en wiens eerste ping terug stilliggend is, wordt daarna getoetst tegen die stilliggende
  ping (62 min) in plaats van tegen het laatste punt ín de track (132.555 min): geen knip.
  **Eerlijke attributie:** dit is een latente fout in `bouw_tracks.py` zélf, niet iets dat
  de bouwer schreef, en hij heeft dat bestand terecht niet aangeraakt. Maar twee
  AMSA-specifieke feiten laten het hier hard bijten en het rapport zwijgt over beide:
  uurkorrel maakt KNIP_MIN maar ~1,5 bemonsteringsinterval breed, en AMSA is
  stilligger-zwaar (70,4%, zie hieronder). **KNIP_MIN van 30 naar 90 zetten VERBREEDT het
  venster waarin een stilliggende ping een gat kan overbruggen — de gekozen override maakt
  dit lek dus erger, niet beter.** "De tracks zijn geometrisch schoon" is waar over bbox en
  over land, niet over tijdcontinuïteit. Hoe erg het in de andere sets is: §7.2.
- **Puntafstand "~37 km" is ~2× mis.** *Zelf gemeten over alle 811.025 segmenten: gemiddeld
  **19,10 km**, mediaan 20,45, p90 30,45.* De toetser meet hetzelfde. De ~37 komt uit
  km-per-track gedeeld door ongeveer de helft van de punten. Voor de Spirit of Tasmania
  zélf is ~40 km wél juist, dus de koorde-diagnose voor díe route blijft staan — maar als
  datasetbreed getal is het onwaar en het laat de bron grover klinken dan hij is.
- **De tijdkorrel-kopcijfers komen uit 6% van de data**, en juist uit de maand die het
  rapport zelf een regressie noemt. Voor 2026-06 reproduceert de toetser ze exact (p10 46 ·
  p25 57 · p50 **60** · p75 62 · p90 79 · p95 112 · p99 479 min · 5,2% ≤ 30 min), maar over
  alle 7.690.085 intervallen is de mediaan **65 min en slechts 0,3% ≤ 30 min** (de drie
  oudere maanden: 0,0%). De richting van de fout is conservatief — de echte data is nóg
  dunner, wat de 0-tracks-conclusie versterkt — maar het gepresenteerde getal beschrijft de
  dataset niet.
- **De −8% blijft onverklaard genoeg om de toets gefaald te laten.** De bouwer
  diagnosticeert koorde-verkorting en onderbouwt dat met een monotone trend op puntdichtheid
  (10 punten → 408,8 km · 11 → 413,3 · 12 → 416,9 · 15 → 418,7); de toetser reproduceert die
  monotonie in eigen meting (398,4 → 404,9 → 409,6 km) en voegt toe dat de gemeten 412,6 km
  **8% bóven** de hemelsbrede koorde van 382,0 km ligt, dus het pad is echt gebogen en niet
  een rechte streep. **Oordeel: de diagnose is aannemelijk, maar een verklaring repareert
  geen meting — de toets is en blijft gefaald**, en beide partijen presenteren hem zo.
- Kleinigheden zonder gevolg: 140 vs 130 oversteken en Dampier 1.725 vs 1.657 (andere
  terminalcoördinaat).

**Bronschade die niet aan ons ligt.** (1) 2026-03/04/05 zijn door AMSA zelf **afgekapt op de
dBASE-grens van 2 GiB**: de DBF-kop belooft 2.713.739 / 2.601.223 / 2.618.631 records,
aanwezig zijn er 2.421.064 → **10,8% / 6,9% / 7,5% weg**, gelijkmatig over de maand
verdeeld (alle 31 dagen van mei aanwezig). (2) **2026-06 is een regressie aan hun kant:
83,5% van de records heeft geen `craft_id`** (2.452.945 van 2.936.215), dus juni levert
483.270 bruikbare posities tegen ~2,42 mln per oudere maand — netto zijn de afgekapte oude
maanden véél bruikbaarder dan de nieuwste, en `--recent N` pakt juist de slechtste.
(3) Er is **geen MMSI, naam, IMO of roepnaam** (AMSA verwijdert die velden); `craft_id` is
een surrogaatsleutel en een *getekende* int32, dus de tool doet `& 0xFFFFFFFF` (bijectie).
(4) Twee onverenigbare schema's met een 12-uurs/24-uursval: t/m 2026-05 is `AM/PM`
betekenisvol, vanaf 2026-06 is het loos (bewezen: het aantal records met uur 00-11 is exact
gelijk aan het aantal "AM"). Eén regel dekt beide; verkeerd toegepast staat de halve
dataset 12 uur verkeerd — onzichtbaar op de kaart, maar de tracks vlechten.

**Licentie, en dat is een besluit voor Lars:** Creative Commons
Attribution-Noncommercial 3.0 Australia. AMSA eist letterlijk de vorm "© AMSA 2013" →
HUD-tekst *"© AMSA 2013 — Australian Maritime Safety Authority, Craft Tracking System
(CC BY-NC 3.0 AU)"*. De NC-clausule past bij de atlas, maar **legt de hele atlas op
niet-commercieel vast zolang deze laag meedraait.**

---

## 3 · Noorwegen — Kystdatahuset (Kystverket)

**Gebouwd:** `v2/tools/haal_kystdatahuset.py` (nieuw, untracked).
`POST /ws/api/ais/positions/within-bbox-time`, **anoniem, géén token**. Het antwoord is een
naamloze 12-koloms array die empirisch is gedecodeerd en gecontroleerd door kolom 7 ≈
kolom 9 / kolom 8 naar knopen om te rekenen (22.916 gecontroleerde rijen kloppen, 0 niet).
Drie valkuilen staan in de kop: het tijdvenster is **[start−23 u, end+1 u]** (server-side,
door de toetser live bevestigd), een ontbrekende dagtabel geeft **HTTP 200 mét
`success:false` en Postgres-fout `42P01`**, en het archief loopt ~4 maanden achter.

**Trackset:** `build-cache/ais/tracks/no-corridors.jsonl.gz` — **26 van 28 dagen
(2026-02-18 t/m 2026-03-17), 9.038 tracks / 301.581 km / 1.120.987 punten / 927 MMSI /
7,7 MB** over drie boxen (oslofjord 3.510 / bergen 5.104 / narvik 424).
**Ruwe cache:** 208,2 MB collector-JSONL + 204,9 MB ruwe API-antwoorden.

**Acceptatie — zeven GESLAAGD, één GEFAALD:**

| toets | uitkomst |
|---|---|
| Contract uitgezocht zónder auth | GESLAAGD — 118 swagger-paden, `security: None` op het bbox-endpoint, en door de toetser met **eigen tokenloze requests** nagedaan. Alleen `/ws/api/ship/data/...` geeft 401, en dat is niet nodig (`statinfo` levert naam/type/maten/diepgang óók anoniem) |
| Maximum per request gemeten i.p.v. gehardcodeerd | GESLAAGD — 6-daagse brok = 1.490.629 rijen zonder afkapping, geen 429 in ~60 requests; brokgrootte 4 dagen gekozen als geheugen-afweging |
| Tijdstempel overleeft de `strptime` van `bouw_tracks.py` | GESLAAGD — toetser: 0 vormfouten en 0 parse-fouten op **alle** 11.596.607 regels, 0 dubbele (mmsi,tijd) |
| Plausibiliteit per box | GESLAAGD — narvik is aantoonbaar het ertsbeen (Capesize 288-292 m, diepgang 18,17-18,32 m; type 70 grootste groep) |
| **LENGTETOETS** Moss–Horten (gepubliceerd 10,5 km / 30 min) | GESLAAGD — bouwer mediaan **10,31 km (−1,8%)**, toetser onafhankelijk **10,29 km (−2,0%)**, p10/p90 10,16/10,66; hemelsbreed kade-kade 9,50 km, dus de meting onderscheidt zich aantoonbaar van een rechte streep |
| Geen kruisbesmetting tussen de boxen | GESLAAGD (maar bijna tautologisch: de boxen zijn disjunct en de API knipt server-side) |
| Bestaande data onaangeraakt, niets gecommit | GESLAAGD |
| **Volledige 4 weken** | **GEFAALD — 26 van 28 dagen geleverd** (zie hieronder: 27 zijn terug te halen) |

**Wat de toetser ervan vond: DEELS.** De data en de hoofdmetingen kloppen exact — posities
per box 6.346.135 / 4.912.242 / 338.230, statisch 3.520 / 4.645 / 476, tracks 9.038 / km
301.581 / punten 1.120.987, per box 3.510/342/170.140 · 5.104/583/125.368 · 424/72/6.072.
Hij zette de lengtetoets van nul op met eigen kadecoördinaten en eigen
overvaart-segmentatie. **Hij loste bovendien het openstaande tijdzonepunt op, in het
voordeel van de bouwer:** de 8 laatste afvaarten in data-uur 23 vallen **alle acht op een
zaterdag om 23:01-23:03** = 00:01-00:03 CET, precies de gepubliceerde weekendafvaart van
24:00; eerste ochtendafvaart 03:47 data = 04:47 CET (gepubliceerd ~04:45). **De tijdkolom
is UTC, onafhankelijk bewezen.** De puntenval (11,60 mln pings → 1,12 mln trackpunten) is
volledig verklaard en géén parse-verlies: de bovengrens "unieke (mmsi,minuut) met SOG ≥ 0,5"
is 1.138.369 en de set benut daar **98,5%** van.

**⚠️ Waar ze elkaar tegenspreken — twee correcties die een besluit raken:**

- **"2 van de 28 dagen zijn onhaalbaar" is onjuist: 2026-03-12 staat al op schijf en is
  weggegooid.** De brok `*-20260313-20260313` bevat 03-12 van 01:00 t/m 23:59 voor alle drie
  de boxen (303.465 + 188.412 + 10.235 = 502.112 ruwe rijen), maar `zet_om()` knipt elke
  brok op zíjn eigen dagen. *Zelf nagekeken op het narvik-brok: 22.461 rijen, waarvan
  **10.235 met datum 2026-03-12** en 12.226 met 03-13 — exact het getal van de toetser.*
  Het **mechanisme** in het rapport is juist (een direct verzoek voor 03-12 loopt óók stuk
  op `42P01` van tabel `ais_20260311`), maar de **conclusie** niet: **27 van 28 dagen zijn
  in huis, alleen 03-11 mist echt in de bron.** De reparatie is client-side en gratis: voor
  een brok die op een gat volgt, is de kopdag door geen andere brok gedekt en mag de knip
  niet.
- **"De bron is gedund tot 1 positie per schip per 2-3 minuten" is onjuist — en de
  gevolgtrekking die eraan hing is dus precies omgekeerd.** Bouwer noemt dit probleem 4 en
  concludeert "voor kadeprecisie (LAR-531) mogelijk te grof". *Zelf gemeten op het
  narvik-bestand, 338.152 intervallen per MMSI gesorteerd: **mediaan 10 s**, p10/p25 3/4 s,
  p90 30 s, p99 821 s, **90,2% ≤ 30 s**.* De toetser meet hetzelfde langs een andere weg
  (7,15 pings per actieve schip-minuut in de Oslofjord ≈ 1 per 8 s). **Dit is vrijwel volle
  AIS-cadans; schrap probleem 4.** Wat je in de trackset ziet (0,265 km per punt) komt
  doordat `bouw_tracks.py` op hele minuten kwantiseert, niet doordat de bron dun is. →
  **Voor kadewerk is dit juist de fijnste bron die we hebben.**
- Bijzaken die niet reproduceren, alle drie in het nadeel van de bouwer: **unieke MMSI per
  box** 405/656/80 (rapport) tegen 399/641/78 in de bestanden — *zelf op narvik geteld: 78*;
  de gerapporteerde getallen zijn de rúwe rijtelling inclusief de weggeknipte kopdag, dus ze
  beschrijven de download en niet het bestand. **Narvik-ertstelling** is een óndertelling:
  23 schepen ≥150 m in plaats van 11, waarvan **8** Capesize van 288-292 m met diepgang
  18,17-18,32 in plaats van 6 (EREIKOUSSA en LOWLANDS SPIRIT erbij) — de inhoudelijke claim
  wordt er sterker van. En "196 MB ruw" is MiB; werkelijk 204,9 MB.
- **Twee toetsen bewijzen minder dan ze suggereren.** De Ofotfjord-meting (25,5 km gevaren
  tegen 24,6 km hemelsbreed) heeft geen externe ijking — dat is de tracks tegen hun eigen
  koorde; de bouwer zegt dat zelf en legde de gepubliceerde-afstandstoets terecht op
  Moss–Horten. En `security: None` is zwak bewijs voor anonimiteit: álle opgevraagde
  endpoints melden dat, inclusief het endpoint dat 401 geeft — de conclusie rust op de
  echte tokenloze requests, niet op de spec.
- **Niet verifieerbaar en dat blijft zo:** alle doorlooptijden (16,5 min / 7,6 min / 149 s)
  en per-verzoek-kosten laten geen spoor op schijf na.

**De box past niet om het ertsbeen.** De opdracht noemde "Narvik-haven naar open zee,
~40 km", maar de narvik-box stopt bij 16,80 O — ongeveer 26 km ten oosten van waar de
vaarweg naar Vestfjorden verder loopt. Die ~40 km is met deze box **niet toetsbaar**; de
bouwer meldt dat zelf en deed de lengtetoets elders.

---

## 4 · De eigen collector op de VPS

**Gewijzigd (niet gecommit):** `v2/tools/haal_ais_data.py` — één gerichte fix: `LOKAAL` wees
naar `build-cache/ais/tracks`, de **uitvoer**map van `bouw_tracks.py`; opgehaalde dagen
zouden daar tussen de gebakken tracksets landen en `bouw_tracks.py --bron` zelfverwijzend
maken. Nu `build-cache/ais/vps`. Plus `v2/design/ais-collector-vps.md` (pad gelijkgetrokken
+ twee waarschuwingen). De toetser las de diff: 8 regels + 14 regels, niets anders geraakt.

**Trackset:** `build-cache/ais/tracks/wereld-collector.jsonl.gz` herbouwd van 10,3 → 16,1 MB
— **35.216 tracks / 1.263.316 km / 1.682.909 punten / 24.211 MMSI**, uit 7.290.239 pings in
101 s.

**⚠️ Wat de groottevergelijking meteen ving:** de lokale `2026-07-26.jsonl.gz` was 312,7 MB
tegen 348,9 MB op de VPS — een eerdere kopie was afgebroken en **36,2 MB (10,4%) ontbrak
stil**, acht uur onopgemerkt. Alleen de bytevergelijking zag het. De trackset waartegen
wordt afgezet was dus op incomplete data gebouwd.

**Acceptatie — alle punten geslaagd volgens het rapport, met één gat in de opzet:**

| toets | uitkomst |
|---|---|
| Tijdstempelvorm op echte data | GESLAAGD — alle drie de positiesoorten aanwezig; toetser: parse faalt op 702 van 9.092.937 regels = 0,008%, gemeten over **alle vier** de bestanden |
| Nieuwste afgesloten dagen binnen, groeiende dag gerespecteerd | GESLAAGD — 3 dagen byte-identiek aan de VPS (toetser via eigen SSH bevestigd), 07-27 apart als `-deel` |
| Aantoonbaar meer data (voor → na) | tracks 23.766 → **35.216** (+48,2%) · MMSI 18.325 → 24.211 · km 794.799 → **1.263.316** (+59,0%) |
| Rotterdam-Rijnmond | 1.433 → **1.918** tracks (+33,8%) |
| Rijn-corridor tot Duisburg | 1.209 → **1.596** tracks (+32,0%) |
| **Wesel-gat** | **NIET dichtgelopen** — 0 trackpunten tussen lon 6,44 en 6,64, 0 tracks overspannen de strook, 34,6 km hemelsbreed, 149 schepen aan béide kanten gezien maar nooit binnen één doorlopende track |
| Schijf op de VPS | 96 GB / 21 GB vrij / 79-80% vol; aangroei door de toetser twee uur later onafhankelijk hermeten: **0,581 MB/min = 837 MB/dag** tegen 0,590 = 844 → ~24 dagen marge |
| **LENGTETOETS** | **ONTBRAK** — geen van de tien acceptatiepunten is een lengtetoets; achteraf door de toetser gedaan |

**Wat de toetser ervan vond: DEELS.** De metingen zijn ongebruikelijk sterk: ruim twintig
kerncijfers reproduceren tot de eenheid, inclusief de vier ruwe pings op Wesel-hoogte
(lat 51,6474-51,6579 / lon 6,5893-6,6048), de pass-1-telling 7.290.239 en de bbox. Hij
ontleedde de puntenval van 77% en sloot de stille fout uit: 7.290.239 pings → 1.928.826
varend (26,5%) → **1.827.621 unieke (mmsi, minuut) én varend = de harde bovengrens** →
uitvoer 1.682.909 = **92,1% daarvan benut**. Geen parse-verlies, alleen filterwerk. Ook:
0 van 1.682.909 punten niet-oplopend in tijd, `km`-veld tegen de geometrie max 0,048 km af,
en de vier bronbestanden sluiten naadloos aaneen (3,60 + 14,15 + 9,85 + 6,78 uur = exact de
totale spanne, **nul overlap, nul gat**).

**⚠️ Waar ze elkaar tegenspreken:**

- **De tijdspanne is met factor 1,6 overschat.** Bouwer: "ca. 2,3 dagen materiaal" en "4
  pings op ca. 55 uur". *Zelf gemeten, twee keer: de trackset loopt van 2026-07-25 20:23
  t/m 2026-07-27 06:46 UTC = **34,4 uur = 1,43 dagen**, en het bronbestand
  `2026-07-25.jsonl.gz` loopt van 20:23:17 tot 23:59:58 = **3 uur 37 min** (173.834
  regels) — een deeldag die als hele dag is geteld.* Het rapport spreekt zichzelf tegen: de
  eigen tabel noemt **35 uurvakken**. Gevolg: de Wesel-hermeting rust op 60% minder
  materiaal dan gemeld; de winst t.o.v. de 12,5-uursmeting is **2,75×**, niet 4,4×. **De
  Wesel-conclusie blijft overeind** — 0 trackpunten in de strook en 0 overspannende tracks
  zijn absolute uitkomsten, en aan beide kanten was 35 uurvakken lang onafgebroken verkeer.
- **"Vier schepen" zijn twee schepen in een venster van vier minuten:** de 4 pings op
  Wesel-hoogte komen van 2 MMSI (244029543 en 211123690), alle tussen 02:32:09 en 02:36:32
  UTC op 26 juli. De bouwer noemt het zelf inconclusief; "hooguit vier schepen" is formeel
  een bovengrens maar verhult dat het één voorbijvaarmoment is.
- **De verplichte lengtetoets ontbrak, en slaagt alsnog.** De toetser deed hem tegen
  gepubliceerde rivierkilometers: **Nijmegen (rkm 884,6) → Rees (837,5), verwacht 47,1 km,
  gemeten mediaan 47,0 km over 20 tracks = −0,3%**; Nijmegen→Emmerich −4,3% en
  Emmerich→Rees +5,5% (kortere spannen, dus de snap-onzekerheid van ~0,45 km weegt
  relatief zwaarder). **De geometrie is dus aantoonbaar goed — maar dat is het bewijs van de
  toetser, niet van de bouwer.**
- **Het dubbeltel-risico van de deeldag treedt niet op.** Het rapport waarschuwt dat
  `2026-07-27-deel.jsonl.gz` straks 6,8 uur dubbel laat tellen zodra de volle dag binnenkomt,
  en de toetser noemt de val "echt en ongeborgd" op grond van de bestandsnaamvergelijking.
  *Zelf de code nagelezen: `bouw_tracks.py` pass 2 doet `rijen.sort()` (regel 177) en daarna
  `if huidig and huidig[-1][2] == t_min: continue` (regel 202) — een gedupliceerde ping
  draagt per definitie dezelfde `t_min`, staat na het sorteren náást zijn tweeling en wordt
  weggegooid.* **Beide waarschuwingen zijn dus half waar: het bestand wordt echt twee keer
  gelezen (leestijd), maar de geometrie verandert niet.** Opruimen blijft nette hygiëne en
  voorkomt verwarring; de gemelde faalwijze is het niet.
- **Niet meer na te rekenen, en dat is een echt verlies:** alle voor-cijfers (23.766 tracks
  / 18.325 MMSI / 794.799 km / 1.074.444 punten / 10,3 MB en de vier venstercijfers). De
  bouwer bakte netjes naar `wereld-collector.nieuw.jsonl.gz` maar hernoemde daarna **over**
  de oude set; er is geen back-up en de map is gitignored. Alleen "23.766 tracks" en
  "Rijnmond→Duisburg 3.195" hebben een papieren spoor in de M28-banner van `CLAUDE.md`. De
  veilige-bouwdiscipline beschermde tegen een mislukte run, niet tegen het verlies van
  auditbaarheid. **Alle voor→na-percentages hierboven rusten dus op een getal dat niemand
  meer kan controleren.**

**Methodefout die de bouwer zelf meldde en die iedereen raakt die Wesel opnieuw meet:**
tellen per 0,1° lon-bak binnen de lat-band 51,15-52,10 husselt riviervakken door elkaar,
want de Rijn loopt onder Duisburg noord-zuid. De 5.435 pings in bak 6,6 en de 36.518 in bak
6,7 liggen op lat ~51,2-51,5 — dat is Duisburg-zuid, Krefeld en Düsseldorf, **niet Wesel
(51,655)**. De toetser bevestigde de lat-bereiken. De tabel in `memory/bugs-and-risks.md`
lijdt aan hetzelfde. **Meet op TRACKS in een smal Rijn-venster, niet op een lon-rechthoek.**

**⚠️ Een gedocumenteerd feit kantelt hiermee:** de M28-banner in `CLAUDE.md` zegt dat het
Wesel-gat "is dichtgelopen". Dat is met 2,75× meer materiaal, door bouwer én toetser
onafhankelijk, **weerlegd**. Banner en `bugs-and-risks.md` moeten worden gecorrigeerd.

---

## 5 · WAT LEEG BLEEF OF FAALDE

Geen verhulling; dit is de complete lijst.

1. **AMSA-lengtetoets: −8,0% en dus GEFAALD.** Spirit of Tasmania meet 412,4-412,6 km tegen
   448 km gepubliceerd. Koorde-verkorting is een aannemelijke diagnose (monotone trend,
   door beide partijen gemeten) maar repareert de meting niet.
2. **AMSA levert 0 tracks met de ongewijzigde `bouw_tracks.py`** — gedraaid, niet
   beredeneerd, door bouwer én toetser: 7.746.422 pings → 0 tracks bij KNIP_MIN=30. De bron
   is door AMSA zelf op één positie per schip per uur gedund. → besluit in §7.2.
3. **De geleverde AMSA-set draagt een knip-lek:** 4,94% van de km (765.365 km) overbrugt een
   gat > 90 min, tot 92,1 dagen en 7.546,6 km in één rechte sprong. Latente fout in
   `bouw_tracks.py`, door AMSA's uurkorrel uitvergroot.
4. **Noorwegen leverde 26 van de 28 gevraagde dagen.** Dagtabel `ais_20260311` bestaat niet
   in de bron (HTTP 200 + `42P01`) en is **niet vanaf onze kant te repareren**. Maar
   **2026-03-12 staat wél op schijf** in de al gedownloade brokken en is door onze eigen
   dagknip weggegooid: 27 van 28 dagen zijn gratis terug te halen.
5. **Noorwegen: het archief loopt ~4,3 maanden achter** (laatste dag 2026-03-17, gemeten op
   2026-07-27). Gevolg: **geen tijdoverlap met onze eigen collector**, dus een kruiscontrole
   tussen die twee bronnen is deze ronde onmogelijk geweest.
6. **Noorwegen: de narvik-box dekt het ertsbeen niet volledig** — hij stopt bij 16,80 O, dus
   de opgegeven ~40 km Narvik → open zee is niet toetsbaar.
7. **Denemarken: de tijdzone is afgeleid, niet gedocumenteerd.** De README van de bron zwijgt
   erover; het bewijs is diurnaal en dus een gevolgtrekking. Alle acceptatiecijfers zijn
   invariant, een latere tijdgebonden koppeling niet.
8. **Denemarken: onze tool kan niet bij 210 maandarchieven** (2006-03 t/m 2024-02, ~3.493 GB)
   die wél in de bucket staan. `--lijst` toont een archief van 17 maanden en weigert elke dag
   vóór 2025-02-27. Toolbeperking, geen broneigenschap.
9. **Denemarken: 94-125 spoofing-tracks staan ongefilterd in de set** (inlandse Russische
   coördinaten bij Smolensk, MMSI 273xxxxxxx).
10. **VPS: het Wesel-gat is NIET dichtgelopen** — 0 trackpunten tussen lon 6,44 en 6,64, 0
    overspannende tracks, 34,6 km hemelsbreed, 149 schepen aan beide kanten gezien. Dat
    weerlegt de M28-banner.
11. **VPS: de voor-cijfers zijn onherstelbaar onauditbaar** (oude trackset overschreven,
    geen back-up, gitignored), en het rapport bevatte geen lengtetoets.
12. **EuRIS: de gehoopte uitkomst is er niet.** Tracks v3 heeft **geen historie-endpoint**, en
    de twee endpoints die een token eisen (`followed`/`owned`) geven volgens de documentatie
    uitsluitend je eigen/gevolgde schepen. Een account ontsluit dus **géén tracks van
    derden**; een token koopt alleen een hogere rate limit (hoeveel hoger staat nergens).
    Posities van derden komen anoniem wél terug maar zonder identiteit: **14 van 1.842 tracks
    hadden een MMSI (0,8%)**. EuRIS is daarmee een poller of een dichtheidsbron, geen archief.
13. **EuRIS: trackId-stabiliteit is maar 16,1 minuten gemeten**, niet over een etmaal — 99,0%
    behouden en **0 nieuwe id's** t.o.v. de basis, wat sterk is maar een cyclus per etmaal
    niet uitsluit (de docs noemen het veld letterlijk "Randomized"). Dit is de enige echt
    openstaande vraag, en hij kost **geen account**.
14. **EuRIS: dode sporen, gemeten.** `locks`, `bridges`, `berthlines`, `berthareas`,
    `risindex`, `TracksV2`, `lockstatus` en `bridgestatus` geven alle **0 features**, ook
    zonder bbox-filter → de doorvaarthoogte uit sluizen/bruggen blijft onbekend. En
    `tracks/fairway-section` geeft 200 met lat/lon = 0,0.
15. **EuRIS: de dekking is niet uniform** — Bulgarije ontbreekt volledig in de vaarweglaag;
    de kadelijnen missen **Nederland en Duitsland** helemaal. Reken niet op een homogeen
    Europees bestand.
16. **GFW: alles zit achter 401**, zelfs `/v3/datasets`. Alle quotagetallen (50.000/dag,
    1.500.000/maand, max 5 tokens) komen uit documentatie en zijn **niet gemeten**.
17. **De EuRIS-Rijn-lengtetoets is niet conclusief** (+7,1% tegen een zelfgekozen, ambigue
    referentie van ~1.233 km). Niet als bewijs gebruiken, in geen van beide richtingen. De
    Donau-toets slaagt wél: 2.471,6 km over 273 secties tegen 2.414 km bekend = **+2,4%**.
18. **Niets staat op de bol, niets in de graaf, niets gecommit.** `bak_aistracks.py` en de
    HUD-laag in `aistracks.js` kennen alleen de VS-variant.

---

## 6 · Alle tracksets die er nu liggen

*Zelf hermeten uit de bestanden op schijf (`scratchpad/meet_sets.py`), niet uit de
rapporten overgenomen. Periode = eerste en laatste trackpunt, in UTC.*

| pad (`v2/build-cache/ais/tracks/`) | bron | periode (UTC) | dagen | tracks | km | punten | MMSI | MB |
|---|---|---|---|---|---|---|---|---|
| `vs-landelijk.jsonl.gz` | MarineCadastre (NOAA/USACE), heel VS incl. binnenrivieren | 2025-06-29 .. 2025-07-26 | 28 | **510.510** | **27.425.004** | 75.900.351 | 44.793 | 659,2 |
| `dk-landelijk.jsonl.gz` | DMA, S3 `aisdata.ais.dk` | 2026-06-27 .. 2026-07-24 | 28 | **170.654** | **10.593.105** | 40.437.626 | 23.362 | 353,1 |
| `au-landelijk.jsonl.gz` | AMSA Craft Tracking System, maanddumps | 2026-03-01 .. 2026-06-30 | 122 | **42.614** | **15.489.056** | 853.639 | 8.193 | 10,4 |
| `no-corridors.jsonl.gz` | Kystdatahuset, 3 boxen (oslofjord/bergen/narvik) | 2026-02-18 .. 2026-03-17 | 26 van 28 | **9.038** | **301.581** | 1.120.987 | 927 | 7,7 |
| `wereld-collector.jsonl.gz` | eigen aisstream-collector (VPS, wereldabonnement) | 2026-07-25 20:23 .. 2026-07-27 06:46 | **1,43** | **35.216** | **1.263.316** | 1.682.909 | 24.211 | 16,1 |
| **totaal** | | | | **768.032** | **55.072.062** | **119.995.512** | | **1.046,5** |

Twee dingen bij deze tabel:

- **De km-velden zijn geen verzinsel.** Voor elke set is de lengte uit de puntenlijst
  herrekend, door de toetsers en steekproefsgewijs door mij: AU 15.489.032 km tegen
  15.489.056 in de velden, DK mediane afwijking 0,025 km per track (max 0,107),
  collector max 0,048 km per track.
- In dezelfde map staan ook `mississippi.json` (146,8 MB) en `ohio-illinois.json`
  (52,0 MB). Dat zijn **geen tracksets** maar de vensterbakken van de VS-pilot
  (`{"venster":[...],"bron":"marinecadastre","tracks":[...]}`), overblijfselen van vóór
  het besluit om zonder vensters te werken. Ze staan buiten de tabel en buiten de graaf.

---

## 7 · Wat dit betekent voor FASE 2 (de track-graaf)

### 7.1 De beslissende maat: punt-tot-punt-afstand BINNEN de tracks

De hoofdsessie heeft dit zelf gemeten, per bron, over 8.000 tracks per set. **Ik heb het
onafhankelijk nagerekend met eigen code en kom tot op het cijfer op dezelfde tabel uit**
(n = 2,32 mln segmenten voor DK, 1,50 mln VS, 1,00 mln NO, 374k collector, 150k AU):

| bron | mediaan | p90 | aandeel ≤ 0,5 km |
|---|---|---|---|
| DK (DMA) | **0,249 km** | 0,46 | **92,3%** |
| NO (Kystdatahuset) | **0,265 km** | 0,46 | **92,4%** |
| VS (MarineCadastre) | **0,269 km** | 0,66 | **81,5%** |
| collector (wereld) | **0,453 km** | 1,73 | **53,7%** |
| AU (AMSA) | **20,430 km** | 30,13 | **1,9%** |

En op de ruwe AMSA-maand 2026-06, gesplitst op snelheid (alleen paren waarvan **beide**
punten varen): een schip ≥ 5 kn springt **landelijk mediaan 21,51 km per stap**, en **ook
binnen de havenvakken — Newcastle 13,73 km, Port Hedland 15,07 km**. De 2-3 km die je in
die vakken ziet als je *niet* op snelheid splitst zijn **wachtende schepen op de
ankerplaats (0,5-5 kn)**, geen fijne bemonstering in de geul. Grootste sprong tussen twee
opeenvolgende AMSA-punten in die maand: **592,7 km**. AMSA's eigen metadata-PDF verklaart
het: "a minimum time interval between successive vessel position reports of 60 minutes".

### 7.2 De besluiten

**BESLUIT 1 — DK + NO + VS + collector gaan de track-graaf in als EDGE-GEOMETRIE.** Met een
korrel van 0,25-0,45 km beschrijven die vier de **gevaren geul**, en dat is precies waar de
Vidalia-toets op stond: de échte gevaren lijn van één schip mat **−0,1%** tegen de
gepubliceerde afstand, terwijl de celgraaf **−7,4%** gaf en door Lars "onrealistisch hoekig"
werd genoemd. Vier bronnen met dezelfde korrel als de bron die die toets haalde, mogen dus
dezelfde rol krijgen.

**BESLUIT 2 — AU/AMSA gaat NIET de graaf in als edge-geometrie, maar als CORRIDOR-/
DEKKINGSLAAG:** welke kustlanen bestaan, plus het **satelliet-bereik offshore dat onze eigen
collector mist**. Reden in één regel: **een koorde van 20 km is aantoonbaar slechter dan de
celcentra die al waren afgekeurd** (de celgraaf werkte op ~500 m cellen en gaf al −7,4%).
Een AMSA-segment van 20,4 km snijdt elke bocht af en kan per definitie geen kade halen.

**BESLUIT 3 — De KNIP moet per bron meeschalen met de korrel van die bron.** Bij AMSA levert
KNIP_MIN=30 **nul** tracks uit 7,75 mln pings (gemeten). Nodig is **~3 uur**, en **STIL_MAX
van 90 min naar enkele uren** — bij één ping per uur is een stop van 90 minuten domweg
onzichtbaar.

**Waarom de knip niet cosmetisch is, en dit is de kern:**

- **De snelheidsguard is blind voor precies de fout die telt.** `MAX_KNOPEN = 40` knipt een
  onmogelijke sprong. Maar een schip dat 6 uur uit dekking valt en 130 km verderop terugkomt
  vaart 11,7 kn — volkomen plausibel. De guard laat het dus door, en je tekent **een rechte
  lijn van 130 km alsof hij gevaren is**. Dat is geen ruis in de statistiek: in de graaf
  wordt zo'n lijn een edge, en een router kiest hem juist graag omdat hij kort en recht is.
- **Zonder knip lassen aankomst en de volgende reis aan elkaar en verdwijnt het eindpunt** —
  en dat eindpunt is het terminal-node-materiaal van LAR-531 (Vidalia: **55 tracks
  eindigen** binnen 3 km van de Syrah-kade).
- **En het lek bestaat nu al, in alle vijf de sets.** *Zelf gemeten (NO en collector
  volledig, DK en VS op de eerste 20.000 tracks):*

  | bron | segmenten met gat > 90 min | aandeel van de km | ergste gat | langste enkele sprong |
  |---|---|---|---|---|
  | AU (AMSA) | 35.659 = 4,397% | **4,94%** | 92,1 dagen | **7.546,6 km** |
  | collector | 557 = 0,034% | 0,15% | 1,1 dag | 189,3 km |
  | NO | 310 = 0,028% | 0,40% | 19,0 dagen | 109,2 km |
  | VS | 649 = 0,019% | 0,29% | 17,0 dagen | **633,7 km** |
  | DK | 641 = 0,014% | 0,43% | 16,6 dagen | 334,4 km |

  De vier fijne bronnen dragen dus **0,15-0,43% van de km** in zulke segmenten — verwaarloosbaar
  als volume, **maar niet als geometrie**: er zitten enkele rechte lijnen van 100-634 km
  tussen, en juist die worden in een graaf een aantrekkelijke edge. **Fase-2-regel, en het is
  drie regels code: gooi elk segment weg dat een gat > KNIP_MIN overspant, ongeacht bron —
  of repareer de wortel in `bouw_tracks.py` (regel 195: een stilliggende ping mag de
  gat-referentie niet verversen als hij niet in de track komt).**

**BESLUIT 4 — Voor het KADE-eind in Australië is onze EIGEN collector de betere bron**
(0,453 km korrel, en 20 walstations in Oceanië volgens de wereldscan). **AMSA en de
collector vullen elkaar dus aan in plaats van te concurreren:** AMSA levert het
offshore-/satellietbereik en het bestaan van de kustlanen, de collector levert de laatste
kilometers naar de kade in de havens waar hij dekking heeft. Schrijf dat zo op in de
graafopzet, anders lijkt het alsof AMSA "verloren" heeft van een bron met 200× minder
volume.

### 7.3 Per bron: wat er verder aan de trackvorm opvalt

- **DK** is de dichtste set (40,4 mln punten op 28 dagen) en zal in de Noordzee/Oostzee-
  overlapzone met de collector domineren; **dubbeltelling per MMSI+minuut is daar het
  aandachtspunt**. Twee dingen om vóór het bakken te regelen: (1) ruwweg **de helft van de
  posities is Class B** (pleziervaart) — dat is geen vrachtgeometrie, en de klasse zit
  **niet** in de trackset, dus filteren vraagt een herbouw uit de collector-JSONL (die staat
  op schijf); (2) de **94-125 spoofing-tracks** met inlandse Russische coördinaten wil je
  eruit hebben, bijvoorbeeld met een kernvak-eis op het zwaartepunt (95,28% van de tracks
  zit al in het DK-kernvak, dus dat kost bijna niets).
- **NO** is de **fijnste** bron die we hebben (mediaan 10 s ruwe cadans) en dus de beste
  kandidaat voor kade-precisie (LAR-531) — de Capesize-eindpunten bij de LKAB-kade in Narvik
  zijn direct materiaal. Maar de set bestaat uit **drie disjuncte boxen**: de graaf krijgt
  daar drie eilanden zonder verbinding, en er is per constructie niets tussen. Wil je het
  ertsbeen Narvik → Vestfjorden echt in de graaf, dan moet de box westelijk worden
  doorgetrokken (~1,2 MB gz per 4 dagen, dus verwaarloosbaar).
- **VS** is de enige set met een geaccepteerde pilot erachter (Vidalia) en blijft de
  referentie; p90 0,66 km is iets grover dan DK/NO en de bron levert al 1 positie per minuut,
  dus daar valt niets te winnen met dunnen.
- **collector** is met 0,453 km de grofste van de vier graafbronnen, en juist híj moet het
  kade-eind dragen buiten VS/DK/NO. Concreet fase-2-probleem bij Wesel: de **622 tracks in
  het venster Emmerich→Duisburg vallen uiteen in 338 west en 237 oost die elkaar nooit
  raken** → de graaf krijgt daar **twee losse componenten, geen doorlopende Rijn**. Conform
  de werkregel niet repareren met geleende geometrie, maar wél expliciet afvangen bij het
  bouwen, anders leest het als een bug in de graaf in plaats van als een dekkingsgat.
- **AU** heeft naast de korrel nog twee eigenaardigheden voor een dekkingslaag: er is **geen
  MMSI** (surrogaat `craft_id`, wel stabiel over maanden: overlap april∩mei = 71%), en er is
  **geen Class A/B-onderscheid** — alles komt binnen als `PositionReport`.

---

## 8 · Openstaande acties voor Lars

1. **Twee accounts aanmaken en twee tokens plakken** in
   `C:\Users\lars\.claude\grondstoffen-atlas.env` als `EURIS_API_TOKEN` en `GFW_API_TOKEN`.
   Het volledige recept staat in **`v2/design/accounts-euris-gfw.md`** (658 regels): per bron
   de exacte URL en velden, de scopes, waar de credential landt, een kant-en-klare testcall
   mét verwacht antwoord, en wat de uitslag betekent. **Ik heb bewust géén account
   aangemaakt, geen formulier ingevuld en geen voorwaarden geaccepteerd.** Kort:
   EuRIS-token via *eurisportal.eu → Username → My Account → API Tokens → Add* (wordt één
   keer getoond, max 1 jaar geldig); GFW via het registratieformulier met
   *Organization category = OTHER*. **Verwacht er niet te veel van bij EuRIS:** het token
   koopt rate limit, geen tracks van derden (§5, punt 12).
2. **Besluit: zet de atlas op niet-commercieel zolang de AMSA-laag meedraait**, of laat die
   laag vallen. CC BY-NC 3.0 AU is een licentiekeuze, geen implementatiedetail.
3. **Besluit: per-bron KNIP als expliciete CLI-vlag op `bouw_tracks.py`** (default 30, dan
   blijft de VS-set bit-identiek) plus MIN_PUNTEN, of het huidige in-memory-pad in
   `haal_amsa.py` laten staan. Zonder besluit is de AMSA-trackset niet reproduceerbaar uit de
   tool alleen.
4. **Besluit: VPS opruimen of niet.** De drie afgesloten dagen staan nu byte-identiek lokaal,
   dus opruimen mág — het levert 450 MB op bij 21 GB vrij (2,1%) en zet de enige kopie
   lokaal. 24 dagen marge bij 837-844 MB/dag. Loont pas bij 3-4 opgespaarde dagen.
5. **Zodra de volle `2026-07-27.jsonl.gz` binnenkomt: verwijder eerst
   `2026-07-27-deel.jsonl.gz`.** Niet omdat er dubbel geteld wordt (dat doet de minuut-dedup
   niet, §4), maar omdat het bestand anders voor niets wordt gelezen en het beeld vervuilt.

**Aan onze kant, en dit kost geen account:** (a) de **overnight trackId-meting** bij EuRIS —
de enige beslissende openstaande vraag, recept staat in de brief, leesregel is "kijk naar het
aantal *nieuwe* id's, niet naar het totaal"; (b) `euris_fairways.json` (7.122 secties met
CEMT-klasse, 100% gevuld, en max diepgang op 68%) omzetten naar het vaarwegformaat van de
atlas — dit is de authoritatieve diepgangbron die LAR-514 miste; (c) `euris_terminals.json`
(3.969 punten, 100% ISRS) en `euris_berths.json` als node-bron voor LAR-531; (d) de Noorse
kopdag-knip repareren zodat 2026-03-12 alsnog meekomt; (e) de DMA-regex verruimen naar de
maandarchieven.

---

## 9 · GECORRIGEERD DOOR DE TOETSERS

**Deze claims mogen niet als feit in de vault of in `CLAUDE.md` terechtkomen.** Ze komen
allemaal uit de bouwersrapporten van deze ronde en zijn door de toetsers — en waar vermeld
door mijzelf — weerlegd.

| claim uit een bouwersrapport | wat er werkelijk staat | hoe vastgesteld |
|---|---|---|
| VPS: "~2,3 dagen materiaal" / "4 pings op ca. 55 uur" | **1,43 dagen = 34,4 uur.** De deeldag `2026-07-25.jsonl.gz` beslaat maar **3 uur 37 min** (20:23:17-23:59:58) maar werd als hele dag geteld. Winst t.o.v. de 12,5-uursmeting is 2,75×, niet 4,4×. **De Wesel-conclusie blijft overeind, op minder materiaal.** | zelf gemeten: trackset-spanne + eerste/laatste `time_utc` in het bronbestand |
| AMSA: de val van 7,75 mln pings naar 853.639 trackpunten zou verdacht zijn | **Géén tijdstempelfout.** 5.454.693 van 7.746.422 posities (**70,4%**) hebben SOG < 0,5 en vallen per ontwerp weg; de harde bovengrens (unieke MMSI-minuut én varend) is 2.291.702, en de rest sneuvelt op MIN_PUNTEN=8 / MIN_KM=2 bij uurkorrel. Alle 7,75 mln tijdstempels overleven de letterlijke `strptime`: 0 fouten. | zelf gemeten over alle 4 AMSA-maanden; parse-controle door de toetser |
| NO: unieke MMSI per box 405 / 656 / 80 | **399 / 641 / 78 in de bestanden.** De gerapporteerde getallen zijn de rúwe rijtelling inclusief de weggeknipte kopdag — ze beschrijven de download, niet de trackbron. | zelf geteld op narvik (78) + toetser op alle drie |
| NO: "11 vrachtschepen ≥150 m, waarvan 6 Capesize" in narvik | **23 schepen ≥150 m, waarvan 8 Capesize** van 288-292 m met diepgang 18,17-18,32 m. De conclusie ("narvik is het ertsbeen") wordt sterker. | toetser, uit de statische data |
| NO: "de bron levert ~1 positie per schip per 2-3 minuten, mogelijk te grof voor kadeprecisie" | **Mediaan ping-interval 10 s, 90,2% ≤ 30 s.** Vrijwel volle AIS-cadans; dit is de fijnste bron die we hebben. De 0,265 km per punt in de trackset komt van de minuut-kwantisering in `bouw_tracks.py`. | zelf gemeten, 338.152 intervallen op narvik |
| NO: "2026-03-11 én 03-12 zijn onhaalbaar" | **Alleen 03-11 mist echt.** 03-12 staat al in de gedownloade brokken (502.112 rijen over drie boxen) en is door onze eigen dagknip weggegooid. 27 van 28 dagen zijn gratis terug te halen. | zelf nageteld: 10.235 rijen met datum 03-12 in het narvik-brok |
| DK: "54,6% Class B, 45,4% Class A" | **Omgedraaid:** A 52,96% / B 47,04% over 28 dagen; op de ijkdag 50,6% B / 49,4% A. Praktisch: ruwweg half-half. | toetser exact over 28 dagen; zelf geteld op 2026-07-24 |
| DK: dunningsfactor "5,8×" | **5,05×** (volle dag). De 5,8 komt uit een monster van 90 minuten. | toetser |
| DK: "0,8% van de posities is de sentinel" (kopcommentaar `haal_dma.py`) | **0,17%** (30.547 van 18,16 mln). | toetser |
| DK: "de bucket bevat 513 dagbestanden, oudste 2025-02-27" | **1.095 keys**, waaronder **210 maandarchieven 2006-03 t/m 2024-02 (~3.493 GB)** die onze regex niet ziet. De "oudste dag" is een eigenschap van onze tool. | toetser (volledige listing) + zelf de regex in `bucket_dagen()` nagelezen |
| DK: "hemelsbreed kade-kade 18,85 km" (en +0,0% daartegen) | **18,33 km** uit de werkelijke ligplaatsnaderingen. De vergelijking die telt (18,86-18,89 tegen 19 km gepubliceerd) houdt wél. | toetser |
| DK: afstandsbakken 117.947 / 46.456 / 4.901 / 1.225 / 125 | **Maatafhankelijk, neem geen van beide over.** De vórm klopt (overweldigend <250 km, staart van ~100 tracks boven 1.000 km); 95,28% van de tracks in het DK-kernvak reproduceert exact. | beide partijen, verschillende referentiepunten |
| AMSA: "~37 km puntafstand" | **19,10 km gemiddeld / 20,45 km mediaan / p90 30,45** over alle 811.025 segmenten. De 37 geldt alleen voor de veerboot uit de lengtetoets. | zelf gemeten + toetser |
| AMSA: tijdkorrel "mediaan 60 min, 5,2% ≤ 30 min" als dataset-eigenschap | Dat geldt voor **2026-06 alleen** = 6% van de data (en juist de regressiemaand). Over alles: **mediaan 65 min, 0,3% ≤ 30 min**. Fout in conservatieve richting. | toetser |
| AMSA: "de tracks zijn geometrisch schoon" | Waar over bbox en over land, **niet over tijdcontinuïteit**: 4,94% van de km overbrugt een gat > 90 min, tot 7.546,6 km in één sprong. | zelf gemeten + toetser (mechanisme in de code getraceerd) |
| VPS: "4 pings van hooguit vier schepen" op Wesel-hoogte | **2 MMSI, binnen 4 minuten** (02:32-02:36 UTC, 26 juli). | toetser |
| VPS: "de deeldag laat 6,8 uur dubbel tellen" | **De dubbeltelling treedt niet op.** Pass 2 sorteert per MMSI en gooit elke ping weg met dezelfde `t_min` als het vorige punt (regel 202). Kosten zijn leestijd, niet geometrie. | zelf de code nagelezen |
| VPS: alle voor→na-percentages | **Niet auditbaar.** De oude trackset is overschreven, gitignored en zonder back-up; alleen "23.766 tracks" en "3.195" hebben een papieren spoor in `CLAUDE.md`. | toetser (hele build-cache doorzocht) |
| `CLAUDE.md`, M28-banner: "het Wesel-gat is dichtgelopen" | **Weerlegd.** 0 trackpunten tussen lon 6,44 en 6,64, 0 overspannende tracks, 149 schepen aan beide kanten. Banner + `bugs-and-risks.md` corrigeren. | bouwer én toetser onafhankelijk |

**En de toetsers zijn ook niet onfeilbaar** — één claim van hén houdt niet: de DK-toetser
verklaart de puntenval met "46,4% van de posities heeft SOG < 0,5". *Zelf gemeten op de
ijkdag: 63,2% (2.262.732 van 3.580.160).* Dat sluit rekenkundig veel beter op de 38,3%
retentie, dus zijn conclusie (geen stil verlies) wordt sterker terwijl zijn percentage
sneuvelt. Zelfde regel als altijd: **een getal dat een conclusie draagt, hermeet je.**
