# Routebrief (licht) · Grafiet · Marovintsy (Gallois) → RN 11a / RN 2 → Toamasina (Madagaskar)

**stroom-id:** `grafiet-marovintsy-toamasina` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** vlokgrafiet uit de Marovintsy-mijn van Etablissements Gallois (oostkust, ~10 km N van Vatomandry) gaat per truck over de lokale weg, RN 11a en RN 2 via Brickaville naar de haven van Toamasina; daar stopt de brief, want geen bron koppelt de lading aan een met naam genoemde afnemer of kade.
**Welke as van het verhaal:** tweede Madagaskar-as aan de oostkust, naast `grafiet-molo-duisburg` (zuidwest). Gallois (drie afzettingen: Antsirakambo, Marovintsy en één onbenoemde) produceerde 30 kt/j in 2025e [5]; in 2018 exporteerde Gallois 46,7 kt, 99% van de Malagassische grafietexport ging naar China [2]. Jaarvolume Marovintsy zelf: onbekend (§7), orde 10 kt/j (sitelaag-schatting). Eenheid kt grafiet per jaar, peiljaar 2025.

## 1 · Ketenkaart
```
Marovintsy-mijn/plant `gr-marovintsy-mijn` ──(b1 truck · lokale weg → RN 11a → Brickaville → RN 2 · OSRM ~176 km, geen gepubliceerde wegkm · aannemelijk: één bron voor de bestemming)──►
Toamasina-haven `gr-toamasina-kade` (hergebruikt anker) ⏹ STOPPUNT (geen zeebeen: geen met naam genoemde afnemer of haven van bestemming)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-marovintsy-mijn` → `gr-toamasina-kade` | RN 11a (vanaf Vatomandry noordwaarts, refs uit de tool-proef) + RN 2 (Brickaville–Toamasina, 105 km [8]) [8][9][10] | geen gepubliceerde totaalkm; OSRM 176 (haalbaarheidstoets), tool-proef 178,0 km (+1,2%); alleen het RN 2-deel is bron-km (105) | `maak_stroombeen_weg.py` (extract `madagaskar`) | nee |

Beennaam: `Marovintsy → Toamasina (RN 11a → RN 2) (aannemelijk: één bron)`. Geen zeebeen: de Toamasina-kade is hergebruikt uit `kobalt-ambatovy-toamasina` en bestaat alleen als marker (haven-aanloop n.v.t.).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-marovintsy-mijn` | mijn/plant (kop) | Marovintsy-mijn (Etablissements Gallois), Sahamatevina, Vatomandry | -19.2401, 48.9488 (letterlijk uit `v2/design/grafiet-sitelaag.json`, id `w-gallois-marovintsy`) | [1][3][5][7] + eigen z15-blik | bron-gelegd (z15 gezien: groot open-pit- en wascomplex met turkooise bezinkvijvers, het kruis ligt op de zuidrand bij een plantgebouw met blauwgroene daken en een zandweg naar het zuiden; het OSM-gehucht Antsapanana Gallois ligt 3,5 km NW). De sitelaag zet hem op onzeker, dat is strenger dan nodig; een bron met coördinaat ontbreekt, de ligging rust op naam + toponiem + beeld |
| `gr-toamasina-kade` | overslag/stoppunt | Toamasina-haven (in `co-toamasina-kade` Ambatovy Bulk Jetty genoemd; z15 toont het hoofdhavengebied) | -18.1556, 49.4278 (letterlijk hergebruikt uit `kobalt-ambatovy-toamasina.md`) | [11] + eigen z15-blik | bron-gelegd (z15 gezien: havenvinger met kranen, schepen langs de kade, containerstapels op het achterterrein) |

Beelden: `v2/build-cache/satcheck/sat-grafiet-marovintsy-toamasina-mijn.png`, `sat-grafiet-marovintsy-toamasina-kade.png`.

## 4 · Via-punten (alleen landbeen b1, in reisvolgorde; (lon, lat) voor het profiel)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Marovintsy-mijn (anker) | -19.2401, 48.9488 | kop; de lokale mijnweg loopt noordwaarts naar de RN 11a |
| b1 | 2 | Antsampanana, Mahatsara (RN 11a) | -18.9619, 48.9679 | pint de noordwaartse hoofdweg richting Brickaville (Mahatsara [10]); 0,004 km van de tool-lijn |
| b1 | 3 | Brickaville (Rianila-oversteek) | -18.8231, 49.0706 | pint de aansluiting op RN 2 bij Brickaville [8]; punt ligt 0,7 km van het plaatsmidden, niet in het centrum; 0,004 km van de tool-lijn |
| b1 | 4 | Tsaratampona (RN 2) | -18.4532, 49.1441 | pint de RN 2 op het middenstuk Brickaville–Toamasina tegen een uitbuiging naar een zijtak; 0,005 km van de tool-lijn |
| b1 | 5 | Toamasina-haven (anker) | -18.1556, 49.4278 | staart |

Profiel: extract `madagaskar`, refs `RN 11a` en `RN 2`, `corridorKlassen` tertiary en unclassified, `vensterKm` 40. De haalbaarheidstoets reed dit met snaps onder 0,25 km (aanloop kop 0,22, staart 0,06).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Marovintsy-mijn en wasinstallatie | Etablissements Gallois S.A. (private Chinese onderneming [5]) | grafiet-erts (3–10% C) → vlokconcentraat 85–90% C (flotatie) | ontwerp 60 kt/j (Marovintsy), 80 kt/j (Antsirakambo) [3]; realistisch 10–15 kt/j (sitelaag); Gallois totaal 30 kt/j 2025e [5] | [3][5] |

## 6 · Stoppunt
De brief stopt bij de Toamasina-haven: bronnen noemen alleen markten (USGS: China 99% van de export in 2018 [2]; Gallois zelf: Europa, Amerika, India, Turkije, Japan [6]) en geen afnemer, schip of haven van bestemming, dus fase B en D vervallen. De bestemming "Toamasina" is één bron: Gallois noemt Tamatave als enige haven [6] en USGS plaatst de mijn "near Tamatave" [2].

## 7 · Open punten
- **Exporthaven niet gebronde:** geen bron zegt dat Marovintsy-lading via Toamasina vertrekt; [6] noemt Tamatave voor Gallois als geheel. Toamasina als enige oostkusthaven is aanname (daarom "aannemelijk: één bron").
- **Geen gepubliceerde wegkm** voor dit traject: 176 km is OSRM, 105 km (Brickaville–Toamasina) is de enige bron-km. De ±15%-toets is hier een indicatie, geen norm.
- **Volume Marovintsy onbekend:** 30 kt/j is Gallois totaal over drie afzettingen [5]; de ontwerpcapaciteit 60 kt/j [3] ligt een orde boven de productie (USGS: 46,7 kt export in 2018 [2]); 10 kt/j is een schatting uit de sitelaag.
- **Tegenstrijdige afstand:** [6] noemt het mijngebied "45 km van Tamatave port"; dat past bij Antsirakambo bij Brickaville, niet bij Marovintsy (~130 km hemelsbreed). Antsirakambo (-18.448, 49.187 in de sitelaag) is een aparte, kortere keten.
- **Afnemers tegenstrijdig:** USGS 2018 (99% China) tegenover het bedrijfsverhaal over Europa en Amerika [6]; L'Express 2026 zegt dat Gallois "plus modestement" doorgaat [12].
- **Mijnanker zonder bron-coördinaat;** de precieze plantpoort en de aansluiting op de openbare weg zijn niet gezien (site-niveau, geen last-mile-been).
- **Sitelaag:** `w-gallois-marovintsy` staat op onzeker; de orchestrator kan dit na de bake gelijktrekken (niet door mij gewijzigd).
- **Webbudget:** 1 WebSearch gebruikt; verder Wikipedia-API, Nominatim en WebFetch/pypdf op de bronnen.

## 8 · Bronnen
[1] Wikipedia (EN), "Mining industry of Madagascar": "Marovinsty mine, near Vatomandry (graphite, Ets. Gallois S.A.)"; "Artsirakambo mine, near Brickaville". https://en.wikipedia.org/wiki/Mining_industry_of_Madagascar
[2] USGS Minerals Yearbook 2019, Madagascar: Gallois Mine "near Tamatave", capaciteit 150.000 t/j; Gallois-export 46.723 t in 2018 (10.702 t in 2017); China 99% van de grafietexport. https://pubs.usgs.gov/myb/vol3/2019/myb3-2019-madagascar.pdf
[3] L'Élémentarium, "Graphite" (2022): Gallois 140.000 t/j in twee mijnen (Antsirakambo 80.000, Marovintsy 60.000), oostkust, regio Toamasina; productie 2017 60.000 t. https://lelementarium.fr/wp-content/uploads/2018/08/Graphite-2022.pdf
[4] USGS Mineral Commodity Summaries 2026, Graphite: Madagascar 85.000 t (2024), 80.000 t (2025e). https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-graphite.pdf
[5] IISD, "Country profile Madagascar" (2026): Gallois (Antsirakabo, Marovintsy en één onbenoemde afzetting), productie 2025e 30.000 t; Etablissements Gallois S.A., private Chinese onderneming. https://www.iisd.org/system/files/2026-07/country-profile-madagascar.pdf
[6] AsianMetal, interview Gallois Graphite (2020): mijngebied 45 km van Tamatave International Port; capaciteit twee sites; markten Europa, Amerika, India, Turkije, Japan. https://wap.asianmetal.com/interview/2020/interview_qiangcuiEn.shtml
[7] OpenStreetMap via Nominatim (ODbL), bevraagd 2026-10-30: dorp Marovintsy (-19.2401, 48.9488, Sahamatevina, Vatomandry) en gehucht "Antsapanana Gallois" (-19.2185, 48.9135). https://nominatim.openstreetmap.org
[8] Wikipedia (EN), "Brickaville": aan RN 2, 105 km ten zuiden van Toamasina, aan de Rianila. https://en.wikipedia.org/wiki/Brickaville
[9] Wikipedia (EN), "Vatomandry": ligt aan het Pangalanes-kanaal en aan RN 11a. https://en.wikipedia.org/wiki/Vatomandry
[10] Wikipedia (EN), "Mahatsara": RN 2 kruist de commune bij Antsampanana. https://en.wikipedia.org/wiki/Mahatsara
[11] `v2/design/routebrieven/kobalt-ambatovy-toamasina.md` en `v2/data/stroomroute-kobalt-ambatovy-toamasina.json` (marker `co-toamasina-kade`, -18.1556, 49.4278).
[12] L'Express de Madagascar, "Production: le marché du graphite gagne du terrain" (2026-01): Gallois als historische producent die "plus modestement" doorgaat. https://www.lexpress.mg/2026/01/production-le-marche-du-graphite-gagne.html
[13] Esri World Imagery via `v2/tools/sat_check.py` (z15, live): twee beelden, zie §3. Tool-proef: `v2/build-cache/ais/graaf/grafiet-toets-marovintsy-toamasina-weg.geojson` (178,0 km).

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)

**Bestand:** `v2/data/stroomroute-grafiet-marovintsy-toamasina.json` (versie 2, lonlat, 81,3 KB, 3.968 punten) · **functie:** `bak_grafiet_marovintsy_toamasina` in `v2/tools/bak_stromen.sh` · **profiel:** `grafiet-marovintsy-toamasina-marovintsy-toamasina` in `v2/tools/maak_stroombeen_weg.py` · **titel:** Grafiet · Marovintsy-mijn (Gallois, Vatomandry) → Toamasina-haven (vlokgrafiet, Madagaskar).

| # | modaliteit | been | km | gepubliceerd | afwijking | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | Marovintsy → Toamasina (RN 11a → RN 2; aannemelijk: één bron) | 173,6 | geen wegkm; OSRM 176 | -1,4% (indicatie) | nee |

Totaal 173,6 km, 1 been, 2 markers (`gr-marovintsy-mijn`, `gr-toamasina-kade`, beide op 0,0 km van de lijn). Naden: geen (één been).

**Recept:** wegscan (`wegscan_puur.py`, extract `madagaskar`, 52 s) met vijf via-punten uit §4 (mijn, Antsampanana/Mahatsara, Brickaville-rand, Tsaratampona, kade), refs `RN 11a` en `RN 2`, `corridorKlassen` tertiary en unclassified, `vensterKm` 40. Segmenten: mijn → Mahatsara 45,3 km, → Brickaville 24,2, → Tsaratampona 50,0, → kade 53,9. Snaps 0,22 km (mijn), 0,06 km (kade), overige 0,00-0,01. Eén keerlus gesnoeid (0,05 km, verwaarloosbaar). Gebakken zonder `--stippel`, zeebeen, haven-aanloop, leiding of luchtbeen; kade-marker letterlijk hergebruikt van `kobalt-ambatovy-toamasina`.

**Toetsen:** `toets_knikken.py`: 24 knikken >= 60 graden (spikes van 2-85 m op de lokale mijnweg en de havenrand), 0 omkeringen, 0 terugloop. `toets_rechte_benen.py --min-km 5`: dit been staat er niet in (omwegfactor niet 1,000). json.load: versie 2, punt_formaat lonlat, modaliteit truck, 3.968 punten.

**Toelichting:** de eerste 45 km (mijn → Mahatsara) buigen eerst 5 km westwaarts via het gehucht Antsapanana Gallois (lon 48,90) en dan noordoost naar de RN 11a; hemelsbreed 31 km, omwegfactor 1,46: een bochtige lokale weg, geen via-punt-omweg. Het mijnanker snapt op 0,22 km, geen last-mile-stippel nodig.

**Lessen:** (1) `hecht_marnet.py route` vraagt altijd `--graaf`, ook zonder spoor-/binnenvaartbeen (staat niet in de handleiding voor wegfuncties). (2) De ±15%-toets is hier een indicatie; alleen RN 2 Brickaville-Toamasina (105 km) is bron-km. (3) Open punten van §7 blijven staan (exporthaven niet gebronde, volume, tegenstrijdige afstand en afnemers, mijnanker zonder bron-coördinaat).
