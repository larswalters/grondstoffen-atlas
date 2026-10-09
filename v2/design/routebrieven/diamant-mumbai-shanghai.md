# Routebrief (licht) · Diamant · Mumbai (BDB) → BOM → Shanghai Pudong vrachtterminal (China)

**stroom-id:** `diamant-mumbai-shanghai` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** gepolijste diamant van de Bharat Diamond Bourse (BKC, Mumbai) gaat per truck naar het Sahar/CSMIA-vrachtcomplex (BOM) en vliegt als aannemelijke vrachtvlucht (grootcirkel) naar de vrachtterminal van Shanghai Pudong (PVG), de invoerpoort van de Shanghai Diamond Exchange (SDE). De keten stopt bij PVG: het SDE-gebouw is niet te leggen (§6, §7).
**Welke as van het verhaal:** *India → mainland China: gepolijst naar de enige invoerpoort* — de SDE is het enige platform in China voor import van gepolijste diamant tegen 0% tarief en 4% btw [2]. Volume: circa 8 Mct/j gepolijst India → China/Hongkong (v1 `design/diamant.md` §4d, natte vinger [5]; de grote poort is Hongkong, het mainland-deel is kleiner en niet apart gebrond). Peiljaren: SDE-nettoimport gepolijst jan–sep 2021 USD 2,316 mld [2]; jan–aug 2025 gepolijste import CNY 2,35 mld (±USD 347 mln, +41,5%) [1]. Eenheid Mct/j; de waarde per karaat verschilt sterk per steen en is niet gebrond. Risico: de Chinese vraag is gedaald en lab-grown knabbelt aan het volume.

## 1 · Ketenkaart
```
Bharat Diamond Bourse `dia-bdb` ──(b1 truck · BKC-connector/Airport Road · 8,4 km · LETTERLIJKE KOPIE diamant-mumbai-newyork b1)──►
CSMIA Air Cargo Complex (BOM) `dia-bom-cargo` ──(b2 lucht · vlucht BOM → PVG, grootcirkel · 5.062,9 km · aannemelijk: één bron)──►
Shanghai Pudong vrachtterminal (PVG) `dia-pvg-cargo` ── stoppunt (SDE in Lujiazui: niet getekend)
```
`dia-bdb` en `dia-bom-cargo` zijn bestaande ankers (`diamant-mumbai-newyork.md`, `diamant-mirny-mumbai.md`); `dia-pvg-cargo` is het bestaande PVG-anker uit `goud-pamp-shanghai.md` / `pgm-rustenburg-shanghai.md`.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Bharat Diamond Bourse → CSMIA Air Cargo Complex (BOM) | BKC-connector / Airport Road (letterlijke kopie `diamant-mumbai-newyork` b1) | 8,4 gebakken in die stroom; hemelsbreed 3,9, geen wegkm | kopie `diamant-mumbai-newyork-weg-bdb-bomcargo.geojson` | nee |
| b2 | B | lucht | BOM → PVG-vrachtterminal | vlucht BOM → PVG, grootcirkel (aannemelijk: één bron) | 5.062,9 berekend op de twee ankers (ontwerp circa 5.063) | maak_luchtbeen | nee, doorgetrokken |

Geen b3. BDB verzorgt dagelijks beveiligd transport tussen de bourse en het Sahar-vrachtcomplex [6], dat is de bronbasis voor b1. Voor b2 noemt geen bron een carrier, vluchtnummer of tussenlanding: één directe vlucht is een aanname (§7).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-bdb` | beursgebouw / vertrek | Bharat Diamond Bourse, G Block, BKC, Mumbai | 19.0641, 72.8646 | [6][7], letterlijk hergebruikt uit `diamant-mumbai-newyork.md` | bron-gelegd (hergebruikt, niet opnieuw gelegd) |
| `dia-bom-cargo` | vrachtterminal / vertrek lucht | CSMIA Air Cargo Complex (Sahar), Mumbai | 19.0994, 72.8673 | [6], letterlijk hergebruikt uit `diamant-mirny-mumbai.md` | bron-gelegd (z15 eigen blik, `…-bom-cargo.png`: kruis net ten noorden van het luchthavenhek tussen dichte bebouwing, vrachtloodsen en hangaars ±0,3 km zuidelijker; niet verschoven, zelfde punt als zes zusterbrieven) |
| `dia-pvg-cargo` | vrachtterminal / aankomst lucht, stoppunt | Shanghai Pudong International Airport, vrachtplatform | 31.1335, 121.8025 | [8], letterlijk hergebruikt uit `goud-pamp-shanghai.md` (au-pvg-vrachtterminal) | aannemelijk (hergebruikt; eigen z15/z16-blik wijkt af, zie §7) |

## 4 · Via-punten
Geen. b1 is een kopie zonder via-punten (stadsrit <15 km binnen Mumbai); b2 is een grootcirkel.

## 5 · Verwerkingsknopen
Geen. De SDE is een handels- en douane-platform, geen bewerkingsplek; het slijpen/polijsten (Surat) valt buiten deze keten.

## 6 · Stoppunt
De brief stopt op de PVG-vrachtterminal, conform de bindende haalbaarheidstoets: het SDE-gebouw staat niet in OSM en geen bron geeft een gebouwcoördinaat, dus een truckbeen PVG → SDE zou een verzonnen anker nodig hebben (fase C vervalt, D/E vervallen).

## 7 · Open punten
- **SDE-gebouw niet te leggen.** Pudong-overheid zet de SDE in Lujiazui (opgericht 27-10-2000) [1]; het adres "No 2001 Century Avenue" staat op die pagina uitsluitend in de footer "Contact Us" van de Pudong-overheidssite en hoort daarom hoogstwaarschijnlijk bij de Pudong-overheid, niet bij de SDE. Nominatim/Photon vinden niets, een zoekopdracht (zh) leverde geen straatadres. Niets getekend; alleen met een brongebouwcoördinaat volgt een truckbeen PVG → SDE (china-extract aanwezig, hemelsbreed circa 27–30 km, geen wegkm).
- **PVG-anker ligt volgens eigen blik op de passagiersapron**, niet op het vrachtplatform: z15/z16 (`…-pvg-cargo.png`, `…-pvg-cargo-z16.png`) toont het kruis aan de westzijde van het satellietterminalcomplex tussen geparkeerde passagierstoestellen; een vrachtzone met freighters en loodsen ligt ±1,2 km zuidelijker (kandidaat ≈ 31.1222, 121.8064, niet gebruikt) en een tweede vrachtzone met grote loodsen ten westen langs lon 121.78. Bindend toch hergebruikt voor consistentie met `goud-pamp-shanghai` en `pgm-rustenburg-shanghai`; correctie hoort centraal, voor alle drie de stromen tegelijk. Effect op de vlucht: <0,03% van de km.
- **Geen bron voor directe BOM → PVG-vracht en geen herkomstaandeel India → SDE.** SDE-leden zijn "voornamelijk groothandelaren uit België, India en Israël" [1]; mainland-volume is klein ten opzichte van Hongkong. Daarom "aannemelijk" in de beennaam.
- **Geen gepubliceerde vluchtlengte**; b2 is een berekende grootcirkel, de echte route kan langer zijn.
- **Gepubliceerde wegkm voor b1 ontbreekt** (kopie van een stroom met −16,5% tegen een ongebronde ~10 km).
- **Volume India → mainland China niet apart gebrond**; 8 Mct/j is de v1-natte-vinger voor China/Hongkong samen.

## 8 · Bronnen
[1] Shanghai Pudong-overheid, "Shanghai Diamond Exchange" (opgericht Lujiazui 2000-10-27; leden vooral uit België, India, Israël; jan–aug 2025 gepolijste import CNY 2,35 mld). https://english.pudong.gov.cn/2026-06/03/c_499178.htm
[2] Israel Diamond Institute, "China's Diamond Import Sustains Growth Momentum in 2021" (SDE enige poort voor gepolijste import, 0% tarief en 4% btw; netto gepolijste import jan–sep 2021 USD 2,316 mld). https://en.israelidiamond.co.il/news/press-releases/china-diamond-import-2021/
[3] Wikipedia, "World Federation of Diamond Bourses" (Mumbai en Shanghai Diamond Exchange als leden-bourses). https://en.wikipedia.org/wiki/World_Federation_of_Diamond_Bourses
[4] Wikipedia, "Shanghai Pudong International Airport" (PVG, referentiepunt 31.1433, 121.8053). https://en.wikipedia.org/wiki/Shanghai_Pudong_International_Airport
[5] v1 `design/diamant.md` §4d (intern): dia-mumbai → dia-mkt-china, 8 Mct/j, mode air.
[6] BDB India, "About Us" (98% van Indiase diamantexport, dagelijks beveiligd transport bourse ↔ Sahar Air-Cargo Complex). https://bdbindia.org/about/
[7] Wikipedia, "Bharat Diamond Bourse" (grootste diamantbeurs ter wereld, BKC, 8,1 ha, ±2.500 handelaren). https://en.wikipedia.org/wiki/Bharat_Diamond_Bourse
[8] `goud-pamp-shanghai.md` en `pgm-rustenburg-shanghai.md` (anker PVG-vrachtplatform 31.1335, 121.8025).
[9] `diamant-mumbai-newyork.md` (b1-kopie, ankers BDB en BOM) en `diamant-mirny-mumbai.md`.
[10] Haalbaarheidstoets golf 8 (bindend): stop bij PVG, SDE-adres niet in OSM (china-pbf gescand op 钻石/Diamond Exchange/钻交所).
[11] Esri World Imagery via `v2/tools/sat_check.py` (live 2026-10-09): `v2/build-cache/satcheck/sat-diamant-mumbai-shanghai-bom-cargo.png`, `-pvg-cargo.png`, `-pvg-cargo-z16.png`.
[12] WebSearch (zh, 2026-10-09) naar SDE-adres en BOM–PVG-diamantvracht: geen straatadres, geen BOM–PVG-bron.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
Bestand `v2/data/stroomroute-diamant-mumbai-shanghai.json` (9,5 KB, contract versie 2, lonlat), functie `bak_diamant_mumbai_shanghai()` in `v2/tools/bak_stromen.sh` (LF, 0 CRLF). Totaal 5.071,3 km, 431 punten, 3 markers (allemaal 0,0 km van hun lijn). Bak 14 s, geen wegscan, geen profiel.

| # | modaliteit | been | km | punten | naad |
|---|---|---|---|---|---|
| b1 | truck | BDB naar CSMIA Air Cargo Complex (kopie diamant-mumbai-newyork b1) | 8,4 | 227 | 0 |
| b2 | lucht | vlucht BOM naar PVG (grootcirkel, aannemelijk: een bron) | 5.062,9 | 204 | 0,0 |

**Recept.** b1: `--been-geojson` rechtstreeks op `diamant-mumbai-newyork-weg-bdb-bomcargo.geojson` (letterlijke kopie, niet opnieuw gerouteerd). b2: `maak_luchtbeen.py --van "CSMIA Air Cargo Complex BOM|19.0994,72.8673" --naar "Shanghai Pudong PVG vrachtterminal|31.1335,121.8025" --uit diamant-mumbai-shanghai-lucht-bom-pvg.geojson` (FeatureCollection, 204 punten, 5.062,9 km zoals verwacht), doorgetrokken.

**Toets.** Lengte b1 is die van de bronstroom (8,4 km tegen alleen hemelsbreed 3,9; geen echte wegkm, dus indicatie). b2 heeft per constructie geen km-toets. Geen naad boven 0,0 km. `toets_knikken.py`: 16 knikken, alle in de gekopieerde b1 (BKC/Sahar-stadsnet, 10-28 m straal), 0 omkeringen, 0 terugloop; b2 0 knikken. Geen stippel, geen haven-aanloop, geen airside-stippel (b1 eindigt op de openbare weg, na PVG volgt geen weg).

**Lessen.** (1) PVG-anker 31.1335,121.8025 ligt op de passagiersapron, vrachtzone circa 1,2 km zuidelijker (kandidaat 31.1222,121.8064); centrale correctie voor goud-pamp-shanghai, pgm-rustenburg-shanghai en deze keten tegelijk (effect op vlucht <0,03%). (2) SDE-gebouw niet te leggen, keten stopt bij PVG. (3) Registerregel centraal: sleutel `dia-ms`, bestand `stroomroute-diamant-mumbai-shanghai.json`.
