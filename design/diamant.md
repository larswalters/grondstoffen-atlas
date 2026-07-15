# Diamant — brief (ingevuld ontwerp) — hoort bij `data/diamond.js`

*Peiljaar ±2023-2024. Volumes in **Mct/jaar** (miljoen karaat ruw), indicatief en afgerond — bedoeld om
verhoudingen te tonen, geen handelsstatistiek. Wereld-ruwproductie ≈ **110-120 Mct** (Kimberley Process /
USGS 2024). Let op: diamant kent een scherpe **volume-vs-waarde-splitsing** — Rusland is #1 op volume,
Botswana #1 op waarde; DRC/Zimbabwe zijn volumineus maar grotendeels industrieel/laagwaardig. Bronnen:
Kimberley Process Certification Scheme (KPCS) ruwstatistiek, USGS Mineral Commodity Summaries 2025
(Diamond, industrial + gem), De Beers/Alrosa/Debswana-rapportages, AWDC (Antwerp), GJEPC (India/Surat). Zie §7.
Status: **uitgewerkt-ontwerp** — klaar om 1-op-1 naar `diamond.js` te zetten.*

> **Principe:** we vertellen geen verhaal, we modelleren de werkelijkheid — het plaatje vertelt zichzelf.
> Voor lithium/koper is de vorm "alles door China-raffinage", voor goud "alles door Zwitserland", voor REE
> "alles door Ganzhou". Voor diamant is de vorm een **nóg scherpere downstream-trechter**: de winning is
> verspreid (Rusland/Botswana/Canada/Angola/Afrika), maar **~90-95% van álle diamant wordt in één Indiase
> stad geslepen en gepolijst: Surat (Gujarat)**. Daar bovenop een **institutioneel knelpunt** — Antwerpen,
> ooit de handelshoofdstad, nu het verplichte **G7-certificeringsknooppunt** tegen Russische (Alrosa)
> diamant. En de hele keten **vliegt** (beveiligde luchtvracht) — dus dezelfde air-mode als goud/PGM,
> **géén nieuw chokepoint**. Onderliggend: het **De Beers + Alrosa-duopolie** (kartel-verleden) en de
> **lab-grown-ontwrichting** (Chinese/Indiase kweekdiamant).

---

## 0. Metadata (→ `REGISTER({...})` in `diamond.js`)

| veld | waarde |
|---|---|
| `id` | `diamond` |
| `name` | Diamant |
| `symbol` | C (kristallijn koolstof — zelfde element als grafiet, tegenovergestelde waarde) |
| `color` | `#9FD9EF` (ijsblauw-wit; markers) |
| `flowColor` | `#CDEEFB` (lichter ijsblauw, voor de bogen tegen de donkere bol) |
| `unit` | `Mct/jaar (ruw, indicatief)` |
| `detail` | `uitgewerkt` |
| `blurb` | De winning is verspreid (Rusland #1 op volume, Botswana #1 op waarde, Canada, Angola, zuidelijk Afrika), maar het slijpen en polijsten knijpt samen in één Indiase stad: **Surat** (~90-95% van alle stenen) — de scherpste downstream-trechter van de atlas. De handel loopt via **Antwerpen** (nu ook het verplichte G7-certificeringsknooppunt tegen Russische diamant) en **Dubai**. Alles **vliegt** (beveiligde koeriers). Onderliggend: het De Beers/Alrosa-duopolie en de opkomst van goedkope **lab-grown** diamant uit China en India. |

## 1. Het verhaal in 3 zinnen
1. **De winning is verspreid, de bewerking niet:** ruwe diamant komt uit Rusland (Alrosa/Jakoetië, #1 volume),
   Botswana (Debswana/Jwaneng+Orapa, #1 waarde), Canada, Angola, Zuid-Afrika, Zimbabwe, Namibië (marien, hoogste
   waarde/karaat) — maar **~90-95% wordt geslepen en gepolijst in Surat, India**. Dát is de trechter.
2. De handel loopt door twee **hubs**: **Antwerpen** (historische hoofdstad, nu het **verplichte
   G7-certificeringsknooppunt** sinds de sanctie op Russische diamant, maart 2024) en **Dubai** (opkomend, en
   het herrouterings-luik voor Russische stenen). De De Beers-verkopen ("sights") lopen via **Gaborone** (Botswana).
3. Alles reist per **beveiligde luchtvracht** (Brink's/Malca-Amit/Ferrari Group) → dezelfde **air-mode** als
   goud/PGM, **géén nieuw chokepoint**. Twee schaduwen over de keten: het **De Beers+Alrosa-duopolie** (kartel-
   verleden, "A Diamond is Forever") en de **lab-grown-ontwrichting** (China/Henan HPHT + India CVD ondergraven
   de natuurlijke, vooral Amerikaanse, verlovingsring-markt).

## 2. De keten & stages (→ `stage`-codes; hergebruikt de bestaande stage-styling)
Diamant kent geen "cel/kathode"; we hergebruiken de drie codes en vullen ze diamant-logisch in.

| stap | `stage`-code | kleur | booghoogte | inhoud |
|---|---|---|---|---|
| 1. mijn → **ruwe diamant** (rough) | `erts` | dof/donker | laag | mijn → sorteer-/handelshub (Gaborone/Antwerpen/Dubai) |
| 2. **geslepen & gepolijst** (Surat) | `raffinaat` | volle ijsblauw (#9FD9EF) | midden | hub → Surat-slijperij → polished-handel (Mumbai/Antwerpen) |
| 3. **sieraad / retail** | `product` | licht, bijna wit | hoog | polished-hub → eindmarkt (VS #1 / China / Golf / EU / India) |

## 3. Nodes (locaties)
> Alle `type`-waarden bestaan al in de rendering-laag: `mine`/`refinery`/`port`/`market`/`hub`/`airport`.
> **Géén nieuwe marker-styling nodig** (`hub` = Antwerpen/Dubai/Gaborone/Mumbai; `refinery` = de slijperij =
> Surat/China; de ruit-marker past treffend bij diamant). Coördinaten: **west = negatief** (gecontroleerd).
> Shares zijn % van ~115 Mct wereld-ruwproductie (op **volume**; waarde-nuance in de `note`).

### 3a. Winning (`type: mine`, met `share` op volume) — de spreiding is de opmaat naar de trechter
*`note` benoemt telkens het volume-vs-waarde-karakter (edelsteen vs. industrieel) en de operator/keten.*

| id | naam | land | lat | lon | share | tier | operator | ~Mct/jr | karakter |
|---|---|---|---|---|---|---|---|---|---|
| dia-alrosa | Alrosa (Mir/Udachny, Jakoetië) | Rusland | 62.53 | 113.96 | 30% | 1 | Alrosa | ~35 | **#1 op volume**; sinds maart 2024 onder G7-sanctie → herrouting Dubai/India |
| dia-jwaneng | Jwaneng | Botswana | -24.60 | 24.73 | 11% | 1 | Debswana (De Beers/Botswana 50/50) | ~12 | **rijkste mijn ter wereld op waarde**; edelsteen-kwaliteit |
| dia-orapa | Orapa | Botswana | -21.31 | 25.37 | 10% | 1 | Debswana | ~11 | grootste Botswaanse mijn op volume; edelsteen + near-gem |
| dia-canada | Canada (Diavik/Ekati/Gahcho Kué, NWT) | Canada | 64.50 | -110.28 | 14% | 1 | Rio Tinto / Burgundy / De Beers | ~16 | hoogwaardig edelsteen, "conflictvrij" premium |
| dia-catoca | Catoca (Lucapa) | Angola | -9.42 | 20.30 | 8% | 1 | Endiama/Alrosa JV | ~9 | grootste Afrikaanse kimberliet; mix edelsteen/industrieel |
| dia-drc | Mbuji-Mayi (MIBA) | DR Congo | -6.13 | 23.60 | 8% | 2 | MIBA / artisanaal | ~9 | **volumineus maar grotendeels industrieel/laagwaardig** (alluviaal) |
| dia-venetia | Venetia | Zuid-Afrika | -22.44 | 29.33 | 5% | 2 | De Beers | ~5 | grootste ZA-mijn (nu ondergronds); edelsteen |
| dia-marange | Marange (alluviaal) | Zimbabwe | -18.92 | 32.55 | 4% | 2 | ZCDC | ~5 | volumineus, laagwaardig; beladen (2008-geweld, mensenrechten) |
| dia-namibia | Namdeb / Debmarine (Oranjemund) | Namibië | -28.55 | 16.45 | 2% | 2 | De Beers/Namibië JV | ~2 | **marien** (zee-bagger); hoogste waarde/karaat ter wereld; `coastal` |
| dia-letseng | Letšeng | Lesotho | -29.02 | 28.87 | 1% | 3 | Gem Diamonds | ~1 | hoogste gemiddelde $/karaat; grote uitzonderlijke stenen |
| dia-argyle | Argyle (**gesloten 2020**) | Australië | -16.70 | 128.40 | 0% | 3 | Rio Tinto (ex) | 0 | ooit ~90% van de roze diamant; sluiting = schaarste-verhaal |

### 3b. Winning — projecten
*(n.v.t. voor v1 — het aanbod groeit nauwelijks; grote mijnen lopen leeg (Argyle dicht, Jwaneng ondergronds).
De schaarste-kant zit al in de bestaande mijnen + de Argyle-sluiting.)*

### 3c. Sorteer-/handelshubs + slijperij (`type: hub` / `type: refinery`)
*Twee soorten knopen tussen mijn en markt: **handelshubs** (rough sorteren/verkopen/certificeren — Gaborone,
Antwerpen, Dubai; polished verhandelen — Mumbai, Ramat Gan) en de **slijperij** (`refinery` = waar rough
polished wordt: Surat = de trechter, China = klein). Antwerpen is sinds 2024 het **verplichte G7-certificerings-
knooppunt** → modelleer de niet-Russische rough fysiek via Antwerpen naar Surat.*

| id | naam | type | land | lat | lon | tier | rol |
|---|---|---|---|---|---|---|---|
| dia-gaborone | Gaborone (De Beers DBGSS / sights) | hub | Botswana | -24.65 | 25.91 | 1 | De Beers verplaatste de aggregatie/verkoop hierheen (2013, beneficiation); sights → sightholders |
| dia-antwerp | Antwerpen (AWDC) | hub | België | 51.22 | 4.42 | 1 | historische handelshoofdstad; **nu het G7-certificeringsknooppunt** (2024→); ~poort naar Surat |
| dia-dubai | Dubai (DMCC / Almas Tower) | hub | VAE | 25.09 | 55.14 | 1 | snelst groeiende rough-hub; herrouterings-luik voor Russische stenen; belastingvrij |
| dia-surat | Surat (slijperij) | refinery | India | 21.17 | 72.83 | 1 | **DE TRECHTER: ~90-95% van alle stenen geslepen/gepolijst**; ~1 mln slijpers (Gujarat) |
| dia-mumbai | Mumbai (Bharat Diamond Bourse) | hub | India | 19.07 | 72.87 | 1 | 's werelds grootste diamantbeurs; polished-handel + financiering + export |
| dia-china-cut | Guangzhou/Shenzhen (slijperij) | refinery | China | 23.13 | 113.26 | 2 | secundaire slijperij, vooral voor de eigen markt + grotere stenen |
| dia-ramat-gan | Ramat Gan (Israel Diamond Exchange) | hub | Israël | 32.08 | 34.81 | 3 | high-end grote stenen + handel/financiering (dun draadje) |
| dia-ny | New York (47th Street) | hub | VS | 40.76 | -73.98 | 3 | topsegment handel + zeer grote stenen; dicht bij de VS-eindmarkt |

### 3d. Havens / gateways
*(n.v.t. — diamant reist **per lucht**, niet over zee. De hubs zelf zijn de luchtpoorten; geen `port`-nodes,
geen zee-A\*. Dit is de goud/PGM-modus.)*

### 3e. Consumptie / eindmarkt (`type: market`)
| id | naam | land | lat | lon | tier | note |
|---|---|---|---|---|---|---|
| dia-mkt-us | VS — sieraden (verlovingsring) | VS | 40.71 | -74.00 | 1 | **#1: ~50% van de wereldvraag** naar polished; ook het front van de lab-grown-ontwrichting |
| dia-mkt-china | China / Hongkong — sieraden | China | 22.32 | 114.17 | 1 | #2-markt; teruggevallen sinds ~2022 (vastgoed/vertrouwen), maar structureel groot |
| dia-mkt-india | India — sieraden (binnenlands) | India | 28.61 | 77.21 | 2 | snelgroeiende eigen vraag (Delhi/Mumbai) naast de exportslijperij |
| dia-mkt-gulf | Golf — retail + re-export | VAE | 24.47 | 54.37 | 2 | Dubai/Abu Dhabi retail + toeristische doorverkoop |
| dia-mkt-eu | EU — luxe (Parijs/Genève) | Frankrijk | 48.85 | 2.35 | 2 | luxemerken (LVMH/Richemont); high-end |
| dia-mkt-japan | Japan — sieraden | Japan | 35.68 | 139.76 | 3 | stabiele high-end markt |

### 3f. Extra laag — **lab-grown diamant** (OPTIONELE toggle, **uitgesteld → aparte issue**)
> **Dit is het "anders"-stuk dat een aparte issue krijgt.** Lab-grown (kweekdiamant) is een *nieuwe optionele
> laag* (`layer:"labgrown"`) die de 5 gedeelde engine-bestanden raakt (`config/main/flows/markers/ui`) — net als
> uranium's militaire-toggle en olie's SPR. Omdat er **parallel een grafiet-sessie op de gedeelde engine loopt**
> (sectie J), bouw ik die laag **niet** in v1. In v1 leeft lab-grown alleen als **tension** (`dia-t-labgrown`).
> Het toggle-ontwerp (voor de latere issue): 2-3 productie-nodes (`type:"mine"`+`layer:"labgrown"`) — **China/
> Henan (Zhengzhou, HPHT-persen)** ~34.75/113.63 + **India/Surat (CVD)** ~21.20/72.90 — die de slijperij (Surat)
> én de VS-markt voeden met `layer:"labgrown"`-flows die de natuurlijke arcs ondergraven. Chip "lab-grown".

## 4. Stromen (flows) — indicatief, ~Mct/jr
*Modi: **`air`** (intercontinentaal — hergebruikt de goud/PGM great-circle-boog, buiten de A\* om) en **`road`**
(korte hops binnen een land/regio: mijn→Gaborone, Surat→Mumbai, hub→lokale markt). **Géén `ship`, géén nieuw
chokepoint.** De Antwerpen-certificering modelleren we als een **fysieke omweg**: niet-Russische rough gaat
mijn→(hub)→**Antwerpen**→Surat; Russische rough gaat om Antwerpen heen via Dubai/direct India.*

### 4a. Mijn → sorteer-/handelshub (stage `erts`) — rough verzamelt in Gaborone/Antwerpen/Dubai
| from | to | ~Mct | mode | note |
|---|---|---|---|---|
| dia-jwaneng | dia-gaborone | 12 | road | Debswana-rough → De Beers-aggregatie in Gaborone (binnen Botswana) |
| dia-orapa | dia-gaborone | 11 | road | idem |
| dia-venetia | dia-gaborone | 5 | road | ZA De Beers-rough → Gaborone-aggregatie (over de grens) |
| dia-namibia | dia-gaborone | 2 | air | mariene Namibische rough → De Beers-aggregatie |
| dia-alrosa | dia-dubai | 20 | air | **Russische rough herrouteert naar Dubai** (om de G7-sanctie/Antwerpen heen) |
| dia-alrosa | dia-surat | 12 | air | Russische rough **direct naar India** (Surat slijpt óók niet-G7-goederen) |
| dia-catoca | dia-antwerp | 5 | air | Angolese rough → Antwerpse tenders |
| dia-catoca | dia-dubai | 4 | air | Angolese rough → Dubai-tenders |
| dia-canada | dia-antwerp | 16 | air | Canadese rough → Antwerpen (certificering + handel) |
| dia-drc | dia-antwerp | 5 | air | Congolese rough → Antwerpen (deels edelsteen) |
| dia-drc | dia-surat | 4 | air | Congolese (industriële/laagwaardige) rough → India |
| dia-marange | dia-dubai | 5 | air | Zimbabwaanse rough via Dubai/Antwerpse tenders |
| dia-letseng | dia-antwerp | 1 | air | Lesothaanse grote stenen → Antwerpse veilingen |

### 4b. Handelshub → slijperij (stage `erts` → de convergentie op Surat)
| from | to | ~Mct | mode | note |
|---|---|---|---|---|
| dia-gaborone | dia-surat | 26 | air | **De Beers-sightholders sturen de rough naar India** — de dikste trechter-arc |
| dia-antwerp | dia-surat | 28 | air | **Antwerpen (gecertificeerd) → Surat** — het gros van de wereld-rough naar India |
| dia-dubai | dia-surat | 24 | air | **Dubai-rough → Surat** — inclusief de herrouteerde Russische stenen |
| dia-gaborone | dia-antwerp | 6 | air | deel van de De Beers-rough → Antwerpse handel |
| dia-antwerp | dia-china-cut | 4 | air | klein deel → Chinese slijperij |
| dia-dubai | dia-china-cut | 3 | air | idem via Dubai |
| dia-antwerp | dia-ramat-gan | 2 | air | high-end grote stenen → Israëlische slijperij (dun draadje) |

### 4c. Slijperij → polished-handel (stage `raffinaat`) — geslepen steen naar de beurs
| from | to | ~Mct | mode | note |
|---|---|---|---|---|
| dia-surat | dia-mumbai | 40 | road | **Surat → Bharat Diamond Bourse (Mumbai)**: polished naar de handel/export (binnen India) |
| dia-china-cut | dia-mkt-china | 7 | road | Chinese slijperij → eigen markt (binnenlandse lus) |
| dia-mumbai | dia-antwerp | 8 | air | polished terug naar de Antwerpse handel (herverkoop wereldwijd) |
| dia-mumbai | dia-dubai | 6 | air | polished naar Dubai (handel/re-export) |
| dia-ramat-gan | dia-ny | 2 | air | Israëlische high-end polished → New York-topsegment |

### 4d. Polished-hub → eindmarkt (stage `product`) — de sieradenvraag
| from | to | ~Mct | mode | note |
|---|---|---|---|---|
| dia-mumbai | dia-mkt-us | 18 | air | **India → VS: de grootste eindstroom** (~50% van de vraag) |
| dia-mumbai | dia-mkt-china | 8 | air | India → China/Hongkong |
| dia-mumbai | dia-mkt-india | 5 | road | India → eigen binnenlandse markt |
| dia-mumbai | dia-mkt-eu | 5 | air | India → Europese luxe |
| dia-mumbai | dia-mkt-gulf | 3 | air | India → Golf-retail |
| dia-mumbai | dia-mkt-japan | 2 | air | India → Japan |
| dia-antwerp | dia-mkt-eu | 3 | road | Antwerpse polished → Europese luxe (over land) |
| dia-antwerp | dia-mkt-us | 4 | air | Antwerpse high-end polished → VS |
| dia-dubai | dia-mkt-gulf | 3 | road | Dubai polished → lokale/Golf-retail |
| dia-ny | dia-mkt-us | 2 | road | New York-topsegment → VS-eindklant |

## 5. Knelpunten & de "knijp"
- Diamant heeft **géén geografisch zee-knelpunt** (het vliegt) → **géén nieuwe `wp-*`/`grens-*`**, precies zoals
  PGM. De knijp is **tweeledig**:
  1. **De Surat-slijptrechter** — ~90-95% van alle diamant geslepen in één stad. De scherpste downstream-
     concentratie van de atlas (scherper dan China-raffinage of Ganzhou-scheiding).
  2. **Antwerpen-certificering** — sinds maart 2024 moet niet-Russische rough via het "Antwerp node" worden
     gecertificeerd om de G7-markt te bereiken (sanctie op Alrosa). Een *institutioneel* knelpunt, gedragen door
     de fysieke omweg mijn→Antwerpen→Surat + een `tension` (zoals Ticino bij goud, Russische verrijking bij uranium).
- Onderliggend structureel: het **De Beers+Alrosa-duopolie** (kartel-verleden) en de **lab-grown-ontwrichting**.

## 6. Emergent plaatje-check (de lat bij oplevering)
1. Mijn-stippen verspreid over Siberië, zuidelijk Afrika, Canada, Angola — met de `note`'s die volume-vs-waarde
   verraden (Rusland volume, Botswana/Namibië/Lesotho waarde, DRC/Zimbabwe industrieel).
2. **Alle rough-arcs convergeren op Surat** (via Gaborone/Antwerpen/Dubai) — de dikste bundel van de kaart loopt
   naar één Indiase stad. Dát is het aha.
3. **Antwerpen** licht op als het knooppunt waar niet-Russische rough doorheen gaat; **Russische (Alrosa) rough
   buigt zichtbaar om Antwerpen heen** via Dubai/direct India — de sanctie-herrouting.
4. Vanaf **Mumbai** waaieren de polished-arcs uit naar de eindmarkten, met **VS veruit de dikste** (~50%).
5. Alles beweegt als **luchtbogen** (great-circle) — géén schepen (dat is de industriële metalen); de tijdlijn
   toont automatisch "✈ vluchten".
6. (Later, met de toggle) **lab-grown**: kweekdiamant-nodes in China/Henan + India die de VS-markt ondergraven.

## 7. Bronnen (peiljaar ±2023-2024)
- **Kimberley Process Certification Scheme (KPCS)** — ruwproductie-statistiek per land (volume Mct + waarde $):
  Rusland #1 volume (~35 Mct), Botswana #1 waarde, Canada/Angola/DR Congo/Zuid-Afrika/Zimbabwe/Namibië.
- **USGS Mineral Commodity Summaries 2025 (Diamond, industrial & gem):** landen-ranking + de industrieel-vs-
  edelsteen-splitsing; industriële diamant nu ~overwegend synthetisch.
- **De Beers / Debswana / Alrosa / Endiama** bedrijfs- en productierapportages; **De Beers Global Sightholder
  Sales (Gaborone)** — de beneficiation-verplaatsing van Londen naar Botswana (2013).
- **AWDC (Antwerp World Diamond Centre)** — Antwerpse rough/polished-doorvoer; **G7-sanctie op Russische diamant
  (maart 2024) + het Antwerpse certificeringsknooppunt (2024-2025 gefaseerd)**.
- **GJEPC (India) / Surat-slijpindustrie** — ~90-95% van de wereld-slijp/polijst in Surat; Bharat Diamond
  Bourse (Mumbai) als polished-handelscentrum.
- **Lab-grown:** Bain/AWDC Global Diamond Report — China (Henan/HPHT) + India (CVD) als producenten; prijsval van
  natuurlijke t.o.v. kweekdiamant in het VS-verlovingssegment.
- **Argyle-sluiting (Rio Tinto, 2020)** — het einde van ~90% van de wereld-roze-diamantproductie.

## 8. Open vragen / research-TODO (vóór of tijdens `diamond.js`)
- [ ] Volumes zijn indicatief (Mct ruw). De **volume↔waarde-discrepantie** (DRC/Zimbabwe volumineus-maar-goedkoop;
  Botswana/Namibië klein-maar-duur) is via `note` gemodelleerd, niet via een tweede metriek — als "indicatief" labelen.
- [ ] Rough-verdeling per hub (hoeveel Alrosa via Dubai vs. direct India; hoeveel De Beers via Gaborone vs.
  Antwerpen) is plausibel maar niet per contract nagetrokken.
- [ ] Surat-aandeel (~90-95%) is robuust; het exacte Chinese slijp-aandeel is klein en als één node gemodelleerd.
- [ ] Co-locatie-check: Surat (21.17/72.83) vs. Mumbai (19.07/72.87) ~230 km OK; Dubai-hub (25.09/55.14) vs.
  Golf-markt Abu Dhabi (24.47/54.37) ~90 km OK; China-slijperij (Guangzhou) vs. China-markt (Hongkong) ~120 km OK.
- [ ] Lab-grown-laag bewust **uitgesteld** (aparte issue) i.v.m. de parallelle engine-sessie (sectie J).

---

## Build-handoff (naar de bouw-issues)
- **Nieuwe 12e grondstof** — er is nog géén `data/diamond.js`: aanmaken + `<script src="data/diamond.js">`
  toevoegen aan `index.html` (na `silver.js`) + diamant-sanity-check in `build-standalone.py`. (Zoals zilver de
  11e was; grafiet/M14 is de laatste van de basis-10, diamant is een echte toevoeging.)
- **Géén nieuwe marker-types** — `mine`/`refinery`/`port`/`market`/`hub`/`airport` bestaan allemaal al
  (`hub` = handelshubs, `refinery` = slijperij met de treffende ruit-marker).
- **Géén nieuwe render-modus** — **air-mode** (hergebruikt de goud/PGM great-circle + lucht-voyages). Alleen
  korte hops binnen een land zijn `road`.
- **Géén nieuw chokepoint** — diamant vliegt; hergebruikt niets van `_chokepoints.js` (zoals PGM). De
  Antwerpen-omweg = data (mijn→Antwerpen→Surat), niet een `wp-*`.
- **Co-locatie-check** — houd diamant-nodes ~30-45 km uit elkaar (zie §8); geen `degDist:0`-arcs.
- **Lab-grown-toggle = APARTE, UITGESTELDE issue** (backlog) — nieuwe optionele laag `layer:"labgrown"` +
  `showLabGrown` in de 5 engine-bestanden; bouwen zodra de gedeelde tree schoon is (grafiet-sessie klaar).
  In v1 alleen als `tension` aanwezig.
