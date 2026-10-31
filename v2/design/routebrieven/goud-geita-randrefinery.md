# Routebrief (licht) · goud — Geita → Mwanza (MWZ) → OR Tambo (JNB) → Rand Refinery (Tanzania → Zuid-Afrika)

**stroom-id:** `goud-geita-randrefinery` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 18) ·
**status:** gebakken
**Keten in één zin:** doré van de Geita-mijn (AngloGold Ashanti, Lake Zone) per truck over de T4 naar het vrachtplatform van Mwanza (MWZ), per vrachtvlucht (grootcirkel) naar de vrachtterminal van OR Tambo (JNB), en per truck over de R21/N12 naar Rand Refinery in Germiston. **Aannemelijk: één bron, en die is boilerplate (§7).**
**Welke as van het verhaal:** Oost-Afrika (Tanzania) → Zuid-Afrika, de doré-as van een AngloGold-mijn naar de raffinaderij waarin AngloGold 42,4% houdt. Geita 2025 = 491.644 oz = **≈15,3 t Au/j** (koz ÷ 32,15) [1]; sinds 17-06-2025 gaat 20% via Geita Gold Refinery naar de Bank of Tanzania [2], dus **hooguit 80% ≈ 12,2 t Au/j** naar Rand.

## 1 · Ketenkaart
```
Geita-verwerkingscomplex `au-geita-plant`
  ──(b1 truck · mijnwegen → T4 → Usagara → R153/R152 · OSRM 137,5 km, TRS ≈120 km)──►
Mwanza-luchthaven (MWZ), Cargo Apron `au-mwz-vracht`  ·  korte airside-stippel (b2)
  ──(b3 lucht · vlucht MWZ → JNB, grootcirkel, aannemelijk: één bron · 2.683 km)──►
OR Tambo vrachtterminal `au-jnb-vracht` (hergebruikt uit goud-mponeng-londen)
  ──(b4 truck · R21/N12 · 25,7 km, kopie van goud-kibali-randrefinery b4, aannemelijk)──►
Rand Refinery, Germiston `au-randrefinery` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Geita-plant → Mwanza, R152 bij het vrachtplatform | mijnwegen → T4 (Geita–Usagara) → R153 → R152 | ≈120 [1] ("approximately 120km west of Mwanza": afstandsopgave, geen wegkm); OSRM 137,5 [7]; hemelsbreed 94,1 | maak_stroombeen_weg (extract tanzania) | nee |
| b2 | A | truck | R152-eindpunt → Cargo Apron-anker | last mile airside | 0,13 [berekend] | stippel | **ja** — "last mile (airside/privéterrein, geen net)" |
| b3 | B | lucht | MWZ → OR Tambo (JNB) | vlucht MWZ → JNB (**aannemelijk: één bron; vlucht zelf niet gebrond**) | 2.683 grootcirkel [berekend] | maak_luchtbeen | nee, doorgetrokken |
| b4 | C | truck | JNB-vrachtterminal → Rand Refinery | R21/N12 (**aannemelijk: één bron voor de afnemer**) | 25,7 [8] | LETTERLIJKE KOPIE goud-kibali-randrefinery-weg-jnb-randrefinery.geojson | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-geita-plant` | mijn / laadplek (verwerking) | Geita-verwerkingscomplex (CIL 5,4 Mt/j) | -2.8676, 32.1865 | [1] | bron-gelegd (z15 gezien: verwerkingscomplex met hallen, ronde tanks en erts-/materiaalopslag, open pit met water 2 km ZW, TSF-plateau O; het punt ligt op het complex. [2] noemt de plant op 2°51'53'' dezelfde plek) |
| `au-mwz-vracht` | overslag truck→lucht | Mwanza Airport, Cargo Apron (NW-kop van de baan) | -2.4404, 32.9176 | [4][6] | bron-gelegd op terreinniveau (z16 gezien: OSM-"Cargo Apron" = grijs verhard vlak aan de baankop met één klein gebouw aan de zuidrand en een weg naar het zuidwesten; geen toestellen zichtbaar, de apron met toestellen en terminal ligt 0,8 km ZO; welk pand vracht afhandelt is niet te zien: pand **onzeker**) |
| `au-jnb-vracht` | overslag lucht→truck | OR Tambo vrachtterminal | -26.1440, 28.2295 | [8] | bron-gelegd (hergebruikt letterlijk uit goud-mponeng-londen.md) |
| `au-randrefinery` | raffinaderij / stoppunt | Rand Refinery, Germiston | -26.2189, 28.1550 | [8] | bron-gelegd (hergebruikt letterlijk uit goud-mponeng-londen.md) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Alle punten zijn OSM-wegvertices op de doorgaande weg (via een OSRM-proefroute langs de OSM-weg gevonden, niet in een centrum). Eerste 6 km vanaf de plant zijn mijn-/kleine wegen.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | T4 ten O van Geita | -2.8738, 32.2562 | verlaat Geita oostwaarts op de T4, sluit een noordelijke weg uit |
| b1 | 2 | T4 | -2.7822, 32.4945 | houdt de corridor op de doorgaande T4 |
| b1 | 3 | T4 bij de rotonde | -2.6609, 32.6219 | pint de T4 zuidwaarts van deze rotonde; golf 9 mat de corridor via de T4, niet via Busisi/de noordelijke oversteek |
| b1 | 4 | T4 | -2.7270, 32.8575 | T4 richting Usagara |
| b1 | 5 | Usagara-rotonde (kruising) | -2.6805, 32.9933 | de T4 draait hier naar Mwanza-noord |
| b1 | 6 | R153 noord van Usagara | -2.5840, 32.9205 | doorgaande R153 naar de luchthaven |
| b1 | eind | R152 bij het vrachtplatform | -2.4410, 32.9186 | R152 (unclassified, paved, OSM way 198258098) = openbare weg 127 m van het anker; hier begint de stippel b2 |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Geita-plant | Geita Gold Mining Ltd (AngloGold Ashanti 100%) | erts → doré (85-92% Au, 8-12% Ag) | 5,4 Mt erts/j; 491.644 oz Au 2025 | [1][2] |
| Rand Refinery (Germiston) | Rand Refinery (Pty) Ltd (AngloGold 42,4%) | doré → LBMA-baren | niet gebronde capaciteit | [2][9] |

## 6 · Stoppunt
Rand Refinery: de brief stopt waar de enige bron stopt (TRS: bullion "shipped to Rand Refinery in Johannesburg for further refining and sale"). De verdere afzet (Londen e.d.) is goud-mponeng-londen; fase D/E vervallen.

## 7 · Open punten
- **Dunne evidentie, boilerplate [1]:** dezelfde Rand-zin staat in de Geita-TRS van FY2021 t/m FY2025 (haalbaarheidstoets): geen nieuw bewijs ten opzichte van golf 9. Daarom "aannemelijk" in b3 en b4, maximaal 80% van het volume.
- **Geen bron voor MWZ als overslag of voor de vlucht MWZ → JNB** (TRS en 20-F: niets over vervoer). Indirect: Rand Refinery ontvangt doré van AngloGold-mijnen in Afrika en leunt daarvoor op vluchten (Bloomberg 2020: levering "disrupted", gebrek aan commerciële vluchten) [10]. Dat is geen Geita-bron.
- **Conflict met de keuze MWZ:** de enige bron die Geita-goud per vliegtuig noemt (Reuters/Miningmx, 06-01-2012) beschrijft 587 kg staven in een toestel op de **mijn-airstrip**, met een wekelijkse vlucht op donderdag; bestemming niet genoemd [3]. De TRS zegt dat de mijn-strip (6 km N van de plant) dirt is voor kleine tot middelgrote propellertoestellen [1]; een vrachtvlucht naar JNB vraagt een verharde baan, vandaar MWZ (3.712 m asfalt [4]). Mogelijk gaat het goud via de mijn-strip eerst naar MWZ of elders: niet gebrond, niet getekend. Geita Airport (GIT, 2,7423 S 31,7068 E, 50 km W van de plant) is een openbare passagiersluchthaven [5]: geen bron voor vracht, niet gebruikt.
- Km b1: TRS-120 is een afstandsopgave ("120km west of Mwanza"), geen wegkm; de ±15%-toets (103-138 km) is indicatie. OSRM-proefroute 137,5 km [7].
- Het Cargo Apron-anker is het OSM-genoemde vrachtplatform, geen bevestigde afhandelaar. Is het airside-pad niet te routeren: stippel b2 zoals in de tabel.
- Sinds 17-06-2025 gaat 20% naar de Bank of Tanzania via Geita Gold Refinery [2]: die afzet is niet getekend.
- **Sitelaag:** `goud-sitelaag.json` heeft geen Geita-site; centraal toevoegen op -2,8676, 32,1865 (= `au-geita-plant`). 20-F noemt de plantlengte als "32°11'12''W": typfout, de TRS zegt oost.

## 8 · Bronnen
[1] AngloGold Ashanti, Geita Gold Mine Technical Report Summary (current at 31-12-2025), SEC EDGAR, 26-03-2026 (2,8676 S 32,1865 E; 120 km W van Mwanza; bullion naar Rand Refinery; 491.644 oz 2025; mijn-airstrip 6 km N, dirt): https://www.sec.gov/Archives/edgar/data/1973832/000197383226000062/geitatechnicalreportsumm.htm
[2] AngloGold Ashanti, Form 20-F FY2025, SEC EDGAR (gold sale agreement 17-06-2025: 20% naar Bank of Tanzania via Geita Gold Refinery; 42,4% van Rand Refinery): https://www.sec.gov/Archives/edgar/data/1973832/000197383226000066/au-20251231.htm
[3] Reuters via Miningmx, 06-01-2012, "Tanzania police foil robbery at AngloGold mine" (587 kg staven in een toestel op de Geita-airstrip, wekelijkse vlucht op donderdag): https://www.miningmx.com/news/gold/26165-tanzania-police-foil-robbery-at-anglogold-mine/ (kopie: https://www.gwern.net/docs/www/www.reuters.com/219e65075a6ae9f0d9f701b09e8720722955ead4.html)
[4] Wikipedia, "Mwanza Airport" (2°26'40''S 32°56'00''E, MWZ/HTMW, baan 3.712 m asfalt): https://en.wikipedia.org/wiki/Mwanza_Airport
[5] Wikipedia, "Geita Airport" (GIT/HTGE, 2,7423 S 31,7068 E, Air Tanzania naar Dar es Salaam en Mwanza): https://en.wikipedia.org/wiki/Geita_Airport
[6] OpenStreetMap (ODbL) via Overpass (overpass.openstreetmap.fr), 2026-10-31: aeroway=apron "Cargo Apron" (way 1446582140, -2,44035 / 32,91757), "General Apron" (way 179263677), hangar (way 873728088), R152 (way 198258098).
[7] OSRM-proefroute (router.project-osrm.org, OSM-data), 2026-10-31: plant → Mwanza-vrachtplatform 137,5 km via T4 en R153; vias uit de weggeometrie.
[8] `v2/design/routebrieven/goud-mponeng-londen.md` §3/§9 en `goud-kibali-randrefinery.md` §3/§9 (au-jnb-vracht, au-randrefinery, b4 25,7 km): hergebruikt.
[9] Wikipedia, "Rand Refinery" (26°13'08''S 28°09'18''E): https://en.wikipedia.org/wiki/Rand_Refinery
[10] Bloomberg via Mining.com, 26-03-2020, "South African gold shipments to London have been cut off" (Rand Refinery: toevoer van mijnen op het continent verstoord, raffineert voor AngloGold Ashanti en Gold Fields): https://www.mining.com/web/south-african-gold-shipments-to-london-have-been-cut-off/
Satellietblik: `v2/build-cache/satcheck/sat-goud-geita-randrefinery-plant.png` (z15), `sat-goud-geita-randrefinery-mwz.png` (z16), Esri, 2026-10-31.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 18)
**Recept:** `bash v2/tools/bak_stromen.sh goud-geita-randrefinery` → `v2/data/stroomroute-goud-geita-randrefinery.json` (56,0 KB, versie 2, `lonlat`).
Functie `bak_goud_geita_randrefinery()`, profiel `goud-geita-randrefinery-plant-mwz` (scan met `wegscan_puur.py`, extract tanzania, 188 s). **2.846,1 km · 4 benen · 2.797 punten · 4 markers · 1 stippel (0,13 km).**

| # | modaliteit | been | km gebakken | km brief | naad naar vorige |
|---|---|---|---|---|---|
| b1 | truck | Geita-plant → R152 bij Mwanza-vrachtplatform (mijnwegen, T4, R153, R152) | 137,4 | ca. 120 (TRS-afstandsopgave, geen wegkm) = +14,5%; OSRM 137,5 | — |
| b2 | truck | stippel: Mwanza-vrachtplatform last mile (airside) | 0,13 | 0,13 (berekend) | 0,000 |
| b3 | lucht | vlucht MWZ → JNB (grootcirkel, aannemelijk: één bron) | 2.682,9 | 2.683 (berekend) | 0,000 |
| b4 | truck | JNB-vrachtterminal → Rand Refinery (R21/N12, kopie) | 25,7 | 25,7 | 0,000 |

**Markers (volgorde = reisvolgorde, alle 0,0 m van de lijn):** au-geita-plant -2.8676,32.1865 · au-mwz-vracht -2.4404,32.9176 · au-jnb-vracht -26.1440,28.2295 · au-randrefinery -26.2189,28.1550.

**Toelichting per been**
- **b1 (weg).** Alle zeven via-punten uit §4 snapten op 0,00-0,02 km (geen omweg, geen bijgeschoven punt). Segmenten 9,8 / 30,0 / 20,0 / 30,0 / 16,3 / 13,8 / 17,6 km. 15 keerlussen gesnoeid (alle < 0,05 km, lengte ongewijzigd). Eerste mile over kleine klassen 6,32 km (mijnwegen, residential/service/tertiary/unclassified), last mile 0,51 km unclassified. +14,5% tegen de TRS-afstandsopgave: binnen de ±15% maar die 120 km is geen wegkm; de gebakken 137,4 km valt samen met de OSRM-proef (137,5). `toets_knikken`: 10 knikken, 0 omkeringen; negen zijn 2-12 m-spikes op de mijnwegen rond de plant en op de rotonde bij het eindpunt, één 128° spike in het complex.
- **b2 (stippel).** R152-eindpunt (-2.4410,32.9186) → Cargo Apron-anker (-2.4404,32.9176), 0,13 km rechte lijn, reden in de naam: airside/privéterrein, geen net. De scan haalde het apron-anker niet zelf (openbare weg eindigt 127 m ervoor).
- **b3 (lucht).** `maak_luchtbeen.py`, 109 punten, doorgetrokken, "grootcirkel" en "aannemelijk: één bron" in de beennaam. Geen bron voor MWZ als overslag of voor de vlucht; de enige vliegbron (2012) noemt de mijn-airstrip (§7).
- **b4 (weg).** Letterlijke kopie (381 punten, 25,717 km, richting JNB → Rand al goed) van `goud-kibali-randrefinery-weg-jnb-randrefinery.geojson`, alleen id/naam/kopieVan in de properties aangepast; coördinaten ongewijzigd. De 2 omkeringen (168°, 162°) en de spikes bij de terminal zijn identiek aan goud-kibali-randrefinery b4 en goud-mponeng-londen b2.
- **Haven-aanloop, leiding, zeebeen:** n.v.t. Fase D/E vervallen (stoppunt Rand Refinery, §6). `toets_rechte_benen --min-km 5`: geen Geita-been gemeld.

**Lessen / open voor centraal**
- Sitelaag `goud-sitelaag.json` mist Geita: centraal toevoegen op -2.8676, 32.1865 (= `au-geita-plant`).
- De Rand-zin in de TRS is boilerplate (FY2021-2025); b3 en b4 blijven "aannemelijk", maximaal 80% van het volume; 20% naar de Bank of Tanzania is niet getekend.
- Het Cargo Apron-anker is een OSM-naam, afhandelaar onbevestigd; pand onzeker.
- De TRS-120 km is een afstandsopgave: de ±15%-toets op b1 is een indicatie, geen norm.
- Een weg-profiel met 7 via-punten op de doorgaande T4/R153/R152 snapte zonder aanpassing; het vooraf geproefde OSRM-traject was een goede voorspeller voor de scan.
