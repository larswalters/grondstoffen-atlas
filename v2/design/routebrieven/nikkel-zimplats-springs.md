# Routebrief (licht) · Nikkel · Zimplats SMC → Springs → Durban → Baltimore (Zimbabwe → Zuid-Afrika → VS)

**stroom-id:** `nikkel-zimplats-springs` (hernoemd uit `nikkel-zimplats-springs`, haalbaarheidstoets) · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** Ni-houdende matte van Zimplats SMC (Great Dyke) per **truck** over A5/A4 naar Beitbridge en over N1/N12 naar Impala Refining Services (IRS) in Springs; daarna nikkelpoeder (HTS 7504) per **truck** over de N3 naar DCT Pier 2 in Durban en per **zeeschip** (MSC, containers) naar Baltimore (Seagirt). Baltimore rust op één bron (US-douanedata): *aannemelijk: één bron*. Geen leiding, spoor, lucht, fase D/E.
**Welke as van het verhaal:** de nikkel-bijproductstroom van de Great Dyke. Volume: orde 4-6 kt Ni in matte per jaar (eigen schatting uit nikkelomzet USD 80,0 mln FY2024 en 69,6 mln FY2025, geen tonnage gevonden, peiljaar FY2024-25 = jul-jun) [1]; het deel dat als Ni-poeder naar Baltimore gaat is ongepubliceerd (één zending 20,9 t op 2025-10-26) [3]. Eenheid kt Ni per jaar.

## 1 · Ketenkaart
```
Zimplats SMC `ni-zimplats-smc` ──(b1 truck · A5 → A4/R1 · hemelsbreed 468 km, geen wegkm · LETTERLIJKE KOPIE pgm-zimplats-springs b1, gebakken 663 km)──►
Beitbridge `ni-beitbridge-grens` ──(b2 truck · N1 → N12 · hemelsbreed 471 km, geen wegkm · LETTERLIJKE KOPIE pgm-zimplats-springs b2, gebakken 583 km)──►
IRS Springs `ni-springs-irs` ──(b3 truck · Wit Road/R29 → N3 · OSRM 559 km, geen wegkm · aannemelijk: modaliteit niet gebronnd)──►
Durban DCT Pier 2 `ni-durban-kade` ──(b4 zee-stippel · haven-aanloop 17,8 km · KOPIE aanloop-durban.geojson)──► zeeknoop Durban
──(b5 zee · MARNET · droogloop 14.387 km · aannemelijk: één bron)──► Seagirt Baltimore `ni-baltimore-seagirt` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-zimplats-smc` → `ni-beitbridge-grens` | A5 Chegutu-Harare → A4/R1 Harare-Masvingo-Beitbridge | hemelsbreed 468, geen wegkm; gebakken 663,2 [11] | LETTERLIJKE KOPIE `pgm-zimplats-springs-weg-smc-beitbridge-gedeeld.geojson` | nee |
| b2 | A | truck | `ni-beitbridge-grens` → `ni-springs-irs` | N1 Musina-Polokwane-Pretoria-Johannesburg → N12 Germiston-Springs | hemelsbreed 471, geen wegkm; gebakken 583,4 [11] | LETTERLIJKE KOPIE `pgm-zimplats-springs-weg-beitbridge-springs.geojson` | nee |
| b3 | B | truck | `ni-springs-irs` → `ni-durban-kade` | Wit Road (R29) → N3 Heidelberg-Villiers-Harrismith-Mooi River-Pinetown → Bayhead | hemelsbreed 478 km, geen wegkm; OSRM 559,3 km [7]; N3 Heidelberg-Durban 501 km [4] + Springs-Heidelberg ~35 + havenstraten ~20 = ~556 | maak_stroombeen_weg (nieuw profiel, `zuid-afrika`) | nee |
| b4 | B | zee | `ni-durban-kade` → zeeknoop 5202 (-29.8168, 31.1737) | haven-aanloop (kade 16,7 km van de zeeknoop, > 5 km) | 17,8 | KOPIE `aanloop-durban.geojson` (koper-tfm-durban) | **ja**, net reikt niet |
| b5 | B | zee | zeeknoop 5202 → `ni-baltimore-seagirt` | Mozambiquekanaal, Kaap, Atlantische Oceaan, Chesapeake Bay | geen gepubliceerde zeekm; droogloop 14.387 (hemelsbreed 13.485) | MARNET, beennaam met "aannemelijk: één bron" | nee (Seagirt 2,7 km van zeeknoop 4839: geen aanloop) |

Geen spoor-, binnenvaart-, leiding- of luchtbeen. De ±15%-toets is voor b1-b3 een indicatie (geen wegkm-bron). b1+b2 zijn byte-gelijk aan `pgm-zimplats-springs`; nieuw is alleen b3 (559 km) + b5 (14.387 km) = ~15.000 km nieuw, ~1.250 km kopie.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-zimplats-smc` | smelter (matte) | Zimplats Selous Metallurgical Complex — letterlijk uit `pgm-zimplats-springs.md` | -18.0328, 30.4334 | [1][2][11] | bron-gelegd (zie die brief: smelter met pluim, tailingsdam) |
| `ni-beitbridge-grens` | grensovergang | Beitbridge-grens, Limpopo-brug — idem | -22.2244, 29.9865 | [11] | bron-gelegd (idem) |
| `ni-springs-irs` | raffinaderij / overslag | Impala Refining Services, Springs — idem | -26.2227, 28.4437 | [2][11] | bron-gelegd (zie die brief: productiehallen, tailingsbekkens) |
| `ni-durban-kade` | overslag truck → container → zee | Durban Container Terminal Pier 2, noordkade — letterlijk uit `lithium-bikita-tianjin.md` | -29.8790, 31.0160 | [3][12] | bron-gelegd (z15: STS-kranen en containerstacks); kadekeuze *aannemelijk*: Panjiva noemt alleen "Durban", Pier 1 of 2 niet gebronnd |
| `ni-baltimore-seagirt` | losplek (zee-eindpunt) | Seagirt Marine Terminal, Baltimore (Nominatim-punt) | 39.2573, -76.5468 | [3][5][6][8] | aannemelijk (z15 gezien, `sat-nikkel-zimplats-springs-seagirt.png`: containerstacks met STS-kranen langs de zuidwestkade, kruis ~0,35 km landinwaarts van de kade op het terrein; terminal volgt uit MSC-gebruik, niet uit de zending) |

## 4 · Via-punten (alleen b3; b1/b2 zijn kopie)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Wit Road (R29-oost Springs-Heidelberg, midden) | -26.3584, 28.4573 | directe zuidroute naar de N3 i.p.v. westwaarts via N12/N17 en Gillooly's (ontwerp: N12/N17; OSRM kiest Wit Road) |
| b3 | 2 | Heidelberg, N3-oprit | -26.4946, 28.3783 | hier gaat de corridor de N3 op |
| b3 | 3 | Villiers (N3) | -27.0414, 28.6268 | N3 i.p.v. een zijroute door de Vrijstaat |
| b3 | 4 | Harrismith (N3-bypass) | -28.2664, 29.1322 | N3 over de bypass, niet de stad in |
| b3 | 5 | Mooi River (N3) | -29.2076, 30.0021 | houdt de N3 vast i.p.v. de R103 |
| b3 | 6 | Pinetown (N3, bij de M7-afslag) | -29.8235, 30.8010 | N3 tot Durban-West i.p.v. een tak naar de Bluff; daarna eindklassen-regel naar Bayhead |
Alle punten komen van de OSRM-geometrie (op de weg), niet uit een stadscentrum. Geofabrik-regio's: `zuid-afrika` (b3; b1 `zimbabwe` + `zuid-afrika`, b2 `zuid-afrika`, beide kopie). Refs b3: `N3`. Venster 40 km volstaat (directe lijn); controleer de wegklasse van Wit Road en zet zo nodig `corridorKlassen: ["tertiary"]`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Zimplats SMC | Zimplats (87% Implats) | concentraat → matte (6E + Ni) | orde 4-6 kt Ni in matte (eigen schatting) | [1][2] |
| IRS Springs (BMR) | Implats | matte → geraffineerde PGM + nikkel (o.a. Ni-poeder) | IRS 10.589 t Ni FY2024 groepsbreed (haalbaarheidstoets, niet zelf geopend) | [2][9] |

## 6 · Stoppunt
Bij Seagirt (Baltimore): Panjiva noemt als geadresseerde Chemalloy Company LLC (Philadelphia), maar geen bron legt een vervolgvervoer of fabriek vast, dus geen fase D/E.

## 7 · Open punten
- **Nikkelherkomst:** Ni-poeder van Springs is niet tot Zimplats-matte te herleiden (IRS raffineert ook andere feed, groepsbreed); alleen "kan zo lopen". Geen Ni-tonnage per Zimplats gepubliceerd [1].
- **Baltimore = één bron** [3]: Panjiva (geen bedrijfsopgave); de grondstof (nikkelpoeder) volgt alleen uit HTS 7504, het goederenveld is afgeschermd; één zending 20.895 kg in 80 vaten, MSC Carmen 538N.
- **Vervoer Springs → Durban onbekend:** truck is aanname (Transnet-spoor of containertrein kan); 559 km is OSRM, geen bedrijfs-wegkm.
- **Corridorkeuze Springs → N3** (Wit Road vs N12/N17) niet gebronnd; OSRM-droogloop kiest Wit Road (ontwerp zei N12/N17).
- **Seagirt-terminal en Durban Pier 1/2** niet in de zending genoemd: MSC werkt sinds 1990 vanuit Seagirt [6], Durban ongebronnd.
- **Zimbabwaans exportbeleid** kan de matte-uitvoer doen stoppen (alleen zoekresultaat, zie `pgm-zimplats-springs.md`).
- **Overlap:** b1+b2 zijn kopie van `pgm-zimplats-springs`; Durban-aanloop kopie van `koper-tfm-durban`.

## 8 · Bronnen
[1] Zimplats, Integrated Annual Report 2025 (nikkelomzet USD 80,0/69,6 mln, p.91; uit het ketenontwerp, PDF > 10 MB niet door mij geopend). https://zimplats.com/data/2026/05/2025-Integrated-Annual-Report.pdf
[2] Implats, Zimplats Fact Sheet 2025 (matte naar Springs onder life-of-mine met IRS). https://implats.co.za/pdf/fact-sheets/2025/fact-sheet-zimplats.pdf
[3] Panjiva, Impala Platinum Ltd Refineries (HTS 7504.00, 20.895 kg, 80 vaten, Durban → Baltimore, 2025-10-26, MSC, geadresseerde Chemalloy Co LLC). https://www.panjiva.com/Impala-Platinum-Ltd-Refineries/1132028
[4] Wikipedia, "N3 road (South Africa)" (Heidelberg 501 km van Durban; totaal 578 km). https://en.wikipedia.org/wiki/N3_road_(South_Africa)
[5] Wikipedia, "Port of Baltimore" (Seagirt: containerterminal, vier ligplaatsen, Northwest Branch Patapsco). https://en.wikipedia.org/wiki/Port_of_Baltimore
[6] FreightWaves, "MSC extends Baltimore contract for 6 years", 2009 (MSC eerste lijn bij Seagirt). https://www.freightwaves.com/news/msc-extends-baltimore-contract-for-6-years
[7] OSRM publieke router, Springs-anker → Durban DCT Pier 2: 559,3 km, 6,9 uur (indicatie, OSM-afgeleid). https://router.project-osrm.org
[8] OSM Nominatim, Seagirt Marine Terminal 39.2573, -76.5468 (webcheck uit de haalbaarheidstoets). https://nominatim.openstreetmap.org
[9] Impala Platinum SENS 2019 (IRS-productie incl. "nickel refined"). https://senspdf.jse.co.za/documents/SENS_20190426_S414083.pdf
[10] Esri World Imagery z15 via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-nikkel-zimplats-springs-seagirt.png` (Seagirt); hergebruikt: `sat-pgm-springs-zurich-springs.png`, `sat-lithium-bikita-tianjin-durban-dct2.png`.
[11] `v2/design/routebrieven/pgm-zimplats-springs.md` (ankers smc, Beitbridge, Springs; b1 663,2 km, b2 583,4 km).
[12] `v2/design/routebrieven/lithium-bikita-tianjin.md` en `koper-kolwezi-durban.md` (Durban DCT Pier 2, `aanloop-durban.geojson`, MARNET-zeeknoop 5202).
[13] MARNET-droogloop (hecht_marnet, scratch): zeeknoop Durban → Seagirt 14.387,3 km, 90 edges; Seagirt snapt 2,67 km op zeeknoop 4839.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-nikkel-zimplats-springs.json` (369,4 KB, contract 2, lonlat) · **functie:** `bak_nikkel_zimplats_springs` in `bak_stromen.sh` (opdracht-id; de brief noemt het id `nikkel-zimplats-springs`, eindpunt is Baltimore: titel en noot zeggen het, centraal hernoemen kan). **Totaal 16.212,7 km** · 5 benen · 5 markers.

| # | modaliteit | km gebakken | brief | afwijking | naad naar vorig been |
|---|---|---|---|---|---|
| b1 | truck | 663,2 | hemelsbreed 468, geen wegkm | kopie, indicatie | 0 |
| b2 | truck | 583,4 | hemelsbreed 471, geen wegkm | kopie, indicatie | 0 |
| b3 | truck | 561,0 (weggeometrie 560,8) | OSRM 559,3 | +0,3% | 0 |
| b4 | zee, stippel | 17,8 | 17,8 | 0 | 0 |
| b5 | zee | 14.387,3 | droogloop 14.387,3 | 0 | 0,04 |

**Recept.** b1/b2 = LETTERLIJKE KOPIE van `pgm-zimplats-springs-weg-smc-beitbridge-gedeeld.geojson` en `…-weg-beitbridge-springs.geojson`. b3 = nieuw profiel `nikkel-zimplats-springs-springs-durban` (extract `zuid-afrika`, refs N3, venster 40 km, 8 via-punten uit §4 inclusief de ankers) via `wegscan_puur.py`: alle snaps 0,00-0,04 km (laatste anker 0,09), geen corridorKlassen nodig (Wit Road lag gewoon in het net), first mile 0,3 km, last mile 7,4 km over havenstraten (service, tertiary, unclassified) naar de DCT-kade. b4 = kopie `aanloop-durban.geojson`. b5 = MARNET zeeknoop 5202 (-29,8168; 31,1737) naar Seagirt (39,2573; -76,5468), 90 edges.

**Stippel/aanloop.** Alleen b4 (net reikt niet: kade 16,7 km van zeeknoop 5202, > 5 km). Geen aanloop bij Baltimore: Seagirt snapt 2,67 km op zeeknoop 4839 (< 5 km). Geen lucht, spoor, leiding, binnenvaart.

**Toets.** Geen naad > 5 km (max 0,04 km). Markers 1-4 op 0,0 km van de lijn; **Seagirt-marker 2,67 km van het lijneinde** (de zee-snap; onder de 5 km-grens, dus geen aanloop; blijft bevinding). `toets_knikken`: 54 knikken, 0 terugloop (52 spikes van 4-35 m op haven- en terreinwegen bij de ankers, 1 omkering in de gekopieerde b2, 1 krappe bocht 6 km vóór Seagirt in de Chesapeake). `toets_rechte_benen --min-km 5`: geen hit voor deze stroom. Bestand 369 KB: boven de ~300 KB-richtlijn (lange truckbenen), noot, geen herbak.

**Lessen.** (1) Wit Road (R29) en de N3 liggen zonder corridorKlassen in het OSM-net; de ontwerp-corridor N12/N17 is niet nodig. (2) De ±15%-toets is voor b1-b3 een indicatie (geen wegkm-bron); b3 komt wel binnen 0,3% van OSRM. (3) Id-kwestie: brief heet `nikkel-zimplats-springs`, opdracht en bestand `nikkel-zimplats-springs`.
