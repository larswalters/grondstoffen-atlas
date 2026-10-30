# Routebrief (licht) · olie — OPF Nogliki (Sachalin) → Trans-Sachalin-leiding → Prigorodnoje-oliesterminal (Rusland)

**stroom-id:** `olie-boatasyn-prigorodnoye` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** Sakhalin Blend (olie Piltun-Astokhskoje + condensaat Lunskoje) verlaat de Onshore Processing Facility (OPF) bij Nogliki per **leiding** (Trans-Sachalin-systeem, Sakhalin Energy) over 623 km noord-zuid door Sachalin naar het oliesterminal-/tankpark bij Prigorodnoje aan de Aniva-baai (Russisch Verre Oosten). Eén doorgetrokken been.
**Welke as van het verhaal:** *de Sachalin-2-oliepijplijn onder sancties* — ontwerp ~180 kb/d [1] (na de OPEC+-korting van 2020 nog 88 kb/d [2]); afnemers (Japan) en de OFAC-uitzondering GL 55F (tot 18-12-2026) zijn niet cargo-gebrond [5].

## 1 · Ketenkaart
```
OPF Nogliki `ol-opf-nogliki` (Bo-Atasyn, noord-Sachalin)
  ──(b1 leiding · Trans-Sachalin oliepijplijn, 8 OSM-ways · 622,9 km doorgetrokken · GEM 637 km, inferred)──►
Prigorodnoje-oliesterminal, tankpark `ol-prigorodnoye-oet` (Aniva-baai) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | OPF Nogliki → Prigorodnoje-oliesterminal | Trans-Sachalin-leiding (Sakhalin Energy), noord-zuid door Sachalin | **622,9** eigen OSM-som [6]; GEM 637 km OPF → LNG-plant/oliesterminal = **−2,2%** [3] (inferred, geen oliespecifieke lengte; 800 km in omloop is de hele lijn incl. kustdelen [4]) | OSM-ways `man_made=pipeline substance=oil operator=Sakhalin Energy`, naam Транссахалинская трубопроводная система, 8 stuks, uiteinden op gedeelde nodes (gap 0,0 m); doorgetrokken | nee |

Aannemelijk-vlag: de bestemming (oliesterminal Prigorodnoje) staat in één bron [1]; dat staat in de beennaam, niet in de lijnstijl. Geen zeebeen: een tanker-laadplek (TLU) ligt ~5 km offshore, maar er is geen coördinaat (§7); de lijn eindigt waar het bewijs eindigt. Geen haven-aanloop nodig (geen kade).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-opf-nogliki` | kop leiding / procesinstallatie | OPF Nogliki (Sakhalin Energy) | 51.4166, 143.3660 | [1][6] | bron-gelegd (z15 gezien: omheind complex met procestreinen, tanks en een groot kampterrein noordelijk; kruis op de zuidrand bij de leidingkop; OSM-way 394946663 begint 7 m ernaast) |
| `ol-prigorodnoye-oet` | overslag leiding → tank/export | Prigorodnoje-oliesterminal, tankpark (Aniva-baai) | 46.6304, 142.9264 | [1][6] | bron-gelegd (z15 gezien: tankpark met twee grote witte tanks ~0,4 km zuidzuidwest en utiliteitsgebouw 0,1 km oost; LNG-complex 1,8 km west; OSM-way 579594727 eindigt op dit punt; Wikipedia: terminal ligt oostelijk van de LNG-plant [1]) |

Het LNG-anker `gas-prigorodnoye-plant` (46.6275, 142.9028; brief gas-prigorodnoye-sodegaura) is **niet hergebruikt**: het ligt 1,4 km van de lijn en 1,8 km westelijk van het oliepunt — een andere site. Geen overlap met die stroom.

## 4 · Via-punten
Geen corridorkeuze (één leiding, geen alternatief). Ter controle bij het bakken de 7 way-grenzen op de lijn (km vanaf OPF): 50.1045,142.7087 (178,7) · 49.1207,142.9328 (297,4) · 48.0997,142.5187 (432,8) · 47.9281,142.4989 (455,0) · 47.8277,142.4992 (467,1) · 47.0125,142.6739 (565,3) · 46.6422,142.8993 (619,5).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| OPF Nogliki | Sakhalin Energy (Gazprom 77,5% / Mitsui / Mitsubishi) | olie + condensaat + gas → stabiele olie naar leiding | ~9.500 m³/d olie/condensaat, 51 mcm/d gas | [1][4] |
| Prigorodnoje-oliesterminal | Sakhalin Energy | leiding → opslag 1,2 mln vaten → tanker via offshore TLU ~5 km | opslag 190.000 m³ | [4][7] |

## 6 · Stoppunt
De brief stopt bij het tankpark van Prigorodnoje: de offshore tanker-laadplek is niet gekarteerd en geen bron legt een lading aan een afnemer of raffinaderij. Fase C/D/E vervallen.

## 7 · Open punten
- **Volume:** 180 kb/d (ontwerp, Wikipedia-tekst) [1] tegen 395 kb/d in de infobox (niet gebruikt) en 88 kb/d na de OPEC+-korting van 2020 [2]; een Reuters-bron noemt ~4 Mt/j ≈ 80 kb/d [7]. Geen peiljaar-2025-cijfer gevonden; sitelaag/volumeagent: bij voorkeur 88 kb/d (laatst gemeten) of 180 kb/d als ontwerp.
- **TLU/exportzijde:** de Tanker Loading Unit (~5 km offshore Aniva-baai [7]) staat niet in OSM (scan bbox 46.58–46.70 / 142.80–143.10: alleen schoorstenen, torens, twee `seamark:type=berth` bij de LNG-jetty). Geen zeebeen getekend.
- **Lengte:** GEM 637 km is de TransSakhalin-lengte OPF → LNG-plant en oliesterminal, geen oliespecifiek cijfer; GEM-pagina is titelmatig de gasleiding (parallel tracé) [3].
- **Kuststuk bij de OPF** (OSM: 2×7,0 km onder de grond + 2×13,8 km onderwater, lagune Piltun, 51.4150,143.6609 → 51.4163,143.3673) en de offshore-platforms liggen vóór de OPF en zijn bewust niet getekend (ontwerp: fase A vanaf OPF).
- **Afnemer/sanctie:** Japan als afnemer en OFAC GL 55F (tot 18-12-2026) niet los gefetcht; qcintel achter paywall [5].
- De plaatsnaam Boatasyn (stroom-id) = OPF-locatie volgens het ketenontwerp; niet apart gecheckt.

## 8 · Bronnen
[1] Wikipedia, "Sakhalin-II" — ~180.000 bpd olie ontwerp, OPF, oliesterminal ten oosten van de LNG-plant, Aniva-baai. https://en.wikipedia.org/wiki/Sakhalin-II
[2] Wikipedia, "Sakhalin Energy" — olie-export sinds 1999; 2020: 108.000 → 88.000 bpd na OPEC+. https://en.wikipedia.org/wiki/Sakhalin_Energy
[3] GEM.wiki, TransSakhalin pipeline (Piltun-Prigorodnoye) — 637 km OPF → Prigorodnoje. https://www.gem.wiki/Piltun-Prigorodnoye_Pipeline
[4] Offshore Technology, "Sakhalin II" — OPF-capaciteit, ~800 km onshore, 190.000 m³ opslag. https://www.offshore-technology.com/projects/sakhalin2/
[5] qcintel, "US extends Japan's waiver for Russian oil from Sakhalin-2" — niet los gefetcht. https://www.qcintel.com/article/us-extends-japan-s-waiver-for-russian-oil-from-sakhalin-2-43213.html
[6] OpenStreetMap (ODbL), lokale Geofabrik `rusland-verrehoosten` (pyosmium, 2026-10-30): ways 394946663, 394946660, 394946668, 394946648, 409387387, 394946661, 209135245, 579594727; som 622,9 km, 1.248 punten. https://www.openstreetmap.org/way/394946663
[7] Web-samenvatting (WebSearch 2026-10-30): TLU ~5 km offshore, opslag 1,2 mln vaten, ~4 Mt/j (Reuters, oud). Niet los gefetcht. https://www.nsenergybusiness.com/projects/sakhalin-2-oil-and-gas-project/
[8] Esri World Imagery via `v2/tools/sat_check.py` (z14/z15): `sat-olie-boatasyn-prigorodnoye-opf-nogliki.png`, `…-oet-eind.png`, `…-oet-overzicht.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Bestand:** `v2/data/stroomroute-olie-boatasyn-prigorodnoye.json` (26,0 KB, versie 2, lonlat) · **functie:** `bak_olie_boatasyn_prigorodnoye()` in `v2/tools/bak_stromen.sh` · **tool:** `v2/tools/maak_leidingbeen_olie_boatasyn_prigorodnoye.py`.

| # | modaliteit | been | km gemeten | km brief | stijl |
|---|---|---|---|---|---|
| b1 | leiding | Trans-Sachalin-oliepijpleiding OPF Nogliki → Prigorodnoje (Sakhalin Energy, OSM-leiding; aannemelijk: één bron voor de bestemming) | 622,9 (1.241 punten) | GEM 637 (inferred), -2,2% | doorgetrokken |

Totaal 622,9 km, 1 been, 2 markers (`ol-opf-nogliki` 51.4166,143.3660 en `ol-prigorodnoye-oet` 46.6304,142.9264), beide 0,004-0,006 km van de lijn. Naad: n.v.t. (één been); de 8 ways sluiten op gedeelde nodes (0 m).

**Recept:** `python v2/tools/maak_leidingbeen_olie_boatasyn_prigorodnoye.py --schrijf` haalt de 8 way-ids (394946663, 394946660, 394946668, 394946648, 409387387, 394946661, 209135245, 579594727) uit de OSM-API (pyosmium is op deze machine geblokkeerd; de ways zijn dezelfde als in de pbf-scan van de brief) met cache, stikt ze in vaste volgorde op gedeelde nodes en schrijft `v2/build-cache/ais/graaf/olie-boatasyn-prigorodnoye-leiding-b1.geojson` (FeatureCollection). Daarna `bash v2/tools/bak_stromen.sh olie-boatasyn-prigorodnoye`.

**Toelichting leiding:** doorgetrokken want OSM heeft de leiding (man_made=pipeline, substance=oil, Sakhalin Energy, naam Транссахалинская трубопроводная система). Geen stippel, geen via-punten, geen haven-aanloop, geen zeebeen (TLU offshore niet gekarteerd), geen kopie; het kuststuk/de lagune bij de OPF en de gas-parallelleiding zitten er bewust niet in. Lengte-toets: 622,9 km tegen GEM 637 km = -2,2%, binnen ±15% (GEM is niet oliespecifiek).

**Toets:** `toets_knikken.py`: 6 knikken >= 60 graden (twee spikes ~50.095,142.716 en 46.648,142.889, rest krappe bochten in het OSM-tracé), 0 omkeringen, 0 terugloop; `toets_rechte_benen.py`: geen melding voor deze stroom; json.load OK, 1 been >= 2 punten, modaliteit `leiding`.

**Lessen:** (1) bij geblokkeerde pyosmium is de OSM-API per way-id een volwaardige route (patroon `maak_leidingbeen_olie_taishet_kozmino.py`), brief-ways staan dan in de cache. (2) De OSM-som uit de brief (622,9 km) komt na stikken exact terug; 1.248 punten in de brief worden 1.241 door het weglaten van dubbele knooppunten op de way-grenzen.

