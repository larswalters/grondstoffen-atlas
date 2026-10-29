# Routebrief (licht) · Gas · Point Fortin (Trinidad) → Panamakanaal → Quintero (Chili)

**stroom-id:** `gas-pointfortin-quintero` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) ·
**status:** gebakken
**Keten in één zin:** Trinidadiaans LNG, vloeibaar gemaakt bij Atlantic LNG (Point Fortin), per **LNG-tanker** de Golf van Paria uit
(Drakenmond), over de Caribische Zee door het **Panamakanaal** en langs de Pacifische kust naar de regasterminal **GNL Quintero**
(Chili), waar het weer pijpleidinggas wordt. Eén zeebeen met twee haven-aanlopen; geen landbenen.
**Welke as van het verhaal:** *Reserve-as Caribisch bekken → Pacifische kust van Chili.* Trinidad is een van de twee grote LNG-herkomsten
van Chili (naast de VS) [3][7][8]. Volume van deze ene lading is niet gebrond; context in §5 (Quintero 2025 ≈ 1,16 Mt ≈ 1,6 bcm/j, zwak [8]).

## 1 · Ketenkaart
```
Atlantic LNG, Point Fortin `gas-pointfortin-kade`
   ──(b1 zee · haven-aanloop over water, stippel · ~28,7 km)──► zeeknoop 8416 (Golf van Paria, 10.2933,-61.5289)
   ──(b2 zee · Golf van Paria → Drakenmond → Caribische Zee → Panamakanaal → Pacifische kust · 7.186,3 km, MARNET)──►
   zeeknoop 486 (-33.0,-72.0)
   ──(b3 zee · haven-aanloop over water, gemeten · ~57,0 km)──► GNL Quintero, pierkop `gas-quintero-kade` ── stoppunt
```
(Bij Panama-congestie of bij een andere bestemming: omweg via Straat van Magellan/Kaap Hoorn, substantieel langer; alleen tekst, geen aparte as.)

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Point Fortin-jetty → zeeknoop 8416 | haven-aanloop, Golf van Paria (watervia-punt 10.2800,-61.7000) | 28,7 [gemeten, rechte stippel via watervia-punt] | geojson `gas-pointfortin-quintero-aanloop-pointfortin.geojson` | ja: kade 21,8 km van de zeeknoop (> 5 km); `maak_havenaanloop` hing > 300 s |
| b2 | B | zee | zeeknoop 8416 → zeeknoop 486 | Golf van Paria → Drakenmond → Panamakanaal → Pacific, aannemelijk: bestemming wisselt per maand | 7.186,3 MARNET; geen gepubliceerde lengte, ontwerpindicatie 6.000-8.000 (schatting) | MARNET | nee |
| b3 | B | zee | zeeknoop 486 → Quintero-pierkop | haven-aanloop, Bahía de Quintero (richting knoop → kade) | 57,0 [gemeten] | `maak_havenaanloop.py` gelukt (cel 0,005° kaal, 51 pt, 0 km land, omweg 1,08) | ja: kade 52,7 km van de zeeknoop (> 25 km max-snap) |

Fase A (offshore gasvelden Trinidad → Point Fortin) **vervalt**: offshore leidingnet, geen gebronde OSM-leiding of enkelvoudig anker. Fase C (regas Quintero →
Chileens net, o.a. GasAndes) wordt niet getekend: de terminal is zelf het knooppunt LNG → pijpleidinggas.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-pointfortin-kade` | liquefactie → zee (laadjetty) | Atlantic LNG, Point Fortin, Trinidad | 10.1910, -61.6986 | [1][2][9] | bron-gelegd (z16 gezien: LNG-tanker afgemeerd aan de kop van een jetty-trestle die ~1 km de Golf van Paria in loopt; tankenpark en trains op het terrein erachter, tweede jetty westelijk) |
| `gas-quintero-kade` | zee → regas (losjetty, pierkop) | Terminal GNL Quintero, Bahía de Quintero (OSM way 216250920) | -32.7665, -71.5094 | [3][4][9][10] | bron-gelegd (z16 gezien: lange pier vanaf het strand met laadplatform en afmeerpalen aan de kop; bij opname geen tanker aan de kade, wel twee ankerliggers; tankenpark op het terrein bij -32.7787,-71.4895) |
Hergebruik: sitelaag `w-atlanticlng` (10.1839,-61.6936) is de fabriekscentroïde, 0,9 km van de jetty; de jetty is het overslaganker. Geen bestaand Chili-anker voor GNL Quintero
(Puerto Ventanas -32.7540,-71.4789 in `koper-elteniente-rotterdam` is een ander bedrijf/pier).

## 4 · Via-punten
Geen landbenen. Watervia-punten alleen in de aanloop: b1 10.2800,-61.7000 (noord van de jetty over open water van de Golf, daarna oost naar zeeknoop 8416;
getoetst tegen `ne_10m_land`: 0,0 km land, rechte lijn kade → knoop zou 4,3 km over land gaan). b3 volgt het gemeten waterpad.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Atlantic LNG, Point Fortin | Shell 51-57,5 %, BP 37,8-42,5 %, NGC (trein 1 en 4) | aardgas → LNG | 14,8 Mtpa nameplate (≈ 20,1 bcm/j; 1 Mt ≈ 1,36 bcm), 4 treinen, 524.000 m³ opslag; trein 1 definitief stilgelegd (maart 2025); sitelaag 20,4 bcm/j. Feitelijke doorzet lager (feedgastekort) | [1][2] |
| GNL Quintero | Fluxys + EIG 80 %, ENAP 20 % | LNG → pijpleidinggas + tankwagens | 15 Mm³/dag regas, 334.000 m³ opslag; 2024 benutting 21,8 %; 2025 ≈ 1,16 Mt ontvangen (≈ 1,6 bcm/j, zwak) | [3][7][8] |
Contractlijn: BG (nu Shell) levert tot 1,7 Mtpa (≈ 2,3 bcm/j) aan Quintero tot 2030 [4][5]; de 500e lading (jan 2023) kwam uit Trinidad op een Shell-gecharterde carrier [3].

## 6 · Stoppunt
De brief stopt bij de pierkop van GNL Quintero, waar LNG weer gas wordt en het Chileense net in gaat. Geen bron koppelt een lading aan één eindgebruiker; fase D/E vervallen.

## 7 · Open punten
- **Bestemming wisselt:** Trinidad-ladingen gaan ook naar Europa/VS; Quintero krijgt ook QCLNG- en VS-ladingen. Eén bron voor "Point Fortin → Quintero als regelmatige lading" (Shell-charter 500e lading [3]; Chili-herkomst T&T ongeveer de helft volgens een niet-geopende zoekresultaatsamenvatting [9]): daarom **aannemelijk, één bron** in de beennaam.
- **Volume van deze lading niet gevonden.** Trinidad-aandeel per jaar zit in een niet-leesbare grafiek van [7]; 2025-cijfers komen uit een LinkedIn-profiel dat GIIGNL citeert (zwak [8]).
- **Contractvolume:** het ontwerp noemde "BG/Shell 3 Mtpa 2009-2030" (tweedehands zoekresultaat); gebrond is 1,7 Mtpa tot 2030 [4][5]. 3 Mtpa niet bevestigd.
- **b2-lengte** is een MARNET-meting (7.186 km), geen gepubliceerde ladingroute; de ±15 %-toets is hier een indicatie (ontwerpindicatie 6.000-8.000 km).
- **Panamakanaal 2026:** droogtebeperkingen en LNG-slotschaarste, zie `gas-corpuschristi-incheon` §7 [7][8][9] daar; deze keten gebruikt dezelfde sluisroute.
- **Piergeometrie:** OSM/satelliet geven ~1,8 km pier, een bron uit 2007 noemt 1.300 m kade [4]; kop op beeld, lengteverschil niet uitgezocht.
- **b1-aanloop:** de stippel loopt eerst noord naar het watervia-punt en dan oost naar knoop 8416 voordat MARNET weer noordwest keert (V-vormige omweg ~17 km). Alternatief getoetst (0 km land): kade → zeeknoop 8414 (10.6313,-61.8036, 50,2 km), die al op de MARNET-route ligt. Niet toegepast omdat de toets bindend 8416 voorschreef.

## 8 · Bronnen
[1] Wikipedia, "Atlantic LNG" (4 treinen, 14,8 Mtpa, eigenaren, opslag 524.000 m³, trein 1 sluiting maart 2025). https://en.wikipedia.org/wiki/Atlantic_LNG
[2] LNG Prime, 11-04-2022, Atlantic LNG 4500e lading (Cool Discoverer; terminal ≈ 15 Mtpa; markten Europa, VS, Zuid-Amerika, Azië, Caraïben). https://lngprime.com/americas/trinidads-atlantic-lng-ships-4500th-cargo/48197
[3] LNG Prime, 07-02-2023, Quintero 500e lading uit Trinidad (Malaga Knutsen, Shell-charter; Fluxys/EIG 80 %, ENAP 20 %; 2 tanks tot 160.000 m³ + 1 kleine; 4 verdampers). https://lngprime.com/?p=72993
[4] Offshore Technology, "Quintero Bay LNG terminal" (2007: kade ± 1.300 m, tanks, regas 10-15 Mm³/dag, BG-contract 1,7 Mtpa/21 jaar). https://www.offshore-technology.com/projects/quniterobay/
[5] Hydrocarbon Processing, 04-2012, BG verkoopt 40 % aan Enagas (leveringscontract tot 1,7 Mtpa tot 2030; terminal 2,5 Mtpa). https://hydrocarbonprocessing.com/news/2012/04/bg-to-sell-40-stake-in-chile-lng-plant-to-enagas/
[6] MundoMaritimo, 27-03-2015, uitbreiding GNL Quintero naar 15 Mm³/dag; 197 schepen in 5,5 jaar. https://www.mundomaritimo.cl/noticias/gnl-quintero-inaugura-nueva-capacidad-de-suministro-de-su-terminal
[7] APERC/OGSNF, Chili olie- en gasupdate, 04-2025 (Quintero opslag 334.000 m³, regas 15 Mm³/dag, benutting 2024 21,8 %; Chili-gasimport 2019-2023). https://aperc.or.jp/file/2025/7/3/1315-1325_Chile_O_and_G_updates_OGSNF_2025.pdf
[8] LinkedIn-profiel (citeert GIIGNL/IGU, zwak): Chili 2025 LNG 1,9-2,19 Mt, Quintero ≈ 1,16 Mt, Mejillones 0,50 Mt; herkomst Trinidad en VS. https://cl.linkedin.com/in/pablo-mercado-schultz-73155956
[9] Datasur (D-Comex; alleen zoekresultaatsamenvatting, pagina niet geopend): Trinidad 50,07 %, VS 48,26 % van Chili-import, periode onbekend. https://www.datasur.com/?p=31176
[10] OpenStreetMap (ODbL): way 216250920 "Terminal GNL Quintero" (pier, kop -32.7666,-71.5095, wal -32.7761,-71.4935); landuse GNL Quintero way 1279095136 (-32.7787,-71.4895). https://www.openstreetmap.org/way/216250920
[11] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-gas-pointfortin-quintero-pf-jetty.png`, `-pf-overzicht.png`, `-quintero-pier.png`, `-quintero-overzicht.png`, `-gnlq.png`.
[12] `gas-corpuschristi-incheon` §7 (Panamakanaal 2026), eerder in dit project. Toetsmeting MARNET en `ne_10m_land` (2026-10-29): zeeknopen 8416 en 486, route 7.186,3 km, aanloop Quintero gemeten 57,0 km.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)

**Bestand:** `v2/data/stroomroute-gas-pointfortin-quintero.json` (15,4 KB, contract versie 2, lonlat) · **recept:** `bak_gas_pointfortin_quintero()` in `v2/tools/bak_stromen.sh`
· **titel:** "Gas · Point Fortin → Quintero". Geen profiel in `maak_stroombeen_weg.py` (geen landbenen), geen extract, geen nieuwe tussenuitvoer.

| # | modaliteit | been | km | punten | naad |
|---|---|---|---|---|---|
| 1 | zee, stippel | haven-aanloop Point Fortin (kade → watervia-punt 10.2800,-61.7000 → zeeknoop 8416) | 28,7 | 3 | 0,00 |
| 2 | zee, doorgetrokken | LNG-tanker zeeknoop 8416 → zeeknoop 486 (aannemelijk: bestemming wisselt) | 7186,3 | 736 | 0,00 |
| 3 | zee, stippel | haven-aanloop Quintero (zeeknoop 486 → pierkop, gemeten waterpad) | 57,0 | 51 | 0,00 |

Totaal 7272,0 km · 790 punten · 2 markers (`gas-pointfortin-kade`, `gas-quintero-kade`, beide 0,0 km van de lijn). Maximale naad 0,00 km.

**Recept:** (1) `--stippel-geojson` met het bestaande `gas-pointfortin-quintero-aanloop-pointfortin.geojson`; (2) `--been "zee|…|10.2933,-61.5289|-33.0,-72.0"` over MARNET (32 edges, snap 0,000 beide kanten);
(3) `--stippel-geojson` met `gas-pointfortin-quintero-aanloop-quintero.geojson`. Beide aanloopbestanden waren al aanwezig en zijn ongewijzigd hergebruikt; niets opnieuw gerekend.

**Toelichting stippels:** beide stippels zijn haven-aanlopen (kade 21,8 km resp. 52,7 km van de MARNET-zeeknoop, dus > 5 km): "hier reikt het net niet". De Quintero-aanloop is een gemeten kortste pad over water (0 km land);
de Point Fortin-aanloop is rechte stukken via het watervia-punt omdat `maak_havenaanloop.py` > 300 s hing. b2 blijft doorgetrokken: de onzekerheid (één bron voor de bestemming) staat in de beennaam, niet in de lijnstijl.

**Toets:** b2 7186,3 km tegen de ontwerpindicatie 6.000-8.000 km (geen gepubliceerde ladingroute; indicatie, geen +/-15%-norm). Geen echte wegkm van toepassing. `toets_knikken.py`: 3 knikken >= 60 graden (80,3 graden bij 9.7500,-80.0000 en 71,8 graden bij 9.1183,-79.8032 in de Panama-doorgang;
73,2 graden bij 10.8453,-61.8171 bij de uitgang van de Golf van Paria), 0 omkeringen, 0 terugloop: kanaal- en kustbochten in MARNET, geen reparatie nodig. `toets_rechte_benen.py`: geen melding voor dit bestand.
json.load slaagt, versie 2, punt_formaat lonlat, modaliteiten {zee}, elk been >= 2 punten.

**Bevindingen:** (a) de Point Fortin-aanloop maakt een V-omweg van ca 17 km (eerst noord naar het watervia-punt, dan oost naar knoop 8416, daarna keert MARNET noordwest); het getoetste alternatief kade → zeeknoop 8414 (10.6313,-61.8036, 50,2 km) is niet toegepast omdat de opdracht 8416 voorschreef en staat open voor een eventuele herbak.
(b) De 25 km-snap van de Quintero-kade (52,7 km) is opgelost met de aanloop, naad 0. (c) Het id noemt Quintero en de lijn eindigt op de pierkop van GNL Quintero: id en eindpunt kloppen.

**Lessen:** een aanloop die in een eerdere sessie al gemaakt is (en een volledige FeatureCollection levert) kan zonder nieuwe `maak_havenaanloop`-poging worden hergebruikt; controleer eerst `ls build-cache/ais/graaf/<stroom-id>-*`. Tijdens de bake las bash `bak_stromen.sh` terwijl een andere agent er een functie in schreef
(regel 12112: "er/smelter: No such file", zonder gevolg voor deze stroom: json en console waren compleet); bij parallelle golven daarom na de bake de uitvoer controleren in plaats van de exitcode te geloven.

**Registerregel:** `{ "sleutel": "gas-pq", "bestand": "stroomroute-gas-pointfortin-quintero.json", "grondstof": "gas", "label": "Point Fortin → Quintero", "aan": true, "noot": "M31 · golf 12 (2026-10-29): Trinidadiaans LNG per tanker door het Panamakanaal naar GNL Quintero (Chili), één zeebeen met twee haven-aanlopen" }`
