# Routebrief (licht) · kolen — Tagebau Hambach (bruinkool) → Hambachbahn → Kohlebunker Niederaussem (Duitsland)

**stroom-id:** `kolen-hambach-niederaussem` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) · **status:** gebakken
**Keten in één zin:** **bruinkool** (geen steenkool) uit de Rijnlandse dagbouw Hambach (RWE Power) gaat per elektrisch **RWE-werkspoor** (Hambachbahn, daarna Nord-Süd-Bahn)
van de Kohlebunker/Wendeschleife Hambach naar de kolenopslag van kolencentrale Niederaussem (RWE, 2.220 MW netto); de band naar de ketels (1,7 km, eigen terrein) is geen been.
Titel noemt het echte eindpunt (kolenopslag, niet de centrale zelf) en dat het bruinkool is: de bol kent nog geen bruinkool, centraal beslissen of dit onder `kolen` mag.
**Welke as van het verhaal:** *Europese eigen winning* — de grootste bruinkoolgroeve van Europa voedt een centrale op 16 km hemelsbreed. Hambach: **ca. 30 Mt bruinkool in 2019**
(RWE Power) [1]; eerder ca. 40 Mt/j (Wikipedia, geen jaartal) [2]. Aandeel Niederaussem: **ca. 10 Mt/j (stand okt. 2018, derdenbron)** [3]; Neurath 18 Mt. Peiljaar 2019 voor het volume.

## 1 · Ketenkaart
```
Kohlebunker + Wendeschleife Hambach `kolen-hambach-laad`
   ──(b1 spoor · RWE-werkspoor Hambachbahn → Bergheim-Auenheim → Nord-Süd-Bahn · router 30,2 km, hemelsbreed 16,3 km)──►
Kolenopslag Niederaussem `kolen-niederaussem-kolenopslag` ⏹ stoppunt (band 1,7 km oost naar de centrale)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `kolen-hambach-laad` → `kolen-niederaussem-kolenopslag` | Hambachbahn (6,6 kV, RWE Power; sinds sept. 2014 3 km zuidwaarts verlegd, parallel aan A4/HSL Köln–Aachen) → Bergheim-Auenheim → Nord-Süd-Bahn; slot via een Wendeschleife noord van Auenheim | geen totaal gepubliceerd; deelstuk Hambachbahn Kohlebunker–Stellwerk Fn **21,00 km** [4]; router 30,2 km over 55 edges (119 punten), hemelsbreed 16,3 km (verhouding 1,85, 0 bochten ≥60°) — ±15%-toets is indicatie, geen norm | toets_spoorroute (1-op-1-net, geen via) | nee |

Fase C vervalt: beide ankers liggen op het werkspoor zelf (snap kop 0,13 km, staart 0,18 km). Geen zee, weg, leiding, lucht, haven-aanloop of kopie.
Geen fase D (centrale draait op de kool, geen product dat een bron verder volgt), geen E.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-hambach-laad` | mijn / laadplek | Kohlebunker en Wendeschleife Hambach (RWE Power), aan de zuidrand van Tagebau Hambach | 50.8705, 6.5110 | [4][8] | bron-gelegd (z15 gezien: zwarte kolenbunker met laadsporen en spoorbundel die zuidoostwaarts het terrein verlaat, pit en afzetting noordoost). Wikipedia-mijncentrum 50.9108, 6.5028 snapt 3,56 km weg (in de groeve) en is niet gebruikt |
| `kolen-niederaussem-kolenopslag` | verwerker / losplek | Kolenopslag (Kohlebunker) kolencentrale Niederaussem, west van de centrale | 50.9890, 6.6490 | [5][8] | bron-gelegd (z15 gezien: lang noordwest–zuidoost kolenlager met laadsporen en rangeerterrein, transportband 1,7 km naar de centrale met koeltorens). Wikipedia-centralepunt 50.9957, 6.6690 ligt bij de ketels en geeft een omweg met 8 km overschiet [7] |

Hergebruik: geen bestaand anker (geen Duitse kolenketen in de sitelaag of de markers).

## 4 · Via-punten
Geen (bindend uit de haalbaarheidstoets). De route volgt het werkspoor zonder via: gemeten loopt hij eerst zuidelijk van de groeve (route-km 2-11, rond 50.85, 6.52-6.55: de in 2014 verlegde trace), passeert Bergheim-Auenheim op 0,3 km (route-km 26) en sluit via een gezien keerlus (Wendeschleife, z14, 51.005, 6.645) op de kolenopslag aan.
Alle punten liggen op OSM-ways met operator RWE Power (toets: 100% binnen 60 m, 0 omkeringen) [7]. Een via zou de lus kunnen forceren.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Tagebau Hambach | RWE Power | bruinkool → werkspoor | ca. 30 Mt (2019); 40 Mt eerder; winning eindigt 2029 (toets) | [1][2][7] |
| Kraftwerk Niederaussem | RWE Power | bruinkool → stroom (2021: 16,1 Mt CO2) | 2.220 MW netto; sinds 1-4-2024 drie blokken, uit 2029/2030 (toets) | [5][6][7] |

## 6 · Stoppunt
De brief stopt bij de kolenopslag: de bruinkool wordt in de centrale verbrand tot stroom en er is geen volgende fysieke locatie van de lading; de band van 1,7 km is eigen terrein.

## 7 · Open punten
- **Bruinkool is geen steenkool:** past alleen als de bol `kolen` ruim opvat; anders afkeuren centraal. Het stroom-id blijft staan.
- **Totale spoorkm niet gepubliceerd:** alleen Hambachbahn 21,00 km tot Stellwerk Fn [4] (een andere bron: 21,5 km); de ±15%-toets is dus indicatie.
- **Volume:** 30 Mt is 2019; huidige productie lager. Aandeel Hambach in Niederaussem (10 Mt/j, 2018) komt uit een derdenartikel [3], niet uit RWE; geen peil sindsdien.
- **Wendeschleife noord van Auenheim** (route-lus ~3 km) zien we op satelliet, geen bron noemt hem; het spoorplan staat in OSM.
- **Hambach levert ook aan Neurath, Frimmersdorf en Goldenberg** [2]; alleen deze streng is gekozen. Sitelaag kolen heeft geen Duitse bruinkoolsites (centraal).
- **Einddatum:** winning Hambach en blokken Niederaussem lopen af (2029/2030) volgens de toets, niet door mij bijgebrond.

## 8 · Bronnen
[1] RWE Power AG, Information an die Landesregierung NRW über die Anpassung der Planungen für das Rheinische Revier, Tagebau Hambach (Anlage 2.1, 2020) — "Im Jahr 2019 wurden rund 30 Mio. t Braunkohle gefördert", Nord-Süd-Bahn. https://www.rwe.com/-/media/RWE/documents/02-unsere-energie/braunkohle/neues-revierkonzept/information-der-rwe-power-ag-an-die-landesregierung-nrw-tagebau-hambach.pdf
[2] de.wikipedia, Tagebau Hambach — ca. 40 Mio. t/j, Transport per Hambachbahn → Auenheim → Nord-Süd-Bahn naar Niederaußem, Neurath/Frimmersdorf, Goldenberg. https://de.wikipedia.org/wiki/Tagebau_Hambach ; en.wikipedia Hambach surface mine https://en.wikipedia.org/wiki/Hambach_surface_mine
[3] Energiezukunft, 10-10-2018, RWE drosselt Braunkohleförderung um ein Drittel — 10 Mt naar Niederaußem, 18 Mt naar Neurath (per jaar, 2018). https://www.energiezukunft.eu/wirtschaft/rwe-drosselt-braunkohlefoerderung-um-ein-drittel
[4] de.wikipedia, Hambachbahn — Werksbahn RWE Power, 6,6 kV 50 Hz, Kohlebunker Hambach–Stellwerk Fn 21,00 km, verlegd sept. 2014. https://de.wikipedia.org/wiki/Hambachbahn
[5] de.wikipedia, Kraftwerk Niederaußem — 2.220 MW netto, drie blokken sinds 1-4-2024, versorging via Nord-Süd-Bahn. https://de.wikipedia.org/wiki/Kraftwerk_Niederau%C3%9Fem
[6] en.wikipedia, Niederaussem Power Station — lignite-fired, Bergheim. https://en.wikipedia.org/wiki/Niederaussem_Power_Station
[7] Haalbaarheidstoets keten kolen-hambach-niederaussem (2026-10-28): ankers gemeten, route 30,2 km, 100% op RWE-Power-ways, webcheck de.wikipedia en RWE (einddata).
[8] Esri World Imagery via `v2/tools/sat_check.py` (2026-10-28) — `v2/build-cache/satcheck/sat-kolen-hambach-niederaussem-laad.png`, `-bunker.png`, `-lus.png`; route-geojson `spoorroute-kolen-hambach-niederaussem-hambach-niederaussem.geojson` (toets_spoorroute, BAKE_SUFFIX=-raw, --hoofd-km=100).

## 9 · Bak-noot
**Gebakken (2026-10-28, lichte werkwijze, M31 golf 10).** `bash v2/tools/bak_stromen.sh kolen-hambach-niederaussem` -> `v2/data/stroomroute-kolen-hambach-niederaussem.json` (2,6 KB, versie 2, lonlat).

| # | modaliteit | been | km | punten | naad | stippel |
|---|---|---|---|---|---|---|
| 1 | spoor | trein Tagebau Hambach (bruinkool) -> Niederaussem-kolenopslag via Hambachbahn en Nord-Süd-Bahn (RWE-werkspoor) | 30,2 | 119 | - | nee |

Totaal 30,2 km, 2 markers (beide ankers uit §3, afstand tot de lijn 0,13 en 0,18 km). Geen naad (één been).

**Recept.** Eén run `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=50.8705,6.5110" "--naar=50.9890,6.6490" "--naam=kolen-hambach-niederaussem-hambach-niederaussem" --hoofd-km=100` (1-op-1-net, geen via; 55 edges, snap 0,13 en 0,18 km, 0 bochten >=60 graden). Het geojson uit die run is ongewijzigd als `--been-geojson "spoor|..."` gebruikt; geen profiel, geen extract-scan, geen haven-aanloop, geen stippel, geen kopie. Functie `bak_kolen_hambach_niederaussem` in `bak_stromen.sh`.

**Toets.** Router 30,2 km tegen hemelsbreed 16,3 km (verhouding 1,85) en tegen het deelstuk Hambachbahn 21,00 km (Kohlebunker tot Stellwerk Fn): geen gepubliceerd totaal, dus de +-15% is indicatie en geen norm; een totaal van 30 km is plausibel omdat het deelstuk nog het stuk Auenheim -> Nord-Süd-Bahn -> opslag mist. `toets_knikken`: 0 knikken, 0 omkeringen. Geen rechte benen. Stippel is er niet, dus geen "hier reikt het net niet".

**Lessen en open punten.**
- Bruinkool is geen steenkool: centraal beslissen of de bol dit onder `kolen` toelaat (kleur/filter); het id blijft staan.
- De Wendeschleife noord van Auenheim is een echte keerlus op een werkspoor, geen knik-fout; de verlegging van 2014 geeft het zuidelijke begin.
- Totale spoorkm niet gepubliceerd; volume 30 Mt (2019) en aandeel Niederaussem (10 Mt/j, 2018) niet bijgebrond; einddata 2029/2030 uit de haalbaarheidstoets.
- Sitelaag kolen mist Duitse bruinkoolsites (centraal; hier niet gewijzigd).
- Register en bundel zijn centraal: niet aangeraakt.

