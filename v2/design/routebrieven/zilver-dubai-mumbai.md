# Routebrief (licht) · zilver — Dubai (DXB) → Mumbai (BOM) → Zaveri Bazaar (VAE → India)

**stroom-id:** `zilver-dubai-mumbai` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken (2026-10-09)
**Keten in één zin:** zilverbaren uit Dubai per belly-/vrachtvlucht (grootcirkel DXB → BOM) van de DXB-vrachtterminal naar het Mumbai Air Cargo
Complex (Sahar), en per truck (Western Express Hwy → S.V. Road → Dr. Annie Besant Rd) naar de Zaveri Bazaar-marktwijk. Eindpunt = marktwijk, geen pand (§6, §7).
**Welke as van het verhaal:** de VAE-route voor Indiase zilverinvoer, een **reserve-as, zwak gebrond**: VAE → India groeide van "close to zero" tot
**1.097 t Ag in jan–feb 2024** (provisional, 2 maanden, alle modaliteiten) naast 1.174 t uit het VK; India totaal **3.625 t Ag in 2023** [3]. Dat zilver in
Dubai per vliegtuig reist staat in één bron (Bloomberg-doorgeefartikel, mrt 2026) [1]; dat déze Indiase invoer vliegt en naar Mumbai gaat niet (§7).

## 1 · Ketenkaart
```
DXB-vrachtterminal (Emirates SkyCargo) `ag-air-dxb` (hergebruik uit goud-dubai-delhi)
  ──(b1 lucht · vlucht DXB → BOM, belly/vracht, grootcirkel, aannemelijk: één bron · 1.927,8 km)──►
Mumbai Air Cargo Complex, Sahar (BOM) `ag-air-bom` (hergebruik uit goud-argor-mumbai)
  ──(b2 stippel · BOM-vrachtplatform last mile, airside · 0,13 km)──►  openbare weg bij BOM
  ──(b3 truck · WEH → S.V. Rd → Dr. Annie Besant Rd · letterlijke kopie · 26,4 km gebakken)──►
Zaveri Bazaar `ag-mkt-zaveri` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | lucht | DXB-vrachtterminal → Mumbai Air Cargo Complex (BOM) | vlucht DXB → BOM, grootcirkel — **aannemelijk: één bron**, luchthavens/volume niet genoemd [1][2] | 1.927,8 (grootcirkel op de twee ankers, `maak_luchtbeen.py`, gemeten) | maak_luchtbeen | nee — doorgetrokken |
| b2 | D | truck | BOM-vrachtplatform → openbare weg | airside last mile (OSM-topologiegat, zie goud-argor-mumbai §9) | 0,13 (hemelsbreed, geen wegkm) | geen — stippel | **ja** — "schematisch — airside/privéterrein" |
| b3 | D | truck | openbare weg bij BOM → Zaveri Bazaar | Western Express Hwy → S.V. Road → Dr. Annie Besant Rd | **hemelsbreed 16,4 km, geen wegkm**; gebakken kopie 26,4 (ontwerp "~25-30", geen bron) [9][11] | **letterlijke kopie** `goud-argor-mumbai-weg-bom-zaveri.geojson` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ag-air-dxb` | vrachtterminal / vertrek lucht | DXB-vrachtterminal (Emirates SkyCargo), Airport Internal Rd — **letterlijk hergebruik** uit `goud-dubai-delhi.md` | 25.2560, 55.3434 | [10][11] | bron-gelegd. z15 (nu) gezien: kruis op een groot loodsgebouw direct ten zuiden van de passagiersconcourses, platform met wide-body toestellen ernaast; zelfde punt als de goudketen |
| `ag-air-bom` | vrachtterminal / aankomst lucht | Mumbai Air Cargo Complex, Sahar (CSMIA) — **letterlijk hergebruik** uit `goud-argor-mumbai.md` | 19.0954, 72.8660 | [9][11] | bron-gelegd. z15 (nu) gezien: loods-/terminalcluster W van de passagiersterminal tussen de banen, apron met toestellen, kruis op het cargo-cluster |
| `ag-mkt-zaveri` | groothandelsmarkt (stoppunt) | Zaveri Bazaar, Bhuleshwar, Zuid-Mumbai — **letterlijk hergebruik** | 18.9518, 72.8307 | [9][11] | **aannemelijk** (z15 gezien: dichte historische marktwijk, geen los pand te onderscheiden; Wikipedia-punt van de bazaar, geen centroïde van de stad) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen nieuwe: b3 is een letterlijke kopie, geen wegscan, geen profiel. De via-punten van die kopie (goud-argor-mumbai §4, lat, lon): Vile Parle (WEH)
19.0999, 72.8440 · Bandra West 19.0583, 72.8303 · Mahim 19.0423, 72.8398 · Worli (Dr. Annie Besant Rd) 19.0308, 72.8157 · Crawford Market 18.9473, 72.8345.
Vlucht en stippel hebben geen via-punten.

## 5 · Verwerkingsknopen
Geen. Geen raffinaderij of overslag onderweg behalve de twee vrachtterminals; geen kade, haven-aanloop, spoor of leiding (geen MARNET, geen extract).

## 6 · Stoppunt
De keten stopt in de marktwijk Zaveri Bazaar: geen bron koppelt deze zilverinvoer aan een bullion-bank, juwelier of kluis met adres, en Mumbai als aankomstplaats is
zelf onbevestigd (§7). Fase E vervalt; geen eindbeen naar een kluis/IIBX-vault (zou een verzonnen coördinaat zijn).

## 7 · Open punten
- **Silver-by-air DXB → India niet bevestigd.** Enige bron: "flights carrying gold and silver to and from Dubai have been grounded" (Bloomberg via Mining Technology, 4 mrt 2026) [1]
  — alleen de leadzin noemt zilver, India komt voor als metaalafnemer, geen luchthaven of volume. Lider (zelfde dag) noemt zilver alleen voor Londen-zendingen [2]. Daarom
  **aannemelijk** in de beennaam, doorgetrokken. Nergens een bron die zilver DXB → BOM aanwijst; zilver gaat normaal waarschijnlijk per schip (niet gebrond, hoort niet als claim).
- **Mumbai ≠ Ahmedabad/GIFT City (open, risico uit het ontwerp).** Het fiscale zwaartepunt is de **IIBX in GIFT City, Gujarat** [8][9]: "most of India's silver imports" van
  een paar private spelers uit Dubai via IIBX (CivilsDaily 2024) [4]; zilverbaren (HS 71069221) mag elke IEC-houder invoeren [8]. Geen bron zegt waar het metaal fysiek landt
  (Ahmedabad SVPI, Mumbai, Mundra). Mumbai blijft de ketennaam; Ahmedabad is niet gelegd (geen coördinaat verzonnen) — alleen een alternatieve keten als een bron de landing noemt.
- **Zaveri Bazaar als zilvereindpunt niet gebrond**: Wikipedia noemt de markt een juwelen-/goudhub [9]; zilver- of bullionrol niet gevonden. Hergebruik van het goud-anker is een aanname.
- **Actualiteit.** Sinds 12 mei 2026 invoerrecht zilver 6% → 15% (CEPA-VAE ~7%) [6], 16 mei zilver "restricted" (licentieplicht), invoer apr→mei 2026 −81,6% ($411 mln → $76 mln) [7];
  Dubai-vluchten in mrt 2026 grotendeels stil door de Iran-oorlog (37% van normaal op 12 mrt, Kitco, alleen uit zoekresultaat) [1]. De keten is dus een structureel patroon, geen huidig volume.
- **Volume niet vast te stellen.** Geen t Ag/j voor VAE → Mumbai, geen luchtaandeel. Wel: UAE → India jan–feb 2024 1.097 t (provisional, alle modaliteiten, niet te annualiseren) [3];
  India totaal 2023 3.625 t, 2024 jan–apr 4.172 t [3][4]; 2025-26 $12,05 mld (waarde, geen tonnage) [7]. Blootstelling per vlucht onbekend.
- **Wegkm b3:** geen gepubliceerde wegkm; 26,4 km gebakken kopie tegen ontwerp ~25 en hemelsbreed 16,4 km — ±15%-toets alleen indicatie.
- **b2 is airside:** het BOM-platform heeft in OSM geen aansluiting op het openbare net (zelfde bevinding als goud-argor-mumbai); de 0,13 km stippel is overgenomen, niet opnieuw gemeten.
- **Geen tussenlanding gebrond** (geen bron noemt een hub): één directe vlucht aangenomen (bakhandleiding §2).
- Bestaande beelden `sat-zilver-dubai-mumbai-jebelali-*` en `-jnpt-*` in `v2/build-cache/satcheck/` (11:38–11:39 vandaag) zijn niet van deze brief (eerdere poging, zee-variant): niet gebruikt, niet aangeraakt.

## 8 · Bronnen
[1] Mining Technology (GlobalData; Bloomberg-doorgeefartikel), 2026-03-04 — "Middle East tensions stall gold and silver shipments in Dubai": gold/silver in cargo holds of passenger planes, India afhankelijk van UAE-metaal. https://finance.yahoo.com/news/middle-east-tensions-stall-gold-142933160.html · Kitco 2026-03-13 (alleen zoekresultaat, niet gelezen): https://www.kitco.com/news/off-the-wire/2026-03-13/partial-flight-resumptions-restore-some-gold-flows-key-hub-dubai
[2] Lider (EN), 2026-03-04 — "Gold and silver trade suffocates due to flight disruptions from Dubai": zilver "more affected" voor Londen-zendingen, goud tot 5 t per passagiersvlucht. https://en.lider.media/2026/03/04/gold-and-silver-trade-suffocates-due-to-flight-disruptions-from-dubai
[3] LBMA Alchemist 113, D. Saha (LSEG) — "Facing Facts: India's Record Silver Imports from UAE": UAE 1.097 t jan–feb 2024, VK 1.174 t, India 2023 3.625 t, vervoersmodus niet genoemd. https://www.lbma.org.uk/alchemist/alchemist-113/facing-facts-indias-record-silver-imports-from-uae-a-paradigm-shift-in-the-supply-chain
[4] CivilsDaily, 2024-07-08 — "Red flags over runaway silver imports from UAE through GIFT City": IIBX-route, 15% vs 9%+3% CEPA, India jan–apr 2024 4.172 t. https://civilsdaily.com/news/red-flags-over-runaway-silver-imports-from-uae-through-gift-city
[5] Khaleej Times, 2025-05-20 — Budget-2025-beperking: nominated agencies/qualified jewellers/TRQ; zilver 7% CEPA-tarief zonder quotum. https://www.khaleejtimes.com/business/markets/india-restrictions-on-uae-gold-silver-imports?amp=1
[6] BasisPoint Insight, 2026-05-13 — duty 6% → 15% op 12 mei 2026; CEPA-zilver 7%. https://basispointinsight.com/Story/india-s-precious-metals-duty-hike-widens-dubai-arbitrage_7323b29ed16f.html
[7] BasisPoint Insight (GTRI), 2026-06-17 — zilverinvoer 2025-26 $12,05 mld; apr $411 mln → mei $76 mln; DGFT "restricted" 16 mei. https://www.basispointinsight.com/Story/silver-imports-plunge-after-duty-hike-and-import-restrictions--gtri_c10f5bc2a782.html
[8] GIFT CFO, "Gold & Silver import rules IIBX GIFT City IFSC" (jaar niet genoemd): zilverbaren HS 71069221 voor elke IEC-houder, BDR's. https://www.giftcfo.com/post/gold-silver-import-rules-iibx-gift-city-ifsc
[9] Wikipedia (MediaWiki API, prop=coordinates/extracts) — Zaveri Bazaar 18.951808/72.830697 (juwelenmarkt); CSMIA 19.08861/72.86806; IIBX = GIFT City, Gujarat. https://en.wikipedia.org/wiki/Zaveri_Bazaar · https://en.wikipedia.org/wiki/India_International_Bullion_Exchange
[10] Wikipedia, "Dubai International Airport" — cargo village, "most of the cargo for Asia and Africa". https://en.wikipedia.org/wiki/Dubai_International_Airport
[11] `v2/design/routebrieven/goud-dubai-delhi.md` (anker `au-air-dxb`, OSM way 249217154) en `goud-argor-mumbai.md` §3/§4/§9 (anker `au-air-bom`, `au-mkt-zaveri`, stippel BOM, gebakken b3). Hemelsbreed (haversine, R 6371,0088): BOM–Zaveri 16,4 km; stippel 0,13 km.
[12] Esri World Imagery via `v2/tools/sat_check.py` (z15, live, 2026-10-09): `v2/build-cache/satcheck/sat-zilver-dubai-mumbai-dxb-cargo.png`, `-bom-cargo.png`, `-zaveri.png`.
[13] WebSearch-webcheck 2026-10-09 (3 aanroepen): geen bron voor zilver per vlucht DXB → BOM of voor de landingsplek; v1 `data/silver.js`: alleen `ag-ex-lbma → ag-mkt-india` per schip (geen waarheid).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-zilver-dubai-mumbai.json` (15,2 KB, versie 2, punt_formaat lonlat) · functie `bak_zilver_dubai_mumbai()` in `v2/tools/bak_stromen.sh` · titel "Zilver · Dubai (DXB) → Mumbai (BOM) → Zaveri Bazaar". Eindpunt klopt met het id (Mumbai), geen afwijking van het ontwerp.

| # | modaliteit | km gebakken | km brief | naad | punten | geometrie |
|---|---|---|---|---|---|---|
| b1 | lucht | 1.927,8 | 1.927,8 (grootcirkel, gemeten) | 0,000 | 79 | `zilver-dubai-mumbai-lucht-dxb-bom.geojson` (maak_luchtbeen.py), doorgetrokken |
| b2 | truck (stippel) | 0,13 | 0,13 hemelsbreed | 0,000 | 2 | `--stippel`, letterlijk uit bak_goud_argor_mumbai |
| b3 | truck | 26,4 | hemelsbreed 16,4, geen wegkm; ontwerp ~25-30 | 0,000 | 637 | `zilver-dubai-mumbai-weg-bom-zaveri.geojson`, byte-identieke kopie van `goud-argor-mumbai-weg-bom-zaveri.geojson` |

Totaal 1.954,3 km · modaliteiten {lucht, truck} · 3 markers (ag-air-dxb, ag-air-bom, ag-mkt-zaveri), alle op 0,0 km van hun lijn.

**Recept.** Geen wegscan, geen PROFIELEN-sleutel, geen extract, geen MARNET-/spoor-/haven-aanloop. De tussenuitvoer (luchtbeen, kopie van het wegbeen) stond al in `v2/build-cache/ais/graaf/`; de functie stikt ze met `hecht_marnet.py route` (zwaar-slot) aan elkaar. Gedeeld met `bak_goud_argor_mumbai` (b2-stippel, b3, ankers BOM en Zaveri) en `bak_goud_dubai_delhi` (anker DXB).

**Vlucht (b1).** Grootcirkel tussen twee satelliet-gelegde vrachtterminals, doorgetrokken, "grootcirkel" en "aannemelijk: één bron" in de beennaam. Zilver per vliegtuig vanuit Dubai staat alleen in het Bloomberg-doorgeefartikel (mrt 2026, §7); geen bron voor DXB → BOM, geen volume. Geen tussenlanding aangenomen.

**Stippel (b2).** 0,13 km airside last mile: het BOM-vrachtplatform heeft in OSM geen aansluiting op het openbare net (zelfde bevinding als goud-argor-mumbai); overgenomen, niet opnieuw gemeten.

**Toets.** Naden 0,000 km (max 0,0). Lengte b3: geen gepubliceerde wegkm, dus geen ±15%-norm; indicatie 26,4 km tegen ontwerp ~25-30 (binnen) en hemelsbreed 16,4 (factor 1,6, stadsroute langs de kust). `toets_knikken.py`: lucht 0 knikken; b3 37 knikken, 1 omkering (180°, 19.05834,72.83066 bij het via-punt Bandra West, "scherpe bocht, echt"), 0 terugloop; dit zijn dezelfde knikken als in de bron goud-argor-mumbai (daar 69 knikken in het hele bestand), dus overgenomen geometrie, hier niet gerepareerd. `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom. `json.load` ok, versie 2, lonlat, elk been ≥ 2 punten.

**Lessen.** (1) Een eerdere afgebroken poging liet alleen beelden achter (`sat-zilver-dubai-mumbai-jebelali-*`, `-jnpt-*`, en graaf-bestanden `…-aanloop-jebelali/-jnpt.geojson`, zee-variant): niet gebruikt, niet aangeraakt. (2) Het slot-protocol met `rm -rf "$d"` wordt door de Claude Code-veiligheidscheck geweigerd (variabele in rm/rmdir); een slot nemen met `mkdir` en vrijgeven met `rm -f`/`rmdir` op letterlijke absolute paden werkt wel. (3) Open punten: Mumbai versus Ahmedabad/GIFT City (IIBX) niet gelegd, Zaveri Bazaar-zilverrol niet gebrond, wegkm b3 zonder bron (§7).
