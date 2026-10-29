# Routebrief (licht) · Kolen · Carmichael → Newlands → Abbot Point (Australië)

**stroom-id:** `kolen-carmichael-abbotpoint` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) · **status:** gebakken
**Keten in één zin:** thermische kolen van de Carmichael-mijn (Bravus/Adani, Galilee-bekken) per **spoor** ~368 km over de eigen
Carmichael Rail Network (~200 km, 2021) en daarna het Aurizon-net (Newlands → Collinsville → Merinda → Kaili) naar de kolenopslag van
de North Queensland Export Terminal (NQXT) bij Abbot Point. Stoppunt = de kade: geen bron noemt een bestemming, dus geen zeebeen.
**Welke as van het verhaal:** *Galilee-bekken: de eerste nieuwe grootmijn van Adani* — 12,9 Mt kolen in FY2024/25 (apr 2024–mrt 2025)
[3][4], gepland 10 Mt/j (gedownsized van 60), uitbreiding naar 16 Mt/j binnen vier jaar [5]; alles verkocht op de internationale
zeekolenmarkt (thermisch), landen niet genoemd [3]. Eenheid Mt kolen per jaar. Eerste lading 29-12-2021 [1].

## 1 · Ketenkaart
```
Carmichael-mijn, CHPP + laadlus `kolen-carmichael-laad`
   ──(b1 spoor · Carmichael Rail ~203 km tot Newlands · daarna Newlands-lijn → Collinsville → Merinda → Kaili → Abbot Point · ~368 km gemeten)──►
NQXT kolenopslag, Abbot Point `kolen-abbotpoint-terminal` ⏹ stoppunt (kade/pier 2,75 km offshore niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | Carmichael-laadlus → NQXT kolenopslag | Carmichael Rail (smalspoor 1067 mm, Bowen Rail Company) → Newlands-systeem → Collinsville → Merinda → Kaili → Abbot Point | 368,4 gemeten; gepubliceerd ~371 = 200 + 73 + 77 + 8 + 13 (−0,7%) [1][2][6] | maak_spoorbeen_raw.py (ruwe OSM-ways, zie §7) | nee; kade-aansluiting 0,2 km en loadout-spur zitten op het net |

Geen zeebeen, geen haven-aanloop: de pier ligt 2,75 km buitengaats [7] en geen bron noemt een afnemer of bestemming.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-carmichael-laad` | mijn / laadplek | Carmichael: wasserij (CHPP), kolenopslag en treinlaadlus | -22.0215, 146.4088 | [1][10][11] | bron-gelegd (z16 gezien: wasserij en kolenopslag, transportband naar de laadlus, spoorlus 40 m van het punt; de Wikipedia-coördinaat -22.0500, 146.3833 ligt in de dagbouwput) |
| `kolen-abbotpoint-terminal` | overslag zee / losplek spoor | NQXT, zuidkop kolenopslag bij Abbot Point | -19.8999, 148.0774 | [7][10][11] | bron-gelegd (z15/z16 gezien: kolenopslagvelden, spoorlus rond een bezinkbekken direct zuid, pier loopt noordwaarts de zee in; spoor eindigt 0,2 km van het punt) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Vanaf de laadlus is er één doorgaande lijn; de punten pinnen de corridor op het Newlands/GAP-systeem noordwaarts (niet naar het Goonyella-net zuidwaarts).
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Carmichael Rail → Newlands-systeem (aansluiting, ~203 km) | -21.1462, 147.8951 | einde Carmichael Rail; hier begint de Newlands-lijn noordwaarts (73 km tot Collinsville) [6][8] |
| b1 | 2 | Collinsville (station/lijn) | -20.5499, 147.8517 | pint de Newlands-lijn; punt 0,7 km van de stad op de lijn, niet in het centrum [6] |
| b1 | 3 | Merinda | -20.0304, 148.1625 | einde Collinsville–Merinda (77 km), aansluiting op de North Coast Line [6] |
| b1 | 4 | Kaili | -19.9962, 148.0871 | afsplitsing 8 km west van Merinda naar Abbot Point (13 km) [6] |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Carmichael CHPP + laadlus | Bravus (Adani) | ruwe kolen → thermisch product, treinlading | 12,9 Mt FY2024/25 (nameplate 15 Mtpa, doel 16) | [3][4][5] |
| NQXT Abbot Point | NQXT, in Adani-beheer (99-jarige lease Terminal 1, 2011) | trein → stockyard → pier/shiploader | niet gevonden (alleen 15,1 Mt in 2010-11) | [7] |

## 6 · Stoppunt
De brief stopt op de kolenopslag van NQXT: kolen verlaten daar het spoor voor de pier, en geen bron noemt een afnemer, schip of bestemmingshaven;
India en Zuidoost-Azië staan alleen als marktrichting zonder lading of koper [2].

## 7 · Open punten
- **Geometrie niet via `toets_spoorroute`:** het 1-op-1-net is bladgesnoeid; de doodlopende Carmichael-tak is weg, het mijnuiteinde snapt 141 km verder
  bij Goonyella (-22,546; 147,661). De lijn is daarom gestikt uit de ruwe OSM-ways (zelfde bron, zonder snoei) met `v2/tools/maak_spoorbeen_raw.py`.
- **Pier en transportband niet getekend:** het berth ligt 2,75 km offshore [7]; geen zeebeen, dus de lijn eindigt op de kolenopslag.
- **Afnemer/bestemming onbekend:** India alleen als vermoeden [2]; geen scheepslading met naam gevonden.
- **Volume:** FY2024/25 is een boekjaar (apr–mrt), geen kalenderjaar; NQXT-doorvoer en aandeel Carmichael niet gepubliceerd.
- **Gepubliceerde spoorkm is een som van vier bronnen** (Carmichael 200 [1][2], Newlands 73 / Collinsville–Merinda 77 / Merinda–Kaili 8 / Kaili–Abbot Point 13 [6]), geen operator-totaal.
- **Aansluitpunt precies:** de OSM-lijn sluit op ~203 km aan bij Newlands; de exacte aansluitkilometer van Bowen Rail Company is niet gevonden.

## 8 · Bronnen
[1] Wikipedia, Carmichael coal mine: 10 Mt/j (gedownsized van 60), eerste lading 29-12-2021, Carmichael Rail Network ~200 km (sept 2021), Bowen Rail Company. https://en.wikipedia.org/wiki/Carmichael_coal_mine
[2] The Coal Face, 10 Mt milestone (15-08-2023): Carmichael Rail Network 200 km naar het Newlands-systeem, NQXT; markt India en Zuidoost-Azië. https://thecoalface.net.au/10mt-milestone/
[3] Adani Enterprises annual report 2025, commercial mining: 12,9 Mt FY25, 15 Mtpa capaciteit, alles op de zeekolenmarkt. https://connect.adani.com/annual_report/2025/ael/commercial-mining-business.html
[4] Argus, Bravus to expand Carmichael: 12,9 Mt apr 2024–mrt 2025. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2722921-bravus-to-expand-australia-s-carmichael-coal-mine
[5] World Coal (19-08-2025), Bravus: van 10+ naar 16 Mtpa binnen vier jaar. https://www.worldcoal.com/coal/19082025/bravus-commits-to-increase-mine-production-in-central-queensland/
[6] Wikipedia, GAP line (Collinsville–Newlands–North Goonyella): Merinda–Collinsville 77 km, Newlands-extensie 73 km, Kaili–Abbot Point 13 km, Kaili 8 km west van Merinda. https://en.wikipedia.org/wiki/GAP_line
[7] Wikipedia, Abbot Point: NQXT, pier en shiploader 2,75 km offshore, GAP-aanvoer, Adani-lease, 25 km NW van Bowen. https://en.wikipedia.org/wiki/Abbot_Point
[8] Global Energy Monitor, Newlands Rail System (QR National, 190 km enkelspoor). https://www.gem.wiki/Newlands_Rail_System
[9] Wikipedia, Goonyella railway line: GAP-verbinding naar Abbot Point. https://en.wikipedia.org/wiki/Goonyella_railway_line
[10] OpenStreetMap (ODbL) via `v2/build-cache/raw1op1/australie.geojson`: Carmichael-laadlus (way 1052941450), Carmichael Rail (ways 1500668324..1500668364, 1000670082/83), Newlands/GAP-lijn. https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16): `v2/build-cache/satcheck/sat-kolen-carmichael-abbotpoint-mijn-chpp.png`, `-mijn-chpp2.png`, `-nqxt.png`, `-nqxt-spoor.png`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)
**Bestand:** `v2/data/stroomroute-kolen-carmichael-abbotpoint.json`, 26,9 KB, versie 2, lonlat, 1 been, 2 markers. **Titel:** Kolen · Carmichael (Galilee) → Abbot Point (Queensland).

| # | modaliteit | been | km gemeten | km brief | afwijking | naad |
|---|---|---|---|---|---|---|
| 1 | spoor | spoor Carmichael-laadlus naar Abbot Point (Carmichael Rail + Newlands/GAP) | 368,4 (1239 punten) | ~371 (som van vier bronnen) | −0,7% | n.v.t. |

**Markers (2):** Carmichael CHPP en laadlus (-22.0215, 146.4088), 0,007 km van de lijn; NQXT kolenopslag, zuidkop (-19.8999, 148.0774), 0,204 km van het lijneinde (anker is niet gelijk aan routeerpunt, spoor eindigt op de lus naast het anker). Geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen letterlijke kopie.

**Recept:** (1) `python v2/tools/maak_spoorbeen_raw.py --extract australie --van=-22.0215,146.4088 --via=-21.1462,147.8951 --via=-20.5499,147.8517 --via=-20.0304,148.1625 --via=-19.9962,148.0871 --naar=-19.8999,148.0774 --uit v2/build-cache/ais/graaf/spoorroute-kolen-carmichael-abbotpoint-carmichael-abbotpoint.geojson` (snaps 3 tot 7 m, aan het eind 203 m; 368,4 km; 0 omkeringen); (2) functie `bak_kolen_carmichael_abbotpoint()` in `v2/tools/bak_stromen.sh` met één `--been-geojson "spoor|…"` en twee `--marker`; (3) `bash v2/tools/bak_stromen.sh kolen-carmichael-abbotpoint`.

**Toelichting:** de lijn is gestikt uit de ruwe OSM-ways omdat `toets_spoorroute` de bladgesnoeide Carmichael-tak mist (mijn snapt 141 km weg bij Goonyella). Er is geen zeebeen: geen bron noemt een bestemming en de pier ligt 2,75 km offshore. De gepubliceerde ~371 km is een som van vier bronnen (200+73+77+8+13), dus de ±15%-toets is een indicatie, geen operatortotaal.

**Toets:** `toets_knikken.py` 0 knikken en 0 omkeringen; `toets_rechte_benen.py --min-km 5` meldt de stroom niet; json.load, versie 2, lonlat, modaliteit spoor, ≥ 2 punten, bestand 26,9 KB.

**Lessen:** (a) `maak_spoorbeen_raw.py` is een nieuw bestand dat nog niet gecommit is en de geojson staat in build-cache (niet in git): bij een herbak eerst het tool terugzetten. (b) Bash leest `bak_stromen.sh` incrementeel: een gelijktijdige edit van een andere agent gaf na afloop een onschuldige "command not found" op een verschoven byte-offset, de bake zelf was klaar.
