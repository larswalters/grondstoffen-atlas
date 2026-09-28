# Routebrief (licht) · Grafiet · Van → Via → Naar (land)

**stroom-id:** `grafiet-skaland-lulea` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** Noors hoogwaardig vlokgrafiet van de Skaland-mijn (Senja) per korte lokale
aansluitweg naar de eigen dorpskade, per **zeeschip** over de Noorse Zee en het Skagerrak/Kattegat
naar de Botnische Golf, naar de kade van Talga's Talnode-anodefabriek in Luleå, Zweden — het
volledig Europese CRMA-draadje. **Reserve-as (prioriteit 4)**: de kernclaim (Skaland-vlok als
Talga-feedstock) is dit onderzoeksbudget niet onafhankelijk bevestigd (zie §7/risico).
**Welke as van het verhaal:** enige geheel-Europese grafiet-anodeketen op de kaart, tegenover de
Balama/China-assen; jaarvolume ~10,5 kt vlokconcentraat/j (Skaland's totale productie, niet per se
allemaal naar Talga — zie §7).

## 1 · Ketenkaart
```
Skaland-mijn `gr-skaland-mijn` ──(b1 truck · lokale aansluitweg mijn→dorpskade · ~0,7 km, niet
gemeten)──► Skaland-kade `gr-skaland-kade` ──(b2 zee · haven-aanloop, stippel, ~27 km, kade ligt
buiten de 25 km-snap van MARNET)──► zeeknoop 4723 ──(b3 zee · Noorse Zee → Vestfjorden-omvaart →
Skagerrak → Kattegat → Botnische Golf, MARNET · ~2.000+ km, niet gemeten)──► Talga Luleå-kade
`gr-lulea-talnode` ⏹ stoppunt (fase C/D niet getekend — geen bron voor vervolg binnen de fabriek)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-skaland-mijn` → `gr-skaland-kade` | lokale dorpsweg Skaland (geen refs; eigen terrein/village-weg, zichtbaar op satelliet) | ~0,7 [eigen meting op satelliet, niet gepubliceerd] | maak_stroombeen_weg (extract `noorwegen`) of korte stippel als het net hier niet aaneengesloten blijkt | nee, tenzij het wegprofiel geen aaneengesloten segment geeft |
| b2 | B | zee | `gr-skaland-kade` → zeeknoop 4723 (69,47970/16,62040) | haven-aanloop over water — MARNET reikt hier niet (kade > 25 km van de dichtstbijzijnde zeeknoop) | ~27,3 [eigen meting, `hecht_marnet`-zeeknopenlijst] | `maak_havenaanloop.py`, terugval: rechte stippel als er geen pad wordt gevonden | ja — haven-aanloop, "hier reikt het net niet" |
| b3 | B | zee (MARNET) | zeeknoop 4723 → `gr-lulea-talnode` | Noorse Zee → (Lofoten/Vestfjorden-omvaart) → Noordzee-noord → Skagerrak → Kattegat → Botnische Golf | onbekend, niet gemeten deze ronde | MARNET `--been "zee|…|69.4797,16.6204|65.58,22.15"` (Luleå-kade snapt op 2,06 km van zeeknoop 8830, geen aanloop nodig aan die kant) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-skaland-mijn` | mijn/verwerkingsplant (kop) | Skaland Grafitverk (Skaland Graphite AS, sinds jan. 2025 Norge Mining), Senja, Noorwegen — hergebruik sitelaag-anker `w-skaland` | 69,4462, 17,3279 | [1][2][3][8], sitelaag `v2/design/grafiet-sitelaag.json` | bron-gelegd (z15 gezien: gebouw op de heuvelflank boven het dorp Skaland, hergebruikt uit de sitelaag; dit onderzoeksbudget opnieuw bekeken, ongewijzigd) |
| `gr-skaland-kade` | lokale overslag (dorpskade) | Skaland fiskerihavn — kleine haven/kade aan Bergsfjorden, direct onder de plant | 69,4428, 17,3125 | [1][3], eigen satellietblik | **onzeker** (z18 gezien: golfbreker met een kleine bootbasin en één aanlegsteiger van ~50 m; alleen kleine vaartuigen zichtbaar, geen kraan/transportband — schaal en functie voor bulk-vlokexport niet bevestigd; wél de enige kade op het terrein en geometrisch de kortste weg naar open zee, zie §7) |
| `gr-lulea-talnode` | losplek + anodefabriek | Talga Talnode-anodefabriek / EVA Plant, Luleå Industripark, Zweden — hergebruik v1-registercoördinaat | 65,58, 22,15 | [4], v1-register (`design/grafiet.md` `gr-ref-sweden`) | **aannemelijk** (z15 gezien dit onderzoeksbudget: het punt landt op de kleinbootenhaven/marina in het centrum van Luleå, niet aantoonbaar op het industrieterrein van de fabriek — coördinaat niet dit jaar geverifieerd, zie §7) |

## 4 · Via-punten
Geen — b1 is een korte lokale weg zonder corridorkeuze; b3 is een open-zee MARNET-been zonder
gekarteerd via-punt (de Vestfjorden/Lofoten-omvaart volgt uit de routering, niet uit een bron).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Skaland Grafitverk | Skaland Graphite AS (Norge Mining, sinds jan. 2025) | grafieterts (Traelen-mijn, sinds 2007) → vlokconcentraat | ~10,5 kt/j (2% van de wereld-vlokproductie; hoogste ertsgehalte ter wereld, ~25% C) | [2][3] |
| Talga EVA Plant / Talnode-fabriek | Talga Group | vlokconcentraat → gecoat anodepoeder (Talnode-C) | EVA-plant 50 t/j (proef, sinds 2022); commerciële fabriek in aanbouw (FID 2027) | [4] |

## 6 · Stoppunt
De brief stopt bij de Talga-kade in Luleå: dat is het bestaande registerpunt en het enige
gedocumenteerde Europese eindpunt voor Noors vlokgrafiet. Fase D/E vervallen — geen bron
beschrijft wat er ná de Talnode-fabriek met het anodemateriaal gebeurt op zendingsniveau.

## 7 · Open punten
- **De kernclaim van deze as (Skaland → Talga) is dit onderzoeksbudget niet onafhankelijk
  bevestigd.** Talga's eigen Luleå-pagina [4] noemt als feedstock uitsluitend "eigen Vittangi-
  ertsvoorraad"; geen vermelding van Skaland of Noors vlok. De relatie steunt alleen op het
  v1-register/checklist [8] — precies het risico dat de haalbaarheidstoets al signaleerde. Vóór
  promotie naar een hogere prioriteit: Talga's jaarverslag/persberichten checken op de actuele
  feedstock-mix.
- **Geen bron bevestigt welke Noorse haven Skaland voor export gebruikt.** Eén bron noemt vaag
  "existing processing and port infrastructure" [3] zonder havennaam. Onderzocht en verworpen:
  Narvik/Fagernes (LKAB-ertsterminal, wél reële bulkinfrastructuur, maar **55 km** van de
  dichtstbijzijnde MARNET-zeeknoop) en Tromsø (36 km) en Finnsnes (53 km) — alle drie liggen
  verder van de zeegraaf dan Skalands eigen dorpskade (27 km). Alle Noord-Noorse fjordhavens in
  deze regio liggen ver van een MARNET-knoop; dit lijkt een korrelgat in het zeenet voor deze
  hele kust, niet iets dat aan de havenkeuze ligt. Gekozen: de eigen dorpskade, als kortste en
  best gedocumenteerde optie — maar de rol als bulk-exportkade is niet bevestigd (§3).
  Truckcorridor-km b1 en de exacte route van b1 zijn dit budget niet gemeten.
- **Jaarvolume-discrepantie:** het ontwerp gebruikte 15 kt/j (v1-register); de bedrijfsbron van
  dit onderzoeksbudget [2] geeft ~10,5 kt/j als Skalands **totale** productie (niet: het deel dat
  naar Talga gaat). Beide cijfers in de brief laten staan; peiljaar 2024-2025 (Norge Mining-
  overname, jan. 2025).
- **Eigendomswijziging:** per jan. 2025 is Skaland Graphite AS overgenomen door **Norge Mining**
  [1] — nieuwer dan het v1-register, dat nog "Skaland Graphite" als zelfstandige naam voert.
- **Haven-aanloop b2 (~27 km) is groter dan enig eerder gebakken precedent** (Fujairah 10,5 km /
  Ras Tanura 11,1 km / Aktau 7,4 km, M31 golf 1) — mogelijk buiten het bereik van
  `maak_havenaanloop.py` binnen de gebruikelijke timeout; terugval is de gestippelde rechte lijn.
- **WEBBUDGET was op** (3 van 3 WebSearch-calls gebruikt); Nominatim/Overpass waren dit budget
  onbereikbaar (429/"access denied", vermoedelijk gedeeld sessiebudget) — Photon werkte wel maar
  vond geen Talga-adres in OSM. Geen Chinese/Zweedse adresregisters geraadpleegd.

## 8 · Bronnen
[1] High North News, 2026 (uittreksel via zoekresultaat) — Norge Mining neemt Skaland Graphite AS over (Europa's grootste natuurlijk-grafietproducent), transactie verwacht jan. 2025. https://en.highnorthnews.com/business/australian-owner-sells-graphite-producer-in-northern-norway/175847
[2] Mineral Commodities Ltd — Skaland Graphite Operation: locatie Senja (~213 km van Tromsø), "existing processing and port infrastructure", grootste kristallijne grafietproducent van Europa (~2% wereld-vlokproductie, ertsgehalte ~25% C), erts sinds 2007 uit de Traelen-mijn. https://www.mineralcommodities.com/operations-projects/graphite/norway/
[3] Wikipedia (EN), "Skaland" — dorp in Senja Municipality, Troms, hoofdwerkgever Skaland Grafitverk (opgericht 1917), coördinaat 69,44444/17,29806. https://en.wikipedia.org/wiki/Skaland
[4] Talga Group, "Luleå" operations-pagina — EVA Plant (50 t/j anodemateriaal, sinds 2022) + commerciële Talnode-fabriek (FID 2027) in Luleå Industripark; feedstock = eigen Vittangi-ertsvoorraad; EU Innovation Fund €70 mln. https://www.talgagroup.com/our-operations/lulea/
[5] Wikipedia (EN), "Port of Narvik" — LKAB-ertsterminal Fagernes, Ofotfjorden, ~16-25 Mt/j ijzererts, geen vermelding van grafiet. https://en.wikipedia.org/wiki/Port_of_Narvik
[6] Zoekresultaat (Wikipedia EN, "Fagernes (Narvik)") — coördinaat LKAB-terminal 68,4135/17,4290, terminus van de Ofotbanen. (via WebSearch-snippet)
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15-z18, live) — `sat-grafiet-skaland-lulea-skaland-mijn.png`, `-skaland-havenblik.png`, `-skaland-kade-west.png`, `-skaland-kade-basin.png`, `-narvik-fagernes.png`, `-talga-lulea.png`.
[8] v1-register `design/grafiet.md` §4a en `v2/design/grafiet-sitelaag.json` (anker `w-skaland`) — oorspronkelijke Skaland→Talga-aanname (15 kt/j) en de v1-coördinaat voor `gr-ref-sweden`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `grafiet-skaland-lulea`** → `v2/data/stroomroute-grafiet-skaland-lulea.json` — 3 benen,
**3.688,0 km**, 465 punten, 3 markers. truck 1,6 + zee 27,3 (stippel) + zee 3.659,1 = 3.688,0 km.
Recept: `bak_stromen.sh` (functie `bak_grafiet_skaland_lulea`). Bestandsgrootte **9,3 KB**.

**b1 (truck, doorgetrokken, `maak_stroombeen_weg.py`, profiel
`grafiet-skaland-lulea-skaland-mijn-skaland-kade`, extract `noorwegen`):** het lokale wegennet bij
Skaland bleek wél aaneengesloten (geen terugval nodig) — **1,6 km over 75 punten**, tegen de eigen
ongepubliceerde meting van ~0,7 km uit §2/de bak-aanwijzingen = **+123,4%, buiten ±15%**.
⚠️ **Bevinding, niet dichtgetrokken:** de brief-km zelf was al "eigen meting op satelliet, niet
gepubliceerd", geen gebronde referentie — het gebakken wegprofiel volgt 74 gesnoeide keerlussen op
het eigen terrein/dorpspad (74 keerlussen gesnoeid, 2,0 → 1,6 km), dus het verschil zit in de
kronkeling van de échte dorpsweg t.o.v. een rechte satellietschatting, niet in een verkeerd gelegd
wegtracé. Beide ankers snappen op 0,08 km (mijn) en 0,00 km (kade) — geen via-punt bijgeschoven.

**b2 (zee, stippel, haven-aanloop Skaland):** de dorpskade ligt **27,31 km** van de dichtstbijzijnde
MARNET-zeeknoop 4723 (69,47970/16,62040), zelf herrekend vóór het bakken en identiek aan de brief —
het **grootste haven-aanloop-precedent tot nu toe** (groter dan Fujairah 10,5 / Ras Tanura 11,1 /
Aktau 7,4 km, M31 golf 1). `maak_havenaanloop.py --van 69.4428,17.3125 --naar 69.4797,16.6204` liep
vast op `timeout 300` (exit 124, na ~300 s) — geen tweede poging (bakhandleiding §2), dus de rechte
stippel is de eindvorm: **27,310 km**.

**b3 (zee, MARNET, doorgetrokken):** `--been "zee|...|69.4797,16.6204|65.58,22.15"` — snap 0,000 km
aan de Skaland-kant (begint al op zeeknoop 4723) en 2,065 km aan de Luleå-kant (Talga-kade snapt
binnen de 5 km-norm op zeeknoop 8830, geen aparte haven-aanloop nodig, zoals de brief voorspelde).
Resultaat **3.659,1 km over 49 MARNET-edges, 388 punten** — de router volgt zelf de
Vestfjorden/Lofoten-omvaart → Skagerrak → Kattegat → Botnische Golf, exact het tracé dat de brief uit
bronnen afleidde. **Geen lengtetoets mogelijk** (brief: "onbekend, niet gemeten deze ronde"; grote
cirkel Skaland–Luleå ≈ 1.850 km, dus de vaarbare route is ~2× de grote cirkel — geografisch verwacht
voor een omvaart om Noord-Noorwegen plus de hele Botnische Golf-lengte). Lengte-invariant: getekende
lijn 3.659,056 km vs som edge-km 3.659,200 km = −0,144 km (de naden).

**Toets naden:** alle overgangen **0,000 km** — elk been begint precies waar het vorige eindigt.

**`toets_knikken.py`:** truck-been 8 kleine spikes (alle <60°, R 2–18 m, OSM-dorpswegdetail, geen
bevinding); zee-been 3 knikken ≥60° waarvan **1 omkering (155,9°, R≈4.609 m) bij 70,00000/17,00000,
geclassificeerd als TERUGLOOP**. ⚠️ **Bevinding, niet dichtgetrokken:** dit is geen handgelegde
stippel maar een MARNET-router-artefact op het open-zee-stuk vlak na de haven-aanloop-knoop (de
route buigt hier scherp om Noord-Noorwegen/de Lofoten-omvaart) — er is in de lichte werkwijze geen
gereedschap om een router-interne MARNET-knik te repareren zonder de graaf zelf aan te raken; hoort
bij een latere netverfijning van de Noord-Noorse kust, niet bij dit bak-recept.

**`toets_rechte_benen.py --min-km 5`:** b2 (haven-aanloop Skaland, 27,3 km, omwegfactor 1,000) komt
naar voren als "rechte lijn" — **verwacht en correct**: een gedocumenteerde stippel met reden (mislukte
haven-aanloop, geen tweede poging). Geen ander been van deze stroom in de lijst.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee} (binnen de
toegestane set), elk been ≥2 punten (minimum 2, het truckbeen 75, het zeebeen 388).

**Markers:** alle drie op de been-eindpunten zelf (gr-skaland-mijn, gr-skaland-kade,
gr-lulea-talnode) — 0,0 m van de lijn (anker = routeerpunt op elk van de drie).

**Gereedschapslessen:**
- De zeeknoop-lookup uit de brief kwam bij het bakken exact terug: Skaland-kade 27,31 km / zeeknoop
  4723, Luleå-kade 2,065 km / zeeknoop 8830 — beide onafhankelijk herrekend vóór het bakken en
  identiek aan de bak-aanwijzingen.
- De haven-aanloop liep zoals voorspeld vast op de gebruikelijke `timeout 300`; consistent met de
  bakhandleiding-observatie dat de 1:10M-kust bepaalde (kleine, geïsoleerde) havens niet kent — geen
  indicatie dat een tweede poging alsnog een pad zou vinden.
- Het lokale Noorse wegennet bleek — anders dan de brief als risico noemde — wél aaneengesloten
  genoeg voor een doorgetrokken been; de terugval-stippel was niet nodig.
- WEBBUDGET niet aangesproken deze bak-ronde (geen WebSearch nodig, alleen bestaand gereedschap).

**⚠️ Overgenomen uit §7 (niet dichtgetrokken bij het bakken):** de kernclaim van deze as
(Skaland-vlok als Talga-feedstock) blijft onbevestigd — Talga's eigen Luleå-pagina noemt uitsluitend
eigen Vittangi-erts; deze stroom blijft reserve-as (prioriteit 4). Ook de rol van de Skaland-dorpskade
als bulkexportkade en het Talga-Luleå-kadepunt (marina-nabijheid) blijven ongewijzigd onzeker/
aannemelijk zoals in §3.
