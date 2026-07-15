# Nikkel — ontwerp (op papier)
*Aangemaakt 2026-07-15 · **status: ✅ GEBOUWD** (2026-07-15) → `data/nickel.js` = "uitgewerkt" (± 55 nodes / ± 45 flows / 6 tensions).*
*Milestone: `M10 · Nikkel`. Cijfers indicatief/afgerond (USGS MCS 2025 = peiljaar 2024, IEA, INSG, bedrijfsrapportages) — dezelfde standaard als goud/koper/uranium; exacte verfijning kan later.*

> Principe: we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig — het plaatje vertelt
> zichzelf. Voor lithium is dat "alles door China", voor koper "raffinage knijpt in China". **Voor nikkel
> is de trechter net andersom: Indonesië heeft in tien jaar niet alleen de mijnbouw maar óók de raffinage
> naar zich toe getrokken.** De exportban op ruw erts (2014 gedeeltelijk, 2020 volledig) dwong de smelters
> aan land te komen — grotendeels met Chinees kapitaal (Tsingshan, Huayou) in de industrieparken IMIP
> (Morowali) en IWIP (Weda Bay). Het erts blíjft dus in Indonesië; wat de zee op gaat is al NPI, matte of MHP.

## De nikkel-"aha" in 3 zinnen
1. **Indonesië = mijn én smelter.** Op de kaart zie je het erts níet de zee op gaan als ruw laterite (zoals
   bij koper het concentraat wél doet), maar in korte hops mijn→smelter binnen Sulawesi/Halmahera blijven —
   dan pas vertrekt het als half- of eindproduct. Dat is de exportban die zichtbaar wordt.
2. **Twee nikkels, twee markten.** Class-2 (NPI/ferronikkel, RKEF uit lateriet) → **roestvrij staal** (~⅔ van
   de vraag, China/Tsingshan). Class-1 (nikkelsulfaat/kathode, ≥99,8%) → **EV-batterijen**. HPAL (→ MHP) en
   matte zijn de bruggen die goedkoop Indonesisch lateriet tóch batterijwaardig maken.
3. **De prijscrash ruimt de rest op.** De Indonesische overvloed heeft de nikkelprijs gecrasht en de
   klassieke class-1-winning (Australië, Nieuw-Caledonië, deels Canada) stilgelegd — een structurele
   shakeout, geen conjunctuurdip.

## Weergave / modi (bevestigd)
- Nikkel reist per **schip + land** (net als koper/kobalt) → **hergebruikt de bestaande zee-A\*/land-A\*-routes
  (M3) en de scheeps-voyages (M4)**. **Géén nieuwe render-modus.**
- **Géén nieuw chokepoint nodig.** Alle knelpunten bestaan al: **Straat van Makassar** + **Lombok** (Sulawesi/
  Australië → Oost-Azië), **Zuid-Chinese Zee** + **Straat van Taiwan** (convergentie op China), **Deense Straten**
  (Fins Baltisch nikkel → EU), **Panamakanaal** + de Pacific-vaarpunten (Cuba/Nieuw-Caledonië), de
  **Saint-Laurent-keten** (Voisey's Bay → Sudbury). Dit is de tweede grondstof (na koper) die volledig op de
  bestaande routekaart draait.
- **Beursvoorraden-laag (LME):** hergebruikt de **bestaande** optionele `type:"exchange"`/`layer:"exchange"`-
  toggle van koper — **nul engine-wijziging** (de chip/marker/gate zijn al generiek: `hasExchangeStocks()` = elke
  actieve grondstof met een exchange-node). De nikkel-nuance is scherper dan bij koper: **alleen class-1 is
  LME-leverbaar** (NPI/MHP/sulfaat niet), waardoor de LME-prijs losraakte van de fysieke batterij-/staalmarkt —
  plus de **short-squeeze van maart 2022** (Tsingshan, ~$100k/t, geannuleerde trades).
- **Recycling = always-on** (net als koper, niet achter de toggle): roestvrij-staalschroot is ~⅓ van de
  staalinput. `type:"recycler"`, `stage:"erts"` (feedstock terug naar de smelters), géén `layer`.

## De keten & stages (→ `stage`-codes + kleur/booghoogte)
| stap | `stage`-code | kleur op de kaart | booghoogte | eenheid |
|---|---|---|---|---|
| 1. Winning → ruw lateriet / sulfide-erts / -concentraat | `erts` | donker/gedempt staalgrijs | laag | kt Ni |
| 2. Smelten/raffineren → NPI · ferronikkel · matte · MHP · geraffineerd class-1 · nikkelsulfaat | `raffinaat` | volle staalkleur | midden | kt Ni |
| 3. Eindproduct → roestvrij staal · batterijkathode/-cel | `product` | licht, bijna wit | hoog | kt Ni |

*Alle volumes indicatief in **kt Ni-inhoud/jaar** (metaalinhoud, niet bruto lateriet), zodat de hele keten
optelbaar blijft. Wereldmijnproductie 2024 ≈ 3.700 kt Ni; Indonesië ≈ 55–60% daarvan.*

## De lagen (nodes) — skelet

### 1. Mijnbouw (Indonesië-dominant, lateriet in de tropen + een krimpende sulfide-gordel)
- **Indonesië (~55%)** — lateriet, blíjft in het land: **Weda Bay** (Halmahera, Eramet/Tsingshan), **Sorowako**
  (Vale, Sulawesi, matte op locatie), **Morowali-district** (IMIP-feed, Centraal-Sulawesi), **Pomalaa** (Antam,
  SO-Sulawesi), **Obi** (Harita, Noord-Molukken, HPAL).
- **Filipijnen (~9%)** — lateriet, **exporteert nog wél ruw erts** naar China (géén ban): Surigao/Taganito
  (Nickel Asia), Coral Bay/Palawan (SMM HPAL → Japan). Het levende contrast met de Indonesische ban.
- **Nieuw-Caledonië (~6%)** — SLN/Doniambo + Prony/Goro; in structurele crisis door de prijscrash.
- **Rusland (~5%)** — Norilsk (Nornickel, sulfide, class-1), Kola/Monchegorsk-raffinage; sanctie-gevoelig.
- **Canada (~5%)** — Sudbury (Vale/Glencore, sulfide) + Voisey's Bay (Vale, Labrador, via de Saint-Laurent).
- **Australië (~4%)** — BHP Nickel West / Mt Keith **grotendeels stilgelegd (2024)** = de shakeout in beeld;
  Murrin Murrin (Glencore, lateriet) draait nog.
- **China (~3%)** — Jinchuan (Gansu, sulfide, class-1). · **Brazilië (~2%)** — Barro Alto (Anglo). ·
  **Madagaskar** — Ambatovy (HPAL, class-1). · **Cuba** — Moa (Sherritt).

### 2. Smelting / raffinage (de nieuwe Indonesische cluster + de oude class-1-garde)
- **Indonesië (de trechter):** IMIP-Morowali (Tsingshan RKEF → NPI + roestvrij; HPAL), IWIP-Weda Bay (RKEF/HPAL,
  matte), QMB/Huayou-HPAL Morowali (MHP → batterij), Harita-Obi HPAL, Pomalaa-HPAL (Vale/Huayou, **project**).
- **China (batterijchemie + roestvrij):** nikkelsulfaat/precursor (Huayou/GEM/CNGR), Jinchuan (klassiek class-1).
- **De oude class-1-garde (krimpend):** Harjavalta (Finland, Nornickel — batterijnikkel), Nikkelverk
  Kristiansand (Noorwegen, Glencore — hoogzuiver), Sudbury (Canada), Kola/Monchegorsk (Rusland),
  Terrafame Sotkamo (Finland — geïntegreerd mijn+sulfaat), Sumitomo Niihama (Japan, matte uit de Filipijnen —
  let op de Seto-brug, net als koper), Korea (POSCO/precursor).

### 3. Havens & landcorridors
- **Indonesische smelters = coastal** (captieve jetty's in IMIP/IWIP/Obi) → schepen direct vanaf de smelter.
- **Filipijnen:** Surigao (ruw-ertsexport). · **China-invoer:** Rizhao (roestvrij + ruw erts). ·
  **Sorowako-matte:** via Malili (kust) → Japan. · **Brazilië:** Vitória. · **Madagaskar:** Toamasina.

### 4. Consumptie (roestvrij staal = ⅔, batterij = snelst groeiend)
- **China** (roestvrij: Foshan/Tsingshan · batterij: CATL/BYD-kathode) · **Korea** (LG/SK batterij) ·
  **EU** (roestvrij Outokumpu · batterij BASF/cathode) · **India** (Jindal roestvrij) · **VS** (superlegeringen/
  lucht­vaart) · **Japan** (roestvrij + legeringen).

### 5. Recycling (always-on)
- Roestvrij-staalschroot (~⅓ van de staalinput) → terug naar de mills/smelters. EU, China, VS.

### 6. Beursvoorraden (optionele toggle-laag — hergebruik koper)
- **LME-magazijnen:** Rotterdam, Johor, Busan, Baltimore, Singapore. Node-grootte = voorraad; laag default uit.
- **Nuance eerlijk modelleren:** buffer-/handelsvoorraad ≠ verbruik; en **alleen class-1 is leverbaar** →
  de LME-prijs vertegenwoordigt niet de fysieke NPI-/sulfaatmarkt (de 2022-squeeze legde dat bloot).

## Kern-stromen (illustratief)
- **Intra-Indonesië** (`erts`, road/kort): mijn → IMIP/IWIP/Obi-smelter — het erts blíjft in het land (de ban).
- **Indonesië → China roestvrij** (`raffinaat`, ship via Makassar/Lombok → SCS → Taiwan → Rizhao): NPI/slab.
- **Indonesië → China/Korea batterij** (`raffinaat`, ship): MHP/matte → nikkelsulfaat.
- **Filipijnen → China** (`erts`, ship): ruw lateriet — het contrast met de ban. · **Filipijnen → Japan**
  (Coral Bay HPAL → Sumitomo/Niihama).
- **Class-1-garde** (`raffinaat`/`product`, land + korte zee): Norilsk→Kola, Voisey's→Sudbury (Saint-Laurent),
  Nikkelverk/Harjavalta/Terrafame → EU-batterij (Deense Straten / bruggen), Sumitomo → Japan.
- **Nieuw-Caledonië → China/Korea/Japan** (ferronikkel, ship via de Pacific-vaarpunten + Taiwan).
- **Eindproduct** (`product`): sulfaat → kathode → batterijmarkten; NPI → roestvrij → staalmarkten.
- **Recycling**: EU/China/VS-schroot → mills. · **Beursvoorraden** (`layer:"exchange"`): class-1 → LME.

## Emergent plaatje (wat je zou moeten zien als het klopt)
1. Een **dichte kluwen korte hops in Indonesië** (Sulawesi + Halmahera): het erts gaat niet de zee op maar
   naar de smelter ernaast = de exportban.
2. Twee **waaiers uit Indonesië naar China**: een dikke NPI/roestvrij-bundel én een batterij-bundel
   (MHP/matte → sulfaat), beide door **Makassar/Lombok → SCS → Taiwan**.
3. Eén **ruw-erts-boog Filipijnen → China** ernaast = het levende contrast (geen ban).
4. Een **dunner, krimpend "oude wereld"-web** van class-1 (Rusland/Canada/Noorwegen/Finland) — zichtbaar
   kleiner dan de Indonesische massa = de shakeout.
5. Toggle beursvoorraden → LME-nodes; besef dat die class-1-voorraad niet de echte (NPI/sulfaat) markt is.

## Knelpunten & vaarpunten (allemaal bestaand)
- `wp-makassar`, `wp-lombok`, `wp-scs`, `wp-taiwan` (Indonesië/Australië/NC → Oost-Azië) ·
  `wp-deense-straten` (Fins/Baltisch nikkel → EU) · `wp-panama` + `wp-pac-*` (Cuba/NC) ·
  `wp-malakka`/`wp-singapore`/`wp-moz-noord` (Brazilië/Madagaskar → Azië) · de `wp-st-laurent-*`-keten
  (Voisey's Bay → Sudbury). **Nieuw knelpunt: geen.**

## Research-TODO (vóór `data/nickel.js`) — ✅ inline verwerkt
- [x] Mijn-shares 2024 (USGS MCS 2025): Indonesië ~55–60%, Filipijnen ~9%, Rusland/Canada/NC ~5% elk.
- [x] Class-1 vs class-2 per node (RKEF/NPI vs HPAL/MHP vs sulfide/matte) — dit stuurt `stage` + `note`.
- [x] IMIP/IWIP/Obi-smelters + operators (Tsingshan/Eramet/Huayou/Harita) + captieve jetty's (coastal).
- [x] LME-magazijnlocaties + de class-1-leverbaarheids-nuance + de 2022-squeeze.

## Bronnen
USGS Mineral Commodity Summaries 2025 (nikkel, peiljaar 2024) · INSG · IEA *Global Critical Minerals Outlook*
· Benchmark Mineral Intelligence (klasse-1/2) · LME (nikkelcontract + 2022-squeeze) · bedrijfsrapportages
(Vale Indonesia, Eramet, Nornickel, Glencore, Sumitomo Metal Mining, Nickel Asia, Harita, Huayou).
