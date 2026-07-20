# Gabarit-veld per edge — besluiten + presettabel (LAR-514)

*Vastgelegd 2026-07-20. **Nog niets gebouwd** — dit is de voorbereiding zodat de bouwsessie
meteen kan beginnen. Status per onderdeel staat onderaan.*

Waarom dit issue bestaat staat in [LAR-514] zelf; deze notitie legt alleen vast wat er ná dat
issue is besloten en welke bron de getallen levert.

---

## 1 · De drie besluiten van Lars (2026-07-20)

Het issue liet drie vragen expliciet open. Alle drie zijn beslist:

| Vraag | Besluit | Waarom |
| -- | -- | -- |
| **Welke vorm** — A klasse-enum · B tonnage · **C vier maten** | **C: vier maten per edge** (diepgang · breedte · lengte · doorvaarthoogte) | Alleen vier maten vangen álle vijf regimes. Erie faalt op **hoogte** (4,7 m), Seaway op **lengte/breedte**, Poe Lock op **lengte** (366 m), Cape Cod op **konvooivorm** — géén daarvan is een CEMT-klasse of een tonnage. CEMT blijft bestaan als **afgeleid label** voor de HUD. |
| **Per edge of per label** | **Per edge, geërfd van het systeem** | De Seaway-beperking zit in enkele sluis-edges van een systeem van 306 km; per label kan dat niet. Bovendien kunnen edges *zonder* label (de 16 graad-1-stubs uit [LAR-507]) niets erven. Kosten ~4-8 byte/edge = ~120-250 KB op ~30.600 edges, verwaarloosbaar naast 2,15 MB. |
| **Zee-edges** (~15.933, incl. Panama/Suez/Kiel) | **Apart issue** | Eerst het mechanisme bewijzen op binnenwater, waar de regimes elkaar aantoonbaar tegenspreken (Freycinet 350 t naast CEMT VIb). Panama/Suez/Kiel zijn echte gabarit-poorten en verdienen hun eigen ronde. |

**Het draagprincipe blijft ongewijzigd:** *bekende maat = harde grens, onbekende maat = géén grens.*
Een lege maat betekent "onbekend" en moet als "past" gelden — anders sluit een ontbrekende tag
stilzwijgend een route af en is het effect onvindbaar.

---

## 2 · De presettabel — CEMT 1992 → vier maten

**Bron:** ECMT Resolution No. 92/2 (12 juni 1992), *New Classification of Inland Waterways* —
de officiële tabel, [PDF bij ITF/OECD](https://www.itf-oecd.org/sites/default/files/docs/wat19922e.pdf),
overzicht via [Classification of European Inland Waterways](https://en.wikipedia.org/wiki/Classification_of_European_Inland_Waterways).
Dit is een gepubliceerde standaardtabel, geen schatting.

**Leesregel:** een vaarweg van klasse X laat schepen tót deze maten toe, dus we nemen de
**bovenkant** van elk lengtebereik. Dat is ook wat [LAR-514] zelf al voorstelt (Va = 110 × 11,4 ·
Vb = 185 × 11,4 · VIb = 185/195 × 22,8).

| Klasse | Lengte (m) | Breedte (m) | Diepgang (m) | Scheepstype |
| -- | -- | -- | -- | -- |
| I | 38,5 | 5,05 | 2,20 | péniche / Freycinet (250-400 t) |
| II | 55,0 | 6,6 | 2,50 | Kempenaar (400-650 t) |
| III | 80,0 | 8,2 | 2,50 | Gustav Koenigs (650-1.000 t) |
| IV | 85,0 | 9,5 | 2,80 | Johann Welker (1.000-1.500 t) |
| Va | 110 | 11,4 | 4,50 | groot Rijnschip (1.600-3.000 t) |
| Vb | 185 | 11,4 | 4,50 | duwstel 1×2 (3.200-6.000 t) |
| VIa | 110 | 22,8 | 4,50 | duwstel 2×1 |
| VIb | 195 | 22,8 | 4,50 | duwstel 2×2 (6.400-12.000 t) |
| VIc | 280 | 22,8 | 4,00 | duwstel 2×3 (9.600-18.000 t) · variant 3×2 = 200 × 34,2 |
| VII | 285 | 34,2 | 4,50 | duwstel 3×3 (14.500-27.000 t) |

### ⚠️ Alleen de LENGTE- en BREEDTE-kolom worden gebruikt

Bij de bouw (2026-07-20) bleek dat **twee** van de vier kolommen niet als grens van de klasse
gelezen mogen worden. Dezelfde reden, twee keer: de klasse *bepaalt* ze niet.

**Doorvaarthoogte** — de CEMT-tabel geeft **alternatieven** ("5,25 of 7,00 of 9,10 m") waaruit
de waterwegbeheerder er één kiest. Dat stond al in deze notitie en is bevestigd.

**Diepgang** — dit is de vondst van de bouwsessie, en hij was niet voorzien. De diepgangkolom
beschrijft het **referentieschip** van de klasse, niet de vaarweg. Het bewijs is objectief en
hoeft niet beredeneerd te worden:

| kolom | reeks I → VII | monotoon? |
| -- | -- | -- |
| lengte | 38,5 · 55 · 80 · 85 · 110 · 185 · 195 · 280 · 285 | ✅ stijgend |
| breedte | 5,05 · 6,6 · 8,2 · 9,5 · 11,4 · 11,4 · 22,8 · 22,8 · 34,2 | ✅ stijgend |
| **diepgang** | 2,2 · 2,5 · 2,5 · 2,8 · 4,5 · 4,5 · 4,5 · **4,0** · 4,5 | ❌ **VIb 4,50 → VIc 4,00** |

Een grootheid die **daalt** terwijl de klasse **stijgt** kan onmogelijk "de grens van die klasse"
zijn — een VIc-duwstel (2×3, breed en lang) is gewoon ondieper geladen dan een VIb.

**Dit was geen theoretisch punt.** Met diepgang in de presets sloot `waal` (VIc → 4,00 m) voor
een klasse Va-schip (4,50 m): de drukste binnenvaartweg van Europa dicht voor een gewoon
Rijnschip, waardoor **R'dam→Nijmegen van 172 km naar 9.405 km sprong** (de router ging om via
zee). Het is dezelfde foutsoort die dit project al kent als *"vaargeul-projectdiepte is niet de
maximale scheepsdiepgang"*, nu in de vorm **"referentieschip is niet de vaarweg"**.

→ **`CEMT_PRESETS` vult alleen `lengte` en `breedte`.** Diepgang en doorvaarthoogte komen
uitsluitend uit een echte meting (§4). Dat volgt rechtstreeks uit het draagprincipe: liever
onbekend dan verzonnen.

---

## 3 · De 22 systemen mét CEMT (presets direct toepasbaar)

`noordzeekanaal` VIb · `waal` VIc · `rijn` VIb · `rijn-boven` VIb · `mosel` Vb · `schelde` VIb ·
`schelde-rijnkanaal` VIb · `seine` VII · `seine-boven` Vb · `rhone` VIb · `rhone-boven` VIb ·
`main` Vb · `main-donau-kanaal` Vb · `donau-zeekanaal` VIb · `donau` VII · `donau-boven` VIb ·
`maas` Vb · `maas-boven` Va · `albertkanaal` VIb · `amsterdam-rijnkanaal` VIb · `wolga` VIc ·
`wolga-don` Va

Deze hebben **geen nieuw onderzoek** nodig — de klasse staat al in `fetch_waterways.py:SYSTEMEN`
en reist al door de hele pijplijn naar `meta.vaarwegen`; hij wordt alleen nog nergens gelezen.

## 4 · ⚠️ OPEN: de 14 systemen zónder CEMT

`mississippi` · `mississippi-boven` · `mississippi-upper` · `illinois` · `chicago-kanaal` ·
`ohio` · `yangtze` · `yangtze-boven` · `yangtze-chongqing` · `grand-canal-zuid` · `parelrivier` ·
`xijiang` · `yangon` · `amazone`

**Nog niet onderzocht.** Een onderzoeksronde hiervoor is op 2026-07-20 gestart maar strandde op
een API-sessielimiet, dus er zijn géén resultaten. Verzin deze maten niet — bronnen die het
project al kent:

* **VS (6 systemen)** — `v2/tools/toets_usace.py` bestaat al en levert USACE-gegevens
  (`GEO_CLASS`/`FUNC_CLASS`); `FUNC_CLASS='B'` bevestigde eerder zelfstandig de zeevaartgrens op
  river mile 237. Nodig: project-diepgang per traject + de standaard sluiskolk-maat.
* **China (5 systemen)** — nationale klasse I-VII, **mét de −1-correctie uit §2.3 van
  `binnenwater-scope.md`**: China klasse IV (500 t) = CEMT **III**, niet IV. Zonder die correctie
  lijkt ±25% van de Chinese systemen aan spelregel 1 te voldoen terwijl dat feitelijk niet zo is.
* **`amazone`** — geen klasse, wél de gemeten klaring uit `middellijn_uit_vlakken.py`
  (≥150 m klaring = commercieel bevaarbaar; min 0,44 / mediaan 1,60 / max 7,61 km).
* **`yangon`** — nog geen bron bekend.

Zolang een maat ontbreekt geldt hij als **onbekend = geen grens**. Dat is veilig (het veld sluit
dan niets af) maar acceptatiepunt 4 van [LAR-514] vraagt om een gemotiveerde maat mét bron, dus
dit blijft open werk.

---

## 5 · Waar de wijziging landt (opgezocht, niet geraden)

| Wat | Plek |
| -- | -- |
| bin-schrijver, per edge `a, b, lengte, soort, aantalPunten` | `v2/tools/bake_marnet.py:1229-1237` |
| formaatbeschrijving (commentaar) | `v2/tools/bake_marnet.py:1216-1221` |
| meta per label naar `marnet.json` | `v2/tools/bake_marnet.py:795-807` |
| `cemt` per systeem | `v2/tools/fetch_waterways.py:134+` (`SYSTEMEN`) |
| bin-lezer, blok 2 | `v2/src/marnet.js:105-122` |
| formaatbeschrijving (commentaar) | `v2/src/marnet.js:11-16` |
| `vaarwegen` naar de browser | `v2/src/marnet.js:212` |
| router, edge-filter vóór de relaxatie | `v2/src/marnet.js:463` (in `zoekRoute`) |
| twee trappen die `schip` moeten doorgeven | `v2/src/marnet.js:381-395` (`zoekRouteRealistisch`) |
| HUD-knop naast "realistisch / alles toestaan" | `v2/index.html:75-78` + `v2/src/main.js:213-220` |

De router krijgt `opties.schip = { diepgang, breedte, lengte, hoogte }`; een edge valt dicht
zodra één van de vier maten niet past — **zelfde plek en zelfde soort filter als `vermijd` nu**,
dus de grootcirkel-heuristiek blijft toelaatbaar. **Zonder `schip` gaat geen enkele edge dicht**,
en dat is meteen acceptatiepunt 2.

---

## 6 · Het formaat zoals gebouwd

Per edge in `marnet.bin`, ná `soort` en `aantalPunten`:

```
gabarietvlag   0 = geen maten (1 byte)  ·  1 = er volgen er vier
  diepgang     decimeter, 0 = onbekend
  breedte      decimeter, 0 = onbekend
  lengte       decimeter, 0 = onbekend
  hoogte       decimeter, 0 = onbekend
```

De vlag scheelt drie bytes op elke ongemeten edge (~15.900 zee-edges) en maakt het formaat
zelfbeschrijvend: *geen maten* is iets anders dan *vier nullen*, ook al gedragen ze zich hetzelfde.
Gemeten kosten: `marnet.bin` 1.249.034 → 1.269.532 byte (**+20 KB, +1,6%**).

De router leest ze in `zoekRoute` via `opties.schip = {diepgang, breedte, lengte, hoogte}`; een
edge valt weg **vóór** de relaxatie, op exact dezelfde plek en van dezelfde soort als `vermijd`.
Daardoor blijft de grootcirkel-heuristiek toelaatbaar en is het gevonden pad nog steeds precies
het kortste over wat overblijft.

⚠️ **De tabel staat in `bake_marnet.py`, niet in `fetch_waterways.py`.** `cemt` hoort daar wél
thuis — de fetcher selecteert er OSM-ways mee. De vier maten hebben géén fetcher-rol: ze komen
niet uit OSM maar uit gepubliceerde sluis-, brug- en vaargeulgegevens. Dat scheelt een volledige
re-fetch bij elke correctie van een brughoogte.

## 7 · Status

- [x] Vorm besloten (C: vier maten)
- [x] Granulariteit besloten (per edge, geërfd)
- [x] Zee-edges afgebakend (apart issue)
- [x] CEMT-presettabel gesourcet en geverifieerd (ECMT 92/2)
- [x] Code-locaties opgezocht
- [x] Doorvaarthoogte bevestigd als "niet uit de klasse" — **en diepgang idem** (§2)
- [x] Schrijver · lezer · router · HUD gebouwd (commit `23d993e`)
- [x] Bake: knopen 10.773 / edges 17.024 ongewijzigd, `ports.json` byte-identiek
- [x] Elf regressieroutes exact zónder schip (acceptatiepunt 2, knoop→knoop gemeten)
- [x] Klein-vs-groot bewezen: R'dam→Luik **375 km voor Vb, DICHT voor VIb** — `maas` is
      11,4 m breed, een 2×2-duwstel 22,8 m (acceptatiepunt 3)
- [x] Zeeroutes onaangetast bij elke klasse (R'dam→Shanghai 19.610), zee-edges dragen geen maten
- [ ] Maten voor de 14 niet-CEMT-systemen (§4) — **onderzoek loopt**; tot dan staan ze op
      onbekend en sluiten ze dus niets af
- [ ] Visuele go van Lars

### Gemeten: welke systemen sluiten per scheepsklasse

Netjes oplopend, wat het nesten van de klassen bevestigt:

| klasse | dicht | systemen |
| -- | -- | -- |
| IV | 0 | — |
| Va | 0 | — |
| Vb | 2 | `maas-boven` · `wolga-don` |
| VIb | 7 | + `mosel` `seine-boven` `main` `main-donau-kanaal` `maas` |
| VII | 20 | + vrijwel de hele Europese as (alleen `waal` VIc en `donau`/`seine` VII blijven) |
