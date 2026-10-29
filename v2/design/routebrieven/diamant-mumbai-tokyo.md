# Routebrief (licht) · diamant — Mumbai → Narita → Okachimachi (Tokio)

**stroom-id:** `diamant-mumbai-tokyo` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** gepolijste diamant van de Bharat Diamond Bourse (BKC, Mumbai) per truck naar het Sahar/CSMIA-vrachtcomplex (BOM), per vrachtvlucht (grootcirkel, aannemelijk: één bron) naar de Narita Cargo Area (NRT), en per truck over Higashi-Kanto/Keiyo/Shuto naar Jewelry Town Okachimachi (Taito, Tokio), de juweliers-groothandelwijk rond Okachimachi Station.
**Welke as van het verhaal:** *India → Japan: gepolijst naar de enige genoemde eindmarkt zonder lijn.* India is de grootste leverancier van Japans gepolijst: 131.514 ct = 45,6% van het volume en 74% van de waarde in apr 2007 [2]; 27,8 van 53,6 mln USD (~52% van de waarde) in feb 2013 [1]. Japan importeert totaal 149.219 ct (feb 2013) tot 177.752 ct (apr 2007) per maand, dus ≈1,8–2,1 Mct/j (maand × 12, indicatie). India alleen: apr 2007 × 12 ≈ 1,6 Mct/j; v1 gebruikt 2 Mct/j (natte vinger). Eenheid Mct/j; waarde per karaat verschilt (India 241 USD/ct in apr 2007, Japan-gemiddelde 359 USD/ct in feb 2013), niet in het gewicht.

## 1 · Ketenkaart
```
Bharat Diamond Bourse (BKC) `dia-bdb` ──(b1 truck · BKC-connector/Airport Road · hemelsbreed 3,9 km, geen wegkm; LETTERLIJKE KOPIE b1 diamant-mumbai-newyork)──►
Sahar/CSMIA Air Cargo Complex (BOM) `dia-bom-cargo` ──(b2 lucht · vlucht BOM → NRT, grootcirkel · 6.785 km berekend, aannemelijk: één bron)──►
Narita Cargo Area (NRT) `dia-nrt-cargo` ──(b3 truck · Narita → Higashi-Kanto/Keiyo → Shuto 7 → Shuto 1 Ueno-lijn · hemelsbreed 55 km, geen wegkm)──►
Jewelry Town Okachimachi (Taito, Tokio) `dia-tokyo-okachimachi` ── stoppunt
```
Ankers `dia-bdb`, `dia-bom-cargo` (uit `diamant-mirny-mumbai.md` / `diamant-mumbai-newyork.md`) en `dia-nrt-cargo` (= `pgm-nrt-vracht` uit `pgm-rustenburg-tokio.md`) zijn hergebruikt, niet opnieuw gelegd.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Bharat Diamond Bourse → Sahar/CSMIA Air Cargo Complex | BKC-connector / Airport Road, binnen Mumbai; **letterlijke kopie b1 van diamant-mumbai-newyork** | hemelsbreed 3,9 km, geen wegkm (gebakken kopie 8,4 km) | kopie bestaand geojson | nee |
| b2 | B | lucht | CSMIA Air Cargo Complex (BOM) → Narita Cargo Area (NRT) | vrachtvlucht BOM → NRT, grootcirkel (aannemelijk: herkomst gebrond [1][2], de vlucht zelf niet) | 6.785 (berekend, grootcirkel) | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | Narita Cargo Area → Jewelry Town Okachimachi | Narita-IC (Higashi-Kanto) → Keiyo-weg → Shuto 7 Komatsugawa → Shuto 1 Ueno-lijn → Okachimachi | hemelsbreed 55 km, geen wegkm (pgm-b3 haalt 74,5 km tot Nihonbashi, eigen meting, geen bron) | maak_stroombeen_weg (extract japan) | nee (evt. korte airside-last-mile bij NRT, zie §7) |

Overlap (haalbaarheidstoets): b3 loopt ca. 90% op de weg van `pgm-rustenburg-tokio` b3 (alleen de laatste 6–10 km is nieuw, Kiba → Shuto 1 → Ueno); toegestaan als eigen route. De BOM-NRT-grootcirkel valt voor 19% binnen 25 km van bestaande lijnen (mumbai-shanghai b2 divergeert).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-bdb` | beurs / vertrekpunt | Bharat Diamond Bourse, G Block, BKC, Mumbai | 19.0641, 72.8646 | [7][10] | bron-gelegd (hergebruikt uit `diamant-mirny-mumbai.md`: torencomplex aan de rivierbocht in BKC, op de OSM-landuse "Bharat Diamond Bourse") |
| `dia-bom-cargo` | vrachtterminal / vertrek lucht | Sahar/CSMIA Air Cargo Complex, Mumbai | 19.0994, 72.8673 | [7][10] | bron-gelegd (hergebruikt uit `diamant-mirny-mumbai.md`: gebouwencluster N van de baan bij de OSM-POI "C.S.I. Airport Cargo Complex Parking") |
| `dia-nrt-cargo` | vrachtterminal / aankomst lucht | Narita Cargo Area (NRT) | 35.7743, 140.3797 | [9] | bron-gelegd (hergebruikt uit `pgm-rustenburg-tokio.md`; hier opnieuw bekeken op z15: rijen blauw gedekte vrachtloodsen met vrachttoestellen op het voorterrein, ten ZW van de passagiersterminals; punt op de loodsenrij) |
| `dia-tokyo-okachimachi` | eindmarkt (wijk) / stoppunt | Jewelry Town Okachimachi, Taito, Tokio (punt: Okachimachi Station) | 35.7073, 139.7748 | [3][4][5] | **onzeker** (z15/z16 gezien: dicht stedelijk blok met het Showa-dori-viaduct van Shuto 1 ~120 m ten oosten van het punt; geen pand te onderscheiden. Wijk-bron: ja.wikipedia zet de groothandelwijk ten oosten van het station over Showa-dori [4]) |

TDE-adres (1-26-2 Higashi-Ueno) heeft geen gevonden coördinaat en volgens WFDB geen handelsvloer [3]: titel en beennaam noemen Okachimachi, niet de TDE-vloer.

## 4 · Via-punten (alleen b3; lat, lon)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b3 | 1 | Narita-IC, Higashi-Kanto Jidoshado | 35.7767, 140.3183 | pgm-b3 via 1: laat de luchthaven-toegangsweg op de snelwegcorridor kiezen i.p.v. de parallelle N51/Narita-kaido |
| b3 | 2 | Chiba, Keiyo-/Tokyo-Bay-Road-corridor | 35.6073, 140.1064 | pgm-b3 via 2 (label daar "Chiba-kita IC", het punt ligt bij Chiba-haven): kiest de zuidelijke kust-corridor boven de noordelijke N14-weg |
| b3 | 3 | Shin-Ohashi-dori (R50), Koto-ku | 35.6825, 139.8869 | pgm-b3 via 3 (label "Ichikawa/Wangan-knoop"): bindend uit de haalbaarheidstoets; OSM: route 50 op 86 m |
| b3 | 4 | Shuto Route 1 Ueno-lijn, vlak S van Okachimachi | 35.7015, 139.7756 | NIEUW: OSM-motorwayvertex (way 254326655, `首都高速1号上野線`) in de laatste 800 m; pint de aankomst op Showa-dori/Shuto 1, niet via Nihonbashi |

b1: geen via-punten (kopie). b2: geen via (grootcirkel). Punt 3 ligt ca. 2 km zuid van Shuto 7: controleer in de bak dat de lijn geen onnodige keerlus maakt.

## 5 · Verwerkingsknopen
*(geen — geen smelter/slijperij: slijpen en polijsten gebeurt vóór deze keten (Surat); Okachimachi is groothandel en juwelenindustrie in gepolijste steen.)*

## 6 · Stoppunt
Bij Jewelry Town Okachimachi: de wijk is het eindpunt uit het ketenontwerp en de enige bron-gedekte plek (groothandelwijk, JTO 1987 met 159 bedrijven, >1.000 bedrijven rond 1989, ca. de helft in de jaren 2000, Indiase bedrijven groeiden [4]); de TDE heeft geen vloer [3] en geen bron noemt één afnemer erachter. Fase D en E vervallen.

## 7 · Open punten
- **Eindanker is een wijkpunt** (Okachimachi Station, 35.7073/139.7748 [5]; ja.wikipedia 35.7074/139.7746 [4]), geen pand en niet de TDE-vloer; status onzeker. De wijk ligt volgens [4] oostelijk over Showa-dori (~120–400 m), dus het punt kan enkele honderden meter te ver westelijk liggen.
- **Vlucht BOM–NRT niet gebrond**: alleen herkomstdata (India grootste bron van Japans gepolijst [1][2][6]); één directe vlucht aangenomen, Narita boven Haneda aangenomen.
- **Cijfers uit 2007 en 2013**, apr/feb-maanden × 12; geen recent Japan-volume gevonden (webbudget). Het India-aandeel op volume (45,6%) komt uit 2007, op waarde (~52%) uit 2013.
- **b3 route**: de gebakken pgm-b3 volgt oppervlakteweg (Narita-kaido, N51, Sakura-kaido, Chiba-kaido) tot de Keiyo-weg, niet de Higashi-Kanto zoals de naam zegt; geen wegkilometer gebrond (hemelsbreed 55 km); de ±15%-toets is alleen indicatie.
- **Airside**: bij NRT sluit het wegbeen op de dichtstbijzijnde openbare weg (pgm-b3 vond 0,28 km first mile); zo niet, korte `--stippel "truck|Narita-vrachtplatform last mile (schematisch — airside/privéterrein)|…"`.
- **b1-kopie**: de bron-tekst in het kopie-geojson noemt (ten onrechte) een andere brief; alleen een tekstveld, geen geometrie.

## 8 · Bronnen
[1] ISDE (Israel Diamond Exchange), 10-04-2013 — Japan polished imports feb 2013: 53,6 mln USD, 149.219 ct, 359 USD/ct; India 27,8 mln USD. https://en.isde.co.il/article.aspx?id=26908
[2] IDEX Online, 04-06-2007 — Japan polished imports apr 2007: 177.752 ct, 69,4 mln USD; India 131.514 ct, 31,64 mln USD (45,6% volume, 74% waarde). https://www.idexonline.com/FullArticle?Id=27632
[3] WFDB — Tokyo Diamond Exchange: 1-26-2 Higashi-Ueno, Taito, opgericht 1994, geen fysieke handelsvloer. https://wfdb.com/bourses/tokyo-diamond-exchange/
[4] ja.wikipedia — 御徒町駅: Jewelry Town Okachimachi ten oosten van het station over Showa-dori; JTO sept 1987, 159 bedrijven; >1.000 rond 1989. https://ja.wikipedia.org/wiki/御徒町駅
[5] en.wikipedia (API, prop=coordinates) — Okachimachi Station 35.707327, 139.774847. https://en.wikipedia.org/wiki/Okachimachi_Station
[6] IDEX Online, 11-10-2011 — grootste importeur van Indiaas gepolijst naar Japan: Tsutsumi Jewelry Co. https://idexonline.com/FullArticle?Id=35917
[7] BDB India (via `diamant-mumbai-newyork.md` [11]) — beveiligd dagelijks transport BDB → Sahar Air-Cargo Complex. https://bdbindia.org/about/
[8] Magical Trip — Okachimachi als groothandel-diamant- en goudwijk (commerciële reisbron, alleen als bevestiging). https://www.magical-trip.com/media/okachimachi-jewelry-shops-2024-famous-for-reasonable-high-quality-jewelry/
[9] `pgm-rustenburg-tokio.md` — anker `pgm-nrt-vracht`, b3-profiel (via 1–3) en gebakken weg 74,5 km; Wikipedia Narita (35,765/140,386).
[10] `diamant-mirny-mumbai.md` en `diamant-mumbai-newyork.md` — ankers `dia-bdb`, `dia-bom-cargo`, b1-geojson `diamant-mumbai-newyork-weg-bdb-bomcargo.geojson`.
[11] OSM via Geofabrik `japan-latest.osm.pbf` (wegscan-cache): Shuto Route 1 Ueno-lijn way 254326655 (139.7756, 35.7015), 首都高速7号小松川線 way 156796455, 新大橋通り R50 way 45664138.
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16) — `v2/build-cache/satcheck/sat-diamant-mumbai-tokyo-okachimachi.png`, `-okachimachi-z16.png`, `-shuto1.png`, `-nrt-cargo.png`.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
**Bestand:** `v2/data/stroomroute-diamant-mumbai-tokyo.json` (51,9 KB, versie 2, lonlat) · functie `bak_diamant_mumbai_tokyo` in `v2/tools/bak_stromen.sh` · profiel `diamant-mumbai-tokyo-narita-okachimachi` in `maak_stroombeen_weg.py`. **Totaal 6.871,2 km · 2.511 punten · 3 benen · 4 markers · geen stippel, geen naad (alle 0,000 km).**

| # | modaliteit | been | km | punten |
|---|---|---|---|---|
| b1 | truck | BDB → Sahar/CSMIA (letterlijke kopie diamant-mumbai-newyork) | 8,4 | 227 |
| b2 | lucht | vlucht BOM → NRT (vrachtvlucht, grootcirkel, aannemelijk: één bron) | 6.785,0 | 273 |
| b3 | truck | Narita Cargo Area → Okachimachi (Higashi-Kanto → Keiyo → Shuto 1) | 77,8 | 2.011 |

**Recept:** b1 = kopie `diamant-mumbai-newyork-weg-bdb-bomcargo.geojson`; b2 = `maak_luchtbeen.py` (CSMIA 19.0994,72.8673 -> Narita 35.7743,140.3797, 273 punten); b3 = `wegscan_puur.py --profiel diamant-mumbai-tokyo-narita-okachimachi` (extract japan, 855 s, 6 via-punten incl. nieuw via 4 op Shuto 1); bake via `bash v2/tools/bak_stromen.sh diamant-mumbai-tokyo`.

**Toets.** b3 77,7 km tegen hemelsbreed 55 (+41%): de brief geeft geen wegkm, dus alleen indicatie; het ligt dicht bij pgm-b3 (74,5 km tot Nihonbashi) en de lijn blijft op de snelweg/oppervlakteweg zonder keerlus. Alle via-snaps 0,00-0,15 km; first mile 0,28 km (service/unclassified) en last mile 0,05 km, dus geen airside-stippel nodig bij NRT. b1 8,4 km tegen hemelsbreed 3,9 (geen wegkm). Markers 0,0 km van de lijn. toets_knikken: 1 omkering (167 gr, R 21 m, 35.7741/140.3822, op het NRT-vrachtplatform, scherpe bocht echt), 0 terugloop; 23 keerlussen gesnoeid (0,6 km). Geen zee, dus geen haven-aanloop.

**Vlucht (b2):** doorgetrokken grootcirkel, geen stippel; aanname één directe vlucht BOM-NRT (niet gebrond, zie §7).

**Lessen:** een Japan-wegscan (japan-pbf, 1,4 mln way-delen) duurt ~14 min: draai hem op de achtergrond met logbestand (een eerste run in de voorgrond brak af op de time-out). De pool `slots/reus` bestond nog niet in de scratchpad (eerst `mkdir -p`). Okachimachi-eindanker blijft een wijkpunt (onzeker), niet de TDE-vloer.
