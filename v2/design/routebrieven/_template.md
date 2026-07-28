# Routebrief · <grondstof> — <mijn/bron> → <eindproduct> (<land>)

**stroom-id:** `<grondstof>-<van>-<naar>`  ·  **geschreven:** <datum>  ·  **status brief:** concept | in toets | vastgesteld
**Keten in één zin:** <bv. sulfide-erts uit X, per leiding naar de kust, over zee naar Y, per binnenvaart naar de
smelter, kathode per spoor naar de walsdraadfabriek, walsdraad per truck naar de kabelfabriek.>

*Volgens `../routebrief-werkwijze.md`. De brief loopt door tot het EINDPRODUCT — hij stopt niet
bij kathode/raffinaat. Elk been draagt dezelfde bewijslast, ook het laatste.*

*Doel: **zelfverificatie** — brief + eigen satellietpass maken de keten controleerbaar zonder
dat Lars hoeft te checken; alleen §5 (openstaande punten) komt bij hem terug.
**Notatie (hard):** coördinaten altijd **lat, lon** met **decimale punt**; ankers 5 decimalen,
passages 2–4. Elk been heeft een **been-id** `<stroom-id>-b<n>`; ankers dragen waar mogelijk
het id uit `aansluitingen.json`.*

---

## 1 · Ketenkaart

*Schematisch, met been-nummers en anker-ids. Toon waar deze streng samenvloeit met of splitst
van een andere brief. Dit is de inhoudsopgave van de rest van het document.*

```
<mijn>            ──(1 truck)──►  <poort/laadplek>
  <anker-id>                        ──(2 spoor)──►  <haven>   ──(3 zee)──►  <haven>
                                                     <anker>                 <anker>
  ◄── samenvloeiing: <andere brief> voegt hier in (been 4)
                                    ──(4 binnenvaart)──►  <smelter/raffinaderij>  <anker>
                                    ──(5 spoor)────────►  <fabriek>               <anker>
                                    ──(6 weg)──────────►  <eindproduct/markt>     <anker>
  ├── vertakking: <x>% gaat naar <bestemming> → eigen brief `<stroom-id>`
```

| | |
|---|---|
| **Fasen** | A mijn → zeehaven · B zee · C aanlanding → smelter/raffinaderij · D raffinaat → fabriek · E fabriek → eindproduct |
| **Benen** | <n> (doorlopend genummerd over de hele keten) |
| **Overslagen** | <n> (elke overslag = 2 ankers) |
| **Gedeelde benen** | <geen \| been <n> is identiek aan been <m> van `<andere brief>` — eigenaar: <brief>> |
| **Vertakkingen** | <geen \| na been <n> splitst <x>% af naar `<stroom-id>`> |
| **Reële alternatieven** | <geen \| been <n>: een deel lost werkelijk bij <plaats>, aandeel ~<x>% — zie punt-type *alternatief*> |

## 2 · Productvormen per fase — wat beweegt er fysiek

*De productvraag ("welk product is dit?") bepaalt welke kade, welk spoor en welk gebouw je
zoekt. Vul hem per fase in vóór je een coördinaat zoekt. Een gehalte-/rendementsregel maakt
de keten intern controleerbaar (past het volume van been N bij dat van been N+1?).*

| fase | product | vorm / verpakking | gehalte of specificatie | omzetting in de volgende stap | jaarvolume |
|---|---|---|---|---|---|
| A | <bv. concentraat> | <bulk / big bag / container / vloeibaar> | <bv. 28% Cu> | <bv. → blister 98%> | <kt> |
| B | | | | | |
| C | | | | | |
| D | <bv. kathode> | <bundels 2,5 t, LME-registreerbaar> | <99,99%> | <→ walsdraad 8 mm> | |
| E | <eindproduct> | | | <eindgebruik> | |

### 2a · De productvraag — van product naar kade

*Dit is het gereedschap dat de juiste haven én de juiste kade vindt: sneller en betrouwbaarder
dan zoeken op havennaam en dan inzoomen. Vul de ladder in voor **elke** overslag-, laad- en
losplek, zodat de keuze navolgbaar is en een fout in stap 2 niet stil doorwerkt in stap 6.*

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, in welke fysieke vorm? | <bv. kathode, bundels van 2,5 t> |
| 2 | Welke soort faciliteit hoort daarbij? | <bv. LME-erkend entrepot voor non-ferro; bulkterminal met transportband; containerterminal; vloeibaar-bulk jetty; ertsveld met portaalkraan> |
| 3 | Welke partijen doen dat op deze plek? | <bv. de erkende entrepothouders ter plaatse: A, B, C> |
| 4 | Welke daarvan hoort bij déze stroom? | <operator/afnemer/concessiehouder + waarom> |
| 5 | Welke kade / welk adres / welk spoor? | <bv. kadenaam + nummer, lengte, wat er behandeld wordt> |
| 6 | Coördinaat + satellietbevestiging | <lat, lon> — Esri z16, <datum>, zichtbaar: <kranen / wagons / stapels / steiger> |

**Wat de productvorm UITSLUIT** — *<bv. containervormig product lost niet aan een bulk-t-dock
met transportband; slurry eindigt bij de indikkers en niet aan de pier; LME-kathode gaat niet
naar een containerhaven op eilanden voor de kust.>* Noteer dit expliciet: een uitsluiting is
vaak sterker bewijs dan een bevestiging, en hij levert meteen de negatieve ankers.

### 2b · De overslagregel

Een overslag is **nooit één punt**, en een overslag is **elke drager-wissel** — óók binnen
dezelfde modaliteit: container-transshipment (deepsea → feeder) en lightering (groot
zeeschip → rivierschip) zijn overslagen, ook al blijft het "schip". Elke overslag krijgt
minstens twee ankers — waar been N aankomt en waar been N+1 vertrekt — plus de
terreinstappen ertussen (opslag, indikker, filter, stockpile, silo, rangeerbundel). Eén
coördinaat kan niet tegelijk kade-einde en vaarwegbegin zijn; wordt dat toch afgedwongen,
dan hoort er een tweede aansluiting te komen, geen compromis-coördinaat.
**Anker ≠ routeerpunt:** een schip vaart in de geul, een trein op het doorgaande spoor —
noteer op water en spoor beide punten + de maximaal verwachte snap-afstand.

## 3 · Kernfeiten die de vorm van de keten bepalen

*3–6 stuks. Alleen feiten die iets aan de LIJN veranderen (een arm, een kade, een modaliteit,
een tussenhaven). Elk feit met bronverwijzing.*

1. <…> [<bron>]
2. <…> [<bron>]

---

# FASE A · <mijn> → <zeehaven>

## Been 1 · <modaliteit> — <van> → <naar>

**been-id:** `<stroom-id>-b1`
**Modaliteit:** <truck / spoor / leiding / transportband>
**Lengte:** gemeten <…> km / gepubliceerd <…> km (<±…%>)
**Net / bron geometrie:** <OSM-wegcorridor / spoornet / AIS-tracks / handmatig satelliet-gelegd>
**Stippel:** nee | ja — reden: <geen net / eigen verbinding>
**Corridor bij naam:** <bv. N380 → N1 / Vía Ferroviaria Albania–Puerto Bolívar>
**Routeerpunt kop / staart:** <lat, lon> · <lat, lon> — max snap <…> m (anker ≠ routeerpunt)
**Toets-marge:** default (2 km passages · 100 m kop/staart) | afwijkend per punt: <#: … km — reden>

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **<laadplek op het terrein>** | laadplek | <…, …> | [<bron>] | **satelliet-gelegd** |
| 2 | | <weegbrug / terreinweg / poort> | poort | | | |
| 3 | | <eerste openbare weg / aansluiting op het net> | kruising | | | |
| 4 | | <plaats> | passage | | | |
| 5 | | <splitsing> + het punt dat de gekozen tak pint | kruising | | | |
| … | | | | | | |
| n | | <havenpoort / laadspoor / kade> | overslag | | | **satelliet-gelegd** |

**Opmerkingen been 1.** <Wat onzeker is en waarom; wat er nog gemeten moet worden.>

**Negatieve ankers been 1** — mét coördinaat + verbodsstraal, anders is het verbod niet toetsbaar:

| punt | lat, lon | straal | reden |
|---|---|---|---|
| <plaats / arm / haven waar de lijn NIET mag komen> | <…, …> | <… km> | <bv. containerhaven — past niet bij de productvorm> |

## Overslag <been 1 → been 2> — <plaatsnaam>

**Productvraag:** <stap 2 → stap 5 uit §2a in één zin: welk soort faciliteit, en dus welke kade.>

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 1 | <losplek / kopspoor / einde leiding> | losplek | | | **satelliet-gelegd** |
| 2 | terrein | <opslag, indikker, filterinstallatie, stockpile, silo> | verwerkingsstap | | | |
| 3 | vertrek been 2 | <ligplaats / laadspoor / kraanpositie> | laadplek | | | **satelliet-gelegd** |

**Routeerpunt ≠ anker.** Routeerpunt <…, …>, afstand tot het anker <…> m.

---

# FASE B · zee

## Been 2 · zee — <haven> → <haven>

**been-id:** `<stroom-id>-b2`
**Modaliteit:** zeeschip <klasse/type>  ·  **Router:** zee = vrij geroutet (werkwijze §6)
**Lengte:** gemeten <…> km  ·  **Overslagen onderweg:** <geen | transshipment bij <hub> — eigen overslag-blok>
**Routeerpunt kop / staart:** <lat, lon> · <lat, lon> — max snap <…> m (het schip vaart in de geul)

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | **<vertrekligplaats>** | laadplek | | | **satelliet-gelegd** |
| 2 | <zeestraat / kanaal / kaap als sanity-anker> | passage | | | |
| 3 | **<aankomstligplaats of riviermond>** | overslag | | | **satelliet-gelegd** |

**Negatieve ankers been 2:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| <bv. Panamakanaal> | <…, …> | <… km> | <de echte stroom vaart om de Kaap> |
| <bv. containerhaven X> | <…, …> | <… km> | <productvorm: bulk lost daar niet> |

---

# FASE C · aanlanding → smelter / raffinaderij

## Been 3 · <binnenvaart / spoor / weg> — <van> → <naar>

**been-id:** `<stroom-id>-b3`
**Modaliteit:** <…>  ·  **Brief-gestuurd** (werkwijze §6: geen vrije Dijkstra)
**Lengte:** gemeten <…> km / officieel <…> (<±…%>)  ·  **km-kolom =** <officiële kilometrering vanaf …>
**Stippel:** nee | ja — reden: <…>
**Routeerpunt kop / staart:** <lat, lon> · <lat, lon> — max snap <…> m
**Toets-marge:** default | afwijkend per punt: <#: … km — reden>

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | <vaarweg-overgang / eerste knoop> | vaarweg-overgang | | | |
| 2 | | <stad aan de route> | passage | | | |
| 3 | | <sluis / kering / brug met hoogtebeperking> | sluis/kering | | | |
| 4 | | <splitsing: welke arm> + pinpunt erna | kruising | | | |
| 5 | | <oriëntatiepunt naast de route> | referentie (niet aan lijn) | | | |
| 6 | | <loshaven waar een déél van de stroom werkelijk lost — lightering/alternatief> | alternatief (aandeel ~<x>%) | | | |
| n | | **<kade van de smelter/raffinaderij>** | losplek | | | **satelliet-gelegd** |

**Negatieve ankers been 3:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| <verkeerde arm / sluiproute / haven> | <…, …> | <… km> | <…> |

## Been 4 · last mile — <kade/losspoor> → <fabriekspoort> → <losplek op terrein>

*Eigen been, geen rechte stub (werkwijze §3.4). Kleine wegklassen (`residential`/`service`/
`tertiary`/`unclassified`) tellen mee binnen ~12 km van plant en kade.*

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | <kade / losspoor> | losplek | | | **satelliet-gelegd** |
| 2 | | <havenstraat / aansluitspoor> | passage | | | |
| 3 | | <fabriekspoort> | poort | | | |
| 4 | | **<losplek op het terrein>** | losplek | | | **satelliet-gelegd** |

## Verwerkingsknoop · <naam raffinaderij / smelter>

| | |
|---|---|
| **anker-id** | `<id uit aansluitingen.json>` |
| **eigenaar van dit anker** | deze brief \| `<andere brief>` |
| **in** | <product fase C> — <volume>, waarvan <…> uit deze streng |
| **andere ingaande strengen** | <geen \| `<stroom-id>` levert <…> — zie die brief> |
| **uit** | <product fase D> — <volume> |
| **uitgaande strengen** | deze brief <x>% · `<stroom-id>` <y>% |
| **verlies / bijproduct** | <slak, zwavelzuur, edelmetaalslib → eigen bestemming?> |

---

# FASE D · <raffinaat, bv. kathode> → fabriek

## Been 5 · last mile uitgaand — <laadplek op terrein> → <poort> → <net>

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **<laadplek: laadspoor, laadkuil, kade>** | laadplek | | | **satelliet-gelegd** |
| 2 | | <poort> | poort | | | |
| 3 | | <aansluiting op het openbare net> | kruising | | | |

## Been 6 · <spoor / weg / zee> — <raffinaderij> → <fabriek>

**been-id:** `<stroom-id>-b6`
**Modaliteit:** <…>  ·  **Lengte:** gemeten <…> km / gepubliceerd <…>  ·  **Stippel:** <…>
**Let op bij container/stukgoed:** vaart dit als lijndienst, dan is de vraag *direct of via
een transshipment-hub?* — een hub is een overslag (eigen blok), en "hub onbekend" is een
openstaand punt (§5), geen reden voor een rechte lijn.
**Routeerpunt kop / staart:** <lat, lon> · <lat, lon> — max snap <…> m

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | <vertrek> | laadplek | | | **satelliet-gelegd** |
| 2 | | <plaats / station / knooppunt> | passage | | | |
| … | | | | | | |
| n | | **<losplek fabriek>** | losplek | | | **satelliet-gelegd** |

**Negatieve ankers been 6:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| <…> | <…, …> | <… km> | <…> |

## Verwerkingsknoop · <naam fabriek>

*Zelfde tabel als bij de vorige verwerkingsknoop. Hier hoort de vraag: wat komt er nog NA dit
product? Zolang het antwoord "nog een bewerking elders" is, gaat de brief door.*

| | |
|---|---|
| **anker-id** | `<id>` |
| **in** | <bv. kathode> — <volume> |
| **andere ingaande strengen** | <bv. schroot uit `<stroom-id>`; tweede kathode-leverancier> |
| **uit** | <bv. walsdraad 8 mm> — <volume> |
| **uitgaande strengen** | <…> |

---

# FASE E · fabriek → eindproduct / markt

## Been 7 · <modaliteit> — <fabriek> → <eindfabriek / distributie / markt>

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | <laadplek> | laadplek | | | **satelliet-gelegd** |
| … | | | | | | |
| n | | **<eindpunt van de keten>** | losplek (keten-eind) | | | **satelliet-gelegd** |

**Waar de keten eindigt, en waarom daar.** *<Bv.: bij de kabelfabriek, want daarna gaat het
product als eindproduct de markt op en is er geen gedocumenteerde volgende locatie. Of: bij een
markt-centroïde — dan expliciet als centroïde markeren, want dat is géén anker.>*

---

## 4 · Samenvloeiingen en vertakkingen (overzicht)

| # | been | soort | met welke brief | wat gedeeld wordt | eigenaar anker |
|---|---|---|---|---|---|
| 1 | <n> | samenvloeiing | `<stroom-id>` | <anker + been-geometrie> | <brief> |
| 2 | <n> | vertakking | `<stroom-id>` | <anker> | <brief> |

**Regel:** één brief = één streng. Een gedeeld been wordt in **één** brief volledig
uitgeschreven; de andere brief verwijst ernaar en herhaalt de puntenlijst niet — anders lopen
twee versies van dezelfde corridor stil uit elkaar.

## 5 · Openstaande punten

| # | been | wat | waarom onzeker | wat het zou oplossen |
|---|---|---|---|---|
| 1 | | | | <z18-pass / één coördinaat van Lars / bron X> |

## 6 · Conflicten met de projectdata (afwerklijst)

| # | wat | nu | hoort te zijn | bron |
|---|---|---|---|---|
| 1 | <node/flow/anker in `data/*.js` of `aansluitingen.json`> | <huidige waarde> | <correcte waarde> | [<bron>] |

## 7 · Wat de kaart moet tekenen

1. **Been 1** (<doorgetrokken/gestippeld>): <van> → <naar>, <bijzonderheden>.
2. **Been 2** …
3. **Referentiemarkers** (niet aan de lijn): <…>.
4. **Kleur / modaliteit per been:** <…>.

## 8 · Toets-checklist (invullen bij de controle)

- [ ] **Notatie:** alle coördinaten lat, lon met decimale punt; ankers op 5 decimalen
- [ ] Elk been heeft een **been-id**; ankers dragen waar mogelijk het `aansluitingen.json`-id
- [ ] Elke laadplek, overslag en losplek heeft status **satelliet-gelegd** (z16) — door de maker zelf gelegd
- [ ] Elke laad-/los-/overslagplek heeft een ingevulde **productvraag** (§2a), inclusief de uitsluitingen
- [ ] Elke overslag (óók transshipment/lightering) heeft **twee** ankers + de terreinstappen ertussen
- [ ] **Routeerpunt + max snap** genoteerd bij elk been-uiteinde op water en spoor
- [ ] **Dekking:** de gerouteerde lijn raakt alle *bevestigde* punten in volgorde
      (default-marge 2 km passages / 100 m kop en staart; afwijkingen per punt in het been-kopblok)
- [ ] **Verklikker:** geen enkele plaats geraakt die niet in de brief staat
- [ ] Geen enkel **negatief anker** binnen zijn verbodsstraal geraakt
- [ ] Lengte per been binnen de tolerantie t.o.v. de gepubliceerde waarde — mét vermelding van
      gereedschap, beide eindpunten en netstadium
- [ ] Volumes sluiten aan over de verwerkingsknopen heen (§2)
- [ ] Elke stippellijn draagt een **reden**; elk reëel **alternatief** heeft een aandeel of een openstaand punt
- [ ] De keten loopt door tot het eindproduct, of het stoppunt is beargumenteerd (fase E)

## 9 · Bronnen

**<Fase/gebied> [X..]:** X1 <bron, wat het levert, licentie> · X2 <…>
**<Fase/gebied> [Y..]:** Y1 <…>
**Eigen metingen:** <satelliet-overlay Esri z16 <datum> · `toets_ankers.py` · `toets_spoorroute.mjs` · …>
