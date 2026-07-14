# Uranium — ontwerp (op papier)
*Aangemaakt 2026-07-15 · status: ontwerp-skelet. Exacte coördinaten, volumes en operators = research (M9-issues).*
*Milestone (aan te maken in Linear): `M9 · Uranium`. Data-doel: `data/uranium.js` van "basis" (9 nodes / 2 flows) → "uitgewerkt" volgens het lithium/goud-schema. Vul dit skelet aan tot een volledige brief volgens `design/_brief-template.md`, waarna het data-issue het 1-op-1 omzet.*

> **De echte vorm (waarom uranium interessant is om uit te werken).** Bij lithium/koper/REE zit de knijp bij de
> **raffinage** (China/Indonesië). Bij uranium ligt de flessenhals **twee stappen verderop** en in een **vijandige
> staat**: de winning is breed verspreid, maar ~44% van de wereld­**verrijking** (SWU) staat in **Rusland**
> (Rosatom). Dat is een institutionele/technologische knijp zoals de Zwitserse goudraffinage (Ticino) — geen
> zeestraat, wél een keiharde afhankelijkheid. Drie dingen die de atlas nog niet heeft: (1) een **4-staps keten**
> (winning → conversie → verrijking → splijtstof → reactor) i.p.v. het 3-staps batterij­sjabloon; (2) **twee
> landlocked routeringen** — Kazachstan (~43% van de winning!) en Niger — met de nieuwe **Trans-Kaspische route**
> die om Rusland heen de-riskt; (3) de **VVER-brandstof-lock-in** (Rusland levert splijtstof voor zijn eigen
> reactorontwerpen in Midden-Europa).

> Principe: we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig — het plaatje vertelt zichzelf.
> Voor uranium is de "aha" dat winnen het probleem *niet* is: het erts komt van overal, maar wie geen toegang tot
> **verrijking** heeft, heeft geen splijtstof. En de grootste mijnbouwer (Kazachstan) zit ingeklemd — zijn erts
> moet fysiek langs of om Rusland heen naar de wereldmarkt.

## Weergave / modi (bevestigd)
- Uranium reist per **schip + land** (kleine, hoogwaardige vracht in verzegelde vaten/cilinders) → **hergebruikt de
  bestaande zee-A\*/land-A\*-routes (M3) en de scheeps-voyages (M4)**. **Géén nieuwe render-modus nodig.**
- Toggle `routes` ↔ `hemelsbreed` zoals lithium/koper (geen verplichte `air`-modus).
- **Optioneel (niet-blokkerend):** enkele intercontinentale UF6/verrijkt-U-legs mogen de **bestaande `air`-modus uit
  M6 (goud)** hergebruiken — luchtvracht is voor deze cargo realistisch. Standaard echter schip+land, om de
  landlocked-routes juist zichtbaar te maken (dat is het hele punt).
- **Optionele toggle-laag "militaire kringloop / secundaire voorraden"** (`layer:"secondary"`, default uit) — het
  uranium-equivalent van de goud-CB-laag en de koper-beursvoorraden-laag, exact hetzelfde `layer`-filterpatroon.

## De keten & stages (→ `stage`-codes + kleur/booghoogte)
De echte keten is 4-staps, maar we mappen hem op de bestaande 3 stages door **conversie bij `erts` te voegen** (het
blijft "feed", nog niet verrijkt) en de **verrijking tot de visuele `raffinaat`-knijp** te maken — precies waar het
verhaal zit. (Zoals REE de "4e stage?"-vraag oploste door binnen 3 te blijven.)

| stap | `stage`-code | kleur op de kaart | booghoogte | eenheid |
|---|---|---|---|---|
| 1. Winning → yellowcake (U₃O₈) **+ conversie → UF₆** | `erts` | donker/gedempt | laag (kruipt over oppervlak) | tU |
| 2. **Verrijking → verrijkt UF₆** (de flessenhals) | `raffinaat` | volle uraankleur (#A3E635) | midden | tU |
| 3. Splijtstoffabricage → brandstofelementen | `product` | licht, bijna wit | hoog | tU |

*Alle volumes indicatief in **tU/jaar** (ton uranium-inhoud), zodat de hele keten optelbaar blijft. Nuance:
verrijking meet eigenlijk in **SWU** en scheidt feed in verrijkt product + verarmde "tails" (minder massa in het
product) — voor de relatieve dikte op de kaart houden we tU aan en noteren de SWU/tails-nuance bij `tensions`.
Wereldmijnproductie ≈ 60 kt U/jr; reactorbehoefte ≈ 65 kt U/jr (het gat vullen secundaire voorraden — zie de
optionele laag). Peiljaar ±2023/24; bronnen WNA / IAEA Red Book / USGS.*

## De lagen (nodes) — skelet
*(exacte lat/lon + tU/jr + operator = research M9; hieronder de knopen + de bedoelde stromen. De huidige
`data/uranium.js` (basis) heeft 6 mijnen + 3 "refinery"-knopen die conversie/verrijking op één hoop gooien — dit
skelet splitst conversie ≠ verrijking ≠ splijtstof en voegt de reactoren + de landlocked-corridors toe.)*

### 1. Winning → yellowcake (breed verspreid — géén trechter; `stage: erts`)
- **Kazachstan (~43%)** — Kazatomprom, **ISR** in de Chu-Sarysu/Syrdarya-bekkens (Inkai, Budenovskoye, Tortkuduk).
  **LANDLOCKED — dit is de routeringscrux.** JV's met Cameco/Orano/CGN/Rosatom. *(al in basis, uitbreiden)*
- **Canada (~15%)** — Cameco, Athabasca-bekken (Cigar Lake, McArthur River), Saskatchewan. *(al in basis)*
- **Namibië (~11%)** — Husab (CGN/Swakop) + Rössing (CNNC) — **Chinees eigendom**, export via Walvis Bay. *(al in basis)*
- **Australië (~9%)** — Olympic Dam (BHP, bijproduct), Four Mile, Honeymoon. **NIEUW.**
- **Oezbekistan (~7%)** — Navoi, ISR. **NIEUW.**
- **Rusland (~5%)** — Rosatom/ARMZ, Priargunsky (Krasnokamensk). **NIEUW.**
- **Niger (~4%)** — Orano, Arlit/SOMAIR. **LANDLOCKED** (historisch per truck naar Cotonou/Lomé); **verstoord na de
  coup van 2023** → sterke `tension`. **NIEUW.**
- Projecten/klein (`potential`, géén share): **VS** (heropstart Wyoming/Texas), China (groeiend, binnenlands),
  Oekraïne (VostGOK), Zuid-Afrika, Groenland (Kvanefjeld — verboden). *(deels al in basis)*

### 2. Conversie (U₃O₈ → UF₆; handvol fabrieken, `stage: erts` — nog feed)
- **Canada** — Cameco Port Hope (Ontario). **NIEUW.**
- **Frankrijk** — Orano Malvési (→UF₄) + Tricastin/Pierrelatte (→UF₆). **NIEUW.**
- **Rusland** — Rosatom (Seversk/Angarsk). **NIEUW.**
- **China** — CNNC. **VS** — Metropolis, Illinois (Honeywell, heropstart). **NIEUW.**

### 3. Verrijking (UF₆ → verrijkt UF₆) — **DE FLESSENHALS** (`stage: raffinaat`)
- **Rusland — Rosatom/TVEL** (Seversk, Zelenogorsk, Novouralsk, Angarsk) — **~44% wereld-SWU**. **Dít is de knijp.**
  *(basis heeft "Rusland-refinery" — dit wordt de kern-node)*
- **Urenco** — Almelo (NL), Gronau (DE), Capenhurst (UK), Eunice/New Mexico (VS). **NIEUW.**
- **Frankrijk — Orano Georges Besse II** (Tricastin). *(basis heeft "Frankrijk-refinery")*
- **China — CNNC** (Lanzhou, Hanzhong). **NIEUW.**

### 4. Splijtstoffabricage (verrijkt U → brandstofelementen; `stage: product`)
- **VS** — Westinghouse (Columbia SC), Global Nuclear Fuel (Wilmington NC). **NIEUW.**
- **Frankrijk/Duitsland** — Framatome (Romans-sur-Isère; Lingen). **Zweden/UK** — Westinghouse (Västerås; Springfields). **NIEUW.**
- **Rusland — TVEL** (Novosibirsk, Elektrostal) — **VVER-brandstofmonopolie** (zie tension). **NIEUW.**
- **Zuid-Korea** (KEPCO NF), **Japan** (GNF-J), **China** (CNNC). **NIEUW.**

### 5. Reactoren / consumptie (waar het eindigt)
- **VS** (~93 reactoren, grootste vloot), **Frankrijk** (~56), **China** (snelst groeiend, bouwt fors),
  **Rusland**, **Zuid-Korea**, **Japan** (heropstart), **Canada**, **India**, **UK**.
- **VVER-vloot in Midden-Europa** (Rusland-ontwerp, Russische brandstof-lock-in): **Hongarije** (Paks), **Tsjechië**
  (Dukovany/Temelín), **Slowakije** (Mochovce), **Bulgarije** (Kozloduy), **Finland** (Loviisa). Westinghouse
  kwalificeert nu VVER-brandstof om de lock-in te breken. **NIEUW — draagt het downstream-verhaal.**

### 6. Militaire kringloop / secundaire voorraden (optionele toggle-laag — `layer:"secondary"`, default uit)
- **Down-blending van wapen-HEU** → reactorbrandstof (historisch "Megatons to Megawatts": Rusland-HEU → VS-reactoren,
  1993–2013 — symbolisch, inmiddels beëindigd). **Herverrijking van tails.** Strategische reserves: **US DOE**,
  **Rosatom**.
- **Weergave:** node-grootte = volume; laag standaard uit; chip alleen bij uranium. Nuance eerlijk: secundaire
  voorraden vullen het gat tussen mijn (~60 kt) en reactorbehoefte (~65 kt) — geen mijnbouw, wél markt-relevant.

## Kern-stromen (illustratief)
- **Kazachstan → verrijking, twee concurrerende routes** — dé kern van dit ontwerp:
  - **Noord/Rusland-route** (historisch, land): Kazachstan → per spoor door Rusland → **St. Petersburg** → Oostzee
    (**wp-deense-straten**) → wereldmarkt. Kort, maar sanctierisico.
  - **Trans-Kaspische route** (de-risking, NIEUW, gemengd land+zee): Kazachstan → **Aktau** → **Kaspische Zee** →
    **Bakoe** → per spoor door Georgië → **Poti/Batumi** → Zwarte Zee → **Bosporus** → Middellandse Zee →
    **Gibraltar** → Europa/N-Amerika. *(de nieuwe Kaspische wateroversteek is het te bouwen stuk — zie bouw-TODO)*
- **Canada (Port Hope) → Urenco/Orano-verrijking** (Atlantic) en **Canada → eigen splijtstof** (binnenlands).
- **Namibië (Walvis Bay) → China (CNNC-conversie/verrijking)** — Chinees erts naar Chinese keten (Kaap of Malakka).
- **Niger (Arlit) → Cotonou/Lomé over land → Frankrijk (Orano)** — de tweede landlocked-corridor (post-coup verstoord).
- **Australië → VS/Frankrijk/China** verrijking (Pacific / Kaap).
- **Verrijkt UF₆ → splijtstoffabrieken → reactoren**: Urenco/Orano → Westinghouse/Framatome → EU/VS-reactoren; de
  waaier van de `product`-stage.
- **VVER-lock-in**: **Rusland (TVEL) → Paks/Dukovany/Mochovce/Kozloduy** — Russische splijtstof voor Russische
  reactorontwerpen in de EU (eenrichtings-afhankelijkheid).
- **Militaire kringloop** (toggle): Rusland-HEU → down-blend → VS-reactoren (historisch); tails → herverrijking.

## Emergent plaatje (wat je zou moeten zien als het klopt)
1. Mijn-stippen over álle continenten (Kazachstan, Canada, Namibië, Australië, Oezbekistan, Rusland, Niger) —
   **winning is niet de flessenhals**.
2. Een **dun ringetje verrijkings-nodes** (Rusland, Urenco-kwartet, Orano, CNNC) waar álle erts doorheen moet — en
   Rusland is de dikste stip. De knijp zit niet op zee maar bij één processing-stap, zoals Ticino bij goud.
3. **Kazachstan zit ingeklemd**: twee zichtbaar concurrerende bogen naar de wereldmarkt — de korte door Rusland, en
   de lange Trans-Kaspische omweg (Aktau → Bakoe → Poti → Bosporus) die het hele Rusland-risico visualiseert.
4. **Niger als tweede landstroom** — erts dat over land naar een West-Afrikaanse haven moet (Cotonou), nu haperend.
5. Downstream een **VVER-lock-in-lijn Rusland → Midden-Europa**: Russische splijtstof die één kant op stroomt naar
   reactoren die alleen op die brandstof draaien.
6. Toggle militaire kringloop → down-blend-nodes + de historische HEU-stroom Rusland → VS + tails-herverrijking.

## Knelpunten & vaarpunten
- Bestaande `wp-*` (uit `_chokepoints.js`) die uranium raakt: **wp-deense-straten** (Oostzee-uitgang, St. Petersburg),
  **wp-bosporus** + **ll-bosporus** (Zwarte Zee), **wp-gibraltar**, **wp-suez/wp-bab** (Azië↔Europa), **wp-kaap**
  (Namibië/Australië → Azië), **wp-panama**, **wp-malakka** (Namibië/erts → China).
- **NIEUW te bouwen — de Kaspische wateroversteek (Aktau ↔ Bakoe):** de Kaspische Zee is een *ingesloten* zee en valt
  in het grove raster waarschijnlijk als land → **water forceren** zoals Lombok/Suez (nieuw `wp-kaspisch`
  vaarpunt/segment). Dit is hét nieuwe route-element van deze grondstof. Daarna land-A\* door de Kaukasus (Bakoe →
  Poti) — check of dat bestaande land-links dekt of dat er een `grens-*`/`ll-*` bij moet.
- **NIEUW mogelijk — Niger-landcorridor:** Arlit → grens → Cotonou/Lomé (analoog aan `grens-kasumbalesa`). Niger is
  ~4% en verstoord; optioneel, maar het maakt het "twee landlocked-drama's"-plaatje compleet.
- **Institutionele "knijp" (geen zeestraat):** de **verrijkingsstap in Rusland** (~44% SWU) én de **VVER-brandstof-
  lock-in** — geografisch/technologisch geconcentreerd, zoals Ticino voor goud. Draag dit via `tensions`, niet via een `wp-`.

## Research-TODO (M9-research-issues, vóór `data/uranium.js`)
- [ ] Exacte lat/lon per nieuwe node (mijnen, conversie Port Hope/Malvési/Seversk, verrijking Urenco-kwartet/Tricastin/
      Rosatom-sites, splijtstoffabrieken, reactor-clusters, VVER-centrales).
- [ ] Volumes tU/jr per stroom (WNA Nuclear Fuel Report · IAEA/OECD-NEA Red Book · USGS MCS · Kazatomprom/Cameco/Orano-rapporten).
- [ ] Verrijkings-SWU-aandeel per speler (Rosatom ~44% verifiëren; Urenco/Orano/CNNC-splitsing) → weegt de `raffinaat`-nodes.
- [ ] Kazachstan-routering: actuele mix Rusland-route vs. Trans-Kaspische route (Aktau-tonnage, spoor Bakoe→Poti).
- [ ] Niger post-coup status (Orano/SOMAIR productie + exportcorridor Cotonou/Lomé).
- [ ] VVER-afhankelijkheid: welke EU-centrales nog op Russische TVEL-brandstof draaien vs. Westinghouse-kwalificatie.
- [ ] Beleid als `tensions`: **VS-verbod op Russisch verrijkt uranium (2024)** + **HALEU-afhankelijkheid** (Rusland is
      de enige commerciële HALEU-leverancier voor SMR's/geavanceerde reactoren) + EU-sanctiediscussie.

## Bouw-TODO (na research)
- [ ] **Kaspische wateroversteek** (Aktau↔Bakoe) als geforceerd waterpunt + de land-A\*-leg Bakoe→Poti (nieuw
      `wp-kaspisch`, evt. `openRadius`/`ll-*`). **Dit is het enige echt nieuwe route-element.** Optioneel: Niger-`grens-*`.
- [ ] **Conversie ≠ verrijking ≠ splijtstof** splitsen (nu 3 refinery-knopen op één hoop) en op de 3 stages mappen
      (`erts` = winning+conversie, `raffinaat` = verrijking, `product` = splijtstof). Reactoren = `market`. *Optioneel:
      eigen marker-types `conversie`/`verrijking`/`fuel` — anders `refinery` hergebruiken (géén nieuwe marker-styling).*
- [ ] `data/uranium.js` van "basis" → "uitgewerkt" volgens het lithium-schema: alle lagen + `detail: "uitgewerkt"`,
      sharpere `blurb` (winning breed / verrijking ~44% Rusland); al geregistreerd in `_registry.js`.
- [ ] **Militaire-kringloop-toggle**: optionele laag (`layer:"secondary"`) volgens het CB/beursvoorraden-patroon
      (filter + config-size + ui-chip + marker-vorm).
- [ ] Verifiëren: routes plausibel, **0 kapotte routes** (headless legs-check — elke ship-leg landt op een kustpunt;
      Kazachstan-corridors kloppen), verrijkings-flessenhals + Trans-Kaspische omweg + VVER-lock-in zichtbaar,
      scheeps-voyages lopen voor uranium, single-file build + visuele bevestiging op Netlify/mobiel → wrapup.
