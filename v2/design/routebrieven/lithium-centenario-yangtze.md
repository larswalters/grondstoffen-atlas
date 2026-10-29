# Routebrief (licht) · Lithium · Centenario-Ratones (Salta) → Rosario → China (Yangtze-monding)

**stroom-id:** `lithium-centenario-yangtze` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** lithiumcarbonaat uit Eramines Centenario-Ratones-plant (Salar Centenario-Ratones, Los Andes, Salta, ~3.900-4.000 m) gaat per **truck** (aannemelijk, wegvorm niet vermeld; 1.580 km volgens Eramine) over de Puna-wegen, RN51 via San Antonio de los Cobres, Salta, RN9/RN34 via Tucuman naar Terminal Puerto Rosario (TPR) en per containerschip via de Parana en de Zuid-Atlantische Oceaan naar China; de Chinese haven is niet gebronnd, dus het eindpunt is het conventie-anker Yangtze-monding (*aannemelijk: één bron*).
**Welke as van het verhaal:** *het Argentijnse Atlantische alternatief* voor de Chileense haven: de eerste export van Eramine (40 t, maart 2025) liep via Rosario, de truckbeweging is 1.580 km [1][2][3]. **24 kt LCE/j nameplate** fase 1 (Eramet 2023/2024; peiljaar 2024/25, volledige ramp-up gepland medio 2025) [7][8]; werkelijk geexporteerd is niet gepubliceerd (alleen 40 t en, via Chili, 80 t [5]). Sinds eind 2025 gaat een deel via Puerto Angamos (Chili), niet getekend [5][6].

## 1 · Ketenkaart
```
Centenario-Ratones-plant `li-centenario-plant` ──(b1 truck · plantweg → RN51 via San Antonio de los Cobres → Quebrada del Toro → Salta → RN9/RN34 via Tucuman → Rosario · 1.580 km Eramine, gemeten 1.491,3)──►
Terminal Puerto Rosario `li-tpr-kade` ──(b2 zee · Parana → Rio de la Plata → 50°S-lane om Afrika → Straat van Soenda → Taiwanstraat · MARNET 21.185 km, geen aanloop)──►
MARNET-eindknoop ──(b3 stippel · 8,6 km, letterlijke kopie bak_lithium)──► Yangtze-monding `li-yangtze-monding` ⏹ stoppunt (aannemelijk)
vertakking (niet getekend): Chileense route Cocel (Salta) → Paso de Jama → Puerto Angamos [5][6]
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (aannemelijk; Forbes noemt trucks, 40 t, ULOG [4]) | `li-centenario-plant` → `li-tpr-kade` | plantweg/RP129 → RN51 (SAC, Quebrada del Toro) → Salta → RN9 → Tucuman → RN34 → Rosario | 1.580 (Eramine/Panorama Minero, 20-02-2025 [1]); gemeten 1.491,3 = -5,6% | maak_stroombeen_weg (extract argentina) | nee |
| b2 | B | zee (containerschip: "being containerized" [3]) | `li-tpr-kade` → MARNET-eindknoop Yangtze | Parana, Rio de la Plata, 50°S-lane ten zuiden van Afrika, Straat van Soenda, Taiwanstraat (MARNET beslist) | 21.185,2 (MARNET-meting; geen gepubliceerde lengte; ontwerp 20.500-21.500) | MARNET | aanloop: nee (TPR-kade 2,13 km van zeeknoop 5116) |
| b3 | B | zee (overgang) | MARNET-eindknoop 31.51,121.4187 → 31.4512,121.4769 | — | 8,6 (letterlijke kopie `bak_lithium`) | rechte stippel | ja, hier reikt MARNET niet; Chinese haven niet gebronnd |
Geen binnenvaartbeen Rosario → Rio de la Plata: de haalbaarheidstoets vond geen waterpad over de bulklaag (maak_rivierbeen), en MARNET vaart zelf over de Parana.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-centenario-plant` | plant / laadplek | Eramine Centenario-Ratones, Salar Centenario-Ratones, Los Andes, Salta | -24.8828, -66.7328 | [9] projectpunt Ministerie van Economie (24°52'58"S 66°43'58"W); geen plantcoordinaat | onzeker (z13/z15 gezien: aan de zuidrand van een salar met industrieel terrein, wegennet en grote vijvervelden 2-4 km noordoost; geen plantgebouw aan te wijzen, exploitant niet bevestigd; kandidaat noord op -24.115,-66.975 met vijvers en loodsen is niet gekozen) |
| `li-tpr-kade` | overslag truck → containerschip | Terminal Puerto Rosario (TPR, Muelles I en II), Rosario | -32.9645, -60.6208 | [2][3] terminal benoemd; punt = OSM (Nominatim) | aannemelijk (z15 gezien: smalle kadestrook met lange loodsen langs de rivier, TPR-loods voor lithium genoemd [2]; containerstapels 1,3 km zuidelijker zijn niet als TPR bevestigd) |
| `li-yangtze-monding` | aanlanding China (stoppunt) | Yangtze-monding | 31.42704, 121.47618 | hergebruik `lithium-atacama-antofagasta.md` §3 | aannemelijk (conventie-anker; haven niet gebronnd; MARNET-eindknoop 10,7 km ervandaan, stippel dicht 8,6 km) |

## 4 · Via-punten (alleen b1; hergebruikt uit `lithium-saldeoro-guemes` en `lithium-olaroz-naraha`, alle snaps <= 0,09 km)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | RN51 zuidrand San Antonio de los Cobres | -24.2278, -66.3187 | de Puna-weg van de plant sluit hier aan op de RN51 (120,6 km, 119 km over kleine klassen) |
| b1 | 2 | RN51 Quebrada del Toro (Campo Quijano) | -24.8956, -65.6047 | pint de afdaling naar Salta |
| b1 | 3 | Salta oostrand (RN9/circunvalacion) | -24.7952, -65.3670 | rond de binnenstad heen naar de RN9 |
| b1 | 4 | Tucuman (RN9/RN34-knoop) | -26.8241, -65.2226 | pint RN34 zuidwaarts i.p.v. een andere route; hergebruikt uit olaroz-naraha, gemeten stuk 900,3 km valt voor ca. 50% samen met die stroom |
| b1 | 5 | Rosario | -32.9442, -60.6505 | laatste knoop voor TPR (4,2 km); hergebruikt uit olaroz-naraha, ligt in het centrum maar kost geen omweg |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Centenario-Ratones, fase 1 | Eramine Sudamerica (Eramet 50,1 % / Tsingshan 49,9 %) | pekel (DLE) → batterijgradig Li2CO3 | 24 kt Li2CO3/j nameplate (24 kt LCE/j); ingebruikname 3-7-2024 | [7][8][11][12] |
| TPR | Terminal Puerto Rosario | opslag en containerisering → container | niet gepubliceerd | [2][3] |

## 6 · Stoppunt
De brief stopt bij de Yangtze-monding: Datamar en La Capital noemen alleen "China", geen Chinese haven of afnemer [2][3]; fase D vervalt, fase E vervalt.

## 7 · Open punten
- **Plantanker onzeker:** alleen een projectpunt uit een overheidsportfolio [9]; Nominatim, Photon en een OSM-scan kennen de plant niet. De lijn begint op dat punt; de plant kan kilometers verderop liggen (ook de noordelijke vijvercomplexen kwamen in beeld).
- **China als bestemming** staat in twee kranten en Datamar, geen haven genoemd; Forbes noemt China niet [2][3][4].
- **Weg-vorm:** trucks genoemd door Forbes [4], containers pas bij TPR [3]; consolidatie in het Cocel-depot (Salta) is alleen voor de Chileense route bevestigd [5][6].
- **Datum Chileense route:** Redimin 18-12-2025 [5] tegen LM Neuquen "maart 2026" [6]; niet getekend, wel relevant: de Rosario-lading van 2025 is niet de enige of nu dominante route (Perfil 2024 verwachtte Chili [10]).
- **Volume:** 24 kt LCE/j is nameplate; geexporteerd bevestigd: 40 t via Rosario (maart 2025), 80 t via Angamos (2025) [2][5]. Wegkm 1.580 is bedrijfsopgave zonder routebeschrijving; gemeten 1.491,3.
- **Naad:** truckeinde (TPR-kade) en MARNET-start liggen 2,13 km uiteen (< 5 km, geen aanloop nodig). Eerste 119 km van b1 loopt over OSM-klassen tertiary/unclassified/track in de Puna.

## 8 · Bronnen
[1] Panorama Minero, "Eramine Completes the First Export of Lithium Carbonate Produced in Salta", 20-02-2025 — 40 t, 1.580 km van Centenario-Ratones naar Puerto Rosario. https://panorama-minero.com/en/news/eramine-completes-the-first-export-of-lithium-carbonate-produced-in-salta
[2] La Capital (Rosario), 10-03-2025 — TPR (Muelles I en II) laadde 40 t Li2CO3 van Eramine voor China, loods voor lithium. https://www.lacapital.com.ar/suscriptores/el-puerto-rosario-se-abrio-la-ventana-que-no-se-escape-la-tortuga-n10183239.html
[3] Datamar, "Rosario port ships Argentina's first lithium carbonate export to China", 07-03-2025 — TPR, vertrek 5 maart, in containers, China zonder haven. https://datamarnews.com/noticias/rosario-port-ships-argentinas-first-lithium-carbonate-export-to-china/
[4] Forbes Argentina, 20-02-2025 — vrachtwagens, ULOG met onderaannemer, Salar Centenario-Ratones naar Rosario. https://www.forbesargentina.com/money/sale-primera-exportacion-litio-salta-empresas-participan-n67870
[5] Redimin, 18-12-2025 — eerste export via Puerto Angamos, Cocel-depot Salta, Paso de Jama, 80 t in 5 containers, "alternatief voor de Atlantische route via Rosario". https://www.redimin.cl/eramine-inaugura-ruta-logistica-por-chile-y-concreta-primera-exportacion-de-litio-desde-puerto-de-antofagasta
[6] LM Neuquen (Mase), "Guerra logistica del litio" — Cocel als eerste depot fiscal van Salta, Paso de Jama, Angamos, datering maart 2026. https://mase.lmneuquen.com/mineria/guerra-logistica-el-litio-rosario-busca-disputarle-chile-la-salida-la-mineria-n1249264/amp
[7] Elektroauto-News, 19-07-2024 — Centenario fase 1, 24.000 t/j batterijgradig carbonaat, inbedrijfname juli 2024. https://www.elektroauto-news.net/news/eramet-lithiumproduktion-argentinien
[8] Eramet, "Eramet in Argentina, Centenario-Ratones Lithium Project", maart 2023 — 50,1 % / 49,9 %, 24 ktpa fase 1, ramp-up medio 2025. https://www.eramet.com/wp-content/uploads/2023/04/2023-03-08-Eramet_Centenario_Investors-Presentation.pdf
[9] Argentina.gob.ar, "Portfolio of advanced projects, lithium" 2024 — locatie 24°52'58"S 66°43'58"W, toegang via San Antonio de los Cobres, RP129. https://www.argentina.gob.ar/sites/default/files/portfolio_lithium_2024.pptx.pdf
[10] Perfil, "Salta entro a la era del litio" — plant op ~3.800 m, 160 km van Salta, in 2024 verwachte uitvoer via Chili. https://www.perfil.com/noticias/economia/salta-entro-a-la-era-del-litio-inauguro-su-primera-mina-productora.phtml
[11] iProfesional, 01-07-2024 — Centenario-Ratones ~4.000 m, activering 3 juli 2024. https://www.iprofesional.com/negocios/408864-franceses-activan-primera-mina-de-litio-en-salta
[12] Mining Data Online — Centenario Phase I DLE commissioned 3-7-2024. https://miningdataonline.com/property/2069/Centenario-Ratones-Project.aspx
[13] Esri World Imagery via `v2/tools/sat_check.py` (`v2/build-cache/satcheck/`): `sat-lithium-centenario-yangtze-gov-24.8828.png`, `-plant-a.png`, `-plant-b.png`, `-plant-noord.png`, `-streek.png`, `-tpr.png`.
[14] OSM-wegscan (Geofabrik argentina, `wegscan_puur.py`, profiel `lithium-centenario-yangtze-centenario-tpr`) en MARNET-meting via `hecht_marnet.py` (21.185,2 km, snaps 2,13 en 13,0 km).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)

**Stroom `lithium-centenario-yangtze`** → `v2/data/stroomroute-lithium-centenario-yangtze.json` (289,1 KB, versie 2, lonlat) — 3 benen, 22.685,3 km, 13.805 punten, 3 markers. Registratie centraal (sleutel `li-cy`).

| # | modaliteit | km | naad | opmerking |
|---|---|---|---|---|
| b1 | truck | 1.491,5 | 0 | gemeten, -5,6% op de gepubliceerde 1.580 (Eramine); 11.646 punten, doorgetrokken |
| b2 | zee | 21.185,2 | 2,13 | MARNET kade TPR -> Yangtze (snaps 2,13 en 13,0 km), doorgetrokken |
| b3 | zee (stippel) | 8,6 | 0 | MARNET-eindknoop -> Yangtze-overgang, letterlijke kopie van `bak_lithium` |

**Recept:** `bash v2/tools/bak_stromen.sh lithium-centenario-yangtze` (functie `bak_lithium_centenario_yangtze`); wegbeen eerst via `python v2/tools/wegscan_puur.py --profiel lithium-centenario-yangtze-centenario-tpr` (profiel in `maak_stroombeen_weg.py`, extract argentina, cache hergebruikt) naar `lithium-centenario-yangtze-weg-centenario-tpr.geojson`.

**Toelichting:**
- **Stippel (b3):** hier reikt MARNET niet; Chinese haven niet gebronnd. Geen andere stippel, geen haven-aanloop (TPR-kade 2,13 km van zeeknoop 5116, < 5 km).
- **Aannemelijk: een bron:** bestemming China en de wegvorm (truck) staan in de beennamen; de lijnen zijn doorgetrokken.
- **Geen binnenvaartbeen** Rosario -> Rio de la Plata: MARNET vaart zelf over de Parana.
- **Toets:** km b1 binnen +-15% (-5,6%); naden 0 / 2,13 / 0 km (max 2,13); markers plant en TPR op de lijn (0 km); `toets_knikken`: 0 omkeringen, 0 terugloop (50 knikken >= 60 gr, vrijwel allemaal bergserpentines in de Puna en op de RN51); `toets_rechte_benen`: alleen de gedeelde Yangtze-stippel (omwegfactor 1,005, bewust).
- **Bevindingen:** (1) marker `li-yangtze-monding` ligt 2,69 km van de lijn (conventie-anker, patroon `bak_lithium`, stippeleinde 31,4512/121,4769); (2) bestand 289 KB, net onder de ~300 KB-grens door de 11.646 wegpunten; (3) plantanker onzeker (projectpunt), lijn begint op dat punt; (4) Tucuman- en Rosario-via liggen in stadscentra, hergebruikt, geen meetbare omweg; (5) Chileense route via Cocel/Angamos niet getekend.
- **Lessen:** profiel en functie stonden al uit een eerdere poging (getest, LF 0 CRLF); herbakken gaf identiek resultaat. Hergebruik van via-punten uit saldeoro-guemes en olaroz-naraha (snaps <= 0,09 km) werkt.
