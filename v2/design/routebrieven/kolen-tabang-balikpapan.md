# Routebrief (licht) · Kolen · Tabang → Senyiur → Balikpapan (Indonesië)

**stroom-id:** `kolen-tabang-balikpapan` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** thermische kolen uit de Bayan-dagbouw Tabang/Pakar (Kutai Kartanegara, Oost-Kalimantan) gaan per **truck** over Bayan's
asfalt-haulroad en openbare weg (69 km gepubliceerd) naar de bargeterminal Senyiur aan de Kedang Kepala, per **binnenvaart** (barge) via de
Mahakam en haar delta naar de zee, en per **zeeschip/kustvaart** (±120 km, Straat Makassar) naar Bayan's Balikpapan Coal Terminal (BCT) in de
baai van Balikpapan, waar de kolen op oceaanschepen worden overgeslagen (aannemelijk: Senyiur → BCT is in geen bron expliciet). Stoppunt = BCT.
**Welke as van het verhaal:** *Bayan's integrale logistieke keten Tabang → Mahakam → Balikpapan* (mijn → rivier → transshipment). Bayan produceerde
**45+ Mt in 2023** (Bayan-site [6]); Bara Tabang **50,5 Mt in 2024** (GEM, sitelaag `w-bara-tabang`); Tabang/Pakar is ~80% van Bayan's productie [1].
Het volume van déze as is niet gepubliceerd: Tabang-kolen verlaten de mijn ook via Muara Pahu en BCT is "not dedicated to any one mine" [3]; Senyiur
laadt 12.000 t/u en wordt op 20 Mt/j geschat [2][7]. Eenheid Mt kolen per jaar; de 50,5 Mt is een **bovengrens** voor de as, geen asvolume.

## 1 · Ketenkaart
```
Tabang/Pakar-dagbouw `kolen-tabang-laad`
   ──(b1 truck · Bayan-haulroad + openbare weg, service/unclassified · 69 km gepubliceerd [5][8], OSM 71,1)──►
Senyiur-bargeterminal `kolen-senyiur-kade`
   ──(b2 binnenvaart · Kedang Kepala → Mahakam → delta · 299,1 km gemeten, niet gepubliceerd, aannemelijk: één bron)──►
Mahakam-monding `kolen-mahakam-monding` ──(b3 zee · stippel 21,7 km naar de zeeknoop · b4 zee MARNET 120,4 km)──►
Balikpapan Coal Terminal `kolen-bct-kade` ⏹ stoppunt (barge → oceaanschip, KFT-drijvers niet gelokaliseerd)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `kolen-tabang-laad` → `kolen-senyiur-kade` | Bayan-haulroad (asfalt) + openbare weg; niet de 101 km-weg naar Muara Pahu [4] | **69** [5][8]; OSM 71,1 (+3,0%) | `maak_stroombeen_weg` via `wegscan_puur.py`, extract `indonesie` | nee |
| b2 | B | binnenvaart | `kolen-senyiur-kade` → `kolen-mahakam-monding` | Kedang Kepala → Mahakam → delta (Wikipedia [9]) | **299,1 gemeten; geen gepubliceerde km** — ±15%-toets is indicatie | `maak_rivierbeen` over de bulklaag | nee — maar begint 2,4 km stroomopwaarts van het anker (bulkknoop 16513, naad < 5 km) |
| b3 | B | zee | `kolen-mahakam-monding` → zeeknoop 5447 | delta-front → open water | 21,7 hemelsbreed | rechte stippel (of `maak_havenaanloop`) | ja — MARNET reikt niet tot de monding |
| b4 | B | zee | zeeknoop 5447 → `kolen-bct-kade` | kustvaart Straat Makassar → baai van Balikpapan | **120,4 MARNET**; geen gepubliceerde km (aannemelijk) | MARNET, 3 edges, snap kade 2,9 km | nee (BCT-snap < 5 km: geen aanloop) |

Totaal gemeten ≈ 512 km (71 + 299 + 22 + 120). De 640 km van Kangaroo (MCM → BCT) hoort bij een andere mijn, die veel verder stroomopwaarts laadt (Long Hubung) [8]: **geen maatstaf**.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-tabang-laad` | mijn | Tabang/Pakar-dagbouw (Bayan) — **hergebruik** sitelaag `w-bara-tabang` | 0.5509, 116.1263 | [1], GEM-sitelaag | bron-gelegd (z14 gezien: kruis op de rand van de wingat-put, ICF/stockpile 1,5 km ZO, haulroad oostwaarts) |
| `kolen-senyiur-kade` | overslag truck → barge | Senyiur-bargeterminal (Bayan), conveyors naar de oeverlaadplek | 0.2930, 116.6280 | [2][10] | bron-gelegd (z16 gezien: groot kolenveld, conveyors naar de rivieroever, beladen kolenbarges langszij op de Kedang Kepala; dorpsnode OSM 0.3115/116.6242 ligt 2,1 km N) |
| `kolen-mahakam-monding` | routepunt (geen overslag) | Mahakam-delta, buitenrand | -0.8265, 117.5006 | [11] | aannemelijk (z12 gezien: deltafront, punt in water bij de slibpluim; routeknoop van de bulklaag, geen site) |
| `kolen-bct-kade` | overslag barge → oceaanschip | Balikpapan Coal Terminal, steiger met shiploader | -1.1955, 116.7830 | [3][10] | bron-gelegd (z16 gezien: bulker langszij de steiger, conveyors naar twee kolenvelden, bargeberths 0,4 km ZZO; OSM-landuse `way/1548261240` -1.1970/116.7883 ligt 0,5 km ONO op het kolenveld) |
Bayan-coördinaten BCT: 01°12′00″S 116°46′60″E = -1.2000/116.7833 [3] (afgerond, 0,5 km mis); `way/1548261240` en het z16-beeld wegen zwaarder.

## 4 · Via-punten (b1 — alleen wegbeen)
Alle zes liggen op doorgaande OSM-ways van de kortste route (`wegscan_puur`-scan Indonesië-pbf, 71,1 km; alleen `service`/`unclassified`, dus profiel met `corridorKlassen`).
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | haulroad-oost bij de ICF (way 581752770/993562729) | 0.5341, 116.1621 | pint het begin van de oostwaartse haulroad (5,4 km) tegen de vele put- en padwegen rond Tabang |
| b1 | 2 | bocht oost → zuid (way 993576937 → 991894637) | 0.5190, 116.2261 | pint het draaipunt (13,4 km) naar de zuidelijke doorgaande weg |
| b1 | 3 | begin lange `unclassified` (way 613748205, 17,4 km) | 0.4914, 116.2376 | pint de lange doorgaande tak (16,8 km) |
| b1 | 4 | overgang `unclassified` → `service` (way 992615191 → 582011286) | 0.3657, 116.3670 | pint het wegtype-wisselpunt (39,1 km) |
| b1 | 5 | knoop `service` (way 582226745 → 616508099) | 0.3277, 116.4951 | pint het midden van de laatste lange tak (54,2 km) |
| b1 | 6 | laatste aanloop Senyiur (way 616475349) | 0.2967, 116.6257 | pint de aanloop 0,5 km vóór de kade (70,3 km), langs het kolenveld |
Via-punten b2–b4: geen (rivier en zee routeren zelf). Geofabrik-extract voor b1: `indonesie`. Geen spoor.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Senyiur-jetty | Bayan Group | truck → barge (7.500 t, 300 ft) | 3 barge-loaders 12.000 t/u; crushing 10.000 t/u; stockpile 1,5 Mt; ~20 Mt/j na uitbreiding | [2][7] |
| Balikpapan Coal Terminal | Bayan Group | barge → oceaanschip (tot Panamax vol, Capesize aangevuld) | 7 grijpers (5 × 1.000 + 2 × 1.500 t/u), 2 shiploaders 8.000 t/u, stockpile 1,5 Mt | [3] |
| KFT-1 / KFT-2 | Bayan Group | drijvend overslagstation, barge → Capesize | 40 kt / 60 kt opslag, 4.000 / 6.000 t/u; "bij Balikpapan", geen coördinaat | [4] |

## 6 · Stoppunt
De brief stopt bij BCT: kolen worden daar van barge op oceaanschip overgeslagen en de bestemming van het oceaanschip is niet gedocumenteerd (geen fase D/E; zelfde afbakening als `kolen-sangatta-mundra`).

## 7 · Open punten
- **Senyiur → BCT staat in geen bron expliciet** (alleen dat Bayan beide bezit en BCT "not dedicated to any one mine" is [3]); een deel kan naar KFT-1/2 of rechtstreeks naar andere afnemers gaan. Beenstatus *aannemelijk*.
- **Het echte eindpunt kan een drijvend station (KFT) zijn**; Bayan geeft alleen "near Balikpapan" [4]. Niet getekend; BCT is de gelegde kade.
- **Barge-km niet gepubliceerd**: 299,1 km (Senyiur → delta) + 120,4 km (kust) zijn gemeten, niet bevestigd. Het bulknet kent één Mahakam-pad naar de delta; een alternatieve uitstroom is niet onderzocht.
- **Rivierbeen begint 2,4 km stroomopwaarts van het anker** (bulknet heeft geen knoop tussen Senyiur-dorp en 0.27 N). Naad < 5 km; meld bij het bakken.
- **Monding → zeeknoop 21,7 km is stippel**: MARNET kent de Mahakam-delta niet; de rechte lijn is schematisch (over open water/slibpluim).
- **Haulroad-profiel zonder gepubliceerde operator-km**: 69 km [5][8] is een Petromindo-opgave over de volledig operationele weg; de 101 km van Bayan [4] gaat naar Muara Pahu en is geschrapt.
- **Gedeeld sitelaag-anker**: `w-bara-tabang` (GEM-centroïde op de putrand) is mijn-anker; geen conflict. Volume per as niet gepubliceerd.
- Geen leiding, geen spoor, geen vlucht.

## 8 · Bronnen
[1] Bayan Resources, Tabang/Pakar mine (12 IUP's, ICF, Senyiur en Muara Pahu, asfalt-haulroad naar Senyiur). https://www.bayan.com.sg/tabang-pakar-mine
[2] Bayan, Senyiur Jetty (Kedang Kepala, 12.000 t/u, 1,5 Mt, 300 ft-barges). https://www.bayan.com.sg/senyiur-jetty
[3] Bayan, Balikpapan Coal Terminal (01°12′S 116°47′E, grijpers, shiploaders, 1,5 Mt, niet mijn-gebonden). https://www.bayan.com.sg/balikpapan-coal-terminal
[4] Bayan, KFT-1 en KFT-2 (drijvende overslag "near Balikpapan") en 101 Km Haul Road (Tabang → Muara Pahu). https://www.bayan.com.sg/kft-1-and-kft-2 · https://www.bayan.com.sg/101-km-haul-road-and-public-road
[5] Petromindo, 2015-11-02 — "Bayan's new 69km coal haul road from Tabang … to Senyiur Port … fully operational". https://www.petromindo.com/news/article/kangaroo-expects-senyiur-port-expansion-to-complete-fourth-quarter
[6] Bayan, startpagina — productie 2023 45+ Mt. https://www.bayan.com.sg/
[7] Petromindo, 2016-06-10 — Senyiur-stockpile-uitbreiding, 69-km-weg, 2.000 → 4.000 t/u, 20 Mt/j. https://www.petromindo.com/news/article/bayan-to-complete-stockpile-expansion-at-senyiur-port-in-q2
[8] Petromindo, 2015-04-30 — Kangaroo: barging MCM → BCT ±640 km langs de Mahakam (andere mijn, indicatie). https://www.petromindo.com/news/article/kangaroo-barging-of-coal-from-mcm-to-bct-has-recommenced
[9] Wikipedia, Mahakam River — Kedang Kepala vloeit in de Mahakam; delta ~1.800 km². https://en.wikipedia.org/wiki/Mahakam_River
[10] OpenStreetMap (ODbL) via Nominatim — Senyiur dorp node 1308630342 (0.3115/116.6242); BCT-landuse way 1548261240 (-1.1970/116.7883).
[11] Global Energy Monitor via `v2/design/kolen-sitelaag.json` (`w-bara-tabang`, 50,5 Mt 2024). (geen losse url; GEM Global Coal Mine Tracker, zoals in de sitelaag).
[12] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-kolen-tabang-balikpapan-{tabang-z14,senyiur-z14,senyiur-z16,bct-z14,bct-z16,delta-z13}.png`.
[13] Meetruns 2026-10-29: `wegscan_puur`-scan Indonesië-pbf (way-id's §4, 71,1 km), `maak_rivierbeen` (299,1 km, bulkknopen 16513/17189), `hecht_marnet route` (zee 120,4 km, snap BCT 2,9 km, monding → zeeknoop 5447 21,7 km).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`bash v2/tools/bak_stromen.sh kolen-tabang-balikpapan` → `v2/data/stroomroute-kolen-tabang-balikpapan.json` (50,7 KB, versie 2, lonlat). Totaal 513,4 km · 2.663 punten · 4 markers.

| # | modaliteit | km | naad | recept |
|---|---|---|---|---|
| b1 | truck | 71,4 (brief 69 gepubliceerd, +3,0% = binnen ±15%) | 0,00 | profiel `kolen-tabang-balikpapan-tabang-senyiur` (indonesie, corridorKlassen service+unclassified, 6 via-punten, ongewijzigd uit §4), `wegscan_puur.py` 432 s, snap plant 0,25 / kade 0,10 km |
| b2 | binnenvaart | 298,9 (brief 299,1; geen gepubliceerde km) | 2,43 | `kolen-tabang-balikpapan-rivier-senyiur-delta.geojson` (maak_rivierbeen, hergebruikt uit de briefrun) |
| b3 | zee, **stippel** | 22,7 | 0,00 | `maak_havenaanloop.py` (kortste pad over water, 0,00 km over land, omwegfactor 1,05) monding -0.8265,117.5006 → zeeknoop 5447 |
| b4 | zee | 120,4 | 0,00 | MARNET `--been` zeeknoop 5447 (-0.9887,117.6086) → BCT-kade, 3 edges, snap kade 2,95 km |

Markers: 4 (§3). Tabang, Senyiur en monding liggen 0,0 km op de lijn; de BCT-marker ligt **2,95 km** van het lijneinde (zie lessen).
Toetsen: `toets_knikken` 0 omkeringen, 0 terugloop (69 knikken >= 60 gr, 60 daarvan in het rivierbeen, 8 in de weg); `toets_rechte_benen --min-km 5` meldt dit bestand niet; stippel alleen b3 en dat is een echt over-water-pad.

**Toelichting stippel b3:** MARNET kent de Mahakam-delta niet; de lijn is een schematisch pad over water (geen land gekruist), geen gemeten vaargeul.
**Lessen / bevindingen:**
- De BCT-marker staat 2,95 km van het einde van b4 (de lijn eindigt op zeeknoop 5448, -1.2208,116.7751). Snap < 5 km, dus geen haven-aanloop volgens de handleiding; het is wel buiten de ~0,5 km-norm voor markers. Bevinding, niet dichtgetrokken.
- Naad b1 → b2 = 2,43 km (rivierbeen begint stroomopwaarts van het kade-anker, zoals in §7 aangekondigd); binnen de 5 km-norm.
- Km van b2 en b4 zijn gemeten, niet gepubliceerd; de ±15%-toets geldt alleen voor b1 als norm.
- Het stroom-id noemt Balikpapan en de keten eindigt ook bij BCT in Balikpapan: id en eindpunt kloppen, geen afwijking.
- Geen herbak van bestaande stromen, geen register- of bundelwijziging (centraal).
