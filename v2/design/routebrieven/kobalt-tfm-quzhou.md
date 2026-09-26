# Routebrief (licht) · kobalt — TFM (Fungurume, DRC) → Durban → Ningbo (China)

**stroom-id:** `kobalt-tfm-quzhou` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken · **Linear:** LAR-563 (ontwerp `kobalt-tfm-durban-quzhou`)
**Keten in één zin:** kobalthydroxide (30–40 % Co) van de TFM-plant (CMOC, Fungurume) gaat per **truck** over dezelfde Copperbelt-zuidroute als de kathode — RN39/RN1 → **Kasumbalesa** → T3/T2 → **Chirundu** → A1/A4 → **Beitbridge** → N1/N3, ~2.982 km — naar de containerkade **Durban DCT Pier 2**, en per **zeeschip** via Malakka naar de containerkade **Ningbo Beilun**; de lijn stopt daar — geen bron koppelt dit hydroxide aan een met naam genoemde afnemer, en de meest genoemde kandidaat (Huayou Quzhou) is niet aantoonbaar de koper van juist déze lading.
**Welke as van het verhaal:** de Chinese hoofdas van de Copperbelt-uitweg. DRC produceerde 207.134 t Co in kobalthydroxide in 2025 (~70 % van de mondiale mijnproductie) [6]; het exportverbod (feb–okt 2025) is vervangen door een quotum dat voor 2026 uitkomt op 87.000 t basis + 9.600 t discretionaire strategische marge = **max. 96.600 t Co** voor alle DRC-producenten samen, en in Q1 2026 was minder dan 50 % daarvan daadwerkelijk verscheept [5]. "Cobalt hydroxide … is usually sent by trucks to the South African port of Durban, where it gets sent into China for processing" [5][6] — modaliteit en haven zijn dus goed gebrond, het mijn-specifieke aandeel en de Chinese eindbestemming niet.

## 1 · Ketenkaart
```
TFM-plant Fungurume `cu-tfm-laad` ──(b1 truck · Copperbelt-zuidroute · ~2.982 km, letterlijke kopie)──► Durban DCT Pier 2 `cu-durban-kade`
  ──(b2 zee · Indische Oceaan → Malakka → Zuid-Chinese Zee → Oost-Chinese Zee · ~12.800 km, afnemer Huayou Quzhou: samenvloeiing/aannemelijk)──► Ningbo Beilun containerkade `co-ningbo-kade` ⏹ stoppunt
       ┊ (niet getekend — geen bron voor de weg China-binnenwaarts)
       ┊
  Huayou New Energy Technology (Quzhou) — raffinaderij `co-quzhou-smelter` (knoop, §5; coördinaat niet gevonden)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `cu-tfm-laad` → `cu-durban-kade` | RN39/RN1 → **Kasumbalesa** → T3/T2 → **Chirundu** → A1/A4 → **Beitbridge** → N1/N3 | 2.982 (gebakken `koper-tfm-durban`, −0,6 % t.o.v. ~3.000 [2][7]) | **letterlijke kopie** van `koper-tfm-durban` been 1 (`stroombeen-tfm-durban.geojson`), incl. de 12 via-punten uit `koper-kolwezi-durban.md` §4 — geen nieuwe wegscan | nee |
| b1a | A | zee (haven-aanloop) | `cu-durban-kade` → Durban-zeeknoop 5202 | — | 17,8 (bestaand) | **letterlijke kopie** van `aanloop-durban.geojson` | ja — MARNET reikt niet tot de kade (bestaand) |
| b2 | B | zee | Durban-zeeknoop 5202 (-29,8168, 31,1737) → Ningbo-zeeknoop 5850 (29,9758, 121,9736) | Indische Oceaan → Malakka → Zuid-Chinese Zee → Oost-Chinese Zee — **afnemer Huayou Quzhou: samenvloeiing, aannemelijk** [3][10] | ~12.800 (indicatief; kade→kade exact bij het bakken — Lobito-guide geeft alleen reistijd Durban→China 25–30 dagen [6]) | MARNET `--been "zee\|…\|-29.8168,31.1737\|29.9758,121.9736"` | nee |
| b2a | B | zee (haven-aanloop, nieuw) | Ningbo-zeeknoop 5850 → `co-ningbo-kade` | — | ~5,6 (indicatief; Beilun-containerzone, exact bij het bakken) | **nieuw**, `maak_havenaanloop.py` | ja — MARNET reikt niet tot de kade |

**Been C (China-binnenwaarts, NIET getekend):** geen bron koppelt TFM-hydroxide aantoonbaar aan Huayou Quzhou — CMOC verkoopt via handelaar IXM [2][9], en Huayou's eigen due-diligence-rapport (dat als enige de route Ningbo/Zhapu → Quzhou noemt) gaf een 403 bij het ophalen [10]. De lijn eindigt op de Ningbo-kade; Huayou Quzhou staat als losse knoop in §5 (regel "de lijn eindigt waar het bewijs eindigt").

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-tfm-laad` | mijn / laadplek (hergebruikt) | TFM hydrometallurgische plant (CMOC 80 %/Gécamines 20 %), Kwatebala, Fungurume — hydroxide-droger/bagging niet apart aangewezen | -10.5685, 26.1975 | [2][8], `koper-kolwezi-durban.md` §3 | bron-gelegd (hergebruikt anker, niet opnieuw satelliet-gecheckt) |
| `cu-durban-kade` | overslag truck → container → zeeschip (hergebruikt) | Durban Container Terminal Pier 2, noordkade (Bayhead) | -29.8790, 31.0160 | [7], `koper-kolwezi-durban.md` §3 | bron-gelegd (hergebruikt anker) |
| `co-ningbo-kade` | overslag zeeschip → (onbekend vervolg) | Beilun Container Terminal Phase 2, Ningbo-Zhoushan | 29.9353, 121.8695 | OSM/Nominatim [11], eigen `sat_check.py` [12] | **bron-gelegd** (z15 gezien: rij portaalkranen langs de pier, containerstapels en -yards direct erachter, schip aan de kade op de kruising) |
| `co-quzhou-smelter` | raffinaderij (knoop, niet gebakken) | Huayou New Energy Technology (Quzhou) Co., Ltd. — No. 18 Nianxin Road, Hi-tech Industrial Park fase II, Quzhou (Zhejiang) | **niet gevonden** | [9][10] | **onzeker/open** — MEE-emissieregister (`permit.mee.gov.cn/perxxgkinfo`) gaf deze sessie herhaald een redirect naar `errorinfo.jsp` (endpoint kennelijk weer verhuisd/anders bevraagd dan het recept beschrijft); OSM heeft geen naam-tag voor dit adres. Coördinaat niet verzonnen — blijft open. |

Bestaande via-ankers hergebruikt zonder wijziging: Kasumbalesa (-12.2658, 27.7959) en Beitbridge (-22.2244, 29.9865) — zie `koper-kolwezi-durban.md` §4.

## 4 · Via-punten
Been b1 hergebruikt **alle 12 via-punten** van `koper-kolwezi-durban.md` §4 ongewijzigd (Likasi, Lubumbashi, Kasumbalesa, Ndola, Kabwe, Lusaka, Chirundu, Harare, Masvingo, Beitbridge, Polokwane, Buccleuch) — zelfde corridorkeuzes, zelfde bron (OSM-node-id's + de gebakken M25-corridor). Been b2/b2a zijn zeebenen (router, geen via-punten). Er is geen been C getekend, dus geen Chinese via-punten.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| TFM, Kwatebala-plant (Fungurume) | CMOC 80 % / Gécamines 20 % | koper- én kobalterts → SX-EW-kathode + kobalthydroxide (30–40 % Co) als bijproduct | onderdeel van DRC 207.134 t Co (hydroxide) 2025; TFM/CMOC-aandeel niet apart gevonden deze sessie (open punt) | [2][6] |
| Ningbo Beilun containerkade | Ningbo Zhoushan Port Group | overslag zeeschip → onbekend vervolgtransport | containerterminal, meerdere fasen | [11][12] |
| Huayou New Energy Technology (Quzhou) — **knoop, niet aan een been gekoppeld** | Zhejiang Huayou Cobalt Co., Ltd. | kobalttussenproduct → sulfaat/tetroxide + precursor op hetzelfde park | ordegrootte enkele tienduizenden t Co/j (WoodMac-rapporttitel bevestigt de raffinaderij; capaciteitscijfer niet zelf uit de bron gehaald, paywall) [9] | [8][9] |

## 6 · Stoppunt
De brief stopt op de Ningbo-kade (`co-ningbo-kade`): het vervolgtransport naar een naam-en-adres-fabriek is niet gebrond. Huayou Quzhou is de meest waarschijnlijke afnemer op marktschaal (grootste Chinese kobaltraffinaderij [4][9]), maar (a) CMOC verkoopt TFM-hydroxide via de handelaar IXM, niet rechtstreeks [2][9], (b) het enige document dat een Ningbo/Zhapu → Quzhou-truckroute noemt (Huayou's eigen due-diligence-rapport) was deze sessie niet op te halen (403) [10], en (c) het alternatief met gesloten eigendom (Huayou's eigen CDM-plant bij Lubumbashi → Durban → Zhapu/Ningbo → Quzhou) ligt sinds de dambreuk van 2025-11-06 geschorst, status 2026 onbekend [13]. Fase D vervalt dus niet — hij staat als losse knoop in §5 — maar wordt niet getekend.

## 7 · Open punten
- **Afnemer niet gebrond:** geen bron koppelt TFM-hydroxide aan Huayou Quzhou specifiek; behandel als "aannemelijk: samenvloeiing" in de beennaam (§2), niet als vaststaand.
- **Huayou Quzhou-coördinaat ontbreekt:** het MEE-emissieregister (normaal de eerste bron voor Chinese fabrieksadressen, zie `zoek-chinees-adres-recept.md`) gaf deze sessie een dode/verhuisde endpoint-route (`permit.mee.gov.cn/perxxgkinfo/...` → 302 naar `errorinfo.jsp`); OSM heeft geen naam-tag. Vraagt een nieuwe poging (het endpoint verhuist vaker, zie het recept) of een Chinese lokale EIA-bron.
- **Ningbo-anker:** Beilun Container Terminal Phase 2 gekozen boven het bestaande `cu-beilun-ertsberth`-anker (dat is bulk/erts, niet container — expliciet niet bruikbaar volgens het ontwerp) en boven Meishan/Zhapu (verder van de zeeknoop, minder goed gedekt). Welke fase/terminal het hydroxide werkelijk gebruikt is niet gebrond — anker op containerhaven-niveau.
- **Jaarvolume dubbelzinnig:** DRC-brede mijnproductie (207 kt Co 2025) ≠ het nationale exportquotum (max. 96,6 kt Co in 2026, en Q1 2026 liep <50 % vol) ≠ TFM/CMOC's eigen aandeel (niet gevonden). De kaart tekent de weg, niet het volume.
- **Zeeroute-lengte:** ~12.800 km is een schatting; de exacte kade-tot-kade-afstand volgt pas uit MARNET bij het bakken.
- **Ningbo-haven-aanloop:** nog niet gemeten (`maak_havenaanloop.py` moet nog draaien; indicatie ~5,6 km).
- **CDM-alternatief (Lubumbashi → Zhapu/Ningbo → Quzhou):** geschorst sinds de dambreuk van 2025-11-06; als de schorsing in 2026 wordt opgeheven, ontstaat een sterker onderbouwd tracé dan de huidige IXM-samenvloeiing — herzien zodra er nieuws is.

## 8 · Bronnen
[1] USGS, Mineral Commodity Summaries 2026 — Cobalt, https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-cobalt.pdf
[2] CMOC Group, "The DRC – copper and cobalt" (TFM 80 %/KFM 71,25 %-belang; "a world-leading cobalt producer"), https://en.cmoc.com/html/Business/Congo-Cu-Co/
[3] Lobito Corridor, "Cobalt Supply Chain Explained" — routetabel Durban ~3.000 km/30–45 dagen; "Most cobalt hydroxide exported from the DRC is shipped to China for refining. The sea route from Durban to Chinese ports adds approximately 25–30 days"; refiners China ~70–80 % (Huayou Cobalt, GEM, Jinchuan, CNGR); geen Ningbo/Zhapu-vermelding, https://www.lobitocorridor.com/guides/cobalt-supply-chain-explained/
[4] policyrisk.com, "Zhejiang Huayou Cobalt Co., Ltd." — "Huayou's Quzhou facility is the single largest cobalt chemical refinery in the world", https://policyrisk.com/supplymap/company/huayou-cobalt
[5] Fastmarkets, "'Massive' discrepancy between DRC cobalt hydroxide exports, allocated quota: sources" — 2026 quotum 87.000 t basis + optioneel 9.600 t strategisch = max. 96.600 t; Q1 2026 <50 % van het quotum verscheept, https://www.fastmarkets.com/insights/discrepancy-between-drc-cobalt-hydroxide-exports-allocated-quota-massive/
[6] Fastmarkets, "Entreprise Générale du Cobalt announces first shipments" (2026-02-12) — "cobalt producers are sending export shipments from the DRC via trucks to Durban in South Africa or to Dar-es-Salaam in Tanzania, which then are mainly destined for China"; DRC 207.134 t Co in hydroxide 2025, https://www.fastmarkets.com/insights/entreprise-generale-du-cobalt-announces-shipments-to-swiss-traders/
[7] `v2/design/routebrieven/koper-kolwezi-durban.md` — hergebruikte geometrie/ankers been A (`cu-tfm-laad`, `cu-durban-kade`, 12 via-punten, `stroombeen-tfm-durban.geojson`, `aanloop-durban.geojson`); gebakken lengte 2.982 km
[8] Huayou Cobalt, corporate site — "Huayou New Energy Technology (Quzhou) Co., Ltd.", https://www.huayou.com/en
[9] Wood Mackenzie, rapportpagina "Quzhou, Huayou Cobalt" (titel/metadata gezien; achter paywall — capaciteitscijfer 3,0+19,1 kt Co niet zelf uit de brontekst gehaald), https://www.woodmac.com/reports/metals-huayou-quzhou-cobalt-refinery-150022263/
[10] Huayou Cobalt, "2024 Mineral Supply Chain Due Diligence Report" (PDF) — enige gevonden document dat Ningbo/Zhapu → Quzhou noemt; 403 bij ophalen deze sessie, niet geverifieerd, https://www.huayou.com/Public/Uploads/uploadfile/files/20250422/2024-Mineral-Supply-Chain-Due-Diligence-Report.pdf
[11] OpenStreetMap via Nominatim (ODbL) — node "Beilun Container Terminal Phase 2" 29.9352897/121.8695084 en "Phase 3" 29.9434295/121.8412286, opgevraagd 2026-09-26, https://nominatim.openstreetmap.org
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15, 5 tegels) — `v2/build-cache/satcheck/sat-kobalt-tfm-quzhou-ningbo-beilun.png`, 2026-09-26
[13] Reuters, "Congo suspends activities at Chinese mine after spill" (2025-11-07) — CDM-schorsing 3 maanden vanaf 2025-11-06, verlengbaar; niet zelf opgehaald (401/toegang geweigerd deze sessie), geciteerd via het ontwerp-onderzoek van deze keten, https://www.reuters.com/sustainability/climate-energy/congo-suspends-activities-chinese-mine-after-spill-2025-11-07/

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `kobalt-tfm-quzhou`** → `v2/data/stroomroute-kobalt-tfm-quzhou.json` — 4 benen, **15.803,9 km**, 29.412 punten, 3 markers. truck 2.982,5 km · zee 17,8 (stippel) + 12.792,0 + 11,6 (stippel) = 12.821,4 km.
Recept: `bak_stromen.sh` (functie `bak_kobalt_tfm_quzhou`).

**b1 (truck, letterlijke kopie):** exact `v2/build-cache/ais/graaf/stroombeen-tfm-durban.geojson` uit `bak_koper_durban` (koper-tfm-durban) — geen nieuwe wegscan. **2.982,5 km, 28.086 punten**, ongewijzigd (byte-identiek aan het gebakken koper-tfm-durban-been). Tegen de brief-schatting "~3.000 (gebakken koper-tfm-durban: 2.982 km, −0,6%)" klopt dit exact, want het ís diezelfde gebakken lijn.

**b1a (zee, haven-aanloop, letterlijke kopie, stippel):** exact `v2/build-cache/ais/graaf/aanloop-durban.geojson` — **17,8 km, 6 punten**, ongewijzigd. Naad b1→b1a **0,00 km** (beide uiteinden op de Durban-kade -29,879/31,016).

**b2 (zee, nieuw, MARNET):** `--been "zee|…|-29.8168,31.1737|29.9758,121.9736"` — snap 0,000 km aan beide uiteinden (op de knopen zelf), 71 MARNET-edges, **12.792,0 km / 1.315 punten** (lengte-invariant getekende lijn vs. som edge-km: +0,54 km = de naden binnen het been zelf, ruim onder de norm). Tegen de brief-schatting "~12.800 (indicatief)" is dit **−0,06%** — de exacte kade-tot-kade-afstand die §7/open-punten van de brief nog miste. Naad b1a→b2 **0,04 km**.

**b2a (zee, haven-aanloop, nieuw):** `timeout 300 python v2/tools/maak_havenaanloop.py --naam kobalt-tfm-quzhou-ningbo --van 29.9758,121.9736 --naar 29.9353,121.8695 --uit …` vond een pad over water op de **eerste trap** (cel 0,02° gebufferd): **11,6 km, 5 punten, 0,00 km over land** (geen terugval nodig, geen tweede poging). Dit is **ruim 2× de indicatieve schatting van de briefschrijver (~5,6 km)** — de indicatie was een educated guess vóór het bakken; de gemeten waarde (omwegfactor 1,059 t.o.v. de rechte lijn van 11,0 km) vervangt hem. Naad b2→b2a **0,00 km**.

**Geen been C (Ningbo → Huayou Quzhou):** conform de bak-aanwijzing en brief §6/§7 — geen bron toont dat dit specifieke hydroxide bij Quzhou aankomt (CMOC verkoopt via handelaar IXM; Huayou's eigen due-diligence-rapport gaf een 403). Geen lijn, geen stippel, geen marker voor Huayou Quzhou (coördinaat niet gevonden, blijft open — §7).

**Toets:** km-som **15.803,9 km** (geen gepubliceerde totaal-km voor de hele keten om tegen te toetsen — de brief geeft alleen per-been schattingen, die hierboven per been zijn nagelopen; alle vier binnen ±15% of exact gelijk aan de vooraf gebakken lijn). Naden **0,00 / 0,04 / 0,00 km**, ruim onder de norm van 5 km. `toets_knikken.py`: **50 knikken ≥60°, 2 omkeringen, 1 TERUGLOOP** — de terugloop (156,6°, boogstraal ~50 m bij -10,56584/26,20270) zit in het **gekopieerde** truck-been b1 en is **byte-identiek aanwezig in koper-tfm-durban zelf** (onafhankelijk nagemeten: zelfde graden/straal/coördinaat) — een pre-existente eigenschap van de gedeelde geometrie, niet iets dat deze bake heeft geïntroduceerd of hier hoort te repareren. `toets_rechte_benen.py --min-km 5`: **geen enkel been van deze stroom in de uitslag** — ook de twee stippel-haven-aanlopen zijn geen ongeteste rechte lijnen (ze zijn via `detour()`/water-pad gerouteerd, geen rechte `--stippel`). json geldig: versie 2, punt_formaat lonlat, modaliteiten uitsluitend {truck, zee}, elk been ≥2 punten. **Bevinding: bestandsgrootte 652,7 KB, boven de ~300 KB-norm** — volledig verklaard door de 28.086 punten van het gekopieerde truck-been (koper-tfm-durban zelf is met dezelfde geometrie 609,7 KB); niet dichtgetrokken, want het is de letterlijke kopie die de bak-aanwijzing voorschrijft. Alle 3 markers liggen op ~0 m van hun been.

**Gereedschapslessen:**
- `maak_havenaanloop.py` kan een korte haven-aanloop (11 km rechte lijn) alsnog fors laten uitwaaieren (+5,6% → in dit geval een omwegfactor van 1,059 over water rond de Beilun-havenkade) — de indicatieve schatting in een brief (§9-voorwerk van de briefschrijver) is nooit een toets-norm, alleen de gemeten uitkomst telt.
- Een "letterlijke kopie" van een moederbeen erft ook diens bevindingen (hier: de terugloop in de TFM-plant-laadlus). `toets_knikken.py` op de kopie herhaalt die dus terecht — controleer bij twijfel of de moederstroom dezelfde uitslag geeft vóór je de kopie als "nieuw probleem" behandelt.
- Bestandsgrootte is een eigenschap van de brongeometrie (hier het 1-op-1-wegprofiel achter b1), niet van deze bake — bij een letterlijke kopie erf je ook de KB's van de bron.
