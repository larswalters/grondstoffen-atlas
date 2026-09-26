# Routebrief (licht) · zeldzame aardmetalen — Sillamäe → Narva (Estland)

**stroom-id:** `ree-sillamae-narva` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** REE-oxide (NdPr/Dy/Tb) gescheiden bij Silmet (Neo Performance Materials, Sillamäe) gaat per **truck** over de E20/Tallinn–Narva mnt (~30 km) naar de nieuwe Neo-magneetfabriek in het Kulgu-industriepark bij Narva, waar het tot gesinterde NdFeB-magneten wordt verwerkt — Europa's eerste fabriek van dit type, sinds sept. 2025 open en in opschaling.
**Welke as van het verhaal:** het Europese draadje — de enige commerciële REE-scheiding in de EU buiten Frankrijk gekoppeld aan Europa's eerste permanente-magneetfabriek, 25 km verderop. Jaarvolume: fase 1 **2 kt NdFeB-magneten/jaar** (2.000 t) gepland Q2 2026, fase 2 **5 kt/jaar** (5.000 t); Narva draait nu in *sample production* — niet gerealiseerd [4][7][8].

## 1 · Ketenkaart
```
Silmet-scheidingsfabriek `ree-silmet-scheiding` (Sillamäe)
   ──(b1 truck · E20/Tallinn–Narva mnt · ~30 km, aannemelijk: één bron)──►
   Neo-magneetfabriek `ree-narva-magneetfabriek` (Kulgu-tööstuspark, Narva) ⏹ stoppunt
   ╌╌ vertakking, niet getekend: upstream-oxide van Lynas + "a wide variety of global sources" (geen laadhaven/aandeel gebrond) ──►
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `ree-silmet-scheiding` → `ree-narva-magneetfabriek` | Tallinn–Narva mnt (E20 / nationale weg 1), Sillamäe → Kulgu-tööstuspark Narva | 30,3 (OSRM, eigen meting) — ontwerp noemde ~25 km voor een centralere Narva-schatting | maak_stroombeen_weg (estland-extract) | nee — *aannemelijk: één bron voor de oxidelevering* [4][5] |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-silmet-scheiding` | scheidingsfabriek (laadplek) | NPM Silmet OÜ, Sillamäe | 59.4031, 27.7421 | [1][9][10] | bron-gelegd (z15 gezien: aaneengesloten industrieterrein met tankenpark, spooraansluiting aan de westzijde en meerdere procesgebouwen tussen spoor en kust — komt overeen met de OSM-landuse "Silmet" op 41 m van het punt) |
| `ree-narva-magneetfabriek` | magneetfabriek (losplek) | Neo Performance Materials — NPM Narva OÜ, Kulgu-tööstuspark | 59.3618, 28.1478 | [2][3][6] | bron-gelegd (z16 gezien: gebouwencluster met parkeer-/opslagterrein direct aan de doorgaande weg in het Kulgu-tööstuspark, tussen twee moerasmeren; individuele fabriekshal niet te onderscheiden van eventuele buurbedrijven in het park — het punt komt uit de Google-Maps-coördinaat voor "Narva Tööstuspark (Kulgu)" [3]) |

## 4 · Via-punten (b1 — E20/Tallinn–Narva mnt heeft weinig corridorkeuze, drie pinnende punten)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | aansluiting Sillamäe op de Tallinn–Narva mnt | 59.3964, 27.7610 | pint de route op de doorgaande E20/weg 1 i.p.v. de binnenweg door het centrum van Sillamäe (OSRM-tracé) |
| b1 | 2 | doorgaande E20/weg 1 ter hoogte van Vaivara | 59.4010, 28.0131 | de route blijft op de kustcorridor i.p.v. een binnenlandse afsnijding via Vaivara-Soldina (OSRM-tracé) |
| b1 | 3 | afslag Tallinn–Narva mnt → Kulgu-tööstuspark | 59.3767, 28.1541 | pint de afslag zuidwaarts naar het industriepark i.p.v. rechtdoor Narva-centrum in (OSRM-tracé) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Silmet-scheidingsfabriek, Sillamäe | Neo Performance Materials (NPM Silmet OÜ) | gemengd REE-concentraat/-carbonaat → individuele REE-oxiden (NdPr, Dy/Tb) | Dy/Tb-scheidingslijn gereed 2025; enige commerciële REE-scheiding in de EU buiten het Franse Solvay/La Rochelle (dat sinds april 2025 NdPr en sinds herfst 2026 Dy/Tb scheidt) | [1][11] |
| Neo-magneetfabriek, Kulgu-tööstuspark Narva | Neo Performance Materials (NPM Narva OÜ) | REE-oxide (deels lokaal van Silmet, deels Lynas + overige bronnen) → gesinterd NdFeB-magneet | *sample production* nu; fase 1 2 kt/j gepland Q2 2026 → fase 2 5 kt/j; investering €100 mln, bouw 2023-08 t/m 2025-09 (500 dagen), eerste bouwfase 20.000 m² in een park van 68.000 m² | [3][4][6][7] |

## 6 · Stoppunt
De brief stopt bij de poort van de Neo-magneetfabriek in Narva: Neo heeft een verlengd strategisch partnerschap met Bosch voor hoogwaardige magneten [2], maar geen bron noemt de fabriek van een afnemer (tractiemotor-Tier-1) met naam en adres — fase D/E vervalt.

## 7 · Open punten
- **Upstream-oxide naar Silmet niet getekend.** Neo noemt zelf "a wide variety of global upstream sources, including Lynas Rare Earths"; geen bron geeft een laadhaven of een aandeel per bron, dus de vertakking blijft ongetekend en ongelegd (geen coördinaat verzonnen) [4][7].
- **NdPr-metaal/legering-stap onbekend.** Geen bron zegt of Narva zelf metaal/gelegeerde strip maakt of inkoopt (bv. bij Neo's eigen Magnequench-fabrieken in Tianjin/Korat); de 30 km-lijn Silmet → Narva geldt dus alleen voor de oxidestap, "aannemelijk" in de beennaam.
- **Narva-anker is site-niveau, niet gebouw-niveau.** Het punt komt uit een generieke Google-Maps-coördinaat voor het Kulgu-tööstuspark; op het satellietbeeld is geen bedrijfsnaam te lezen en de opnamedatum t.o.v. de opening (sept. 2025) is niet vastgesteld met een aparte Wayback-pass.
- **"Enige commerciële scheiding in Europa" is gecorrigeerd** naar "enige in de EU buiten Frankrijk": Solvay La Rochelle scheidt sinds april 2025 weer NdPr voor magneten en breidt sinds 2026 uit naar Dy/Tb [11].
- **Volumes zijn gepland, niet gerealiseerd** — Narva draait in *sample production*; 2 kt/j (fase 1) is een Q2-2026-doel, geen huidig volume [4][7].
- **Spoor is bewust niet gebruikt**: het net ligt er wel (0,7 km bij Sillamäe, 0,3 km bij Narva volgens het ontwerp), maar geen bron noemt treinvervoer voor deze 30 km-rit; de weg is de enige gedocumenteerde modaliteit.
- Een eventueel zeebeen (Port of Sillamäe, 21,4 km van MARNET-zeeknoop 6851) is niet getekend: er is geen gedocumenteerde zeevracht op deze as.

## 8 · Bronnen
[1] Wikipedia, "Silmet" — locatie Sillamäe, eigendom Neo Performance Materials (voorheen Molycorp), ~330 werknemers, REE-metaaloxiden + niobium/tantaal. https://en.wikipedia.org/wiki/Silmet
[2] Neo Performance Materials, "Neo Performance Materials Opens State-of-the-Art Permanent Magnet Facility in Europe" (19-09-2025) — grand opening, gebouwd in 500 dagen, Bosch-partnerschap. https://www.neomaterials.com/neo-performance-materials-opens-state-of-the-art-permanent-magnet-facility-in-europe/
[3] Invest in Estonia, "Just Transition Fund's success: Neo's €100M magnet factory in Narva" — locatie Narva Kulgu tööstuspark, bouwstart 01-08-2023, eerste fase 20.000 m², investering €100 mln, JTF-bijdrage €19 mln; incl. Google Maps-coördinaat voor het Kulgu-industriepark (59,3590/28,1464). https://investinestonia.com/neo/
[4] Rare Earth Exchanges / persoverzicht — Narva in sample production, fase 1 2.000 t Q2 2026 → 5.000 t/j; feedstock lokaal van Silmet + "wide variety of global upstream sources, including Lynas Rare Earths". https://rareearthexchanges.com/news/neo-performance-materials-estonia-ndfeb-magnets/
[5] Neo Performance Materials, estonia-landingspagina — locatie Narva, opening 19-09-2025, fase 2.000 → 5.000 t/j, NdFeB voor EV/wind, Bosch-samenwerking genoemd. https://www.neomaterials.com/estonia/
[6] Ida-Viru Investeeringute Agentuur (IVIA), "Narva tööstuspark" — NPM Narva OÜ-fabriek in het Kulgu-deel van het park; totale productiehallen in het park 68.000 m². https://ivia.ee/toostuspargid/kuidas-valida-toostuspark/narva-toostuspark/
[7] Mining.com, "Neo Performance begins producing heavy rare earths at Estonia plant" — sample production, fase 1/Q2-2026-doel, feedstock Silmet + Lynas. https://www.mining.com/neo-performance-begins-producing-heavy-rare-earths-at-estonia-plant/
[8] Northern Miner, "Neo Performance opens Europe's first REE magnet plant" — $75 mln investering (andere valuta-noemer dan [3]), automotive/wind-toepassing. https://northernminer.com/news/neo-performance-opens-europes-first-ree-magnet-plant/1003882816/
[9] OpenStreetMap (ODbL) via Nominatim — landuse-punt "Silmet", Sillamäe linn, Ida-Viru maakond: 59.40312, 27.74211. https://nominatim.openstreetmap.org/search?q=Silmet+Sillam%C3%A4e
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) — `v2/build-cache/satcheck/sat-ree-sillamae-narva-silmet.png`.
[11] Solvay, "Solvay advances European rare earths production through capacity expansion" — La Rochelle: NdPr-lijn commercieel sinds april 2025, Dy/Tb-scheiding vanaf najaar 2026, doel 30 % van Europese magneet-REE-vraag in 2030. https://www.solvay.com/en/press-release/solvay-advances-european-rare-earths-production-through-capacity-expansion
[12] Esri World Imagery via `v2/tools/sat_check.py` (z16, live) — `v2/build-cache/satcheck/sat-ree-sillamae-narva-narva2.png`.
[13] OSRM (router.project-osrm.org), routeberekening Silmet-anker → Narva-anker over het wegennet — 30,3 km, gebruikt voor km-schatting en de drie via-punten in §4.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `ree-sillamae-narva`** → `v2/data/stroomroute-ree-sillamae-narva.json` — 1 been, 29,4 km, 2 markers: truck 29,4 km.
Recept: `bak_stromen.sh` (functie `bak_ree_sillamae_narva`). Profiel `ree-sillamae-narva-silmet-narva` in `maak_stroombeen_weg.py` (extract `estland`), via-punten letterlijk uit §4 overgenomen (aansluiting Sillamäe→E20, E20 t.h.v. Vaivara, afslag Kulgu-tööstuspark).
Lengtetoets: 29,4 km tegen 30 (eigen OSRM-meting, §2/§8[13], geen onafhankelijke operator-publicatie) = **−2,0%** [OK, binnen ±15%]. Naad: n.v.t. (één been). Markers op 0,00 km van de lijn (beide ankers zijn de begin-/eindpunt van het been zelf). `toets_knikken.py`: 0 omkeringen, 0 terugloop (8 spikes <60 m boogstraal op wisselpunten, geen kopmaak). `toets_rechte_benen.py --min-km 5`: geen melding (geen ongestippelde rechte lijn). Contract: versie 2, `punt_formaat lonlat`, modaliteit `truck`, bestand 10,3 KB.
Geen stippel: modaliteit truck, doorgetrokken over de hele lengte — "aannemelijk: één bron" staat in de beennaam, niet in de lijnstijl (brief §2/§7).
Gereedschapslessen: het Silmet-anker hangt via `service`+`access=private`-terreinwegen aan de doorgaande E20 (gemeten op de ongefilterde OSM-graaf) — zonder `eindToegangPrivaat: True` gaf de scan "geen wegpad tussen punt 0 en 1"; met de vlag (alleen binnen de 12-km-eindzone) routeert hij meteen door. Extract `estland` (0,1 GB) volstond, geen tweede extract of Overpass-terugval nodig.
Niet getekend (bewust, zie §7): upstream-oxide naar Silmet, spoor (net ligt er wel maar geen bron noemt treinvervoer), een zeebeen bij Port of Sillamäe (21,4 km van de dichtstbijzijnde MARNET-zeeknoop), fase D/E (geen bron noemt de afnemersfabriek van Narva).
