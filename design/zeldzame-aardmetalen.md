# Zeldzame aardmetalen — ontwerp (op papier)
*Aangemaakt 2026-07-14 · status: ontwerp-skelet. Exacte coördinaten, volumes en operators = research (M8-issues).*
*Milestone (aan te maken in Linear): `M8 · Zeldzame aardmetalen`. Data-doel: `data/rare-earths.js` van "basis" → "uitgewerkt". Vul dit skelet aan tot een volledige brief volgens `design/_brief-template.md`, waarna het data-issue het 1-op-1 omzet.*

> Principe: we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig — het plaatje vertelt
> zichzelf. Voor lithium is dat "raffinage door China"; zeldzame aardmetalen zijn hetzelfde thema in het
> extreme én met een nieuwe geografische vorm. **Winning is breed verspreid, maar de scheiding zit voor
> ~85–90% in Zuid-China (Ganzhou) en de magneet-productie (NdFeB) voor ~90%+ óók in China.** Twee dingen
> die lithium/koper niet hebben: (1) een **zware-REE-landstroom** die de grens Myanmar→China oversteekt
> (Dy/Tb komt bijna 100% uit Chinese + Kachin-klei), en (2) de emblematische **Mountain Pass-rondreis**:
> de VS delft het, maar vaart het naar China om het te láten scheiden en krijgt het als oxide terug.

## Weergave / modi (bevestigd)
- REE reist per **schip + land** (net als lithium/kobalt/koper) → **hergebruikt de bestaande zee-A\*/land-A\*-
  routes (M3) en de scheeps-voyages (M4)**. **Géén nieuwe render-modus** (dat was het goud-specifieke stuk).
- Toggle `routes` ↔ `hemelsbreed` zoals lithium/koper (geen `air`-modus).
- **Licht vs. zwaar REE apart modelleren** — dit is de kern van de grondstof:
  - **Licht REE (Nd/Pr/La/Ce)** uit bastnäsiet/monaziet (Bayan Obo, Mountain Pass, Mount Weld). Stage `erts`.
  - **Zwaar REE (Dy/Tb/Y)** uit ionadsorptie-klei — bijna uitsluitend **Zuid-China + Myanmar (Kachin)**. Dít is de echte flessenhals: zonder Dy/Tb geen hittebestendige magneten. Visueel onderscheid via `stage`/annotatie.
- **Magneten (NdFeB) als eindstap** — de échte geopolitieke hefboom zit één stap ná de scheiding. Standaard stage `product`, met een open bouw-vraag: een aparte 4e stage `magneet` splitsen? (nieuwe stage = stage-styling toevoegen in de code, zie template-waarschuwing.)
- **Recycling-laag** (magneetschroot → terug naar scheiding) als **optionele toggle** (`layer:"recycle"`, default uit) — het REE-equivalent van de goud-CB-/koper-beursvoorraden-laag.

## De keten & stages (→ `stage`-codes + kleur/booghoogte)
| stap | `stage`-code | kleur op de kaart | booghoogte | eenheid |
|---|---|---|---|---|
| 1. Winning → concentraat / ionklei | `erts` | donker/gedempt | laag (kruipt over oppervlak) | kt REO |
| 2. Scheiding/raffinage → oxides/metalen | `raffinaat` | volle REE-kleur (#C9A227) | midden | kt REO |
| 3. Magneten (NdFeB) → eindtoepassing | `product` | licht, bijna wit | hoog | kt REO |

*Alle volumes indicatief in **kt REO/jaar** (rare-earth-oxide-inhoud), zodat de keten optelbaar blijft. Wereldmijnproductie ≈ 390 kt REO; scheiding ≈ 300 kt (waarvan ~85–90% China); NdFeB-magneten ≈ 220–240 kt (waarvan China ~90%+).*

## De lagen (nodes) — skelet
*(exacte lat/lon + kt REO/jr + operator = research M8; hieronder de knopen en de bedoelde stromen. De huidige `data/rare-earths.js` (basis) heeft al 9 mijnen + 5 scheidingsfabrieken — dit skelet vult de ontbrekende kernknopen aan: Zuid-China-klei, Myanmar/Kachin, Mount Weld, Sichuan, magneetfabrieken.)*

### 1. Mijnbouw (breed verspreid — géén trechter; splits licht/zwaar)
- **China — Bayan Obo** (Binnen-Mongolië, bastnäsiet, licht REE) — grootste REE-mijn ter wereld. *(al in basis)*
- **China — Zuid-China ionklei** (Jiangxi/Ganzhou, Guangdong, Fujian) — **de zware-REE-bron** (Dy/Tb). **NIEUW, cruciaal.**
- **Myanmar — Kachin** (ionadsorptie-klei, zwaar REE) → grens over naar Yunnan. **NIEUW, cruciaal (landstroom).**
- **VS — Mountain Pass** (Californië, MP Materials, bastnäsiet, licht REE). *(al in basis)*
- **Australië — Mount Weld** (Lynas, WA, monaziet/bastnäsiet, licht REE) — voedt Lynas Maleisië. **NIEUW.**
- **Vietnam** (Lai Chau/Dong Pao) · **Brazilië** (Araxá) · **India** (kustmonaziet) · **Rusland** (Lovozero) — *(al in basis)*.
- Projecten (`potential`, geen share): **Groenland** (Kvanefjeld) · **Zweden** (Per Geijer/Kiruna, LKAB) · Afrika (Songwe Hill Malawi, Ngualla Tanzania, Longonjo Angola). *(deels al in basis)*

### 2. Scheiding / raffinage (hier knijpt het samen: Zuid-China ~85–90%)
- **China — Ganzhou/Jiangxi** — wereldcentrum zware-REE-scheiding. *(al in basis)*
- **China — Baotou** (Binnen-Mongolië) — lichte-REE-scheiding + magneten, gekoppeld aan Bayan Obo. *(al in basis)*
- **China — Sichuan** (Leshan/Mianning) — lichte-REE-scheiding. **NIEUW.**
- **Maleisië — Lynas LAMP Kuantan** — grootste scheiding buiten China. *(al in basis)*
- **Estland — Silmet/Sillamäe** (Neo) — enige werkende REE-scheiding in de EU. *(al in basis)*
- **Frankrijk — La Rochelle (Solvay)** — REE-scheiding, heropstart voor magneten. *(al in basis)*
- Projecten: **VS — Mountain Pass on-site + Seadrift/Fort Worth (Texas)** · **Lynas Texas** — mine-to-magnet buiten China. **NIEUW (project).**

### 3. Magneten (NdFeB) — de downstream-flessenhals (stage `product` / evt. 4e stage)
- **China** — Ningbo, Baotou, Ganzhou magneetclusters (~90%+ wereld-NdFeB). **NIEUW.**
- **Japan** — Shin-Etsu, Proterial (ex-Hitachi Metals), TDK — belangrijkste niet-Chinese makers (hoogwaardig). **NIEUW.**
- **Duitsland** — Vacuumschmelze (VAC, Hanau) — Europa's magneetmaker. **NIEUW.**
- Projecten: **VS — MP Materials Fort Worth**, e-VAC. **NIEUW (project).**

### 4. Havens & land-corridors
- **China**: Shanghai, Ningbo-Zhoushan, Tianjin (in- én uitvoer).
- **Mountain Pass → Long Beach → Stille Oceaan → China** (de rondreis).
- **Mount Weld → Fremantle → Kuantan (Maleisië)** (de Lynas-route, via Lombok/Sunda).
- **Kachin (Myanmar) → grensovergang Ruili/Yingjiang → Yunnan** — **NIEUWE land-flessenhals** (analoog aan Kasumbalesa voor kobalt).

### 5. Consumptie (China-dominant, maar breed)
- **EV-tractiemotoren** (China, EU/Duitsland, Japan, VS, Korea) · **windturbines** (direct-drive PMG: China + EU-offshore).
- **Defensie** (VS — F-35, raketten, sonar) · **elektronica/robotica** · **katalysatoren/glas** (licht REE: La/Ce).

### 6. Recycling (optionele toggle-laag — `layer:"recycle"`, default uit)
- Magneetschroot (productie-swarf) + end-of-life → terug naar scheiding. China (dominant) + EU: **HyProMag** (UK/Duitsland), **Solvay** (La Rochelle), MP (VS).
- **Weergave:** node-grootte = volume; laag standaard uit; chip alleen bij REE. Nuance eerlijk modelleren: recycling is nu <5% van het aanbod, wél strategisch.

## Kern-stromen (illustratief)
- **Bayan Obo → Baotou** (licht REE, binnenlands, weg/spoor) — de lichte-REE-loop.
- **Zuid-China klei → Ganzhou** (zwaar REE, binnenlands) — de zware-REE-scheiding.
- **Kachin (Myanmar) → Ruili → Ganzhou** (zwaar REE, **land, grensoversteek**) — ~de helft van China's zware-REE-voeding.
- **Mountain Pass → China (Ganzhou/Sichuan) over de Stille Oceaan (schip)** — de emblematische rondreis (concentraat heen, oxide impliciet terug).
- **Mount Weld → Kuantan (Maleisië) (schip, via Lombok/Sunda)** — de enige scheidingsroute buiten China.
- **Kuantan → Japan (Shin-Etsu)/wereld** — gescheiden oxides uit de niet-Chinese fabriek.
- **Chinese oxides → Chinese magneetfabrieken (Ningbo/Baotou) → magneet-waaier** naar EV/wind/defensie wereldwijd — de downstream-flessenhals.
- **Chinese oxides → Japan (Shin-Etsu)/Duitsland (VAC)** — zelfs niet-Chinese magneetmakers kopen scheiding uit China.
- **EU-draadje**: Zweden/Noorwegen erts → Silmet (Estland)/La Rochelle (Frankrijk) — de dunne EU-keten. *(al in basis)*
- **Recycling** (toggle): EU/China magneetschroot → scheiding.

## Emergent plaatje (wat je zou moeten zien als het klopt)
1. Mijn-stippen over álle continenten (VS, Australië, China, Brazilië, Vietnam, India, Afrika) — **winning is niet de flessenhals**.
2. Een dichte bundel scheidings-bogen die convergeren op **Zuid-China (Ganzhou/Sichuan/Baotou)** — nóg extremer dan lithium: zelfs Amerikaans erts vaart hierheen.
3. Een **zware-REE-landstroom over de grens Myanmar→China** (Kachin → Ruili → Ganzhou) — een land-flessenhals zoals Kasumbalesa; zwaar REE (Dy/Tb) is bijna 100% China+Myanmar.
4. De **Mountain Pass-rondreis**: Amerikaans erts vaart naar China en komt terug — hét symbool van "we delven het, maar kunnen het niet scheiden".
5. Eén dun **niet-Chinees draadje**: Mount Weld → Lynas Maleisië → Japan/wereld — de enige scheiding buiten China.
6. Downstream een **magneet-waaier vanuit China** naar elke EV/wind/defensie-afnemer — de echte geopolitieke hefboom (2025-exportvergunningen).
7. Een dunne, ambitieuze EU/VS-keten (Silmet, La Rochelle, MP Texas, VAC) die de lus probeert te sluiten.

## Knelpunten & vaarpunten
- Bestaande `wp-*` (uit `_chokepoints.js`) die REE raakt: **Stille Oceaan** (Mountain Pass→China), **Lombok/Makassar** (Mount Weld→Maleisië/China), **Malakka** (Kuantan/China west-export), **Taiwan/Zuid-Chinese Zee** (Chinese oostkust), **Suez/Bab el-Mandeb** (China↔Europa), **Kaap**.
- **NIEUWE land-flessenhals nodig:** grensovergang **Myanmar→China** (Kachin/Ruili–Yingjiang) — nieuw `grens-*`-punt in `_chokepoints.js`, analoog aan `grens-kasumbalesa` (`kind:"grensovergang"`, evt. `openRadius`). Dit is het enige nieuwe knelpunt.
- Institutionele "knijp" (geen zeestraat): de **scheidingsstap zelf** (Ganzhou) én de **NdFeB-magneetfabricage** — geografisch geconcentreerd, zoals Ticino voor goud.

## Research-TODO (M8-research-issues, vóór `data/rare-earths.js`)
- [ ] Exacte lat/lon per nieuwe node (Zuid-China klei, Kachin, Mount Weld, Sichuan, magneetfabrieken).
- [ ] Volumes kt REO/jr per stroom, gesplitst **licht vs. zwaar REE** (USGS MCS · Adamas Intelligence · IEA · bedrijfsrapporten Lynas/MP/Neo).
- [ ] Aandelen winning/scheiding/magneten actueel verifiëren (China-scheiding ~85–90%, magneten ~90%+).
- [ ] Myanmar-Kachin-volume + grenscorridor (Ruili/Yingjiang) — hoeveel van China's zware REE komt hiervandaan.
- [ ] Operators + status per scheidings-/magneetfabriek (Lynas, MP, Solvay, Neo/Silmet, Shin-Etsu, VAC).
- [ ] Beleid: China-exportvergunningen 2023–2025 (scheidingstech-verbod, magneetlicenties) — als `tensions`.

## Bouw-TODO (na research)
- [ ] **Licht/zwaar-REE-onderscheid** + de **Myanmar-grenscorridor** op bestaande land-A\*-infra (nieuw `grens-*`-punt). **Geen nieuwe route-generator.**
- [ ] Beslissen: magneet als stage `product` óf een aparte 4e stage `magneet` (dan stage-styling toevoegen in de render-laag).
- [ ] `data/rare-earths.js` van "basis" → "uitgewerkt" volgens het lithium-schema; alle lagen + `detail:"uitgewerkt"`; al geregistreerd in `_registry.js`.
- [ ] **Recycling-toggle**: optionele laag (`layer:"recycle"`) volgens het CB/beursvoorraden-patroon.
- [ ] Verifiëren: routes plausibel, 0 kapotte routes (headless legs-check), Ganzhou-scheidingstrechter + Myanmar-landstroom + Mountain-Pass-rondreis zichtbaar, scheeps-voyages lopen, single-file build + visuele bevestiging → wrapup.
