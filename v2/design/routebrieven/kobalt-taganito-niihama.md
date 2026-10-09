# Routebrief (licht) · kobalt — Taganito (Claver) → THPAL → Niihama (Japan)

**stroom-id:** `kobalt-taganito-niihama` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** limoniet uit de Taganito-mijn (TMC, Nickel Asia) gaat per eigen mijnweg naar de aangrenzende HPAL-fabriek THPAL (Sumitomo Metal Mining/Mitsui/Nickel Asia, Claver), waar het kobalt als deel van het nikkel-kobalt mixed sulfide (MS) van de eigen steiger per zeeschip naar de Niihama Nickel Refinery (SMM, Ehime, Shikoku) vaart — Japans enige raffinaderij van elektrolytisch kobalt.
**Welke as van het verhaal:** *Filipijns HPAL-kobalt naar Japanse raffinage* — kobalt als bijproduct van nikkel-HPAL, in Japan tot kobaltmetaal. Volume: **ca. 2,8 kt Co/jaar** (2.795 t contained Co verkocht in 2017; ontwerp 2.600–2.640 t; **peiljaar 2017, niet actueel**) [5][6]. Een Niihama-eigen kobaltoutput is niet gepubliceerd.
**⚠️ Dubbel met de nikkelstroom:** alle vier de benen zijn een **letterlijke kopie** van `nikkel-taganito-niihama` b1–b4 (zelfde lading in het MS, andere grondstoflaag — precedent `zilver-valcambi-londen` ↔ `goud-valcambi-londen`). Hachinohe/PAMCO-vertakking (b5/b6, saproliet-DSO) is **niet** mee: saproliet draagt geen kobalt.

## 1 · Ketenkaart
```
Taganito-mijn `co-taganito-laad` ──(b1 truck · eigen mijnweg TMC → THPAL · hemelsbreed 1,2 km, geen wegkm)──► THPAL-plant `co-thpal-plant`
   (interne overslag ~1,2 km naar de kade, geen eigen been — MS "verschijnt" op de kade)
   → THPAL-steiger `co-thpal-pier` ──(b2 zee · haven-aanloop Claver, stippel · 65,9 km)──► MARNET-zeeknoop 8314
   ──(b3 zee · MARNET · 3.043,8 km)──► MARNET-zeeknoop 5746 ──(b4 zee · haven-aanloop Niihama, stippel · 25,7 km)──►
   Niihama Nickel Refinery `co-niihama-refinery` (SMM) ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `co-taganito-laad` → `co-thpal-plant` | eigen mijnweg TMC → THPAL, aangrenzend terrein (Taganito-ecozone) [5][7] — **letterlijke kopie** nikkel b1 | hemelsbreed 1,2 km, geen wegkm; gebakken geometrie 1,9 km [9] | kopie `nikkel-taganito-niihama-weg-taganito-thpal.geojson`, geen nieuw profiel | nee |
| b2 | B | zee (haven-aanloop) | `co-thpal-pier` → MARNET-zeeknoop 8314 (9.8356, 125.3465) | — **letterlijke kopie** nikkel b2 | 60,5 hemelsbreed; 65,9 gebakken [9] | kopie `nikkel-taganito-niihama-aanloop-claver.geojson` | **ja** — kade 60,5 km van de zeeknoop, MARNET reikt niet tot de steiger |
| b3 | B | zee | MARNET-zeeknoop 8314 → 5746 (34.0720, 133.0479) | Filipijnenzee → oostelijk om Kyushu → Bungo-kanaal → Seto-binnenzee; **aannemelijk: Niihama = enige Japanse Co-raffinaderij (SMM), deel van het MS gaat mogelijk naar Harima** — **letterlijke kopie** nikkel b3 | 3.043,8 (gemeten MARNET) [9] | MARNET (`--been`, identiek aan nikkel b3) | nee |
| b4 | B | zee (haven-aanloop) | MARNET-zeeknoop 5746 → `co-niihama-refinery` | **aannemelijk: één bron voor de bestemming** — **letterlijke kopie** nikkel b4 | 23,2 hemelsbreed; 25,7 gebakken [9] | kopie `nikkel-taganito-niihama-aanloop-niihama.geojson` | **ja** — kade 23,2 km van de zeeknoop (>5 km), snap net binnen 25 km |

## 3 · Ankers (één per site en per overslag) — allemaal letterlijk hergebruikt uit `nikkel-taganito-niihama.md` §3
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `co-taganito-laad` | mijn / laadplek | Taganito Mining Corp. (Nickel Asia), Claver | 9.5464, 125.8193 | [7][9] | bron-gelegd (hergebruik `ni-taganito-laad`, z17 gezien in nikkelbrief: ertsstockpile naast de laadsteiger, mijnterrassen landinwaarts) |
| `co-thpal-plant` | verwerking (HPAL → MS, bevat het kobalt) | Taganito HPAL Nickel Corp. (THPAL) | 9.5395, 125.8106 | [3][5][6] | bron-gelegd (hergebruik `ni-thpal-plant`; z15 hier opnieuw gezien: groot procesterrein met tankbatterij en rode tailingsvijvers, ~1,2 km zuidwest van de steiger) |
| `co-thpal-pier` | overslag (kade) | Taganito/Claver-laadsteiger (TMC/THPAL) | 9.5490, 125.8160 | [7][9] | bron-gelegd (hergebruik `ni-thpal-pier`; z15 hier gezien: kruis op de kop van een steiger die vanaf de kust het water in loopt, schepen voor anker erachter) |
| `co-niihama-refinery` | losplek + raffinaderij | Niihama Nickel Refinery, SMM (Besshi-Niihama) | 33.9669, 133.2658 | [1][9] | bron-gelegd (hergebruik `ni-niihama-refinery`; z15 hier gezien: kadegebonden industrieblok tussen twee havenbekkens aan de westrand van Niihama, kades langs het blok; eigenaarschap volgt uit de OSM-landuse "SMM Besshi Works" [9], niet uit het beeld) |

**Ankerverschil (centraal rechttrekken):** kobalt-sitelaag `w-niihama` staat op 33.9496, 133.2316 (bedrijfsadres, ~3 km west); gebruik het satelliet-gelegde `ni-`/`co-niihama-refinery`-anker 33.9669, 133.2658. De kobalt-sitelaag heeft verder **geen** THPAL-site (alleen Niihama).

## 4 · Via-punten
Geen. b1 is een kopie van een 1,9 km-weg zonder corridorkeuze (eigen mijnweg, aangrenzend terrein); b2/b4 zijn haven-aanlopen en b3 is MARNET (zee = router, geen via-punten).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| THPAL | SMM (meerderheid) / Mitsui 15 % / Nickel Asia 10 % (stand 2018) | limonietertsslurry → Ni-Co mixed sulfide (~57–60 % Ni) | ontwerp 30 kt Ni (later 36 kt) + 2,6–2,64 kt Co/jaar; Co-verkoop 2.530 t (2016), 2.795 t (2017) | [3][5][6] |
| Niihama Nickel Refinery | SMM | MS (Coral Bay + Taganito) + nikkelmatte → elektrolytisch Ni + elektrolytisch Co (MCLE) | Co-tonnage niet gepubliceerd | [1][3][4] |

## 6 · Stoppunt
De brief stopt bij de Niihama-raffinaderij: dat is het eindpunt van het ketenontwerp (elektrolytisch kobalt voor magneet- en hardmetaaltoepassing [1]) en geen bron noemt een vervolgafnemer van dit specifieke kobalt — fase D/E vervallen.

## 7 · Open punten
- **"Alle Taganito-Co naar Niihama" is aannemelijk, niet bewezen:** in 2010/2011 kocht SMM het hele MS-volume voor Niihama [3][4], maar SMM noemt nu ook Harima (nikkelsulfaat) als afnemer van THPAL-MS [2]; waar de Co-fractie daar heen gaat is niet gepubliceerd.
- **Volume is peiljaar 2017**; geen 2023–2025-cijfer gevonden (zwavelprijs/Hormuz-verstoring kan de productie gedrukt hebben, voor THPAL niet bevestigd). Een Q3-2025-cijfer (9,9 kt Ni, −17,8 % j/j) staat in de pers zonder duidelijke THPAL-attributie — niet gebruikt.
- **Kobalt-sitelaag mist een THPAL-site** (capaciteit 2,6–2,8 kt Co) en heeft het verkeerde Niihama-anker — centraal toevoegen/rechttrekken.
- b1-km is hemelsbreed + gebakken geometrie; een gepubliceerde wegkilometer van de TMC–THPAL-mijnweg is niet gevonden (privéterrein).
- Visueel dubbel met de nikkelstroom (zelfde lijn, andere kleur) — bewust, per grondstoflaag.

## 8 · Bronnen
[1] Sumitomo Metal Mining, Niihama Nickel Refinery: enige Japanse plant voor elektrolytisch nikkel én kobalt; grondstof o.a. MS van Coral Bay en Taganito HPAL (2026-10-09 opgehaald). https://www.smm.co.jp/en/corp_info/location/domestic/nickel/
[2] Sumitomo Metal Mining, Harima Refinery: nikkelsulfaat uit MS van Coral Bay en THPAL. https://www.smm.co.jp/en/corp_info/location/domestic/harima/
[3] Mitsui & Co., Form 6-K (SEC), 2010: SMM koopt het gehele MS-volume (≈50 kt = 30 kt Ni + 2,6 kt Co/jaar) voor Niihama (Ehime) voor elektrolytisch Ni en Co. https://www.sec.gov/Archives/edgar/data/0000067099/000119312510210185/d6k.htm
[4] JBIC persbericht 2011, THPAL-lening: SMM koopt de hele MS-productie (50.000 t/jaar) en voert in naar Niihama voor nikkel- en kobaltblokken. https://www.jbic.go.jp/en/information/press/press-2011/0705-6295.html
[5] Nickel Asia Corp., Analysts' Presentation augustus 2018: THPAL-kobaltverkoop 2.265/2.638/2.530/2.795 t (2014–2017), MS "sold exclusively to Sumitomo", eerste lading okt 2013, NAC 10 %. https://nickelasia.com/assets/documents/Analysts_Presentation_August_2018.pdf
[6] THPAL-projectdocument (Caraga EMB/Land Matrix): 30.000 t Ni + 2.640 t Co als MS per jaar, exportzone Taganito. https://landmatrix.org/media/uploads/thpal.pdf
[7] Nickel Asia, Taganito Mining Corporation: mijn in Claver die limoniet aan THPAL levert. https://nickelasia.com/subsidiaries/taganito-mining-corporation
[8] Wikipedia, Nickel Asia Corporation: THPAL en Taganito-mijn in Claver, Surigao del Norte. https://en.wikipedia.org/wiki/Nickel_Asia_Corporation
[9] Eigen repo: `v2/design/routebrieven/nikkel-taganito-niihama.md` (ankers, OSM-landuse, km) en `v2/data/stroomroute-nikkel-taganito-niihama.json` (benen b1–b4 gebakken); satellietblikken `v2/build-cache/satcheck/sat-kobalt-taganito-niihama-co-{thpal-pier,niihama-refinery}.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-kobalt-taganito-niihama.json` (versie 2, `lonlat`, 10,3 KB) · functie `bak_kobalt_taganito_niihama()` in `v2/tools/bak_stromen.sh` · **4 benen · 3.137,3 km · 484 punten · 4 markers.** Recept: `bash v2/tools/bak_stromen.sh kobalt-taganito-niihama` (één `hecht_marnet.py route`-call, geen via-punten, geen nieuw wegprofiel, geen herbake van wegscan of aanlopen, geen extracts).

| # | modaliteit | km (bake) | km (brief) | punten | naad naar vorige | stippel |
|---|---|---|---|---|---|---|
| b1 | truck | 1,9 | hemelsbreed 1,2, geen wegkm | 73 | — | nee |
| b2 | zee (haven-aanloop Claver) | 65,9 | 60,5 hemelsbreed / 65,9 gebakken | 52 | 1,21 km | ja |
| b3 | zee (MARNET 8314 → 5746) | 3.043,8 | 3.043,8 (MARNET) | 316 | 0,00 km | nee |
| b4 | zee (haven-aanloop Niihama) | 25,7 | 23,2 hemelsbreed / 25,7 gebakken | 43 | 0,00 km | ja |

**Markers (alle vier ≤ 0,001 km van hun lijn):** Taganito Mining Corp. 9.5464,125.8193 · THPAL-plant 9.5395,125.8106 · Claver-laadsteiger 9.5490,125.8160 · Niihama Nickel Refinery 33.9669,133.2658 (stoppunt).

**Toelichting.**
- **Alle vier de benen zijn byte-identiek aan `nikkel-taganito-niihama` b1–b4** (punten én km gelijk, per been in het json vergeleken): b1/b2/b4 via `--been-geojson`/`--stippel-geojson` op dezelfde `nikkel-taganito-niihama-*.geojson` in `build-cache/ais/graaf/`, b3 via dezelfde MARNET-zeeknoop-coördinaten. De namen noemen de kopie letterlijk. Hachinohe/PAMCO (nikkel b5/b6) is niet mee: saproliet draagt geen kobalt.
- **Stippel b2 (haven-aanloop Claver):** de steiger ligt 60,5 km van MARNET-zeeknoop 8314; MARNET reikt niet tot de kade. **Stippel b4 (haven-aanloop Niihama):** kade 23,2 km van zeeknoop 5746 (> 5 km), de snap valt net binnen de 25 km; zonder aanloop zou b3 kilometers vóór de raffinaderij stoppen. Beide zijn de kortste waterpaden uit `maak_havenaanloop.py` (nikkelbake), zonder landkruising.
- **Aannemelijk (b3/b4, in de beennaam):** Niihama is Japans enige Co-raffinaderij (SMM); een deel van het MS gaat mogelijk naar Harima. Doorgetrokken, want gemeten; de onzekerheid zit in de naam en in §7.
- **Naad b1 → b2 = 1,21 km** = procesgat THPAL-plant → THPAL-kade binnen de verwerkingsknoop (onder de 5 km-norm, bewust geen eigen been, zie §1). Alle andere naden 0,00 km.
- **Toets:** geen naad > 5 km · `toets_knikken.py`: 0 omkeringen, 0 terugloop (8 knikken ≥ 60°, alle uit de nikkelgeometrie: 4 spikes op de mijnweg-OSM-zigzag van 7–18 m straal, 4 krappe zeebochten met R > 4,6 km in Bungo-kanaal/Seto/Filipijnenzee) · b2/b4 zijn geen rechte lijn (omwegfactor 1,09 resp. 1,11 tegen hemelsbreed) · json.load, `versie 2`, `punt_formaat lonlat`, modaliteiten ∈ {truck, zee}, elk been ≥ 2 punten, 10,3 KB.
- **b1-km:** geen gepubliceerde wegkilometer (privé-mijnweg); de ±15%-toets is hier een indicatie, geen norm. 1,9 km tegen hemelsbreed 1,2 km (factor 1,6) is dezelfde geometrie als de nikkelbake.

**Lessen.** (1) Een grondstoflaag-kopie van een bestaande stroom kost één functie en één minuut bakken: geen scans, geen aanlopen, en het json is byte-identiek per been te bewijzen. (2) De semafoor-snippet uit de golf-opdracht gebruikt `rm -rf "$d"` met een variabele en wordt door de Claude Code-veiligheidscheck geweigerd; een slot nemen met `mkdir` en loslaten met `rmdir` op een letterlijk pad werkt wel. (3) `toets_rechte_benen.py` leest het register, niet het bestand: een nog niet geregistreerde stroom komt er niet in voor, de omwegfactoren hierboven zijn uit het json zelf berekend.

**Centraal nog te doen (niet door de bak-agent):** registratie in `stromen-register.json` (sleutel `co-tn`) en bundel · kobalt-sitelaag: THPAL-site toevoegen (capaciteit ~2,6–2,8 kt Co) en `w-niihama` van 33.9496,133.2316 naar 33.9669,133.2658 trekken.
