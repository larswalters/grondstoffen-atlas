# Routebrief (licht) · diamant — Dubai (DMCC) → DXB → Hong Kong (HKG) → Hong Kong Diamond Exchange (Verenigde Arabische Emiraten → Hongkong)

**stroom-id:** `diamant-dubai-hongkong` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Keten in één zin:** ruwe/gepolijste diamant van de Dubai Diamond Exchange (DMCC, Almas Tower, JLT) per truck naar de DXB-vrachtterminal, als
vrachtvlucht (grootcirkel DXB → HKG, **aannemelijk: handelsstroom gebrond, vlucht niet**) naar de Cathay Pacific Cargo Terminal van Hong Kong
International, en per truck via de North Lantau Highway en de Tsing Ma Bridge naar het Hong Kong Diamond Exchange Building in Central.
**Welke as van het verhaal:** *Dubai → Hongkong: de Golf-tak naar de Aziatische beurs.* Geen Mct-cijfer gevonden. Gedocumenteerd is de **waarde**: VAE-export
HS 7102 in 2023 naar Hongkong **2,15 mld USD = 11,1%**, derde bestemming na India (8,99 mld) en België (3,29 mld) [1]. Rough en polished zijn niet gesplitst
(Dubai totaal 2022: 37,4 mld USD [2]). Het v1-getal 3 Mct/j (`dia-dubai → dia-china-cut`) gaat naar een Chinese slijperij, niet naar Hongkong, en hoort hier niet
[7]. Eenheid Mct/j = miljoen karaat per jaar; de waarde per karaat zit niet in het gewicht. Risico: de Hongkongse vraag is teruggevallen sinds ~2022 [7].

## 1 · Ketenkaart
```
DMCC / Almas Tower `dia-dmcc-almas` ──(b1 truck · Sheikh Zayed Road E11 → Airport Road · letterlijke kopie diamant-dubai-surat b1 · 31,2 km)──►
DXB-vrachtterminal (Cargo Village) `dia-dxb-vracht` ──(b2 lucht · vlucht DXB → HKG, grootcirkel, aannemelijk · 5.923,3 km)──►
Cathay Pacific Cargo Terminal, Chek Lap Kok `dia-hkg-cargo` ──(b3 truck · North Lantau Hwy → Tsing Ma → Kwai Chung → Western Harbour Crossing · letterlijke kopie diamant-surat-hongkong b4 · 40,8 km)──►
Hong Kong Diamond Exchange Building, Central `dia-hk-exchange` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | DMCC/Almas Tower → DXB-vrachtterminal | Sheikh Zayed Road (E11) → Airport Road; **letterlijke kopie** (niet omgekeerd, het bestand loopt al DMCC → DXB) van `diamant-dubai-surat` b1 (ook in `-dubai-antwerpen`, `-dubai-ramatgan`) | hemelsbreed 29,0 km, geen wegkm (gebakken kopie 31,2 km, +7,6% t.o.v. hemelsbreed als indicatie) [8] | kopie geojson | nee |
| b2 | C | lucht | DXB-vrachtterminal → Cathay Pacific Cargo Terminal (HKG) | vlucht DXB → HKG (vrachtvlucht, grootcirkel), aannemelijk: handelsstroom gebrond, vlucht niet | 5.923,3 grootcirkel [berekend, `maak_luchtbeen`, proefrun 238 punten] | maak_luchtbeen | nee — doorgetrokken |
| b3 | C | truck | Cathay Pacific Cargo Terminal (HKG) → Hong Kong Diamond Exchange Building | North Lantau Highway → Tsing Ma Bridge → Kwai Chung Interchange → Western Harbour Crossing; **letterlijke kopie** (richting HKG → exchange) van `diamant-surat-hongkong` b4 (ook in `-ramatgan-hongkong` b3) | 40,8 km kopie, **geen gepubliceerde wegkm**; hemelsbreed 24,0 km, geen wegkm [berekend] [9] | kopie geojson | nee |

Geen zeebeen (dus geen haven-aanloop), geen leiding, geen spoor, geen nieuw wegprofiel. Het DXB-platform ligt airside, maar het gekopieerde wegbeen eindigt 0,22 km van het
anker op de openbare weg en het HKG-wegbeen begint 0,05 km van het anker (kleine wegklassen-aanloop 0,98 km): geen airside-last-mile-stippel nodig (anders dan
`goud-loulo-ticino`). De ±15%-toets geldt voor b1 en b3 niet als norm: alleen hemelsbreed, geen echte wegkm.

## 3 · Ankers (alle vier HERGEBRUIKT letterlijk, niet opnieuw gelegd)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `dia-dmcc-almas` | handelshub / vertrek | DMCC/Dubai Diamond Exchange, Almas Tower, JLT | 25.0689, 55.1412 | [3][8] (`diamant-dubai-surat`) | bron-gelegd (daar z15 gezien: 68-verdiepingentoren in het JLT-hoogbouwcluster aan de Sheikh Zayed Road) |
| `dia-dxb-vracht` | overslag truck → lucht | DXB Cargo Village / SkyCargo-loodsen, Al Garhoud (DXB) | 25.2574524, 55.3405972 | [4][8] (`diamant-dubai-surat`) | bron-gelegd (daar z15 gezien: rij vrachtloodsen en apron NW van de terminals) |
| `dia-hkg-cargo` | overslag lucht → truck | Cathay Pacific Cargo Terminal, Chek Lap Kok (HKG) | 22.2975, 113.9247 | [5][9] (`diamant-surat-hongkong`) | bron-gelegd (daar z15 gezien: apart vrachtgebouwencomplex met loodsen aan het platform, wide-body vrachttoestellen op het apron) |
| `dia-hk-exchange` | beurs-/handelsgebouw / bestemming | Hong Kong Diamond Exchange Building, 20 Ice House Street, Central | 22.2797, 114.1570 | [9] (`diamant-surat-hongkong`; OSM-landuse) | bron-gelegd (daar z16 gezien: dicht bouwblok in Central bij het havenfront, geen eigen terrein te onderscheiden) |

Geen nieuwe satellietblik: de coördinaten staan letterlijk op de bron-briefs (beelden `v2/build-cache/satcheck/sat-diamant-dubai-surat-{dmcc-almas,dxb-vracht}.png`,
`sat-diamant-surat-hongkong-{hkg-vracht,hk-diamantbeurs}.png`); niets verschoven. Luchthaven-IATA: DXB = Dubai International, HKG = Hong Kong International.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | — | geen | — | één doorgaande stadsweg, letterlijke kopie; geen nieuw profiel |
| b3 | 1–4 | North Lantau Highway · Tsing Ma Bridge · Kwai Chung Interchange · Western Harbour Crossing (HK-portaal) | 22.3143,113.9924 · 22.3514,114.0742 · 22.3667,114.1250 · 22.3014,114.1567 | letterlijke kopie, geen nieuw profiel; zie `diamant-surat-hongkong.md` §4 (enige snelwegcorridor van de luchthaven, enige tunnel naar Hong Kong Island) |
Geofabrik-regio's: geen nieuwe scan (b1 `gcc-staten` en b3 `china` zijn al gebakken in de bronstromen).

## 5 · Verwerkingsknopen
Geen fysieke bewerking onderweg: DMCC is veiling/handel [3]; de Cathay-terminal is overslag en beveiliging; het Hong Kong Diamond Exchange Building is handelsgebouw.
Het slijpen/polijsten gebeurt buiten deze keten.

## 6 · Stoppunt
De brief stopt bij het Hong Kong Diamond Exchange Building: het eindpunt uit het ketenontwerp en een handelsgebouw; geen bron koppelt déze Dubai-lading aan een
individuele juwelier of fabriek — fase D en E vervallen.

## 7 · Open punten
- **Geen bron voor een vlucht DXB → HKG met diamant.** Gebrond is de handelsstroom (Hongkong 11,1%, 2,15 mld USD, 2023 [1]); voor Emirates SkyCargo is alleen een
  vrachtdienst in de omgekeerde richting gevonden (Hong Kong → Delhi → Dubai, 777F, start juni 2016; "18 vrachtvluchten Hong Kong → Dubai" zonder periode, geen diamant genoemd [6]).
  Eén directe vlucht aangenomen; een tussenlanding (bv. Delhi) is niet uitgesloten. In de beennaam staat daarom "aannemelijk: handelsstroom gebrond, vlucht niet" (precedent `diamant-dubai-ramatgan`).
- **DXB of DWC:** Emirates SkyCargo's vrachttoestellen vlogen vanuit Al Maktoum (DWC) en de vrachtafhandeling verhuisde in april 2020 naar DXB [10]; welk Dubai-veld deze lading
  gebruikt is onbekend. DXB-anker blijft consistent met de overige Dubai-ketens (`-dubai-surat`, `-dubai-ramatgan`, `-dubai-antwerpen`).
- **Volume:** geen karaatcijfer. Centraal te kiezen: een natte-vinger-gewicht of alleen de dollarwaarde (2,15 mld USD, 2023) tonen. Het v1-getal `dia-dubai → dia-china-cut` (3 Mct/j) hoort bij een Chinese slijperij.
- **Eigen km-correcties t.o.v. het ketenontwerp:** b3 is 40,8 km (kopie), niet "ca. 35"; hemelsbreed 24,0 km. Geen gepubliceerde wegkm voor b1 of b3.
- **Geërfde bevindingen van de kopie b3** (uit `diamant-surat-hongkong`): +25,8% t.o.v. de via-puntensom en 15 knikken, waaronder een terugloop van 162 graden bij Kwai Chung; noot, geen reparatie (kopie is bewust, één lijn per grondstof).
  Idem b1: 6 knikken in de JLT/Al Garhoud-bochten.
- **Vraagval Hongkong sinds ~2022** en de Iran-oorlog 2026 (verstoring DMCC en vluchten) zijn niet in de lijn verwerkt; de kaart toont de vaste vorm. Rough/polished niet gesplitst.
- Het HKG-anker ligt op terminalniveau; welk pand diamant afhandelt is niet onderzocht.

## 8 · Bronnen
[1] Trendeconomy, UAE export HS 7102 (diamant) 2023: India 8,99 mld (46%), België 3,29 mld (17%), Hongkong 2,15 mld (11,1%), VS 1,66 mld, Israël 799 mln. https://trendeconomy.com/data/h2/UnitedArabEmirates/7102
[2] Rapaport, 19 feb 2023, "Dubai Diamond Trade Sees Further Growth" (2022: 37,4 mld USD, +17%; rough +7%, polished +42%; geen bestemmingen). https://rapaport.com/news/dubai-diamond-trade-sees-further-growth/
[3] Wikipedia, "Dubai Multi Commodities Centre" (Almas Tower, Dubai Diamond Exchange; via brief `diamant-dubai-antwerpen` [3]). https://en.wikipedia.org/wiki/Dubai_Multi_Commodities_Centre
[4] Wikipedia, "Dubai International Airport" (Cargo Village; via brief `diamant-dubai-antwerpen` [4]). https://en.wikipedia.org/wiki/Dubai_International_Airport
[5] Wikipedia, "Hong Kong International Airport" (wereldwijd drukste vrachtpoort; Emirates gebruikt Hong Kong als tussenstop). https://en.wikipedia.org/wiki/Hong_Kong_International_Airport
[6] MaltaToday, "Emirates SkyCargo launches new Hong Kong-Delhi freighter service" (EK 9219, 777F, 1 juni 2016, wekelijks; HK "world's top cargo hub"). http://www.maltatoday.com.mt/business/business_news/65971/emirates_skycargo_launches_new_hong_kongdelhi_freighter_service
[7] v1 `data/diamond.js` + `design/diamant.md` §4 (flow `dia-dubai → dia-china-cut` 3 Mct, geen Dubai → Hongkong; `dia-mkt-china` teruggevallen sinds ~2022) — intern.
[8] Brieven `diamant-dubai-surat` (ankers + b1) en `diamant-dubai-ramatgan` (zelfde b1-kopie, zelfde vlucht-formulering); bestand `v2/build-cache/ais/graaf/diamant-dubai-surat-weg-dmcc-dxb.geojson` (406 punten, 31,2 km, FeatureCollection).
[9] Brief `diamant-surat-hongkong` (ankers `dia-hkg-cargo`, `dia-hk-exchange`, b4; OSM/Photon 22.2975/113.9247 en 22.2797/114.1570) en `diamant-ramatgan-hongkong` (b3-kopie); bestand `…/diamant-surat-hongkong-weg-hkgcargo-hkexchange.geojson` (1.251 punten, 40,8 km).
[10] Wikipedia, "Emirates SkyCargo" (vrachttoestellen vanuit Al Maktoum DWC; afhandeling naar DXB in april 2020; 20 okt 2025 ongeval 747-vrachttoestel in Hong Kong). https://en.wikipedia.org/wiki/Emirates_SkyCargo
[11] `maak_luchtbeen.py` DXB → HKG: 5.923,3 km, 238 punten (proefrun 2026-11-01, scratchpad, niet in build-cache). Eigen berekening.
[12] DMCC, Dubai Diamond Exchange (Almas Tower). https://www.dmcc.ae/ (zoals in het ketenontwerp; hier niet geopend).

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
Bestand `v2/data/stroomroute-diamant-dubai-hongkong.json`, 39,5 KB, 3 benen, 4 markers, 1.895 punten, 5.995,3 km totaal, contract versie 2 (lonlat). Functie `bak_diamant_dubai_hongkong` in `bak_stromen.sh`; geen profiel, geen wegscan, geen zee, geen haven-aanloop.

| # | modaliteit | gebakken km | brief | punten | stippel |
|---|---|---|---|---|---|
| b1 | truck | 31,2 | hemelsbreed 29,0 km, geen wegkm (+7,6%, indicatie) | 406 | nee |
| b2 | lucht | 5.923,3 | 5.923,3 grootcirkel | 238 | nee, doorgetrokken |
| b3 | truck | 40,8 | 40,8 kopie, hemelsbreed 24,0 km, geen wegkm | 1.251 | nee |

**Markers** (alle vier op de brief-coordinaten): dia-dmcc-almas 0,02 km van de lijn, dia-dxb-vracht 0,00 km, dia-hkg-cargo 0,00 km, dia-hk-exchange 0,00 km. **Naden:** b1 naar b2 0,00 km, b2 naar b3 0,00 km (geen naad > 5 km).

**Recept:** b1 en b3 zijn letterlijke kopieen (`--been-geojson`, geen herberekening): `diamant-dubai-surat-weg-dmcc-dxb.geojson` (niet omgekeerd) en `diamant-surat-hongkong-weg-hkgcargo-hkexchange.geojson`. b2 via `python v2/tools/maak_luchtbeen.py --van "DXB-vrachtterminal|25.2574524,55.3405972" --naar "Cathay Pacific Cargo Terminal HKG|22.2975,113.9247"` naar `diamant-dubai-hongkong-lucht-dxb-hkg.geojson` (FeatureCollection). Geen stippels: het DXB-wegbeen eindigt 0,22 km van het anker en het HKG-wegbeen begint 0,05 km ervan, dus geen airside-last-mile.

**Toelichting vlucht:** doorgetrokken grootcirkel, aannemelijk (handelsstroom gebrond, vlucht niet, zie §7); "aannemelijk" staat in de beennaam, niet in de lijnstijl.

**Toetsen:** `toets_knikken.py`: b1 6 knikken (spikes in de JLT/Al Garhoud-bochten), b2 0, b3 15 knikken waarvan 1 terugloop van 162 graden bij Kwai Chung (22.3636, 114.1191), geerfd van de bronkopie, bewust niet gerepareerd (een lijn per grondstof). `toets_rechte_benen.py --min-km 5`: geen regel voor deze stroom (luchtbeen overgeslagen). JSON: versie 2, punt_formaat lonlat, modaliteiten {truck, lucht}, elk been >= 2 punten.

**Lessen:** een stroom van alleen kopieen plus een grootcirkel bakt zonder net, slot of wegscan; de kopie-ankers snappen op 0,00 km. De geerfde kwaliteitsbevindingen van b3 (+25,8% op de via-puntensom, terugloop Kwai Chung) komen mee en horen bij de bronstroom diamant-surat-hongkong.
