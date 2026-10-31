# Routebrief (licht) · PGM — Norilsk Nickel Harjavalta → Via Pori en Moermansk → Koperfabriek Norilsk (Finland/Rusland)

**stroom-id:** `pgm-harjavalta-norilsk` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** PGM-houdende **koperkoek** (neven-product van de Nikkel-raffinage in Harjavalta) gaat per **truck** (vt 2) naar de haven van Pori (Mäntyluoto), per **zeeschip** naar de Nornickel-terminal in Moermansk, dan met de Arc7-vloot via Karskiye Vorota naar de Jenisej-golf, per **binnenvaart** naar Dudinka en per **spoor** (geïsoleerd Norilsk-net) naar de Koperfabriek in Norilsk; stoppunt = de Koperfabriek.
**Welke as van het verhaal:** de Nornickel-lus: Russische matte gaat naar Finland, de PGM-rijke koek keert terug naar Norilsk. Volume **2E (Pd+Pt) in koek: 2018 69 koz = 2,1 t, 2019 66 koz = 2,05 t, 2020 21 koz = 0,65 t** (koz ÷ 32,15; geen Rh/Au) [3]; **indicatie ~2,1 t 2E/j** (peiljaar 2019), het aandeel dat naar Norilsk gaat is niet gepubliceerd. ⚠️ **Sinds het 20e EU-pakket (23-4-2026, haven Moermansk) staat de scheepvaart Pori → Moermansk stil** [1][2][6]: de lijn toont de gedocumenteerde route 2022–apr 2026, niet de lading van vandaag.

## 1 · Ketenkaart
```
Nornickel Harjavalta `pgm-nn-harjavalta` ──(b1 truck · vt 2 · gemeten 47,7 km, hemelsbreed 45,3)──► Pori Mäntyluoto `pgm-pori-kade`
──(b2 zee · haven-aanloop Pori, stippel 25,7 km, kopie)──► zeeknoop 4537 ──(b3 zee · 3.943,2 km)──► Moermansk-terminal `pgm-moermansk-terminal`
──(b4 zee · Arc7 · 2.124,5 km)──► zeeknoop 2338 Jenisej-golf ──(b5 stippel 20,2 km · b6 binnenvaart 430,2 km)──► Dudinka-kade `pgm-dudinka-kade`
──(b7 spoor · Norilsk-industrienet · 84,8 km)──► Koperfabriek Norilsk `pgm-koperfabriek-norilsk` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | NN Harjavalta → Pori Mäntyluoto (aannemelijk: modaliteit niet gebrond) | vt 2 (Harjavalta–Nakkila–Pori) | hemelsbreed 45,3 km, geen wegkm; gemeten 47,7 | maak_stroombeen_weg (profiel `pgm-harjavalta-norilsk-nn-pori`) | nee |
| b2 | C | zee | kade Pori → zeeknoop 4537 | — | 25,7 (kopie `grafiet-harjavalta-heroya`) | maak_havenaanloop (bestaand geojson) | ja, kade 22,3 km van de zeeknoop |
| b3 | B | zee | zeeknoop 4537 → Moermansk-terminal (aannemelijk: één bron) | Botnische Golf, Sont, Skagerrak, Noordkaap, Barentszzee | geen gepubliceerde km; MARNET 3.943,2 | MARNET | nee |
| b4 | B | zee | Moermansk → zeeknoop 2338 | Barentszzee, Karskiye Vorota, Karazee; Arc7 [5] | 2.124,5 (MARNET, omgekeerd van `nikkel-norilsk-monchegorsk` b3) | MARNET | nee |
| b5 | B | zee | zeeknoop 2338 → bulk-knoop Jenisej | — | 20,2 (naad > 5 km, omgekeerde kopie nikkel b2b) | rechte stippel | ja, net reikt niet |
| b6 | B | binnenvaart | bulk-knoop → Dudinka-kade | Jenisej stroomopwaarts | 430,2 (omgekeerde kopie nikkel b2, geen gepubliceerde km) | gespiegeld geojson | nee |
| b7 | C | spoor | Dudinka-kade → Koperfabriek | Norilsk-industrienet Dudinka–Kajerkan–Norilsk [4] | geen spoorkm gepubliceerd; router 84,5 / bake 84,8 | toets_spoorroute rusland-siberie, `--hoofd-km=50 --max-snap=10` | nee |

Geen b3b-aanloop Moermansk: kade 1,2 km van zeeknoop 6906 (< 5 km). Naad rivier-einde ↔ spoor-begin 3,1 km (< 5), alle andere naden 0,00.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-nn-harjavalta` | raffinaderij (kop) | Norilsk Nickel Harjavalta Oy, Teollisuuskatu 1 (hergebruik `ni-harjavalta-raffinaderij`, nikkel-norilsk-monchegorsk) | 61.3188, 22.1225 | [3][8] | bron-gelegd (z15 gezien: groot raffinaderijcomplex met hallen en rangeerspoor, punt midden op de fabriekshallen; geen perceelgrens t.o.v. Boliden te zien) |
| `pgm-pori-kade` | overslag truck → zee | Port of Pori, Mäntyluoto noordkade (hergebruik `gr-pori-kade`, grafiet-harjavalta-heroya) | 61.5959, 21.4966 | [1][8] | aannemelijk (haven bron-gelegd in andere brief; bron zegt alleen Porin satama, alternatief Tahkoluoto 61.6353, 21.4036) |
| `pgm-moermansk-terminal` | overslag zee → zee | Nornickel Murmansk Transport Division, Портовый проезд 31/1 (hergebruik `ni-moermansk-terminal`) | 68.9737, 33.0658 | [5][8] | aannemelijk (adres uit bedrijvenregister, geen naambord gezien; overgenomen) |
| `pgm-dudinka-kade` | overslag binnenvaart → spoor | Dudinka-havenkade, Jenisej (hergebruik `ni-dudinka-kade`) | 69.4030, 86.1680 | [5][8] | bron-gelegd (kadekranen langs de rivier, spoor erlangs; overgenomen) |
| `pgm-koperfabriek-norilsk` | losplek/smelter (staart) | Koperfabriek (Copper Plant, Medny Zavod), Norilsk (sitelaag koper `w-norilsk-copper-plant`) | 69.3632, 88.1279 | [4][9] | bron-gelegd voor de fabriek (z15 gezien: smelter met twee rood-wit gestreepte pijpen, rookpluim, hallen en spoorbundel; het punt ligt op de ketelhal naast de pijpen) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | vt 2 west van Harjavalta | 61.3446, 22.0253 | pint de oprit op vt 2 (hergebruik via-punten `grafiet-harjavalta-heroya`) |
| b1 | 2 | vt 2 bij Nakkila | 61.4068, 21.9161 | houdt de route op vt 2 |
| b1 | 3 | vt 2 / vt 8 west van Pori | 61.4792, 21.7600 | Pori-ringweg, niet door het centrum |
| b1 | 4 | vt 2 noordoost van Pori | 61.5494, 21.5906 | pint de nadering van Mäntyluoto |
Spoor b7: geen via-punt nodig (één lijn, enige corridor; één run, 63 edges).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Harjavalta (International site) | Nornickel | matte uit Kola → Ni-producten + koperkoek met Pd/Pt | 66 kt Ni/j; koek 2018 18 kt Cu, 58 koz Pd + 11 koz Pt | [3] |
| Murmansk-terminal | Nornickel Murmansk Transport Division | koek/halffabricaten → Dudinka (ook matte Dudinka → Kola) | niet gepubliceerd | [5] |
| Koperfabriek | Nornickel Polar Division | koperconcentraat + koek van de International site → kathodekoper, zwavel, edelmetaalconcentraat | niet gepubliceerd | [4] |

## 6 · Stoppunt
De brief stopt bij de Koperfabriek: AR 2025 noemt hem als verwerker van de koek [4]; wat met de PGM-concentraten daarna gebeurt (raffinage onder tolling) staat niet met locatie in de bron, dus geen fase D/E.

## 7 · Open punten
- **Route niet in één bron:** Yle noemt schip Pori → Moermansk en verwerking in Norilsk [1]; AR 2025 zegt koek naar de Norilsk-site en Murmansk-terminal → Dudinka [4][5]. Het stuk Moermansk → Norilsk is dus afgeleid (Dudinka-schip + spoor); de Moermansk-terminal is aannemelijk.
- **Sanctie:** verscheping stil sinds april 2026; haven-alternatieven (Vyborg, Sint-Petersburg, Oest-Loega) onbeslist [1][2]. Niet getekend. Ook directe zeevaart uit een andere Finse haven is niet uit te sluiten.
- **Pori-kade en modaliteit Harjavalta → Pori** niet gebrond (Mäntyluoto aangenomen; Tahkoluoto als alternatief; spoor Pori-lijn niet uitgesloten). Geen wegkm: 47,7 gemeten is een indicatie.
- **Volume:** 2020 laat 21 koz zien omdat de koek naar Norilsk ging [3]; geen publicatie over de PGM-inhoud van de koek 2021–2025; aandeel PGM dat in Norilsk aankomt onbekend.
- Spoor b7: een terugloop van ~1 km bij 69.3603, 88.1362 en twee scherpe bochten aan het fabrieksemplacement (OSM-topologie, bewust gelaten). Dudinka-marker ligt 1,3 km van de lijn (anker ≠ routeerpunt).
- Koperfabriek-anker uit Photon/OSM, geen bedrijfsadres. Sitelaag: Norilsk Nickel Harjavalta staat niet in de PGM-sitelaag (centraal toevoegen).

## 8 · Bronnen
[1] Yle, 10-5-2026, EU:n pakotteet iskevät Nornickel Harjavaltaan — schip Pori → Moermansk (~6/j sinds 2022), kuparisakka verwerkt in Norilsk, stilgezet. https://yle.fi/a/74-20225231
[2] Yle, 12-5-2026, Nornickel Harjavalta selvittää toimitussatamaa — haven Moermansk sinds april onder EU-sanctie, geen alternatief besloten. https://yle.fi/a/74-20225512
[3] Nornickel AR 2020, Kola division (Finland), p. 94-95 — productietabel koek 2018-2020; koek 2020 vooral naar de Polar Division. https://ar2020.nornickel.ru/pdf/ar/en/business-overview_operational-performance_kola-finland.pdf
[4] Nornickel AR 2025, p. 41-45 — "Copper Plant processes ... copper cake from the International site"; koek naar de Norilsk-site. https://nornickel.com/upload/files/ru/investors/reports-and-results/annual-reports/annual_report_of_pjsc_mmc_norilsk_nickel_2025-eng.pdf
[5] Nornickel AR 2025, p. 51-52 — Murmansk Transport Division; eigen terminal Moermansk, halffabricaten naar Dudinka; Arc7-vloot; Dudinka-spoor p. 3. Zelfde pdf als [4].
[6] Europese Commissie, 23-4-2026, 20th package (haven Moermansk op de lijst; via zoekresultaat, niet zelf gelezen). https://malta.representation.ec.europa.eu/news/eu-adopts-20th-package-sanctions-against-russia-2026-04-23_en
[7] Barents Observer, Brussels adds port of Murmansk to sanctions list (via zoekresultaat, niet gelezen). https://www.thebarentsobserver.com/news/brussels-adds-port-of-murmansk-to-sanctions-list/449431
[8] Eigen briefs: `nikkel-norilsk-monchegorsk.md` (Harjavalta, Moermansk, Dudinka, rivier, zee), `grafiet-harjavalta-heroya.md` (Pori-kade, aanloop, via-punten vt 2).
[9] `v2/design/koper-sitelaag.json` `w-norilsk-copper-plant` (OSM landuse "Медный завод", Photon).
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15): `pgm-harjavalta-norilsk-nn-harjavalta`, `pgm-harjavalta-norilsk-koperfabriek` in `v2/build-cache/satcheck/`.
[11] Eigen metingen: `maak_stroombeen_weg.py` (47,7 km), `toets_spoorroute.mjs` (84,5 km), `hecht_marnet.py` (naden).

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
**Bestand:** `v2/data/stroomroute-pgm-harjavalta-norilsk.json` (65,7 KB, versie 2, punt_formaat lonlat), functie `bak_pgm_harjavalta_norilsk` (bak_stromen.sh), wegprofiel `pgm-harjavalta-norilsk-nn-pori` (maak_stroombeen_weg.py). **Totaal 6.676,3 km, 7 benen, 5 markers.** Register (centraal): sleutel `pgm-hn`, label "Harjavalta → Norilsk Koperfabriek".

| # | modaliteit | van → naar | km gebakken | km brief | stijl |
|---|---|---|---|---|---|
| b1 | truck | NN Harjavalta → Pori Mäntyluoto (vt 2) | 47,7 | geen wegkm; hemelsbreed 45,3 | doorgetrokken |
| b2 | zee | haven-aanloop Pori (kade → zeeknoop 4537) | 25,7 | 25,7 (kopie) | stippel: net reikt niet |
| b3 | zee | zeeknoop 4537 → Moermansk | 3.943,2 | MARNET 3.943,2 | doorgetrokken |
| b4 | zee | Moermansk → zeeknoop 2338 (Arc7, Karskiye Vorota) | 2.124,5 | 2.124,5 | doorgetrokken |
| b5 | zee | zeeknoop 2338 → bulk-knoop Jenisej | 20,2 | 20,2 | stippel: naad > 5 km |
| b6 | binnenvaart | bulk-knoop → Dudinka-kade | 430,2 | 430,2 (gespiegeld) | doorgetrokken |
| b7 | spoor | Dudinka-kade → Koperfabriek | 84,8 | router 84,5 | doorgetrokken |

**Recept:** b1 `wegscan_puur.py --profiel pgm-harjavalta-norilsk-nn-pori` (extract finland, 4 via-punten op vt 2, venster 25 km); b2 letterlijke kopie `grafiet-harjavalta-heroya-aanloop-pori.geojson`; b3 en b4 MARNET `--been` kade → kade (b4 = omgekeerde run van nikkel-norilsk-monchegorsk b3); b5 `--stippel` rechte lijn (omgekeerd van nikkel b2b); b6 gespiegeld geojson `pgm-harjavalta-norilsk-rivier-bulkknoop-dudinka.geojson`; b7 `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` rusland-siberie, hoofd-km 50, max-snap 10. Geen lucht, geen leiding, geen via-punt op spoor.

**Toets:** naden 0,00 km behalve rivier-einde ↔ spoor-begin 3,08 km (< 5). Geen b3b-aanloop Moermansk (kade 1,2 km van zeeknoop). Markers: NN Harjavalta en Pori-kade 0,0 km van de lijn, Koperfabriek 0,18 km, Moermansk 1,11 km en Dudinka 1,26 km (anker is geen routeerpunt, zelfde als nikkel-norilsk-monchegorsk; bewust). toets_knikken: één terugloop op spoor b7 bij 69.3603, 88.1362 (OSM-emplacement Koperfabriek), bewust gelaten; krappe bochten in zee b3/b4 zijn gedeelde MARNET-geometrie. Geen km-toets ±15% mogelijk op b1 (geen wegkm; 47,7 vs hemelsbreed 45,3 = +5,3% als indicatie).

**Stippels:** b2 (Pori: MARNET reikt niet tot de kade, 22,3 km) en b5 (Jenisej-golf: naad MARNET ↔ rivierlaag 20,2 km); beide schematisch over water. De sanctie-stilstand sinds apr 2026 en het aannemelijke Moermansk-Norilsk-stuk staan in de brief en niet in de lijnstijl.

**Lessen:** gedeelde benen (Pori-aanloop, Moermansk-Jenisej, rivier) zijn letterlijke kopieën of omgekeerde runs van bestaande stromen en leveren 0,00-naden; geen last-mile-been nodig omdat alle ankers binnen 2 km van het net liggen.
