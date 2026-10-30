# Routebrief (licht) · Lithium · Bikita → Durban → Tianjin (Zimbabwe → China)

**stroom-id:** `lithium-bikita-tianjin` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 14) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van Bikita Minerals (Sinomine) gaat per **truck** over de A4/R1 naar de grens bij Beitbridge, verder over de N1/N3 naar de containerkade DCT Pier 2 in Durban, per **zeeschip** door het Mozambiquekanaal, Malakka en de Zuid-Chinese Zee naar Tianjin (Beijiang-kade, *aannemelijk: één bron* voor Durban én Tianjin); de Chinese converter wordt niet getekend.
**Welke as van het verhaal:** Zimbabwaans concentraat via Zuid-Afrika (de zuidroute naast Beira) naar Noord-China. Bikita: 85 kt LCE/j naamplaat, 66,5 kt LCE/j prognose 2026 (sitelaag B16, Sinomine) [8]; Zimbabwe voerde 2025 1.204.072 t concentraat naar China uit = 15% van de Chinese spodumeenimport (douane, Fastmarkets) [3]. Aandeel Durban/Tianjin niet gepubliceerd. *Eenheid kt LCE/j; concentraat in t erbij.*

## 1 · Ketenkaart
```
Bikita-plant `li-bk-plant` ──(b1 truck · A9 → Masvingo → A4/R1 via Ngundu, Rutenga · 358 km gemeten, hemelsbreed 293)──► Beitbridge-grens `li-beitbridge-grens`
  ──(b2 truck · N1 via Polokwane → Gauteng → N3 via Harrismith · 1.103 km gemeten, routeplanner ~1.080)──► Durban DCT Pier 2 `li-durban-kade`
  ──(b3 zee, stippel · haven-aanloop 17,8 km, kopie koper-tfm-durban)──► MARNET-knoop Durban
  ──(b4 zee · Mozambiquekanaal → Malakka → Bohai · ~14.050 km MARNET, aannemelijk: één bron)──► zeeknoop 9649 Tianjin
  ──(b5 zee, stippel · haven-aanloop 30,8 km, omgekeerde kopie ree-baotou-hanau)──► Tianjin Beijiang-kade `li-tianjin-kade` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-bk-plant` → `li-beitbridge-grens` | mijnweg → A9 west → Masvingo → A4/R1 (Ngundu, Rutenga) → Beitbridge | hemelsbreed 293 km, geen wegkm; indicatie ~370 (Sinomine: mijn 80 km van Masvingo [1] + Masvingo–Beitbridge ~290 routeplanner [5]); droogloop 358,1 | maak_stroombeen_weg (zimbabwe) | nee |
| b2 | A | truck | `li-beitbridge-grens` → `li-durban-kade` | N1 (Polokwane, Gauteng-ring) → N3 (Harrismith) → Durban | 1.079 routeplanner [5]; droogloop 1.103 (+2,2%); zelfde via-punten als koper-tfm-durban/kobalt-kcc-durban | maak_stroombeen_weg (zimbabwe, zuid-afrika) | nee |
| b3 | B | zee (stippel) | `li-durban-kade` → MARNET-knoop Durban (-29.817, 31.174) | haven-aanloop (kade 16,7 km van de zeeknoop, > 5 km) | 17,8 | letterlijke kopie `aanloop-durban.geojson` (koper-tfm-durban) | ja, net reikt niet |
| b4 | B | zee | Durban (-29.817, 31.174) → zeeknoop 9649 (38.8910, 117.8503) | Mozambiquekanaal, Malakka, Zuid-Chinese Zee, Bohai | droogloop 14.048; geen gepubliceerde km, eigen schatting ~14.800 | MARNET (`--been "zee\|…"`) | nee; *aannemelijk: één bron* in de beennaam |
| b5 | B | zee (stippel) | zeeknoop 9649 → `li-tianjin-kade` | haven-aanloop (kade 14,9 km van de zeeknoop, > 5 km) | 30,8 (22 punten) | omgekeerde kopie van `ree-baotou-hanau-aanloop-tianjin.geojson` = `lithium-bikita-tianjin-aanloop-tianjin.geojson` | ja, net reikt niet |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-bk-plant` | mijn / laadplek | Bikita Minerals, concentratorplant | -19.9512, 31.4245 | [1][8]; hergebruik lithium-bikita-zhangjiagang | bron-gelegd (z15 gezien 2026-10-30: procesgebouwen en plantcomplex aan een mijnweg, open pits direct oostelijk) |
| `li-beitbridge-grens` | grensovergang | Beitbridge, Limpopo-brug | -22.2244, 29.9865 | [4][5]; hergebruik pgm-beitbridge-grens (pgm-zimplats-rustenburg) | bron-gelegd (z15: rivier met brug, grenscomplex met opstelvelden aan beide oevers; punt gedeeltelijk onder wolk, ligging bevestigd door de oude brief) |
| `li-durban-kade` | overslag truck → zee | Durban Container Terminal Pier 2, noordkade | -29.8790, 31.0160 | [2]; hergebruik koper-kolwezi-durban (cu-durban-kade) | bron-gelegd (z15 gezien: STS-kranen en containerstacks langs de noordkade); kadekeuze *aannemelijk*: concentraat gaat doorgaans als bulk (Maydon Wharf), niet gebronnd |
| `li-tianjin-kade` | losplek (stoppunt) | Tianjin Port, Beijiang-haven, oostkade | 39.0100, 117.7705 | [2]; hergebruik ree-baotou-hanau (ree-tianjin-kade) | bron-gelegd (z15 gezien: kadekranen en containerstacks langs de oostkade); bestemming *aannemelijk: één bron* [2]; een bulkterminal is niet gebronnd |

## 4 · Via-punten (alleen landbenen; lon,lat in het profiel is (lon, lat))
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Bikita-plant (anker) | -19.9512, 31.4245 | beginpunt |
| b1 | 2 | mijnafrit op de A9 | -19.9721, 31.4148 | pint de afrit naar het westen (Masvingo) i.p.v. oostwaarts naar Mutare/Beira |
| b1 | 3 | Ngundu, A4 | -20.8015, 30.8009 | A4 zuid over de Masvingo-ring i.p.v. een tak naar Chiredzi |
| b1 | 4 | Rutenga, A4 | -21.2327, 30.7275 | A4 naar Beitbridge i.p.v. een zijtak naar Mwenezi/Chiredzi |
| b1 | 5 | Beitbridge-grens (anker) | -22.2244, 29.9865 | eindpunt; droogloop gaf snaps van hooguit 0,68 km |
| b2 | 1 | Beitbridge-grens (anker) | -22.2244, 29.9865 | beginpunt |
| b2 | 2 | Polokwane N1-bypass | -23.9218, 29.4803 | N1 over de bypass i.p.v. de stad in |
| b2 | 3 | Buccleuch N1/N3-splitsing | -26.0493, 28.1004 | N3 naar Durban i.p.v. de N12/N4 |
| b2 | 4 | Durban DCT Pier 2 (anker) | -29.8790, 31.0160 | eindpunt (havenstraten Bayhead via de eindklassen-regel, zoals koper-tfm-durban) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Bikita-concentrator | Sinomine Resource Group | erts → spodumeenconcentraat (5,0–5,5% Li2O) en petaliet | 85 kt LCE/j naamplaat; 66,5 kt LCE prognose 2026 | [1][8] |

Fase C/D niet getekend: geen bron koppelt een lading aan een converter of afnemer in Tianjin.

## 6 · Stoppunt
De brief stopt op de Beijiang-kade: SunSirs noemt Tianjin als aankomsthaven van Bikita-ladingen maar koppelt geen fabriek of landbeen, dus fase C is niet in één zin gegeven; D/E vervalt.

## 7 · Open punten
- **Durban en Tianjin zijn elk één zwakke bron** [2]: de bedrijfstabel noemt Durban en Beira voor Bikita, de tekst Tianjin of Zhangjiagang; geen lading is aan beide gekoppeld. Het verhaal is beperkt tot "kan zo lopen".
- **Terminalkeuze:** DCT Pier 2 en Beijiang zijn containerkades; concentraat gaat doorgaans als bulk (Maydon Wharf in Durban; een bulkterminal in Tianjin). Niet gebronnd, bewust niet verlegd (aanpassing haalbaarheidstoets).
- **Wegkm b1:** geen bron geeft de rit Bikita–Beitbridge; ~370 is een som van een bedrijfsopgave en een routeplanner, 358,1 is de droogloop. Oxpeckers [4] geeft 550 km tussen Beitbridge en Machipanda (Beira-grens), dus niet vanaf Bikita, en noemt Durban niet.
- **Volume-split** Beira/Durban/Tianjin/Zhangjiagang ongepubliceerd; het jaarvolume van de mijn is geen volume van deze lijn.
- **Beleidsrisico:** Zimbabwe stopte de export van concentraat op 25-02-2026 [3]; quota 200 kt (apr) + 300 kt (jul) 2026 [6][7]; verbod per jan 2027 en sulfaatfabriek Bikita medio 2027 veranderen het product.
- **Overlap:** de mijn deelt het anker met lithium-bikita-zhangjiagang (Beira-route); de Zuid-Afrika-benen zijn kopie van koper-tfm-durban, de Tianjin-aanloop van ree-baotou-hanau.

## 8 · Bronnen
[1] Sinomine Resource Group, Bikita Minerals (80 km NO van Masvingo, spodumeen- en petalietlijn). https://en.sinomine.cn/25/93.html
[2] SunSirs, 2026: Bikita-vertrek Beira, tabel noemt Durban Port en Beira Port, aankomst Tianjin/Zhangjiagang 10–18 juli, 15–25 kt per schip. https://www.sunsirs.com/uk/detail_news-34127.html
[3] Fastmarkets, 2026: exportstop 25-02-2026; China-douane 2025: 1.204.072 t uit Zimbabwe van 7.750.630 t (15%). https://www.fastmarkets.com/insights/zimbabwe-imposes-immediate-ban-on-exports-of-raw-minerals-lithium-concentrates/
[4] Oxpeckers, 04-2025: Beitbridge SADC's drukste landgrens, ~550 km ten zuiden van Machipanda; smokkel via Beira. https://oxpeckers.org/2025/04/lithium-smugglers/
[5] Routeplanners (consumentensites, geen autoriteit): Beitbridge–Durban ~1.079 km, Masvingo–Beitbridge ~290 km. https://www.rome2rio.com/s/Beitbridge/Durban · https://www.rome2rio.com/s/Masvingo/Beitbridge
[6] Mining Weekly, 25-08-2026: extra quotum, transport Bikita hersteld (alleen zoekresultaat gelezen, pagina gaf 403). https://www.miningweekly.com/article/sinomine-secures-additional-zimbabwe-lithium-export-quota-2026-08-25
[7] Mysteel, 25-08-2026: quota 200 + 300 kt (overgenomen uit lithium-bikita-zhangjiagang [4]). https://www.mysteel.net/news/5138179-flash-sinomine-resource-group-has-restored-normal-transport-operations-for-its-bikita-lithium-concentrate
[8] `v2/design/lithium-sitelaag.json` (w-li-bikita, B16: 85 kt LCE naamplaat, 66,5 kt prognose 2026).
[9] Wikipedia, A4 road (Zimbabwe): Beitbridge – Rutenga – Ngundu – Masvingo. https://en.wikipedia.org/wiki/A4_road_(Zimbabwe)
[10] Eerdere brieven (ankers en benen hergebruikt): lithium-bikita-zhangjiagang, koper-kolwezi-durban, pgm-zimplats-rustenburg, ree-baotou-hanau.
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15, live, 2026-10-30): `v2/build-cache/satcheck/sat-lithium-bikita-tianjin-{bikita-plant,beitbridge,durban-dct2,tianjin-kade}.png`.

## 9 · Gebakken (2026-10-30, lichte werkwijze, M31 golf 14)
`v2/data/stroomroute-lithium-bikita-tianjin.json` (versie 2, lonlat, 308,4 KB, 15.277 punten, 4 markers), functie `bak_lithium_bikita_tianjin()` in `v2/tools/bak_stromen.sh`, profielen `lithium-bikita-tianjin-bkplant-beitbridge` en `lithium-bikita-tianjin-beitbridge-durban` in `maak_stroombeen_weg.py`. Totaal 15.554,2 km.

| # | modaliteit | km | naad | stippel | toets |
|---|---|---|---|---|---|
| b1 | truck Bikita-plant → Beitbridge | 354,2 (weg 353,8) | 0,00 | nee | indicatie ~370: -4,4% (geen wegkm; hemelsbreed 293) |
| b2 | truck Beitbridge → DCT Pier 2 | 1.103,0 | 0,00 | nee | routeplanner ~1.080: +2,1% |
| b3 | zee haven-aanloop Durban | 17,8 | 0,00 | ja | letterlijke kopie `aanloop-durban.geojson` (koper-tfm-durban) |
| b4 | zee Durban → zeeknoop 9649 Tianjin | 14.048,4 | 0,04 | nee | MARNET, geen gepubliceerde km; *aannemelijk: één bron* in de beennaam |
| b5 | zee haven-aanloop Tianjin | 30,8 | 0,00 | ja | omgekeerde kopie `ree-baotou-hanau-aanloop-tianjin.geojson` (zeeknoop → kade) |

**Markers (4):** plant, Beitbridge, DCT Pier 2, Beijiang-oostkade, alle 0,00 km van hun lijn. Grootste naad 0,04 km (zee-snap Durban). `toets_knikken`: 0 omkeringen en 0 terugloop; 32 knikken >= 60 graden op de twee truckbenen (kruispunten Masvingo, haven Durban/Bayhead, plantafrit), geen lus.
**Recept:** b1 en b2 via `python v2/tools/wegscan_puur.py --profiel <sleutel>` (zimbabwe, resp. zimbabwe + zuid-afrika, weg-slots), dan `bash v2/tools/bak_stromen.sh lithium-bikita-tianjin` (zwaar-slot, 16 s).
**Toelichting:**
- **b1 corridorKlassen.** De eerste scan (zonder corridorKlassen) gaf "geen wegpad tussen punt 1 en 2": de P4/A4-trunk in Masvingo eindigt bij 30.8408,-20.0668 en het zuidelijke A4-deel begint 5,4 km verder (secondary bij 30.8222,-20.1122), de stadsdoorsteek is tertiary/unclassified. Profiel kreeg `corridorKlassen: ["tertiary","unclassified"]`; geen via-punt bijgeschoven. Het mijnafrit snapt op de P4-trunk (0,01 km), plant → weg 0,37 km (first mile 2,64 km over kleine klassen).
- **b1 km:** 353,8 km tegen de brief-indicatie ~370 (-4,4%) en de droogloop 358,1; geen gepubliceerde wegkm, dus indicatie, geen norm.
- **b2:** 1.103,0 km, +2,1% tegen routeplanner ~1.080; N1 over de Polokwane-bypass en Buccleuch, N3 naar Durban; last mile 7,41 km over kleine klassen in de havenstraten (eindklassen-regel).
- **Stippels:** twee haven-aanlopen (Durban 17,8 km, kade 16,7 km van de zeeknoop; Tianjin 30,8 km, kade 14,9 km van zeeknoop 9649). Het zeebeen b4 loopt van knoop tot knoop, doorgetrokken; "aannemelijk: één bron" staat in de beennaam.
- **Geen lucht, leiding of spoor.** Geen nieuwe extracts.
**Lessen:** (1) een stad op de corridor kan de trunk breken in OSM; `corridorKlassen` lost dat op zonder via-punt in het centrum. (2) Een bestand van 308 KB (twee truckbenen van 3,6 en 10,2 duizend punten) zit net boven de ~300 KB-richtlijn; niets herbakken, centraal noteren.

