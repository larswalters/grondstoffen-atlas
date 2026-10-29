# Routebrief (licht) · Zeldzame aardmetalen · Silmet Sillamäe → Muuga → Rotterdam → Port Newark (VS)

**stroom-id:** `ree-sillamae-newark` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · Silmet Sillamäe → Muuga → Rotterdam → Port Newark (REE-oxiden en katalysatorpoeder, aannemelijk: één bron)
**Keten in één zin:** REE-oxide en katalysatorpoeder (Supported Catalysts, o.a. neodymiumoxide) van NPM Silmet in Sillamäe gaat per **truck** (weg 1/E20 en weg 94, ~178 km) naar de containerterminal van Muuga bij Tallinn, per feeder over Finse Golf, Oostzee en Noordzee naar de Maasvlakte (Rotterdam) en per containerschip over de Atlantische Oceaan naar Port Newark (NJ), waar Neo Chemicals and Oxides LLC de consignee is. Stoppunt aan de kade.
**Welke as van het verhaal:** Europese REE-scheiding die de VS bevoorraadt. Jaarvolume ca. **0,45 kt REO-equivalent per jaar** Estland → VS (eigen omrekening: 5% van circa 9 kt invoer compounds en metalen, gemiddelde 2021-24, USGS MCS 2026 [2]); Silmet scheidt 2 kt per jaar licht REE [5]. Indicatie, geen Newark-specifiek cijfer; deel van de lading is katalysator of waterbehandeling [1].
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** Muuga-anker 59.4915, 24.9675 (containerterminal, niet het Wikipedia-punt op de bulkkade 0,55 km westelijker [3]); Rotterdam-anker is de containerkade Maasvlakte 51.9583, 4.0450 in plaats van RHB Waalhaven (MARNET zou 30 km de rivier in en uit varen); Muuga-aanloop als rechte stippel 37,5 km (maak_havenaanloop liep vast op 300 s). Het ontwerp zei 36,5 km: eigen meting 37,5 km tot knoop 1970. Eindpunt blijft Newark; sample-B/L eindigt in Savannah, dus aannemelijk.

## 1 · Ketenkaart
```
NPM Silmet `ree-silmet-scheiding` (Sillamäe)
  ──(b1 truck · weg 1/E20 + weg 94 · ~178 km, aannemelijk)──► Muuga-containerterminal `ree-muuga-ct` (HHLA TK, Tallinn)
  ╌╌(b2 zee-stippel · haven-aanloop Muuga · 37,5 km, schematisch)╌╌► zeeknoop 1970 (59.8, 24.7, Finse Golf)
  ──(b3 zee · feeder Finse Golf–Oostzee–Noordzee · 2.065,6 km)──► Maasvlakte-containerkade `ree-maasvlakte-ct` (Rotterdam)
  ──(b4 zee · Kanaal–Atlantische Oceaan–The Narrows · 6.131,6 km, aannemelijk)──► Port Newark Container Terminal `ree-newark-ct` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `ree-silmet-scheiding` → `ree-muuga-ct` | weg 1 (E20, Tallinn–Narva mnt) → Peterburi tee → Muuga sadama tee (weg 94) | hemelsbreed 157 km, geen wegkm; OSRM 178,4 km [10]; weg 1 zelf is 212 km Tallinn–Narva [4] | maak_stroombeen_weg (extract estland) | nee — *aannemelijk: één bron* |
| b2 | C | zee | `ree-muuga-ct` → zeeknoop 1970 | haven-aanloop Muuga, over water tussen Viimsi-punt en Prangli | 37,5 (eigen meting, rechte lijn) | rechte stippel (terugval) | **ja — hier reikt het net niet** |
| b3 | C | zee | zeeknoop 1970 → `ree-maasvlakte-ct` | Finse Golf, Oostzee, Deense wateren, Noordzee (feeder) | 2.065,6 (eigen MARNET-meting [12]; snap Maasvlakte 3,67 km, geen aanloop) | MARNET | nee |
| b4 | C | zee | `ree-maasvlakte-ct` → `ree-newark-ct` | Engels Kanaal, Noord-Atlantische Oceaan, The Narrows | 6.131,6 (eigen MARNET-meting [12]; snap Newark 3,58 km, geen aanloop) | MARNET | nee — *aannemelijk: Newark volgens consignee* |

Het ontwerp liet Rotterdam als lading-haven gelden (sample-B/L Tallinn via Rotterdam [1]); b3 en b4 delen geen geojson met een bestaande stroom (geen letterlijke kopie nodig).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-silmet-scheiding` | scheidingsfabriek (laadplek) | NPM Silmet OÜ, Sillamäe | 59.4031, 27.7421 | [6][9], **hergebruikt letterlijk** uit `ree-sillamae-narva.md` §3 | bron-gelegd (z15 gezien in die brief: aaneengesloten industrieterrein met tankenpark en spooraansluiting) |
| `ree-muuga-ct` | overslag land→zee (containerterminal) | Muuga-containerterminal (HHLA TK Estonia), Muuga sadam | 59.4915, 24.9675 | [3][9], haalbaarheidstoets | bron-gelegd (z16 gezien: portaalkranen en containerstapels op de kade met een schip aan de kade; het Wikipedia-punt 59.4917, 24.9583 ligt op de bulkkade 0,55 km westelijker) |
| `ree-maasvlakte-ct` | overslag feeder→oceaan (containerkade) | Maasvlakte-containerterminal, Beerkanaal-kade (ECT Delta-complex, exacte terminal niet vastgesteld) | 51.9583, 4.0450 | [9][11], haalbaarheidstoets | bron-gelegd (z15 gezien: containerstapels en kranen aan de noordkade; OSM "Container Exchange Route" op 0,6 km) |
| `ree-newark-ct` | losplek (containerterminal) | Port Newark Container Terminal, Newark NJ | 40.6873, -74.1499 | [8][9] | bron-gelegd (z15 gezien: containerterminal met stapels en kranen op de kadevinger, spoor en luchthaven westelijk) |

Zeeknoop 1970 (59.8000, 24.7000) is een MARNET-knoop, geen anker. Eindsite van Neo in de VS is onbekend (consignee-notify-adres Greenwood Village, CO [7]), dus geen last-mile.

## 4 · Via-punten (b1; corridorkeuze: hoofdweg 1 i.p.v. Sillamäe-centrum en binnenwegen, daarna Tallinn-ring naar Muuga)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | oprit Sillamäe → weg 1 (Tallinn–Narva 1) | 59.3908, 27.7432 | pint de route op de doorgaande weg 1 i.p.v. door het centrum van Sillamäe (OSRM stap "merge") |
| b1 | 2 | weg 1, ca. 45 km westelijk van Sillamäe (westelijk van Kohtla-Järve/Jõhvi) | 59.4064, 27.0591 | houdt de route op weg 1 in plaats van de binnenwegen langs Kohtla-Järve en Jõhvi (OSRM nearest 0 m) |
| b1 | 3 | weg 1, noordwestelijk van Rakvere | 59.4267, 26.2455 | pint de doorgaande weg langs Rakvere i.p.v. de stadsdoorsnede (OSRM nearest 1 m) |
| b1 | 4 | weg 1, noordkust-corridor (Lahemaa-streek) | 59.4606, 25.7924 | houdt de route op weg 1 i.p.v. kustwegen (OSRM nearest 0 m) |
| b1 | 5 | weg 1 ten oosten van Tallinn (Kuusalu-streek) | 59.4440, 25.3533 | pint de aanloop naar de Tallinn-ring (OSRM nearest 5 m) |
| b1 | 6 | begin Muuga sadama tee (weg 94) | 59.4526, 24.9828 | pint de afslag naar Muuga i.p.v. door Maardu-stad (OSRM nearest 1 m) |
Totaal 178,4 km met deze via-punten (OSRM [10]). Alle punten liggen buiten stadscentra; refs voor het profiel: `["1", "E20", "94"]`. Profiel-coördinaten zijn (lon, lat).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Silmet-scheiding, Sillamäe | Neo Performance Materials (NPM Silmet AS) | REE-concentraat → REE-oxiden en katalysatorpoeder (Supported Catalysts) | 2 kt/j licht REE; Dy/Tb-lijn in aanbouw | [5][6] |
| Muuga-containerterminal | HHLA TK Estonia (Port of Tallinn) | truck → feeder | 267.752 TEU in 2022 voor Muuga | [3] |
| Maasvlakte-containerterminal | Port of Rotterdam | feeder → oceaanschip | niet nagezocht | [11] |
| Port Newark Container Terminal | PNCT (Port Authority NY/NJ) | oceaanschip → kade | 180 acres, uitbreiding naar 287 acres | [8] |

## 6 · Stoppunt
De brief stopt aan de kade van Port Newark: de eindsite van Neo Chemicals and Oxides LLC in de VS is niet gedocumenteerd (alleen een notify-adres in Colorado [7]), dus fase D/E vervalt.

## 7 · Open punten
- **Newark is volgens de consignee-samenvatting, niet volgens het enige B/L.** Het sample-B/L Tallinn via Rotterdam eindigt in Savannah (product Supported Catalysts 5052); records noemen ook Savannah, Norfolk, Houston en Charleston [1]. Daarom "aannemelijk" in de beennaam van b4.
- **Product is deels geen magneetoxide.** Het sample-product is katalysator (HS 3815.19.90), een deel waterbehandeling; REE-oxide voor magneten is een aandeel dat geen bron kwantificeert [1].
- **Volume 0,45 kt/j is een eigen omrekening**, geen Silmet- of Neo-opgave; gemiddelde invoer 2021-24 en 5% aandeel Estland gelden voor compounds en metalen in totaal [2].
- **Muuga-aanloop is schematisch**: 37,5 km rechte stippel naar knoop 1970 (ontwerp zei 36,5 km); de lijn kruist op de satelliet (z10) geen land, tussen Viimsi-punt en Prangli [11].
- **Truck b1 heeft alleen een hemelsbreed getal en een OSRM-meting**, geen operator-km; de ±15%-toets is een indicatie.
- **Maasvlakte-terminalnaam niet vastgesteld** (ECT Delta of buurterminal); het anker staat op de containerkade, niet op een benoemde operator.
- **Ontwerp-km 36,5 en 2.095,5/6.161,5 komen uit de ontwerpfase (RHB-anker)**; de bindende ankers geven 37,5, 2.065,6 en 6.131,6.

## 8 · Bronnen
[1] ImportGenius, NPM Silmet OÜ — 350 zendingen, consignee Neo Chemicals and Oxides 217 containers, havens Newark/Savannah/Norfolk/Houston/Charleston, sample-B/L Tallinn–Rotterdam–Savannah. https://www.importgenius.com/suppliers/npm-silmet-ou
[2] USGS, Mineral Commodity Summaries 2026, Rare Earths — invoerbronnen 2021-24: China 71%, Maleisië 13%, Japan 5%, Estland 5%. https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-rare-earths.pdf
[3] Wikipedia, "Muuga Harbour" — 59°29′30″N 24°57′30″E, HHLA-terminal sinds 2018, 267.752 TEU in 2022. https://en.wikipedia.org/wiki/Muuga_Harbour
[4] Wikipedia, "Estonian national road 1" — Tallinn–Narva 212 km, onderdeel van E20, via Rakvere, Kohtla-Järve, Jõhvi, Sillamäe. https://en.wikipedia.org/wiki/Estonian_national_road_1
[5] Fastmarkets, "Neo adds heavy rare earth line, opens EV motor magnet plant" — Silmet 2.000 tpy licht-REE-scheiding. https://www.fastmarkets.com/insights/neo-adds-heavy-rare-earth-line-opens-ev-motor-magnet-plant/
[6] Wikipedia, "Silmet" — NPM Silmet AS, Sillamäe, dochter van Neo Performance Materials. https://en.wikipedia.org/wiki/Silmet
[7] Panjiva, Neo Chemicals And Oxides LLC, Greenwood Village CO 80111 (notify-adres, secundaire bron via zoekresultaat). https://es.panjiva.com/Neo-Chemicals-And-Oxides-Llc-Greenwood-Village-Co-80111/41509361
[8] Wikipedia, "Port Newark–Elizabeth Marine Terminal" — PNCT 180 acres, lease tot 2050, uitbreiding naar 287 acres. https://en.wikipedia.org/wiki/Port_Newark%E2%80%93Elizabeth_Marine_Terminal
[9] OpenStreetMap (ODbL) via Nominatim — Muuga sadam, Container Exchange Route (Maasvlakte), Starboard Street (Port Newark). https://nominatim.openstreetmap.org
[10] OSRM (router.project-osrm.org) — Silmet-anker → Muuga-anker 178,4 km; met zes via-punten 178,4 km, alle via-punten op weg 1 binnen 5 m.
[11] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-ree-sillamae-newark-{muuga-ct,maasvlakte,newarkct,muuga-aanloop10}.png`.
[12] Eigen MARNET-dry-run (`hecht_marnet.py route`, scratch): b3 2.065,6 km, b4 6.131,6 km, snaps 3,67 en 3,58 km, stippel 37,452 km.
[13] Routebrief `ree-sillamae-narva` — Silmet-anker 59.4031, 27.7421 (bron-gelegd z15). `v2/design/routebrieven/ree-sillamae-narva.md`

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`bash v2/tools/bak_stromen.sh ree-sillamae-newark` -> `v2/data/stroomroute-ree-sillamae-newark.json` (47,7 KB, contract versie 2, lonlat). **4 benen · 8.411,0 km · 2.464 punten · 4 markers.** Functie `bak_ree_sillamae_newark` in `bak_stromen.sh`, profiel `ree-sillamae-newark-silmet-muuga` in `maak_stroombeen_weg.py`.

| # | modaliteit | km (gebakken) | km (brief) | naad | stippel | geometrie |
|---|---|---|---|---|---|---|
| b1 | truck | 176,3 | OSRM 178,4 (geen wegkm) -> -1,0% (indicatie) | - | nee | wegscan estland, 6 via-punten + beide ankers, refs 1/E20/94, eindToegangPrivaat |
| b2 | zee | 37,5 | 37,5 | 0,0 | **ja** (haven-aanloop Muuga) | rechte stippel 59.4915,24.9675 -> 59.8,24.7 |
| b3 | zee | 2.065,6 | 2.065,6 | 0,0 | nee | MARNET knoop 1970 -> Maasvlakte (snap 3,67 km) |
| b4 | zee | 6.131,6 | 6.131,6 | 0,0 | nee | MARNET Maasvlakte -> Port Newark (snap 3,58 km) |

**Recept.** b1: wegscan (pure-Python pbf-lezer, extract estland, 31 s): 7 segmenten, alle via-snaps <= 0,07 km, 2 keerlussen gesnoeid (176,2 km), first mile 1,47 km en last mile 1,81 km over kleine klassen (service/unclassified). Geen via-punt verplaatst. Lengtetoets 176,2 tegen ~178 = -1,0% [OK] - een indicatie, de brief heeft geen operator-wegkm. b2: stippel, geen tweede aanloop-poging (de brief zegt dat maak_havenaanloop op 300 s vastliep). b3/b4: `--been zee` kade -> kade.

**Toelichting stippel.** b2 = "hier reikt het net niet": de Muuga-kade ligt 37,5 km van MARNET-zeeknoop 1970 (59.8, 24.7) in de Finse Golf; de rechte lijn kruist volgens de brief op satelliet z10 geen land. Alle andere benen zijn doorgetrokken; "aannemelijk: een bron" staat in de beennamen van b1 en b4, niet in de lijnstijl.

**Toets (handleiding §5).** Naden 0,0 / 0,0 / 0,0 km (geen naad > 5 km). Markers: Silmet 0,0 km en Muuga 0,0 km van de lijn; **Maasvlakte 3,4 km en Port Newark 2,0 km van de lijn** - de zeebenen eindigen op de MARNET-zeeknoop (snap 3,67 en 3,58 km, onder de 5 km-grens voor een haven-aanloop), niet op de kade. Bevinding: anker != routeerpunt, bewust niet dichtgetrokken (de brief besluit "geen aanloop"). `toets_knikken.py`: 0 omkeringen en 0 terugloop; truck heeft 11 knikken, de scherpste spikes van 10-70 m straal bij de ankers (Muuga-terrein rond 59.4892,24.9701 en Silmet 59.4025,27.7426; first/last mile op service-wegen), zee b4 heeft spikes bij 50.3375,-0.7643 (MARNET-kustknopen) en krappe bochten bij 52.0,3.9 en de Narrows. `toets_rechte_benen.py`: alleen b2 is recht (omwegfactor 1,001), en dat is de stippel met reden. json.load: versie 2, lonlat, modaliteiten {zee, truck}, elk been >= 2 punten.

**Afwijkingen van het ontwerp.** Geen: het eindpunt is Port Newark zoals het id belooft (aannemelijk, sample-B/L eindigt in Savannah). Het Rotterdam-anker is de Maasvlakte-containerkade (niet RHB Waalhaven).

**Lessen.** (1) Alle vier weg-slots waren bezet; een slot werd vrij na ~10 min wachten. (2) Estland is een kleine extract (122 MB, 31 s). (3) Twee zee-snaps van 3,6-3,7 km laten de kade-markers op > 0,5 km van de lijn staan; wie dat wil sluiten moet een haven-aanloop toevoegen, ook onder de 5 km-regel van de handleiding.
