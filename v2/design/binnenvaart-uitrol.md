# Binnenvaart — wereldwijde uitrol (M24, ná LAR-486/487/488)

*Opgesteld 2026-07-19, ná de drie pilots. Status: plan, nog niet gebouwd.*

## De regel (Lars)

> *"als er geen commercieel boten kunnen varen dan niet, of als het echt nergens
> heen leidt, maar het moet wel uitgebreid zijn voor de simulator"*

Drie criteria, in deze volgorde:

1. **Commercieel bevaarbaar.** Recreatievaart en seizoensgebonden lokaal verkeer
   tellen niet. Dit bevestigt de eerdere M24-keuze (EU CEMT ≥ IV, VS het
   USACE-net, elders de bekende commerciële systemen; klasse I–III = ruis).
2. **Het moet ergens heen leiden.** Een vaarweg die niet aan het zeenetwerk
   hangt is voor de router een **geïsoleerde component**: er kan nooit een route
   overheen lopen. Dat is de scherpste snoeiregel — zie de uitsluitingen hieronder.
3. **Verder zo compleet mogelijk**, want M21 (disruptie-simulator) kan alleen
   knelpunten doorrekenen die ook echt in het netwerk zitten.

## Wat criterium 2 uitsluit — de niet-voor-de-hand-liggende gevallen

Deze rivieren dragen **wél** echt commercieel verkeer, maar hun bevaarbare deel
is fysiek afgesneden van zee. Ze toevoegen levert knopen op waar geen enkele
route ooit komt.

| systeem | de blokkade | wat er wél vaart |
|---|---|---|
| **Congo boven Kinshasa** | **Livingstone-watervallen** — ~350 km stroomversnellingen tussen Matadi (zeehaven) en Kinshasa, absoluut onbevaarbaar | ~1.700 km druk bevaarbaar Kinshasa↔Kisangani, maar volledig ingesloten |
| **Paraná boven Itaipú** | Itaipú-dam heeft **geen schutsluis** | bovenstrooms verkeer bestaat, maar komt nooit bij zee |
| **Mekong boven de Khone-watervallen** | watervallen op de grens Laos/Cambodja | Laos/Thailand hebben lokaal verkeer, geen doorvaart |
| **Nijl boven de Aswandam** | stuwdam zonder doorvaart | grotendeels toerisme |

> [!note] Dit is een bewuste keuze, geen omissie
> De Congo is het scherpste geval: het ís een van de drukst bevaren rivieren van
> Afrika, maar voor een routeernetwerk waardeloos. Als we hem ooit tóch willen
> tonen (visuele volledigheid), dan als **losse laag**, niet als routeerbare edges.

Verder uitgesloten op criterium 1 (te weinig commercieel verkeer): Missouri boven
Sioux City (bargeverkeer vrijwel verdwenen), Elbe boven Maagdenburg (chronisch
laagwater), Irrawaddy boven de delta, Niger.

## Wat er in gaat

Per systeem het natuurlijke **kopeinde van de commerciële vaart** — dáár stopt
de keten. Exacte ankers + namen worden per systeem geverifieerd tegen de
Geofabrik-extract én tegen waar MARNET werkelijk ophoudt (zoals bij de pilots
bleek: de zone-naam zegt niets over het echte uiteinde).

### Europa — de Rijn-Donau-as
De drukste binnenvaartcorridor ter wereld; met het Main-Donau-Kanaal loopt er
een doorgaande vaarweg van **Rotterdam tot de Zwarte Zee**.

| systeem | traject | kopeinde omdat |
|---|---|---|
| Rijn | Rotterdam → Duisburg → Köln → Mainz → Basel | Basel = kop van de scheepvaart |
| Main + Main-Donau-Kanaal | Mainz → Bamberg → Kelheim | de verbinding naar de Donau |
| Donau | Kelheim → Wenen → Boedapest → IJzeren Poort → Sulina | zee |
| Schelde | Vlissingen → Antwerpen | Europa's #2 haven |
| Seine | Le Havre → Rouen → Parijs | kop van de vrachtvaart |
| Rhône | Fos-sur-Mer → Lyon | idem |

### Noord-Amerika — het binnenvaartnet rond de Mississippi
| systeem | traject | waarom |
|---|---|---|
| Ohio | Cairo → Louisville → Cincinnati → Pittsburgh | **kolen** — direct relevant voor M26 |
| Upper Mississippi | Memphis → St. Louis → Minneapolis | graan |
| Illinois | Grafton → Chicago | verbindt de Mississippi met de Grote Meren/Seaway |

### Zuid-Amerika
| systeem | traject | waarom |
|---|---|---|
| Amazone | Belém → Manaus | **zeeschepen varen 1.500 km landinwaarts** tot Manaus |
| Paraná/Paraguay (Hidrovía) | Buenos Aires → Rosario → Asunción → Corumbá | soja/ijzererts |
| Orinoco | Boca Grande → Puerto Ordaz | ijzererts-export |

### Azië
| systeem | traject | waarom |
|---|---|---|
| Yangtze-verdieping | Wuhan → Chongqing | de Drieklovensluizen wérken; schepen komen tot Chongqing |
| Grand Canal | Hangzhou → Jining | naar tonnage het drukste kanaal ter wereld (kolen/bulk) |
| Parelrivier / Xi Jiang | Hongkong → Guangzhou → Wuzhou | containers + bulk |
| Mekong | Vũng Tàu → Phnom Penh | stopt bij de Khone-watervallen |

### Rusland
| systeem | traject | waarom |
|---|---|---|
| Wolga | Astrachan → Volgograd → Samara → Nizjni Novgorod | de as van het Russische binnenland |
| Wolga-Don | → Zee van Azov | verbindt Kaspische Zee met de Zwarte Zee |
| Wolga-Baltisch | → Sint-Petersburg | verbindt met de Oostzee |

## Aanpak

De pijplijn staat en is drie keer bewezen; dit is uitrol, geen nieuw ontwerp.

1. **Bron = Geofabrik** (`fetch_waterways.py geofabrik`). Gevalideerd tegen
   Overpass: coördinaat voor coördinaat identiek, maar instant en offline.
   Overpass blijft bestaan als kruiscontrole.
2. **Namen opzoeken, niet raden.** Met de extract lokaal is de namenlijst uit de
   data te lezen (51.191 ways in 4 s). Dat is bij niet-Latijnse namen het verschil
   tussen werken en niets vinden — de Yangon-pilot vond `ရန်ကုန်မြစ်`, wat als
   blinde query nooit was gelukt. Doe dit vóór elk systeem.
3. **Ankers verifiëren tegen MARNET**, niet tegen de zone-naam. Alle drie de
   pilots eindigden ergens anders dan hun zone suggereerde.
4. **Segmenteren met `volgtOp`** waar de zeevaart-grens binnen een rivier ligt
   (Rijn: zeeschepen tot ±Keulen; Amazone: tot Manaus; Donau: tot Brăila).
5. **Meetlat waar die bestaat**: UNECE voor de EU (CEMT-klassen), USACE voor de
   VS. Elders de haventoets uit LAR-488 — vallen de searoute-havens vanzelf op
   de keten?
6. **Lengte tegen de officiële vaarafstand** blijft de beslissende controle.

## Wat de data zei (survey over de 17 GB extracts, 2026-07-19)

De namenlijsten zijn **opgezocht, niet geraden** — stap 2 van de aanpak, meteen
toegepast op de plan-fase zelf. Dat leverde vier dingen op die stilzwijgend fout
waren gegaan.

**Eerst een methodefout van mezelf, voor de volgende keer.** Mijn eerste survey
rangschikte op vertex-aantal. Fout: dat meet detailniveau, niet belang. Een grote
bevaarbare rivier is vaak als *vlak* gemapt met een spaarzame middellijn, terwijl
een beek een lange fijn-gemapte enkele lijn is. Resultaat: de Rijn stond 6e, en
Donau, Wolga, Paraná en Amazone vielen volledig uit de top-6. **Rangschik op
totale lengte.** Daarmee komen de hoofdstromen bovenaan (Волга 2.668 km, Ohio
River 2.667, Mississippi 2.665, Río Paraná 1.649, 长江 1.437).

**1 · De Donau heet per land anders én draagt gecombineerde grensnamen.**
`Donau` (DE/AT) · `Duna` (HU) · `Dunaj` (SK) · `Dunărea` (RO) · `Дунав` (BG/RS)
— maar op grenstrajecten staat er één samengestelde naam: **`Dunaj / Duna`**
(288 km, SK/HU) en **`Dunărea - Дунав`** (1.111 km, RO/BG). Zonder die twee
knipt de keten bij elke grens door. Dit had ik nooit geraden.

**2 · De Wolga-Don draagt een eretitel.** Niet `Волго-Донской судоходный канал`
maar **`Волго-Донской судоходный канал им. В. И. Ленина`**. Exacte tag-match
faalt op de korte vorm.

**3 · `扬子江` bestaat niet** in OSM — alleen `长江`. Staat nu als dode
whitelist-regel in het `yangtze`-systeem; onschadelijk, maar weg ermee.

**4 · De Amazone heeft géén benoemde middellijn** — de echte blokkade.
`Rio Solimões` dekt 349 km bovenstrooms, `Río Amazonas` is een fragment van
20 km, en juist het stuk **Manaus → Belém** (waar de zeeschepen varen) heeft
geen enkele benoemde `waterway=river`-lijn. Oorzaak: die rivier is daar tot
>10 km breed en als **wátervlak** gemapt, niet als lijn.

> [!done] Opgelost — `v2/tools/middellijn_uit_vlakken.py` (Lars: *"dat moeten we
> wel eerst fixen"*)
> Er is nu een tweede manier om aan een middellijn te komen: **afleiden uit de
> watervlakken** in plaats van stitchen uit lijnen. Herbruikbaar voor élke brede
> rivier (Rio de la Plata, estuaria, stuwmeren).
>
> **Hoe:** watervlakken rasteren → per watercel de **klaring** bepalen (afstand
> tot de oever, exacte afstandstransformatie, anisotroop want een graad lon is
> korter dan een graad lat) → alleen cellen met ≥150 m klaring gelden als
> bevaarbaar (dát encodeert "commercieel bevaarbaar" meteen in de geometrie) →
> Dijkstra van anker naar anker met een milde voorkeur voor het midden van de
> geul. Bewust géén medial axis: we willen één vaarbare lijn, geen skelet.
>
> **Uitkomst Amazone (Macapá → Manaus):** 1.319,9 km · 312 punten · klaring
> langs de route min 0,44 / mediaan 1,60 / max 7,61 km. Lengte klopt met de
> echte riviervaarafstand. Haventoets (searoute, andere bron dan OSM): Manaus
> 0,55 km (= het anker) en **Óbidos 3,15 km** — een echte rivierhaven halverwege,
> dus onafhankelijke bevestiging. Santarém 10,8 / Macapá 12,4 / Santana 13,2 km
> liggen verder, maar dat zijn oeverhavens terwijl de lijn mid-geul loopt en de
> rivier daar 20+ km breed is (gemeten max klaring 7,61 km ≈ 15 km breed).
> Consistent, niet apart bewezen.
>
> **Twee dingen die dit kostte, voor de volgende keer.** De eerste versie
> verzamelde álle watervlakken in het venster en deed er één `union_all` overheen
> → 5,5 GB RAM en na 11 min CPU nog niet klaar, want een venster over het
> Amazonebekken bevat duizenden meren. Nu wordt elk vlak **direct in het raster
> gebrand** en weggegooid: 911 MB, vlak. Van de 289.365 watervlakken in Brazilië
> raken er maar **1.241** het venster. En de osmium-pass zelf kost ~13 min (twee
> passes over 2 GB om multipolygoon-relaties te reconstrueren) → resultaat gaat
> in een cache, zelfde les als de verzoening-cache.

## Uitgevoerd: de Rijn (LAR-492, 2026-07-19)

Eerste systeem van de uitrol. Twee ketens, `rijn` (Nijmegen → Bingen, 355,0 km)
en `rijn-boven` (Bingen → Basel, 360,6 km), beide `volgtOp` de vorige.

**Drie dingen die de volgende systemen ook gaan raken.**

1. **De namen-survey is nu gereedschap:** `v2/tools/survey_vaarwegen.py` geeft
   per venster de benoemde vaarwegen **op lengte** mét hun lon/lat-strekking —
   aan die strekking zie je of de whitelist een *doorlopend* traject dekt. Dat
   ving hier twee stille ketenbreuken: **`Boven-Rijn`** (mét koppelteken, 4,3 km)
   is de enige schakel tussen `Bijlandsch Kanaal` en `Rhein`, en
   **`Le Rhin / Rhein`** is de gecombineerde grensnaam op het Frans-Duitse
   traject — precies de `Dunaj / Duna`-val, nu voorspeld in plaats van geraden.
2. **Een extract kan buiten de oeverlanden liggen.** Tussen Basel en Straatsburg
   ligt de vaargeul niet in de Rijn maar in het **Grand Canal d'Alsace**, volledig
   op Frans grondgebied: zonder `fr-alsace` knipt de keten met een gat van
   **72,9 km**, en beide randen van dat gat heten verwarrend genoeg allebei
   `Grand Canal d'Alsace`. Les: kijk niet naar welke landen de rivier *raakt*,
   maar naar waar de **geul** ligt.
3. **Bewust uitgesloten: `Vieux Rhin / Altrhein`** (54 km). Dat is de Restrhein —
   wél water, géén bevaarbare geul. Whitelisten zou een korter, onvaarbaar pad
   opleveren; hetzelfde principe als de ≥150 m-klaring bij de Amazone.

**Gesplitst bij Bingen, niet bij de zeevaartgrens.** Het issue stelde
`zeevaart=True` → `False` voor bij Keulen/Duisburg, maar `waal` stroomafwaarts
staat al op binnenvaart, dus dat splitspunt beschrijft niets. Besluit van Lars:
splits waar een **echte verstoring** zit. Bij Kaub, in de Gebirgsstrecke, legde
het laagwater van 2018 en 2022 de as stil; `rijn-boven` in `vermijd` reproduceert
dat exact — Duisburg en Keulen blijven bereikbaar, Mainz/Karlsruhe/Kehl niet.

> [!warning] Voor LAR-493 (Main + Main-Donau-Kanaal)
> `volgtOp` hecht aan het **binneneinde** van een keten, en Mainz ligt 30 km
> ínterne keten van `rijn-boven` (Bingen rkm 528, Mainz rkm 498). De Main kan er
> dus niet aan hangen zoals hij nu staat. Goedkoopste oplossing: knip
> `rijn-boven` bij Mainz in tweeën — de middellijn zelf verandert niet, alleen
> de ankers, en de bake kost ~2 s dankzij de verzoening-cache.

## Open punten

- **Frankrijk-regio's — opgelost:** Geofabrik staat nog op de **pre-2016**
  indeling. `alsace`, `basse-normandie` (136 MB) en `rhone-alpes` (500 MB)
  bestaan; **`normandie` bestaat niet** en geeft geen 404 maar een bestand van
  **0 bytes** — dezelfde val als de Brazilië-shapefile, dus controleer de
  bestandsgrootte, niet de HTTP-status. India/West-Bengalen nog uitzoeken vóór
  Hooghly.
- **Volgorde:** Rijn-Donau eerst (grootste tonnage, en de EU heeft een meetlat),
  dan Noord-Amerika (kolen → M26), dan de rest.
- **Chongqing en St. Louis** stonden als "evt." in LAR-487/488 en vallen nu
  binnen de regel — meenemen in de uitrol.
