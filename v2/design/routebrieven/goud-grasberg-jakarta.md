# Routebrief (licht) · goud — PTFI Manyar-PMR (Gresik) → Antam Logam Mulia (Pulogadung, Jakarta), Indonesië

**stroom-id:** `goud-grasberg-jakarta` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken (2026-10-09)
**Keten in één zin:** goudbaren (99,99%) uit de Precious Metal Refinery (PMR) van PT Freeport Indonesia in het JIIPE-complex bij
Gresik, per truck (aannemelijk: vervoerswijze niet gebrond) over de Trans-Java-tolweg naar de Antam Logam Mulia-vestiging in
Pulogadung (Jakarta Timur). **Eén been** — ingekort van 6 benen tot het enige gebronde stuk (haalbaarheidstoets, bindend).
**Welke as van het verhaal:** *Indonesische downstreaming van goud* — Freeport-goud (bijproduct van Grasberg-koper) wordt
sinds 2025 in Indonesië zelf geraffineerd en aan staatsbedrijf Antam geleverd. **Volume: 24–28 t Au/j** (Freeport-raming voor
2025, president-directeur, Republika 26-02-2025 [2]); contract Freeport→Antam tot **30 t Au/j** (5 jaar, US$ 12,5 mrd) [1]; PMR-capaciteit
≈ 50 t Au/j [1]. Peiljaar 2025; 2026 ligt lager na de modderstroom van 08-09-2025 (zie koper-grasberg-manyar §1). Eerste levering 12-02-2025: 125 kg [3][4].

## 1 · Ketenkaart
```
PTFI Manyar-PMR (JIIPE, Gresik) `au-pmr-manyar`
  ──(b1 truck · Trans-Java-tolweg Gresik–Mojokerto–Ngawi–Kartasura–Semarang–Pemalang–Cipali–Cikampek · ≈760 wegkm [7], hemelsbreed 640)──►
Antam Logam Mulia, Pulogadung (Jakarta Timur) `au-antam-pulogadung` ── stoppunt
```
Niet getekend (bewust): Grasberg-mill → Portsite → Manyar. Dat is dezelfde lading als **koper-grasberg-manyar** (concentraat,
nog geen goud) en staat daar al als gemeten keten (leiding 89,6 km stippel + aanloop 53,2 + MARNET-zee 2.816,7 + aanloop 6,7 +
eigen terrein 2,6); een goud-kopie zou dezelfde lijn nogmaals leggen en baren suggereren waar concentraat reist.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | PTFI Manyar-PMR → Antam Pulogadung | Trans-Java-tolweg: Surabaya–Mojokerto → Kertosono–Ngawi → Solo–Ngawi → Kartasura–Semarang → Semarang–Batang → Pejagan–Pemalang → Cikopo–Palimanan → Jakarta–Cikampek → JORR/Cawang | **760 wegkm Jakarta–Surabaya via tol** [7] (BPJT/Jasa Marga; eindpunten wijken af: Gresik ligt ~20 km voorbij Surabaya, Pulogadung ~20 km vóór Jakarta-centrum) — dus **indicatie, geen harde ±15%-norm**; hemelsbreed 639,8 km (berekend), via-puntensom 699,8 km | maak_stroombeen_weg (extract indonesie, `--bron overpass`) | nee — doorgetrokken |

**Aannemelijk: één bron voor de bestemming, vervoerswijze niet gebrond.** Bisnis (13-02-2025) en Antara melden alleen dat de
125 kg naar Antam "in Pulogadung, Jakarta" ging [3][4]; Republika, Indonesia Business Post en Antara noemen geen transportmethode [1][2][4].
Een vlucht SUB→CGK is het alternatief en wordt niet getekend (geen bron). Beennaam: *vrachtwagen PTFI Manyar-PMR (Gresik) → Antam Logam Mulia (Pulogadung), aannemelijk: vervoerswijze niet gebrond*.

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-pmr-manyar` | laadplek / verwerkingsknoop | PTFI Manyar-smelter + PMR, KEK JIIPE, Gresik | -7.0890, 112.6270 | **hergebruikt letterlijk** `cu-manyar-smelter` uit koper-grasberg-manyar §3 [5][1] | bron-gelegd als terreinanker (koperbrief); zelf opnieuw gezien op z15 (`sat-goud-grasberg-jakarta-pmr.png`): groot smelterperceel aan de oostkust van JIIPE tussen spoorbundel en kust, kruis op een kaal, gestreept perceeldeel; het PMR-gebouw zelf is **niet aanwijsbaar** (PMR ligt volgens [1] "in het kopersmeltcomplex") |
| `au-antam-pulogadung` | losplek / afnemer | PT Aneka Tambang (Antam) UBPP Logam Mulia, Pulogadung | -6.1916, 106.9051 | [3][4][6][osm] | **aannemelijk** (z16 + z17 gezien: `sat-goud-grasberg-jakarta-antam-z16.png`, `…-antam-poly.png` — compact industriecompound met lange witte loodsen aan een kanaal en een ringweg midden in dicht stedelijk weefsel, groter loodsterrein direct oostwaarts over de weg; OSM-landuse "Aneka Tambang", way 155950968, 0,96 ha, kelurahan Jatinegara Kaum/Pulo Gadung, het punt is het representatieve punt ín die polygoon) |

## 4 · Via-punten (b1, volgorde van reizen; alle punten zijn middenpunten van OSM-`highway=motorway`-ways met `Jalan Tol …`-naam, via Photon)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Jalan Tol Surabaya–Mojokerto, Canggu (Mojokerto) | -7.4259, 112.4499 | Gresik→Mojokerto via de tol, niet via Pantura of de Jombang-wegen; Mojokerto-stadscentrum ligt ~6 km verder |
| b1 | 2 | Jalan Tol Solo–Ngawi, Ngawi | -7.4138, 111.4015 | sluit de zuidelijke Madiun/Solo-tolcorridor vast (sluit Pantura-noord uit); W1557886230 |
| b1 | 3 | Jalan Tol Semarang–Solo, Trayu (Kartasura) | -7.5229, 110.7058 | de tol knoopt hier Solo–Ngawi aan Semarang–Solo; sluit de Yogyakarta-afslag uit; W750686324 |
| b1 | 4 | Jalan Tol Semarang–Batang, westrand Semarang | -6.9992, 110.3633 | ná Semarang door op de kust-tol (geen Pantura-binnenweg); buiten het stadscentrum (Ngaliyan-kant) |
| b1 | 5 | Jalan Tol Pejagan–Pemalang, Jebed Selatan | -6.9310, 109.4090 | pint Pemalang–Brebes-corridor op de tol i.p.v. de Pantura-weg |
| b1 | 6 | Jalan Tol Cikopo–Palimanan, Gempol | -6.6899, 108.3958 | de Cipali-route (West-Java) in plaats van de kustweg via Cirebon-centrum |
| b1 | 7 | Jalan Tol Jakarta–Cikampek, Kamojing | -6.4322, 107.4485 | laatste keuzepunt: Jakarta–Cikampek-tol (niet de Cikampek-binnenweg) |
Eerste en laatste punt zijn de ankers (§3). Geen via-punt in een stadscentrum; tussen de via-punten kiest de router vrij over
het tolnet. Venster: ≈ 50 km om ankers → via-punten. Refs: leeg (Jalan Tol-namen).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| PMR (Manyar/JIIPE) | PT Freeport Indonesia | anodeslijk → goudbaar 99,99% (+ zilver, Pt, Pd) | ≈ 50 t Au, 200 t Ag, 30 kg Pt, 375 kg Pd per jaar; ingehuldigd 17-03-2025 | [1] |
| Antam UBPP Logam Mulia (Pulogadung) | PT Aneka Tambang | goudbaar → LBMA-baren/muntjes (afnemer; LBMA-geaccrediteerd) | afname tot 30 t Au/j onder het contract van 07-11-2024 | [1][2][6] |

## 6 · Stoppunt
De brief stopt aan de Antam-vestiging in Pulogadung: één bron noemt Antam als afnemer in Pulogadung [3][4], en wat Antam daarna aan
kluizen/handelaren/juweliers levert is niet gebrond. Fase E vervalt.

## 7 · Open punten
- **Haalbaarheidstoets bindend verwerkt:** niet bij Grasberg beginnen en geen kopie-benen van koper-grasberg-manyar; Grasberg-goud (≈ 55 t Au/j bijproduct, FCX 2024) reist al als concentraat over die gemeten koperketen (Grasberg blijft als site in `goud-sitelaag`).
- **Het id `goud-grasberg-jakarta` is bewust gehouden (id-regel golf 7)**, terwijl het werkelijke beginpunt PTFI Manyar-PMR is; eerlijker was `goud-manyar-jakarta`. Titel en beennaam noemen het werkelijke traject; de centrale registratie kan de sleutel/het label kiezen.
- **Vervoerswijze niet gebrond** (truck aannemelijk; vlucht SUB→CGK denkbaar). **Wegkm niet voor déze eindpunten gebrond:** 760 km is Jakarta–Surabaya via tol [7]; hemelsbreed 640 km. De bake-km wordt een bevinding, geen fout.
- **Feedstock-nuance:** de eerste baren (30-12-2024; levering 12-02-2025) kwamen uit 12,56 t anodeslijk van PT Smelting (Roomo) → 189 kg Au, 125 kg op 99,99% [1][3]; PTFI's eigen Manyar-smelter had brand op 14-10-2024 en voert sinds aug/sep 2026 weer. PMR-voeding en -locatie binnen het terrein onzeker.
- **Antam-anker:** OSM-polygoon van 0,96 ha is klein; of precies déze plek de refinery is (en niet het Graha Dipta-verkooppunt of kantoor) is niet bevestigd, en een straatadres van de UBPP is niet gevonden (Jalan Pemuda niet bevestigd). Het eindpunt kan verschuiven: Antam bouwt een eigen fabriek in JIIPE Gresik, productie gericht op Q4 2027 (Bisnis 16-07-2025, via zoekresultaat — pagina gaf 403; Kontan [6]).
- **Bake-risico:** Overpass was op 2026-10-09 onbereikbaar (drie mirrors: leeg of HTTP 500) en `pyosmium` is geblokkeerd → de weg-scan van b1 (≈ 750 km, extract indonesie) kan pas draaien als Overpass terug is; er staat geen Java-wegcache op schijf. Eventueel in 2–3 deelprofielen splitsen (per Jakarta–Cikampek / Semarang / Mojokerto-blok), met één gedeeld via-punt als naad.
- JIIPE-estatewegen staan vermoedelijk niet allemaal in OSM (koperbrief §7): `eindToegangPrivaat: True`; ligt het net > ~2 km van het anker → stippel "last mile (geen net op deze korrel)" aan de PMR-kant.
- Jaarvolume uitsluitend als raming/contract; werkelijk 2025-volume nog niet gebrond.

## 8 · Bronnen
[1] Indonesia Business Post, 17-03-2025 — PMR Gresik ingehuldigd (JIIPE, Manyar-smeltercomplex): ≈ 50 t Au/j, 200 t Ag; levering 12-02-2025 125 kg uit 12,56 t anodeslijk; Antam-contract tot 30 t/j, 5 jaar, US$ 12,5 mrd. https://indonesiabusinesspost.com/3937/national-resilience/president-inaugurates-freeports-precious-metal-refinery-facility-in-gresik
[2] Republika, 26-02-2025 — Freeport raamt 24–28 t Au aan Antam in 2025; contract 30 t/j; geen transportwijze. https://ekonomi.republika.co.id/berita/ssaj9f370/freeport-perkirakan-suplai-28-ton-emas-ke-antam-pada-2025
[3] Bisnis.com, 13-02-2025 — "Perdana, Freeport Kirim 125 Kg Emas Batangan ke Antam" (levering in Pulogadung, Jakarta; gelezen via zoekresultaat — 403 op directe fetch). https://ekonomi.bisnis.com/read/20250213/44/1839196/perdana-freeport-kirim-125-kg-emas-batangan-ke-antam
[4] Antara Papua, 13-02-2025 — 125 kg ter waarde van Rp 207 mrd naar Antam in Pulogadung, uit de PMR van PTFI; geen transportwijze. https://papua.antaranews.com/berita/737653/pt-freeport-indonesia-kirim-emas-batangan-perdana-senilai-rp207-miliar-ke-antam
[5] `v2/design/routebrieven/koper-grasberg-manyar.md` — ankers `cu-manyar-smelter`, `cu-manyar-kade`, bronnen [6][13][17] aldaar.
[6] Kontan — Antam bouwt Logam Mulia-fabriek in Gresik/JIIPE (uitbreiding van UBPP Logam Mulia; gelezen via zoekresultaat). https://industri.kontan.co.id/news/antam-antm-bangun-pabrik-pengolahan-logam-mulia-di-gresik
[7] detikFinance, 2018 — "Perjalanan Tol Trans Jawa akhirnya nyambung dari JKT sampai SBY": Jakarta–Surabaya via tol 760 km (BPJT/Jasa Marga). https://finance.detik.com/infrastruktur/d-4351951/perjalanan-tol-trans-jawa-akhirnya-nyambung-dari-jkt-sampai-sby
[osm] OpenStreetMap (ODbL) via Nominatim/Photon — landuse "Aneka Tambang" way 155950968 (representatief punt -6,1916167/106,9051486); `Jalan Tol`-motorwayways: Surabaya–Mojokerto W676507836 · Solo–Ngawi W1557886230 · Semarang–Solo W750686324 · Semarang–Batang W794262069 · Pejagan–Pemalang W1038587969 · Cikopo–Palimanan W475450437 · Jakarta–Cikampek W1414042421. https://www.openstreetmap.org
[v1/sitelaag] `v2/design/goud-sitelaag.json` (Grasberg 55 t Au/j, FCX 2024) en `data/goud.js`.
Satellietblik (Esri z15–z17, 2026-10-09): `v2/build-cache/satcheck/sat-goud-grasberg-jakarta-antam.png`, `…-antam-z16.png`, `…-antam-poly.png`, `…-pmr.png`.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Status: gebakken** — `v2/data/stroomroute-goud-grasberg-jakarta.json` (versie 2, lonlat, 156,9 KB), 1 been, 780,5 km, 7.702 punten, 2 markers. Stroom-id `goud-grasberg-jakarta` klopt met het eindpunt (Jakarta); het beginpunt is PTFI Manyar-PMR (Gresik), zoals de brief al zei.

| # | modaliteit | been | km | punten | stippel? |
|---|---|---|---|---|---|
| b1 | truck | vrachtwagen PTFI Manyar-PMR (Gresik) → Antam Logam Mulia (Pulogadung), aannemelijk: vervoerswijze niet gebrond | **780,5** | 7.702 | nee — doorgetrokken |

Segmenten (via-punt → via-punt, km uit de scan): anker PMR → Canggu 54,1 · → Ngawi 133,0 · → Trayu/Kartasura 86,6 · → westrand Semarang 84,3 · → Jebed Selatan (Pejagan–Pemalang) 110,3 · → Gempol (Cipali) 124,1 · → Kamojing (Jakarta–Cikampek) 115,8 · → Antam 72,0. Alle zeven via-punten snappen binnen 0,08 km op de tol-ways (geen punt > 5 km, geen omweg: elk segment is 1,04–1,28 × hemelsbreed); de ankers snappen op 0,32 km (PMR) en 0,01 km (Antam).
**Toets.** (1) Lengte: 780,2 km (scan) / 780,5 km (getekende lijn) tegen de ~760 wegkm Jakarta–Surabaya via tol [7] = **+2,7%** — binnen ±15%, maar zoals in §2 een indicatie: de 760 km hoort bij andere eindpunten (Gresik ligt ~20 km voorbij Surabaya, Pulogadung ~20 km vóór Jakarta-centrum), dus de ruim 20 km extra is verklaarbaar. (2) Naden: één been, dus geen naad; markers liggen 0,0 km van de lijn. (3) `toets_knikken`: 53 knikken ≥ 60°, 2 omkeringen ≥ 150°: een 169°-terugloop bij -6.53069,107.78127 (een ~90 m lange stub in een afrit bij Subang, ruim onder de snoeidrempel van 25 m radius) en een 168° "scherpe bocht, echt" bij -6.94707,109.69769 (~100 m, Pejagan–Pemalang-afrit); de overige zijn spikes (radius ≤ ~55 m) op knooppunten, in de JIIPE-estate en in Jakarta-oost. Geen visuele fout op schaal van de bol, wel een bevinding. (4) `toets_rechte_benen --min-km 5`: b1 niet gemeld. (5) json.load OK: versie 2 · punt_formaat lonlat · modaliteit {truck} · 7.702 punten.
**Recept.** Profiel `goud-grasberg-jakarta-manyar-pulogadung` in `maak_stroombeen_weg.py` (extract `indonesie`, 9 via-punten = 2 ankers + 7 tol-via's uit §4, vensterKm 50, `eindToegangPrivaat` True, `corridorKlassen` **leeg**). Wegscan met een eigen pure-Python-PBF-lezer (`v2/build-cache/ais/graaf/goud-grasberg-jakarta-wegscan-wrapper.py`, afgeleid van de ree-larochelle-wrapper; leest alleen het databestand `indonesie-latest.osm.pbf`, laadt de geblokkeerde pyosmium-DLL niet) die `weg_houden`/`corridor_keten` van het wegtool aanroept: 130,6 mln nodes in de bbox, 589 s scan, 212.505 way-delen → 146.564 ways in het corridorvenster (waarvan 89.902 kleine-klasse-ways binnen 12 km van de ankers). Eerst eenmaal `--bron overpass` geprobeerd: weer reset/HTTP 500. Daarna `bash v2/tools/bak_stromen.sh goud-grasberg-jakarta` (`bak_goud_grasberg_jakarta`: één `--been-geojson "truck|…"`, twee markers).
**Toelichting.**
- **Stippel: geen.** Het wegnet reikt tot 0,32 km van het PMR-anker (de scan liep 7,0 km eerste mijl over `highway=service` in de JIIPE-estate, dus de estatewegen staan wél in OSM en het `eindToegangPrivaat`-pad was voldoende) en tot 0,01 km van Antam (laatste mijl 0,13 km service). Geen last-mile-stippel nodig.
- **Geen zee, geen haven-aanloop, geen vlucht, geen leiding, geen kopie** van koper-grasberg-manyar of een andere stroom (bewust, zie §1/§7).
- **Aannemelijk blijft aannemelijk:** de lijn is gemeten (doorgetrokken), maar dat de baren per truck reizen en dat Pulogadung de refinery is, rust op één bron (§2/§7); dat staat in de beennaam en niet in de lijnstijl.
**Lessen.**
1. Voor een weg-stroom door Java (of elk zwaar bemapt eiland) werkt een pure-Python-PBF-scan van de lokale extract wél, terwijl Overpass daar niet haalbaar is: 10 min voor 1,7 GB / 130 mln nodes in de bbox.
2. Voor een tol-corridor kan `corridorKlassen` leeg: de tol is `highway=motorway`, de eindzone (12 km) draagt de estatewegen. Met `tertiary/unclassified/service` corridor-breed over heel Java had de scan miljoenen extra ways in het geheugen gehouden (de wrapper schiet bovendien kleine klassen buiten de ankerboxen er vroeg uit).
3. De via-puntensom (699,8 km) onderschatte de routekm (780 km) met 11%: de tol maakt vanzelf omwegen langs de kust en rond Semarang/Cirebon die een rechte via-puntlijn niet ziet — de hemelsbreedte-som is dus geen goede voorspeller van wegkm op Java.
