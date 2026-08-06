# Routebrief · koper — Collahuasi → Tongling → elektronicakoperfolie (China)

**stroom-id:** `koper-collahuasi-tongling`  ·  **geschreven:** 2026-07-28, omgezet naar het mijn-tot-eindproduct-format + fase D/E toegevoegd 2026-07-29  ·  **status brief:** in toets (fase A–C gelegd en live; fase D/E nieuw — satellietpass open)
**Keten in één zin:** sulfide-concentraat uit Collahuasi als slurry per **leiding** naar Puerto Patache (192,4 km — als enige leiding van de atlas mét gekarteerd tracé), na indikken/filteren per **zeeschip** naar de Yangtze, per **binnenvaart** (~550 rivier-km) door de **oostgeul** naar de kade van het TNMG-smeltercomplex in Tongling, daar tot **kathode**, en de kathode groepsintern (grotendeels via een draad-/铜丝-tussenstap) naar de **koperfoliefabriek van 铜冠铜箔** in dezelfde ontwikkelingszone; de folie gaat naar PCB-laminaat- en batterijfabrikanten — daar stopt de brief beargumenteerd.

*Volgens `../routebrief-werkwijze.md`. De brief loopt door tot het EINDPRODUCT — hij stopt niet
bij kathode/raffinaat. Elk been draagt dezelfde bewijslast, ook het laatste.*

*Doel: **zelfverificatie** — brief + eigen satellietpass maken de keten controleerbaar zonder
dat Lars hoeft te checken; alleen §5 (openstaande punten) komt bij hem terug.
**Notatie (hard):** coördinaten altijd **lat, lon** met **decimale punt**; ankers 5 decimalen,
passages 2–4. Elk been heeft een **been-id** `koper-collahuasi-tongling-b<n>`; ankers dragen waar
mogelijk het id uit `aansluitingen.json`.*

*Herkomst: vierde routebrief van het project (2026-07-28, aangescherpt formaat). Bij de omzetting
op 2026-07-29 zijn drie lon,lat-regels uit het oude been 3 (noord-junctie, kade, referenties)
naar lat, lon gecorrigeerd — zie de notatie-noot onder been 3.*

---

## 1 · Ketenkaart

```
Collahuasi — pompstation      ──(b1 slurryleiding, 192,4 km — eigen verbinding)──►  Puerto Patache
  `cu-collahuasi-laad`                                                              espesadores → moly-/filterplant → stockpile
                                                                                    → kop laadsteiger  `cu-patache-kade`
                              ──(b2 zee, vrij geroutet; monding 吴淞口 = rivier-km 0)──►  losligplaats benedenrivier
                                                                                    (Nantong — gedocumenteerd, ligplaats open)
  ├── alternatief: een deel van het zeebeen lost werkelijk bij Zhangjiagang / Jiangyin (aandeel onbekend)
                              ──(b3 binnenvaart, ~550 rivier-km; stedenlijst)──►  noordpunt eiland → oostgeul
                                                                                  → kade TNMG  `cu-tongling-kade`
                              ═══ verwerkingsknoop: TNMG-smeltercomplex 铜陵经开区 (金冠 76万 + 金新 50万 t/a) ═══
                              ──(b4 last mile kathode: terrein → poort → net — ankers open)──►
                              ──(b5 weg, binnen de 经开区 — lengte n.t.b.)──►  铜冠铜箔, basis Tongling (folie)
  ├── vertakking: kathode/铜丝 → 铜冠铜箔-bases Chizhou en Hefei · 芜湖铜冠电工 (draad) · SHFE-entrepots
  │                Wuxi/Changzhou/Suzhou/Shanghai · 铜板带-tak — elk aandeel onbekend, geen eigen brief
                              ──(fase E: folie → PCB-laminaat (生益科技 c.s.) en batterij (BYD) — beargumenteerd stoppunt)
```

| | |
|---|---|
| **Fasen** | A mijn → zeehaven · B zee · C aanlanding → smelter · D kathode → foliefabriek · E folie → markt |
| **Benen** | 5 (doorlopend genummerd; fase E krijgt bewust géén been — zie het stoppunt) |
| **Overslagen** | 2 uitgewerkte blokken (Patache · benedenrivier) — 4 anker-slots, waarvan 1 satelliet-gelegd (kop laadsteiger Patache), 1 kandidaat zonder coördinaat (espesadores), 2 open (losligplaats zeeschip · laadligplaats binnenvaart) |
| **Gedeelde benen** | geen — geen andere brief deelt een been met deze streng |
| **Vertakkingen** | na de smelter-knoop: 铜冠铜箔 Chizhou/Hefei · 芜湖铜冠电工 · SHFE-entrepots (Jiangsu/Shanghai) · 铜板带-tak — aandelen onbekend (§4, §5) |
| **Reële alternatieven** | been 2/3: een deel van het concentraat lost werkelijk bij **Zhangjiagang** of **Jiangyin** — punt-type *alternatief*, aandeel onbekend (§5) |

## 2 · Productvormen per fase — wat beweegt er fysiek

| fase | product | vorm / verpakking | gehalte of specificatie | omzetting in de volgende stap | jaarvolume |
|---|---|---|---|---|---|
| A | Cu-concentraat | **slurry** in de leiding; na espesadores → filterplant **droge bulk** | niet in projectdata vastgelegd | 4 t concentraat → 1 t ruwkoper (blister) [D4] | niet vastgelegd |
| B | Cu-concentraat | droge bulk, scheepsruim bulkcarrier | idem | — | — |
| C | Cu-concentraat | droge bulk, binnenvaartruim | idem | → anode → kathode | smeltercomplex: 金冠 760 kt/a [D3] + 金新 500 kt/a [D1][D2] |
| D | **kathode** | bundels; SHFE-warrant = 25 t; GB/T 467: Cu+Ag ≥ 99,95% [D7] | LME-/SHFE-leverbare klasse | → 铜丝/铜杆 (draad) → elektrolytische folie; deel direct verkocht | TNMG-verwerking totaal > 400 kt/a [D3] |
| E | **elektronicakoperfolie** (PCB- + lithiumfolie) | rollen | — | → copper-clad laminate/PCB · anodefolie batterij | 铜冠铜箔 55 kt/a, uitbreidend naar 80 [D5] |

### 2a · De productvraag — van product naar kade

*Ingevuld voor elke laad-, overslag- en losplek. Een fout in stap 2 mag niet stil doorwerken in stap 6.*

**Ladder 1 — kop slurryleiding Collahuasi (vertrek been 1, laadplek mijnzijde)**

*Toegevoegd bij de toets van 2026-07-29 — deze laadplek miste als enige een ladder. Nuance: dit
is een pijpleidingkop op eigen mijnterrein (eigen verbinding, geen gedeeld net), dus het
kade-víndende doel van de ladder speelt hier nauwelijks; werkwijze en sjabloon vragen hem
echter bij élke laad-, overslag- en losplek, en de uitsluitingen houden hun waarde.*

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, in welke fysieke vorm? | Cu-concentraat als **slurry**, ná de molen — het erts uit de putten gaat naar de molen, niet de pijp in [P1] |
| 2 | Welke soort faciliteit? | pompstation aan de kop van de eigen slurryleiding, op het mijnterrein — geen kade of overslag; eigen verbinding, geen gedeeld net (`modi: []` in `aansluitingen.json`) |
| 3 | Welke partijen op deze plek? | alleen Collahuasi — eigen terrein, eigen leiding; er valt hier geen operator of kade te kiezen |
| 4 | Welke hoort bij déze stroom? | Collahuasi zelf — de kop van de leiding is het vertrekpunt van been 1 |
| 5 | Welke kade / welk laadpunt? | geen kade — het laadpunt is de kop van de leiding (pompstation), 1,9 km van Rajo Ujina en 2,3 km van het mijncomplex; anker `cu-collahuasi-laad` |
| 6 | Coördinaat + satellietbevestiging | **-20.97783, -68.64395** — [P1]-coördinaat, satelliet-check doorstaan 2026-07-28 (Esri z16); status **bevestigd** (been 1, punt 1) — niet satelliet-gelegd, want niet door de maker zelf op de overlay gelegd |

**Wat de productvorm UITSLUIT:** slurry vertrekt bij het pompstation ná de molen — de putten
zelf (Rajo Ujina / Rajo Rosario) zijn níet het laadpunt; en aan de mijnzijde bestaat geen kade,
spoor of overslag — de drager ís de leiding, dus elk haven- of laadspoor-achtig punt zou hier
per definitie fout zijn.

**Ladder 2 — Patache (overslag been 1 → been 2, laadplek zee)**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, in welke fysieke vorm? | concentraat als **slurry** in de leiding; ná espesadores → moly-plant → filterplant → stockpile als **droge bulk** [P2] |
| 2 | Welke soort faciliteit? | eigen concentraatterminal: indikkers + filtergebouw + overdekte stockpile + laadsteiger met band naar een bulkcarrier |
| 3 | Welke partijen op deze plek? | Collahuasi (eigen terminal); de aparte, noordelijker pier (o.a. kolencentrale) is een ándere terminal |
| 4 | Welke hoort bij déze stroom? | Collahuasi zelf — Patache is de eigen terminal van de mijn [P1][P2] |
| 5 | Welke kade / welk laadpunt? | de kop van de laadsteiger — de ligplaats van de bulkcarrier, 286 m NW van de walkant |
| 6 | Coördinaat + satellietbevestiging | **-20.80270, -70.19890** — Esri z16, 2026-07-28, zichtbaar: steiger met ligplaats; anker `cu-patache-kade` |

**Wat de productvorm UITSLUIT:** slurry eindigt bij de indikkers, niet aan de pier — het leidingeind
en de scheepsligplaats kúnnen niet één punt zijn; concentraat is geen containerlading (geen
containerterminal); de kolen-pier noordelijker hoort niet bij deze stroom.

**Ladder 3 — losligplaats benedenrivier (overslag been 2 → been 3)**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, in welke fysieke vorm? | Cu-concentraat, droge bulk in de ruimen van een zeeschip |
| 2 | Welke soort faciliteit? | bulk-losligplaats met kranen/grijpers + douane-/entrepotfunctie voor geïmporteerd concentraat; daarna belading binnenvaart |
| 3 | Welke partijen doen dat op de benedenrivier? | Nantong (gedocumenteerde loshaven voor geïmporteerd concentraat richting TNMG [D4]; 165 partijen concentraat in 2017 [D10]) · Zhangjiagang · Jiangyin (bekende concentraat-loshavens [Y2]) · Luojing/Baogang-bulkpier (aanlandingsalternatief [T2]) |
| 4 | Welke hoort bij déze stroom? | **Nantong** — "国外进口铜精砂到南通港卸货后沿长江水运到公司" (geïmporteerd concentraat lost bij Nantong en gaat per Yangtze-binnenvaart naar het bedrijf) [D4]; let op: de klassieke **江心-ankerplaats-overslag** bij Nantong is eind 2017 beëindigd [D10] → het is nu een walligplaats |
| 5 | Welke kade? | **niet vastgepind** — openstaand punt (§5); geen coördinaat verzonnen |
| 6 | Coördinaat + satellietbevestiging | open — z16-pass ná plaatsbepaling |

**Wat de productvorm UITSLUIT:** concentraat komt **niet** binnen op een containerhaven — Yangshan
(containerhaven op eilanden vóór de kust) is uitgesloten [T2]; en een zeeschip komt **niet boven
Nanjing** (brughoogte ~24 m [Y3]), dus de losligplaats ligt op de benedenrivier.

**Ladder 4 — kade TNMG-smeltercomplex (losplek been 3)**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, in welke fysieke vorm? | Cu-concentraat, droge bulk in binnenvaartruimen |
| 2 | Welke soort faciliteit? | eigen loskade van de smelter aan de oostgeul, met kranen en opslag op het terrein erachter |
| 3 | Welke partijen op deze plek? | TNMG — het smeltercomplex in de 铜陵经开区 ligt "毗邻长江" (pal aan de Yangtze) [D3-omgeving]; de oude, gesloten smelter zuidelijker hoort er niet bij [T1] |
| 4 | Welke hoort bij déze stroom? | de kade van de **nieuwe** TNMG-smelter (aangewezen door Lars: roze = kade, blauw = smelter) [T1] |
| 5 | Welke kade? | oostgeul-kade: kade-tip 30.98236, 117.77170 → begin 30.99133, 117.77190; smelterterrein erachter op 30.98656, 117.78060 |
| 6 | Coördinaat + satellietbevestiging | **30.98656, 117.77180** — satelliet-gelegd (Esri z14, 2026-07-24, go Lars; z16-hercheck 2026-07-28 ongewijzigd); anker `cu-tongling-kade` |

**Wat de productvorm UITSLUIT:** bulk-concentraat lost niet bij een containerkade; de doorgaande
vaart hoort door de **oostgeul**, niet de west-arm (die is in de bake weggeknipt [T1]).

**Ladder 5 — kathode-laadplek smelterterrein (fase D, vertrek been 4)**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, in welke fysieke vorm? | kathode in bundels (warrant-eenheid 25 t [D7]) — stukgoed, truckable |
| 2 | Welke soort faciliteit? | expeditie-/magazijnhal met weegbrug aan de wegkant van het terrein; eventueel laadkade (het complex ligt aan de rivier) of laadspoor |
| 3 | Welke partijen? | TNMG zelf (groepsinterne leveringen aan 铜冠铜箔 c.s. [D6]); externe verkoop en eventuele SHFE-levering |
| 4 | Welke hoort bij déze stroom? | de expeditie van 金新铜业 (het nieuwe 500 kt/a-blok, ontstoken 2025-03-26 [D1][D2]) — terreingrens met 金冠铜业 nog aan te wijzen (§5) |
| 5 | Welke hal / welk laadpunt? | **niet vastgepind** — openstaand punt (§5) |
| 6 | Coördinaat + satellietbevestiging | open — z16-pass nodig; nieuw D/E-punt krijgt hoogstens "bevestigd" tot die pass gedaan is |

**Wat de productvorm UITSLUIT:** kathode gaat **niet** over de concentraatband en niet door een
bulkruim zonder verpakking; de laadplek is dus een ándere plek dan de concentraat-loskade — één
kade-coördinaat kan niet beide zijn.

**Ladder 6 — losplek foliefabriek 铜冠铜箔, basis Tongling (fase D, einde been 5)**

| stap | vraag | antwoord |
|---|---|---|
| 1 | Welk product, in welke fysieke vorm? | kathode-bundels en/of 铜丝 (koperdraad — het volumineuzere inkoopproduct van de foliefabriek [D6]) per truck |
| 2 | Welke soort faciliteit? | elektrolytische foliefabriek: oploshal (draad/kathode in zwavelzuur), foliemachines, rollenmagazijn — losdock aan de hal |
| 3 | Welke partijen? | 铜冠铜箔 (安徽铜冠铜箔集团, beursgenoteerd 301217) — foliebases in **Tongling, Chizhou en Hefei** [D5] |
| 4 | Welke hoort bij déze stroom? | de **basis Tongling** — fase 1 van het 2万吨-project draait er sinds december 2017, in de 铜陵经开区, dezelfde zone als de smelter [D5]; ~68% van de kathode-inkoop komt intern van TNMG [D6] |
| 5 | Welk adres / welke kavel? | **niet vastgepind** binnen de 经开区 — openstaand punt (§5) |
| 6 | Coördinaat + satellietbevestiging | open — z16-pass ná adresbepaling |

**Wat de productvorm UITSLUIT:** folie-grondstof komt aan als stukgoed op trucks — geen kade of
bulkoverslag nodig; een gepind punt op een kade of ertsveld zou hier per definitie fout zijn.

### 2b · De overslagregel

Een overslag is **nooit één punt**, en een overslag is **elke drager-wissel** — óók binnen dezelfde
modaliteit (transshipment, lightering). Elke overslag krijgt minstens twee ankers — waar been N
aankomt en waar been N+1 vertrekt — plus de terreinstappen ertussen. Eén coördinaat kan niet
tegelijk leiding-eind en zeebeen-begin zijn; wordt dat toch afgedwongen, dan hoort er een tweede
aansluiting te komen, geen compromis-coördinaat. **Anker ≠ routeerpunt:** een schip vaart in de
geul, een trein op het doorgaande spoor — noteer op water en spoor beide punten + de maximaal
verwachte snap-afstand.

## 3 · Kernfeiten die de vorm van de keten bepalen

1. **De leiding ís gekarteerd** — anders dan bij Escondida. Het tracé Collahuasi→Patache is uit
   **14 OSM-ways met `substance=slurry`** gestikt tot 1.363 punten en meet **192,4 km tegen ±200
   gepubliceerd (−3,8%)** [P1]. **7 van die 14 ways dragen tegelijk `highway=track` +
   `surface=dirt`**: de pijp ligt begraven onder zijn eigen onderhoudsweg — dat is meteen de beste
   onafhankelijke bevestiging dat het tracé klopt, want die zandweg is op de satelliet zichtbaar.
2. **De leiding eindigt niet bij de pier maar bij de indikkers.** Collahuasi's eigen materiaal
   geeft de keten ná de leiding: *espesadores → planta de molibdeno → planta de filtro →
   stockpile → embarque* [P2]. Er zitten dus **vier verwerkingsstappen** tussen het eind van de
   leiding en het schip; die horen niet in één punt samengeperst.
3. **Patache is Collahuasi's eigen terminal**, niet de haven Antofagasta waar `data/copper.js` de
   stroom heen stuurt (~317 km zuidelijker — zie het negatieve anker in been 2).
4. **Tongling ligt aan de oostgeul, niet aan de hoofdgeul.** De kade van de nieuwe TNMG-kopersmelter
   ligt op de oostelijke arm om het eiland; het schip komt van benedenstrooms, gaat bij de noordpunt
   de oostgeul in en zakt naar de kade. Die geul is 2026-07-24 handmatig satelliet-gelegd omdat OSM
   hem alleen als onvolledig watervlak kent — zie `data/vaarwegen-handmatig.geojson` [T1].
5. **Nantong is de gedocumenteerde losplek van het geïmporteerde concentraat**: "国外进口铜精砂到
   南通港卸货后沿长江水运到公司" — gelost bij Nantong, daarna per Yangtze-binnenvaart naar het
   bedrijf; 1 t ruwkoper vraagt 4 t concentraat, dus de waterligging scheelt fors in vrachtkosten
   [D4]. De klassieke **江心-ankerplaats-overslag** bij Nantong (concentraat was er een
   "merk-goederensoort") is eind 2017 beëindigd [D10] — de hedendaagse losplek is een walligplaats,
   nog te pinnen.
6. **De keten stopt niet bij de kathode.** Het aangewezen smelterterrein is sinds 2025 een
   dúbbel complex: **金冠铜业** (Jinguan, "dubbel-flash" + Ausmelt, 760 kt/a kathode — grootste
   enkelvoudige matsmelter van China [D3]) én het nieuwe **金新铜业** (Jinxin, "铜基新材料"-project:
   500 kt/a, 10,3 mrd yuan, bouw gestart december 2022, flash-oven ontstoken 2025-03-26, met
   smelten, elektrolyse, zwavelzuur, **koperverwerking** en slakflotatie op één terrein [D1][D2]).
7. **De kathode blijft grotendeels in de eigen groep en in de Yangtze-gordel.** TNMG's
   verwerkingstak (folie, plaat/band, gelakte draad, fosforkoperballen, staf) draait > 400 kt/a
   "met de Anhui-Yangtze-gordel als kern" [D3]; foliedochter **铜冠铜箔** koopt **~68%** van zijn
   kathode intern en begroot voor 2026 496 mln yuan kathode + 3.195 mln yuan 铜丝 (koperdraad) aan
   inkoop bij TNMG [D6] — de folie-voeding loopt dus deels via een draad-tussenstap.
8. **Er is géén SHFE-entrepot in Tongling of elders in Anhui.** De aangewezen
   kathode-entrepots clusteren in Shanghai, Jiangsu (Wuxi, Suzhou, Changzhou), Zhejiang en
   Guangdong [D7] — SHFE-levering is dus een eigen vertakking ~300 km stroomafwaarts, geen
   eigenschap van het smelterterrein.

---

# FASE A · Collahuasi → Puerto Patache

## Been 1 · slurryleiding — Collahuasi (pompstation) → Puerto Patache

**been-id:** `koper-collahuasi-tongling-b1`
**Modaliteit:** slurryleiding — **eigen verbinding**, geen gedeeld net (`modi: []` in `aansluitingen.json`)
**Lengte:** gemeten 192,4 km (OSM-tracé) / gepubliceerd ±200 km (−3,8%) [P1]; in de ?v=099-keten 193 km [Z2]
**Net / bron geometrie:** 14 OSM-ways `substance=slurry`, 1.363 punten [P1]
**Stippel:** grotendeels nee (tracé gekarteerd); **laatste ~736 m gestippeld** — de kartering stopt daar [P1]
**Corridor bij naam:** het leidingtracé zelf; 7 van de 14 ways dragen de eigen onderhoudsweg (`highway=track` + `surface=dirt`)
**Routeerpunt kop / staart:** n.v.t. — eigen verbinding; de leiding ís de geometrie (anker = kop van de leiding)
**Toets-marge:** default (2 km passages · 100 m kop/staart)

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **Kop van de slurryleiding (pompstation Collahuasi)** — 1,9 km van Rajo Ujina, 2,3 km van het mijncomplex — anker `cu-collahuasi-laad` | laadplek | -20.97783, -68.64395 | [P1] | bevestigd (satelliet-check doorstaan 2026-07-28, z16) |
| 2 | — | Rajo Ujina / Rajo Rosario — de putten zelf; erts gaat naar de molen, niet de pijp in | referentie (niet aan lijn) | — | [P1] | bevestigd |
| 3 | 0–192 | Het tracé daalt van ~4.400 m naar zeeniveau; 7 van de 14 ways dragen `highway=track` + `surface=dirt` = de onderhoudsweg bovenop de pijp | passage | — | [P1] | bevestigd |
| 4 | ~191,7 | **Einde van de OSM-kartering** — 736 m vóór het terminalvlak | referentie | — | [P1] | bevestigd |
| 5 | ~192,4 | **Espesadores (indikkers) Patache** — hier mondt de leiding uit | overslag (aankomst b1) | *nog te leggen (z18)* | [P2] | **onzeker** |
| 6 | — | planta de molibdeno → planta de filtro → stockpile | passage (terreinproces) | — | [P2] | aannemelijk |
| 7 | — | **Terminalgebouwen + wal-einde van de laadsteiger** | overslag (terrein) | -20.80503, -70.19773 | [P1] + satelliet z16 | **satelliet-gelegd** |
| 8 | — | **Kop van de laadsteiger — ligplaats bulkcarrier** ⟵ sinds 2026-07-28 HET ANKER `cu-patache-kade` (286 m verplaatst vanaf punt 7, de walkant; goedkeuring Lars, doorgevoerd) | laadplek zee (vertrek b2) | -20.80270, -70.19890 | satelliet z16 | **satelliet-gelegd** |
| 9 | — | Tweede, noordelijker pier bij Patache (aparte terminal, o.a. de kolencentrale) hoort NIET bij deze stroom | referentie (niet aan lijn) | ~-20.7985, -70.1955 | satelliet z16 | aannemelijk |

**Opmerkingen been 1.** ⚠️ **Openstaand punt (§5.1–5.2).** Het punt `cu-patache-kade` deed
oorspronkelijk twee dingen tegelijk — eind van de leiding én begin van het zeebeen — terwijl dat
twee plekken zijn met vier verwerkingsstappen ertussen. De satelliet-check bevestigt dat het oude
anker op de **wal** lag: de ligplaats waar het schip afmeert ligt ~280 m NW, aan de kop van de
steiger (nu het anker). De **espesadores** staan niet in OSM (binnen 1,8 km kent de kaart vijf
objecten, geen tank) en zijn op z16 niet met zekerheid aan te wijzen → een z18-pass met Lars' oog
erbij, of één coördinaat van hem. Tot dan blijft punt 5 **onzeker** en tekent de kaart de leiding
tot het terminalvlak.

**Negatieve ankers been 1:** geen — de uitsluitingen van deze fase zitten in ladders 1–2 (§2a) en punt 9 (referentie).

## Overslag been 1 → been 2 — Puerto Patache

**Productvraag:** ladder 2 in §2a — slurry eindigt bij de indikkers; na moly-plant, filterplant en
stockpile gaat droge bulk via de steigerband het schip in; de laadplek is de kop van de steiger.

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 1 | espesadores (einde leiding) | losplek | *nog te leggen (z18)* | [P2] | **onzeker** |
| 2 | terrein | planta de molibdeno → planta de filtro → stockpile | verwerkingsstap | — | [P2] | aannemelijk |
| 3 | terrein | terminalgebouwen + wal-einde laadsteiger | passage | -20.80503, -70.19773 | [P1] + satelliet z16 | **satelliet-gelegd** |
| 4 | vertrek been 2 | kop laadsteiger — ligplaats bulkcarrier (`cu-patache-kade`) | laadplek | -20.80270, -70.19890 | satelliet z16 | **satelliet-gelegd** |

**Routeerpunt ≠ anker.** Zee-routeerpunt -20.2313, -70.6311 — gemeten snap **77,86 km**
[`aansluitingen.json`]: de haven-aanloop van Chili heeft geen AIS-net (nul havens met varend
verkeer) en blijft per de stippellijn-conventie (werkwijze §7) de **eindvorm** gestippeld.

---

# FASE B · zee — Puerto Patache → Yangtze-benedenrivier

## Been 2 · zee — Patache → Yangtze-monding → losligplaats benedenrivier

**been-id:** `koper-collahuasi-tongling-b2`
**Modaliteit:** zeeschip (bulkcarrier)  ·  **Router:** zee = vrij geroutet (werkwijze §6); kade→kade + sanity-ankers
**Lengte:** ?v=099-meting zeebeen 18.590 km [Z2]; M26.1-meetlat hele keten 19.406 km met 2 overslagen [Z1]
**Overslagen onderweg:** geen transshipment-hub — bulkcarrier, geen lijndienst; de drager-wissel zit aan het eind (blok hieronder)
**Routeerpunt kop / staart:** kop -20.2313, -70.6311 — max snap ~78 km (gestippelde haven-aanloop, zie overslagblok) · staart **nog te bepalen** (los-ligplaats niet gepind; tot dan tekent de kaart de modus-wissel op 吴淞口)

| # | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|
| 1 | **Patache — kop laadsteiger** (vertrek; `cu-patache-kade`) | laadplek | -20.80270, -70.19890 | satelliet z16 | **satelliet-gelegd** |
| 2 | Open Stille Oceaan, noordelijke lane richting Oost-Azië | passage | — | [Z1] | aannemelijk |
| 3 | **Yangtze-monding / 吴淞口** — rivier-km 0, overgang zee → binnenwater; het zeeschip vaart de rivier op | vaarweg-overgang | 31.39, 121.51 | [Y1] | bevestigd |
| 4 | **Losligplaats zeeschip — Nantong** (rivier-km ~92–110): gedocumenteerde losplek van het geïmporteerde concentraat; exacte ligplaats onbekend | overslag (aankomst b2) | *geen coördinaat — open (§5.3)* | [D4][D10] | aannemelijk |

**Negatieve ankers been 2** — mét coördinaat + verbodsstraal, anders is het verbod niet toetsbaar:

| punt | lat, lon | straal | reden |
|---|---|---|---|
| Panamakanaal | 9.10, -79.70 | 200 km | de echte stroom vaart de Grote Oceaan over, niet via Panama |
| Kaap Hoorn | -55.98, -67.27 | 300 km | idem — geen ronding van Zuid-Amerika |
| haven Antofagasta | -23.65, -70.40 | 50 km | ~317 km zuidelijker gelegen publieke haven (nagemeten 317,3 km hemelsbreed vanaf `cu-patache-kade`); Patache is de eigen terminal — `data/copper.js` stuurde de stroom hier ten onrechte heen |
| Yangshan | 30.63, 122.06 | 20 km | containerhaven op eilanden vóór de kust, tientallen km van de riviermond — concentraat voor de Yangtze-smelters komt daar niet binnen [T2] |

*Correctie 2026-07-29: de Antofagasta-regel zei "120 km" en kernfeit 3 (overgenomen uit de oude
brief) zelfs "120 km noordelijker" — nagemeten ligt Antofagasta **317,3 km ten zuiden** van
`cu-patache-kade` (-20.80270, -70.19890 → -23.65, -70.40). Het ankercoördinaat en de
verbodsstraal (50 km) waren al goed, dus de machinetoets zat nooit fout; alleen het proza is
rechtgezet.*

**Meetlat:** de atlas mat de hele keten Collahuasi→Tongling op **19.406 km** met 2 overslagen
[Z1]; na de ankercorrecties van 2026-07-28 staat hij live op **19.299 km** (leiding 193 · zee
18.590 · Yangtze 517) [Z2].

## Overslag been 2 → been 3 — benedenrivier (Nantong; alternatieven Zhangjiagang/Jiangyin)

**Productvraag:** ladder 3 in §2a — bulkconcentraat vraagt een bulk-losligplaats met
douane-/entrepotfunctie; Nantong is de gedocumenteerde losplek [D4], maar de ligplaats is niet
gepind en de historische ankerplaats-overslag bestaat er sinds eind 2017 niet meer [D10].

| # | rol | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | aankomst been 2 | losligplaats zeeschip, Nantong (rivier-km ~92–110) | losplek | *geen coördinaat — open (§5.3)* | [D4][D10] | aannemelijk |
| 2 | terrein | kadeopslag/entrepot + belading binnenvaart | verwerkingsstap | — | [D4] | aannemelijk |
| 3 | vertrek been 3 | laadligplaats binnenvaart | laadplek | *geen coördinaat — open (§5.4)* | — | **onzeker** |

**Alternatieven (reëel, geen referentie):** een deel van het Andes-concentraat lost werkelijk
stroomopwaarts bij **Zhangjiagang** (rivier-km ~130) of **Jiangyin** (~154–178) [Y1][Y2] — dan
schuift de b2/b3-grens 20–70 km mee. Aandeel onbekend (§5.5). **Luojing/Baogang-bulkpier**
(31.42704, 121.47618, `cu-shanghai-kade`) blijft het benedenstrooms aanlandingsalternatief [T2].

**Been-grens, eerlijk:** de kaart tekent de modus-wissel nu op 吴淞口 (rivier-km 0) — het
administratieve zee/binnenwater-punt. De fysieke overslag ligt ~100 km stroomopwaarts (Nantong) of
verder (alternatieven). Zodra de losligplaats gepind is, verhuist de been-grens naar dat anker;
het stuk monding→ligplaats is dan de staart van been 2 (het zeeschip vaart het zelf).

---

# FASE C · aanlanding → smelter

## Been 3 · binnenvaart — Yangtze-monding → Tongling, oostgeul, kade TNMG (~550 rivier-km)

**been-id:** `koper-collahuasi-tongling-b3`
**Modaliteit:** binnenvaart  ·  **Brief-gestuurd** (werkwijze §6: geen vrije Dijkstra)
**Lengte:** gemeten 516,6 km als tekengeometrie over 72 MARNET-bulkedges (Shanghai→Tongling, `maak_rivierbeen.py`) [Z2] / stedenlijst-kilometrering: Tongling-stad op vaarweg-km ~547–552 [Y1]  ·  **km-kolom =** officiële vaarweg-kilometrering vanaf de monding; waar bronnen een bereik geven staat het bereik
**Stippel:** nee — geometrie uit de MARNET-bulklaag + handgelegde oostgeul [T1]
**Toets-doel:** dit been als **stedenlijst op rivier-kilometrering**, zodat een verkeerde arm of een overgeslagen stad meetbaar wordt
**Routeerpunt kop / staart:** kop **nog te bepalen** (hangt aan de losligplaats, §5.3–5.4) · staart 30.9901, 117.7713 — max snap 0,4 km [`aansluitingen.json`]
**Toets-marge:** default, behalve de stedenpassages (stadscentroïden op 2 decimalen): **6 km** per punt — een stad ligt zelden óp de geul (Beilun→Guixi-les: corridorpunten geraakt op 0,8–6,4 km)

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **吴淞口 / Yangtze-monding** | vaarweg-overgang | 31.39, 121.51 | [Y1] | bevestigd |
| 2 | ~30 | Baoshan / Luojing — de Baogang-bulkpier aan de Yangtze (aanlandingsalternatief; `cu-shanghai-kade`) | referentie (niet aan lijn) | 31.42704, 121.47618 | [T2] | bevestigd |
| 3 | ~92–110 | **南通 (Nantong)** — vanaf hier stroomafwaarts is de geul geschikt voor 50.000-tonners; tevens de gedocumenteerde losplek van het zeebeen (overslagblok hierboven) | passage | 32.02, 120.86 | [Y1][D4] | bevestigd |
| 4 | ~130 | **张家港 (Zhangjiagang)** — grote concentraat-loshaven; véél Andes-concentraat lost hier (stond als referentie; per werkwijze-aanscherping nu alternatief) | **alternatief (aandeel onbekend, §5.5)** | 31.97, 120.55 | [Y2] | aannemelijk |
| 5 | ~154–178 | **江阴 (Jiangyin)** — idem: bekende loshaven voor concentraat | **alternatief (aandeel onbekend, §5.5)** | 31.92, 120.28 | [Y1][Y2] | bevestigd |
| 6 | ~200–240 | **镇江 (Zhenjiang)** | passage | 32.19, 119.43 | [Y1] | bevestigd |
| 7 | ~330–370 | **南京 (Nanjing)** — bovengrens voor zeeschepen; de Nanjing Yangtze-brug (1968, ~24 m) is het fysieke mechanisme | sluis/kering (hoogtebeperking) | 32.06, 118.74 | [Y1][Y3] | bevestigd |
| 8 | ~390–399 | **马鞍山 (Ma'anshan)** | passage | 31.70, 118.48 | [Y1] | bevestigd |
| 9 | ~440–449 | **芜湖 (Wuhu)** — passage; tevens vestigingsplaats van vertakking 芜湖铜冠电工 (§4) | passage | 31.33, 118.37 | [Y1] | bevestigd |
| 10 | ~547–552 | **铜陵 (Tongling)** — vaarwegkilometrering van de stad | passage | 30.94, 117.81 | [Y1] | bevestigd |
| 11 | — | **Noordpunt van het eiland — invaart oostgeul** (zuid-junctie 30.9102, 117.7373 en noord-junctie 31.1091, 117.7696 zijn de gedeelde knopen) | vaarweg-overgang | 31.1091, 117.7696 | [T1] | bevestigd |
| 12 | — | **Kade TNMG-kopersmelter Tongling** (`cu-tongling-kade`) — losplek concentraat, einde fase C | losplek | 30.98656, 117.77180 | [T1] + satelliet (2026-07-24, go Lars; z16-hercheck 2026-07-28) | **satelliet-gelegd** |
| 13 | — | Oude, gesloten smelter (30.918, 117.756) en het eerdere foute terrein (30.939, 117.773) | referentie (niet aan lijn) | — | [T1] | bevestigd |

*Notatie-correctie 2026-07-29: punten 11–13 stonden in de eerste versie van deze brief als
lon,lat ("117.7696, 31.1091" enz.) — gecorrigeerd naar lat, lon en op plausibiliteit gecheckt
tegen de werkelijke plaats (Tongling ligt op lat ~31).*

**Negatieve ankers been 3:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| west-arm om het Tongling-eiland (benaderd midden van het weggeknipte stuk, vertex 2..7 van way 226556520 — centroïde, géén anker) | ~31.010, 117.730 | 0,5 km | de doorgaande vaart neemt de oostgeul; de west-arm is in de bake weggeknipt met `knipWayId` [T1]. Straal bewust klein: het eiland is smal — verfijnen op de stitch (§5.6) |

**Volgorde- en type-toetsen (uit de oude brief, onverkort):** **géén sluizen** op de benedenloop —
de Yangtze is vrij stromend tot ver boven Tongling · **niet boven Nanjing met een zeeschip**
(bruggenhoogte ~24 m [Y3]) — vanaf de losligplaats tot de smelter is dit één binnenvaartbeen na de
overslag · de lijn hoort **Wuhu vóór Tongling** te raken; omgekeerde volgorde = fout gekozen arm.

**Last mile fase C — er is er geen.** De kade van de smelter ligt aan de rivier en het schip lost
direct op het terrein. Dat is de uitzondering die de regel bevestigt — bij grafiet (1 km truck) en
bij Guixi (aansluitspoor) is de last mile er wél, hier valt hij weg. Aan de mijnkant is de "last
mile" de leiding zelf, been 1.

## Verwerkingsknoop · TNMG-smeltercomplex Tongling (金冠铜业 + 金新铜业)

| | |
|---|---|
| **anker-id** | `cu-tongling-kade` (kade); smelterterrein op 30.98656, 117.78060 [T1] |
| **eigenaar van dit anker** | deze brief |
| **wat hier staat** | het TNMG-smeltercomplex in de 铜陵经开区, pal aan de Yangtze: **金冠铜业** (Jinguan; "dubbel-flash" 2013 + Ausmelt; 760 kt/a kathode — China's grootste enkelvoudige matsmelter [D3]) + **金新铜业** (Jinxin; "铜基新材料"-project, 500 kt/a, flash-oven ontstoken 2025-03-26, volledig in bedrijf juni 2025; smelten + elektrolyse + zwavelzuur + koperverwerking + slakflotatie op één terrein [D1][D2]). De door Lars aangewezen "nieuwe smelter" = dit complex; welk terreindeel 金冠 en welk 金新 is, staat open (§5.7) |
| **in** | Cu-concentraat per binnenvaart — deze streng: Collahuasi-concentraat (volume niet in projectdata); 4 t concentraat → 1 t ruwkoper [D4] |
| **andere ingaande strengen** | overig geïmporteerd + binnenlands concentraat (niet in de atlas gemodelleerd — de smelter draait vele malen meer dan deze ene mijn levert) |
| **uit** | **kathode** (Cu+Ag ≥ 99,95%, warrant 25 t [D7]) + goud/zilver [D1] |
| **uitgaande strengen** | deze brief: fase D naar 铜冠铜箔-basis Tongling (~68% interne kathode-inkoop van de foliedochter [D6]) · vertakkingen §4: Chizhou/Hefei-foliebases, 芜湖铜冠电工, SHFE-entrepots Jiangsu/Shanghai, 铜板带-tak — aandelen onbekend |
| **verlies / bijproduct** | zwavelzuur (制酸-installatie [D1]) · goud/zilver [D1] · slak → slakflotatie op het terrein [D1]; bestemmingen bijproducten niet onderzocht |

---

# FASE D · kathode → foliefabriek

## Been 4 · last mile uitgaand — kathode-expeditie → poort → openbaar net

**been-id:** `koper-collahuasi-tongling-b4`
**Modaliteit:** **weg (truck)** — beslist op een negatieve meting: er kruist **geen spoor** 翠湖六路 het 金冠-blok in, dus het terrein heeft in OSM geen spooraansluiting (§5.9)
**Stippel:** **nee — doorgetrokken.** Gemeten aanloop 38 m aan de kop en een aaneengesloten intern servicenet ertussen; werkwijze §7 reserveert stippel uitsluitend voor *hier reikt het net niet*
**Routeerpunt kop / staart:** 30.99602, 117.78548 / 30.99058, 117.78147
**Toets-marge:** kop 100 m (anker ≠ routeerpunt)
**GEBAKKEN 2026-08-06:** 1,1 km · 11 punten · snaps 0,04 → 0,01 → 0,00 km · lengtetoets −3,8%

⚠️ **DE KOP IS 金冠铜业, NIET 金新铜业 — een wijziging aan ladder 5, geen stille swap.** Redenen: (a) 金冠 is het bestaande 760 kt/a-blok dat de foliefabriek al levert sinds fase 1 in dec 2017 draaide, zeven jaar vóór 金新 werd ontstoken (2025-03-26); (b) 金冠 is verifieerbaar op het enige beschikbare beeld en 金新 principieel niet — de hele Tongling-scene is één opname van **2019-04-05** (Esri identify-service `SRC_DATE2`), en op het 金新-registerpunt 31.00410/117.78538 staat daar nog rauw, deels drassig struweel: de opnamedatum-faalmodus (Shed 8-8 / De Soto-klasse) en het zoomplafond treffen hier dezelfde stroom tegelijk; (c) [D6] documenteert de interne levering op **concern**niveau, niet op blokniveau, dus 金冠 spreekt de bron niet tegen. 金新 blijft in de brief als tweede kathodebron met zijn registerpunt als **knoop-marker, geen anker**.

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | **kathode-laadplek → SUBSTITUUT-KOP: registerpunt 金冠铜业分公司** (vergunning `91340764551849860L001P`, 铜冶炼). Op de stitch: bedieningsblok in een draaiende zware installatie, pijpenrek ZW, zwavelzuurkolommen west, tankpark van zes cilinders ZO, elektrolysehallen NW | laadplek (substituut) | **30.99602, 117.78548** | MEE-emissieregister + eigen z18-stitch | **satelliet-gelegd (z18)** |
| 2 | 0,9 | **terreinpoort zuid** (翠湖六路-zijde) — poortwachterspaar, parkeerstrook met ~15 auto's, verharde apron | poort | **30.99156, 117.78146** | eigen z18-stitch + 四至 verificatiebesluit | **satelliet-gelegd (z18)** |
| 3 | 1,0 | aansluiting op het openbare net (翠湖六路) — OSM-knoop graad 3 | kruising | **30.99058, 117.78147** | OSM (ODbL) | **bevestigd** |

**Negatief anker been 4 (aanvullend):** de **noordpoort** 30.99961, 117.78145 is óók satelliet-gelegd maar niet gekozen; komt er een bron die hém aanwijst, dan verandert alleen dit been (+~1,3 km op been 5).

**Negatieve ankers been 4:**

| punt | lat, lon | straal | reden |
|---|---|---|---|
| oude, gesloten smelter | 30.918, 117.756 | 1 km | de kathodestroom vertrekt van het nieuwe complex, niet van het oude terrein [T1] |

## Been 5 · weg — smeltercomplex → 铜冠铜箔, basis Tongling (koperfolie)

**been-id:** `koper-collahuasi-tongling-b5`
**Modaliteit:** weg (stukgoed per truck — aannemelijk; zie been 4 voor het voorbehoud)
**Lengte:** **6,9 km gebakken** (2026-08-06), tegen 4,2 km hemelsbreed = ratio 1,50 — normaal voor een orthogonaal 经开区-raster op een diagonaal
**Let op bij container/stukgoed:** dit is een kort binnenzone-been, geen lijndienst — de direct-vs-hub-vraag speelt hier niet; voor de véérdere vertakkingen (SHFE-entrepots, Chizhou/Hefei, Wuhu) is de modaliteit per tak onbekend = openstaand punt (§5.11), geen rechte lijn
**Routeerpunt kop / staart:** 30.99058, 117.78147 / 30.96137, 117.81051
**Toets-marge:** staart 100 m (anker ≠ routeerpunt; gemeten 41,9 m)
**GEBAKKEN 2026-08-06:** 6,9 km · 51 punten · snaps 0,00 → 0,05 km · lengtetoets +7,6%

⚠️ **DE STAART IS GETRIMD OP DE ANKERPROJECTIE.** De dichtstbijzijnde OSM-**knoop** ligt 51 m vóórbij de projectie van het folie-anker op 翠湖二路; ongetrimd reed de lijn de poort voorbij en keerde terug — de overschiet-en-terug-klasse, hier op het been-EINDE (zelfde klasse als de 792 m bij Guixi). `snoei_keerlussen` kan die per constructie niet vangen omdat de anker-stub ná de snoei wordt aangeplakt. Nieuwe opt-in `"trimStaart"` in `maak_stroombeen_weg.py` knipt op de projectie, en de **lengtetoets draait ná de trim** — 7,00 → 6,87 km, +9,7% → +7,6%.

| # | km | punt | type | lat, lon | bron | status |
|---|---|---|---|---|---|---|
| 1 | 0 | vertrek: aansluiting openbaar net (= einde been 4) | laadplek | **30.99058, 117.78147** | OSM (ODbL) | **bevestigd** |
| 2 | — | 翠湖六路 1.438 m → 长山大道 1.974 m → 五松山大道/S335 619 m → tertiary 479567771 1.276 m → 479567772 806 m → 翠湖二路 248 m | passage | — | OSM (ODbL), eigen Dijkstra | **bevestigd** |
| 3 | 6,9 | **铜陵铜冠电子铜箔有限公司** — 翠湖二路西段789号. Op de stitch: verhard voorterrein binnen een ommuurd perceel, L-vormige blauwe overkapping, ronde siertuin (klassiek 厂前区), en op ~180 m de witte proceshal met dakgemonteerde 酸雾净化塔 uit de vergunning | losplek (vestigingspunt) | **30.96174, 117.81059** | MEE-emissieregister `91340700MA2NH25G2R001V` + EIA + 水土保持 + eigen z18-stitch | **satelliet-gelegd (z18)** |

**Bewijs voor dit been (waarom deze fabriek de streng is):** 铜冠铜箔 koopt **~68%** van zijn
kathode intern bij TNMG en begroot voor 2026 bij de moedergroep 496 mln yuan **kathode** plus
3.195 mln yuan **铜丝 (koperdraad)** [D6] — de folie-voeding loopt dus deels via een
draad-/waltrekstap (locatie onbekend, §5.12). De Tongling-basis is één van drie foliebases
(Tongling · Chizhou · Hefei) met samen 55 kt/a elektronicafolie (35 kt PCB + 20 kt lithium),
uitbreidend naar 80 kt/a [D5]. Stad-context: Tongling heeft ~600 kt/a walsdraadcapaciteit
(铜杆) en 400 kt/a wikkeldraad (电磁线) [D9] — "walsdraad in de regio" is dus ruimschoots
aanwezig, maar plant-niveau-toewijzing aan déze kathode is alleen voor de foliedochter
gedocumenteerd.

## Verwerkingsknoop · 铜冠铜箔, basis Tongling (foliefabriek)

| | |
|---|---|
| **anker-id** | nog geen — aan te maken in `aansluitingen.json` ná plaatsbepaling + z16 (§5.10) |
| **eigenaar van dit anker** | deze brief |
| **in** | kathode + 铜丝 van TNMG (~68% van de kathode-inkoop intern; 2026: 496 mln yuan kathode + 3.195 mln yuan draad) [D6] |
| **andere ingaande strengen** | kathode/draad van derden (~32% [D6]) — niet gemodelleerd |
| **uit** | elektronicakoperfolie: PCB-folie (35 kt/a) + lithiumbatterijfolie (20 kt/a), groei naar 80 kt/a totaal [D5] |
| **uitgaande strengen** | fase E (marktrichting, geen been): PCB-laminaat — top-5-klanten 2021H1: 生益科技 26,5% · 台燿科技 18,6% · 华正新材 11,3% · 金安国纪 8,5% · 台光电子 8,3%; lithiumfolie: BYD = 43–58% van de li-folie-omzet 2019–2021H1 [D11] |
| **verlies / bijproduct** | zuur-/elektrolytkringloop foliefabriek — niet onderzocht |

---

# FASE E · foliefabriek → eindproduct / markt

**Er wordt bewust géén been 6 getekend.** De folie gaat naar gedocumenteerde **bedrijven** maar
niet naar één gedocumenteerde **plek**: de PCB-folie naar copper-clad-laminate-fabrikanten (grootste
klant 生益科技/Shengyi, de wereldleider in CCL, met meerdere fabrieken; verder 台燿, 华正, 金安国纪,
台光) en de lithiumfolie overwegend naar **BYD** (43–58% van de li-folie-omzet 2019–2021H1) [D11] —
beide afnemers hebben tientallen productielocaties en geen bron wijst de fabriek(en) aan waar déze
folie heengaat, laat staan de modaliteit of corridor.

**Waar de keten eindigt, en waarom daar.** De keten eindigt bij de foliefabriek in Tongling. Wat ik
zocht en niet vond (fase E-regel uit het sjabloon — het niet-vinden is zelf de bevinding): (a) een
plant-niveau-toewijzing van 铜冠铜箔-folie aan een specifieke 生益- of BYD-vestiging — niet
gedocumenteerd in jaarverslagen/prospectus-uittreksels die de klantaandelen wél geven [D11]; (b) de
afvoermodaliteit van het smelterterrein (weg/water/spoor) — geen bron gevonden (§5.9); (c) een
SHFE-entrepot in Anhui als alternatieve eindbestemming van de kathode — bestaat niet; de
entrepotlijst clustert in Shanghai/Jiangsu/Zhejiang/Guangdong [D7], dus die tak is een vertakking
stroomafwaarts en geen keten-eind hier. Een markt-centroïde ("de Chinese PCB-industrie") zou géén
anker zijn en wordt niet getekend.

---

## 4 · Samenvloeiingen en vertakkingen (overzicht)

| # | been | soort | met welke brief | wat gedeeld/afgesplitst wordt | eigenaar anker |
|---|---|---|---|---|---|
| 1 | b2/b3 | alternatief (geen aparte streng zolang het aandeel onbekend is) | — | losplek-alternatief Zhangjiagang / Jiangyin voor het zeebeen [Y2] | deze brief |
| 2 | na de smelter-knoop | vertakking | *nog geen brief* | kathode/铜丝 → 铜冠铜箔-bases **Chizhou** (池州经开区, overzijde/stroomafwaarts) en **Hefei** [D5] — aandeel onbekend | deze brief (knoop) |
| 3 | na de smelter-knoop | vertakking | *nog geen brief* | draadproducten → **芜湖铜冠电工** (Wuhu-经开区; gelakte draad 10 kt/a, NEV-flatwire [D8]) — ligt aan de b3-corridor bij rivier-km ~440 | deze brief (knoop) |
| 4 | na de smelter-knoop | vertakking | *nog geen brief* | kathode → **SHFE-entrepots** (dichtstbijzijnde cluster: 中储无锡, 上港物流苏州, 常州融达 e.a., Jiangsu; verder Shanghai/Zhejiang/Guangdong) [D7] — aandeel en modaliteit onbekend | deze brief (knoop) |
| 5 | na de smelter-knoop | vertakking | *nog geen brief* | 铜板带-tak van de TNMG-verwerking (>400 kt/a totaal, "皖江als kern") [D3] — bedrijfsnaam/locatie niet geverifieerd | deze brief (knoop) |

**Regel:** één brief = één streng. Zodra een vertakking een gedocumenteerd aandeel + plek krijgt,
wordt het een eigen `stroom-id` met eigen brief; tot dan staan ze hier als benoemde, niet-getekende
takken.

## 5 · Openstaande punten

| # | been | wat | waarom onzeker | wat het zou oplossen |
|---|---|---|---|---|
| 1 | b1 | espesadores-coördinaat (leiding-eind, aankomstanker overslag Patache) | niet in OSM; op z16 niet met zekerheid aan te wijzen | z18-pass, of één coördinaat van Lars |
| 2 | b1→b2 | `cu-patache-kade` splitsen in leiding-eind · terminal · ligplaats (drie punten) | tot punt 1 opgelost is tekent de kaart de leiding tot het terminalvlak | idem als 1; daarna registry-splitsing |
| 3 | b2 | losligplaats zeeschip benedenrivier — Nantong aannemelijk [D4] maar terminal/ligplaats onbekend; de historische ankerplaats-overslag is eind 2017 beëindigd [D10] | één bron op havenniveau, geen kade | havenbron Nantong (welke terminal doet concentraat) + z16-pass |
| 4 | b3 | laadligplaats binnenvaart (vertrekanker van dezelfde overslag) | geen bron; bewust géén coördinaat verzonnen | idem als 3 — twee ankers, geen compromis-punt |
| 5 | b3 | aandeel Zhangjiagang/Jiangyin (alternatief) kwantificeren | [Y2] zegt "veel", geen getal | haven-/douanestatistiek concentraat per loshaven |
| 6 | b3 | west-arm-negatief-anker: centroïde + straal verfijnen | eiland is smal; centroïde benaderd uit de junctie-coördinaten | aanwijzen op de bestaande oostgeul-stitch |
| 7 | knoop C | terreingrens 金冠铜业 / 金新铜业 op het aangewezen smelterterrein | beide delen van het complex zijn actief; Lars wees "de nieuwe smelter" aan vóór de naamsidentificatie | z16-pass met de twee plantnamen erbij |
| 8 | b4 | ~~kathode-laadplek + poort~~ → **POORT GESLOTEN 2026-08-06.** Twee poorten satelliet-gelegd op **z18**: zuid **30.99156, 117.78146** en noord **30.99961, 117.78145**, beide een poortwachterspaar in een onderbroken haag-/muurlijn. Identiteit via het 四至 uit het gemeentelijke verificatiebesluit over het 奥炉改造工程 van 金冠铜业分公司: *"西湖二路以南，翠湖六路以北"*. De **zuidpoort** is gekozen door te meten, niet te kiezen: een Dijkstra naar de foliefabriek neemt hem vanzelf (7,41 tegen 8,70 km) | — | — |
| 8b | b4 | **NIEUW — de kathode-expeditie zelf is NIET gevonden**, met twee gemeten oorzaken die elkaar niet vervangen: (a) het emissievergunningregister geeft één punt per vergunning — de **vestiging, geen deur** (het 副本 rendert leeg, dezelfde blokkade als Guixi); (b) **Esri heeft hier geen z19** — z19 én z20 leveren op alle drie de punten exact 2.521 byte placeholder terwijl z17/z18 16–18 kB echte tegels geven, dus **z18 = 0,51 m/px** is de fijnste korrel en een laadperron van 10–15 m ligt op de resolutiegrens. Vijfde bevestigde zoomplafond na Guixi, Zhangjiagang, Tianqi en Chizhou. Vier zoeklijnen liepen alle randen van het 金冠-blok af op 0,13–0,26 m/px: geen perron, geen dock, geen weegbrug | registergrens + zoomplafond | een **niet-Esri-bron** (Amap/Baidu met sleutel, of een 总平面布置图 uit een EIA-bijlage) — géén andere Wayback-release |
| 9 | b4 | uitgaande modaliteit kathode (weg / eigen kade / spoor-siding) — en: hoort de op 2026-07-24 geheelde spoor-siding bij dít terrein? | geen bron; de siding-heal dateert van vóór de naamsidentificatie van het complex | bron over TNMG-expeditie, of de siding op de stitch volgen |
| 10 | b5 | ~~exacte kavel 铜冠铜箔-basis Tongling~~ → **GESLOTEN 2026-08-06.** **铜陵铜冠电子铜箔有限公司**, USCC `91340700MA2NH25G2R`, **翠湖二路西段789号**, anker **30.96174, 117.81059**, satelliet-gelegd z18. Drie onafhankelijke overheidscoördinaten binnen 256 m op hetzelfde ommuurde perceel: MEE-register 30.96174/117.81059 · EIA 厂区中心 30.96330/117.81123 · 水土保持 30.96288/117.81292. ⚠️ **Rolverdeling vastleggen** (de Greenbushes-les): het EIA-厂区中心 is de waarde voor de *verwerkingsknoop op registerschaal*, het MEE-punt is de *aansluiting* voor de staart van been 5. ⚠️ **Niet verwarren met de moeder** 安徽铜冠铜箔集团 (301217), die in hetzelfde register in **Chizhou** staat op 30.70621/117.55141 — 37,7 km ZW | — | — |
| 10b | b5 | **NIEUW — het losdock van de foliefabriek is niet gevonden** (zelfde twee oorzaken als §5.8b). Het folie-EIA documenteert **twee poorten** (翠湖二路 zuid, 泰山大道 oost) — dat is de goedkoopste gerichte vervolgstap | registergrens + zoomplafond | niet-Esri-bron, of de 总平面布置图 uit de EIA-bijlage |
| 10c | b5 | ⚠️ **OSM-polygoon `way/1247093617` draagt de naam-tag 铜冠铜箔有限公司 maar omsluit 铜冠黄铜棒材** (翠湖二路2135号, registerpunt 30.96290/117.80663), 400 m westelijker. Armchair-edit, v1, geen source-tag. **Dit is de gevaarlijke variant van de OSM-regel: niet een lege uitslag maar een positieve en foute** — gebruik hem niet | — | staat als waarschuwing in de node-noot |
| 11 | vertakkingen | aandeel + modaliteit per tak (Chizhou/Hefei/Wuhu/SHFE/板带); container-of-bulk per tak onbekend = geen rechte lijn | RPT-cijfers geven bedragen, geen tonnage per bestemming | jaarverslag-segmentatie of vrachtstatistiek |
| 12 | fase D/E | locatie van de 铜丝/铜杆-tussenstap (kathode → draad → folie) | [D6] documenteert de inkoop, niet de fabriek | TNMG-bron over de draadfabriek; stad heeft ~600 kt/a walsdraad [D9] |
| 13 | fase D | SHFE-merkregistratie van de TNMG-kathode niet geverifieerd (bijlage achter CAPTCHA) | levering aan de entrepots [D7] veronderstelt een geregistreerd merk | SHFE-bijlage 注册商标 raadplegen |

## 6 · Conflicten met de projectdata (afwerklijst)

| # | wat | nu | hoort te zijn | bron |
|---|---|---|---|---|
| 1 | `cu-patache-kade` doet leiding-eind én zeebeen-begin | één punt (sinds 2026-07-28 op de ligplaats) | **splitsen**: espesadores (leiding-eind, nog te leggen) · terminal · **-20.80270, -70.19890** (ligplaats, zeebeen) | [P2] + satelliet |
| 2 | flow `cu-collahuasi → cu-ref-tongling`, `via: [cu-port-antofagasta, cu-port-shanghai]` in `data/copper.js` | de bol vaart sinds ?v=099 al via Patache en de Yangtze [Z2], maar de flow-definitie in `data/copper.js` noemt nog Antofagasta + Shanghai/Yangshan | via **Patache** en de **Yangtze-benedenrivier**; Yangshan is een containerhaven en hoort er niet in | [T2] |
| 3 | Yangtze-been zonder tussenpunten | ?v=099: tekengeometrie via `maak_rivierbeen.py` (516,6 km) [Z2]; via-punt-toets tegen de stedenlijst nog niet gedraaid | **via-punt→via-punt** langs de stedenlijst van been 3, mét de 6 km-marge per stadspunt | werkwijze §5 |
| 4 | Zhangjiagang / Jiangyin | niet in de data | opnemen als **alternatief** (punt-type met aandeel zodra bekend, §5.5) — niet meer als "referentie" | [Y2] |
| 5 | keten-eind in de data | `data/copper.js` eindigt bij kathode (`cu-ref-tongling`) | fase D/E toevoegen zodra §5.8/5.10 ankers opleveren: knoop foliefabriek + been smelter→folie; SHFE-tak apart | deze brief |
| 6 | `aansluitingen.json` | geen entry voor de foliefabriek of de kathode-expeditie | nieuwe aansluitingen ná z16-pass (§5.8, §5.10) — niet eerder aanmaken | werkwijze §2 |
| 7 | **NIEUW 2026-08-06** — de bron-noot van `cu-tongling-kade` zegt *"smelter erachter op 117,7806/30,98656"* | dat punt ligt **106 m** van het registerpunt van **铜冠冶化分公司** (行业类别 **炼铁** — ijzerbereiding) en **1.150 m** van 金冠铜业; het ligt bovendien **zuid** van 翠湖六路 terwijl 金冠铜业 volgens het gemeentelijke 四至 **noord** ervan ligt | de noot moet **冶化** noemen of de kopersmelter-coördinaat 30.99602/117.78548 gebruiken. ⚠️ **De kade zelf (117.7718/30.98656) staat en beweegt niet** — die is door Lars op de foto aangewezen en op 2026-07-28 satelliet-gecheckt | eigen meting |
| 8 | **NIEUW** — de naad kade → kop been 4 | **1.503 m**, en dat is een **procesgat binnen de verwerkingsknoop**: van de kade, dwars door het smeltercomplex (98,5 ha), naar de expeditie. Zelfde klasse als Guixi (584 m), groter omdat het complex groter is en de kade aan de rivier ligt | blijft bewust staan; er wordt geen lijn dwars door een fabriek getekend. `voeg_been_toe.py` weigerde hem op de default van 1,0 km — bewust verhoogd naar 2,0 met deze reden | werkwijze §7 |

## 7 · Wat de kaart moet tekenen

1. **Been 1 — leiding** (doorgetrokken; het tracé is gekarteerd, anders dan bij Escondida):
   pompstation -20.97783, -68.64395 → terminalvlak Patache. Laatste 736 m gestippeld (kartering
   houdt daar op).
2. **Been 2 — zee**: ligplaats Patache → Yangtze-monding; haven-aanloop Chili gestippeld
   (stippellijn = eindvorm, werkwijze §7).
3. **Been 3 — binnenvaart**: monding → Nantong → (Zhangjiagang/Jiangyin als alternatief-markers)
   → Zhenjiang → Nanjing → Ma'anshan → Wuhu → Tongling, dan de **oostgeul** naar de kade.
4. **Geen last mile fase C** — de kade ís het eindpunt van het natte deel.
5. **Referentie- en alternatiefmarkers** (niet aan de lijn): Luojing/Baogang-pier (referentie),
   Zhangjiagang/Jiangyin (alternatief), oude smelter (referentie).
6. **Fase D/E nog níet tekenen** — geen been 4/5-lijn zolang de ankers ontbreken (§5.8, §5.10);
   ook de SHFE-/Chizhou-/Wuhu-vertakkingen niet (aandeel onbekend = geen lijn). Als er iets
   getoond wordt, dan uitsluitend de knoop-markers met een "fase D open"-annotatie.
7. **Kleur / modaliteit per been:** leiding = leidingstijl · zee = zee · binnenvaart = binnenvaart;
   been 5 wordt t.z.t. weg (truck, amber).

## 8 · Toets-checklist (invullen bij de controle)

- [ ] **Notatie:** alle coördinaten lat, lon met decimale punt; ankers op 5 decimalen — *bij deze omzetting gecorrigeerd voor been 3, punten 11–13*
- [ ] Elk been heeft een **been-id**; ankers dragen waar mogelijk het `aansluitingen.json`-id (`cu-collahuasi-laad` · `cu-patache-kade` · `cu-shanghai-kade` · `cu-tongling-kade`)
- [ ] Elke laadplek, overslag en losplek heeft status **satelliet-gelegd** (z16) — *nu: 3 van de benodigde punten gelegd (Patache-steigerkop, terminal-walkant, Tongling-kade); espesadores, benedenrivier-overslag en alle fase D/E-punten open (§5)*
- [ ] Elke laad-/los-/overslagplek heeft een ingevulde **productvraag** (§2a), inclusief de uitsluitingen — *6 ladders ingevuld; 3 daarvan eindigen eerlijk op "open" (benedenrivier · kathode-expeditie · foliefabriek)*
- [ ] Elke overslag heeft **twee** ankers + terreinstappen — *Patache: 1 gelegd + 1 onzeker; benedenrivier: 2 open — géén compromis-coördinaten verzonnen*
- [ ] **Routeerpunt + max snap** genoteerd bij elk been-uiteinde op water/spoor — *b2-kop en b3-staart gemeten; overige "nog te bepalen"*
- [ ] **Dekking:** de gerouteerde lijn raakt alle *bevestigde* punten in volgorde (stedenpassages: 6 km-marge, zie been 3-kop)
- [ ] **Verklikker:** geen enkele plaats geraakt die niet in de brief staat
- [ ] Geen enkel **negatief anker** binnen zijn verbodsstraal geraakt
- [ ] Lengte per been binnen tolerantie — mét gereedschap, beide eindpunten en netstadium (b1: 192,4 OSM vs ±200 · b3: 516,6 km `maak_rivierbeen.py` op de MARNET-bulklaag, Shanghai→Tongling)
- [ ] Volumes sluiten aan over de verwerkingsknopen (§2) — *concentraatvolume deze streng niet vastgelegd; smelter- en foliecapaciteit wél [D1][D3][D5]*
- [ ] Elke stippellijn draagt een **reden**; elk reëel **alternatief** heeft een aandeel of een openstaand punt (§5.5, §5.11)
- [ ] De keten loopt door tot het eindproduct, óf het stoppunt is beargumenteerd — *stoppunt: foliefabriek; fase E-afnemers benoemd, plant-niveau niet gedocumenteerd (fase E-sectie)*

## 9 · Bronnen

**Leiding/Patache [P..]:** P1 OpenStreetMap (ODbL) via `fetch_pijpleidingen.py` — 14 ways
`substance=slurry`, 1.363 punten, 192,4 km tegen ±200 gepubliceerd; kartering stopt 736 m vóór het
terminalvlak · P2 Collahuasi bedrijfsmateriaal: espesadores → planta de molibdeno → planta de
filtro → stockpile → embarque · + eigen satelliet-overlay Esri z16, 2026-07-28.

**Zee [Z..]:** Z1 atlas-meting Collahuasi→Tongling 19.406 km / 2 overslagen (M26.1) · Z2
atlas-stand ?v=099 (2026-07-28): keten 19.299 km — leiding 193 (echte OSM-geometrie) · zee 18.590 ·
Yangtze 517; rivierbeen 516,6 km over 72 MARNET-bulkedges via `tools/maak_rivierbeen.py`.

**Yangtze [Y..]:** Y1 *长江干线航道列表* (wikipedia) + NDRC *长江干线过江通道布局规划 2020-2035* —
hoofdvaarweg 2.838 km, kilometrering vanaf de monding, klasse per traject (南通–浏河口 50.000 t;
南京 10.000 t) · Y2 loshavens Zhangjiagang/Jiangyin voor concentraat (projectnotitie M26.1) · Y3
Nanjing Yangtze-brug 1968, doorvaarthoogte ~24 m (LAR-514-onderzoek).

**Tongling [T..]:** T1 `data/vaarwegen-handmatig.geojson` + `tools/maak_tongling_oostgeul.py`
(18 punten, satelliet-gelegd Esri z14, go van Lars 2026-07-24, `?v=077`; kade-anker z16-hercheck
2026-07-28 ongewijzigd) · T2 `aansluitingen.json` — Baogang-pier Luojing, en de vaststelling dat
Yangshan een containerhaven op eilanden is.

**Fase D/E-research [D..] (2026-07-29, webresearch; passages via zoekextract tenzij anders vermeld):**
D1 央广网/cnr.cn 2025-03-26 — *铜陵有色金新铜业铜基新材料项目点火*: bouwstart december 2022,
10,3 mrd yuan, 500 kt/a hoogwaardig kopermateriaal + goud/zilver; hoofdwerken 熔炼·电解·制酸·
铜材加工·渣选矿; locatie 铜陵经开区 — https://www.cnr.cn/ah/jhfc/20250326/t20250326_527113743.shtml
(+ 中安在线/anhuinews 2025-06-23 over de volledige ingebruikname, artikel achter redirect) ·
D2 SMM news.metal.com — "the new project is put into production … largest single-series copper
smelting plant", naast het bestaande dubbel-flash-project — https://news.metal.com/newscontent/101166656
+ Sina Finance 2025-03-31 (全球首个50万吨产能铜冶炼项目点火) ·
D3 铜陵市工业和信息化局 — *打造世界铜冠 争创一流企业*: 金冠铜业 760 kt/a ("我国单体最大的矿铜冶炼工厂",
"世界铜冶炼标杆工厂"); verwerkingsproducten 铜箔/铜板带/漆包线/磷铜球/棒材 > 400 kt/a, "以皖江为主";
folie-capaciteit 80 kt/a (doel); afzet in PV/hogesnelheidsspoor/defensie, Fortune-500-ketens —
https://gxj.tl.gov.cn/tlsjjhxxhj/c00155/pc/content/content_1876201987618168832.html ·
D4 国信证券 (Guosen Securities) rapport 铜陵有色 000630.SZ, 2023-12-22 — "国外进口铜精砂到南通港
卸货后沿长江水运到公司，冶炼1吨粗铜需要4吨铜精矿…" (concentraat lost bij Nantong, verder per
Yangtze-binnenvaart; 4:1-verhouding) — https://pdf.dfcfw.com/pdf/H3_AP202312221614826947_1.pdf
(PDF lokaal opgeslagen; passage via zoekextract, regelnummer niet geverifieerd) ·
D5 铜冠铜箔-capaciteit en -bases: 财联社/cls.cn (55 kt/a: 35 PCB + 20 li; fase-2-project) +
cmpe360 (naar 80 kt/a) + 池州经开区-site (basis Chizhou) + 铜陵-investeringscentrum (fase 1
20 kt-project in bedrijf december 2017, 铜陵经开区; drie bases Tongling/Chizhou/Hefei) —
https://m.cls.cn/detail/980774 · https://czkfq.chizhou.gov.cn/Content/show/661822.html ·
D6 安徽铜冠铜箔集团 (301217), aankondiging verwachte verbonden-partijtransacties 2026
(2026-03-05): ~68% van de benodigde kathode intern van 铜陵有色; 2026 begroot: 阴极铜 496 mln +
铜丝 3.195 mln yuan — http://static.cninfo.com.cn/finalpage/2026-03-05/1224995566.PDF +
Sina Finance 2026-05-28 (PCB热潮"带飞"铜冠铜箔) ·
D7 SHFE-leveringsinfrastructuur: entrepotlijst per provincie (Shanghai · Guangdong · Jiangsu:
中储无锡/上港物流苏州/无锡国联/添马行/常州融达 · Zhejiang) via het 铜道-entrepot-dagrapport
2022-07-01 — https://www.tongdow.com/zixun/tong/chicangtongji/2022-07-01-578965.html; warrant
25 t + GB/T 467 (Cu+Ag ≥ 99,95%) uit de SHFE-contractdocumentatie via 平安期货 —
https://futures.pingan.com/touzizhejiaoyu/pinzhongjieshao/98822.shtml; de merkenbijlage zelf
(t20240104_801223) is achter een CAPTCHA niet geverifieerd (§5.13) ·
D8 芜湖铜冠电工有限公司 — TNMG-dochter in de 芜湖经开区, gelakte draad 10 kt/a (Ø 0,05–0,60 mm),
NEV-flatwire — https://pitchhub.36kr.com/project/2204964470141576 ·
D9 Sina Finance / 界面 2024-09-25 — *铜陵：电缆产能跃升300万公里*: stad Tongling 电磁线 400 kt/a,
铜杆 ~600 kt/a — https://finance.sina.com.cn/jjxw/2024-09-25/doc-incqivrv0804853.shtml ·
D10 Nantong-concentraathaven: 中国江苏网 2017-11-16 (grootste short-weight-zaak in tien jaar;
165 partijen concentraat in 2017) + Sina 2018-01-08 (进口铜精矿船舶集中到港) + 上海市商务委-archief
(江心过驳 als merk-goederensoort; ankerplaats-einde per eind 2017) —
https://jsnews.jschina.com.cn/nt/a/201711/t20171116_1194826.shtml ·
D11 铜冠铜箔-afnemers: onderzoeksrapport via Zhihu (2022) — PCB-folie top-5 2021H1: 生益科技 26,5% /
台燿科技 18,6% / 华正新材 11,3% / 金安国纪 8,5% / 台光电子 8,3%; lithiumfolie: BYD 43,01% / 45,02% /
58,14% van de li-folie-omzet 2019/2020/2021H1 — https://zhuanlan.zhihu.com/p/557170796.

**Eigen metingen:** satelliet-overlay Esri z16 2026-07-28 (Patache, Collahuasi, Tongling-kade) ·
Esri z14 2026-07-24 (oostgeul, go Lars) · `fetch_pijpleidingen.py` · `maak_rivierbeen.py` ·
`toets_ankers.py`. **Fase D/E: nog géén eigen satellietmeting — alle nieuwe punten wachten op de
z16-pass (§5.8).**
