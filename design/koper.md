# Koper — ontwerp (op papier)
*Aangemaakt 2026-07-14 · status: ontwerp-skelet. Exacte coördinaten, volumes en operators = research (LAR-404 / LAR-405).*
*Milestone: `M7 · Koper` (LAR-404 t/m LAR-409). Vul dit skelet aan tot een volledige brief volgens `design/_brief-template.md`, waarna LAR-407 het 1-op-1 naar `data/copper.js` omzet.*

> Principe: we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig — het plaatje vertelt
> zichzelf. Voor lithium is dat "alles door China"; voor koper is het bijna hetzelfde maar één stap
> verderop: **mijnbouw breed verspreid met een Andes-zwaartepunt, maar ~50% van de raffinage in China**.
> Concentraat vaart van Chili/Peru over de Stille Oceaan naar Chinese smelters en komt als kathode terug.
> Daarnaast een tweede, kleinere trechter: de **Afrikaanse Copperbelt** (DR Congo/Zambia) die over land
> naar de kust moet vóór hij de wereldmarkt op kan.

## Weergave / modi (bevestigd)
- Koper reist per **schip + land** (net als lithium/kobalt) → **hergebruikt de bestaande zee-A\*/land-A\*-routes
  (M3) en de scheeps-voyages (M4)**. **Géén nieuwe render-modus** — dat was juist het goud-specifieke stuk.
- Toggle `routes` ↔ `hemelsbreed` zoals lithium/kobalt (geen `air`-modus).
- **Twee productvormen die apart gemodelleerd worden (LAR-406):**
  - **Concentraat** (sulfide-erts, ~25–30% Cu) → smelter → kathode. Stage `erts`.
  - **SX-EW-kathode** (oxide-erts, direct bij de mijn geraffineerd) → reist meteen als afgewerkt metaal, zónder smelter-tussenstop. Stage `raffinaat` al bij de bron.
  - Visueel onderscheid via `stage` + annotatie (evt. subtiele lijnstijl), zodat je de trechter-naar-China (concentraat) los ziet van het directe kathode-verkeer.
- **Beursvoorraden-laag** (LME/SHFE/COMEX) als **optionele toggle** (LAR-408) — het koper-equivalent van de goud-CB-laag.

## De keten & stages (→ `stage`-codes + kleur/booghoogte)
| stap | `stage`-code | kleur op de kaart | booghoogte | eenheid |
|---|---|---|---|---|
| 1. Winning → concentraat / oxide-erts | `erts` | donker/gedempt | laag (kruipt over oppervlak) | kt Cu |
| 2. Smelten/raffineren → kathode (incl. SX-EW) | `raffinaat` | volle koperkleur (#C87D4A) | midden | kt Cu |
| 3. Halffabricaat → draadstaven/buizen | `product` | licht, bijna wit | hoog | kt Cu |

*Alle volumes indicatief in **kt Cu-inhoud/jaar** (metaalinhoud, niet bruto erts), zodat de hele keten optelbaar blijft. Wereldmijnproductie ≈ 22.000 kt Cu, geraffineerd ≈ 26.000 kt (incl. schroot).*

## De lagen (nodes) — skelet
*(exacte lat/lon + kt Cu/jr + operator = research LAR-404/405; hieronder de knopen en de bedoelde stromen)*

### 1. Mijnbouw (Andes-zwaartepunt, breed verspreid)
- **Chili** (~24% wereld): Escondida (BHP), Collahuasi, El Teniente (Codelco), Chuquicamata (Codelco), Los Pelambres — deels sulfide (concentraat), deels oxide (SX-EW).
- **Peru**: Cerro Verde (Freeport), Antamina, Las Bambas (MMG), Toromocho.
- **DR Congo** (Copperbelt): Kamoa-Kakula (Ivanhoe/Zijin), Tenke Fungurume (CMOC), Kolwezi — grotendeels **SX-EW-kathode**.
- **Zambia** (Copperbelt): Kansanshi (First Quantum), Lumwana, Mopani.
- **China** (binnenlands, bescheiden t.o.v. de raffinage): diverse.
- **VS**: Morenci (Freeport), Bingham Canyon (Rio Tinto) — Arizona/Utah.
- **Australië**: Olympic Dam (BHP), Mount Isa.
- **Rusland**: Norilsk (Nornickel — koper-nikkel).
- **Indonesië**: Grasberg (Freeport, Papoea).
- **Kazachstan**: Kazakhmys/KAZ Minerals. · **Mexico**: Buenavista (Grupo México).
- **Polen**: KGHM (Lubin/Głogów — grootste EU-mijn). · **Zweden**: Aitik (Boliden).

### 2. Smelting / raffinage (hier knijpt het samen: China ~50%)
- **China** (de trechter): Jiangxi Copper (Guixi), Tongling, Jinchuan, Yanggu Xiangguang, Daye — samen ~⅘ van Azië's smeltcapaciteit.
- **Chili**: Chuquicamata, Chagres, Caletones — smelters bij de mijnen (Chili exporteert zowel concentraat als kathode).
- **Japan**: Pan Pacific (Saganoseki/Tamano), Sumitomo (Toyo), Mitsubishi (Naoshima).
- **Duitsland**: Aurubis Hamburg — grootste raffinaderij van Europa. · **Polen**: KGHM Głogów/Legnica.
- **DRC/Zambia**: SX-EW-kathodeplants pal bij de mijn. · **India**: Hindalco/Adani, Vedanta (Tuticorin, stilgelegd).

### 3. Havens & Copperbelt-landcorridors
- **Chili**: Antofagasta, Mejillones, Angamos, Valparaíso. · **Peru**: Callao, Matarani, Ilo.
- **China-invoer**: Shanghai, Ningbo-Zhoushan, Qingdao, Tianjin.
- **Copperbelt → kust (landcorridors, hergebruik kobalt-infra):**
  - Zuid: DRC/Zambia → **Kasumbalesa-grensovergang** → Durban / Richards Bay (per truck/spoor).
  - Oost: → Dar es Salaam (TAZARA-corridor).
  - West: → Walvis Bay (Namibië) · **Lobito-corridor** (Angola, nieuwe spoorlijn) — kandidaat.

### 4. Consumptie (China-dominant)
- **China** (~50%+ van de vraag): elektriciteitsnet, bouw, EV, elektronica, airco.
- **Europa** (Duitsland — kabels/auto), **VS**, **India**, **Japan/Korea**.
- Semi's-fabricage: draadstaven (wire rod), buizen, walserijen.

### 5. Recycling / schroot (~⅓ van het aanbod)
- Koperschroot → terug naar smelters. **Nieuw schroot** (fabricage-afval) vs. **oud schroot** (end-of-life).
- Stromen: Europa, VS, Japan → China (historisch groot) + binnenlandse secundaire smelters.

### 6. Beursvoorraden (optionele toggle-laag — LAR-408)
- **LME-magazijnen**: Rotterdam, Busan, Kaohsiung, Johor (Maleisië), New Orleans, Gwangyang.
- **SHFE** (Shanghai, bonded) · **COMEX** (VS).
- **Weergave:** node-grootte = voorraadniveau; laag staat standaard uit. **Nuance eerlijk modelleren:** beursvoorraad ≠ verbruik — het is buffer-/handelsvoorraad.

## Kern-stromen (illustratief)
- **Andes-concentraat** (Chili/Peru sulfide) → Antofagasta/Callao → **Stille Oceaan** → Chinese smelters (Ningbo/Shanghai) = de hoofdtrechter.
- **SX-EW-kathode** (DRC/Zambia oxide) → Kasumbalesa → Durban/Dar es Salaam → wereldmarkt (Azië/Europa) — zónder smelter.
- **Chili-kathode** → eigen smelters → markt (deels ook direct).
- **Grasberg/Australië** → Chinese/Japanse smelters (Lombok/Makassar of directe Pacific).
- **Recycling**: EU/VS/Japan-schroot → China + binnenlandse secundaire smelters.
- **Halffabricaat**: Chinese kathode → draadstaven → binnenlandse + Aziatische fabricage.

## Emergent plaatje (wat je zou moeten zien als het klopt)
1. Mijn-stippen over meerdere continenten, met een duidelijk **Andes-zwaartepunt** (Chili/Peru).
2. Een dikke bundel **concentraat-bogen over de Stille Oceaan die convergeren op de Chinese smelters** = de koper-"aha" (zoals China bij lithium).
3. Een tweede, aparte trechter: de **Afrikaanse Copperbelt** die eerst over **land** naar Durban/Dar es Salaam kruipt vóór hij de zee op gaat — en die als **kathode** (niet concentraat) reist.
4. **China = grootste smelter én grootste verbruiker** — pijlen naar binnen én binnenlands rondgaand.
5. Toggle beursvoorraden → LME/SHFE/COMEX-nodes + schroot-loop terug naar de smelters.

## Knelpunten & vaarpunten
- Bestaande `wp-*` (uit `_chokepoints.js`) die koper raakt: **Stille Oceaan** (Andes→China), **Lombok/Makassar** (Australië/Indonesië→China), **Malakka** (Afrika/Atlantic→China), **Panamakanaal** (Pacific-ZA↔Atlantic/Europa), **Suez/Bab el-Mandeb** (Europa↔Azië), **Kaap de Goede Hoop**.
- Land: **Kasumbalesa** (Copperbelt-grensovergang, al in de M5-set) + Copperbelt-corridors naar Durban/Dar es Salaam/Walvis Bay/Lobito.
- Nieuwe knelpunten nodig? Waarschijnlijk niet — check tijdens LAR-406 of de Copperbelt-corridors bestaande land-links dekken.

## Research-TODO (LAR-404 / LAR-405, vóór `data/copper.js`)
- [ ] Exacte lat/lon per node (mijnen, smelters, havens, LME/SHFE/COMEX-magazijnen).
- [ ] Volumes kt Cu/jr per stroom (USGS Mineral Commodity Summaries · ICSG · Wood Mackenzie · IEA).
- [ ] Per mijn: concentraat (sulfide) vs. SX-EW-kathode (oxide) — dit stuurt de stromen.
- [ ] Operators + capaciteiten per smelter/raffinaderij.
- [ ] Copperbelt-corridors: welke mijn via welke haven (Durban / Dar es Salaam / Walvis Bay / Lobito).
- [ ] Beursvoorraad-locaties + indicatieve niveaus (LME/SHFE/COMEX).

## Bouw-TODO (na research)
- [ ] **Productvorm-onderscheid** (LAR-406): concentraat vs. kathode visueel + de Copperbelt-landroutes op bestaande infra. **Geen nieuwe route-generator.**
- [ ] `data/copper.js` (LAR-407): van "basis" → "uitgewerkt" volgens het lithium-schema; alle lagen + `detail: "uitgewerkt"`; al geregistreerd in `_registry.js`.
- [ ] **Beursvoorraden-toggle** (LAR-408): optionele laag + schroot-loop.
- [ ] Verifiëren (LAR-409): routes plausibel, 0 kapotte routes (headless legs-check), China-smelttrechter zichtbaar, scheeps-voyages lopen voor koper, single-file build + visuele bevestiging op Netlify/mobiel → wrapup.
