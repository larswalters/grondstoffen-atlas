# Gas · Bonny Island (Nigeria) → Zeebrugge (België)

**stroom-id:** `gas-bonny-zeebrugge` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) · **status:** gebakken
**Keten in één zin:** Nigeriaans LNG van het NLNG-complex op Bonny Island, per zeeschip langs de West-Afrikaanse kust
en door de Straat van Gibraltar naar de Fluxys LNG-terminal in Zeebrugge, waar het hervergast het Belgisch/
NW-Europese gasnet in gaat.
**Welke as van het verhaal:** de enige Afrikaanse LNG-stem naar Europa, kwetsbaar vóór de kade — Nigeria's
gasexport hangt structureel af van een feedgas-aanvoer die herhaaldelijk wordt gesaboteerd in de Niger-delta,
ver vóór het schip ooit vertrekt.

## 1 · Ketenkaart
```
NLNG-complex Bonny Island `gas-bonny-nlng` ──(b1 zee · Golf van Guinee → Straat van Gibraltar →
   Golf van Biskaje → Het Kanaal/Noordzee · ~7.500–8.000 km, MARNET, haven-aanloop beide zijden)──►
   Fluxys LNG-terminal Zeebrugge `gas-zeebrugge-lng`
   ──(b2 leiding · korte terreinleiding · ~5 km, stippel)──►
   netinvoedingspunt `gas-zeebrugge-iuk` (Fluxys/Interconnector-zone) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | NLNG-complex Bonny Island → Fluxys-terminal Zeebrugge | Golf van Guinee → Straat van Gibraltar → Golf van Biskaje → Kanaal/Noordzee | ~7.500–8.000 [ontwerp] | MARNET (kade→kade) | nee — met haven-aanloop aan beide zijden (zie §3/§7) |
| b2 | C | leiding | Fluxys-terminal Zeebrugge → netinvoedingspunt | korte terreinleiding, Zeebrugge-industriezone | 4,98 [eigen meting, OSM-punten] | stippel; OSM `man_made=pipeline` niet gecontroleerd (webbudget) — bak-agent checkt | ja, tenzij het bakken een OSM-way vindt |

Fase A (Niger-delta gasverzamelsysteem) vervalt: diffuus, geen enkelvoudig traceerbaar tracé
(haalbaarheidstoets-aanpassing).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-bonny-nlng` | productie + laadkade (LNG-complex) | Nigeria LNG Ltd, Bonny Island | 4.41836, 7.16157 | [1][2][3][8] | bron-gelegd (z15 gezien: industrieel complex met meerdere procestreinen, tankenpark, twee steigers de zee in aan de westkant — jetty-structuur duidelijk zichtbaar) |
| `gas-zeebrugge-lng` | losplek + regasterminal (Fluxys) | Fluxys LNG Zeebrugge | 51.3537, 3.2200 | [4][5][6][8] | bron-gelegd (z15/z16 gezien: 4 bolvormige LNG-tanks, tankenpark met procesinstallaties, twee steigerconstructies met laadarmen het LNG-dok in) |
| `gas-zeebrugge-iuk` | netinvoedingspunt (fase C-eind) | terrein "UK Gas Interconnector Terminal" (Fluxys-gaszone), Zeebrugge | 51.3156, 3.1822 | [8][9] | aannemelijk (z15 gezien: ommuurd industrieterrein met gebouwen en een cirkelvormige toegangsweg, consistent met een gasinstallatie; koppeling aan specifiek de Zeebrugge-zendlijn niet apart gebrond) |

## 4 · Via-punten
Niet van toepassing: het zeebeen routeert via MARNET (geen corridorkeuze door ons te leggen) en het leidingbeen
is te kort (< 5 km) voor een corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| NLNG-complex Bonny Island | Nigeria LNG Ltd (NNPC 49% · Shell 25,6% · TotalEnergies 15% · Eni 10,4%) | feedgas → LNG | 22 Mtpa nominaal (6 bestaande treinen); Train 7 (4,2 Mtpa, 80% gereed medio 2025, operationeel 2027) brengt het naar ~30 Mtpa | [1][3] |
| Fluxys LNG-terminal Zeebrugge | Fluxys | LNG (tanker) → hervergast pijpleidinggas | opslag 566.000 m³ (5 tanks); regas 11,3 Mtpa na de 2024–2026-uitbreiding met 4,7 Mtpa (open rack vaporizers); +1,3 Mtpa sendout begin 2026; lange-termijnslots 9/j vanaf april 2027, 12/j 2028–2044 | [4][5] |

## 6 · Stoppunt
De brief stopt bij het netinvoedingspunt in de Zeebrugge-gaszone: vanaf hier verdwijnt de LNG-herkomst in het
gemengde Belgisch/NW-Europese pijpleidingnet — er is geen enkelvoudige "fabriek" die dit gas als eindproduct
ontvangt, en fase D/E vervallen (geen bron koppelt dit gas aan één specifieke afnemer of installatie).

## 7 · Open punten
- **Fase A vervallen** (haalbaarheidstoets-aanpassing): het Niger-delta gasverzamelsysteem is diffuus en niet
  in één tracé te vangen; het structurele feedgas-risico (sabotage/diefstal, herhaalde force-majeure-
  verklaringen van NLNG) speelt hier, vóór de kade — niet in de zeeroute.
- **Europa-specifiek cargovolume Bonny→Zeebrugge niet los gebrond**: alleen totaalcijfers voor NLNG (export)
  en Zeebrugge (regas) gevonden, geen bron die één specifieke ladingstroom koppelt.
- **`gas-zeebrugge-iuk` is een aanname op naam + afstand**: het OSM-terrein "UK Gas Interconnector Terminal"
  ligt op 4,98 km van de LNG-terminal (< 5 km, consistent met het ontwerp) en toont op satelliet een
  gasinstallatie, maar geen bron bevestigt expliciet dat dít de Fluxys-zendlijn vanaf de LNG-terminal is.
- **OSM `man_made=pipeline` voor fase C niet gecontroleerd** (webbudget) — bak-agent checkt bij het bakken;
  zonder OSM-way blijft b2 een schematische stippel.
- **Haven-aanloop nodig aan beide zijden van b1**: Bonny-jetty ligt 7,94 km van de dichtstbijzijnde
  MARNET-zeeknoop, Zeebrugge-terminal 20,50 km — beide boven de 5 km-drempel (bakhandleiding §2, sinds
  2026-09-28).
- **Grote cirkel Bonny–Zeebrugge is 5.232 km**, ruim korter dan de ~7.500–8.000 km ontwerp-schatting —
  plausibel doordat de rechte lijn dwars over West-Afrika/Frankrijk zou lopen; de vaarbare route volgt de
  kust en Gibraltar. Definitieve km volgt uit de MARNET-bake.

## 8 · Bronnen
[1] Global Energy Monitor (GEM.wiki), "Nigeria LNG Terminal" — coördinaat 4,41836/7,16157, capaciteit per
trein (Train 1-3 3,3 Mtpa, Train 4-6 4,1 Mtpa, Train 7 4,2 Mtpa in aanbouw), eigendom NNPC/Shell/
TotalEnergies/Eni. https://www.gem.wiki/Nigeria_LNG_Terminal
[2] Wikipedia, "Nigeria LNG" — coördinaat 4,4258/7,1531 (Bonny Island). https://en.wikipedia.org/wiki/Nigeria_LNG
[3] Wikipedia, "Bonny Island" — ligging Rivers State, Niger-delta. https://en.wikipedia.org/wiki/Bonny_Island
[4] Fluxys, "Zeebrugge LNG" — terminaldiensten (lossen/laden LNG-schepen, transshipment, truck loading,
regasificatie voor invoeding in het transmissienet). https://www.fluxys.com/en/about-us/zeebrugge-lng
[5] LNG Prime, "Belgium's Fluxys offers long-term capacity at Zeebrugge LNG terminal" — opslag 566.000 m³
(5 tanks), regas 11,3 Mtpa na uitbreiding met 4,7 Mtpa, tijdlijn 2027–2044.
https://lngprime.com/europe/belgiums-fluxys-offers-long-term-capacity-at-zeebrugge-lng-terminal/114411/
[6] Wikipedia, "Zeebrugge" — "grootste LNG-terminalcomplex van Europa". https://en.wikipedia.org/wiki/Zeebrugge
[7] Wikipedia, "List of LNG terminals" — Zeebrugge LNG terminal, geëxploiteerd door Fluxys.
https://en.wikipedia.org/wiki/List_of_LNG_terminals
[8] OpenStreetMap (ODbL) via Photon/Nominatim — Bonny: "Nigeria LNG Residential" 4,3871/7,1789, "LNG Train 2"
4,4210/7,1538, "LNG Train 7" 4,4171/7,1644; Zeebrugge: "LNG-dok" 51,3483/3,2138, "Zeebrugge lng-terminal"
landuse 51,3527/3,2224, "UK Gas Interconnector Terminal" landuse 51,3156/3,1822. https://www.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16) — `sat-gas-bonny-zeebrugge-bonny-nlng.png`,
`sat-gas-bonny-zeebrugge-zeebrugge-lngdok.png`, `sat-gas-bonny-zeebrugge-zeebrugge-jetty.png`,
`sat-gas-bonny-zeebrugge-iuk-interconnector.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `gas-bonny-zeebrugge`** → `v2/data/stroomroute-gas-bonny-zeebrugge.json` — 4 benen, **8.198,4 km**,
858 punten, 3 markers. zee 7,9 (stippel) + 8.165,0 + 20,5 (stippel) = 8.193,4 km · leiding 5,0 km (stippel).
Recept: `bak_stromen.sh` (functie `bak_gas_bonny_zeebrugge`).

**b1a (zee, stippel, haven-aanloop Bonny Island):** de Bonny-jetty ligt 7,94 km van de dichtstbijzijnde
MARNET-zeeknoop 5231 (4,39020/7,09580) — boven de 5 km-drempel (bakhandleiding §2, sinds 2026-09-28), dus een
haven-aanloop nodig ook al snapt MARNET zelf ruim binnen de 25 km-norm. `maak_havenaanloop.py --van
4.41836,7.16157 --naar 4.39020,7.09580` liep vast op `timeout 300` (exit 124) — geen tweede poging, rechte
stippel: **7,936 km**.

**b1 (zee, MARNET, geen aanloop meer nodig — begint al op de zeeknoop):** `--been "zee|...|4.39020,7.09580|
51.50000,3.40000"` — snap aan beide zijden 0,000 km (de knopen zelf zijn het beginpunt). Resultaat **8.165,0 km
over 60 MARNET-edges, 852 punten**, tegen de ontwerpschatting ~7.500–8.000 km uit de brief. Dat is +2,1% boven het
bovenste ontwerpgetal en +56,1% boven de grote cirkel (5.232 km) — de vaarbare route volgt de West-Afrikaanse
kust en Gibraltar zoals de brief voorspelde, en het totaal (incl. beide haven-aanlopen: 8.193,4 km) valt nog
ruim binnen de brede ±15%-marge rond het ontwerpmidden (~7.750 km). Lengte-invariant: getekende lijn 8.165,031 km
vs som edge-km 8.165,100 km = −0,069 km (de naden).

**b1b (zee, stippel, haven-aanloop Zeebrugge):** de Zeebrugge-terminal ligt 20,50 km van de dichtstbijzijnde
MARNET-zeeknoop 1629 (51,50000/3,40000) — eveneens boven de 5 km-drempel. `maak_havenaanloop.py --van
51.3537,3.2200 --naar 51.50000,3.40000` liep óók vast op `timeout 300` (exit 124) — geen tweede poging, rechte
stippel: **20,503 km**.

**b2 (leiding, Zeebrugge-terrein, stippel, GECONTROLEERD):** het OSM `man_made=pipeline`-net is dit keer wél
gecontroleerd (brief §7 zei "niet gecontroleerd binnen het webbudget"). Een pyosmium-scan op de belgie-
Geofabrik-extract binnen een venster rond Zeebrugge vond **73 pijpleiding-ways**, waaronder de benoemde
"Interconnector"- en "Zeepipe"-lijnen. Een topologische component-analyse (gedeelde OSM-nodes, zelfde methode als
`bake_marnet.py`) over het VOLLEDIGE Belgische pijpleidingnet (1.861 ways, 61.119 knopen) laat zien dat het
LNG-terminal-anker (51,3537/3,2200, component van 118 nodes) en het IUK-netinvoedingspunt (51,3156/3,1822,
component van 7 nodes) op **twee gescheiden, niet-verbonden componenten** liggen — géén enkele gedeelde node. De
Interconnector-lijn (way 584264074) en het cluster rond de IUK-poort liggen alle in het IUK-component, maar dat
component raakt de LNG-terminal-zijde nergens. Blijft dus een rechte stippel: **4,984 km** (het eigen-metingsgetal
uit de brief, 4,98 km, bevestigd).

**Toets naden:** alle overgangen tussen de vier benen **0,000 km** — elk been begint precies waar het vorige
eindigt (geen tussenliggend routeerpunt dat afwijkt van het anker).

**`toets_knikken.py`:** 1 knik ≥60° (86,8°, R≈6.355 m, bij 4,15470/7,10270 — een krappe bocht vlak na het
vertrek van de Golf van Guinee, waar de MARNET-route de kust rondt), **0 omkeringen, 0 terugloop**. Geen bevinding.

**`toets_rechte_benen.py --min-km 5`:** alle drie de stippelbenen van deze stroom (b1a 7,9 km · b1b 20,5 km ·
b2 5,0 km, alle omwegfactor ~1,00) komen in de uitslag naar voren als "rechte lijn" — dat is **verwacht en
correct**: elk van de drie is een gedocumenteerde stippel met reden (twee mislukte haven-aanlopen, één
gecontroleerde en negatieve OSM-pijpleidingcheck), niet een abusievelijk rechtgetrokken gemeten been.

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {zee, leiding} (binnen de toegestane
set), elk been ≥2 punten (minimum 2, het gemeten zeebeen 852), bestandsgrootte **16,2 KB** (ruim < 300 KB).

**Markers:** alle drie op **0,0 m** van de lijn (het zijn de been-eindpunten zelf: gas-bonny-nlng, gas-zeebrugge-
lng, gas-zeebrugge-iuk).

**Gereedschapslessen:**
- De zeeknoop-lookup uit de brief (`bak_aanwijzingen`) kwam bij het bakken exact terug: Bonny-jetty 7,94 km /
  zeeknoop 5231, Zeebrugge-terminal 20,50 km / zeeknoop 1629 — beide onafhankelijk herrekend vóór het bakken en
  identiek aan de brief.
- Twee haven-aanlopen op rij die allebei op `timeout 300` vastlopen (Bonny én Zeebrugge) is geen toeval-per-been
  maar consistent met de bakhandleiding-observatie dat de 1:10M-kust bepaalde havens niet kent; geen van beide
  is een indicatie dat er wél een pad bestaat dat een tweede poging zou vinden.
- "Niet gecontroleerd binnen het webbudget" uit de brief is nu wél gecontroleerd: een topologische component-
  check (gedeelde OSM-nodes) op het VOLLEDIGE landelijke pijpleidingnet is sterker bewijs dan een lokale
  bbox-scan, want hij sluit uit dat de twee punten via een omweg buiten het venster alsnog verbonden zijn.
