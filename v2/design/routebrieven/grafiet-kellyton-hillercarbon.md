# Routebrief (licht) · Grafiet · Kellyton (Alabama) → I-10 → Hiller Carbon Dayton (Texas, VS)

**stroom-id:** `grafiet-kellyton-hillercarbon` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** SG-fines (graphietbijproduct van de Westwater-plant bij Kellyton) gaan per **truck** over AL-9, US-231, I-65 (Montgomery, Mobile), I-10 (Slidell, I-12 om Baton Rouge heen, Lafayette, Lake Charles, Beaumont) en US-90/TX-146 naar de Hiller Carbon-locatie in Dayton (Liberty County, Texas) — **bestemming aannemelijk: één bron voor de plaats**, geen bron koppelt de fines aan Dayton. Eén landbeen, geen zee.
**Welke as van het verhaal:** *Amerikaans grafietbijproduct naar staal en gieterij, een niet-batterij-afnemer.* **Jaarvolume: 0 kt grafiet/j in 2024** (plant niet in productie); Phase I ontwerp 14 kt SG-fines/j [1]. Eenheid kt grafiet/j, peiljaar 2024.

## 1 · Ketenkaart
```
Kellyton-plant `gr-kellyton-plant` ──(b1 truck · AL-9/AL-115 → US-231 → I-65 → I-10 → I-12 → I-10 → US-90 → TX-146 · tool-schatting ~1.045–1.060 km, OSRM 1.047, hemelsbreed 904 km, geen wegkm)──► Hiller Carbon Dayton `gr-hiller-dayton` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck (werkaanname) | `gr-kellyton-plant` → `gr-hiller-dayton` | AL-115/AL-9 → US-231 → I-65 (Montgomery, Evergreen, Mobile) → I-10 (Slidell) → I-12 → I-10 (Lafayette, Lake Charles) → US-90 → TX-146 | hemelsbreed 904 km, geen wegkm; OSRM 1.047,0 [7]; eerste 531,0 km Kellyton–Slidell gemeten in de gebakken b3 van `grafiet-balama-kellyton` [10] | maak_stroombeen_weg (profiel `grafiet-kellyton-hillercarbon-kellyton-dayton`, extracts us-alabama, us-mississippi, us-louisiana, us-texas) | nee — *aannemelijk: één bron voor de bestemming (Dayton), vervoerswijze niet gebrond (Hiller meldt truck, rail, barge)* |

Geen zee, geen haven-aanloop. De eerste ~531 km (Kellyton → Slidell) vallen samen met b3 van `grafiet-balama-kellyton` in omgekeerde richting: **dezelfde via-punten** (§4, nrs 1–8) zodat de lijnen vallen, maar geen letterlijke kopie (andere richting, ander eindstuk). Slotstuk: Dayton-anker ligt ~0,2 km west van TX-146 (< 2 km): geen last-mile-been, `trimStaart` knipt op de ankerprojectie.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-kellyton-plant` | fabriek / laadplek | Westwater Kellyton Graphite Plant, Lake Martin Regional Industrial Park | 32.9625, -86.0390 | hergebruik letterlijk `grafiet-balama-kellyton.md` (z15/z16: nieuw hallencomplex met bluspoel, toegang van US-280) | aannemelijk — hergebruik; coördinaat niet in een bron |
| `gr-hiller-dayton` | afnemer (eindpunt) | Hiller Carbon, Dayton TX (TX-146) | 29.9850, -94.9091 | stad Dayton [5]; adres/Waze en vacature Dayton via haalbaarheidstoets (door mij niet herverifieerd) [12]; coördinaat van satelliet [9], niet in een bron of in OSM | **aannemelijk** (z15 `sat-grafiet-kellyton-hillercarbon-dayton.png` gezien: klein terrein met loodsen en open opslagveld ~0,2 km west van TX-146, naast een groot rangeerterrein ten noorden; geen bedrijfsnaam zichtbaar; OSM heeft geen Hiller-object [8]) |

## 4 · Via-punten (b1, in reisvolgorde Kellyton → Dayton; lat, lon; eerste en laatste = ankers)
Nrs 1–8 zijn de b3-punten uit `grafiet-balama-kellyton.md` in omgekeerde volgorde (punt 8→1, binnen 0,01 km op de weg gesnapt); geen punt in een stadscentrum, niet in Baton Rouge of Houston. Het aantal (12) is hoger dan 3–8 om de b3-lijn te laten vallen (bindende aanpassing haalbaarheidstoets).
| # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|
| 1 | AL-9 / AL-115-splitsing | 32.9344, -86.0613 | AL-115 naar Kellyton i.p.v. AL-9 naar Alexander City |
| 2 | AL-9 bij Jacksons Gap | 32.7547, -86.1004 | AL-9 zuid; zonder dit punt een omweg van 50 km via Sylacauga |
| 3 | US-231 bij Wetumpka | 32.5458, -86.1907 | US-231/AL-9 naar Montgomery |
| 4 | I-65 Montgomery | 32.2536, -86.3649 | I-65 buiten het stadscentrum |
| 5 | I-65 bij Evergreen | 31.4665, -86.9578 | I-65 doorrijden naar Mobile |
| 6 | I-65 noord van Mobile | 30.9071, -87.9845 | I-65/I-10 i.p.v. US-43/US-45 |
| 7 | I-10 Mississippi kust | 30.4455, -88.7294 | I-10 langs de kust i.p.v. de I-59/I-55-route via Hattiesburg |
| 8 | I-10 Louisiana oost (Slidell) | 30.2375, -89.7679 | I-10 oost bij Slidell; vanaf hier I-12 om Baton Rouge heen (OSRM kiest I-12, 137 km) |
| 9 | I-10 oost van Lafayette | 30.2815, -91.9492 | I-10 over het Atchafalaya-bekken, niet door Lafayette |
| 10 | I-10 west van Lake Charles | 30.2287, -93.3005 | I-10 langs Lake Charles i.p.v. US-90 door de stad |
| 11 | US-90 west van Beaumont | 30.0607, -94.2405 | route verlaat I-10 bij Beaumont voor US-90 naar Liberty (snap 2 m) |
| 12 | US-90 / TX-146 Dayton-noord | 30.0420, -94.8934 | TX-146 zuid naar het anker (snap 0 m) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kellyton Graphite Plant (Phase I, nog niet in productie) | Westwater Resources / Alabama Graphite Products | vlokconcentraat → CSPG + SG-fines | 14 kt SG-fines/j van 26,5 kt/j product | [1] |
| Hiller Carbon, Dayton TX (aannemelijk) | Hiller Carbon | breken, zeven, drogen, pelletiseren, verpakken van koolstof en grafiet voor staal, gieterij, vuurvast | onbekend | [4][5] |

## 6 · Stoppunt
De brief stopt bij de Dayton-vestiging: de offtake noemt alleen "plants within the US" en geen bron legt de fines aan een plaats [1]; fase D/E vervallen (afnemers van Hiller zijn niet genoemd).

## 7 · Open punten
- **Bestemming niet bron-gelegd:** de offtake (17 sep 2024) zegt alleen "plants located within the US"; Dayton is de enige gevonden Hiller-verwerker [5]. Hiller heeft volgens zijn historiepagina meerdere locaties en een nieuwe faciliteit in ontwikkeling [5][12]: de fines kunnen elders heen. Hiller-site toont geen vestigingen [4].
- **Dayton-coördinaat niet bronbaar:** geen bron noemt een coördinaat (Waze 6736 TX-146 via de toets [12]); anker gelegd op het terreintje bij het adres, aannemelijk. Geen Hiller-object in OSM; Nominatim geeft alleen TX-146 op 0,2 km [8].
- **Geen gepubliceerde wegkm:** de ±15%-toets is een indicatie tegen OSRM 1.047,0 km [7]. Truck is werkaanname (Dayton ligt naast een rangeerterrein; Hiller meldt truck, rail, barge).
- **Volume nul:** Kellyton produceert niet (productiestart 2026 voorwaardelijk volgens 10-K FY2024, kosten 128 van 245 mln eind 2025, streefjaar 2027) [1][2]. Eenheid kt/j; geen leverbare hoeveelheid.
- Kellyton-anker en toegangsweg: zie `grafiet-balama-kellyton.md` §7 (coördinaat niet bronbaar, plantweg niet in OSM).

## 8 · Bronnen
[1] Westwater Resources, Form 10-K FY2024 (SEC): Hiller-offtake 17 sep 2024, ~14 kt/j SG-fines Phase I, "plants located within the U.S." zonder plaats; Phase I 26,5 kt/j. https://www.sec.gov/Archives/edgar/data/839470/000155837025003382/wwr-20241231x10k.htm
[2] Westwater 10-K FY2025 en NS Energy (offtake Hiller, kosten 128 van 245 mln): via `grafiet-balama-kellyton.md` [1][2], niet opnieuw geopend. https://www.sec.gov/Archives/edgar/data/839470/000110465926032111/wwr-20251231x10k.htm
[3] Westwater/Business Wire 2022-04-19: Kellyton, Lake Martin Regional Industrial Park, 349 McClellan Industrial Drive (via de balama-brief [4]). https://www.businesswire.com/news/home/20220419006039/en/Westwater-Resources-and-Alabama-Graphite-Products-Break-Ground-on-Kellyton-Processing-Plant/
[4] Hiller Carbon, bedrijfssite (2026-10-30): diensten crushing, screening, drying, pelletizing, packaging; geen vestigingen genoemd. https://www.hillercarbon.com/
[5] Kaishan USA, case study Hiller Carbon (ongedateerd): plant in Dayton, TX, verwerkt koolstof en grafiet voor staal, gieterij, vuurvast; nieuwe faciliteit in ontwikkeling; geen adres. https://kaishanusa.com/case-studies/hiller-carbon/
[6] Wikipedia, Martin H. Hiller: CEO Hiller Carbon, levert koolstof en mineralen aan staal en gieterij. https://en.wikipedia.org/wiki/Martin_H._Hiller
[7] OSRM-demoserver (OSM), 2026-10-30: Kellyton → anker Dayton 1.047,0 km via AL-9, I-65, I-10, I-12, I-10, US-90, TX-146; Slidell → Dayton 530,9 km. https://router.project-osrm.org/
[8] Nominatim reverse 29.9850, -94.9091: TX 146, Dayton, Liberty County (0,2 km); geen Hiller-object. https://nominatim.openstreetmap.org/
[9] Esri World Imagery via `v2/tools/sat_check.py` (2026-10-30): `v2/build-cache/satcheck/sat-grafiet-kellyton-hillercarbon-dayton.png` (z15), `-dayton-z14.png`; plus `sat-toets-grafiet-kellyton-hillercarbon-a.png`.
[10] Atlas: `grafiet-balama-kellyton.md` (via-punten, anker Kellyton, b3) en `v2/build-cache/ais/graaf/grafiet-balama-kellyton-weg-nola-kellyton.geojson` (Kellyton → Slidell-punt 531,0 km langs de lijn).
[11] Geofabrik us-alabama, us-mississippi, us-louisiana, us-texas (ODbL).
[12] Haalbaarheidstoets golf 15 (orkestrator-invoer): Waze-plaats 6736 TX-146, vacature Dayton 77535, historiepagina Hiller met meerdere locaties; door mij niet herverifieerd.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)
**Bestand:** `v2/data/stroomroute-grafiet-kellyton-hillercarbon.json` (156,2 KB, versie 2, punt_formaat lonlat) · **recept:** functie `bak_grafiet_kellyton_hillercarbon` in `v2/tools/bak_stromen.sh`, profiel `grafiet-kellyton-hillercarbon-kellyton-dayton` in `v2/tools/maak_stroombeen_weg.py` (scan via `wegscan_puur.py`, extracts us-alabama, us-mississippi, us-louisiana, us-texas), tussenuitvoer `v2/build-cache/ais/graaf/grafiet-kellyton-hillercarbon-weg-kellyton-dayton.geojson` en `…-wegscan.log`.

| # | modaliteit | km (gebakken) | brief | stippel | naam |
|---|---|---|---|---|---|
| b1 | truck | **1.055,4** (7.656 punten) | OSRM 1.047,0 (indicatie, geen wegkm): +0,8% | nee | vrachtwagen Kellyton → Hiller Carbon Dayton TX (… aannemelijk: één bron voor de bestemming, truck werkaanname) |

Totaal 1.055,4 km, 2 markers (`gr-kellyton-plant` 32.9625,-86.0390 en `gr-hiller-dayton` 29.9850,-94.9091), beide 0,0 km van de lijn. Eén been: geen naden. Geen zee, haven-aanloop, stippel, kopie, lucht of leiding.

**Toets.** Km binnen de verwachte 1.045–1.060 km (indicatie, geen ±15%-norm want geen gepubliceerde wegkm). Kellyton → Slidell-punt 530,7 km (brief: ca. 531 gemeten in b3 balama-kellyton): de b3-lijn valt. Alle 13 via-segmenten snappen ≤ 0,32 km; slotstuk plant → weg 0,32 km en weg → anker 0,04 km (last mile 0,28 km service); `trimStaart` knipte 2 punten. `toets_knikken.py`: 22 knikken ≥ 60 graden (kleine spikes van 4–27 m bij knooppunten, o.a. Slidell en Beaumont), 0 omkeringen, 0 terugloop. `toets_rechte_benen.py`: het been staat er niet in (omwegfactor > 1). `json.load` ok, bestand < 300 KB.

**Lessen / noten.** (1) Slidell-via-punt blijft de grens met b3 van balama-kellyton; de 12 via-punten (meer dan 3–8) houden de lijnen identiek tot Slidell. (2) Geen via-punt in Baton Rouge of Houston: de router kiest zelf I-12 om Baton Rouge. (3) Bestemming en truck blijven aannemelijk (§7), alleen in de beennaam en de markernaam, niet in de lijnstijl. (4) Volume nul (Kellyton produceert niet).

