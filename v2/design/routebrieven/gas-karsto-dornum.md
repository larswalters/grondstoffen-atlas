# Routebrief (licht) · gas — Kårstø (Noorwegen) → Dornum (Duitsland)

**stroom-id:** `gas-karsto-dornum` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken
**Keten in één zin:** Noors Noordzeegas (o.a. Åsgard, Sleipner Oost/West, Gullfaks, Statfjord — diffuus
verzameld via Statpipe) wordt bij Kårstø behandeld en gaat via de Europipe II-gasleiding (deels
offshore, Noorwegen → Duitsland) naar de Gasempfangsanlage bij Dornum/Nesse, het Duitse
invoedingspunt voor het NW-Europese gasnet (NETRA-kop) — Europa's #2-ná-Rusland-gasleverancier.
**Welke as van het verhaal:** Europipe II — 24 bcm/jaar ontwerpcapaciteit [1], Noorwegen als
structurele vervanger van Russisch pijpgas sinds 2022.

## 1 · Ketenkaart
```
Kårstø-gasbehandelingsanlegg `gas-karsto-plant` (fase A vervalt — diffuus Statpipe-verzamelnet,
   zoals bij de Amerikaanse schaliegasvelden)
   ──(b1 leiding · Europipe II: 13 km onshore NO (Kårstø→Vestre Bokn) → ~642 km offshore
       (NO/DK/DE-sector Noordzee) → 15 km onshore DE · ~670 km)──►
Gasempfangsanlage Dornum/Nesse `gas-dornum-netra` — stoppunt, invoedingspunt Duits/NW-Europees net
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-karsto-plant` → `gas-dornum-netra` | Europipe II (Gassco/Equinor; 13 km onshore NO Kårstø→Vestre Bokn + ~642 km offshore NO/DK/DE-sector + 15 km onshore DE) | ~670 [1] (13+642+15; DE Wikipedia noemt ruw "ongeveer 660 km" [2]) | OSM-pipeline — bak-agent stikt de OSM-ways `man_made=pipeline` naam=Europipe II aaneen; offshore-continuïteit niet geverifieerd deze sessie, zie §7 | nee op naam/tag-niveau bevestigd aan beide kanten; het offshore-middenstuk wordt stippel als de bake geen doorlopende way vindt |

Fase A vervalt: diffuus Statpipe-verzamelnet vanaf meerdere Noordzeevelden (Åsgard, Sleipner Oost/West,
Gullfaks, Statfjord), niet als los been getekend (23 ways/597 nodes bevestigd in OSM, ontwerp-toets).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-karsto-plant` | gasbehandelingsanlegg (kop) | Kårstø-gasbehandelingsanlegg (Equinor/Gassco), Tysvær | 59.2774, 5.5247 | [1][3][4] | bron-gelegd (z15 gezien: groot industrieel complex met tankenpark, procesinstallaties en een eigen kade/jetty aan de Boknafjord, tanker afgemeerd) |
| `gas-dornum-netra` | overslag leiding → net (staart, stoppunt) | Gasempfangsanlage/Heizhaus Europipe (Open Grid Europe/Gasunie Deutschland), tussen Dornum en Nesse | 53.6564, 7.4039 | [2][5][6] | bron-gelegd (z15 gezien: omheind industrieterrein met gebouwen en leidingwerk, los van de bebouwde kom van Dornum — komt overeen met de Wikipedia-coördinaat 53°39'23"N 7°24'14"O) |

## 4 · Via-punten
Niet van toepassing: het enige been is een leidingbeen waarvan de geometrie uit aaneengestikte
OSM-pijpleiding-ways ontstaat (geen corridorkeuze door ons te leggen, zoals bij weg/spoor).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kårstø-gasbehandelingsanlegg | Equinor (operator) / Gassled (eigenaar leidingen) | Noordzeegas (Statpipe/Åsgard Transport) → drooggas + NGL/condensaat | droge-gasexport via Europipe II (24 bcm/j) en via Statpipe/Norpipe naar Emden; grootste NGL-exportpoort van Europa | [1][3] |
| Gasempfangsanlage Dornum | Open Grid Europe / Gasunie Deutschland | Europipe-gas (~160 bar) → ontspand (~80 bar) → NETRA-net / Emden-Knock | NETRA 341 km totaal naar Salzwedel-Steinitz (49 km Etzel→Dornum sinds 1999); apart 49 km verder naar meetstation Emden-Knock | [2][5] |

## 6 · Stoppunt
De brief stopt bij de Gasempfangsanlage/het invoedingspunt Dornum: dit is precies het door het
ontwerp gevraagde stoppunt (invoedingspunt Duits/NW-Europees net). Vanaf hier vertakt het gas
anoniem het Duitse net in (NETRA naar Salzwedel-Steinitz én de 49 km-leiding naar Emden-Knock) —
geen bron volgt één specifieke gasstroom verder naar een fabriek of centrale.

## 7 · Open punten
- **Het ~642 km offshore-stuk is alleen op naamtag-aanwezigheid gecontroleerd** (pyosmium-scan
  bevestigt `man_made=pipeline`+`substance=gas`+naam Europipe II aan beide kustzijden: Noorwegen 6
  ways/176 nodes, Duitsland 2 ways/81 nodes — haalbaarheidstoets, bindend), niet op doorlopende
  geometrie of lengte. Een Dijkstra/lengtetoets bij de bake kan een gat in het midden opleveren —
  wordt dat dan een stippel (bakhandleiding §2).
- **Fase A (verzamelvelden) is bewust niet getekend** — Statpipe verzamelt van meerdere platforms
  (Åsgard, Sleipner Oost/West, Gullfaks, Statfjord); geen enkelvoudig traceerbaar tracé, zelfde
  behandeling als de diffuse Amerikaanse schaliegasvelden in andere gas-brieven.
- **Geen Europa-specifiek jaarvolume voor déze as** — alleen de 24 bcm/j ontwerpcapaciteit (algemeen
  bekend Wikipedia-cijfer [1], geen vers 2025/2026-brondocument).
- **Dornum-anker scherper gelegd dan het ontwerp** (ontwerp: 53,64589/7,43022 → nu 53,6564/7,4039):
  het ontwerp-coördinaat bleek het dorpscentrum van Dornum zelf (geen zichtbare installatie op
  satelliet); de Duitse Wikipedia geeft de exacte coördinaat van de Gasempfangsanlage/het Heizhaus
  (53°39'23"N 7°24'14"O), en dát punt toont wél een omheind industrieterrein. Zelfde locatie
  (invoedingspunt bij Dornum), scherper anker.
- **NETRA zelf (Dornum → Salzwedel-Steinitz, 341 km) is niet getekend** — het ontwerp vraagt het
  invoedingspunt, niet het vervolgnet; zou een aparte as/keten zijn.

## 8 · Bronnen
[1] Wikipedia (EN), "Europipe II" — route (13 km onshore Kårstø→Vestre Bokn, 642 km offshore
    NO/DK/DE-sector, 15 km onshore DE), diameter 1.100 mm, capaciteit 24 bcm/j, velden Åsgard/
    Sleipner Oost-West/Gullfaks/Statfjord, operator Gassco/Equinor, in bedrijf 1999.
    https://en.wikipedia.org/wiki/Europipe_II
[2] Wikipedia (DE), "Europipe (Pipeline)" — Europipe II ~660 km, landing tussen Dornum en Nesse,
    Gasempfangsanlage (160→80 bar), Heizhaus 53°39'23"N/7°24'14"O, 49 km verder naar Emden-Knock
    (53°21'40"N/7°0'31"O, meetstation 60 mln Nm³/dag), NETRA-aftakking vanaf Dornum.
    https://de.wikipedia.org/wiki/Europipe_(Pipeline)
[3] Wikipedia (EN), "Kårstø" — gasbehandelingscomplex Tysvær, coördinaat 59,2774/5,5247, grootste
    NGL-exportpoort van Europa, drooggas via Europipe II naar Dornum en via Statpipe/Norpipe naar
    Emden. https://en.wikipedia.org/wiki/K%C3%A5rst%C3%B8
[4] OpenStreetMap/Nominatim (ODbL) — Kårstø-omgeving, industrieel complex bevestigd op satelliet.
    https://www.openstreetmap.org
[5] Wikipedia (DE), "Norddeutsche Erdgas-Transversale" — NETRA 341 km, importpunt Europipe bij
    Dornum, verlenging Etzel→Dornum 1999 (49 km), Verdichterstation Wardenburg, eigenaar/beheerder
    Open Grid Europe en Gasunie Deutschland.
    https://de.wikipedia.org/wiki/Norddeutsche_Erdgas-Transversale
[6] OpenStreetMap/Nominatim (ODbL) — Dornum-omgeving; geen naam-tag voor de Gasempfangsanlage
    gevonden, coördinaat uit bron [2] gebruikt en satellietbevestigd. https://www.openstreetmap.org
[7] gem.wiki, "NETRA Gas Pipeline" — Global Energy Monitor-samenvatting, Open Grid Europe/Gasunie
    Deutschland als eigenaars, bevestigt bron [5]. https://www.gem.wiki/NETRA_Gas_Pipeline
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) —
    `v2/build-cache/satcheck/sat-gas-karsto-dornum-karsto-plant.png`,
    `sat-gas-karsto-dornum-dornum-gasempfangsanlage.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Eén been (fase B, leiding), 655,8 km, 181 punten, 2 markers — géén stippel.**

| # | modaliteit | van → naar | km | naad | stippel |
|---|---|---|---|---|---|
| b1 | leiding | `gas-karsto-plant` → `gas-dornum-netra` (Europipe II) | 655,8 | 0,00 km (enige been) | nee |

**Recept:** `bak_gas_karsto_dornum()` in `v2/tools/bak_stromen.sh`, één
`--been-geojson "leiding|…"`. Geen weg-/spoor-/zee-profiel nodig (geen andere
modaliteit in deze keten).

**⚠️ Het open punt uit §7 is deze sessie WEERLEGD — de offshore-continuïteit
is bevestigd, geen stippel nodig.** Een pyosmium-scan op de lokale extracts
`noorwegen` + `de-niedersachsen` (⚠️ extract-naam is `noorwegen`, niet
`norwegen` zoals de opdracht schreef) vond een DOORLOPENDE keten van 7 exact
aaneensluitende OSM-ways (elk paar deelt zijn eindpunt-coördinaat, geen enkel
gat): `1117764491 → 1117764494 → 1117764490 → 1117764492 → 523930562 →
174152562 → 795944175`. De eerste vijf + `174152562` dragen `man_made=pipeline`
+ `substance=gas` + naam-tag "Europipe II"; `174152562` is de lange
hoofd-offshore-way (70 nodes) die in z'n eentje van de Noorse landing tot bij
de Duitse landing loopt. `795944175` heeft geen eigen naam-tag maar sluit
exact aan op `174152562` (identieke coördinaat 7,4753165/53,7001936) en ligt
tussen de Duitse landing en de Dornum-aansluiting — inhoudelijk hetzelfde
tracé, zonder OSM-naamlabel. Het OUDERE "Europipe" (I, ways `174152545` +
`1167437586`, begint bij het Draupner-platform) is apart en NIET meegenomen.

**Lengte:** 655,8 km tegen ~670 km (Engelse Wikipedia, 13+642+15 km) = **−2,1%**;
tegen de Duitse Wikipedia's ruwe "~660 km" = **−0,6%**. Beide binnen de
indicatieve marge die de brief hier aanhoudt (de ±15%-toets als indicatie,
geen harde norm — dat voorbehoud is met deze bevestigde continuïteit
achterhaald, maar de meting bevestigt het toch ruimschoots).

**Ankers/markers:** `gas-karsto-plant` (59,2774/5,5247, kop) en
`gas-dornum-netra` (53,6564/7,4039, staart, stoppunt) — ongewijzigd t.o.v. de
brief. Marge kop-anker → eerste stitch-punt 0,94 km; staart-anker → laatste
stitch-punt 0,16 km. Beide < 5 km → geen losse stippel nodig (anker ≠
routeerpunt, bakhandleiding §5).

**Toets (§5 bakhandleiding):** `toets_knikken.py` — 2 knikken ≥ 60°, 0
omkeringen, 0 terugloop (normale bochten in een reëel OSM-tracé, geen
reparatie nodig). `toets_rechte_benen.py --min-km 5` — dit been staat NIET in
de lijst (181 punten, omwegfactor ≠ 1,000, dus geen "rechte lijn"-verdenking).
`json.load` slaagt: versie 2, punt_formaat lonlat, modaliteit `leiding` ∈ de
toegestane set, been ≥ 2 punten (181), bestand 4,06 KB (ruim onder de norm).

**Lessen voor een volgende leiding-bake:**
- Een offshore pijpleiding kan als ÉÉN OSM-way de hele lengte dekken (hier 70
  nodes over ~640 km, met een enkel segment van 241 km tussen twee
  opeenvolgende nodes) — dat is geen kartering-gat maar een sparsely-vertexed
  rechte offshore-tracé; niet verwarren met een echt gat tussen twee
  losstaande ways.
- Extract-namen zijn Nederlandse Geofabrik-slugs; controleer de exacte
  schrijfwijze in `v2/build-cache/geofabrik/` vóórdat je "extract ontbreekt"
  concludeert (`noorwegen`, niet `norwegen`).
- Bij twee gelijkende leidingnamen op dezelfde landing (hier Europipe I vs II
  bij Dornum) sluit alleen de exacte way-id-keten uit dat de verkeerde
  generatie meegepakt wordt — filteren op naam alleen is hier voldoende
  geweest (beide dragen een eigen naam-tag), maar de way-ids zijn vastgelegd
  in de kopcommentaar voor reproduceerbaarheid.
