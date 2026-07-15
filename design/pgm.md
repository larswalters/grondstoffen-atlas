# Platinagroepmetalen (PGM) — ontwerp (op papier)
*Aangemaakt 2026-07-15 · **status: ✅ GEBOUWD** (2026-07-15) → `data/pgm.js` = "uitgewerkt" (± 44 nodes / ± 42 flows / 6 tensions).*
*Milestone: `M12 · PGM`. Cijfers indicatief/afgerond (USGS MCS 2025 = peiljaar 2024, Johnson Matthey PGM Market Report, WPIC, bedrijfsrapportages) — dezelfde standaard als goud/koper/nikkel; exacte verfijning kan later.*

> Principe: we vertellen geen verhaal, we modelleren de werkelijkheid nauwkeurig — het plaatje vertelt
> zichzelf. Voor lithium is dat "alles door China", voor goud "raffinage knijpt in Zwitserland". **Voor PGM
> is het de meest EXTREME twee-landen-concentratie van de hele atlas: Zuid-Afrika (het Bushveld-complex)
> levert het leeuwendeel van het platina en het rodium, Rusland (Norilsk) domineert het palladium.** Twee
> metalen, twee landen, twee eindmarkten — en een verwerkingsstap die dwars door een handvol westerse
> edelmetaalhuizen loopt (Johnson Matthey, BASF, Umicore, Heraeus) die óók de gebruikte katalysatoren recyclen.

## De PGM-"aha" in 3 zinnen
1. **Eén geologische formatie + één Russische mijn dragen de wereld.** Op de kaart zie je vrijwel al het
   platina/rodium uit het Bushveld (een dichte kluwen mijnen bij Rustenburg + de Noord- en Oost-rand) en
   vrijwel al het palladium uit Norilsk — de scherpste bron-concentratie sinds de zeldzame aardmetalen.
2. **PGM vliegt, net als goud.** Geraffineerd platina/palladium/rodium is per kilo even waardevol als goud
   → het reist als beveiligde **luchtvracht** (hergebruik van de goud-air-mode), niet over zee. Alleen de
   concentraat-/matte-hops binnen Zuid-Afrika/Rusland (en de Zimbabwaanse matte naar Zuid-Afrika) gaan over land.
3. **De vraag hangt aan de uitlaatpijp.** ~80–90% van het rodium, het gros van het palladium en ~40% van het
   platina gaat in **autokatalysatoren**; emissieregelgeving stuurt alles, en als de Pt/Pd-prijzen omdraaien
   substitueren autobouwers het ene metaal voor het andere. De hedge tegen de EV-transitie is **waterstof**
   (Pt in PEM-elektrolysers en brandstofcellen).

## Weergave / modi (bevestigd)
- PGM reist als **luchtvracht** → **hergebruikt de bestaande goud-air-mode** (`mode:"air"`: great-circle-boog,
  buiten de A\*-routering om, hoogte ∝ afstand). De concentraat-/matte-legs binnen een land zijn `road`/`rail`
  (land-A\*). **Géén nieuwe render-modus.** De tijdlijn toont automatisch "vluchten" i.p.v. "schepen"
  (`activeHasAir()` vuurt op elke `mode:"air"`-stroom — 0 engine-wijziging).
- **Géén nieuw chokepoint én geen nieuw vaarpunt.** Luchtvracht negeert de zeestraten volledig; de landhops
  lopen over bestaande, aaneengesloten landmassa's (Rustenburg-cluster, Zimbabwe→Zuid-Afrika over Beitbridge,
  Finland→continent via de bestaande Øresund/Storebælt/Fehmarn-landbruggen, VK→continent via de Kanaaltunnel).
  Dit is — na koper en nikkel — de derde grondstof die niets aan `_chokepoints.js` toevoegt.
- **Recycling = optionele toggle-laag** (`layer:"recycle"`, default uit) → **hergebruikt het REE-patroon met
  0 engine-wijziging** (de chip verschijnt automatisch via `hasRecycle()`, gate op node.layer + flow.layer).
  Autokat-recycling is ~25% van het PGM-aanbod en loopt door **dezelfde** westerse raffinaderijen die de
  katalysatoren máken — een echte gesloten kringloop, bewust achter de toggle zoals REE's magneetschroot.
  *(Kanttekening: de gedeelde recycling-chip-tooltip is nog REE-bewoord ("<5% van het aanbod") — apart issue.)*
- **Beursvoorraden/exchange-laag bewust UITGESTELD** (backlog): Pt/Pd zijn wél beursverhandeld (NYMEX/TOCOM-
  futures + Zürich/Londen-kluizen via de LPPM), maar die tweede optionele laag raakt de gedeelde engine-
  bestanden → zoals uranium's militaire-toggle (LAR-414) en olie's SPR-toggle (LAR-432) alleen de data-laag nu.

## De keten & stages (→ `stage`-codes + kleur/booghoogte)
| stap | `stage`-code | kleur op de kaart | booghoogte | eenheid |
|---|---|---|---|---|
| 1. Winning → PGM-erts / concentraat / matte (mijn → smelter/raffinaderij) | `erts` | donker/gedempt platina-grijs | laag | t 3E |
| 2. Raffinage → geraffineerd Pt/Pd/Rh (sponge, ingot, zouten) dat de lucht in gaat | `raffinaat` | volle platina-kleur | midden | t 3E |
| 3. Eindproduct → autokatalysator / brandstofcel / sieraad / industrie | `product` | licht, bijna wit | hoog | t 3E |

*Alle volumes indicatief in **t 3E/jaar** (Pt+Pd+Rh gecombineerd, "3E"), zodat de hele keten optelbaar blijft.
Wereldmijnproductie ≈ 400 t 3E/jaar (Pt ~180 t, Pd ~210 t, Rh ~24 t) + ~90 t gerecycled.*

## De lagen (nodes) — skelet

### 1. Mijnbouw (Zuid-Afrika-dominant Pt/Rh + Rusland Pd + Great Dyke + Noord-Amerika)
- **Zuid-Afrika (~60% van 3E, het Bushveld-complex):** de Westelijke rand bij Rustenburg (**Mogalakwena**
  (Amplats, Noordelijke rand, grootste open-pit, Pt/Pd), **Impala Rustenburg** (Implats), **Sibanye Rustenburg**
  + **Marikana** (Sibanye, ex-Lonmin), **Amandelbult** (Amplats), **Bafokeng/Styldrift** (RBPlat→Implats),
  **Northam Zondereinde**) en de Oostelijke rand (**Two Rivers** e.a., Implats/ARM/Amplats). Diepe, arbeids-
  intensieve schacht­mijnen; kwetsbaar voor de Eskom-stroomcrisis.
- **Rusland (~25% van 3E, Pd-dominant):** **Norilsk** (Nornickel) — palladium en platina als bijproduct van
  het Ni-Cu-sulfide-erts boven de poolcirkel. ~40% van het wereld-palladium.
- **Zimbabwe (~8%):** de **Great Dyke** — **Zimplats** (Implats), **Mimosa** (Sibanye/Implats-JV), **Unki**
  (Amplats). Smelt tot matte en stuurt die (nog) naar Zuid-Afrika voor eindraffinage; Zimbabwe bouwt eigen
  smeltcapaciteit onder druk van een dreigend ruw-matte-exportverbod.
- **Noord-Amerika (~5%):** **Stillwater** (Sibanye-Stillwater, Montana — het enige Amerikaanse PGM-erts,
  Pd/Pt), **Lac des Îles** (Impala Canada, Ontario, Pd), **Sudbury** (Vale/Glencore, PGM bij Ni-Cu).
- **Finland (~1%):** **Kevitsa** (Boliden) — PGM als bijproduct van nikkel/koper.

### 2. Smelting / raffinage
- **Zuid-Afrika (de trechter):** **Rustenburg PMR** (Anglo American Platinum Precious Metals Refinery — de
  grootste PGM-raffinaderij ter wereld) en de **Impala-raffinaderij bij Springs** (bij Johannesburg). Hier
  komt ook de Zimbabwaanse matte binnen.
- **Rusland:** **Krastsvetmet (Krasnoyarsk)** raffineert de Norilsk-PGM tot geregistreerd Pt/Pd/Rh.
- **Noord-Amerika:** **Sibanye-Stillwater Metallurgical Complex (Columbus, Montana)** — raffineert het
  Stillwater-erts én recyclet Amerikaanse autokatalysatoren.
- **De westerse edelmetaalhuizen (raffinage + katalysator-fabricage + recycling ineen):** **Johnson Matthey**
  (Royston, VK), **BASF** (Duitsland), **Umicore** (Hoboken, België), **Heraeus** (Hanau, Duitsland),
  **Tanaka** (Japan). Zij ontvangen geraffineerd metaal, coaten er katalysatoren mee, en winnen het metaal
  terug uit gebruikte katalysatoren (de recycling-kringloop).

### 3. Gateway (luchthaven)
- **OR Tambo (Johannesburg, JNB)** — de uitgaande trechter: vrijwel al het Zuid-Afrikaanse geraffineerde
  metaal vliegt hierlangs de wereld in. (Enige airport-node; overige luchtlegs gaan rechtstreeks great-circle.)

### 4. Consumptie (autokatalysator dominant + waterstof/sieraad/industrie)
- **Autokatalysator:** China (grootste automarkt), EU (Duitsland), Noord-Amerika (Detroit), Japan (Toyota/
  Nagoya), India (groeiend, BS6-norm). Het gros van Pd/Rh + ~40% van Pt.
- **Waterstof (de groeicurve):** Pt in PEM-elektrolysers (groene H₂) en brandstofcellen (FCEV); iridium (óók
  een PGM) is kritiek voor de elektrolyser-anode. De hedge tegen de EV-gedreven daling van de autokat-vraag.
- **Sieraad:** platina-sieraden (China/India/Japan). **Industrie:** glas, chemie, elektronica, petroraffinage.

### 5. Recycling (optionele toggle-laag — `layer:"recycle"`)
- Gebruikte autokatalysatoren (Europa/VS/Japan/China) → terug naar de westerse raffinaderijen (Umicore/JM/
  BASF/Heraeus/Columbus) → opnieuw geraffineerd metaal. ~25% van het aanbod; achter de toggle zoals REE.

## Kern-stromen (illustratief)
- **Intra-Zuid-Afrika** (`erts`, road/rail): Bushveld-mijnen → Rustenburg PMR / Springs. De dichte kluwen.
- **Zimbabwe → Zuid-Afrika** (`erts`, road via Beitbridge): matte → Springs voor eindraffinage.
- **Norilsk → Krasnoyarsk** (`erts`, rail): Russische Pd/Pt naar de eigen raffinage.
- **Zuid-Afrika → wereld** (`raffinaat`, air via JNB): geraffineerd metaal naar JM/BASF/Umicore/Heraeus/Tanaka
  + rechtstreeks naar de Chinese katalysator-/sieraadmarkt.
- **Rusland → wereld** (`raffinaat`, air): Pd naar Europese fabrikanten en — sinds 2022 verschuivend — China.
- **Fabrikant → automarkt** (`product`, road/rail; VK→continent via de Kanaaltunnel): gecoate katalysatoren.
- **Waterstof** (`product`): Pt → PEM-elektrolysers/brandstofcellen (EU/Azië) — de nieuwe vraagbron.
- **Recycling** (`layer:"recycle"`): gebruikte autokats → westerse raffinaderijen → terug de keten in.

## Emergent plaatje (wat je zou moeten zien als het klopt)
1. Een **extreem dichte kluwen** in Zuid-Afrika (het Bushveld bij Rustenburg + de Oostrand) — bijna alle
   platina/rodium uit één formatie — plus **één zware punt op Norilsk** voor het palladium. Twee bronnen.
2. Vanuit beide een **waaier van luchtbogen** (hoge, opgetilde arcs — géén zeeroutes) naar een handvol
   westerse edelmetaalhuizen + de Aziatische markten.
3. Een **westerse midstream-ring** (VK/België/Duitsland/Japan/Montana) die zowel máákt als recyclet — zet de
   recycling-toggle aan en er komen retourbogen bij van de automarkten terug naar diezelfde huizen.
4. Een **dun, groeiend waterstof-draadje** naast de dikke autokat-bundel = de vraag-hedge.

## Knelpunten & vaarpunten (allemaal bestaand / n.v.t.)
- **Nieuw knelpunt: geen. Nieuw vaarpunt: geen.** Luchtvracht negeert de zeestraten; de landhops gebruiken
  bestaande landbruggen (Beitbridge-land, Øresund/Storebælt/Fehmarn voor Finland, Kanaaltunnel voor het VK).
- De "knijp" van PGM is niet geografisch (een zeestraat) maar **structureel**: twee landen, twee metalen, de
  autokat-leiband en de Zuid-Afrikaanse stroomcrisis — gedragen door `tensions`, niet door een `wp-`.

## Tensions (6)
1. **Twee landen, twee metalen** (concentratie) — Bushveld (Pt/Rh) + Norilsk (Pd).
2. **De autokatalysator-leiband + Pt↔Pd-substitutie** (structureel) — emissienorm stuurt de vraag.
3. **Rodium: minuscuul volume, extreme prijs, één land** (spof) — ~80% uit Zuid-Afrika, piek ~$29k/oz (2021).
4. **Palladium & Rusland: Norilsk + sanctierisico** (beleid) — ~40% Pd uit één sanctiegevoelig land.
5. **De waterstof-ommekeer** (structureel) — Pt/Ir voor elektrolyse & brandstofcellen = de vraag-hedge.
6. **Zuid-Afrika: stroomcrisis knijpt de smelters** (beleid) — Eskom-load-shedding + diepe, dure schachten.

## Research-TODO (vóór `data/pgm.js`) — ✅ inline verwerkt
- [x] Mijn-shares 2024 (USGS MCS 2025): ZA ~60% 3E (Pt/Rh-dominant), Rusland ~25% (Pd), Zimbabwe ~8%, NA ~5%.
- [x] Pt/Pd/Rh-splitsing per land (ZA = Pt+Rh; Rusland = Pd) — dit stuurt de tensions/notes.
- [x] Raffinage-topologie: Rustenburg PMR + Impala Springs + Krasnoyarsk + Columbus + de westerse huizen.
- [x] Eindgebruik-aandelen (autokat dominant, waterstof-groei, sieraad/industrie) + de substitutie-dynamiek.
- [x] Recycling ~25% via dezelfde westerse raffinaderijen (achter de toggle).

## Bronnen
USGS Mineral Commodity Summaries 2025 (platinum-group metals, peiljaar 2024) · Johnson Matthey *PGM Market
Report* · World Platinum Investment Council (WPIC) · bedrijfsrapportages (Anglo American Platinum, Impala
Platinum, Sibanye-Stillwater, Northam, Nornickel, Zimplats, Umicore, BASF, Heraeus, Tanaka).
