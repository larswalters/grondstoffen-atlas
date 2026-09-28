# Routebrief (licht) · PGM — Van → Via → Naar (land)

**stroom-id:** `pgm-unki-rustenburg` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** PGM-matte van de Unki Mine (Anglo American Platinum/Valterra Platinum, eigen on-site
smelter sinds 2018/19, Shurugwi, Midlands, Zimbabwe) per **truck** over de A9-corridor (Shurugwi–Zvishavane–
Masvingo) naar de grensovergang **Beitbridge** (hergebruikt anker), en vandaar per **truck** — LETTERLIJKE
KOPIE van `pgm-zimplats-rustenburg` been b2 — over de N1/N4-corridor naar de eindraffinage **Rustenburg PMR**
(Valterra Platinum), Zuid-Afrika.
**Welke as van het verhaal:** de tweede Zimbabwaanse Great Dyke-mijn op de bol met een eigen on-site smelter
(Unki, naast Zimplats/`pgm-zimplats-rustenburg`) — matte die al in Zimbabwe wordt gesmolten en rechtstreeks
naar de Anglo Converter Plant in Rustenburg gaat, niet naar Polokwane (dat ruw concentraat verwerkt, geen
matte-inputstroom heeft — zie §7).

## 1 · Ketenkaart
```
Unki Mine `pgm-unki-mijn` ──(b1 truck · A9 Shurugwi–Zvishavane–Masvingo → A4 Masvingo–Beitbridge ·
   hemelsbreed ~428 km, geen wegkm)──► Beitbridge-grens `pgm-beitbridge-grens`
   ──(b2 truck · N1 Musina–Polokwane–Pretoria → N4 Pretoria–Rustenburg · letterlijke kopie
   pgm-zimplats-rustenburg b2 · ~582 km gebakken)──► Rustenburg PMR `pgm-rustenburg-pmr`
   (Valterra Platinum) ── stoppunt (eindraffinage)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `pgm-unki-mijn` → `pgm-beitbridge-grens` | A9 (Shurugwi–Zvishavane–Masvingo) → A4/R1 (Masvingo–Beitbridge) | hemelsbreed ~428 km (via-puntensom), geen wegkm-bron gevonden — zie §7 | maak_stroombeen_weg | nee |
| b2 | A | truck | `pgm-beitbridge-grens` → `pgm-rustenburg-pmr` | N1 (Musina–Polokwane–Pretoria) → N4 (Pretoria–Rustenburg) — LETTERLIJKE KOPIE van `pgm-zimplats-rustenburg` b2 (zelfde ankers, zelfde corridor, zelfde eindraffinaderij-entiteit) | 582,1 km (reeds gebakken op `pgm-zimplats-rustenburg`) | hergebruik geojson `pgm-zimplats-rustenburg-weg-beitbridge-rustenburg.geojson` | nee |

Geen zee-, spoor-, binnenvaart- of luchtbeen; geen fase B/C (geen overslag op een haven); geen fase D/E (geen
bron noemt een vervolgbestemming ná de eindraffinage in déze as — §6).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-unki-mijn` | mijn/smelter (on-site gesmolten en verbrijzeld) | Unki Mine (Anglo American Platinum/Valterra Platinum), Shurugwi, Midlands, Zimbabwe | -19.6246, 30.0950 | [1][2][6] | bron-gelegd (z15 gezien: proces­gebouwen met een grote lichtgekleurde tailings-opslag en een blauwgroene bezinkvijver direct ten westen, toegangsweg naar het complex — twee onafhankelijke bronnen, Wikipedia-geohack en OSM-landuse, kwamen op ditzelfde punt uit) |
| `pgm-beitbridge-grens` | grensovergang / overslag tussen twee truckcorridors | Beitbridge grensovergang, Limpopo-brug (Zimbabwe ↔ Zuid-Afrika) — **hergebruikt letterlijk** uit `pgm-zimplats-rustenburg.md` (oorspronkelijk `koper-kolwezi-durban.md`) | -22.2244, 29.9865 | [7] | bron-gelegd (overgenomen, zelfde grensanker als `pgm-zimplats-rustenburg`) |
| `pgm-rustenburg-pmr` | losplek / eindraffinaderij | Rustenburg Precious Metals Refinery (Waterval-complex), Valterra Platinum (ex-Anglo American Platinum), Rustenburg, Zuid-Afrika | -25.6838, 27.3272 | [7] | bron-gelegd (overgenomen, zelfde eindanker als `pgm-zimplats-rustenburg`) |

## 4 · Via-punten (in reisvolgorde)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Shurugwi (A9-corridor, dichtst bij de mijn) | -19.6667, 30.0000 | pint de corridor richting Zvishavane i.p.v. noordwaarts naar Gweru |
| b1 | 2 | Zvishavane (A9/P7, junctie met A18) | -20.3333, 30.0333 | sluit de A18-afslag naar Gweru uit; bevestigt de doorgaande A9 zuidoostwaarts |
| b1 | 3 | Masvingo (A9→A4-wissel) — **hergebruikt** uit `pgm-zimplats-rustenburg.md`/`koper-kolwezi-durban.md` | -20.0745, 30.8332 | dwingt de wissel naar de A4/R1 zuidwaarts af i.p.v. doorgaan op A9 naar Mutare |
| b2 | 1–4 | Musina · Polokwane · Pretoria (N1/N4) · Rustenburg (N4/R24) — **letterlijke kopie**, zelfde vier via-punten als `pgm-zimplats-rustenburg.md` §4 | zie die brief | ongewijzigd overgenomen, geen tweede versie van dezelfde corridor |

Geofabrik-regio's: `zimbabwe` (b1), `zuid-afrika` (b1-staart + b2, reeds gedekt door de bestaande b2-bake).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Unki Mine (on-site smelter) | Anglo American Platinum / Valterra Platinum | Great Dyke-concentraat (eigen mijn) → PGM-furnace-matte, on-site gesmolten sinds mei 2019 | Unki 2023 ≈ 190 koz 6E/jaar ≈ 5,9 t 6E/jaar | [3][4][8] |
| Rustenburg PMR / Anglo Converter Plant | Valterra Platinum (ex-Anglo American Platinum) | matte (Unki + Zimplats + eigen Bushveld-concentraat) → geregistreerd Pt/Pd/Rh | grootste PGM-raffinagecomplex ter wereld (capaciteit niet in t/j gepubliceerd in de geraadpleegde bronnen) | [7] |

## 6 · Stoppunt
De brief stopt bij Rustenburg PMR / Anglo Converter Plant: dat is de eindraffinage in deze as (matte →
geregistreerd Pt/Pd/Rh) en geen bron in dit onderzoek noemt een specifieke vervolgzending van het
geraffineerde metaal (dat zou een luchtbeen zijn — bewust niet getekend, geen bron voor luchtvracht in déze
as).

## 7 · Open punten
- **BEWUSTE AFWIJKING van de opdrachthint** ("Unki → Beitbridge → Anglo Polokwane-smelter"): Valterra/Anglo's
  eigen persbericht bij de opening van de Unki-smelter (16-05-2019, "furnace matte... transported to the Anglo
  American Platinum Converter process facility in Rustenburg") en een SAIMM-vakartikel (Snodgrass e.a. 2024)
  zeggen beide dat Unki-matte rechtstreeks naar de Anglo Converter Plant in Rustenburg gaat — niet naar
  Polokwane, dat ruw concentraat verwerkt en geen matte-inputstroom heeft. Rustenburg is hier toegepast als
  juiste eindbestemming [4][5].
- **Km been b1 is hemelsbreed, geen wegkm-bron gevonden** (bindend uit de haalbaarheidstoets, geen blokkade).
  Eigen onderzoek (Wikipedia A9/A6-roadpagina's [9][10]) laat zien dat er vanaf Zvishavane ook een kortere,
  geografisch directere corridor bestaat via Mbalabala/A6 (hemelsbreed via-puntensom ~399 km) in plaats van via
  Masvingo/A4 (~428 km, hier gevolgd conform de ontwerphint en omdat de A4/R1 de gedocumenteerde Chirundu–
  Beitbridge-handelscorridor is). Welke corridor het echte vrachtverkeer volgt is niet bevestigd met een
  wegkm-bron; bij het bakken tegen de ±15%-norm toetsen en zo nodig heroverwegen.
- **`pgm-unki-mijn` ligt 0,68 km van het sitelaag-punt `w-unki`** (`v2/design/pgm-sitelaag.md`, -19.6800,
  30.0000, status aannemelijk/geografische aanduiding) — het hier gelegde, satelliet-bevestigde punt is
  preciezer (twee onafhankelijke bronnen + z15-blik); de sitelaag-centroïde is niet aangepast (buiten scope).
- **Jaarvolume:** Unki 2023 ≈ 190 koz 6E/jaar (Anglo/Valterra jaarverslag 2023, overgenomen uit
  `v2/design/pgm-sitelaag.md` `w-unki`) ≈ **5,9 t 6E/jaar** (190.000 ÷ 32.150 × 1.000, koz→t via oz÷32,15).
  Mix (Pt+Pd+Rh+Au+Ru+Ir = 6E) niet verder uitgesplitst in de geraadpleegde bronnen.

## 8 · Bronnen
[1] Wikipedia, "Unki mine", https://en.wikipedia.org/wiki/Unki_mine (coördinaat-geohack -19.6246, 30.0950)
[2] OpenStreetMap-contributors (ODbL), landuse-object bij Unki Mine (-19.6207, 30.0955), https://www.openstreetmap.org
[3] Valterra Platinum, persbericht opening Unki-smelter, 2019-05-16,
https://www.valterraplatinum.com/media/press-releases/archive/2019/16-05-2019
[4] Mining Review Africa, "Anglo American Platinum opens smelter at Unki mine in Zimbabwe", 2019,
https://www.miningreview.com/platinum-group-metals/anglo-american-platinum-opens-smelter-at-unki-mine-in-zimbabwe/
[5] SAIMM, Snodgrass e.a., "Pyrometallurgy 2024" (PDF, Unki-matte → Rustenburg Converter Plant),
https://www.saimm.co.za/Conferences/files/pyrometallurgy-2024/16_646-Snodgrass.pdf
[6] Wikipedia, "Great Dyke" (geografische aanduiding Unki bij Shurugwi), https://en.wikipedia.org/wiki/Great_Dyke
[7] `v2/design/routebrieven/pgm-zimplats-rustenburg.md` — hergebruikte ankers `pgm-beitbridge-grens`
(-22.2244, 29.9865) en `pgm-rustenburg-pmr` (-25.6838, 27.3272), letterlijke kopie been b2
[8] `v2/design/pgm-sitelaag.md` `w-unki` — Anglo/Valterra jaarverslag 2023, ~190 koz 6E/jaar
[9] Wikipedia, "A9 road (Zimbabwe)" (Masvingo–Mashava–Zvishavane–Filabusi–Mbalabala, junctie met A4 te
Masvingo), https://en.wikipedia.org/wiki/A9_road_(Zimbabwe)
[10] Wikipedia, "A4 road (Zimbabwe)" (Beitbridge–Rutenga–Ngundu–Masvingo–Mvuma–Chivhu–Harare, R1/Chirundu–
Beitbridge-corridor), https://en.wikipedia.org/wiki/A4_road_(Zimbabwe)
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15), `v2/build-cache/satcheck/sat-pgm-unki-rustenburg-unki.png`

## 9 · Bak-noot (voor de bak-agent)

**Gebakken (2026-09-28, lichte werkwijze, M31 golf 6).** `bash v2/tools/bak_stromen.sh pgm-unki-rustenburg`
→ `v2/data/stroomroute-pgm-unki-rustenburg.json` (178,5 KB, contract versie 2, `punt_formaat: lonlat`).

| # | modaliteit | km gebakken | km brief | afwijking | stippel | naad met vorig been |
|---|---|---|---|---|---|---|
| b1 | truck | 476,9 | ~428 (hemelsbreed, geen wegkm-bron) | +11,4% | nee | 0,000 km (start) |
| b2 | truck | 582,4 | 582,1 (reeds gebakken op pgm-zimplats-rustenburg) | +0,05% | nee | 0,000 km |
| **totaal** | | **1.059,3 km** | | | | 3 markers, 8.742 punten |

**Been b1 (Unki-mijn → Beitbridge-grens).** Vers gebakken wegprofiel `pgm-unki-rustenburg-unki-beitbridge`
in `v2/tools/maak_stroombeen_weg.py` (extract `zimbabwe`, `vensterKm` 90, geen `corridorKlassen`/
`eindToegangPrivaat` nodig). Landscan: 24.379 km ruw over 1 extract, 16.185 unieke ways, 6 keerlussen
gesnoeid (499,2 → 476,9 km). Uitkomst 476,9 km tegen het hemelsbreed-ontwerpcijfer ~428 km = **+11,4%**.
Dit is BUITEN de ±10%-waarschuwing van het wegtool en ook buiten de ±15%-norm, maar de brief geeft hier
géén gepubliceerde wegkm — alleen een via-puntensom hemelsbreed — dus de toets is hier indicatief en niet
bindend (routebrief-licht.md §1, brief §7/§bak_aanwijzingen). Een echte wegroute buigt onvermijdelijk meer
uit dan een hemelsbrede via-puntensom; 476,9 km over vier via-punten (11,3 · 87,1 · 99,7 · 288,4 km) is
zonder afwijkende corridor-signalen (geen `corridorKlassen`/private wegklassen nodig, snap op de via-punten
0,00–1,64 km, ver onder de 5 km-drempel voor een wegklasse-controle). Geen stippel: doorgetrokken truckbeen
over de openbare A9/A4-corridor; plant → weg-aansluiting 0,00 km (geen last-mile-stippel nodig, < 2 km).
**Open bevinding (niet zelf gewijzigd, zie brief §7):** het alternatief via Zvishavane→Mbalabala/A6
(~399 km hemelsbreed, brief §7) is niet gescand — de brief noemt dit als onbevestigd, en deze bake volgt
de aangegeven Masvingo/A4-route conform de ontwerphint. Welke corridor het echte vrachtverkeer volgt blijft
onbevestigd; een eventuele herbake op het A6-alternatief is een apart besluit.

**Been b2 (Beitbridge-grens → Rustenburg PMR).** LETTERLIJKE KOPIE van `pgm-zimplats-rustenburg` been b2:
geojson gekopieerd naar `v2/build-cache/ais/graaf/pgm-unki-rustenburg-weg-beitbridge-rustenburg.geojson`
(byte-identiek aan het bronbestand, alleen de bestandsnaam draagt de nieuwe stroom-id voor de
agentdiscipline uit bakhandleiding §0.2). Geen nieuwe wegscan, geen nieuw profiel. Gemeten 582,4 km tegen
582,1 gepubliceerd op de bronstroom = +0,05%. Vier via-punten (Musina/Polokwane/Pretoria N1-N4/Rustenburg
N4-R24), identiek aan de bronbrief.

**Naad b1↔b2:** 0,000 km — beide benen delen letterlijk het Beitbridge-grensanker (-22,2244, 29,9865).

**Toets (bakhandleiding §5).** `toets_knikken.py`: been b1 heeft 7 spikes (alle < 60 m straal, OSM-
kruispunt-artefacten van de wegscan), **0 omkeringen** — geen bevinding. Been b2 heeft 16 knikken/2
omkeringen/1 terugloop, **exact gelijk aan de bronstroom `pgm-zimplats-rustenburg`** (zelfde geometrie,
zelfde afwijkingen, byte-identieke coördinaten in de terugloop-regel −25,70456/27,25575) — pre-existent,
niet door deze bake geïntroduceerd en niet aangeraakt (bestaande brief/stroom, buiten scope).
`toets_rechte_benen.py --min-km 5`: geen been van deze stroom gemeld (geen omwegfactor-1,000-lijn).
JSON-contract: `versie` 2, `punt_formaat` "lonlat", beide `modaliteit`-waarden `truck` (geldig), elk been
≥ 2 punten (4.688 en 4.054), bestand 178,5 KB (ruim binnen de ~300 KB-marge). Markers: `pgm-unki-mijn` en
`pgm-beitbridge-grens` op 0,0 m van de lijn; `pgm-rustenburg-pmr` op 200,4 m — anker ≠ routeerpunt, exact
dezelfde afstand/reden als op de bronstroom (niet aangepast).

**Geen** haven-aanloop (geen zeebeen), **geen** luchtbeen, **geen** leiding/binnenvaart, **geen** fase D/E
(brief §6: geen bron noemt een vervolgbestemming ná Rustenburg PMR in deze as).

**Registerregel voor `main.js`** (centraal, niet door deze agent doorgevoerd):
`{ sleutel: "pgm-ur", bestand: "stroomroute-pgm-unki-rustenburg.json", grondstof: "pgm", aan: true }`.

**Lessen:** een hemelsbreed-via-puntensom is geen wegkm-bron — de ±15%-toets is dan indicatief, dus een
+11,4%-afwijking op zo'n cijfer is geen blokkade, wel een bevinding om in de brief te laten staan i.p.v.
via-punten te verschuiven om het getal te halen. Een letterlijke geojson-kopie draagt de knikken/afwijkingen
van de bronstroom automatisch mee — die zijn dus geen nieuwe bevinding van déze bake.
