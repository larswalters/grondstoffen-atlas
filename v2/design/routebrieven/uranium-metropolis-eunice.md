# Routebrief (licht) · Uranium — Metropolis Works (Illinois) → Urenco USA Eunice (New Mexico)

**stroom-id:** `uranium-metropolis-eunice` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 15) · **status:** gebakken
**Keten in één zin:** UF6 uit de Honeywell/ConverDyn-conversiefabriek Metropolis Works (Illinois) gaat per **truck** (aannemelijk: modaliteit en corridor niet gepubliceerd) over IL-37/I-57, I-55, I-40, I-30 en I-20 en TX-176 naar de Urenco USA-verrijkingsfabriek bij Eunice (New Mexico) — stoppunt.
**Welke as van het verhaal:** *VS binnenlands: conversie → verrijking* — de enige VS-UF6-fabriek voedt de enige commerciële VS-verrijker. Volume: Urenco USA ~5.850 t U feed-equivalent/j (SCHATTING, ~9% wereld-SWU x ~65.000 t U, WNA 2023/24, sitelaag); aandeel Metropolis niet gepubliceerd. Route-bewijs: één contract, Transnuclear voor Urenco USA, 2010 [1], zonder tonnage of modaliteit.

## 1 · Ketenkaart
```
Metropolis Works `u-metropolis-conversie` ──(b1 B truck · US-45 → IL-169 → IL-37 → I-57 → I-55 → I-40 (West Memphis → Little Rock)
 → I-30 (Texarkana, Dallas) → I-20 → TX-176 → NM-176 · hemelsbreed 1.408 km, geen wegkm; OSRM-indicatie 1.653 km, aannemelijk)──►
Urenco USA Eunice `u-eunice-verrijking` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | truck | Metropolis Works → Urenco USA Eunice (aannemelijk: één bron) | US-45, IL-169, IL-37, I-57, I-55, I-40, I-30, I-20, TX-176, NM-176 | hemelsbreed 1.408 km, geen wegkm [4: OSRM 1.653 km als indicatie, x1,17]; de ±15%-toets is indicatie, geen norm | maak_stroombeen_weg (us-illinois, us-missouri, us-arkansas, us-texas, us-new-mexico) | nee |

Gedeelde geometrie: geen letterlijke kopie mogelijk (zie §7: ~35% overlap met `uranium-eunice-columbia`, andere routering). Geen zee, spoor, leiding of lucht.

## 3 · Ankers (één per site; beide HERGEBRUIKT)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-metropolis-conversie` | UF6-fabriek (kop) | Honeywell/ConverDyn Metropolis Works, Illinois | 37.1718, -88.7570 | letterlijk uit `uranium-smithranch-metropolis` §3 (= sitelaag `w-metropolis`) [2][5][6] | bron-gelegd (z15 opnieuw gezien 2026-10-30: ommuurd fabrieksterrein met hallen, tanks en verharde erven in de bossen langs de Ohio, kruis op het complex; een spoor- en wegtracé loopt langs de oostrand) |
| `u-eunice-verrijking` | verrijking (staart, stoppunt) | Urenco USA / National Enrichment Facility, 8 km oost van Eunice | 32.4356, -103.0796 | letterlijk uit `uranium-eunice-columbia` §3 (= sitelaag `w-urenco-eunice`, Wikipedia-infobox) [3][5][7] | bron-gelegd (z15 opnieuw gezien: cascadecomplex met lange hallen, bufferbekkens en omheining, kruis op de hoofdhal; de doorgaande weg NM-176 loopt ten zuiden langs (0,66 km van het anker volgens `uranium-eunice-columbia` §9), het WCS-terrein ligt ernaast) |

## 4 · Via-punten (b1; (lat, lon) hier, in het profiel (lon, lat); allemaal OSRM-manoeuvrepunten op de doorgaande weg, niet in een stad)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | I-57/US-51 (merge vanaf IL-37) | 37.1252, -89.1813 | het eerste stuk gaat noordwest via US-45/IL-169/IL-37 naar I-57 en niet via I-24 Paducah en Kentucky; pint I-57 zuidwaarts naar de Mississippi |
| b1 | 2 | I-57/I-55-knoop, Missouri-bootheel | 36.8742, -89.5332 | pint de overgang van I-57 naar I-55 zuid; het alternatief is US-60 en I-44 (OSRM 1.705 km, +3%) |
| b1 | 3 | I-55/I-40-knoop, West Memphis (Arkansas) | 35.1696, -90.1975 | pint I-40 west richting Little Rock; de route blijft aan de Arkansas-kant van de rivier, Tennessee wordt niet aangedaan |
| b1 | 4 | I-30/US-67/US-70, Benton (Arkansas) | 34.5501, -92.6247 | pint I-30 zuidwest naar Texarkana, Dallas en Fort Worth, geen I-40-door-Oklahoma-variant |
| b1 | 5 | I-20/I-30-knoop, west-Fort Worth | 32.7253, -97.5819 | I-30 eindigt hier op I-20; pint de westwaartse I-20 (niet via Midland-Odessa-noordroute US-82 en US-62) |
| b1 | 6 | I-20, afslag TX-176 (Big Spring) | 32.2609, -101.5043 | pint TX-176 naar Andrews en NM-176 (95 + 48 km) in plaats van I-20 door Midland en Odessa |

OSRM-segmenten (indicatie): 107,7 / 211,4 / 244,3 / 544,8 / 393,1 / 155,5 km = 1.656,8 km totaal; zonder via-punten kiest OSRM dezelfde corridor (1.653 km).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Metropolis Works | Honeywell / ConverDyn | U3O8 → UF6 | nominaal 15.000 t U/j (~20% wereldcapaciteit) | [2], sitelaag |
| Urenco USA Eunice | Urenco | UF6 → LEU-UF6 | ~5.850 t U feed-equivalent/j, SCHATTING (sitelaag) | [3], sitelaag |

## 6 · Stoppunt
De brief stopt bij Urenco USA Eunice (verrijking, het opgegeven eindpunt): de bron noemt alleen de levering UF6 van Metropolis naar Eunice; de verrijkte LEU-vervolgstroom is `uranium-eunice-columbia` (fase D van een andere keten).

## 7 · Open punten
- **Eén bron, alleen het bestaan:** WNN 11 okt 2010: Transnuclear (Areva) kreeg van Urenco USA het contract UF6 van ConverDyn Metropolis naar Eunice te vervoeren [1]. Geen modaliteit, corridor, tonnage of looptijd. Truck en corridor zijn aanname (de OSRM-snelste weg); aandeel van Metropolis in de feed van Eunice onbekend (Urenco USA kan ook UF6 uit andere conversiefabrieken krijgen; niet onderzocht).
- **Geen wegkm gepubliceerd:** hemelsbreed 1.408 km; OSRM 1.653 km (+17%) is indicatie. De NRC-EIS (NUREG-1790, 2005) heeft een hoofdstuk "Truck Route"; nrc.gov gaf HTTP 403 en WebFetch kon de pdf's niet lezen: niet geverifieerd.
- **Overlap `uranium-eunice-columbia`:** ~35% (Fort Worth tot Eunice, I-20 en TX-176, ~590 km van 1.653 km) is een tweede routering over dezelfde weg, geen kopie. Dat vorige been gaat via Odessa en NM-176; deze brief via Big Spring en TX-176; beide eindigen op NM-176 bij Eunice. Een stuk van ~16 km begin (US-45 noord) zit mogelijk ook in `uranium-metropolis-almelo` (andere corridor daarna).
- **Eunice-snap:** de eigen brief van `uranium-eunice-columbia` §9 vond een geïsoleerd `highway=service`-lusje (way/905682611) bij de poort dat de snap kaapt; NM-176 ligt op 0,66 km. Zie §9 hoe de bak-agent daarmee omgaat.
- **Nog niet gecontroleerd:** de brug bij Cairo en de Arkansas-ritten; `us-tennessee` en `us-kentucky` (in het ketenontwerp genoemd) zijn volgens het OSRM-spoor niet nodig: pas toevoegen bij een "geen wegpad" bij de Mississippi.
- **Actualiteit:** Metropolis lag stil 2017/18 tot 2023 (bronnen verschillen, zie `uranium-metropolis-almelo`); of de stroom nu loopt is niet bekend.

## 8 · Bronnen
[1] World Nuclear News, "Front-end contract for Transnuclear", 11 okt 2010 (Urenco USA; Metropolis → Eunice; geen modaliteit). https://world-nuclear-news.org/articles/front-end-contract-for-transnuclear
[2] Wikipedia (en), "Honeywell Uranium Hexafluoride Processing Facility" — 3 km NW van Metropolis, 15.000 t U/j; coördinaat 37.1718, -88.7570. https://en.wikipedia.org/wiki/Honeywell_Uranium_Hexafluoride_Processing_Facility
[3] Wikipedia (en), "National Enrichment Facility" — 5 mijl oost van Eunice, Urenco USA; coördinaat 32.4356, -103.0796. https://en.wikipedia.org/wiki/National_Enrichment_Facility
[4] OSRM publieke demo-server (project-osrm.org), eigen runs 2026-10-30: Metropolis → Eunice zonder via 1.653,2 km (alternatief via I-44 1.705,0 km); met de zes via-punten 1.656,8 km.
[5] `v2/design/uranium-sitelaag.json` — `w-metropolis` en `w-urenco-eunice` (centraal gelijkgetrokken met de keten-ankers, volumecijfers).
[6] Routebrief `uranium-smithranch-metropolis.md` §3 — Metropolis-anker, satelliet-gelegd.
[7] Routebrief `uranium-eunice-columbia.md` §3/§9 — Eunice-anker, NM-176-snap, `eindKlassen` zonder service.
[8] Esri World Imagery via `v2/tools/sat_check.py` z15 (2026-10-30): `v2/build-cache/satcheck/sat-uranium-metropolis-eunice-metropolis.png` en `-eunice.png`.
[9] Urenco, "UUSA's 500th product shipment" (2022; product-, geen feedcilinders): https://www.urenco.com/news/usa/2022/uusas-500th-product-shipment — alleen als zoekresultaat gezien.
[10] NRC, NUREG-1790 (FEIS National Enrichment Facility, 2005), https://www.nrc.gov/docs/ML0523/ML052360183.pdf — HTTP 403 / niet leesbaar (open punt).
[11] Haalbaarheidstoets `uranium-metropolis-eunice` (bindend invoerdocument): via-punten I-55, I-40, I-30, I-20, TX-176; OSRM 1.653 km.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 15)

**1 been, 1.653,5 km, 9.057 punten, 2 markers, 186,0 KB.** Eén doorgetrokken truckbeen (b1, fase B); geen stippel, haven-aanloop, leiding, luchtbeen of gedeeld been.

| # | modaliteit | km | naad met vorige | opmerking |
|---|---|---|---|---|
| b1 | truck | 1.653,5 | 0,00 (eerste been) | Metropolis Works → IL-37 → I-57 → I-55 → I-40 → I-30 → I-20 → TX-176 → NM-176 → Urenco USA Eunice |

**Recept:** profiel `uranium-metropolis-eunice-metropolis-eunice` in `v2/tools/maak_stroombeen_weg.py` (extracts us-illinois, us-missouri, us-arkansas, us-texas, us-new-mexico, alle vijf aanwezig; us-tennessee/us-kentucky niet nodig) → `python v2/tools/wegscan_puur.py --profiel uranium-metropolis-eunice-metropolis-eunice` (weg- plus reus-slot vanwege Texas; ~190 s Texas-scan) → `v2/build-cache/ais/graaf/uranium-metropolis-eunice-weg-metropolis-eunice.geojson` → `bash v2/tools/bak_stromen.sh uranium-metropolis-eunice` (functie `bak_uranium_metropolis_eunice`, één `--been-geojson`, twee `--marker`).

**Lengtetoets (indicatie, geen norm):** geen wegkm gepubliceerd; gemeten 1.652,4 km weggeometrie (1.653,5 km met de ankerstukjes) tegen OSRM-indicatie 1.653 km (+0,0%) en hemelsbreed 1.408 km (+17,4%). Alle zes via-punten snapten op 0,00 tot 0,33 km (geen via-snap > 5 km, geen via-punt verschoven of verwijderd).

**Toelichting per bevinding:**
- **Weg → kade-aanloop 0,83 km (> 0,5 km)**: het rechte ankerstukje van NM-176 naar de poort van Urenco USA. Geen procesgat; het Eunice-anker ligt 0,66 km van NM-176 (zelfde bevinding als `uranium-eunice-columbia` §9), de trimStaart-projectie maakt het 0,83 km. Plant → weg-aanloop 0,33 km (OK). Geen last-mile-stippel nodig (anker < 2 km van het net).
- **Eunice-snap**: `eindKlassen` zonder `service` (residential, tertiary, unclassified) volstond meteen; het geïsoleerde service-lusje (way 905682611) kaapte de snap niet. `service` is dus niet toegevoegd (de brief liet dat alleen toe als het Eunice niet terugbracht).
- **Knikken**: 5 knikken >= 60 gr, 0 omkeringen, 0 terugloop: vier op- en afritten bij de IL-37/I-57-aansluiting (37,17 tot 37,29 N) en één bij de I-20/TX-176-afslag Big Spring (32,26086, -101,50433, 84,9 gr, R 18 m): oprit-spikes op de doorgaande as, geen repareerbare terugloop.
- **Rechte benen**: `toets_rechte_benen.py --min-km 5` meldt niets voor dit been (omwegfactor 1,17 ten opzichte van hemelsbreed).
- **Markers**: beide op 0,00 km van de lijn (de geometrie begint en eindigt op de ankers).
- **Overlap met `uranium-eunice-columbia`** (Fort Worth tot Eunice, ~35%): bewust een tweede routering (via Big Spring en TX-176 in plaats van Odessa), geen kopie; stoppunt Eunice, fase D vervalt (§6).
- **Bewijs blijft dun**: alleen het bestaan van het Transnuclear-contract (WNN 2010); modaliteit en corridor zijn aanname, vandaar "aannemelijk: één bron" in de beennaam (lijn doorgetrokken). Actuele stroom onbevestigd (Metropolis lag stil 2017/18 tot 2023).

**Lessen voor de volgende bak-agent:** (1) Texas (710 MB) is een reus-extract: weg- plus reus-slot, ~190 s, daarna uit cache. (2) Op deze corridor volstaat `eindKlassen` zonder `service` plus `eindToegangPrivaat`/`trimStaart` voor het Eunice-anker; geen BFS-componenttelling meer nodig. (3) Zes via-punten op de doorgaande knooppunten gaven een lijn die op de meter gelijk is aan de OSRM-indicatie (1.653 km).
