# Routebrief (licht) · lithium — Pilgangoora → Port Hedland → Morowali (IMIP, Indonesië)

**stroom-id:** `lithium-pilgangoora-morowali` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 19) · **status:** gebakken
**Keten in één zin:** spodumeenconcentraat van de Pilgan-plant (Pilbara Minerals, PLS, Pilbara WA) gaat per **road train** ~120–140 km naar Utah Point (Port Hedland), per **bulkcarrier** ~2.000 km hemelsbreed over Timorzee–Banda-zee–Tolobaai naar de exporthaven van het Morowali Industrial Park (IMIP, Bahodopi, Sulawesi), waar ChengTok Lithium (Chengxin 65 % / Tsingshan 35 %) een lithiumchemicaliënfabriek heeft; de lijn eindigt op de IMIP-kade.
**Welke as van het verhaal:** de Indonesische converter-hub — Australisch erts draait mee in de nikkelparken. BPS-douanedata: Morowali (Bahodopi) importeerde 293 kt spodumeen in 8M-26, 91 % Australië, 9 % Zimbabwe [1]. Jaarvolume voor deze lijn: **ca. 20 kt LCE/j** (peiljaar 2026) = PLS-Chengxin-offtake 150 kt concentraat/j in CY25–CY26 [3][4] × 0,136 (5,5 % Li2O × 2,473; eigen omrekening). Ter context: heel Morowali geannualiseerd ca. 440 kt concentraat ≈ 60 kt LCE (293 kt is 8 maanden, geen jaar). **Aannemelijk, één bron:** geen bron koppelt PLS expliciet aan Morowali; Chengxin heeft een PLS-contract [3], ChengTok is een Chengxin-dochter [2], en 91 % van het Morowali-erts is Australisch [1].

## 1 · Ketenkaart
```
Pilgan-plant `li-pilgangoora-plant` ──(b1 truck · Marble Bar Rd → Great Northern Hwy → Utah Rd · ~120–140 km)──►
Utah Point `li-porthedland-utahpoint`
   ──(b2 zee · aanloop 79,7 km stippel + MARNET Hedland → Tolobaai ~2.000 km hemelsbreed + aanloop IMIP ~93 km stippel)──►
IMIP-exporthaven `li-imip-kade` (aannemelijk: één bron) ⏹ stoppunt
   (ChengTok-fabriek binnen IMIP: niet gelegd, niet getekend)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck (road trains, Qube) | `li-pilgangoora-plant` → `li-porthedland-utahpoint` | mijnweg → Marble Bar Rd → GNH → Utah Rd | ~120–140 [6] (gepubliceerd; gebakken 145,6 in de bronstroom) | LETTERLIJKE KOPIE van `pilgangoora-gwangyang`: twee weg-geojsons + het 0,355 km stippelgat | ja — alleen het 0,355 km OSM-gat bij South Hedland |
| b2a | B | zee | Utah Point → zeeknoop Hedland (−19,6000, 118,6000) | haven-aanloop Utah Point | 79,7 → bestaande aanloop 80,5 [6] | LETTERLIJKE KOPIE `…-aanloop-utahpoint.geojson` van `pilgangoora-gwangyang` | ja — MARNET reikt niet |
| b2b | B | zee | zeeknoop Hedland → zeeknoop IMIP 5491 (−2,0357, 122,0017) | Timorzee, Banda-zee, Tolobaai (MARNET beslist) | hemelsbreed ~1.988; geen zeekm gepubliceerd | MARNET (`--been "zee|…"`) | nee |
| b2c | B | zee | zeeknoop IMIP → `li-imip-kade` | haven-aanloop IMIP, aankomstrichting | 92,9 hemelsbreed (kade ↔ zeeknoop); bestaande aanloop 95,6 [7] | OMGEDRAAIDE KOPIE van `nikkel-morowali-quzhou-aanloop-imip.geojson` | ja — MARNET reikt niet |

Geen b3: geen fabriekspand gelegd (zie §7), dus de lijn eindigt op de kade. Geen last-mile-been.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-pilgangoora-plant` | mijn / concentratorplant | Pilgan-plant, Pilgangoora Operation (PLS) | -21.0595, 118.8956 | [6][10] | bron-gelegd — hergebruikt letterlijk uit `lithium-pilgangoora-gwangyang.md` §3 (z15 daar: plant, tailings, pits) |
| `li-porthedland-utahpoint` | laadkade (bulk) | Utah Point Bulk Handling Facility, Port Hedland | -20.3153, 118.5585 | [6] | aannemelijk — hergebruikt letterlijk (welke berth de lithiumlader is, is daar niet te onderscheiden) |
| `li-imip-kade` | losplek (zee) | IMIP-exporthaven, oostpunt van het complex, Bahodopi (BPS: hoofdhaven Morowali = Bahodopi) | -2.8480, 122.1980 | [1][7][9] | bron-gelegd — hergebruikt letterlijk uit `nikkel-morowali-quzhou.md` (`ni-imip-jetty`); eigen z16-blik: kruis op de oostrand van een landtong met schepen langszij, opslagterreinen en kraanspoor erachter. Of dit specifiek de invoerkade van ChengTok is, staat in geen bron |

## 4 · Via-punten
Geen nieuwe: beide landdelen zijn letterlijke kopieën van `pilgangoora-gwangyang` (via-punten daar al op GNH/Marble Bar Rd gelegd, §4 van die brief); zee en aanlopen zijn geometriebestanden, geen via-puntroutering.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| ChengTok Lithium Indonesia (IMIP) | Chengxin Lithium 65 % / Tsingshan 35 % | spodumeenconcentraat → lithiumchemicaliën | ontwerp 60 kt/j chemicaliën; proefproductie jun-2024, tot eind 2024 geen omzet | [2][5] |
| IMIP-lithiumketen (alle tenants) | BPS-douane | concentraat 293 kt (8M-26) → hydroxide 21,9 kt + carbonaat 9,9 kt | export 8M-26 US$ 613 mln, naar China (hydroxide 79 %, carbonaat 100 %) en Korea | [1] |

## 6 · Stoppunt
De brief stopt op de IMIP-kade: geen bron geeft een coördinaat of adres van het ChengTok-pand (Nominatim en Photon kennen het niet), dus fase C vervalt; fase D/E vervallen, de chemicaliën gaan volgens BPS naar China en Korea zonder genoemde afnemer [1].

## 7 · Open punten
- **PLS ↔ Morowali niet expliciet gekoppeld.** Petromindo noemt Pilbara Minerals als langetermijnleverancier van Chengxin maar geen specifiek leveringscontract voor de Indonesische fabriek [2]; smallcaps noemt geen land of fabriek [3]. Daarom "aannemelijk: één bron" in de beennaam.
- **ChengTok-fabriek niet gelegd** en niet getekend; geen bron met coördinaat.
- **IMIP-invoerkade onbekend:** `li-imip-kade` is de enige exportpier die al satelliet-gelegd is (nikkelbrief); BPS zegt alleen "geïmporteerd te Morowali en Bahodopi" [1].
- **Utah Point-berth niet met naam bevestigd voor lithium;** Lumsden Point is vanaf medio 2026 een alternatief (zie `lithium-pilgangoora-gwangyang.md` §7) — niet getekend.
- **Zeekm niet gepubliceerd;** de ±15 %-toets geldt niet voor b2b (hemelsbreed ~1.988 km, geen zeekm).
- **Volume is afgeleid:** 20 kt LCE/j rust op het contractvolume 150 kt/j (CY25–26) × eigen factor 0,136; geen bron geeft de feitelijke levering aan Morowali. Een deel van het PLS-concentraat gaat naar andere Chengxin-fabrieken.
- **Zimbabwe-aandeel (9 %)** en Chengxins eigen mijnen in China/Zimbabwe [2] zijn niet getekend.

## 8 · Bronnen
[1] Dewan Ekonomi Nasional, Battery Materials (BPS-douanedata), slides 42–45 — spodumeen geïmporteerd te Morowali en Bahodopi: 2024 72 kt, 2025 111 kt, 8M-26 293 kt, Australië 91 % en Zimbabwe 9 %; hoofdhaven Morowali = Bahodopi (IMIP). https://www.dewanekonomi.go.id/public/storage/event-materials/01M5BNCV5NQGV1M3Z2Y9SG4Q1T.pdf
[2] Petromindo, 1-4-2025 — PT Chengtok Lithium Indonesia op IMIP, 60 kt/j chemicaliën, proefproductie jun-2024, Chengxin 65 % / Tsingshan 35 %, ~US$ 350 mln, Pilbara Minerals als langetermijnleverancier genoemd. https://www.petromindo.com/news/article/chengxin-strives-for-full-capacity-at-indonesian-lithium-chemical-plant
[3] smallcaps.com.au — Pilbara Minerals levert 85 kt (2024) en 150 kt/j (twee volgende kalenderjaren) aan Chengxin, uit Pilgangoora; geen land of fabriek genoemd. https://smallcaps.com.au/article/pilbara-minerals-boosts-lithium-exports-chengxin-ganfeng-offtake-agreements
[4] mining.com — Pilbara Minerals upgrades offtake deal with Chengxin (85 kt CY24, 150 kt/j CY25–CY26), via zoekresultaat. https://www.mining.com/?p=1138914
[5] Reuters, 24-9-2021 — Chengxin/Tsingshan US$ 350 mln lithiumproject in Indonesië (titel uit het ketenontwerp; pagina niet te openen vanuit deze sessie). https://www.reuters.com/world/chinas-chengxin-tsingshan-team-up-350-mln-indonesia-lithium-project-2021-09-24/
[6] Eigen brief `v2/design/routebrieven/lithium-pilgangoora-gwangyang.md` — ankers plant/Utah Point, wegbenen, aanloop Utah Point; bronnen daar [1]–[6] (PLS, Pilbara Ports Authority, Ventia, PHIC).
[7] Eigen brief `v2/design/routebrieven/nikkel-morowali-quzhou.md` — IMIP-exporthaven −2,8480/122,1980, zeeknoop 5491 op 92,9 km, aanloop IMIP.
[8] OpenStreetMap (ODbL) via Nominatim — landuse "Indonesia Morowali Industrial Park" way/299975400, −2,8368/122,1640 (zoekpunt uit het ketenontwerp). https://www.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py` (z16) — `v2/build-cache/satcheck/sat-lithium-pilgangoora-morowali-imip-kade.png`.
[10] PLS, Pilgangoora Operation. https://www.pls.com/assets/pilgangoora-operation

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 19)
`v2/data/stroomroute-lithium-pilgangoora-morowali.json` (27,2 KB, versie 2, lonlat, modaliteiten truck + zee) via `bash v2/tools/bak_stromen.sh lithium-pilgangoora-morowali` (functie `bak_lithium_pilgangoora_morowali`). **6 benen, 2.728,5 km, 1.240 punten, 3 markers; stippel 176,5 km (6,5 %).** Naden overal 0,000 km; markers 0,0 km van de lijn.

| # | modaliteit | km | geometrie | stippel |
|---|---|---|---|---|
| 1 | truck | 136,5 | letterlijke kopie `…-gwangyang-weg-plant-southhedland.geojson` (826 punten) | nee |
| 2 | truck | 0,4 | OSM-graafgat South Hedland (0,355 km), kopie uit pilgangoora-gwangyang | ja |
| 3 | truck | 8,7 | letterlijke kopie `…-gwangyang-weg-southhedland-utahpoint.geojson` | nee |
| 4 | zee | 80,5 | haven-aanloop Utah Point, letterlijke kopie `…-gwangyang-aanloop-utahpoint.geojson` | ja |
| 5 | zee | 2.406,8 | MARNET zeeknoop Hedland (-19,6000/118,6000) naar zeeknoop IMIP 5491 (-2,0357/122,0017), snap 0,000 km aan beide kanten; 10 MARNET-edges, 246 punten | nee |
| 6 | zee | 95,6 | haven-aanloop IMIP, OMGEDRAAIDE kopie `lithium-pilgangoora-morowali-aanloop-imip.geojson` (42 punten, kade als laatste punt) | ja |

**Recept:** b1 tot en met b2a zijn byte-gelijk aan de bak van pilgangoora-gwangyang (geen wegscan, geen profiel, geen extract). b2c: het nikkel-bestand loopt kade naar zeeknoop (vertrek); json laden, coordinates omkeren, als eigen FeatureCollection wegschrijven (het nikkel-bestand is niet gewijzigd). b2b met `--max-snap 25`.

**Toelichting.** Stippel betekent hier alleen "hier reikt het net niet": het OSM-gat bij South Hedland (0,355 km) en de twee haven-aanlopen (MARNET reikt niet tot Utah Point en niet tot de IMIP-kade; bestaande aanlopen 80,5 en 95,6 km tegen de 79,7 en 92,9 km hemelsbreed van de zeeknoop-meting). De 2.406,8 km zee is gemeten (verhouding 1,21 op de 1.988 km hemelsbreed: Timorzee, Banda-zee, Tolobaai); er is geen gepubliceerde zeekm, dus geen +-15%-toets op b5. De 136,5 km wegbeen valt in de brief-band 120-140 km. Geen luchtbeen, geen leiding, geen spoor, geen last mile; de lijn eindigt op de IMIP-kade.

**Bevindingen.** (1) `toets_knikken`: 16 knikken, waarvan 1 terugloop (172 graden, -20.4084/118.5985, in b1): dat is de bestaande wegscan van pilgangoora-gwangyang, hier letterlijk gekopieerd; niet aangeraakt. (2) Zee-knik 63,7 graden bij -8.385/125.299 met boogstraal 8,75 km (krappe bocht in de Banda-zee, geen omkering). (3) `toets_rechte_benen --min-km 5`: geen treffer voor deze stroom. (4) Het volume (20 kt LCE/j) blijft afgeleid; "aannemelijk: een bron" staat in de beennaam van b5 en in §3/§7.

**Lessen.** Een aankomst-aanloop hergebruiken van een vertrek-aanloop vraagt een omkering van de coordinaten; de bake zelf controleert de richting niet, de naad (0,000 km) wel. `bak_stromen.sh` na de edit: 0 CRLF, `bash -n` schoon.
