# Routebrief (licht) · Nikkel · Onça Puma → Estrada de Ferro Carajás → São Luís (Brazilië)

**stroom-id:** `nikkel-oncapuma-saoluis` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** Braziliaanse ferronikkel (~40 kt Ni/j nameplate) van Vale's Onça Puma-smelter
(Ourilândia do Norte, Pará) per **truck** naar het spoorwegstation van Parauapebas en per **spoor**
(Estrada de Ferro Carajás, containerwagons) naar de openbare bulkhaven Porto do Itaqui in São Luís
(Maranhão) — stoppunt, geen gedocumenteerde afnemer na de haven.
**Welke as van het verhaal:** de enige nikkeloperatie van Vale in Brazilië, en het enige gedocumenteerde
gebruik van de Carajás-spoorlijn voor een niet-ijzerertsproduct (speciaal aangepaste containerwagons).
40 kt Ni/j nameplate na opstart Forno 2 (2025) [3]; eerste geregistreerde zending 1.078 t ferronikkel
(385 t Ni-inhoud) [1].

## 1 · Ketenkaart
```
Onça Puma-smelter `ni-oncapuma-smelter` ──(b1 truck · hemelsbreed ~147 km, geen wegcorridor
    geverifieerd)──► Parauapebas-station `ni-parauapebas-efc` ──(b2 spoor · Estrada de Ferro
    Carajás (EFC/EF-315), containerwagons · gepubliceerd ~892 km)──► Porto do Itaqui-kade
    `ni-itaqui-kade` (São Luís) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-oncapuma-smelter` → `ni-parauapebas-efc` | onbevestigd; vermoedelijk oostwaarts, mogelijk nabij Canaã dos Carajás — geen bron, geen via-punt geverifieerd deze ronde | hemelsbreed 146,9 km, geen wegkm gepubliceerd [webcheck] | maak_stroombeen_weg (bake) | nee |
| b2 | B | spoor | `ni-parauapebas-efc` → `ni-itaqui-kade` | Estrada de Ferro Carajás (EFC/EF-315), Parauapebas → Marabá → Açailândia → Santa Inês → São Luís [4] | ~892 [algemeen bekend, Wikipedia Vale S.A./Carajás Railway, niet deze ronde herbevestigd; webcheck grootcirkel 721,1 km, ratio 1,24] | toets_spoorroute (`BAKE_SUFFIX=-raw`) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-oncapuma-smelter` | mijn + smelter (ferronikkel) | Onça Puma-smelter (Vale), Ourilândia do Norte, Pará | -6.5730, -51.0900 | [2][3][6] | bron-gelegd (z15/z16 gezien: elektrische ovens met schoorsteen/rookpluim, ertsopslag, tailingsbekkens, directe wegaansluiting) |
| `ni-parauapebas-efc` | overslag weg → spoor | Spoorwegstation Parauapebas (EFC) | -5.9942, -49.8949 | [1][4][6] | aannemelijk (z15 gezien: spoorlijn met stationsgebouw bij een rivieroversteek aan de rand van Parauapebas; de exacte container-overslagplek is niet gepubliceerd — Vale noemt alleen "Parauapebas" als vertrekpunt van de aangepaste wagons [1]) |
| `ni-itaqui-kade` | losplek (haven) | Porto do Itaqui, São Luís | -2.5768, -44.3667 | [5][6] | bron-gelegd (z15 gezien: pakhuizen, tankopslag en kademuur met ligplaatsen direct aan het vaarwater; onderscheiden van Vale's eigen Ponta da Madeira-ertsterminal 3 km noordelijker) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen via-punten deze ronde: de wegcorridor b1 is niet onderzocht (geen gepubliceerde route, webbudget
besteed aan de knoop- en haven-anker). PA-279 (de doorgaande weg bij Ourilândia do Norte/Tucumã) loopt
zuidwaarts naar Xinguara en is dus **niet** de corridor naar Parauapebas [6] — de bake-agent moet de
werkelijke oostwaartse verbinding zelf vinden via een geofabrik-scan met een ruim venster (≥75 km).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Onça Puma-smelter | Vale Base Metals | lateriet-erts (eigen mijn) → ferronikkel (granulaat) | 40 kt Ni/j nameplate (na Forno 2, 2025) | [2][3] |

## 6 · Stoppunt
De brief stopt bij Porto do Itaqui: de enige gedocumenteerde zending (1.078 t ferronikkel, 52
containers over de EFC) ging naar "Azië en Europa" zonder genoemde afnemer of fabriek [1] — er is dus
geen fase D. ⚠️ Vale's eigen actuele Onça Puma-operatiepagina noemt daarnaast een andere bestemming:
"processed and granulated for transport to Barcarena, Pará, from where it is sold" [2] (Vila do
Conde-haven, Belém-regio) — mogelijk de huidige hoofdroute naast of in plaats van Itaqui. De hier
getekende Itaqui/EFC-keten is gekozen omdat dit de enige route is met concreet gedocumenteerde
infrastructuur (aangepaste containerwagons, benoemd spoortraject, benoemde haven); zie open punt.

## 7 · Open punten
- **Wegcorridor b1 onbevestigd**: geen gepubliceerde route of via-punten tussen Onça Puma-smelter en
  Parauapebas; alleen de hemelsbrede afstand (146,9 km) is bekend.
- **Exacte overslagplek Parauapebas**: Vale noemt alleen de plaatsnaam, geen terreinadres of
  containerterminal — het stationsanker is een schematische benadering.
- **Concurrerende exportroute (Barcarena/Vila do Conde)**: Vale's eigen operations-pagina wijst naar
  een kortere weg-route via Barcarena, Pará [2] — bevestigt het risico uit de haalbaarheidstoets. Niet
  uit te sluiten dat beide routes naast elkaar bestaan (verschillende ladingen/klanten); bij bake beide
  corridors (deze keten vs. een Belém/Vila do Conde-variant) vergelijken, zoals de haalbaarheidstoets
  al aangaf.
- **Afwijking van de haalbaarheidstoets**: die noemde een schematisch instappunt bij Canaã dos Carajás
  (~93 km, gemeten op het dichtstbijzijnde spoorpunt — dat bleek bij nader onderzoek de private S11D-
  ertsspoorlus, "Administração S11D - Ferro", geen publieke overslag). Dit rapport gebruikt in plaats
  daarvan Parauapebas (~147 km), rechtstreeks genoemd door Vale/IBRAM als vertrek van de containerwagons
  [1] — beter gebrond, maar verder van de smelter.
- **Geen fase D/afnemer**: bestemming "Azië en Europa", geen fabriek of koper met naam.

## 8 · Bronnen
[1] IBRAM, "Onça Puma embarca 1.078 t de ferro-níquel" — eerste zending, 52 containers via EFC, 50
    aangepaste wagons Parauapebas → Porto do Itaqui. https://ibram.org.br/noticia/onca-puma-embarca-1-078-t-de-ferro-niquel/
[2] Vale Base Metals, Onça Puma-operatiepagina — "processed and granulated for transport to Barcarena,
    Pará, from where it is sold". https://valebasemetals.com/our-operations/onca-puma/
[3] Vale, "Vale Base Metals Announces Start-Up of Furnace 2 at Onça Puma" — nameplate 40 kt Ni/j na
    Forno 2 (2025). https://vale.com/w/vale-base-metals-announces-start-up-of-furnace-2-at-onca-puma-1
[4] Wikipedia, "Carajás Railway" — EFC/EF-315, Parauapebas–São Luís, vijf stations incl. Parauapebas.
    https://en.wikipedia.org/wiki/Caraj%C3%A1s_Railway ; lengte (892 km) via Wikipedia "Vale S.A."
    https://en.wikipedia.org/wiki/Vale_S.A.
[5] Wikipedia, "Port of Itaqui" — openbare bulkhaven (EMAP), apart van Vale's private Ponta da Madeira-
    ertsterminal. https://en.wikipedia.org/wiki/Port_of_Itaqui
[6] OpenStreetMap/Nominatim (ODbL) — "Vale Onça Puma"-toegangsweg, Estação Ferroviária de Parauapebas,
    Porto do Itaqui-adrespunt, PA-279-tracé. https://www.openstreetmap.org
[7] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16) —
    `v2/build-cache/satcheck/sat-nikkel-oncapuma-saoluis-smelter.png`,
    `sat-nikkel-oncapuma-saoluis-smelter2.png`, `sat-nikkel-oncapuma-saoluis-parauapebas.png`,
    `sat-nikkel-oncapuma-saoluis-itaqui.png`.

## 9 · Bakresultaat (2026-09-28, lichte werkwijze, M31 golf 6)

**Totaal: 1.156,6 km · 4.600 punten · 3 markers · 2 benen (truck + spoor), geen zeebeen.**

| # | fase | modaliteit | km gebakken | naad | recept |
|---|---|---|---|---|---|
| b1 | A | truck | 282,6 km (3.300 pt) | — | `maak_stroombeen_weg.py --profiel nikkel-oncapuma-saoluis-smelter-parauapebas --bron geofabrik` |
| b2 | B | spoor | 874,0 km (1.300 pt) | 0,02 km | `BAKE_SUFFIX=-raw node toets_spoorroute.mjs --van=-5.9942,-49.8949 --naar=-2.5768,-44.3667 --naam=nikkel-oncapuma-saoluis-parauapebas-itaqui` |

**b1 (truck) — de wegcorridor is gevonden, niet gegokt.** Open punt 1 uit §7 ("wegcorridor
b1 onbevestigd — PA-279 loopt zuidwaarts") is opgelost via een **OSRM-routecontrole**
(router.project-osrm.org, driving; binnen het webbudget — curl, geen WebSearch): OSRM vindt
zelf één route van 289,4 km (geen kortere alternatieve route, `alternatives=true` gaf 1
resultaat) die niet rechtstreeks oostwaarts loopt maar eerst **zuidoost via Água Azul do
Norte**, dan **noordoost door Canaã dos Carajás** naar Parauapebas. Reverse-geocode
(Nominatim) van de bochtpunten bevestigde de plaatsen. OSRM routeert zelf over OSM-data en is
dus een **voorspelling** van de corridor, geen bron — de onafhankelijke scan van
`maak_stroombeen_weg.py` op de lokale `brazilie`-extract (venster 25 km om de OSRM-punten,
`corridorKlassen: ["tertiary","unclassified"]` nodig omdat de toegangsweg bij de smelter zelf
geen hoofdweg is) bevestigt de voorspelling: **282,6 km getekende lijn**, snap-afstanden alle
≤ 0,07 km (plant→weg 0,07 · weg→kade 0,05 km) — **geen last-mile-stippel nodig**. Tegen de
hemelsbreed-schatting (146,9 km) is dat **+92,4%**; de brief geeft geen gepubliceerde wegkm,
dus dit is een **bevinding**, geen toets-overtreding (werkwijze §1: de ±15%-norm geldt hier
als indicatie). De grote afwijking is verklaarbaar: een structureel dun wegennet in dit
Amazone-grensgebied (Ourilândia do Norte–Parauapebas heeft geen doorgaande oostwaartse weg;
OSRM zelf vond ook geen kortere route) — geen teken van een verkeerd gelegde via.
⚠️ Canaã dos Carajás is dezelfde plaats die de haalbaarheidstoets in open punt 5 al noemde en
verwierp als schematisch spoor-instappunt (de private S11D-ertsspoorlus) — dit been gebruikt
daar de **openbare weg**, niet dat spoor. Geen tegenspraak.

**b2 (spoor) — bevestigt de brief.** Estrada de Ferro Carajás (EF-315), Parauapebas-station →
São Luís: **873,8–874,0 km** over 229 edges (grootcirkel 721,1 km, verhouding 1,21), **0
bochten ≥ 60° na de keerstraf** (25 km, `BAKE_SUFFIX=-raw`, 3.260.717 spoor-edges bevestigd in
de consoleregel). Tegen de brief se ~892 km (algemeen bekend, Wikipedia Vale S.A./Carajás
Railway, niet deze ronde herbevestigd): **−2,1%**, ruim binnen de ±15%-norm. Snap 0,02/0,31 km
— geen `--via` nodig, één doorgaande hoofdlijn (enkelsporig hoofdtraject), geen omweg
gevonden door de router.

**Geen zeebeen, geen haven-aanloop.** Beide ankers (Onça Puma-smelter, Parauapebas-station)
zijn landankers; het spoorbeen eindigt zelf al op 0,31 km van het Itaqui-kade-anker. De brief
stopt bewust bij Porto do Itaqui (§6) — geen fase D/E, geen gedocumenteerde afnemer na de
haven.

**Toets (§5 bakhandleiding): geslaagd.**
- Naden: 0,00 km (leg 1, eerste been) en 0,02 km (leg 2 op leg 1) — geen naad > 5 km.
- Markers: `ni-oncapuma-smelter` 0,0 m · `ni-parauapebas-efc` 0,0 m · `ni-itaqui-kade` 314,5 m
  (anker ≈ routeerpunt — de kade-marker ligt op het bron-gelegde kadepunt, de spoorlijn snapt
  op de dichtstbijzijnde hoofdnet-knoop; ruim binnen de norm).
- `toets_knikken.py`: truck 32 knikken/0 omkeringen (alle "spike" = kleine OSM-bochtjes op
  residential/tertiary-klasse, geen omkering); spoor 0 knikken/0 omkeringen.
- `toets_rechte_benen.py --min-km 5`: omwegfactor truck 1,923 · spoor 1,212 — geen been op
  1,000 (geen verdachte rechte lijn).
- JSON-contract: `json.load` slaagt, `versie == 2`, `punt_formaat == "lonlat"`, modaliteiten
  `{truck, spoor}` ⊂ toegestane set, elk been ≥ 2 punten, bestand 92,0 KB.

**Lessen voor latere bak-agenten:**
- Bij een niet-gepubliceerde/onbevestigde wegcorridor is een OSRM-routecontrole (curl, geen
  WebSearch, geen bron in de brief-zin — alleen een voorspelling) een goedkope manier om een
  blinde 75-100 km-vensterscan te vervangen door een gerichte 20-30 km-scan op de echte
  bochtpunten. De onafhankelijke OSM-scan bevestigde de OSRM-voorspelling op 2,4% (282,6 vs
  289,4 km) — dat verschil is precies waarom de scan zelf nog nodig is en OSRM niet als bron
  volstaat.
- Een hemelsbrede schatting die met +92% wordt overtroffen door de gemeten wegkm is geen
  gefaalde toets zolang de brief geen gepubliceerde wegkm geeft (werkwijze §1) — het hoort als
  bevinding in de brief, niet als een reden om een korter (fout) tracé te zoeken.
