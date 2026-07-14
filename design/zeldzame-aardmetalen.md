# Zeldzame aardmetalen — magneet-REE (NdPr + Dy/Tb) — ontwerp (op papier)
*Aangemaakt 2026-07-14 · herzien 2026-07-15 (optie 2: scherpe magneet-REE-framing i.p.v. "alle 17 elementen").*
*Status: ontwerp-skelet. Exacte coördinaten, volumes en operators = research (M8-issues).*
*Milestone (aan te maken in Linear): `M8 · Zeldzame aardmetalen`. Data-doel: `data/rare-earths.js` van "basis" → "uitgewerkt". Vul dit skelet aan tot een volledige brief volgens `design/_brief-template.md`, waarna het data-issue het 1-op-1 omzet.*

> **Framing-keuze (optie 2).** Niet "alle 17 zeldzame aarden" (dan wordt het een vage blob incl. de
> bulk-cerium/lanthaan voor glas en katalysatoren), maar de **magneet-REE**: het handjevol dat de
> geopolitiek draagt — **NdPr** (neodymium+praseodymium, licht, de massa van de magneetvraag) plus de
> zware toevoegingen **Dy/Tb** (dysprosium/terbium — maken de magneet hittebestendig). Zo leest de
> grondstof als één verhaal, net als lithium/kobalt, terwijl de winning eerlijk het **gemengde erts**
> blijft (je kunt Nd niet los uit de grond halen — dat is juist de crux).

> Principe: we modelleren de werkelijkheid, het plaatje vertelt zichzelf. De echte vorm hier: **winning
> breed verspreid, maar de scheiding van NdPr/Dy uit het mengsel zit ~85–90% in Zuid-China (Ganzhou),
> en de NdFeB-magneetproductie ~90%+ óók in China.** Drie dingen die lithium/koper niet hebben: (1) een
> **zware-REE-landstroom** over de grens Myanmar→China (Dy/Tb komt bijna 100% uit Chinese + Kachin-klei);
> (2) de emblematische **Mountain Pass-rondreis** (VS delft → China scheidt → oxide terug); (3) de
> **NdFeB-magneet-flessenhals** als eindstap — dé geopolitieke hefboom (China-exportvergunningen 2025).

## Metadata (→ `REGISTER({...})`) — sharpening t.o.v. de basis-file
| veld | huidige basis | voorstel (magneet-REE) |
|---|---|---|
| `id` | `rare-earths` | **ongewijzigd** (bestaande file + registratie in `_registry.js` intact) |
| `name` | "Zeldzame aardmetalen" | **"Zeldzame aardmetalen (magneet-REE)"** — knoplabel kort, focus zichtbaar |
| `symbol` | `REE` | **`NdPr`** (verhandeld product = NdPr-oxide; Dy/Tb als zware toevoeging) |
| `color` | `#C9A227` | ongewijzigd |
| `unit` | — | **`kt magneet-REO/jaar`** (NdPr + Dy/Tb-oxide-inhoud) — hele keten optelbaar |
| `blurb` | "17 elementen… China beheerst winning en scheiding." | **"De magneetmetalen NdPr + Dy/Tb voor EV-motoren, windturbines en defensie. China scheidt ~85–90% en maakt ~90%+ van de NdFeB-magneten."** |

## Weergave / modi (bevestigd)
- Magneet-REE reist per **schip + land** (net als lithium/kobalt/koper) → **hergebruikt de bestaande zee-A\*/
  land-A\*-routes (M3) en de scheeps-voyages (M4)**. **Géén nieuwe render-modus** (dat was het goud-stuk).
- Toggle `routes` ↔ `hemelsbreed` zoals lithium/koper (geen `air`-modus).
- **Licht vs. zwaar magneet-REE apart modelleren** — dit is de kern:
  - **NdPr (licht)** uit bastnäsiet/monaziet (Bayan Obo, Mountain Pass, Mount Weld). Stage `erts`.
  - **Dy/Tb (zwaar)** uit ionadsorptie-klei — bijna uitsluitend **Zuid-China + Myanmar (Kachin)**. Dít is de scherpste flessenhals: zonder Dy/Tb geen hittebestendige magneet. Visueel onderscheid via `stage`/annotatie.
- **NdFeB-magneet = de eindstap en het `product`.** In deze framing is de magneet ondubbelzinnig de product-stage; de eindtoepassingen (EV/wind/defensie) zijn consumptie-eindpunten, geen aparte stage. (Daarmee vervalt de eerdere open vraag "4e stage of niet".)
- **Recycling-laag** (magneetschroot → terug naar scheiding) als **optionele toggle** (`layer:"recycle"`, default uit) — het REE-equivalent van de goud-CB-/koper-beursvoorraden-laag.

## De keten & stages (→ `stage`-codes + kleur/booghoogte)
| stap | `stage`-code | kleur op de kaart | booghoogte | eenheid |
|---|---|---|---|---|
| 1. Winning → gemengd concentraat / ionklei | `erts` | donker/gedempt | laag (kruipt over oppervlak) | kt magneet-REO |
| 2. Scheiding/raffinage → NdPr/Dy-oxide + metaal | `raffinaat` | volle REE-kleur (#C9A227) | midden | kt magneet-REO |
| 3. NdFeB-magneet → EV/wind/defensie | `product` | licht, bijna wit | hoog | kt magneet-REO |

*Volumes indicatief in **kt magneet-REO/jaar** (alleen de NdPr + Dy/Tb-oxide-inhoud, niet de totale REO). Let op: een mijn-`share` telt dus zijn **magneet-relevante** fractie — Dy/Tb-rijke ionklei weegt zwaarder dan zijn tonnage, La/Ce-rijk erts weegt lichter. Wereld-NdPr-oxide ≈ 90–100 kt/jr; NdFeB-magneten ≈ 220–240 kt/jr (waarvan China ~90%+).*

## De lagen (nodes) — skelet
*(exacte lat/lon + kt/jr + operator = research M8; hieronder de knopen + de bedoelde stromen. De huidige `data/rare-earths.js` (basis) heeft 9 mijnen + 5 scheidingsfabrieken — dit skelet vult de kernknopen aan die het magneet-verhaal dragen: Zuid-China-klei, Myanmar/Kachin, Mount Weld, Sichuan, en de magneetfabrieken. La/Ce-only-bronnen mogen dun/tier-3.)*

### 1. Mijnbouw (breed verspreid — géén trechter; splits NdPr/Dy)
- **China — Bayan Obo** (Binnen-Mongolië, bastnäsiet, NdPr-bron) — grootste REE-mijn ter wereld. *(al in basis)*
- **China — Zuid-China ionklei** (Jiangxi/Ganzhou, Guangdong, Fujian) — **de Dy/Tb-bron**. **NIEUW, cruciaal.**
- **Myanmar — Kachin** (ionadsorptie-klei, Dy/Tb) → grens over naar Yunnan. **NIEUW, cruciaal (landstroom).**
- **VS — Mountain Pass** (Californië, MP Materials, bastnäsiet, NdPr). *(al in basis)*
- **Australië — Mount Weld** (Lynas, WA, monaziet/bastnäsiet, NdPr) — voedt Lynas Maleisië. **NIEUW.**
- **Vietnam** (Lai Chau) · **Brazilië** (Araxá) · **India** (kustmonaziet) · **Rusland** (Lovozero) — NdPr-relevant, houden. *(al in basis)*
- Projecten (`potential`): **Groenland** (Kvanefjeld) · **Zweden** (Per Geijer/Kiruna, LKAB) · Afrika (Songwe Hill Malawi, Ngualla Tanzania, Longonjo Angola). *(deels al in basis)*

### 2. Scheiding / raffinage (hier knijpt het samen: Zuid-China ~85–90%)
- **China — Ganzhou/Jiangxi** — wereldcentrum Dy/Tb-scheiding. *(al in basis)*
- **China — Baotou** (Binnen-Mongolië) — NdPr-scheiding + magneten, gekoppeld aan Bayan Obo. *(al in basis)*
- **China — Sichuan** (Leshan/Mianning) — NdPr-scheiding. **NIEUW.**
- **Maleisië — Lynas LAMP Kuantan** — grootste scheiding buiten China. *(al in basis)*
- **Estland — Silmet/Sillamäe** (Neo) — enige werkende REE-scheiding in de EU. *(al in basis)*
- **Frankrijk — La Rochelle (Solvay)** — REE-scheiding, heropstart voor magneten. *(al in basis)*
- Projecten: **VS — Mountain Pass on-site + Seadrift/Fort Worth (Texas)** · **Lynas Texas** — mine-to-magnet buiten China. **NIEUW (project).**

### 3. NdFeB-magneten — de downstream-flessenhals (stage `product`)
- **China** — Ningbo, Baotou, Ganzhou magneetclusters (~90%+ wereld-NdFeB). **NIEUW.**
- **Japan** — Shin-Etsu, Proterial (ex-Hitachi Metals), TDK — belangrijkste niet-Chinese makers (hoogwaardig). **NIEUW.**
- **Duitsland** — Vacuumschmelze (VAC, Hanau) — Europa's magneetmaker. **NIEUW.**
- Projecten: **VS — MP Materials Fort Worth**, e-VAC. **NIEUW (project).**

### 4. Havens & land-corridors
- **China**: Shanghai, Ningbo-Zhoushan, Tianjin (in- én uitvoer).
- **Mountain Pass → Long Beach → Stille Oceaan → China** (de rondreis).
- **Mount Weld → Fremantle → Kuantan (Maleisië)** (de Lynas-route, via Lombok/Sunda).
- **Kachin (Myanmar) → grensovergang Ruili/Yingjiang → Yunnan** — **NIEUWE land-flessenhals** (analoog aan Kasumbalesa voor kobalt).

### 5. Consumptie (magneet-eindgebruik — géén La/Ce-bulk)
- **EV-tractiemotoren** (China, EU/Duitsland, Japan, VS, Korea) · **windturbines** (direct-drive PMG: China + EU-offshore).
- **Defensie** (VS — F-35, raketten, sonar) · **robotica/elektronica** (voice coils, HDD, actuatoren).
- *Buiten scope in deze framing: katalysatoren/glas/polijstpoeder (dat is La/Ce-bulk, geen magneet-REE) — hooguit als grijze noot.*

### 6. Recycling (optionele toggle-laag — `layer:"recycle"`, default uit)
- Magneetschroot (productie-swarf, ~⅓ van elke magneet is afval) + end-of-life-magneten → terug naar scheiding. China (dominant) + EU: **HyProMag** (UK/Duitsland), **Solvay** (La Rochelle), MP (VS).
- **Weergave:** node-grootte = volume; laag standaard uit; chip alleen bij REE. Nuance eerlijk: recycling is nu <5% van het aanbod, wél strategisch en bij uitstek relevant voor NdFeB (magneet → magneet).

## Kern-stromen (illustratief)
- **Bayan Obo → Baotou** (NdPr, binnenlands, weg/spoor) — de lichte-magneet-loop.
- **Zuid-China klei → Ganzhou** (Dy/Tb, binnenlands) — de zware-scheiding.
- **Kachin (Myanmar) → Ruili → Ganzhou** (Dy/Tb, **land, grensoversteek**) — ~de helft van China's zware-REE-voeding.
- **Mountain Pass → China (Ganzhou/Sichuan) over de Stille Oceaan (schip)** — de emblematische rondreis (concentraat heen, oxide impliciet terug).
- **Mount Weld → Kuantan (Maleisië) (schip, via Lombok/Sunda)** — de enige scheidingsroute buiten China.
- **Kuantan → Japan (Shin-Etsu)/wereld** — gescheiden NdPr-oxide uit de niet-Chinese fabriek.
- **Chinese NdPr/Dy-oxide → Chinese magneetfabrieken (Ningbo/Baotou) → NdFeB-waaier** naar EV/wind/defensie wereldwijd — de downstream-flessenhals.
- **Chinese oxide → Japan (Shin-Etsu)/Duitsland (VAC)** — zelfs niet-Chinese magneetmakers kopen scheiding uit China.
- **EU-draadje**: Zweden/Noorwegen erts → Silmet (Estland)/La Rochelle (Frankrijk) → VAC — de dunne EU-magneetketen. *(deels al in basis)*
- **Recycling** (toggle): EU/China magneetschroot → scheiding → magneet.

## Emergent plaatje (wat je zou moeten zien als het klopt)
1. Mijn-stippen over álle continenten (VS, Australië, China, Brazilië, Vietnam, India, Afrika) — **winning is niet de flessenhals**.
2. Een dichte bundel scheidings-bogen die convergeren op **Zuid-China (Ganzhou/Sichuan/Baotou)** — nóg extremer dan lithium: zelfs Amerikaans erts vaart hierheen.
3. Een **Dy/Tb-landstroom over de grens Myanmar→China** (Kachin → Ruili → Ganzhou) — een land-flessenhals zoals Kasumbalesa; zwaar magneet-REE is bijna 100% China+Myanmar.
4. De **Mountain Pass-rondreis**: Amerikaans erts vaart naar China en komt terug — hét symbool van "we delven het, maar kunnen het niet scheiden".
5. Eén dun **niet-Chinees draadje**: Mount Weld → Lynas Maleisië → Japan/wereld — de enige scheiding buiten China.
6. Downstream een **NdFeB-magneet-waaier vanuit China** naar elke EV/wind/defensie-afnemer — de echte geopolitieke hefboom (2025-exportvergunningen op magneten + zware REE).
7. Een dunne, ambitieuze EU/VS-keten (Silmet, La Rochelle, MP Texas, VAC) die de lus probeert te sluiten.

## Knelpunten & vaarpunten
- Bestaande `wp-*` (uit `_chokepoints.js`) die magneet-REE raakt: **Stille Oceaan** (Mountain Pass→China), **Lombok/Makassar** (Mount Weld→Maleisië/China), **Malakka** (Kuantan/China west-export), **Taiwan/Zuid-Chinese Zee** (Chinese oostkust), **Suez/Bab el-Mandeb** (China↔Europa), **Kaap**.
- **NIEUWE land-flessenhals nodig:** grensovergang **Myanmar→China** (Kachin/Ruili–Yingjiang) — nieuw `grens-*`-punt in `_chokepoints.js`, analoog aan `grens-kasumbalesa` (`kind:"grensovergang"`, evt. `openRadius`). Dit is het enige nieuwe knelpunt.
- Institutionele "knijp" (geen zeestraat): de **scheidingsstap** (Ganzhou) én de **NdFeB-magneetfabricage** — geografisch geconcentreerd, zoals Ticino voor goud.

## Research-TODO (M8-research-issues, vóór `data/rare-earths.js`)
- [ ] Exacte lat/lon per nieuwe node (Zuid-China klei, Kachin, Mount Weld, Sichuan, magneetfabrieken).
- [ ] Volumes kt magneet-REO/jr per stroom, gesplitst **NdPr (licht) vs. Dy/Tb (zwaar)** (USGS MCS · Adamas Intelligence · IEA · bedrijfsrapporten Lynas/MP/Neo).
- [ ] Magneet-relevante `share` per mijn (NdPr/Dy-fractie, niet totale REO) — dit herweegt de bolgroottes.
- [ ] Myanmar-Kachin-volume + grenscorridor (Ruili/Yingjiang) — hoeveel van China's Dy/Tb komt hiervandaan.
- [ ] Operators + status per scheidings-/magneetfabriek (Lynas, MP, Solvay, Neo/Silmet, Shin-Etsu, VAC).
- [ ] Beleid: China-exportvergunningen 2023–2025 (scheidingstech-verbod, magneet-/zware-REE-licenties) — als `tensions`.

## Bouw-TODO (na research)
- [ ] **NdPr/Dy-onderscheid** + de **Myanmar-grenscorridor** op bestaande land-A\*-infra (nieuw `grens-*`-punt). **Geen nieuwe route-generator.**
- [ ] `data/rare-earths.js` van "basis" → "uitgewerkt" volgens het lithium-schema: magneet-framing in `name`/`symbol`/`unit`/`blurb` (zie metadata-tabel), alle lagen + `detail:"uitgewerkt"`; al geregistreerd in `_registry.js`.
- [ ] **Recycling-toggle**: optionele laag (`layer:"recycle"`) volgens het CB/beursvoorraden-patroon.
- [ ] Verifiëren: routes plausibel, 0 kapotte routes (headless legs-check), Ganzhou-scheidingstrechter + Myanmar-landstroom + Mountain-Pass-rondreis + NdFeB-waaier zichtbaar, scheeps-voyages lopen, single-file build + visuele bevestiging → wrapup.
