# Routebrief (licht) · gas — Yarraloola → Goldfields Gas Pipeline → Kalgoorlie (Australië)

**stroom-id:** `gas-yarraloola-kalgoorlie` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** Carnarvon-bekkengas gaat bij Yarraloola (Pilbara, WA) de **Goldfields Gas Pipeline** in (APA, DN350-400, ondergronds) en loopt in één doorgetrokken leiding van ca. 1.410 km door Newman-, Leinster- en Menzies-streek naar het eindstation bij Kalgoorlie, naast de Kalgoorlie Nickel Smelter in Feysville. Een een-been-pijp; de tekening stopt op het eindstation.
**Welke as van het verhaal:** *Gas als mijn-energie* — het gas dat het droge binnenland van de Pilbara en de Goldfields draait: ijzererts, goud en nikkel [3]. Volume: **ca. 0,9 bcm/j** (indicatie: ERA-prognose gemiddelde doorzet vanaf het Yarraloola-ontvangstpunt, 94,2 TJ/d, 2025-29; 1 PJ ≈ 26,3 Mm³ is eigen omrekening) [3]. Contracted 110,4 TJ/d ≈ 1,06 bcm/j; AEMC-capaciteit 202 TJ/d ≈ 1,9 bcm/j [6].

## 1 · Ketenkaart
```
DBNGP-aftakking bij Yarraloola (Pilbara) `gas-yarraloola-station`
  ──(b1 leiding · Goldfields Gas Pipeline, 8 OSM-ways, DOORGETROKKEN · 1.411,8 km OSM / 1.378 APGA, APA, Wikipedia / 1.380 WA-overheid 1996)──►
Kalgoorlie-eindstation, naast de Kalgoorlie Nickel Smelter (Feysville) `gas-kalgoorlie-eind` — stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | leiding | `gas-yarraloola-station` → `gas-kalgoorlie-eind` | Goldfields Gas Pipeline (APA): Pilbara, Newman-streek, Leinster-streek, Menzies, Kalgoorlie. OSM-ways 579631963, 106538223, 1421965205, 376247352, 186178339 (omgekeerd), 218817589, 426111593, 426111599 (man_made=pipeline, substance=gas, DN350-400, operator APA) | gemeten OSM **1.411,8**; gepubliceerd 1.378 [1][2][10], 1.380 [4]: +2,4% / +2,3% | vooraf gestikt geojson (FeatureCollection, 845 punten; grootste segment 19,0 km; grootste naad 51 m bij way 426111593 → 426111599) | nee |

Eerste way (579631963, 31,8 km) loopt van een kustpunt (-21.1946,115.8473) naar de DBNGP-aftakking (-21.4450,115.9557): OSM noemt hem Goldfields Gas Pipeline maar hij is het eind van een toevoerlijn (zie §7). Zonder dit stuk is het GGP-trace 1.380,0 km (0,0% tegen [4]); de ±15%-toets slaagt met en zonder. **Niet getekend:** Newman-lateral (47 km [2]), laterals naar Wiluna, Mt Keith, Leinster, Parkeston en Kalgoorlie Power Station [2], de Kalgoorlie-Kambalda-leiding (OSM-way 579631964, ca. 40 km), spoor way 426119366.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-yarraloola-station` | ontvangstpunt, begin GGP | Yarraloola, aftakking van de DBNGP-kust-trunkline (660 mm) naar de GGP | -21.4450, 115.9557 | [2][3][8][9] | aannemelijk (z15 gezien: faciliteitsterrein met enkele installaties en kale leidingstroken ca. 500 m zuidwestelijk van het punt, drie leidingstroken komen samen; de naam Yarraloola komt uit APGA/ERA, geen bron geeft een coördinaat; het punt is de OSM-junctie van GGP en DBNGP-way, 0 m van de lijn) |
| `gas-kalgoorlie-eind` | eindstation / stoppunt | Kalgoorlie-eindstation GGP, aan de NW-rand van de Kalgoorlie Nickel Smelter, Feysville | -30.8657, 121.4805 | [4][7][8][9][13] | bron-gelegd (z15 gezien: de leidingstrook en toegangsweg "Gas Pipeline Access" lopen noord-zuid; ca. 0,6-1 km zuidwaarts het smelterterrein met schoorstenen, bezinkvijvers en gebouwen, oostelijk een dagbouwput; OSM-landuse "Kalgoorlie Nickel Smelter" op -30.8709,121.4870 [8]; Wikipedia -30.8736,121.4841 [7]) |

Hergebruik: geen. `au-kalgoorlie-mill` (-30.7897,121.4990, goud-kalgoorlie-singapore) ligt 8,7 km van het eind en wordt NIET getekend: geen bron noemt KCGM als GGP-afnemer (zie §7). Beide ankers staan niet in `gas-sitelaag.json`.
⚠️ Sitelaag-melding (niet aangeraakt): `w-bhp-nickelwest-kalgoorlie` in `nikkel-sitelaag.json` staat op -30.7489,121.4708 (status onzeker, midden Kalgoorlie-Boulder); de smelter ligt volgens OSM en Wikipedia in Feysville, ca. 13 km zuidelijker (-30.871,121.485).

## 4 · Via-punten
Niet van toepassing: leiding = vooraf gestikte OSM-ways, geen corridorkeuze.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Yarraloola-ontvangstpunt (covered GGP) | APA (Goldfields Gas Transmission) | Carnarvon-bekkengas via DBNGP → GGP | 110,4 TJ/d gecontracteerd, 94,2 TJ/d gemiddelde doorzet (ERA-prognose 2025-29); 202 TJ/d AEMC-register | [3][6] |
| Kalgoorlie Nickel Smelter (BHP Nickel West) | BHP | gas → elektriciteit voor de smelter (1996: gasgestookte centrale) | niet gevonden; BHP schortte de Nickel West-activiteiten op sinds oktober 2024, herziening uiterlijk februari 2027 | [4][3] |

## 6 · Stoppunt
De tekening stopt op het eindstation bij Kalgoorlie: het gas verdeelt zich daarachter over de Kalgoorlie-Kambalda-leiding en het distributienet van Kalgoorlie (Parkeston-lateral [3]), en geen bron koppelt de stroom aan één afnemer met naam. Geen fase D/E. Verhaal: één pijp van 1.380 km brengt het kustgas het droge binnenland in.

## 7 · Open punten
- **Kop (-21.1946,115.8473) is niet Yarraloola.** Dat punt ligt op een getijdenplaat bij de kust, aan het eind van een zandweg (z15 gezien); de OSM-ways 579631954 (69,9 km, zonder naam, vanaf -20.6503,115.5795) en 579631963 vormen er een toevoerlijn, vermoedelijk van een offshore-aanlanding. Naam, eigenaar en bron van die toevoer zijn niet gevonden. Hij wordt getekend omdat de haalbaarheidstoets de achtweg-keten bindend voorschrijft (1.411,8 km), maar niet gemarkeerd.
- **Geen bron noemt KCGM / Super Pit als GGP-afnemer.** Genoemd zijn sectoren (ijzererts, goud, nikkel [3]) en in 1996 zes gasgestookte centrales (Newman, Mt Keith, Leinster, Parkeston, Kalgoorlie Nickel Smelter, Kambalda) [4]. Daarom geen last-mile-stippel naar de Fimiston-mill (8,7 km).
- **Jaarvolume is een prognose**, niet gemeten: het ontwerp noemde 123,3 TJ/d maar dat is Yarraloola 110,4 + NGI 12,9; de NGI (580 km, DBNGP bij Ambania → GGP ten zuiden van Leinster [3]) komt NIET via Yarraloola. Een jaarverslag of AEMO-bulletin met werkelijke doorzet is niet gelezen.
- **Eigenaarschap:** APA-pagina noemt 100% [10]; de 88,2% uit het ontwerp is niet teruggevonden.
- **Gas dat nu door de leiding gaat** (welke velden, welke afnemers) is niet gevonden; ERA noemt alleen sectoren.
- Capaciteitspagina's van AEMC/APA/ERA-final decision deels alleen via zoekresultaat of PDF-uittreksel gelezen.

## 8 · Bronnen
[1] Wikipedia, "Goldfields Gas Pipeline" — 1.378 km, Carnarvon-bekken → Kalgoorlie, 1996, APA, Newman-lateral 47 km. https://en.wikipedia.org/wiki/Goldfields_Gas_Pipeline
[2] APGA, "Goldfields Gas Pipeline" — hoofdleiding 1.378 km Yarraloola → Kalgoorlie, Newman-lateral 47 km, laterals Wiluna, Mt Keith, Leinster, Kalgoorlie Power Station, koppeling EGP bij Leonora en KKP. https://apga.org.au/goldfields-gas-pipeline
[3] ERA WA, GGP AA5 Attachment 3.1 Demand Forecast Report (revised proposal), 2024 — Yarraloola 110,4 TJ/d contracted, 94,2 TJ/d doorzet, NGI 12,9-14,3 TJ/d, sectoren ijzererts/goud/nikkel, Parkeston-lateral, BHP-opschorting. https://www.erawa.com.au/sites/default/files/24287/GGP-AA5-Attachment-3-1-Demand-forecast-report-Public.pdf
[4] Overheid van West-Australië, "Goldfields pipeline will underpin growth of State's resources sector", 4 okt 1996 — 1.380 km, zes gasgestookte centrales (370 MW) incl. Kalgoorlie Nickel Smelter. https://www.wa.gov.au/government/media-statements/Court%20Coalition%20Government/Goldfields-pipeline-will-underpin-growth-of-State%27s-resources-sector-19961004
[5] Overheid van West-Australië, "Official opening of Goldfields Gas Pipeline", 16 jul 1996 — Yaraloola bij Karratha → Kalgoorlie, volledige leiding 1.400 km. https://www.wa.gov.au/government/media-statements/Court%20Coalition%20Government/Official-opening-of-Goldfields-Gas-Pipeline-19960716
[6] AEMC, Gas pipeline register "WA: Goldfields Gas Pipeline (GGP)" — 1.378 km, 202 TJ/d (inhoud uit zoekresultaat). https://aemc.gov.au/energy-system/gas/gas-pipeline-register/wa-goldfields-gas-pipeline
[7] Wikipedia, "Kalgoorlie Nickel Smelter" — Feysville, BHP/Nickel West, -30.8736,121.4841. https://en.wikipedia.org/wiki/Kalgoorlie_Nickel_Smelter
[8] OpenStreetMap (ODbL), ways 579631963, 106538223, 1421965205, 376247352, 186178339, 218817589, 426111593, 426111599 (GGP) en landuse-way 675267037 "Kalgoorlie Nickel Smelter", gelezen uit de Geofabrik australie-pbf en Overpass. https://www.openstreetmap.org/way/426111599
[9] Esri World Imagery via `v2/tools/sat_check.py` (z15, live, 2026-10-31): `v2/build-cache/satcheck/sat-gas-yarraloola-kalgoorlie-kop.png`, `-dbngp.png`, `-station.png` (eind; ook `-kop-z14.png`, `-station-z14.png`, niet bekeken).
[10] APA Group, "Goldfields Gas Pipeline (GGP)" — 1.378 km, 100% APA, 1996. https://www.apa.com.au/operations-and-projects/gas/gas-transmission/goldfields-gas-pipeline-ggp
[11] Ketenontwerp + haalbaarheidstoets M31 golf 19 (orkestrator-invoer): wayvolgorde, +2,4%, eindmarker, bronnen_start.
[12] `v2/design/nikkel-sitelaag.json` (w-bhp-nickelwest-kalgoorlie) en `v2/design/routebrieven/goud-kalgoorlie-singapore.md` (anker `au-kalgoorlie-mill`).
[13] Nominatim (OSM) reverse op -30.8657,121.4805: "Gas Pipeline Access, Feysville, Kalgoorlie" (highway=track). https://nominatim.openstreetmap.org/

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Bestand:** `v2/data/stroomroute-gas-yarraloola-kalgoorlie.json` (versie 2, lonlat, 18,8 KB) · functie `bak_gas_yarraloola_kalgoorlie` in `v2/tools/bak_stromen.sh` · tool `v2/tools/maak_leidingbeen_gas_yarraloola_kalgoorlie.py`.

| # | modaliteit | been | km gemeten | km brief | afwijking | stippel |
|---|---|---|---|---|---|---|
| b1 | leiding | Goldfields Gas Pipeline DN350-400 (OSM-ways, APA, ondergronds) Yarraloola naar Kalgoorlie | 1.411,8 (845 punten) | 1.378 (APGA, APA, Wikipedia, AEMC) / 1.380 (WA-overheid) | +2,4% / +2,3% | nee |

Totaal 1.411,8 km, 845 punten, 1 been, 2 markers (Yarraloola -21.4450,115.9557 op 0 m van de lijn, 31,8 km na de lijnkop; Kalgoorlie-eind -30.8657,121.4805 op 10 m). Naad n.v.t. (een been); grootste segment 19,0 km; grootste naad in de stikketen 51 m (way 426111593 naar 426111599).

**Recept:** `--been-geojson leiding` met het vooraf gestikte `v2/build-cache/ais/graaf/gas-yarraloola-kalgoorlie-leiding-ggp.geojson` (FeatureCollection; herhaalbaar met `python v2/tools/maak_leidingbeen_gas_yarraloola_kalgoorlie.py`, 14 s, uit de lokale australie-pbf). Ways 579631963, 106538223, 1421965205, 376247352, 186178339 (omgekeerd door het script), 218817589, 426111593, 426111599. Geen extract, via-punten, profiel, MARNET-zeebeen, haven-aanloop, stippel, vlucht of gedeeld been; hecht_marnet.py nam de lijn letterlijk over.

**Toets:** km binnen 15% van de gepubliceerde 1.378-1.380; beide markers op de lijn; toets_rechte_benen geen melding; toets_knikken 9 knikken >= 60 graden (spikes en krappe bochten van 73-478 m radius, o.a. rond de DBNGP-junctie -21.44,115.95), 0 omkeringen, 0 terugloop: kartering van het OSM-tracé zelf, niet aangepast. json.load: versie 2, lonlat, modaliteit leiding, 845 punten.

**Leiding-toelichting:** doorgetrokken omdat OSM de leiding volledig kent (man_made=pipeline, name Goldfields Gas Pipeline, substance gas, diameter 350-400, operator APA). De lijnkop (-21.1946,115.8473) is het eind van een toevoerlijn op een getijdenplaat, geen Yarraloola: getekend (bindende toets 1.411,8 km), niet gemarkeerd; zonder way 579631963 is het trace 1.380,0 km. Niet getekend: Newman-lateral, laterals Wiluna/Mt Keith/Leinster/Parkeston, Kalgoorlie-Kambalda-leiding (way 579631964). Geen last-mile naar de Fimiston-mill: geen bron noemt KCGM als afnemer.

**Lessen:** een vooraf gestikte OSM-leiding is een enkele regel `--been-geojson` (patroon bak_gas_moomba_wilton); de ways-volgorde met een omgekeerde way regelt het script op afstand tot het vorige eind. Centraal nodig: register, bundel; sitelaag-fout `w-bhp-nickelwest-kalgoorlie` (13 km te noordelijk) gemeld, niet aangeraakt.
