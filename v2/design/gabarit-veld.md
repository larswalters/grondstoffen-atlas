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

## 4 · De 14 systemen zónder CEMT — onderzocht 2026-07-20

Onderzocht met 14 parallelle onderzoekers, elk aangevallen door **twee** onafhankelijke skeptici:
een algemene weerlegger en een *poort-jager* die specifiek zocht naar gemiste, strengere poorten
(bruggen, kleine sluiskolken, drempels, kabels). 43 agents, nul fouten, ~2,5 miljoen tokens.

### ⚠️ De scheidslijn die het onderzoek zelf als belangrijkste bevinding aanwees

Niet elke gevonden maat mag de graaf in. De onderzoekers labelden elke waarde met een `soort_maat`,
en dat label blijkt **beslissend**:

| soort | in de graaf? | waarom |
| -- | -- | -- |
| gepubliceerde **max scheepsdiepgang / LOA** | ✅ | precies wat het veld bedoelt |
| **sluiskolk-maat** als lengte/breedte | ✅ | een kolk van 600 ft neemt geen schip van 600 ft, maar niets lángers past hoe dan ook — als bovengrens correct, hooguit iets te ruim, en te ruim is de veilige kant |
| **brugklaring** met bekend referentievlak | ✅ | echte fysieke poort |
| **vaargeul-projectdiepte / 维护水深** als diepgang | ❌ | **de val waar dit veld aan kapot zou gaan** |
| alles onder voorbehoud | ❌ | |
| alles op een edge die eerst gesplitst moet worden | ❌ | |

**Waarom projectdiepte nooit als maximum mag.** Een onderhouden geuldiepte is een *garantie*, geen
*maximum*. Op de Mississippi is de projectdiepte 9 ft terwijl de USCG in 2023 nog 10–10,5 ft
toestond: werkelijke schepen steken **dieper** dan het "maximum" dat we zouden invullen. Wie dat
wegschrijft sluit bestaand verkeer af — stil, want je ziet alleen dat een route niet bestaat.
Exact dezelfde foutsoort als de CEMT-diepgangkolom uit §2: *een getal dat de vaarweg beschrijft is
geen getal dat het schip begrenst.*

### Wat er is ingevuld

| systeem | diepgang | breedte | lengte | hoogte | herkomst |
| -- | -- | -- | -- | -- | -- |
| `mississippi` | 13,716 | | | | 45 ft, NOAA Coast Pilot 5 + NOBRA-loodsbulletins |
| `illinois` | | 33,528 | 182,88 | 14,29 | 110×600 ft kolken + I-80 Bridge, USACE Rock Island |
| `chicago-kanaal` | | | 182,88 | | 600 ft kolk, drie onafhankelijke bronnen |
| `ohio` | 2,7432 | 33,528 | 182,88 | | USACE HEC: *"vessels drafting up to nine feet"* |
| `yangtze-chongqing` | | 34,0 | 280,0 | | Drieklovensluis 280×34 m (CTG) |
| `yangon` | 9,6 | | 200,0 | | Myanma Port Authority, *Yangon Ports* (2024) |
| `amazone` | 11,5 | | | | Marinha do Brasil, NPCF Anexo 1-G (Passagem do Tabocal) |

**Zeven systemen blijven bewust leeg**, elk met een reden die in de baker staat:
`mississippi-boven` (alleen projectdiepte) · `mississippi-upper` (56 ft-kolken gelden maar over de
laatste ~10 km van 1.728,7 km → eerst splitsen bij LD 2) · `yangtze` en `yangtze-boven` (node
pinnen) · `grand-canal-zuid` (zwakste dossier; route loopt sinds 2023 via een bypass) ·
`parelrivier` (alles hangt aan het eindpunt) · `xijiang` (eerst splitsen bij Sixianjiao).

### De vier vondsten die CEMT nooit had gevangen

1. **`ohio` 2,7432 m diepgang** — 9 ft is hier écht een scheepsmaat, niet de geul (die is 12 ft).
   Gevolg: de Ohio sluit voor **élke** CEMT-klasse, want zelfs klasse IV steekt 2,80 m. Zes
   centimeter, en fysiek juist: een Europees binnenvaartschip is dieper dan een Ohio-duwbak.
   Cincinnati en Louisville zijn daarmee onbereikbaar voor de hele Europese vloot.
2. **De 600 ft-kolken** (182,88 m) op Illinois/Chicago sluiten een Vb-duwstel van 185 m — twee
   meter te lang. Chicago is bereikbaar t/m klasse Va en dicht vanaf Vb.
3. **Doorvaarthoogte is de maat die geen klasse draagt.** De Nanjing Yangtze River Bridge (1968,
   24 m) is het fysieke mechanisme waardoor zeeschepen niet boven Nanjing komen — precies wat
   [LAR-514] als motivatie noemde. Nog niet ingevuld omdat de waarde aan de node hangt (24 m óf
   18 m), maar de vondst staat.
4. **Kabels en leidingen zijn stelselmatig lager dan bruggen** en werden in drie van de vier
   gevallen vergeten: de Harahan-kabels (Mississippi, 145 ft — láger dan elke brug op dat vak,
   terwijl de bruggen wél waren geïnventariseerd), een hoogspanningsleiding over het 坭洲航道
   (Parelrivier), en de Linhão de Tucuruí over de Amazone. Neem ze standaard mee.

### Openstaand werk dat hieruit volgt

* **Zes edges splitsen of hun node pinnen** vóór hun gabariet zinvol wordt: `mississippi-upper`
  (bij LD 2 Hastings) · `xijiang` (bij Sixianjiao) · `grand-canal-zuid` (aan de 运河二通道-bypass) ·
  `yangtze` (Xinshengwei/Longtan, zuidtak Runyang) · `yangtze-boven` (benedenstrooms van de
  武汉长江大桥) · `parelrivier` (eindpunt op het 西基调头区).
* **Vier verificaties**, in volgorde van waarde: Chicago-breedte (80 ft in 33 CFR 207.420 tegen
  50 ft in de USACE WCM van mei 2024 — die twee liggen aan wéérszijden van CEMT VIb) · Yangon 44 m
  (bevestiging van ná de brugopening 06-02-2026) · staan 旧五斗大桥 en 旧西樵大桥 er nog · de 18 m
  van de 武汉长江大桥.
* **Herbruikbare bron gevonden**: de USACE ArcGIS-host die `toets_usace.py` al aanroept draagt óók
  `Locks` (kolkmaten + drempeldieptes) en `USACE_IENC_Master_Service` laag 92 `BRIDGE_AREA`
  (klaring per structuur) en lagen 43/44 (kabels en leidingen). Zo is de Ohio-hoogte gevonden, met
  97% dekking — veel harder dan gescande kaart-PDF's.
* **Elk hoogtecijfer is waardeloos zonder referentievlak, en het werkt ómgekeerd aan diepgang:**
  voor diepgang is laagwater de harde kant, voor hoogte juist hóógwater.

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
- [x] Maten voor de 14 niet-CEMT-systemen onderzocht (§4) — 7 ingevuld, 7 bewust leeg
- [x] Acceptatiepunt 5 gemeten: van de 16.153 edges zónder maat gaat er **0** dicht
- [ ] Zes edges splitsen / nodes pinnen (§4) — eigen vervolgissue
- [ ] Vier openstaande bronverificaties (§4)
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
