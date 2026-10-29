# Routebrief (licht) · Uranium — Novosibirsk → Tolmachevo → Dhaka → Rooppur (Rusland/Bangladesh, peiljaar 2026)

**stroom-id:** `uranium-novosibirsk-rooppur` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) ·
**status:** gebakken
**Keten in één zin:** VVER-1200-splijtstof (eerste kernlading Rooppur-eenheid 2) van TVEL NZHK in Novosibirsk gaat per truck naar
het vrachtplatform van Tolmachevo (OVB, aannemelijk), per vrachtvlucht (grootcirkel) naar de vrachtterminal van Dhaka (DAC) en per
legerconvooi over de weg (Jamuna-brug, Bonpara, Dashuria) naar de kerncentrale Rooppur — **stoppunt**: de reactor.
**Welke as van het verhaal:** *Rosatom-brandstofexport per lucht: Siberië naar Bangladesh.* Volume **≈ 79 t U in 2026** (eigen schatting:
163 assemblages per kern [1][5], ~0,48 t U per assemblage uit 312 staven van ~3,75 m — geen gepubliceerd cijfer); 7 vluchten van ~41 t brutolading
(12 TPK-containers) [6]. Eenheid t U/j, peiljaar 2026.

## 1 · Ketenkaart
```
TVEL Novosibirsk Chemical Concentrates Plant (NZHK) `u-nzhk`
  ──(b1 truck · Ob-oversteek bij ~55.066, 82.93 → stad → Tolmachevo-weg · hemelsbreed 23,8 km, geen wegkm · aannemelijk: geen bron noemt de truck)──►
Tolmachevo (OVB) vrachtplatform `u-ovb-vrachtplatform`   [wegeinde landside 55.0042, 82.6428 + stippel 0,26 km airside]
  ──(b2 lucht · vlucht OVB → DAC, grootcirkel 3.523 km · aannemelijk: bronnen noemen geen luchthavens)──►
Dhaka Hazrat Shahjalal (DAC) vrachtterminal `u-dac-vrachtterminal`
  ──(b3 truck · N4 Gazipur–Tangail → Jamuna-brug → Hatikumrul → N6 Bonpara → Dashuria · >200 km politie, hemelsbreed 140 km)──►
Rooppur kerncentrale (Ishwardi) `u-rooppur` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | NZHK → OVB landside | Ob-oversteek ~55.066, 82.93, daarna door Novosibirsk (router-keuze) | hemelsbreed 23,8, geen wegkm; gemeten 30,5 | maak_stroombeen_weg (rusland-siberie) | nee — *aannemelijk: modaliteit in geen bron* |
| b1s | D | truck | OVB landside → platform | luchthaventerrein | 0,26 (eigen meting) | rechte stippel | **ja — airside, geen wegpad (ZRH-patroon)** |
| b2 | D | lucht | OVB → DAC | vrachtvlucht (WNN: "cargo plane") [1] | grootcirkel 3.523,0 (berekend) | maak_luchtbeen | nee — doorgetrokken, *aannemelijk: luchthavens niet genoemd* |
| b3 | D | truck | DAC vrachtterminal → Rooppur | Dhaka–Gazipur–Tangail (N4) → Bangabandhu-brug → Hatikumrul → N6 Bonpara → Dashuria [3][6] | ">200 km" (politie, via [6]); gemeten 212,1 (+6%); hemelsbreed 139,8 | maak_stroombeen_weg (bangladesh) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-nzhk` | fabriek (kop) | Novosibirsk Chemical Concentrates Plant (TVEL/Rosatom) | 55.0909, 82.9847 | [1][7] OSM-way 51916722 (bbox 55.0846–55.0987, 82.9759–82.9952) | bron-gelegd (z15 gezien: groot industrieterrein aan de oostrand van de stad met een grote fabriekshal onder het kruis en een spoorbundel langs de oostkant; welke hal splijtstof maakt niet te zien). Sitelaag `w-tvel-novosibirsk` (54.9667, 82.8833) ligt ~14 km ZW van de fabriek — fout, niet gebruikt |
| `u-ovb-vrachtplatform` | overslag weg → lucht | Tolmachevo (OVB), betonnen apron met pakhuis zuid van de baan | 55.0065, 82.6420 | [8] wiki-luchthaven 55.0125, 82.6506; platform eigen keuze | **aannemelijk** (z15 gezien: apron met vrachtachtige toestellen en een groot pakhuis (~170 × 60 m) direct ten zuiden ervan; geen bron noemt de OVB-vrachtterminal bij naam). Routeerpunt landside voor b1: 55.0042, 82.6428 (dienstweg, snap 0,05 km) |
| `u-dac-vrachtterminal` | overslag lucht → weg | Hazrat Shahjalal Airport Cargo Terminal (বিমানবন্দর কার্গো টার্মিনাল) | 23.8514, 90.4027 | [9][10] OSM-terminal 23.85135, 90.40272 | bron-gelegd (z15 gezien: vrachtplatform met geparkeerde toestellen langs de oostrand van de baan, direct ten westen van de Airport Road; OSM-terminalparking 23.8518, 90.4037 ligt 0,1 km oostelijker) |
| `u-rooppur` | reactor (eindpunt) | Rooppur NPP, Ishwardi (Pabna) | 24.0667, 89.0472 | [2] wiki-coördinaat | bron-gelegd (z15 gezien: omheind centralecomplex met vier koeltorens en reactorgebouwen aan de Padma, bruggen noordwestelijk; kruis midden op het complex) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; op de doorgaande weg)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | geen bron noemt een corridor; de router koos de Ob-oversteek bij ~55.066, 82.93 (brug niet bij naam geverifieerd) |
| b3 | 1 | N4 Gazipur Chowrasta | 23.9897, 90.3820 | begin van de N4 naar Tangail (snap 0,00 km); houdt de lijn uit het stadscentrum van Dhaka |
| b3 | 2 | N4 Elenga | 24.3352, 89.9252 | knoop vóór de Bangabandhu-brug [3][6] (snap 0,04 km) |
| b3 | 3 | N5/N6 Hatikumrul | 24.4182, 89.5518 | westeinde van de brug, afslag naar de N6 (snap 0,17 km) |
| b3 | 4 | N6 Bonpara (Natore) | 24.3002, 89.0757 | bronnen noemen Bonpara en Dashuria [6]; sluit de route via Sirajganj–Pabna uit (snap 0,39 km) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| NZHK (Novosibirsk) | TVEL / Rosatom | uraniumoxide → VVER-assemblages | ≈ 1.200 t HM/j (sitelaag-indicatie, alle klanten) | [1][sitelaag] |
| Rooppur (2 × VVER-1200) | BAEC / Rosatom | splijtstof → 2,4 GWe | 163 assemblages per kern; EPC-contract omvat eerste lading + twee herladingen [2] | [2][5] |

## 6 · Stoppunt
De brief stopt bij de reactor: Rooppur is de enige afnemer en geen bron noemt een volgende locatie (E vervalt). Fase D is hier de hele
keten: WNN noemt NZHK als fabrikant en "cargo plane and then by road" [1]; luchthavens, vertrekplaats en truck zijn aanvullingen.

## 7 · Open punten
- **Vertrekluchthaven niet bevestigd:** WNN noemt geen luchthavens [1]; OVB is aannemelijk (fabriek in Novosibirsk; Wikipedia noemt Tolmachevo als tankstop voor vrachtvluchten [8]). Een OVB-vrachtterminal is niet bij naam te vinden (OSM, Wikipedia, tolmachevo.ru leeg).
- **Tussenlanding Delhi niet getekend:** een zoekuittreksel van Dhaka Tribune noemt een stop in Delhi [6] (zelf niet gelezen, 403); bdnews24 noemt de luchtroute via Kazachstan, Turkmenistan, Afghanistan, Pakistan en India en een vlucht die door een Pakistaanse overvliegweigering werd gestopt [5]. De grootcirkel claimt alleen "van terminal naar terminal"; een technische tussenstop is geen overslag.
- **Eén vlucht is getekend, 7 vluchten bestaan** voor eenheid 2 (plus 2 voor de herlading van eenheid 1: 48 assemblages) [4][5]; geen vluchtenlijst met vertrekplaats gevonden.
- **Het WNN-getal 163 geldt voor één kern**; het aantal assemblages per lading en het gewicht per assemblage zijn eigen schatting.
- **b1-corridor is router-keuze** (door de stad, geen ringweg); geen bron noemt de rit NZHK → OVB.
- **b3 volgt de bronnen** (Jamuna-brug [3], Bonpara/Dashuria [6]); de Dhaka Tribune-tijden spreken elkaar tegen (vertrek 04:56 of 07:00), de route niet.
- **Sitelaagfout gemeld:** `w-tvel-novosibirsk` ligt ~14 km ZW van de fabriek (54.9667, 82.8833 tegen 55.0909, 82.9847); niet aangepast.

## 8 · Bronnen
[1] World Nuclear News, 2026-10-28 — "Nuclear fuel delivered for Bangladesh's second unit" (NZHK/TVEL, cargo plane then road, Rooppur ~160 km van Dhaka). https://world-nuclear-news.org/articles/nuclear-fuel-delivered-for-bangladeshs-second-unit
[2] Wikipedia, "Rooppur Nuclear Power Plant" — 24.0667 N 89.0472 E; 2 × VVER-1200; EPC-contract incl. brandstof voor eerste lading en twee herladingen. https://en.wikipedia.org/wiki/Rooppur_Nuclear_Power_Plant
[3] The Daily Star, 2026-10 — "Uranium on its way to Rooppur amid tight security": convooi verlaat DAC 07:00, Jamuna-brug 09:10, Rooppur 12:30; negen vluchten. https://www.thedailystar.net/news/power-and-energy/news/uranium-its-way-rooppur-amid-tight-security-4289156
[4] Bangladesh Post, 2026-10 — "Uranium convoy heads to Rooppur under tight security": 48 assemblages eenheid 1, 163 eenheid 2, negen vluchten. https://bangladeshpost.net/posts/uranium-convoy-heads-to-rooppur-under-tight-security-174004
[5] bdnews24, 2026-09 — "Uranium shipments for Rooppur second unit set to arrive from October": schema, luchtroute via Kazachstan–India, Pakistaanse overvliegweigering. https://bdnews24.com/bangladesh/9z077vlv5g
[6] Dhaka Tribune, 2026-10 — "Second/Third uranium shipment arrives at Rooppur under tight security" (alleen zoekuittreksel; 403): landing DAC 26-10 08:14, 41 t in 12 TPK, stop Delhi, Bangabandhu-brug, Bonpara, Dashuria, ">200 km groene corridor". https://www.dhakatribune.com/bangladesh/power-energy/422590/second-uranium-shipment-arrives-at-rooppur-under
[7] OpenStreetMap, way 51916722 "Новосибирский завод химконцентратов" (industrial/works, Rosatom). https://www.openstreetmap.org/way/51916722
[8] Wikipedia, "Tolmachevo Airport" — 55.0125 N 82.6506 E; aantrekkelijk als tankstop voor vrachtvluchten. https://en.wikipedia.org/wiki/Tolmachevo_Airport
[9] Wikipedia, "Hazrat Shahjalal International Airport" — cargo terminal 200.000 t/j. https://en.wikipedia.org/wiki/Hazrat_Shahjalal_International_Airport
[10] OpenStreetMap via Nominatim — "বিমানবন্দর কার্গো টার্মিনাল" 23.85135, 90.40272; parking 23.85180, 90.40375; Bonpara 24.3002/89.0757; Hatikumrul 24.4182/89.5518; Elenga 24.3352/89.9252; Gazipur Chowrasta 23.9897/90.3820. https://nominatim.openstreetmap.org
[11] VVER-1200-kerngegevens (zoekuittreksel, o.a. Springer 10.1007/s44245-025-00175-7): 163 assemblages, 312 splijtstofstaven, kernhoogte 3,75 m. https://link.springer.com/article/10.1007/s44245-025-00175-7
[sitelaag] `v2/design/uranium-sitelaag.json` `w-tvel-novosibirsk` (capaciteit ~1.200 t HM/j; coördinaat fout).
Eigen scans: `wegscan_puur.py` (rusland-siberie, bangladesh) 2026-10-29; `maak_luchtbeen.py` OVB → DAC 3.523,0 km. Satellietblik: `v2/build-cache/satcheck/sat-uranium-novosibirsk-rooppur-nzhk.png`, `-ovb.png`, `-dac.png`, `-rooppur.png` (Esri z15, 2026-10-29).

## 9 · Gebakken

**Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)** · `bash v2/tools/bak_stromen.sh uranium-novosibirsk-rooppur` → `v2/data/stroomroute-uranium-novosibirsk-rooppur.json` (55,7 KB, contract versie 2, 4 benen, 4 markers, totaal 3.765,9 km, alle naden 0,000 km).

| # | modaliteit | km gemeten | km brief | naad | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 30,5 | hemelsbreed 23,8, geen wegkm | 0 | doorgetrokken; router-keuze door de stad; ±15% geldt niet als norm (geen echte wegkm) |
| b1s | truck (stippel) | 0,26 | 0,26 | 0 | airside last mile OVB landside → vrachtplatform (ZRH-patroon) |
| b2 | lucht | 3.523,0 | 3.523,0 grootcirkel | 0 | doorgetrokken, `maak_luchtbeen.py`, 142 punten |
| b3 | truck | 212,1 | >200 (politie, via Dhaka Tribune-uittreksel) | 0 | +6% op ondergrens, binnen norm |

**Recept:** profielen `uranium-novosibirsk-rooppur-nzhk-ovb` (rusland-siberie, geen via-punten) en `uranium-novosibirsk-rooppur-dac-rooppur` (bangladesh, 4 via-punten) in `maak_stroombeen_weg.py`, gescand met `wegscan_puur.py`; luchtbeen met `maak_luchtbeen.py`; functie `bak_uranium_novosibirsk_rooppur` in `bak_stromen.sh` (LF, 0 CRLF). Geen zee, geen haven-aanloop, geen spoor, geen letterlijke kopie.

**Toelichting:** de enige stippel is de 0,26 km airside last mile op OVB (geen wegpad op het vrachtplatform; "hier reikt het net niet"). De vlucht is doorgetrokken: "grootcirkel" en "aannemelijk: luchthavens niet genoemd" staan in de beennaam. b1 en OVB-vrachtplatform zijn aannemelijk (alleen in beennaam/markernaam). Delhi-tussenstop niet getekend.

**Toets:** markers 0,0 km van hun lijn (alle vier); `toets_knikken.py`: 40 knikken >= 60 gr, 0 omkeringen, 0 terugloop (spikes liggen in de aansluitingen bij Rooppur, DAC en de Jamuna-brug-afslagen, 6-61 m); `json.load` ok, modaliteiten {truck, lucht}, elk been >= 2 punten.

**Lessen / bevindingen:** (1) b3 eindigt pas op het anker na een last mile van 0,82 km over service/unclassified; (2) sitelaagpunt `w-tvel-novosibirsk` ligt ~14 km ZW van de fabriek (niet aangepast, centraal); (3) per-kern volume 79 t U is eigen schatting; (4) het id noemt Rooppur en de lijn eindigt daar: id en eindpunt kloppen.
