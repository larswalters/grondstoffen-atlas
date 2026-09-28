# Routebrief (licht) · gas — Ras Laffan (Qatar) → Sodegaura (Japan)

**stroom-id:** `gas-raslaffan-chiba` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 2) ·
**status:** gebakken
**Keten in één zin:** Aardgas uit het North Field (gedeeld met Iran/South Pars) komt via een offshore
verzamelleiding aan land bij Ras Laffan, wordt er tot LNG verwerkt (QatarEnergy LNG) en vaart als LNG-tanker
via de Straat van Hormuz en de Straat Malakka naar de Sodegaura LNG-terminal (JERA) in Tokiobaai, waar het
hervergast en direct het Kanto-gasnet/de JERA-centrale in gaat.
**Welke as van het verhaal:** *het scherpste Hormuz-only-verhaal van de atlas* — anders dan olie heeft Qatar's
LNG-export geen Yanbu/Fujairah-achtige omleidingspijp: 100% van de export moet door één zeestraat. Ras Laffan
is 's werelds grootste LNG-complex (~77 Mtpa huidige liquefactiecapaciteit, oplopend naar >126 Mtpa na de
North Field East/South-uitbreiding, peiljaar 2025–2027) [8][9][11]; Japan is decennialang wereldwijd #1/#2
LNG-importeur, maar het exacte Ras Laffan→Sodegaura-cargovolume is niet los gebrond (§7).

## 1 · Ketenkaart
```
North Field (offshore gasveld, >6.000 km², gedeeld met Iran) ── stoppunt: geen site-anker (§7) ──
   (b1 leiding · offshore subsea trunkline (gathering) · ~80 km, stippel)──►
   Ras Laffan LNG-laadkade `gas-raslaffan-kade` (QatarEnergy LNG)
   ──(b2 zee · Perzische Golf → Straat van Hormuz → Arabische Zee → Straat Malakka/Singapore →
       Zuid-Chinese Zee → Straat Taiwan → Oost-Chinese Zee · ~11.500 km, MARNET, lange haven-aanloop)──►
   Sodegaura LNG-terminal `gas-sodegaura-term` (JERA, Tokiobaai)
   ──(b3 leiding · korte terreinleiding naar het Kanto-gasnet/de JERA-centrale · <5 km, stippel)──►
   stoppunt: invoedingspunt Kanto-gasnet/JERA-centrale
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | North Field (offshore) → Ras Laffan-kade | offshore verzamelleiding (subsea gathering) | ~80 (ontwerp-indicatie) | stippel (rechte lijn) | ja — subsea trunkline, niet in de Geofabrik-landextracts en niet als OSM-way gekarteerd [ontwerp; bevestigd door haalbaarheidstoets] |
| b2 | B | zee | Ras Laffan-kade → Sodegaura-terminal | Golf → Hormuz → Arabische Zee → Malakka/Singapore → Zuid-Chinese Zee → Taiwan-straat → Oost-Chinese Zee | ~11.000–12.000 (ontwerp-indicatie) | MARNET (kade → kade) | nee, maar met **lange haven-aanloop** aan de Qatar-kant (§7) |
| b3 | C | leiding | Sodegaura-terminal → Kanto-net/centrale | korte terreinleiding, zelfde terrein als de terminal | < 5 | stippel | ja — last mile op eigen terrein, geen net op deze korrel; niet gekarteerd in OSM |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-raslaffan-kade` | overslag leiding→zee / LNG-laadkade | Ras Laffan LNG-laadsteiger (QatarEnergy LNG-complex) | 25.9265, 51.5955 | [1][7][12] | bron-gelegd (z16 gezien: kade-eiland/laadperron met 2 opslagtanks en een leidingtracé, verbonden via twee lange trestle-toegangswegen met het vasteland-complex; ligt tussen twee vergelijkbare naburige laadsteigers in hetzelfde havenbekken van het QatarEnergy LNG-complex) |
| `gas-sodegaura-term` | losplek zee/leiding, regas-terminal + invoeding (JERA) | Sodegaura LNG-terminal & gascentrale (JERA), Tokiobaai | 35.4675, 139.9700 | [5][6][10][12] | bron-gelegd (z15 gezien: tankenpark met ~8 grote cilindrische/bolvormige LNG-tanks op het schiereiland-terrein, twee aanlegsteigers met laadarmen richting de baai, direct grenzend aan het gascentrale-complex — matcht het JERA/Sodegaura-industriegebied) |

## 4 · Via-punten
Geen — beide landbenen (b1, b3) zijn korte, ongekarteerde stippel-verbindingen zonder corridorkeuze; het
zeebeen (b2) routeert kade → kade over MARNET.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ras Laffan LNG-complex | QatarEnergy LNG | pijpleidinggas (North Field) → LNG | ~77 Mtpa huidig, >126 Mtpa na uitbreiding (2025–2027) ≈ 104,7–171,4 bcm/j (1 Mt LNG ≈ 1,36 bcm) | [8][9][11] |
| Sodegaura LNG-terminal + centrale | JERA | LNG → hervergast pijpleidinggas → net/centrale | niet in deze brief gebrond (§7) | [5][10] |

## 6 · Stoppunt
De brief stopt bij het invoedingspunt van de Sodegaura-terminal in het Kanto-gasnet/de JERA-centrale: geen
bron koppelt één specifieke Ras Laffan-lading aan één Japanse ontvangsthaven — Japan neemt structureel een
groot deel van Qatar's LNG af, maar dat cijfer is een aggregaat over heel Qatar's export, niet cargo- of
terminalspecifiek (zelfde klasse als het "Japan 30%"-cijfer bij de olie-brief Habshan-Chiba). Fase D/E
(gas vanaf de centrale/het net verder) vervallen: geen bron benoemt een specifieke fabriek stroomafwaarts.

## 7 · Open punten
- **Geen site-anker voor het beginpunt van fase A.** North Field/South Pars is een offshore gasveld van
  >6.000 km², gedeeld met Iran, zonder kade of installatie op één punt (referentiecoördinaat van het veld
  als geheel: 26,6191/52,0685 [3] — dit is een veldcentroïde, geen anker). Fase A begint daarom in algemene
  zin "in het veld" en eindigt gemeten op het Ras Laffan-kade-anker.
- **Ras Laffan-kade ligt 41,5 km van de dichtstbijzijnde MARNET-zeeknoop** (zeeknoop 4090, 26,30000/51,60000
  — gemeten met `hecht_marnet.marnet_zee`), ruim boven zowel de 5 km- als de 25 km-snapgrens. Dit is nog
  verder dan de haalbaarheidstoets' proxy-schatting (49,6 km vanaf de industriegebied-centroïde) al aangaf,
  omdat het satelliet-gelegde site-anker dichter bij zee ligt maar het net zelf nog steeds niet reikt.
  **Reken bij het bakken op een forse haven-aanloop** (`maak_havenaanloop.py`, mogelijk traag/vastlopend
  zoals het Hamburg-precedent van ~20 min) **met een rechte-stippel-terugval klaar** (bakhandleiding §2).
- **Sodegaura-terminal ligt 1,6 km van de dichtstbijzijnde zeeknoop** (zeeknoop 9067, 35,48190/139,97200) —
  ruim binnen de 5 km-grens, geen haven-aanloop nodig aan de Japanse kant.
- **Fase A (offshore trunkline) is subsea en niet gekarteerd** in de Geofabrik-landextracts of als
  getraceerde OSM-way (`man_made=pipeline`) — stippel is de bevestigde uitkomst, geen zoekactie meer nodig.
- **Fase C (terreinleiding Sodegaura-terminal → Kanto-net/centrale) is aangenomen, niet gemeten** — de
  terminal en de JERA-centrale liggen op hetzelfde omheinde terrein (zie satellietbeeld), dus < 5 km is een
  redelijke aanname, geen gepubliceerde leidinglengte gevonden.
- **Exact Ras Laffan→Sodegaura-cargovolume niet gebrond** — alleen Qatar-totaal (§0) en Japan-totaal-import
  bekend; geen bron koppelt een specifiek volume aan deze ene as.
- **Risico, nieuw t.o.v. het ontwerp — twee gebeurtenissen bij Ras Laffan zelf in 2026, niet alleen Hormuz:**
  (1) op **18 maart 2026** (tijdens de 2026 Iran-oorlog) raakte een Iraanse raket Ras Laffan; 2 van de 14
  productie-units raakten beschadigd, wat de LNG-productiecapaciteit met **17%** verlaagde, met een geschatte
  **3–5 jaar** hersteltijd en ~$20 mrd/jaar aan gederfde inkomsten volgens QatarEnergy [1]. (2) op
  **21 juni 2026** vond een explosie plaats bij de Barzan-gasfabriek binnen Ras Laffan Industrial City
  (13 doden, 66 gewonden, oorzaak "technisch ongeval", geen sabotage volgens QatarEnergy/de Qatarese
  autoriteiten; Barzan produceert geen LNG maar leveringsgas voor lokale industrie/energie) [1][2]. Beide
  horen naast het structurele Hormuz-verhaal in de risicoparagraaf van deze as.

## 8 · Bronnen
[1] Wikipedia, "Ras Laffan Industrial City" — coördinaat 25,8575/51,53889, 's werelds grootste kunstmatige
    haven (4.500 ha) en grootste LNG-exportfaciliteit; 2026 Iran-oorlogschade (18-3-2026, −17% capaciteit,
    3–5 jaar herstel, ~$20 mrd/j) en de Barzan-explosie (21-6-2026). https://en.wikipedia.org/wiki/Ras_Laffan_Industrial_City
[2] Wikipedia, "2026 Ras Laffan explosion" — Barzan-gasfabriek, 13 doden/66 gewonden, technisch ongeval, geen
    sabotage, geen impact op exportcapaciteit. https://en.wikipedia.org/wiki/2026_Ras_Laffan_explosion
[3] Wikipedia, "South Pars/North Dome Gas-Condensate field" — 's werelds grootste gasveld, >6.000 km²,
    referentiecoördinaat 26,6191/52,0685, Qatar-productie ~18,5 bcf/d (520 mln m³/d) begin 2026.
    https://en.wikipedia.org/wiki/South_Pars/North_Dome_Gas-Condensate_field
[4] Wikipedia, "QatarEnergy" — staatsbedrijf, alle olie/gas-activiteiten Qatar. https://en.wikipedia.org/wiki/QatarEnergy
[5] Wikipedia, "Sodegaura" — stad in Chiba-prefectuur, kustlijn 28,7 km aan Tokiobaai, petrochemisch complex
    op opgespoten land. https://en.wikipedia.org/wiki/Sodegaura
[6] OpenStreetMap/Photon (ODbL) — landuse "袖ヶ浦火力発電所" (Sodegaura Thermal Power Station, JERA),
    35,4624/139,9768. https://www.openstreetmap.org
[7] OpenStreetMap/Photon (ODbL) — "Port Gate 2", Ras Laffan-havenpoort, 25,9154/51,5799. https://www.openstreetmap.org
[8] QatarEnergy, officiële website — North Field-uitbreiding/LNG-capaciteit. https://www.qatarenergy.qa
[9] IEA, Global LNG Capacity Tracker — liquefactiecapaciteit per terminal/land. https://www.iea.org/data-and-statistics/data-tools/global-lng-capacity-tracker
[10] JERA, officiële website — Sodegaura-centrale/LNG-terminal, operator. https://www.jera.co.jp/en
[11] IGU, World LNG Report — jaarlijkse liquefactiecapaciteitscijfers (peiljaar 2025–2027), zoals aangehaald
    in het ketenontwerp en `v2/design/gas.md`.
[12] Esri World Imagery via `v2/tools/sat_check.py` (z13–z16) — `sat-gas-raslaffan-chiba-port-overview.png`,
    `sat-gas-raslaffan-chiba-harbor-wide.png`, `sat-gas-raslaffan-chiba-lng-pier2.png`,
    `sat-gas-raslaffan-chiba-sodegaura-wide.png`.
[13] Geofabrik OSM-extracts — `gcc-staten-latest.osm.pbf`, `japan-latest.osm.pbf` (`v2/build-cache/geofabrik/`).

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 2)

**Stroom `gas-raslaffan-chiba`** → `v2/data/stroomroute-gas-raslaffan-chiba.json` — 4 benen,
**12.388,5 km**, 1.282 punten, 2 markers. leiding 84,7 (stippel) + zee 41,6 (stippel) + zee 12.261,8 + leiding
0,4 (stippel) km. Recept: `bak_stromen.sh` (functie `bak_gas_raslaffan_chiba`).

**b1 (leiding, stippel, geen site-anker aan de kop, §7):** rechte lijn tussen het schematische veldpunt
26,6191/51,9500 (Wikipedia-referentiecoördinaat van het North Field, lon aangepast naar het Qatarese deel —
niet 52,0685 dat richting Iran ligt) en het `gas-raslaffan-kade`-anker: **84,7 km** tegen de ~80 km
ontwerp-indicatie uit de brief = **+5,9%**, ruim binnen ±15%; de brief noemt deze km-toets zelf al zwak (geen
harde bron), dus geen alarm.

**b2a (zee, stippel-geojson, haven-aanloop Ras Laffan, verplicht — LAR-586):** Ras Laffan-kade ligt 41,5 km
van de dichtstbijzijnde MARNET-zeeknoop (zeeknoop 4090, 26,30000/51,60000 — gemeten met
`hecht_marnet.marnet_zee`), ver boven zowel de 5 als de 25 km-norm. `maak_havenaanloop.py --van
25.9265,51.5955 --naar 26.30000,51.60000` **SLAAGDE** op de eerste getoetste trap (cel 0,02° gebufferd) —
**41,6 km · 20 punten · 0,00 km over land**, omwegfactor 1,002 tegen de rechte lijn (41,5 km). Geen terugval
naar een rechte stippel nodig, ondanks de vrees in de brief voor een traag/vastlopend Hamburg-precedent (de
run duurde hier ~4 min, ruim binnen de `timeout 300`).

**b2b (zee, MARNET, geen aanloop nodig aan de Sodegaura-kant):** `--been "zee|...|26.30000,51.60000|
35.4675,139.9700"` — snap Ras Laffan-zeeknoop **0,000 km** (sluit exact aan op het einde van de aanloop-
geojson), snap Sodegaura-terminal **1,611 km** (ruim onder de 5 km-norm, dus geen tweede haven-aanloop nodig
aan de Japanse kant, zoals de brief al voorspelde: 1,61 km tot zeeknoop 9067). Resultaat **12.261,8 km over
1.258 punten (61 MARNET-edges)** tegen de indicatieve ~11.000–12.000 km uit de brief = **+2,2% boven de
bovengrens / +6,6% boven het midden**, binnen ±15%; de brief noemt dit cijfer zelf al een zwakke
ontwerp-indicatie (net als bij olie-Habshan-Chiba) — de afwijking is eerder een correctie van de schatting
dan een routefout. Lengte-invariant: getekende lijn 12.261,829 km vs som edge-km 12.262,000 km = −0,171 km
(de naden). Route loopt zoals verwacht via Hormuz + Straat Malakka/Singapore, **geen Kaap-omweg**.

**b3 (leiding, stippel, last mile, kop en staart vrijwel samen):** de terminal en het JERA-centraleterrein
liggen op hetzelfde omheinde terrein, dus i.p.v. een nul-lengte-stippel is de staart een punt ~1 km
landinwaarts op het centraleterrein (35,4650/139,9670, zichtbaar op
`sat-gas-raslaffan-chiba-sodegaura-wide.png`) — **0,4 km**, tegen de aanname "< 5 km" uit de brief (geen
gepubliceerde leidinglengte, §7).

**Toets naden:** b1→b2a **0,000 km** · b2a→b2b **0,000 km** (de aanloop-geojson eindigt exact op de
zeeknoop-coördinaat waar het hoofdzeebeen begint) · b2b→b3 **1,611 km** (anker ≠ routeerpunt — het zeebeen
snapt op de Sodegaura-zeeknoop, 1,611 km van het terminal-anker; binnen de norm van ≤5 km, geen haven-aanloop
nodig). Geen enkele naad boven de 5 km-norm.

**`toets_knikken.py`:** 3 knikken ≥60°, **0 omkeringen ≥150°** (dus ook 0 terugloop) — alle drie op het
zeebeen (79,2° bij 35,36610/139,68570 · 64,4° bij 35,23890/139,79280 · 62,3° bij 24,57220/123,41820), krappe
bochten op de MARNET-route bij de nadering van Tokiobaai en de Straat Taiwan, geen fout.

**`toets_rechte_benen.py --min-km 5`:** b1 (84,7 km) en b2a (41,6 km) komen in de uitslag, maar allebei
gemarkeerd **"(stippel)"** — precies zoals het hoort: een recht been mag alleen als stippel met reden
voorkomen, en dat is hier het geval (offshore trunkline resp. haven-aanloop).

**json geldig:** versie 2, punt_formaat lonlat, modaliteiten uitsluitend {leiding, zee} (binnen de toegestane
set), elk been ≥2 punten (minimum 2), bestandsgrootte **23,5 KB** (ruim < 300 KB-richtwaarde).

**Markers:** gas-raslaffan-kade 0,0001 km (op de lijn) · gas-sodegaura-term 0,0001 km (op de lijn) — beide
ruim binnen ~0,5 km.

**Gereedschapslessen:** de veronderstelde "trage/vastlopende" haven-aanloop bij Ras Laffan (het
Hamburg-precedent van de brief) bleek in de praktijk snel te slagen op de eerste getoetste trap — de vrees in
§7 van de brief was terecht als voorzorg, maar niet als uitkomst; niet elke >25 km-snap is een tijdrovende
zoektocht.
