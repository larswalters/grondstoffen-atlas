# Routebrief (licht) · goud — Otjikoto (Otjozondjupa) → Hosea Kutako (WDH) → OR Tambo (JNB) → Rand Refinery (Namibië → Zuid-Afrika)

**stroom-id:** `goud-otjikoto-randrefinery` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) ·
**status:** gebakken
**Keten in één zin:** doré van de Otjikoto-mijn (B2Gold 90% / EVI 10%) per truck over de B1/A1 en de B6 naar het vrachtplatform van Windhoek Hosea Kutako (WDH), per vrachtvlucht (grootcirkel) naar de vrachtterminal van OR Tambo (JNB), en per truck over de R21/N12 naar Rand Refinery in Germiston. **Aannemelijk: één bron voor de afnemer, geen bron voor het vervoer (§7).**
**Welke as van het verhaal:** Namibië → Zuid-Afrika, de doré-as van Namibië's grootste goudmijn naar de Afrikaanse doré-raffinaderij. Otjikoto 2025 = 199.139 oz = **≈ 6,2 t Au/j** (koz ÷ 32,15; 100%-basis, B2Gold houdt 90%) [2]; 2026-guidance 70.000–90.000 oz (≈ 2,2–2,8 t) omdat de dagbouw in Q4 2025 klaar is [2]. Peiljaar 2025.

## 1 · Ketenkaart
```
Otjikoto-verwerkingscomplex `au-otjikoto-plant`
  ──(b1 truck · mijnweg → B1 (Otjiwarongo) → A1 (Okahandja, Windhoek-Western Bypass) → Nelson Mandela Ave → B6 · hemelsbreed 280 km, geen wegkm; OSRM-indicatie 364 km)──►
Windhoek Hosea Kutako (WDH), terminal-/vrachtapron `au-wdh-vracht` (hergebruikt uit diamant-namdeb-gaborone)
  ──(b2 lucht · vlucht WDH → JNB, grootcirkel, aannemelijk: één bron voor de afnemer, vervoer niet gebronnd · 1.164 km grootcirkel)──►
OR Tambo vrachtterminal `au-jnb-vracht` (hergebruikt uit goud-mponeng-londen)
  ──(b3 truck · R21/N12 · 25,7 km, letterlijke kopie van goud-kibali-randrefinery b4, aannemelijk)──►
Rand Refinery, Germiston `au-randrefinery` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Otjikoto-plant → WDH-vrachtapron | mijnweg (OSM service, asfalt) → B1 → Otjiwarongo → A1-bypass Okahandja → A1 Western Bypass Windhoek → Nelson Mandela Ave → B6 (Sam Nujoma Dr). **Aannemelijk: vervoer niet gebronnd** | hemelsbreed 280 km, geen wegkm; AIF: "approximately 300 km north of Windhoek" en "70 km NE of Otjiwarongo" [1] (afstandsopgaven, geen wegkm); OSRM-proefroute 364,1 km [9] (B1 69,1 km tot Otjiwarongo klopt met de AIF). ±15%-toets = indicatie (310–420 km) | maak_stroombeen_weg (extract namibie) | nee |
| b2 | B | lucht | WDH → OR Tambo (JNB) | vlucht WDH → JNB (**aannemelijk: één bron voor de afnemer; vlucht zelf niet gebrond**) | 1.163,7 grootcirkel [berekend met maak_luchtbeen] | maak_luchtbeen | nee, doorgetrokken |
| b3 | C | truck | JNB-vrachtterminal → Rand Refinery | R21/N12 (**aannemelijk: één bron voor de afnemer**) | 25,7 [10] | LETTERLIJKE KOPIE goud-kibali-randrefinery-weg-jnb-randrefinery.geojson | nee |

Het ontwerp had een vierde been (last mile airside, stippel). Dat vervalt: de B6-weg uit goud-/diamant-namdeb eindigt 0,04 km van `au-wdh-vracht` (diamant-namdeb-gaborone §9), dus geen airside-gat. Komt de bake alsnog > 0,2 km van het anker uit, voeg dan een stippel "truck|WDH-vrachtplatform last mile (schematisch — airside/privéterrein)" toe.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-otjikoto-plant` | mijn / laadplek (verwerking) | Otjikoto-verwerkingscomplex (B2Gold) | -19.9923, 17.0906 | [1][5][osm] | bron-gelegd (z15 gezien: processing-hallen, tanks en erts-/materiaalopslag direct ZW van de pit, TSF-plateau 1,5 km ZZW, mijnweg naar de B1 in het NW; het ontwerppunt -19.92, 16.95 is niet de mijn maar het Otjikoto Solar Power Station [8], 15 km W: verschoven; OSM landuse "Otjikoto Mine" -19.9923, 17.0906) |
| `au-wdh-vracht` | overslag truck → lucht | Hosea Kutako Int'l (WDH), terminal-/vrachtapron | -22.4863, 17.4643 | [6][dia-brief] | aannemelijk (hergebruikt letterlijk uit diamant-namdeb-gaborone; z16 hier opnieuw gezien: terminalgebouw met platform en meerdere toestellen, geen los vrachtgebouw te onderscheiden; pand **onzeker**) |
| `au-jnb-vracht` | overslag lucht → truck | OR Tambo vrachtterminal | -26.1440, 28.2295 | [10] | bron-gelegd (hergebruikt letterlijk uit goud-mponeng-londen.md) |
| `au-randrefinery` | raffinaderij / stoppunt | Rand Refinery, Germiston | -26.2189, 28.1550 | [7][10] | bron-gelegd (hergebruikt letterlijk uit goud-mponeng-londen.md) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Alle punten zijn wegvertices van de OSRM-proefroute [9] en liggen 4–14 m van de OSM-weg (gemeten); geen enkel punt in een stadscentrum.
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | B1 bij de mijntoegang (OSM service way 666012294 begint hier) | -19.9808, 17.0683 | pint de mijnweg-aansluiting op de B1 (mijnweg 2,4 km); de B1 loopt hier met de spoorlijn parallel (z15 gezien) |
| b1 | 2 | B1 ten Z van Otjiwarongo | -20.5857, 16.7462 | houdt de route op de B1 en buiten het stadscentrum van Otjiwarongo; geen alternatief verhard pad |
| b1 | 3 | A1-bypass ten W van Okahandja | -22.0098, 16.8810 | pint de route op de A1-snelweg om Okahandja; **niet** het via-punt van motheo-walvisbay (-21.9858, 16.9114): dat ligt op Koebel Street in de stad, 2,8 km van de A1 |
| b1 | 4 | A1 Western Bypass, noordrand Windhoek | -22.5242, 17.0727 | kiest de westelijke A1-bypass boven Independence Avenue (B1 door het centrum) |
| b1 | 5 | Nelson Mandela Avenue ten O van het centrum | -22.5509, 17.0868 | verbindt de A1 met de B6 zonder het CBD; alternatief via Independence Ave/Hosea Kutako Drive uitgesloten |
| b1 | 6 | B6 Sam Nujoma Drive, begin Trans-Kalahari-corridor | -22.5796, 17.1168 | pint de B6 oostwaarts naar het vliegveld (gedeeld stuk met diamant-namdeb b2) |
| b3 | — | geen: de kopie draagt de via-punten van de bron | — | niet opnieuw routeren |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Otjikoto-verwerkingscomplex | Otjikoto Mine (B2Gold 90% / EVI Mining 10%) | erts → doré | 199.139 oz Au 2025 (≈ 6,2 t); 2026 70–90 koz | [1][2][3] |
| Rand Refinery (Germiston) | Rand Refinery (Pty) Ltd | doré → LBMA-baren | niet gebronde capaciteit | [7][10] |

## 6 · Stoppunt
Rand Refinery: de brief stopt waar de enige bron stopt ("doré … exported to the Rand Refinery in South Africa") [1]. De verdere afzet (Londen e.d.) is goud-mponeng-londen; fase D/E vervallen. Het BoN-plan om Otjikoto-goud in Zuid-Afrika te laten raffineren en terug te halen voor de reserves [4] is een voorstel en niet getekend.

## 7 · Open punten
- **Dunne evidentie voor de afnemer, één bron [1]:** alleen de AIF over FY2022 zegt dat Otjikoto-doré naar Rand gaat; de AIF over FY2025 [3] noemt Rand niet (Fekola gaat daar wel naar Metalor). Daarom "aannemelijk" in b2 en b3. Of dit nog geldt in 2025/26 is niet aangetoond.
- **Vervoer niet gebronnd:** geen bron noemt WDH, een vlucht of een truck naar Johannesburg (≈ 1.600 km over de weg) voor deze doré. De mijn heeft een eigen landingsstrip (AIF [1]; OSM-baan -19.992, 17.127, gravel, 4 km O van de plant): een vlucht rechtstreeks vanaf de mijn kan evengoed. Gekozen is de verharde baan van WDH op het ontwerp; niet getekend: een directe mijn-vlucht, of de weg naar JNB.
- **BoN-plan (06-02-2026) [4]:** de Bank of Namibia voert gesprekken met Rand Refinery om Otjikoto- en Navachab-goud te raffineren (99%) en in eigen kluis te bewaren: voorstel, geen contract voor Otjikoto gevonden; implicatie voor de huidige route onbekend.
- Km b1: AIF "300 km north of Windhoek" is een afstandsopgave; OSRM 364 km is OSM-gebaseerd, geen onafhankelijke toets: de ±15%-toets is een indicatie.
- Pand op WDH onzeker (zie §3); WDH is aannemelijk-anker uit de diamantbrief.
- **Sitelaag:** `goud-sitelaag.json` heeft geen Otjikoto-site; centraal toevoegen op -19.9923, 17.0906 (= `au-otjikoto-plant`, 90% B2Gold, ≈ 6,2 t Au/j).
- Volume daalt sterk in 2026 (70–90 koz) door einde dagbouw; peiljaar blijft 2025.

## 8 · Bronnen
[1] B2Gold, Annual Information Form FY2022, SEC EDGAR (Otjikoto: "approximately 300 km north of Windhoek", 70 km NE van Otjiwarongo, airstrip, B1; "Doré produced is exported to the Rand Refinery in South Africa"; 161.614 oz in 2022): https://www.sec.gov/Archives/edgar/data/1429937/000106299323007087/exhibit99-1.htm
[2] B2Gold, Form 6-K Q4/FY2025 results (Otjikoto 199.139 oz in 2025; 2026-guidance 70.000–90.000 oz; open pit klaar Q4 2025): https://www.sec.gov/Archives/edgar/data/1429937/000117184326000905/exh_991.htm
[3] B2Gold, Annual Information Form (stand 31-12-2025), SEC EDGAR (Otjikoto 90% / EVI 10%; Rand Refinery niet genoemd): https://www.sec.gov/Archives/edgar/data/1429937/000110465926026310/tm266740d1_ex99-1.htm
[4] Windhoek Observer, 06-02-2026, "Gold stockpile talks advanced, says B2Gold" (BoN-gesprekken met Rand Refinery over raffinage Otjikoto/Navachab): https://www.we.com.na/market-watch/gold-stockpile-talks-advanced-says-b2gold-nmh004876-3015-5041
[5] Miningmx, "Namibia's gold rush is intact thanks to Wia, B2Gold" (Otjikoto "about 300km north of Windhoek", open pit klaar okt-2025, LoM 2032): https://www.miningmx.com/news/gold/66110-namibias-gold-rush-is-intact-thanks-to-wia-b2gold/
[6] Wikipedia, "Hosea Kutako International Airport" (22°29'12"S 17°27'45"E; 45 km ten oosten van Windhoek): https://en.wikipedia.org/wiki/Hosea_Kutako_International_Airport
[7] Wikipedia, "Rand Refinery" (26°13'08''S 28°09'18''E): https://en.wikipedia.org/wiki/Rand_Refinery
[8] Wikipedia, "Otjikoto Solar Power Station" (-19.9237, 16.9529: het ontwerppunt van de mijn bleek dit): https://en.wikipedia.org/wiki/Otjikoto_Solar_Power_Station
[9] OSRM-proefroute (router.project-osrm.org, OSM-data), 2026-10-31: mijn → WDH-apron 364,1 km via B1, A1, Nelson Mandela Ave, B6; vias uit de weggeometrie.
[10] `v2/design/routebrieven/goud-mponeng-londen.md` §3/§9 en `goud-kibali-randrefinery.md` §3/§9 (au-jnb-vracht, au-randrefinery, b4 25,7 km): hergebruikt.
[dia-brief] `v2/design/routebrieven/diamant-namdeb-gaborone.md` §3/§9 (dia-wdh-cargo -22.4863, 17.4643; B6-weg 44,6 km, anker-stukje 0,04 km): hergebruikt.
[osm] OpenStreetMap (ODbL) via Overpass (overpass.openstreetmap.fr), 2026-10-31: landuse "Otjikoto Mine" -19.9923, 17.0906; service-weg 666012294 (asfalt) B1 → plant; A1 Western Bypass (way 56415136), B6 Sam Nujoma Drive (way 24747741), B1 Okahandja Bypass (way 83491388), baan -19.992, 17.127.
Satellietblik: `v2/build-cache/satcheck/sat-goud-otjikoto-randrefinery-plant.png` (z15), `-mijnweg.png` (z15), `-wdh.png` (z16), Esri, 2026-10-31.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
**Recept:** `bash v2/tools/bak_stromen.sh goud-otjikoto-randrefinery` → `v2/data/stroomroute-goud-otjikoto-randrefinery.json` (45,6 KB, versie 2, `lonlat`).
Functie `bak_goud_otjikoto_randrefinery()`, profiel `goud-otjikoto-randrefinery-plant-wdh` (scan met `wegscan_puur.py`, extract namibie, 10 s). **1.555,4 km · 3 benen · 2.170 punten · 4 markers · 0 stippel.**

| # | modaliteit | been | km gebakken | km brief | naad naar vorige |
|---|---|---|---|---|---|
| b1 | truck | Otjikoto-plant → WDH-vrachtapron (mijnweg, B1, A1-bypass, A1 Western Bypass, Nelson Mandela Ave, B6) | 366,0 | hemelsbreed 280, geen wegkm; OSRM 364,1 (+0,5%); AIF ca. 300 | — |
| b2 | lucht | vlucht WDH → JNB (grootcirkel, aannemelijk: één bron) | 1.163,7 | 1.163,7 (berekend) | 0,000 |
| b3 | truck | JNB-vrachtterminal → Rand Refinery (R21/N12, kopie) | 25,7 | 25,7 | 0,000 |

**Markers (reisvolgorde, alle 0,0 m van de lijn):** au-otjikoto-plant -19.9923,17.0906 · au-wdh-vracht -22.4863,17.4643 · au-jnb-vracht -26.1440,28.2295 · au-randrefinery -26.2189,28.1550.

**Toelichting per been**
- **b1 (weg).** Alle zes via-punten uit §4 snapten op 0,00-0,11 km (geen omweg, geen bijgeschoven punt); segmenten 2,8 / 87,4 / 162,8 / 63,2 / 3,9 / 5,7 / 40,1 km. 12 keerlussen gesnoeid (alle < 0,05 km). Eerste mile over de mijnweg (service) 2,74 km, last mile 1,30 km. Geen wegkm gepubliceerd: de ±15%-toets is een indicatie en klopt met de OSRM-proef (364,1 km). `toets_knikken`: 8 knikken, 0 omkeringen, allemaal spikes van 2-119 m op de mijnwegen rond de plant en het apron.
- **b1 eindigt 0,04 km van het WDH-anker** (B6): geen airside-stippel nodig, dus geen stippel in deze stroom.
- **b2 (lucht).** `maak_luchtbeen.py`, 48 punten, doorgetrokken; "grootcirkel" en "aannemelijk: één bron" in de beennaam. Geen bron voor WDH als overslag of voor de vlucht (§7).
- **b3 (weg).** Letterlijke kopie (381 punten, 25,7 km) van `goud-kibali-randrefinery-weg-jnb-randrefinery.geojson`; de 2 omkeringen (168°, 162°) en de spikes bij de terminal zijn identiek aan goud-kibali-randrefinery b4 en goud-geita-randrefinery b4.
- **Haven-aanloop, leiding, zeebeen:** n.v.t. Fase D/E vervallen (stoppunt Rand Refinery, §6). `toets_rechte_benen --min-km 5`: geen Otjikoto-been gemeld.

**Lessen / open voor centraal**
- Sitelaag `goud-sitelaag.json` mist Otjikoto: centraal toevoegen op -19.9923, 17.0906 (= `au-otjikoto-plant`).
- Namibie-scan van 10 s: de extract is klein en het venster van 40 km volstond; geen `corridorKlassen` nodig.
- Aannemelijk: één bron (AIF FY2022) voor de afnemer; AIF 2025 noemt Rand niet; vervoer via WDH en de vlucht zijn niet gebronnd (§7).
