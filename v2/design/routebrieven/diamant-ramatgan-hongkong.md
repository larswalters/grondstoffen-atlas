# Routebrief (licht) · diamant — Ramat Gan → Ben Gurion → Hongkong (Israël → Hongkong)

**stroom-id:** `diamant-ramatgan-hongkong` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** gepolijste diamant van de Israel Diamond Exchange (Diamond Tower, Ramat Gan) gaat per beveiligde truck (stippel, geen net) naar de Maman-vrachtterminal van Ben Gurion (TLV), vliegt als vrachtvlucht (grootcirkel, aannemelijk: één bron voor de handelsstroom, vlucht niet gebrond) naar de Cathay Pacific Cargo Terminal van Hong Kong International (HKG) en rijdt over North Lantau Highway, Tsing Ma Bridge en Western Harbour Crossing naar het Hong Kong Diamond Exchange Building in Central.
**Welke as van het verhaal:** *Israël → Azië: de tweede polished-markt* — Hongkong nam 28% van de Israëlische polished-export in 2012 [1] en 18% van de gross polished-export in 2024 (secundair, niet geopend) [2]; 2024 netto polished-export 1,87 mld USD (-35,7%) [3]. **Volume in Mct/j: niet gevonden** (geen karaatcijfer per bestemming; Kimberley Process geeft Israël-totaal 2025 uitvoer 2,0 Mct, 579 mln USD, rough+polished, zonder bestemming [8]). Waarde per karaat ligt hoog (grote stenen); het gewicht blijft Mct, de waarde staat niet in het gewicht.

## 1 · Ketenkaart
```
Israel Diamond Exchange, Diamond Tower `dia-ide` ──(b1 truck · stippel last mile, geen net: Israel-extract ontbreekt · hemelsbreed 13,6 km, geen wegkm; kopie)──►
Maman Cargo Terminal, Ben Gurion (TLV) `dia-tlv-cargo` ──(b2 lucht · vlucht TLV → HKG, grootcirkel, aannemelijk: een bron, 2012 · 7.726,4 km)──►
Cathay Pacific Cargo Terminal, HKG `dia-hkg-cargo` ──(b3 truck · North Lantau Hwy → Tsing Ma Bridge → Kwai Chung → Western Harbour Crossing · 40,8 km, kopie)──►
Hong Kong Diamond Exchange Building, Central `dia-hk-exchange` ── stoppunt
```
Alle vier ankers bestaan al (`diamant-ramatgan-newyork.md`, `diamant-surat-hongkong.md`) en zijn hier letterlijk hergebruikt; b1 en b3 zijn letterlijke kopieën, alleen b2 is nieuw.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Israel Diamond Exchange → TLV-vrachtterminal | geen corridor: stippel last mile (geen net op deze korrel: Israel-extract ontbreekt, schematisch); kopie `diamant-ramatgan-newyork` b1 | hemelsbreed 13,6 km, geen wegkm [berekend] | `--stippel` (kopie van de beenregel) | ja — hier reikt het net niet |
| b2 | B | lucht | TLV → HKG | vlucht TLV → HKG (vrachtvlucht, grootcirkel, aannemelijk: een bron, 2012) | 7.726,4 grootcirkel [berekend, `maak_luchtbeen`, 311 punten]; ontwerp 7.726 | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | Cathay Pacific Cargo Terminal (HKG) → Hong Kong Diamond Exchange Building | North Lantau Hwy → Tsing Ma Bridge → Kwai Chung → Western Harbour Crossing (kopie `diamant-surat-hongkong` b4, richting HKG → exchange) | 40,8 [gebakken kopie]; geen gepubliceerde wegkm; hemelsbreed ca. 24 km, geen wegkm | letterlijke kopie geojson `diamant-surat-hongkong-weg-hkgcargo-hkexchange.geojson` (1.251 punten) | nee |

b1 en b3 hebben geen eigen wegkilometer-toets: b1 is hemelsbreed (indicatie); b3 is een bestaande bake (+25,8% op de via-puntensom 32,4 km, daar al als bevinding gemeld, hoort bij `diamant-surat-hongkong`).

## 3 · Ankers (één per site en per overslag) — alle hergebruikt, geen nieuwe gelegd
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-ide` | beursgebouw / vertrekpunt | Israel Diamond Exchange, Diamond Tower, Ramat Gan | 32.0836, 34.8024 | [4] (brief `diamant-ramatgan-newyork`) | bron-gelegd (daar z16 gezien: hoogbouwcluster van het Bourse-district; Wikipedia 32.08357/34.80236) |
| `dia-tlv-cargo` | vrachtterminal / vertrek luchtvracht | Maman Cargo Terminal, Ben Gurion Airport (TLV) | 31.9949, 34.9019 | [4][5] | bron-gelegd op terminalniveau (daar z17 gezien: groot loodsgebouw met truckparking oostzijde, platform met vrachttoestellen ca. 300 m noordelijker; pand dat diamant afhandelt onzeker). Landzijde: geen airside-stippel |
| `dia-hkg-cargo` | vrachtterminal / aankomst luchtvracht | Cathay Pacific Cargo Terminal, Chek Lap Kok | 22.2975, 113.9247 | [6] (brief `diamant-surat-hongkong`) | bron-gelegd (daar z15 gezien: apart vrachtgebouwencomplex met loodsen direct aan het platform, wide-body vrachttoestellen op het apron; OSM `post_depot` "Cathay Pacific Cargo Terminal") |
| `dia-hk-exchange` | beurs-/handelsgebouw / eindpunt | Hong Kong Diamond Exchange Building, 20 Ice House Street, Central | 22.2797, 114.1570 | [6] | bron-gelegd (daar z16 gezien: dicht stedelijk bouwblok in Central bij het havenfront) |

Geen nieuwe satellietblik: alle vier staan letterlijk op de coördinaat van de bron-brief (beelden `v2/build-cache/satcheck/sat-diamant-ramatgan-newyork-ide.png`, `-tlv-maman-z17.png`, `sat-diamant-surat-hongkong-hkg-vracht.png`, `-hk-diamantbeurs.png`). Het HKG-anker ligt airside; het gekopieerde wegbeen snapt op 0,05 km en gebruikt de kleine-wegklassen-aanloop (0,98 km service/tertiary), dus geen extra last-mile-stippel.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | stippel, geen routering |
| b3 | 1–4 | North Lantau Highway · Tsing Ma Bridge · Kwai Chung Interchange · Western Harbour Crossing (HK-portaal) | 22.3143,113.9924 · 22.3514,114.0742 · 22.3667,114.1250 · 22.3014,114.1567 | letterlijke kopie, geen nieuw profiel; zie `diamant-surat-hongkong.md` §4 (enige snelwegcorridor van de luchthaven en enige tunnel naar Hong Kong Island) |

## 5 · Verwerkingsknopen
*(geen — handelsketen van reeds gepolijste steen; geen bron koppelt déze stenen aan een slijperij. Fase D/E vervallen.)*

## 6 · Stoppunt
De brief stopt bij het Hong Kong Diamond Exchange Building: het eindpunt uit het ketenontwerp en een handelsgebouw; geen bron koppelt déze stroom aan een individuele juwelier of fabriek. Fase D vervalt.

## 7 · Open punten
- **De directe vlucht is historisch, niet actueel.** Cathay Pacific vloog TLV–HKG met A350 sinds maart 2017 (zes per week in 2018, buikvracht) [7]; de route is sinds de oorlog opgeschort (Cathay-melding: nog altijd "until further notice" per 8 okt 2025, via zoekresultaat, niet geopend) [9] en Cathay Cargo sloot het Tel Aviv-station definitief op 24 mei 2026, Israëlische lading naar Cathay gaat nu "via Hong Kong" (offline GSA WTA) [10]. De getekende vlucht is dus de vaste vorm van de handelsstroom, niet de huidige operatie; welke carrier/tussenlanding nu vliegt: niet gevonden. Geen bron noemt diamant op déze vlucht; diamant gaat als beveiligde vracht op lijnvluchten [11]. Beennaam: aannemelijk.
- **Aandeel is oud of secundair.** Hongkong 28% van de polished-export in 2012 [1]; 18% van gross polished 2024 volgens Jewish Business News (pagina niet te openen, cijfer via zoekresultaat; USA 55%, Zwitserland 7%) [2]. Netto polished 2024 1,87 mld USD [3] (netto en gross zijn verschillende maten).
- **Volume in Mct/j niet gevonden** (geen bestemming-splitsing in karaat); alleen dollar-aandelen gebrond.
- **Oorlog 2026:** Iran-conflict vanaf 1 maart 2026 verstoorde vluchten van/naar Israël en sloot tijdelijk de IDE-handelsvloer (Rapaport, via brief `diamant-dubai-ramatgan` [2b], niet opnieuw geopend) [12]. De kaart toont de vaste vorm, niet de ontregeling.
- **b1 is schematisch** (13,6 km hemelsbreed, geen wegkm); optioneel centraal: Israel-extract (`fetch_landnet.py`). Sitelaag `w-ramatgan` staat 0,7 km van `dia-ide` (centraal gelijktrekken).
- **Bakker:** het ontwerp noemt b3 "b5 van diamant-surat-hongkong"; in de brief en het geojson is het been b4 (naam "Cathay Pacific Cargo Terminal (HKG) → Hong Kong Diamond Exchange Building ..."). TLV-pand voor diamantafhandeling onzeker.

## 8 · Bronnen
[1] Wikipedia, "Diamond industry in Israel" — VS 36%, Hongkong 28%, België 8% van de polished-export 2012; polished-export 2012 netto 5,56 mld USD. https://en.wikipedia.org/wiki/Diamond_industry_in_Israel
[2] Jewish Business News, 26-1-2025, "2024 Israeli Diamond Sector Sees Dramatic Revenue Downturn" — VS ca. 55%, Hongkong 18%, Zwitserland 7% (gross polished 2024). Niet geopend (DNS-fout); cijfer uit zoekresultaat. https://jewishbusinessnews.com/2025/01/26/2024-israeli-diamond-sector-sees-dramatic-revenue-downturn/
[3] Xinhua, 23-1-2025, "Israel sees sharp decline in diamond trade in 2024" — netto polished-export 1,87 mld USD (-35,7%), rough 634,9 mln USD (-24,1%), bron Ministry of Economy and Industry. http://english.news.cn/20250123/32b1607425624c9093f1e4552ebc246f/c.html
[4] `diamant-ramatgan-newyork.md` (M31 golf 9) — ankers `dia-ide`, `dia-tlv-cargo`, stippel b1; bestand `v2/data/stroomroute-diamant-ramatgan-newyork.json`.
[5] Maman Group, "Maman Cargo Terminal" (kluizen, beveiligde begeleiding). https://en.maman-group.co.il/companies/maman-cargo-terminal/
[6] `diamant-surat-hongkong.md` (M31 golf 3) — ankers `dia-hkg-cargo`, `dia-hk-exchange`, b4 en geojson `v2/build-cache/ais/graaf/diamant-surat-hongkong-weg-hkgcargo-hkexchange.geojson` (40,81 km, 1.251 punten, FeatureCollection, richting HKG → exchange).
[7] WTA Cargo, 18-2-2018, "Cathay Pacific to Increase flights to Daily HKG-TLV-HKG" — A350-900, gelanceerd maart 2017, vanaf 25-3-2018 zes per week. https://www.wta.co.il/cathay-pacific-to-increase-flights-to-daily-hkg-tlv-hkg/
[8] TheGlobalEconomy.com (Kimberley Process), Israël diamant-uitvoer 2025: 2.002.626 ct, 579,45 mln USD (via brief `diamant-dubai-ramatgan` [2]; niet opnieuw geopend). https://www.theglobaleconomy.com/Israel/diamond_exports_carats/
[9] Cathay Pacific, "Cathay Pacific temporarily suspends Tel Aviv services" — vluchten opgeschort tot nader order (laatste update 8-10-2025, via zoekresultaat; pagina time-out). https://www.cathaypacific.com/cx/en_HK/latest-news/flight-disruptions/latest-situation-in-tlv.html
[10] WTA Cargo, 24-5-2026, "Cathay Cargo Closes Tel Aviv Station — WTA Continues as Offline GSA via Hong Kong". https://www.wta.co.il/cathay-cargo-closes-tel-aviv-station-wta-continues-as-offline-gsa-via-hong-kong/
[11] Israel Diamond Institute, "Transports of diamonds in the world" (via brief `diamant-ramatgan-newyork` [7]; pagina 403, niet opnieuw geopend). https://en.israelidiamond.co.il/diamond-articles/diamonds/transports-diamonds-world/
[12] Rapaport, "Iran War Disrupts Diamond Trade in Dubai, Israel" (1-2 maart 2026; via brief `diamant-dubai-ramatgan` [2b]). https://rapaport.com/news/iran-war-disrupts-diamond-trade-in-dubai-israel/
[13] `maak_luchtbeen.py` TLV → HKG: 7.726,4 km, 311 punten (proefrun 2026-10-31, uitvoer in scratchpad, niet in build-cache). Eigen berekening.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
`bash v2/tools/bak_stromen.sh diamant-ramatgan-hongkong` → `v2/data/stroomroute-diamant-ramatgan-hongkong.json` (33,1 KB, versie 2, lonlat, 3 benen, 1.564 punten, 4 markers). Functie `bak_diamant_ramatgan_hongkong` in `bak_stromen.sh`; geen profiel, geen wegscan, geen zee, geen haven-aanloop, geen extract.

| # | modaliteit | km | naad | stijl | geometrie |
|---|---|---|---|---|---|
| b1 | truck | 13,6 | – | stippel | rechte lijn dia-ide → dia-tlv-cargo (beenregel van `diamant-ramatgan-newyork` b1) |
| b2 | lucht | 7.726,4 | 0,00 km | doorgetrokken | `maak_luchtbeen.py` TLV → HKG, 311 punten, `diamant-ramatgan-hongkong-lucht-tlv-hkg.geojson` |
| b3 | truck | 40,8 | 0,00 km | doorgetrokken | letterlijke kopie `diamant-surat-hongkong-weg-hkgcargo-hkexchange.geojson` (1.251 punten) |

Totaal 7.780,8 km (verwacht 7.780,8). Alle vier markers liggen 0,0 km van hun lijn.

- **Stippel (b1):** "hier reikt het net niet": Israel-extract ontbreekt (13,6 km hemelsbreed, geen wegkm; de ±15%-toets is indicatie). Optioneel centraal: Israel-extract via `fetch_landnet.py`.
- **Vlucht (b2):** doorgetrokken grootcirkel, aannemelijk (een bron); de beennaam zegt "aannemelijk: een bron". Het TLV-anker is landzijde, dus geen airside-stippel. De directe vlucht is historisch (§7), de lijn is de vaste vorm van de handelsstroom.
- **Kopie (b3):** letterlijk, geen tweede versie. Het HKG-anker is airside; de kopie snapt op 0,05 km via kleine wegklassen, dus geen last-mile-stippel. Bevinding blijft bij `diamant-surat-hongkong`: +25,8% op de via-puntensom, en `toets_knikken` meldt in dit been 15 knikken, waarvan een terugloop van 162 graden bij 22.3636,114.1191 (Kwai Chung, 4 m) en spikes bij de Western Harbour Crossing-aansluiting. Niet gerepareerd (andermans been).
- **Geen haven-aanloop, geen leiding:** de keten heeft geen zee- of leidingbeen.
- **Recept:** drie `hecht_marnet.py route`-regels (stippel, twee `--been-geojson`), vier `--marker`; zwaar-slot genomen en vrijgegeven.
- **Lessen:** een keten van twee kopieën plus één nieuwe grootcirkel bakt in één run zonder scans; het b3-been heet in de brief en het geojson b4 van `diamant-surat-hongkong` (het ontwerp noemde b5).

