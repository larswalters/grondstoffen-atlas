# Ontwerpbrief · LOD-systeem (level of detail) — M26

*Vastgelegd 2026-07-19 na ontwerpgesprek met Lars. Status: **richting, geen eindbesluit** — de
definitieve visuele go valt op de bol zelf, bij de koper-pilot (go/no-go-moment, M22-precedent).*

## Waarom

De tegels hebben al LOD (z-levels tot z19); al het andere niet. Inzoomen moet **nieuwe informatie**
opleveren in plaats van grotere pixels: een hotspot valt uiteen in z'n onderdelen, flows
her-bundelen mee. Dit is de kern van wat M26 tot een echte atlas maakt — en daarmee is M26
definitief **herontwerp van het datamodel**, geen verhuizing van de v1-bestanden.

## Referentiebeelden

Drie concept-mockups in `referenties/` (ook als bijlage op het Linear-issue):

1. **`lod-referentie-1-zoomniveaus.png`** ⭐ — **de primaire stijlreferentie** (Lars: de gloeiende
   plekken met de bollen + de verbindingen). Toont de 4 zoomniveaus wereld → continent → regionaal
   → lokaal, night-side esthetiek, stadslicht-aderen, glow-bollen op nodes, dunne elegante lijnen.
2. `lod-referentie-2-hotspots.png` — hotspot-hiërarchie (groot = cluster van mijnen/fabrieken/
   havens · medium = regionaal industriegebied · klein = individuele faciliteit) + "dikte en
   helderheid = volume en activiteit".
3. `lod-referentie-3-drilldown-koper.png` — de koper-drill-down: wereld → Zuid-Amerika → Copper
   Belt (Chili) → mijncluster → ultra-lokaal de individuele mijn. Let op: de hoogte-pilaren uit
   dit beeld zijn **vervallen** (zie besluiten).

**Doelbeeld = combinatie van deze referenties en de v1-look** (Lars vindt v1 visueel al erg
sterk); niet één-op-één de mockups nabouwen.

## De visuele taal

| encoding | betekent |
|---|---|
| kleur | grondstof (koper oranje, lithium paars, ijzererts blauw, nikkel groen, …) |
| gloed/intensiteit bol | activiteit & volume van de node |
| grootte bol | capaciteit/belang (i.p.v. hoogte-pilaren) |
| dikte flow | volume (in **meters**, zie lijndikte-strategie) |
| lijnstijl | modaliteit (zee / binnenvaart / spoor / weg / pijpleiding) |

## Glow-gedrag per zoomniveau (Lars, 2026-07-19)

Het glow-systeem past zich aan het zoomniveau aan — geen harde omschakeling maar een vloeiend
verloop:

- **🌍 Wereldniveau:** geen losse fabrieken, maar **één grote zachte gloed boven een regio** —
  de Ruhr, de Copperbelt, Pilbara of de Yangtze-delta lijken echt "op te lichten". Dus niet
  vier losse bollen naast elkaar, maar één mooie diffuse gloed over het hele industriegebied.
- **🌎 Continentniveau:** de grote gloed **splitst zich langzaam op**; meerdere industriële
  hotspots worden onderscheidbaar.
- **🏭 Lokale zoom:** de regionale glow verdwijnt; **iedere fabriek krijgt een kleine, subtiele
  eigen glow** — eventueel met een **pulserend effect** als de faciliteit actief is in de
  geselecteerde grondstof.

**Kernprincipe: de glow telt op** (additief). Twintig fabrieken dicht bij elkaar geven
automatisch één grote heldere hotspot — een heatmap, maar dan in 3D.

**Technische consequentie (belangrijk voor de bouw):** doordat de glow optelt, hoeft de
wereld-hotspot **geen apart getekend object** te zijn — hij *ontstaat vanzelf* uit de
individuele site-glows zodra de glow-radius meeschaalt met de kijkafstand. Dat betekent:

- de overgang wereld ↔ continent ↔ lokaal is **continu** (geen pop-in of crossfade-trucs nodig
  voor de glow zelf);
- het hiërarchische nodemodel (`level`/`parent`) blijft nodig voor **labels, interactie en
  flow-aggregatie**, maar niet voor de glow — die is emergent;
- de glow-radius/-intensiteit per site schaalt met camerahoogte (dichtbij klein en scherp,
  veraf breed en diffuus zodat buren overlappen tot één hotspot), capaciteit bepaalt het gewicht
  in de optelling.

## Besluiten (2026-07-19)

1. **Semantische zoom in ~4–5 niveaus**, banden op `getAltitude()` (richtwaarden, in de pilot
   kalibreren): >20.000 km wereld · 3.000–20.000 continent · 300–3.000 regionaal · <300 lokaal ·
   <~10 km ultra-lokaal (= de Esri-tegels zelf + onze markers/labels).
2. **Hiërarchisch nodemodel:** elke node krijgt `level` + `parent`. Data op het fijnste niveau
   dat we hebben; grovere niveaus (hotspots) worden **build-time geaggregeerd** — zelfde patroon
   als `bake_world.py`/`bake_marnet.py`. Flows aggregeren mee met de nodes: wereldniveau één band
   Chili→Shanghai, regionaal splitst die naar de afzonderlijke sites. Bundeling is gratis dankzij
   M23 (routes delen letterlijk edges).
3. **Glow-bollen, géén hoogte-pilaren.** Gelaagde glow (felle kern + zachte halo in
   grondstofkleur), additief geblend zodat overlappende clusters vanzelf een hotspot vormen.
   **Selective bloom** (alleen de glow-laag bloomt, niet de tegels — anders wast het beeld uit).
   Bollen zijn goedkoper dan pilaren en werken op elke kijkhoek.
4. **Lijndikte hybride:** dikte in **meters, geschaald op volume**, met een **minimum in pixels**
   als ondergrens. Dichtbij een fysiek lint op het landschap, van veraf klemt hij op leesbare
   minimale dikte — grote stromen blijven dus zichtbaar op wereldniveau. Bouwconsequentie:
   Three's standaardlijnen zijn altijd 1 px → **ribbon/`Line2`-geometrie met glow-shader**, van
   meet af aan.
5. **Data-ambitie = optie C, koper-pilot eerst.** Koper krijgt de volledige site-hiërarchie
   (top-±15–30 échte benoemde sites: Escondida, Collahuasi, Chuquicamata, smelters, terminals —
   coördinaten op ~100 m nauwkeurig zodat de marker op z17 óp de site ligt, + capaciteitscijfer
   voor de glow). De andere 13 grondstoffen blijven op de huidige abstracte nodes en worden
   daarna **één voor één** verdiept — het bewezen M5–M17-patroon.
6. **Night-side/gedimde modus:** voorkeur = stromen-laag aan → satelliet gedimd + stadslichten
   (Black Marble-stijl; stond al op de M22-restlijst als "dag/nacht-terminator met stadslichten").
   Glow op fel daglicht verliest altijd. **Te bevestigen met visuele check in de pilot** — geen
   default vastleggen vóór Lars het op de bol gezien heeft.

## Volgorde & afhankelijkheden

**M24 (binnenwater, bezig) → M25 (weg/spoor/pijpleiding) → dit (M26).** M25 is een hárde
afhankelijkheid, geen nice-to-have: op regionaal/lokaal niveau zijn de verbindingen bijna
allemaal land-transport (mijn → smelter → haven = spoor + weg). Zonder M25 heeft de lokale view
zwevende lijnen. Ultra-lokaal wordt de OSM-weg/spoorlijn zelf de flow-drager.

## Technische aandachtspunten van dichtbij

- **Tegelgrenzen zijn géén probleem** — flows zijn eigen 3D-geometrie in wereldcoördinaten boven
  het oppervlak; ze merken niets van de tegels eronder.
- **Wél: hoogte boven de tegel-schil.** De tegels liggen boven de bol (sphere sink, M22-bug 4).
  Lijnen en markers moeten boven de *tegels* liggen, niet boven de bol — anders prikken tegels
  erdoorheen.
- **Geometrie-LOD:** routes zijn op ~2 km gesampled → hoeken op <5 km hoogte. Dichtbij fijnere
  geometrie of smoothing.
- **Positionele juistheid is de echte lat:** op z17 zie je de kade liggen; de route moet het
  juiste havenbekken in, niet 800 m over de containers. MARNET is km-nauwkeurig; de
  meter-nauwkeurigheid komt uit M24/M25 (OSM-geometrie).
- **Ultra-lokaal is goedkoop:** de open-pit mijn ís gewoon Esri z17–19 (hebben we al, tot ~1 km
  hoogte). Wij leveren alleen precieze coördinaten + marker/outline/label erbovenop.

## Open punten (beslissen in/na de pilot)

- Visuele go op de totale look (combinatie referenties + v1) — **go/no-go bij de koper-pilot**.
- Night-side als default bij stromen-laag aan: testen met visuele check.
- Exacte zoom-banden en overgangen (crossfade hotspot ↔ kinderen).
- Of de M22-schoonheidsslag (Rayleigh/Mie, oceaan-specular, terminator + stadslichten) vóór of
  samen met de pilot gebouwd wordt — stadslichten horen in elk geval bij deze look.

## Gerelateerd

- Linear: issue onder **M26 · Samenvoegen** (dit document is de spec; het issue verwijst hierheen).
- Vault: [[2026-07-18-grondstoffen-atlas-fundament-plan-m22-m26]] (het plan waar dit op voortbouwt,
  incl. de correctie dat M26 herontwerp is i.p.v. verhuizing).
