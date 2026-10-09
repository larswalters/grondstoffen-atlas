# Routebrief (licht) · nikkel — Raglan → Deception Bay → Québec → Sudbury (Canada)

**stroom-id:** `nikkel-raglan-sudbury` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** nikkel-koperconcentraat van de Raglan-mijn en concentrator (Glencore, Katinniq, Nunavik) per **truck** over de
grindweg Katinniq–Deception Bay naar Glencore's eigen laadkade, per **zeeschip** door de Hudsonstraat, langs Labrador en door de
Golf van Saint-Laurent naar de Glencore-terminal in de haven van Québec (seizoensvaart, ~8 reizen/jaar), dan per **spoor** (CN, via
Montréal en Toronto) naar de Glencore Sudbury Smelter — de omgekeerde richting van het spoorbeen van `nikkel-sudbury-kristiansand`.
Stoppunt Sudbury: wat de smelter verlaat (matte) staat in die andere brief.
**Welke as van het verhaal:** de Arctische Canadese nikkelketen — het enige grote nikkel-erts dat Nunavik per schip verlaat en de
feed van de Sudbury-smelter. **≈39,9 kt Ni/j** (Glencore "at a glance", cijfers 2025; peiljaar niet scherp) [2]; vervoerd als
**~240.000 t concentraat/j in ~8 reizen** [1]. Eenheid: kt Ni per jaar. (Het ontwerp van Wikipedia, 21 kt Ni/130 kt concentraat, is achterhaald [3].)

## 1 · Ketenkaart
```
Raglan-mijn/concentrator `ni-raglan-mijn` ──(b1 truck · Route Baie Déception–Katinniq, grind · ~96 OSM-km)──►
Deception Bay-kade `ni-deceptionbay-kade` ──(b2a zee-haven-aanloop, STIPPEL · ~120 km)──► MARNET-zeeknoop 471 (Hudsonstraat)
   ──(b2 zee · Hudsonstraat → Labradorzee → Belle Isle/Cabot (router) → Golf → Saint-Laurent · ~3.225 km, MARNET)──►
Québec-kade `ni-quebec-kade` ──(b3 spoor · CN Kingston Sub → Taschereau Yard → MacMillan Yard → CN Bala Sub · ~1.294 km)──►
Sudbury Smelter `ni-sudbury-smelter` ── stoppunt
```
Seizoen: de kade is ~8 maanden per jaar bereikbaar, ook met ijsbreker [3]; de lijn is een jaargemiddelde, geen continue stroom.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-raglan-mijn` → `ni-deceptionbay-kade` | Route Baie Déception–Katinniq (OSM tertiary, grind), 11 ways, geen zijtak | **hemelsbreed 73,6 km, geen wegkm**; Wikipedia ~100 km (afstand, geen routelengte) [3]; Sivumut-kaart: wegkm-posten t/m km 95 bij Katinniq [4]; OSM-ketensom 95,9 (eigen meting) [7] | maak_stroombeen_weg (`--bron overpass`) of de kant-en-klare OSM-keten (§9-aanwijzing) | nee |
| b2a | B | zee | `ni-deceptionbay-kade` → zeeknoop 471 (63.2000, -75.0000) | haven-aanloop over water | 118,3 hemelsbreed tot de knoop; `maak_havenaanloop` gaf **119,8** | maak_havenaanloop (liep 2026-10-09 binnen de timeout) | **ja** (net reikt niet; >5 km én >25 km snap) |
| b2 | B | zee | zeeknoop 471 → `ni-quebec-kade` | MARNET kiest de corridor | **3.224,8** (proefbake; geen gepubliceerde lengte) | MARNET (12 edges, snap 0,000/1,617 km) | nee |
| b3 | C | spoor | `ni-quebec-kade` → `ni-sudbury-smelter` | CN Kingston Sub + CN Bala Sub, via Taschereau Yard en MacMillan Yard | ~1.230 [webcheck uit de bestaande brief]; kopie meet **1.293,6** (+5,1%) | **letterlijke kopie, omgekeerd, van `nikkel-sudbury-kristiansand` b1** (3 geojsons) + b0 omgekeerd | alleen het slot-emplacement (0,16 km) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-raglan-mijn` | mijn + concentrator | Raglan Mine, Katinniq (Glencore) | 61.6876, -73.6750 | [2][3][4]; Wikipedia 61.6875, -73.6781 (170 m) | bron-gelegd (z16 gezien: groot industrieel complex met molengebouw, brekertoren/transportband, tailingsmeer en kampvleugels) |
| `ni-deceptionbay-kade` | overslag truck → zee | Deception Bay-kade (Glencore, pier uit 1971) | 62.1458, -74.6933 | [4][5][6][7] | bron-gelegd (z17 gezien: gevulde kadedek met laadgalerij langs de pier; ~300 m westelijk een grote koepelloods en een kampcomplex; de OSM-weg Raglan eindigt exact op deze kade) |
| `ni-quebec-kade` | overslag zee → spoor | Glencore-terminal, Port de Québec, Beauport | 46.8330, -71.2035 | hergebruikt uit `nikkel-sudbury-kristiansand` [1][8] | aannemelijk (z15 opnieuw gezien: tankenpark + steigers; welke steiger is niet te zien, Glencore noemt geen kade) |
| `ni-sudbury-smelter` | losplek / smelter | Glencore Sudbury Smelter (Falconbridge) | 46.5786, -80.7993 | hergebruikt uit `nikkel-sudbury-kristiansand` [1][8] | bron-gelegd (daar z15 gezien: smelter met schoorsteen, 6 Edison Rd) |
Zeeknoop 471 is een routeerpunt, geen anker. Nabije andere pier (zuidoost, 62.1385, -74.6845, met schuur) is vermoedelijk Nunavik Nickel/CRI [5] en is niet gekozen.

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | wegknoop OSM-ways 587588827/949525173 | 62.0987, -74.5456 | op de doorgaande weg; stabiliseert tegen service-sporen bij de haven (geen corridorkeuze, één weg) |
| b1 | 2 | wegknoop 949525174/517305879 | 62.0952, -74.3177 | idem, begin van de 64 km-lange hoofdway |
| b1 | 3 | wegknoop 517305879/1266330307 | 61.7176, -73.7173 | idem, laatste 8 km naar de concentrator |
| b3 | 4 | MacMillan Yard (CN, Vaughan) | 43.8119, -79.5111 | in de gekopieerde geometrie; trekt de route om Toronto-lakeshore |
| b3 | 5 | Taschereau Yard (CN, Montréal) | 45.4686, -73.6861 | in de gekopieerde geometrie; pint Kingston Sub door Montréal |
Alle drie wegpunten liggen op OSM-vertices (1–5 m). Geen stadscentra; niets nieuws voor het spoor.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Raglan concentrator (Katinniq) | Glencore | erts (~1,5 Mt/j) → Ni-Cu-concentraat | 39,9 kt Ni/j; ~240 kt concentraat/j | [1][2][3] |
| Sudbury Smelter | Glencore Sudbury INO | concentraat (o.a. Raglan) → matte ~60 % Ni | zie `nikkel-sudbury-kristiansand` §5 | [1] |

## 6 · Stoppunt
De brief stopt bij de Sudbury Smelter: Glencore noemt die zelf als bestemming van het Raglan-concentraat [1]; de matte-keten
daarna (Québec → Nikkelverk) is al getekend in `nikkel-sudbury-kristiansand`. Fase D/E vervalt, geen tweede bron.

## 7 · Open punten
- **Welke pier is Raglan's**: de noordpier (OSM-weg eindigt er; Sivumut-kaart toont laadleiding, loods en kamp) is gekozen; een
  bronvermelding mét coördinaat ontbreekt. De zuidoostpier is waarschijnlijk CRI (Nunavik Nickel), niet bevestigd [5].
- **Km b1 is geen bedrijfsopgave**: 95,9 is de som van de OSM-ways; "~100" van Wikipedia is een afstand. Indicatie, geen ±15%-norm.
- **Aanloop b2a is schematisch** (rechte route over het water, 120 km noordwaarts de Hudsonstraat in; de echte vaarlijn volgt een
  zuidoever); het zeebeen begint op knoop 471. Een tweede bestemming van Raglan-concentraat is niet gedocumenteerd.
- **Spoor is een kopie** met de twee bekende TERUGLOOP-omkeringen bij MacMillan Yard; geen eigen spoorrun.
- **Seizoen en reizen**: [1] noemt ~8 reizen/j, een rapport uit 2013 noemde 12 [5]; peiljaar van 39,9 kt Ni niet scherp.
- **Quebec-kade** blijft aannemelijk (zie `nikkel-sudbury-kristiansand` §7).

## 8 · Bronnen
[1] Glencore Canada, "Facilities at Port of Quebec" — ~8 reizen/j, ~240.000 t, rail naar Sudbury. https://www.glencore.ca/en/our-assets/facilities-at-port-of-quebec
[2] Glencore Canada, Raglan "At a glance" — 39,9 kt Ni (2025), wegen naar de seaport. https://www.glencore.ca/en/raglan/who-we-are/at-a-glance
[3] Wikipedia, "Raglan Mine" (61.6875, -73.6781) — ~100 km, 8 maanden open. https://en.wikipedia.org/wiki/Raglan_Mine
[4] Glencore Raglan, Sivumut ESIA-samenvatting 2017 (kaart: Deception Bay seaport, loading pipe, warehouse, wegkm-posten). https://minedocs.com/24/Reglan(Sivumut)-ProjectDescription-012017.pdf
[5] Federal Review Panel North, CRI/Nunavik Nickel Deception Bay, aanbevelingsrapport (~800 m, 12 reizen/j, bestaande Glencore Xstrata-kade). https://www.canada.ca/content/dam/iaac-acei/documents/jbnqa/deception-bay/recommendation_report_frp-north.pdf
[6] IAAC/Onemine, Deception Bay Wharf (gebouwd 1971 voor de Asbestos Hill-mijn; alleen uit zoekresultaat). https://onemine.org/documents/arctic-emergency-operation-deception-bay-rehabilitation
[7] OpenStreetMap (ODbL) via Overpass maps.mail.ru 2026-10-09 en Nominatim — ways 1266330306, 53534572, 517305877, 587588827, 587588824, 949525173, 949525174, 517305879, 587603368, 1266330307, 587605472. https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-nikkel-raglan-sudbury-{mijn-z16,deceptionbay,deceptionbay-z17,quebec-kade}.png`.
[9] Brief `nikkel-sudbury-kristiansand` — spoorgeojsons b0/b1, Québec- en Sudbury-anker, MacMillan-/Taschereau-via-punten.
[10] `hecht_marnet.py` proefbake 2026-10-09 (scratch): zee 3.224,8 km, totaal 4.734,3 km; `maak_havenaanloop.py` 119,8 km.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
Recept: `bash v2/tools/bak_stromen.sh nikkel-raglan-sudbury` (functie `bak_nikkel_raglan_sudbury`) → `v2/data/stroomroute-nikkel-raglan-sudbury.json`
(77,8 KB, versie 2, `lonlat`). **7 benen · 4.734,3 km · 4.071 punten · 6 markers.** Voorwerk (OSM-keten, aanloop, drie omgekeerde spoorkopieën) stond al in `v2/build-cache/ais/graaf/` en is ongewijzigd gebruikt; geen eigen profiel in `maak_stroombeen_weg.py` (de spiegels daar gaven 500/504), dus geen wijziging aan dat bestand.

| # | modaliteit | km | punten | naad naar vorige | stippel | toelichting |
|---|---|---|---|---|---|---|
| 1 | truck | 95,9 | 644 | — | nee | OSM-keten Route Baie Déception–Katinniq (11 ways, via Overpass-spiegel maps.mail.ru). **Geen wegkm-opgave**: de ±15%-toets is indicatie (Wikipedia ~100 km → −4,1%; brief: "hemelsbreed 73,6 km, geen wegkm") |
| 2 | zee | 119,8 | 108 | 0,00 | **ja** | haven-aanloop Deception Bay → zeeknoop 471 (118,3 km hemelsbreed, >25 km snap): `maak_havenaanloop`, 0 km over land, omwegfactor 1,013; schematisch (echte vaarlijn volgt de zuidoever van de Hudsonstraat) |
| 3 | zee | 3.224,8 | 331 | 0,00 | nee | MARNET knoop 471 → Québec-kade, 12 edges, snap 0,000 / 1,617 km; "kade aannemelijk: één bron" staat in de beennaam |
| 4 | spoor | 286,9 | 595 | **1,51** | nee | omgekeerde kopie van `nikkel-sudbury-kristiansand` (Taschereau → Québec). Naad = zeeknoop-snap Québec (1,617 km), ruim < 5 km, geen aanloop nodig |
| 5 | spoor | 541,0 | 993 | 0,00 | nee | omgekeerde kopie (MacMillan → Taschereau) |
| 6 | spoor | 465,7 | 1.398 | 0,00 | nee | omgekeerde kopie (Sudbury → MacMillan) |
| 7 | spoor | 0,2 | 2 | 0,00 | **ja** | Falconbridge-emplacement → smelter 0,16 km: net reikt niet tot de smelterdeur (omgekeerde kopie van b0) |

Spoor totaal 1.293,6 km tegen ~1.230 uit de webcheck (+5,2%, binnen ±15%). Stippel totaal 120,0 km van 4.734,3 (2,5%); geen last-mile-benen, geen vlucht, geen leiding.
**Markers (6)** op 0,00–0,14 km van hun lijn: Raglan-mijn 0,141 · Deception Bay-kade 0,000 · Québec-terminal (aannemelijk) 0,122 · MacMillan Yard 0,088 · Taschereau Yard 0,110 · Sudbury Smelter 0,000.
**Toetsen:** geen naad > 5 km (max 1,51 km); `toets_rechte_benen --min-km 5` meldt niets voor deze stroom; `json.load` ok, versie 2, alle modaliteiten in de toegestane set, elk been ≥ 2 punten.
**Knikken (`toets_knikken`)**: 5 knikken ≥ 60°, 3 omkeringen ≥ 150°, waarvan 2 TERUGLOOP — beide op de gekopieerde MacMillan Yard-geometrie (43,8263/−79,5153 en 43,6673/−79,4652), dezelfde bekende bevinding als `nikkel-sudbury-kristiansand`, niet gerepareerd. Daarnaast één omkering van 167° (R ≈ 10 m, geen terugloop) in b1 bij 61,6886/−73,6682: een ~20 m-stompje waar twee OSM-ways op het mijnterrein aan elkaar sluiten, 0,4 km van het mijnanker; echte OSM-geometrie, niet bijgewerkt. Verder één krappe zeebocht (98°, R 6,5 km, 52,50/−54,00 bij Labrador/Belle Isle) en één spike in b6 bij Sudbury (46,4859/−80,8324).

**Lessen / afwijkingen**
- Het stroom-id noemt Sudbury als eindpunt en dat klopt: de lijn eindigt op de Sudbury Smelter. Geen afwijking van het ontwerp.
- b1 gebruikt de kant-en-klare OSM-keten i.p.v. een profiel: de Overpass-spiegels die `maak_stroombeen_weg.py` hard-codeert zijn vandaag onbereikbaar; `maps.mail.ru` ontbreekt in die lijst (centraal toe te voegen als een profiel gewenst is).
- Gedeelde benen (b3 spoor) zijn letterlijke kopieën, in de beennaam benoemd; de gekopieerde omkeringen zijn dus geen nieuwe fout.
- Open (centraal): Raglan ontbreekt nog in `v2/design/nikkel-sitelaag.json` (61,6876/−73,6750, 39,9 kt Ni/j, bron Glencore at-a-glance, eenheid kt Ni per jaar); registerregel sleutel `ni-ra` (vrij).
