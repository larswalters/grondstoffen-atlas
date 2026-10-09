# Routebrief (licht) · grafiet — Balama → Pemba → Kendal (Indonesië)

**stroom-id:** `grafiet-balama-kendal` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) · **status:** gebakken
**Keten in één zin:** natuurlijk vlokgrafiet (fines, breakbulk) gaat per **truck** over N14/N1 van de Balama-plant (Syrah) naar de breakbulk-kade van Pemba, per **bulkschip** (breakbulk) over de Indische Oceaan en Sunda-/Lombokstraat naar Tanjung Emas, Semarang (losplek aannemelijk) en per **truck** ~25–29 km over de Pantura naar PT Indonesia BTR New Energy Material (anodefabriek) in Kendal Industrial Park/SEZ.
**Welke as van het verhaal:** *ex-China vlok naar een Indonesische anodefabriek* — de ontwijk-as: sinds 2025 gaat Balama-fines niet meer naar China (geen verkoop aan Chinese anodeklanten) maar naar Indonesië. **Volume: ~30 kt vlokconcentraat (fines)/j, peiljaar 2025** = 3 × ~10 kt breakbulk Pemba → Indonesië = 55% van 55 kt derde-partijverkoop [1]. Eenheid kt grafiet/j (zoals de grafiet-sitelaag). 2026 onzeker: Balama deels stilgelegd [8], geen 2026-zending bevestigd.

## 1 · Ketenkaart
```
Balama-plant `gr-balama-plant` ──(b1 truck · N14 → Metoro → N1/EN106 via Mieze · 257 km)──► Porto de Pemba `gr-pemba-kade`
  ──(b2 haven-aanloop Pemba 58,8 km stippel over water)──(b3 aanloop-vervolg 233 km rechte stippel)──► zeeknoop 2193 (-12.0, 43.0)
  ──(b4 zee · Indische Oceaan → Sunda/Lombok → Javazee · ≈ 7.605 km, aannemelijk)──► zeeknoop 5470 (-6.8337, 110.4071)
  ──(b5 haven-aanloop Semarang 12,4 km stippel)──► Tanjung Emas, Dermaga Samudera 2 `gr-semarang-kade` (aannemelijk)
  ──(b6 truck · Pantura Jl Arteri · 29,3 km gemeten, 25 gepubliceerd, aannemelijk)──► BTR Kendal `gr-btr-kendal` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (breakbulk-vracht in zakken/bulk, Grindrod) | `gr-balama-plant` → `gr-pemba-kade` | OSM-ref N14 (Balama–Metoro, primary, 112,5 km) → Metoro → N1/EN106 via Mieze → Pemba. Brief balama-vidalia noemt N380: dat is OSM-wise N14 | 250–265 gepubliceerd [7]; gemeten haalbaarheidstoets 161,6 + 95,5 = 257 | maak_stroombeen_weg (nieuw profiel, extract `mozambique`) | nee |
| b2 | A | zee (aanloop) | `gr-pemba-kade` → (-12.9700, 41.0000) | Pemba-baai → open water oost | 58,8 gemeten over water | maak_havenaanloop.py (53 punten, 0 km land) | ja — MARNET reikt niet (dichtste zeeknoop 2148 ligt 261 km zuid, verkeerde kant) |
| b3 | A | zee (aanloop-vervolg) | (-12.9700, 41.0000) → zeeknoop 2193 | open water, 0 km land | 233 hemelsbreed | rechte stippel | ja — hier reikt het net niet (293 km tot 2193) |
| b4 | B | zee (breakbulk/bulkschip) | zeeknoop 2193 → zeeknoop 5470 | Indische Oceaan → Sunda- of Lombokstraat (router kiest) → Javazee | ≈ 7.605 gemeten MARNET; hemelsbreed 7.401; geen gepubliceerde lengte | MARNET `--been zee` | nee — *aannemelijk: één bron voor de bestemming* |
| b5 | B | zee (aanloop) | zeeknoop 5470 → `gr-semarang-kade` | Javazee → havenmond Semarang | 12,4 hemelsbreed (kade > 5 km van zeeknoop → aanloop) | maak_havenaanloop.py (gemeten 233 s), terugval rechte stippel | ja — MARNET reikt niet tot de kade |
| b6 | C | truck | `gr-semarang-kade` → `gr-btr-kendal` | Semarang → Kendal over de Pantura-arteri (Jl Raya Arteri km 19, Brangsong); geen corridorkeuze | 29,3 gemeten OSM (24,4 km ref 1 trunk); **25 gepubliceerd** (Tanjung Emas → KIP) [3]; 21 voor Semarang City Seaport | maak_stroombeen_weg (extract `indonesie`, kort profiel, vensterKm 15) | nee — +17% t.o.v. 25: net buiten ±15%, indicatie, geen norm |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-balama-plant` | mijn / laadplek | Balama-plant (Syrah/Twigg) | -13.3100, 38.6600 | [7][9] hergebruik letterlijk | bron-gelegd — hergebruik (z14 gezien in [9][10]: procesfabriek met bezinkvijvers en zonnepark) |
| `gr-pemba-kade` | overslag truck → zee | Porto de Pemba, breakbulk-kade | -12.9672, 40.4853 | [1] Pemba-verscheping; [7] punt 18 kade (183 m, ~9 m diepte) | bron-gelegd (z16 gezien [10]: kade met schip langszij, blauwdak-loods en korte steiger; het vidalia-punt -12.9680, 40.4860 ligt 0,11 km ZO in het water) |
| `gr-semarang-kade` | losplek zee / overslag | Tanjung Emas, Dermaga Samudera 2 (OSM way 1430916358, Pelabuhan Indonesia) | -6.9442, 110.4240 | [5][6] haven en kade; geen bron noemt de losplek | **aannemelijk** (z15 gezien [10]: containerschiereiland met kraanrij, stapels en schepen langs de westkade; 12,4 km tot zeeknoop 5470) |
| `gr-btr-kendal` | verwerkingsknoop / fabriek | PT Indonesia BTR New Energy Material, Kendal SEZ | -6.9237, 110.2685 | [2][3][4] BTR gevestigd in KIP; sitelaag `w-btr-kendal` (OSM landuse + z14) | bron-gelegd — hergebruik (z15 gezien [10]: blauwdak-fabriekscomplex midden in het park) |

## 4 · Via-punten (alleen b1; b6 heeft geen corridorkeuze)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Metoro, T-kruising N14 × N1 | -13.1040, 39.8730 | pint oost (Pemba) i.p.v. zuid (Nacala, EN8/N12) — de enige corridorkeuze; hergebruik [7] punt 7; z15: kruising in het dorp, weg W–O en zuidtak [10] |
Profielvolgorde (lon, lat) voor de bak-agent: plant → Metoro → Pemba-kade; refs N14, N1; gepubliceerdKm 257; geen verdere via-punten (Montepuez-centrum en Pemba-stadsroute bewust niet).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Pemba breakbulk-kade (geen eigen been) | CFM/Grindrod, Syrah gebruikt | zakken/bulk → bulkschip | overcapaciteit beschikbaar | [1] p.18 |
| BTR Indonesia, Kendal | BTR New Energy | natuurlijk vlok → anodemateriaal (SPG/AAM) | 160 kt/j (80 + 80, fase 1/2) | [3][9] |

## 6 · Stoppunt
De brief stopt bij de BTR-fabriek in Kendal: hij is de enige afnemer met naam en fabrieksadres (ASX/AR noemen "BTR Indonesia"/"battery supply chain participant"); wat BTR daarna met het AAM doet (export naar de VS) is niet getekend — fase D/E vervallen.

## 7 · Open punten
- **Losplek op Java niet genoemd.** AR2025 zegt alleen "battery supply chain participant in Indonesia" [1]; "BTR Indonesia" met naam staat in de ASX-melding [2] zonder havenplaats. Tanjung Emas = aanname (KIP noemt 25 km tot Tanjung Emas, het park heeft geen eigen kade in de tekst [3]; op z15 liggen wel pieren aan de kust van het park, geen bron). Daarom b4–b6 aannemelijk.
- **BTR heeft ook een site in IMIP Morowali** (haalbaarheidstoets); welke fabriek de Pemba-fines ontvangt is niet bewezen — Kendal is gekozen omdat de ASX/KIP-bron Kendal noemt.
- **b6 +17%:** 29,3 OSM tegen 25 opgave: indicatie, geen toets. Site > 2 km van de Pantura → dan stippel "last mile (geen net op deze korrel)".
- **Geen gepubliceerde zeelengte** Pemba → Semarang; b2/b3 zijn de eerlijke stippel: MARNET heeft geen knoop in de buurt van Pemba.
- **Lading 2026 niet bevestigd:** Balama deels stilgelegd, Q2 2026 slechts 2,3 kt [8]; as = 2025-volume, de weg is echt, de lading nu niet zeker.
- Syrah noemt een 4e Pemba-verscheping (VS, maiden) — andere keten, niet getekend.

## 8 · Bronnen
[1] Syrah Resources, 2025 Annual Report (mrt 2026), pp. 12/18/19/37: drie ~10 kt breakbulk fines Pemba → "battery supply chain participant in Indonesia" voor AAM; 55 kt derdepartij, 55% naar Indonesië; Pemba-kade, magazijn, overcapaciteit. https://www.datocms-assets.com/65260/1774572803-syr_2025_annual_report.pdf
[2] Syrah, ASX-melding 24-03-2025 (jaarcijfers 2024): "spot natural graphite sales to BTR Indonesia", maiden breakbulk-zending naar Indonesië. https://announcements.asx.com.au/asxpdf/20250324/pdf/06gxq03hsz3qwj.pdf
[3] Kendal Industrial Park: Jl Raya Arteri KM 19, Brangsong; Tanjung Emas 25 km, Semarang City Seaport 21 km; BTR-directeur: "close to the port". https://www.kendalindustrialpark.co.id/
[4] Wikipedia, Kendal Industrial Estate (PT Kawasan Industri Kendal; Jababeka + Sembcorp, 2.700 ha, geopend 2016). https://en.wikipedia.org/wiki/Kendal_Industrial_Estate
[5] Wikipedia, Port of Tanjung Emas (Semarang; coördinaat -6.947, 110.424). https://en.wikipedia.org/wiki/Port_of_Tanjung_Emas
[6] OpenStreetMap (ODbL), way 1430916358 Dermaga Samudera 2, operator Pelabuhan Indonesia, industrial=port (Nominatim lookup). https://www.openstreetmap.org/way/1430916358
[7] Atlas: `v2/design/routebrieven/grafiet-balama-vidalia.md` §3 (Pemba-variant: Metoro -13.104/39.873, Pemba -12.968/40.486, 250–265 km [M1][M9], kade 183 m/~9 m).
[8] Syrah Q2 2026 slides (Balama 2,3 kt, campagne uitgesteld). https://www.investing.com/news/company-news/syrah-q2-2026-slides-balama-curtailed-vidalia-nears-commercial-sales-93CH-4807440
[9] Atlas: `v2/design/grafiet-sitelaag.json` (`w-balama`, `w-btr-kendal` 160 kt/j) en `routebrieven/grafiet-balama-laixi.md` §3 (Balama-anker).
[10] Esri World Imagery via `sat_check.py` (live, 2026-10-09): `v2/build-cache/satcheck/sat-grafiet-balama-kendal-{pemba-kade,pemba-pier,samudera2-kade,btr-kendal,balama-plant,metoro}.png`.
[11] Haalbaarheidstoets 2026-10-09 (wegtool, MARNET-knopen 2148/2193/5470, maak_havenaanloop; interne meting, geen publicatie).
[12] Wikipedia, Pemba, Mozambique (coördinaat -12.967, 40.55 = stadscentroïde, geen anker). https://en.wikipedia.org/wiki/Pemba,_Mozambique

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Uitvoer:** `v2/data/stroomroute-grafiet-balama-kendal.json` (68,7 KB, versie 2, lonlat) · **6 benen · 8.210,1 km · 3.380 punten · 5 markers** · functie `bak_grafiet_balama_kendal` in `v2/tools/bak_stromen.sh`, profielen `grafiet-balama-kendal-balama-pemba` en `grafiet-balama-kendal-semarang-kendal` in `maak_stroombeen_weg.py`.

| # | modaliteit | km gemeten | tegen brief | naad | opmerking |
|---|---|---|---|---|---|
| b1 | truck | 260,2 (weg 259,7) | 257 (+1,1%) | — | N14 → Metoro → N1/EN106, extract mozambique, doorgetrokken |
| b2 | zee, stippel | 58,8 | 58,8 | 0,00 | haven-aanloop Pemba over water (0 km land), MARNET reikt niet |
| b3 | zee, stippel | 242,4 | brief 233 (hemelsbreed gemeten 242,4) | 0,00 | rechte stippel open water → zeeknoop 2193, hier reikt het net niet |
| b4 | zee | 7.604,7 | ~7.605 | 0,00 | MARNET zeeknoop 2193 → 5470, 27 edges, doorgetrokken, aannemelijk |
| b5 | zee, stippel | 12,7 | 12,4 | 0,00 | haven-aanloop Semarang over water (0 km land), aannemelijk |
| b6 | truck | 31,3 (weg 31,2) | 25 parkopgave (+24,8%) / 29,3 haalbaarheidstoets (+6,5%) | 0,00 | Pantura, extract indonesie, doorgetrokken, aannemelijk |

**Markers (5, alle 0,0 m van de lijn):** `gr-balama-plant` (-13.3100, 38.6600) · `gr-pemba-kade` (-12.9672, 40.4853) · Pemba-baai open water, einde aanloop (-12.9700, 41.0000) · `gr-semarang-kade` (-6.9442, 110.4240) · `gr-btr-kendal` (-6.9237, 110.2685). Geen naad > 0,00 km: alle benen sluiten op de kilometer.

**Recept:** b1 `wegscan_puur.py --profiel grafiet-balama-kendal-balama-pemba` (52 s scan; 1 via-punt Metoro, snap 0,22 km; ankersnaps 0,39 / 0,09 km; first mile 4,9 km en last mile 1,3 km over kleine klassen) · b2 `maak_havenaanloop.py` (cel 0,01 kaal, omwegfactor 1,054) · b3 `--stippel` · b4 `--been zee` · b5 `maak_havenaanloop.py` (cel 0,02 gebufferd, 12,7 km, omwegfactor 1,019; eerste poging mislukte op een argumentfout, niet op de timeout) · b6 `wegscan_puur.py --profiel grafiet-balama-kendal-semarang-kendal` (428 s scan op de indonesie-extract, geen via-punten).

**Toelichting.**
- **Stippel (b2, b3, b5):** b2 en b3 vormen samen het gat waar MARNET niet reikt (dichtste zeeknoop 2148 ligt 261 km zuid; Pemba heeft binnen 261 km geen zeeknoop). b2 is het kortste pad over water, b3 de rechte vervolgstippel naar zeeknoop 2193 (242,4 km, de brief noemde 233: dat was een schatting). b5 is de aanloop omdat de kade 12,4 km van zeeknoop 5470 ligt (> 5 km). Alle drie blijven stippel: dat is uitsluitend "hier reikt het net niet".
- **Aannemelijk (b4-b6):** doorgetrokken. De onzekerheid zit in de beennamen en in deze brief (§7: de losplek op Java is een aanname). b4 heeft geen gepubliceerde lengte; 7.604,7 km is de MARNET-meting (hemelsbreed 7.401).
- **b6 +24,8% tegen 25:** de 25 km komt van Kendal Industrial Park (Tanjung Emas → KIP) en is een parkopgave, geen wegmeting. De baklijn is 31,2 km: 1,4 km binnen de haven (service), 3,9 km in en naar het park (service/unclassified) en de rest over de Semarang-arteri. Geen via-punt bijgeschoven. Het eindstuk draait in het park 2 km westwaarts en terug naar het anker (hairpin 164° op het anker zelf, R 13 m: vermoedelijk de parkwegen: de OSM-route nadert het anker vanuit het westen, niet nagemeten); beschouwd als parkinfrastructuur, geen terugloop (toets_knikken: 0 terugloop).
- **Geen vlucht, geen leiding, geen letterlijke kopie.**
- **toets_knikken:** 17 knikken, 1 omkering (het anker in Kendal), 0 terugloop; de spikes bij de kade van Pemba en in de haven van Semarang zijn OSM-zigzag op kadewegen. **toets_rechte_benen --min-km 5:** alleen b3 (242,4 km, omwegfactor 1,000) en dat is een stippel met reden.

**Lessen / aandachtspunten.**
- `maak_havenaanloop.py` neemt een negatieve breedtegraad alleen met `--van=-12.9672,40.4853` (zonder `=` leest argparse het getal als vlag).
- De brief gaf 233 km voor de rechte stippel b3; hemelsbreed is dat 242,4 km. Controleer hemelsbreed-getallen in een brief met de grootcirkel.
- De wegtoets van b6 blijft een indicatie (parkopgave, geen wegkm); bevinding, geen foutmelding.
- Open uit §7 blijft staan: losplek Java niet genoemd (b4-b6 aannemelijk), BTR Morowali niet uitgesloten, lading 2026 niet bevestigd.
