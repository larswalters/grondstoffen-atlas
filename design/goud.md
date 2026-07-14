# Goud — ontwerp (op papier)
*Aangemaakt 2026-07-14 · status: ontwerp-skelet. Exacte coördinaten, volumes en operators = research volgende sessie.*

> Principe: we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig — het plaatje vertelt
> zichzelf. Voor lithium is dat "alles door China"; voor goud is de vorm anders (mijnbouw wijd verspreid,
> raffinage geknepen in Zwitserland, een handvol kluis-/handelshubs, China als eenrichtings-put).

## Weergave / modi (bevestigd)
- **Toggle `routes` ↔ `hemelsbreed`** net als lithium.
  - `hemelsbreed` = directe great-circle-boog (opgetild, hoogte ∝ afstand).
  - `routes` = **echte luchtroutes via luchthaven-nodes** + weg/spoor-legs voor de korte Europese hops.
- **Great-circle-boog is voor goud correct** (goud vliegt écht die boog) — voor lithium was hij juist fout.
- **Voyages-playback:** lichtpuntjes/vliegtuig-glyphs over de luchtlijnen; teller "hoeveel goud / hoeveel zendingen".
- **Zee-A\*** speelt vrijwel geen rol; **transportmodi:** lucht (intercontinentaal, dominant) + weg/spoor (Europa kort).
- **Luchthaven-granulariteit:** kleine/artisanale mijnen clusteren naar regionale gateway-luchthaven.

## De lagen (nodes) — skelet
*(exacte lat/lon + t/jr = research; hieronder de knopen en de bedoelde stromen)*

### 1. Mijnbouw (wijd verspreid — géén trechter)
- China (Shandong-cluster) · Rusland (Olimpiada/Polyus, Siberië) · Australië (Kalgoorlie Super Pit, Boddington, Cadia)
- Canada (Ontario/Québec — Detour, Malartic) · VS (Nevada — Carlin/Cortez) · Kazachstan · Uzbekistan (Muruntau)
- Peru (Yanacocha) · Mexico · Brazilië · Ghana (Obuasi/Tarkwa) · West-Afrika artisanaal (Mali Loulo-Gounkoto, Burkina)
- Indonesië (Grasberg, Papoea) · Papoea-Nieuw-Guinea (Lihir/Porgera) · Zuid-Afrika (Witwatersrand — Mponeng) · Sudan (artisanaal → Dubai)

### 2. Raffinage (hier knijpt het samen: Zwitserland/Ticino)
- **Zwitserland:** Valcambi (Balerna), PAMP (Castel San Pietro), Argor-Heraeus (Mendrisio), Metalor (Neuchâtel) — samen ~⅔–70% wereld.
- Perth Mint (AU) · MMTC-PAMP (IN) · Dubai (o.a. Emirates Gold) · China-intern (Zijin/China Gold, insulair)
- Rand Refinery (ZA) · Royal Canadian Mint (CA) · Japan (Tanaka/Mitsubishi)

### 3. Handels- & kluishubs (klein aantal, schuiven ook onderling)
- **Londen (LBMA)** — Bank of England-kluis + commercieel (JPMorgan/HSBC/Brink's/Malca-Amit/Loomis); prijsbenchmark
- **New York** — COMEX-kluizen + NY Fed (custodie buitenlands CB-goud)
- **Zürich** · **Shanghai (SGE)** · **Dubai (DMCC)** · **Singapore** · **Hongkong** (conduit naar China)

### 4. Consumptie (waar het eindigt)
- India (sieraden — import via Mumbai/Delhi) · China (sieraden + belegging) · Midden-Oosten/Turkije (sieraden)
- Tech/electronica: Japan/Korea/Taiwan (klein aandeel) · Westerse belegging: baren/munten (Duitsland, VS)

### 5. Centrale banken (optionele toggle-laag)
- **Voorraden:** VS (Fort Knox/West Point/Denver + NY Fed voor anderen) · Duitsland (Frankfurt) · Italië · Frankrijk
  · Rusland (Moskou) · China (Beijing) · Zwitserland · Japan · India · Nederland (DNB)
- **Huidige kopers/stromen (2022–2025):** Polen (naar Warschau), China, Turkije, India (repatrieerde 2024),
  Kazachstan, Tsjechië, Singapore. Rusland = absorbeert eigen mijnproductie (geen wereldmarkt-koop).
- **Weergave:** node-grootte = voorraad; stromen = repatriëringsvluchten (Londen/Zürich → hoofdstad) +
  accumulatie. Nuance: veel "koop" is titeloverdracht ín een kluis (blijft in Londen).

### 6. Recycling
- Schroot → terug naar raffinage: India · Italië (Arezzo/Vicenza sieraadschroot) · China · Midden-Oosten · Turkije

## Kern-stromen (illustratief)
- Mijn-doré → gateway-luchthaven → **ZRH → weg → Ticino-raffinage** (de grote convergentie)
- Zwitserse baren → ZRH → **LHR (Londen)** / **JFK (NY)** / **DXB** / **SIN** / **HKG→Shanghai**
- **Londen ↔ Zürich ↔ New York** (interbancaire kluisoverdrachten)
- Londen/Zürich → **India (DEL/BOM)** voor sieraden · Dubai → India (corridor)
- **Hongkong → Shanghai** (China in, eenrichting)
- Recycling: India/Italië/Midden-Oosten schroot → raffinaderijen
- CB: Londen/Zürich → **Warschau / Delhi / Beijing** (repatriëring)

## Emergent plaatje (wat je zou moeten zien als het klopt)
1. Mijn-stippen over álle continenten — geen enkel land domineert de mijnbouw.
2. Een spectaculaire convergentie van doré-bogen uit de hele wereld op **één hoekje Ticino** = de visuele knijp.
3. Vanuit Zwitserland waaieren bogen uit naar een kleine ring kluis-/handelshubs (Londen/NY/Zürich/Shanghai/Dubai/Singapore) die óók onderling verbonden zijn.
4. **China = pijlen naar binnen, niets naar buiten** (eenrichtings-put).
5. **India = grote consumptie-instroom** + recycling terug.
6. Toggle centrale banken → voorraad-nodes + repatriëringsvluchten + de huidige inkoopgolf.
7. Alles beweegt via **luchtbogen**; enkele Europese weg/spoor-legs.

## Research-TODO (volgende sessie, vóór `data/goud.js`)
- [ ] Exacte lat/lon per node (mijnen, raffinaderijen, luchthavens, kluizen).
- [ ] Volumes t/jr per stroom (World Gold Council / USGS / LBMA / Metals Focus).
- [ ] Operators + capaciteiten per raffinaderij.
- [ ] Actuele CB-kopers + tonnages (WGC central-bank-data).
- [ ] Mapping welke mijnen naar welke gateway-luchthaven clusteren.

## Bouw-TODO (na research)
- [ ] Air-route path-generator (great-circle, opgetilde boog) als derde route-modus naast zee-A\* en land-A\*.
- [ ] `voyages.js` uitbreiden: lichtpuntjes/vliegtuig-glyph over luchtlijnen.
- [ ] `data/goud.js` volgens lithium-schema + registreren in `_registry.js`.
- [ ] Verifiëren in de atlas (routes plausibel, Ticino-trechter zichtbaar, labels) → wrapup.
