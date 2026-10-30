# Routebrief (licht) · nikkel — Koniambo-mijn → Vavouto-smelter → Port de Vavouto (Nieuw-Caledonië)

**stroom-id:** `nikkel-koniambo-vavouto` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** lateriet-erts uit de Koniambo-mijn (Voh, Noordprovincie) gaat over een **11 km lange overlandband** (OSM `man_made=goods_conveyor`, way 294630247) naar de ferronikkelsmelter van Koniambo Nickel SAS bij Vavouto en vandaar over de eigen servicewegen van het terrein naar de eigen diepwaterkade **Port de Vavouto** — mine-mouth, geen zeebeen, want geen bron noemt een afnemer; de smelter ligt sinds 2024 stil (stoppunt: de kade).
**Welke as van het verhaal:** *het symbool van de Indonesië-shakeout* — SMSP (51 %) en Glencore (49 %) bouwden een eigen mijn-smelter-haven-keten van ~US$7 mld (2014) die nooit zijn 60 kt Ni per jaar haalde [1][4]. Volume: **27,2 kt Ni in ferronikkel** (Fastmarkets, "in 2024", maar het artikel is van feb 2024: peiljaar onzeker) tegen nameplate **60 kt Ni/j** [3][4]; Wikipedia noemt 176 kt ferronikkel/j als productcapaciteit [1].

## 1 · Ketenkaart
```
Koniambo-mijn, ertsbewerking `ni-koniambo-bandbegin`
   ──(b1 leiding/band · overlandband mijn → smelter, OSM way 294630247 · 12,1 km; SMSP 11,2, Wikipedia 11)──►
Ertsplaats Vavouto `ni-koniambo-ertsplaats` (bandeinde, naad)
   ──(b2 leiding/band, STIPPEL · laatste stuk terrein ertsplaats → smelter · 1,3 km, geen net op deze korrel)──►
Smelter Koniambo Nickel SAS `ni-koniambo-smelter`
   ──(b3 truck · OSM-service Accès Usine du Nord / Accès Usine de Vavouto · ~3,2 km)──► Port de Vavouto-kade `ni-vavouto-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding (band) | `ni-koniambo-bandbegin` → `ni-koniambo-ertsplaats` | overlandband Koniambo, OSM way 294630247 (`goods_conveyor`, 112 punten, source bing) | OSM **12,1**; SMSP 11,2 [2], Wikipedia 11 [1] = +8 % / +10 %; hemelsbreed 11,1 | `--been-geojson "leiding\|…"` (FeatureCollection, vooraf gestikt: `nikkel-koniambo-vavouto-leiding-band.geojson`) | nee |
| b2 | A | leiding (band) | `ni-koniambo-ertsplaats` → `ni-koniambo-smelter` | terrein Vavouto (band loopt op beeld door, OSM kent het stuk niet) | hemelsbreed 1,3, geen wegkm | `--stippel "leiding\|…"` | ja (geen net op deze korrel) |
| b3 | C | truck | `ni-koniambo-smelter` → `ni-vavouto-kade` | OSM-service Accès Usine du Nord (way 229110797) → Accès Usine de Vavouto (way 375917195, 2,45 km) | hemelsbreed 2,3 km, geen wegkm (eigen OSM-meting over de servicewegen 3,2 km) | maak_stroombeen_weg (profiel `nikkel-koniambo-vavouto-smelter-kade`) | nee |

Beennaam b1 (leiding, doorgetrokken): `overlandband Koniambo-mijn → ertsplaats Vavouto (OSM goods_conveyor, 12,1 km; SMSP 11,2 km)`. Geen zeebeen, geen haven-aanloop, geen MARNET: de keten stopt op de kade omdat de productie stil ligt en geen afnemer gebronnen is. Geen fase D/E.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-koniambo-bandbegin` | mijn / ertsbewerking (kop van b1, marker) | Koniambo-mijn, bandbegin aan de ertsbewerking | -20.9871, 164.7981 | [1][5][8] | bron-gelegd (z15 gezien: ertsbewerkingsvlak met witte gebouwen en een klein blauw bassin op de zuidrand van de pitten, haulwegen en terrassen; het kruis ligt op het bandbegin aan de westrand) |
| `ni-koniambo-ertsplaats` | ertsplaats (bandeinde, naad b1/b2, geen marker) | Ertsplaats bij de smelter, eindpunt OSM-band | -21.0190, 164.6969 | [5][8] | bron-gelegd (z15 gezien: bruin ertsopslagveld met een donker bandspoor dat vanaf het kruis noordwest naar de smelter loopt) |
| `ni-koniambo-smelter` | smelter (marker, kop b3) | Koniambo Nickel SAS ferronikkelsmelter, Vavouto | -21.0125, 164.6870 | [2][6][8] | bron-gelegd (z15 gezien: ovenhallen, hoge schoorstenen, ketelhuizen en kolenstapels van de eigen centrale op het schiereiland; het OSM-plantpolygoncentroïde -21.0085/164.6903 ligt in mangrove) |
| `ni-vavouto-kade` | overslag, eigen diepwaterkade (marker, staart b3, stoppunt) | Port de Vavouto, kade | -21.0027, 164.6670 | [2][6][8] | bron-gelegd (z16 gezien: L-vormige betonnen kade met opslagvlak aan het einde van de dam, tankopslag en weg erachter; geen schip langszij, productie ligt stil) |

Hergebruik: geen Nieuw-Caledonië-anker bestond voor deze keten (de ouaco-brief gebruikt Koniambo alleen als context). Sitelaag `w-koniambo-kns` (-21.0080, 164.7300, Wikipedia-geohack van de mijnpagina) ligt op **4,3 km oost** van de smelter en op 7,5 km van het bandbegin, dus op geen van beide: zie §7.

## 4 · Via-punten (alleen b3; b1 volgt één gekarteerde way, b2 is een stippel)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Knoop Accès Usine du Nord / Accès Usine de Vavouto | -21.0122, 164.6812 | pint de benoemde servicekade-weg 375917195 (permissive, 2,45 km) tegenover de naamloze service-way 1175565313 met bijna dezelfde uiteinden; zonder dit punt kiest Dijkstra vrij tussen de twee |

Profielcoördinaten (lon, lat): smelter (164.6870, -21.0125) → knoop (164.6812, -21.0122) → kade (164.6670, -21.0027).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Koniambo-mijn + ertsbewerking | Koniambo Nickel SAS (SMSP 51 %, Glencore 49 %) | saprolietisch lateriet-erts (~2,6 % Ni) → ertsstroom naar de band | reserve ~62 Mt erts (SMSP), resource >150 Mt bij 2,57 % Ni | [1][2] |
| Vavouto-smelter | idem | erts → ferronikkel (twee elektrische ovens, twee lijnen 2013/2014; eigen 132 MW kolencentrale) → grenaille in zakken van 2 t | nameplate 60 kt Ni/j; 27,2 kt Ni geproduceerd (Fastmarkets); productie gestopt feb 2024, mijn en fabriek dicht aug 2024, ovens later in 2024 uitgezet | [1][2][3][4] |

## 6 · Stoppunt
De brief stopt op de kade van Port de Vavouto: de smelter ligt stil (feb–aug 2024, >1.200 banen verloren) en geen bron noemt een afnemer of bestemming voor het ferronikkel, dus er is geen zeebeen — de keten is mine-mouth en bewust kort.

## 7 · Open punten
- **Afnemer/bestemming onbekend:** Wikipedia en SMSP noemen alleen export vanaf de eigen haven [1][2]; één ongedateerd lnc-bericht noemt een eerste lading van 322 t grenaille per container naar India (schip Cape-Don), KNS niet bij naam genoemd [9]. Dat is te weinig voor een zeebeen.
- **Band is `goods_conveyor`, geen pipeline:** doorgetrokken als leidingbeen op besluit van de haalbaarheidstoets (precedent kolen-grootegeluk-medupi); source=bing 2014, het laatste bandstuk naar de smelter ontbreekt in OSM en is stippel (b2).
- **Wegkm bij b3:** geen bedrijfs- of overheidsopgave; de 3,2 km is mijn eigen OSM-meting over de servicewegen en geldt als indicatie, niet als ±15 %-norm.
- **Plantcentroïde en haven in OSM:** `Usine Koniambo` (way 104422889) heeft een centroïde in mangrove; `Port de Vavouto` (way 74113359) draagt `fixme=coastline_please_check`: gebruikt voor oriëntatie, niet voor coördinaten.
- **Sitelaag-correctie (centraal):** `w-koniambo-kns` (rol smelter) staat 4,3 km ten oosten van de smelter; voorstel -21.0125/164.6870.
- **Status:** herstart onzeker; Lygend (CN) bood in maart 2026, nog geen uitkomst gevonden [10]. Productie 27,2 kt Ni: peiljaar niet vast te stellen (2023 of 2024).
- **Productvorm:** SMSP noemt zakken van 2 t [1], lnc containers [9]; beide zijn plausibel, niet uitgezocht omdat er geen volgend been is.

## 8 · Bronnen
[1] Wikipedia (EN), Koniambo mine — 11 km band, 176 kt ferronikkel/j, productie gestopt feb 2024, KNS 2014-aug 2024, coördinaat 21°00′29″S 164°43′48″E. https://en.wikipedia.org/wiki/Koniambo_mine
[2] SMSP, Koniambo Nickel SAS — band 11,2 km, twee ovenlijnen, 132 MW centrale, diepwaterhaven Vavouto voor export, reserve 62 Mt, Glencore verkoopt (29-02-2024). https://smsp.nc/en/koniambo-nickel-sas-eng/
[3] ABC News, 2025-04-11 — fabriek en mijn dicht augustus 2024, tot 60.000 t nikkel/j, >1.200 banen, twee gegadigden. https://www.abc.net.au/news/2025-04-11/new-caledonia-koniambo-nickel-mine-shutdown/105151562
[4] Fastmarkets, Hotter, "Billions of dollars for a teacup of nickel" — 27.200 t Ni in ferronikkel ("2024"), 60 kt/j nameplate, Glencore 49 % / SMSP 51 %, care and maintenance. https://fastmarkets.com/insights/glencore-koniambo-nickel-joint-venture-andrea-hotter
[5] OpenStreetMap (ODbL), way 294630247 (`man_made=goods_conveyor`, 112 punten, 12,10 km, source bing), via de OSM-API 0.6 opgehaald 2026-10-30. https://www.openstreetmap.org/way/294630247
[6] OpenStreetMap (ODbL), ways 104422889 (Usine Koniambo), 74113359 (Port de Vavouto, container-seamark, fixme coastline). https://www.openstreetmap.org/way/74113359
[7] OpenStreetMap (ODbL), ways 375917195 (Accès Usine de Vavouto, 2,45 km) en 229110797 (Accès Usine du Nord), kaartgebied via `api/0.6/map`; eigen Dijkstra smelter → kade 3,19 km. https://www.openstreetmap.org/way/375917195
[8] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16): `v2/build-cache/satcheck/sat-nikkel-koniambo-vavouto-bandbegin.png`, `-bandeinde.png`, `-smelter.png`, `-kade.png`.
[9] Les Nouvelles Calédoniennes, "Grenaille en haute mer" — eerste export 322 t grenaille in 16 containers naar India, schip Cape-Don (ongedateerd, paywall). https://www.lnc.nc/article/pays/economie/grenaille-en-haute-mer
[10] WebSearch 2026-10-30 (lnc.nc, La Voix du Caillou, SMSP): Lygend-bod maart 2026, in studie bij Glencore en SMSP; Mining.com, "Two bids made for Glencore stake in New Caledonia's Koniambo Nickel". https://www.mining.com/web/two-bids-made-for-glencore-stake-in-new-caledonias-koniambo-nickel/

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

Bestand `v2/data/stroomroute-nikkel-koniambo-vavouto.json` (4,5 KB, versie 2, lonlat), functie `bak_nikkel_koniambo_vavouto` in `v2/tools/bak_stromen.sh`, profiel `nikkel-koniambo-vavouto-smelter-kade` in `v2/tools/maak_stroombeen_weg.py`. Titel: Nikkel · Koniambo → Vavouto (Nieuw-Caledonië, band + smelter + haven). Totaal 16,8 km, 158 punten, 3 markers.

| # | modaliteit | been | km | stippel | naad |
|---|---|---|---|---|---|
| b1 | leiding | overlandband Koniambo-mijn → ertsplaats Vavouto (OSM goods_conveyor, vooraf gestikt) | 12,1 | nee | - |
| b2 | leiding | bandvervolg ertsplaats → smelter (schematisch) | 1,3 | ja: geen net op deze korrel | 0,002 km |
| b3 | truck | servicewegen smelter → Port de Vavouto-kade | 3,4 (getekend; 3,19 km puur weg + ankerstukjes 0,06 en 0,16 km) | nee | 0,000 km |

Markers: ni-koniambo-bandbegin (-20.9871, 164.7981), ni-koniambo-smelter (-21.0125, 164.6870), ni-vavouto-kade (-21.0027, 164.6670); alle op 0,0 tot 0,005 km van de lijn. De ertsplaats is naad zonder marker.

Recept: b1 `--been-geojson` met het eerder gestikte FeatureCollection (OSM way 294630247, 12,1 km tegen SMSP 11,2 km = +8 procent en Wikipedia 11 km = +10 procent: binnen 15 procent, maar geen wegkm). b2 `--stippel` rechte lijn. b3 nieuwe wegscan via `wegscan_puur.py` (extract nieuw-caledonie, 14 MB, 3 s scan, vensterKm 8, eindKlassen service/residential/tertiary/unclassified, eindToegangPrivaat); via-punt in de knoop Accès Usine du Nord / Accès Usine de Vavouto pint de benoemde way 375917195. Geen zeebeen, geen haven-aanloop, geen MARNET-snap, geen kopie, geen fase D/E.

Toelichting:
- b2 is stippel omdat OSM het laatste bandstuk niet kent (hemelsbreed 1,3 km, geen wegkm).
- b3: geen gepubliceerde wegkm; de wegscan geeft 3,19 km (service) tegen de eigen meting 3,2 km uit de brief: indicatie, geen norm. Getekende lijn 3,4 km omdat de ankerverbindingen (plant naar weg 0,06 km, weg naar kade 0,16 km) meetellen.
- Toetsen: geen naad > 5 km (max 0,002 km); toets_knikken: 2 knikken (101 graden op 38 m en 87,5 graden op 98 m bij de ankers, spikes in de ankerverbinding), geen omkeringen of terugloop; json.load goed, modaliteiten {leiding, truck}, alle benen >= 2 punten.

Lessen: (1) bij een mine-mouth keten zonder afnemer stopt de lijn op de eigen kade; (2) een goods_conveyor is een doorgetrokken leidingbeen zolang OSM de way heeft, het ontbrekende stuk is stippel; (3) bij een kleine extract (14 MB) is de wegscan in seconden klaar.
