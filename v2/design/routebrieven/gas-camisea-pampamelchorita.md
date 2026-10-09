# Routebrief (licht) · gas — Camisea (Malvinas) → Chiquintirca → Pampa Melchorita (Peru)

**stroom-id:** `gas-camisea-pampamelchorita` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 9) · **status:** gebakken
**Keten in één zin:** aardgas uit de Camisea-velden (Urubamba, Cusco) wordt in het **Malvinas-gasplant** van vloeistoffen ontdaan, gaat per **ondergrondse leiding** (TGP-trunk, dan de Peru LNG-leiding, samen 601 km) over de Andes naar de **Peru LNG-fabriek** bij Pampa Melchorita (San Vicente de Cañete) en wordt daar tot LNG verwerkt: de eerste LNG-fabriek van Zuid-Amerika. Stoppunt = de fabriek; geen LNG-been.
**Welke as van het verhaal:** Camisea naar de eerste LNG-export van Zuid-Amerika. Nominaal 4,4 Mtpa ≈ 6,0 bcm/j [1]; werkelijk 2023: 55 ladingen, ca. 3,69 Mt ≈ 5,0 bcm/j [3]; 2024: 57 ladingen, 205 TBtu (opgave Hunt Oil) [4] (1 Mt LNG ≈ 1,36 bcm). Bestemmingen wisselen per maand (VK, Zuid-Korea, Japan, China, Spanje, Canada) [3].

## 1 · Ketenkaart
```
Camisea-velden (San Martín, Cashiriari; niet getekend, geen bronpunt)
   ──► Malvinas-gasplant `gas-camisea-malvinas` (Cusco, Urubamba-oever)
   ──(b1 leiding · Camisea Pipeline/TGP, OSM way 227404355 · 199,4 km OSM)──►
Chiquintirca-knoop `gas-camisea-chiquintirca` (Ayacucho, afsplitsing Peru LNG; naad 0,28 km)
   ──(b2 leiding · Gasoducto Peru LNG, OSM way 239636419 · 401,6 km OSM tegen 408 gepubliceerd)──►
Peru LNG Pampa Melchorita `gas-camisea-melchorita` ⏹ stoppunt (LNG-bestemmingen wisselen; Shell neemt de ladingen af)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | `gas-camisea-malvinas` → `gas-camisea-chiquintirca` | Camisea Pipeline (TGP): Urubamba-dal, Andes-pas, Chiquintirca | 199,4 OSM; geen gepubliceerde deellengte (hemelsbreed 156,6 km, geen wegkm) [2][5] | OSM-way 227404355, `man_made=pipeline`, `substance=gas`, ondergronds, `fixme` (geschat, wolken); 1.805 punten, **omgekeerd** (OSM loopt Chiquintirca → Malvinas) | nee |
| b2 | B | leiding | `gas-camisea-chiquintirca` → `gas-camisea-melchorita` | Gasoducto Peru LNG (34″, Techint): Ayacucho → Ica-kust → Pampa Melchorita | 401,6 OSM tegen 408 gepubliceerd [1] = −1,6% | OSM-way 239636419, `man_made=pipeline`, `substance=gas`, ondergronds, `fixme=yes`; 1.061 punten, **omgekeerd** (OSM loopt Melchorita → Chiquintirca) | nee |

Naad b1→b2: 0,28 km (A-eind -13.0508,-73.6965 → B-begin -13.0526,-73.6983), ruim < 5 km; geen stippel nodig. Totaal 601,0 km, 0% stippel. Geen zee-, weg- of luchtbeen, dus geen haven-aanloop. De vooraf gestikte geojson's staan klaar (zie §9-aanwijzing).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-camisea-malvinas` | leidingkop / gasplant | Malvinas-gasplant (Pluspetrol/TGP), Urubamba | -11.8502, -72.9421 | [2][5][6] | bron-gelegd (z15/z16 gezien: zuidpunt van het Malvinas-complex, vlak bij de landingsstrip: servicecompound, wegknoop en gebouwen in het bos; de procesblokken en tanks liggen 0,8–1,1 km noordnoordwest, zie §7) |
| `gas-camisea-chiquintirca` | knoop / afsplitsing | Chiquintirca-station (TGP-trunk → Peru LNG-leiding) | -13.0517, -73.6974 | [1][5][6] | bron-gelegd (z15 gezien: omheinde installatie met witte gebouwen op een Andes-terras, in een dal met akkers; 0,14 km van beide leidinguiteinden) |
| `gas-camisea-melchorita` | fabriek / stoppunt | Peru LNG, Pampa Melchorita (San Vicente de Cañete) | -13.2426, -76.2918 | [1][5][6] | bron-gelegd (z15/z16 gezien: groot LNG-complex in de woestijn langs de Panamericana: procesblokken, witte gebouwen, twee bolvormige LNG-tanks 1,5 km ZW en de pier de zee in; punt ligt binnen de terreingrens) |

Hergebruik: geen. `gas-sitelaag.json` en de gas-brieven kennen Peru niet; het Malvinas-punt is de OSM-leidingkop (marker op de lijn), de coördinaat van Wikipedia (-11.8387,-72.9503) ligt aan de rivierrand van de fabriek. Beelden: `v2/build-cache/satcheck/sat-gas-camisea-pampamelchorita-{malvinas-osm,malvinas-wiki,malvinas-z16,chiquintirca,melchorita,melchorita-z16}.png` [7].

## 4 · Via-punten
Niet van toepassing: elk been is één doorlopende OSM-leiding (geen corridorkeuze, geen router).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Malvinas-gasplant | Pluspetrol (operator Camisea); leiding TGP (Tecgas, Pluspetrol, Hunt, SK, Sonatrach, Graña y Montero) | veldgas → gas zonder vloeistoffen (LPG) | niet gebrond | [2] |
| Peru LNG | Hunt Oil (operator, 35%), MidOcean Energy (35%), Shell (20%, neemt alle LNG af), Marubeni (10%) | pijpleidinggas → LNG, twee tanks van 130.000 m³ | 4,4 Mtpa ≈ 6,0 bcm/j nominaal; 2023 ca. 5,0 bcm/j | [1][3][8] |

## 6 · Stoppunt
De brief stopt bij de LNG-fabriek: Shell neemt de ladingen af en de bestemming wisselt per maand (VK, Korea, Japan, China, Spanje); een LNG-been zou een niet-bestaande vaste route suggereren. Upstream stopt bij het Malvinas-plant: de Camisea-velden zelf hebben geen gebronde coördinaat.

## 7 · Open punten
- **Malvinas-anker ligt aan de zuidrand van het complex:** OSM-leidingkop -11.8502,-72.9421 ligt op faciliteitsterrein (landingsstrip, servicecompound), maar 0,8–1,1 km ZZO van de procesblokken (ca. -11.8408,-72.9455). Gekozen voor de leidingkop zodat de marker op de lijn staat (≤0,5 km); de gloed valt dus ~1 km van de installatie. Geen last-mile gebouwd (< 2 km).
- **OSM-geometrie indicatief:** beide ways dragen `fixme` (b1: "estimated due to coverage by clouds", bron Bing/MapBox; b2: `fixme=yes`, bron Bing). Doorgetrokken (gemeten OSM), onzekerheid staat hier en in de beennaam, niet in de lijnstijl.
- **Geen gepubliceerde lengte voor b1**; ±15%-toets alleen op b2 (−1,6% tegen 408 km) en op het totaal niet te leggen. De aansluiting Malvinas → Chiquintirca volgt de TGP-trunk (totale TGP naar Lima 540 km volgens Wikipedia [2]).
- **Geen jaarvolume voor de Camisea-leiding zelf** (alleen de afname van Peru LNG gebrond); capaciteit Malvinas niet gevonden.
- **Leveringsonderbrekingen:** twee leidingbreuken/-storingen stopten de export (februari 2018 na een aardverschuiving; maart 2026: 2 ladingen, geen in april, weer 5 in mei en juni) [9][4]. Volume is dus variabel.
- **Eigenaren:** het ketenontwerp noemde SK; recente bronnen noemen MidOcean (EIG) met 35%; SK-uitstap niet apart bevestigd.
- **Sitelaag mist Peru LNG en Malvinas** (centraal: 4,4 Mtpa ≈ 6,0 bcm/j als gloedgewicht; Malvinas zonder gewicht).

## 8 · Bronnen
[1] Wikipedia (EN), "Peru LNG" — Pampa Melchorita, km 170 Panamericana Sur, 4,4 Mtpa, 2 tanks van 130.000 m³, 34″ leiding 408 km vanaf Chiquintirca, Hunt/SK/Shell/Marubeni (oud). https://en.wikipedia.org/wiki/Peru_LNG
[2] Wikipedia (EN), "Camisea Gas Project" — Camisea-pijpleiding 540 km via Malvinas, tweede leiding 714 km naar Lima/Callao, operator Pluspetrol, TGP-consortium. https://en.wikipedia.org/wiki/Camisea_Gas_Project
[3] LNG Prime, "Peru LNG's 2023 exports rise" — 55 ladingen, ca. 3,69 Mt in 2023, bestemmingen. https://lngprime.com/americas/peru-lngs-2023-exports-rise/101810
[4] LNG Prime, "Peru LNG expects to load 57 cargoes this year" (2024) en "Peru LNG sent five cargoes in May" (2026): 57 ladingen 2024, 205 TBtu (opgave Hunt Oil); 5 ladingen mei 2026 na nul in april. https://lngprime.com/americas/peru-lng-expects-to-load-57-cargoes-this-year/131427 · https://lngprime.com/americas/peru-lng-sent-five-cargoes-in-may/188773/
[5] OpenStreetMap-bijdragers (ODbL), via api.openstreetmap.org (2026-10-09) — way 227404355 "Camisea Pipeline" (1.805 punten, 199,4 km) en way 239636419 "Gasoducto Perú LNG" (1.061 punten, 401,6 km, operator Perú LNG). https://www.openstreetmap.org/way/227404355 · https://www.openstreetmap.org/way/239636419
[6] Esri World Imagery via `v2/tools/sat_check.py` (z15/z16, live, 2026-10-09).
[7] Satellietbeelden: `v2/build-cache/satcheck/sat-gas-camisea-pampamelchorita-*.png` (zie §3).
[8] LNG Prime (zoekresultaten 2026): Shell 20% en neemt alle volumes af, Hunt 35%, MidOcean Energy (EIG) 35%, Marubeni 10%. https://lngprime.com/americas/peru-lngs-2023-exports-rise/101810
[9] Offshore Energy, "Peru resumes LNG exports after pipeline rupture" (2018) — breuk 3 februari 2018 door aardverschuiving. https://offshore-energy.biz/?p=59093
[10] Ketenontwerp + haalbaarheidstoets M31 golf 9 (orkestrator).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 9)
**Bestand:** `v2/data/stroomroute-gas-camisea-pampamelchorita.json` (61,9 KB, versie 2, `lonlat`) · **recept:** `bash v2/tools/bak_stromen.sh gas-camisea-pampamelchorita` (functie `bak_gas_camisea_pampamelchorita`, `hecht_marnet.py route` met twee `--been-geojson`, drie `--marker`, geen router, extract, via-punt, profiel of stippel). **Titel:** Gas · Malvinas → Chiquintirca → Pampa Melchorita (Peru). Het id noemt het werkelijke eindpunt (Pampa Melchorita), geen afwijking.

| # | modaliteit | km gemeten | punten | brief | naad naar volgend been | stippel |
|---|---|---|---|---|---|---|
| b1 | leiding | 199,4 | 1.805 | 199,4 OSM, geen gepubliceerde deellengte (hemelsbreed 156,6, geen wegkm) | 0,28 km (voor b2) | nee |
| b2 | leiding | 401,6 | 1.061 | 408 gepubliceerd = -1,6% (binnen 15%) | n.v.t. | nee |
| | | **601,0** | 2.866 | | | 0% stippel |

**Markers (3):** Malvinas 0,004 km, Chiquintirca 0,137 km, Pampa Melchorita 0,004 km van de lijn (alle binnen 0,5 km; Chiquintirca ligt tussen de twee leidinguiteinden, anker is geen routeerpunt).

**Leidingen:** beide benen zijn de OSM-ways van §2 (227404355 en 239636419), in OSM tegengesteld aan de reisrichting en daarom vooraf omgekeerd en als FeatureCollection weggeschreven (`$BEEN/gas-camisea-pampamelchorita-leiding-malvinas-chiquintirca.geojson` en `-chiquintirca-melchorita.geojson`). Doorgetrokken, geen stippel: er is geen net-gat. Beide ways dragen `fixme` (geschat, Bing/wolken): de onzekerheid staat in de beennaam ("OSM-geometrie indicatief"), niet in de lijnstijl. Geen offshore-stuk en geen eigen-terrein-stuk: b1 begint op het Malvinas-terrein en b2 eindigt binnen de Peru LNG-terreingrens.

**Toets:** km per been als in de brief (b2 -1,6%), naden 0 en 0,28 km (norm < 5 km), `toets_knikken.py`: 46 knikken ≥ 60° waarvan 1 omkering (172° op -12.4596,-73.0562, R 23 m, "scherpe bocht, echt", 0 terugloop) en rest spikes met R 20-130 m: dat zijn kartering-hoekpunten van de ondergrondse leiding (`fixme`), geen routefout; `toets_rechte_benen.py --min-km 5`: geen regel voor deze stroom (omwegfactor niet 1,000). `json.load` ok, versie 2, `lonlat`, modaliteiten {leiding}, elk been ≥ 2 punten.

**Lessen:** (1) een volledig OSM-gedekte leiding is de goedkoopste keten (geen router, geen slot-zwaar werk behalve de bake zelf, 30 s); (2) de vooraf gestikte FeatureCollection moet in reisrichting staan, de bake draait niets om; (3) de gloed van Malvinas valt ~1 km van de procesblokken (§7) omdat het anker de leidingkop is.
