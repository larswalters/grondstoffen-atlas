# Routebrief (licht) · koper — Ok Tedi (Tabubil) → Kiunga → Port Moresby (Papoea-Nieuw-Guinea)

**stroom-id:** `koper-oktedi-portmoresby` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Titel:** Koper · Ok Tedi → Kiunga → Port Moresby (Papoea-Nieuw-Guinea)
**Keten in één zin:** koperconcentraat (Cu-Au-Ag) van de Ok Tedi-molen per **slurryleiding** langs de Kiunga-Tabubil Highway naar Kiunga, per **schip** (rivier-zeevaartuigen van P&O) 800+ km de Fly River af, de Golf van Papoea over naar de **silovaartuig-ligplaats Port Moresby**; stoppunt daar, afnemers niet benoemd.
**Welke as van het verhaal:** Papoea-Nieuw-Guinea, een koperstroom die uit het bergland over een rivier naar zee gaat. Volume 106 kt Cu in 2025, 103 kt Cu in 2024 (OTML, eenheid kt Cu per jaar, Cu-inhoud van het concentraat) [7].

## 1 · Ketenkaart
Ok Tedi-molen `cu-oktedi-molen` ──(b1 leiding, stippel · tracé langs de Kiunga-Tabubil Highway · 156,6 km tracé, OTML 156 km)──► Kiunga-haven `cu-kiunga-haven`
──(b2 binnenvaart · Fly River · 803 km gemeten, OTML >850 km)──► Fly-delta (routeerpunt) ──(b3 haven-aanloop, stippel · 131 km over water, MARNET reikt hier niet)──► zeeknoop 2654
──(b4 zee · Golf van Papoea · 374 km)──► zeeknoop 5906 ──(b5 haven-aanloop, stippel · 22 km)──► silovaartuig Port Moresby `cu-portmoresby-silo` (onzeker) ── stoppunt

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | molen → Kiunga-haven | slurryleiding langs de Kiunga-Tabubil Highway via Tabubil en Ningerum (schematisch) | 156 (oktedi.com) [6]; 137 (Wikipedia) [1]; gemeten tracé 156,6 | profiel `koper-oktedi-portmoresby-oktedi-kiunga` → geojson (wegtracé als leiding-stippel) | **ja** — OSM heeft de pijp niet |
| b2 | A | binnenvaart | Kiunga-haven → Fly-delta | Fly River (bulklaag) | >850 (oktedi.com) [6]; gemeten 803,4 (−5,5%) | `maak_rivierbeen.py` | nee |
| b3 | B | zee | Fly-delta → zeeknoop 2654 | — | niet gepubliceerd; gemeten 130,8 | `maak_havenaanloop.py` | **ja** — 120 km van de dichtste zeeknoop |
| b4 | B | zee | zeeknoop 2654 → zeeknoop 5906 | Golf van Papoea [3][4] | niet gepubliceerd; MARNET 374,2 | MARNET | nee |
| b5 | B | zee | zeeknoop 5906 → silo Port Moresby | — | niet gepubliceerd; gemeten 21,9 | `maak_havenaanloop.py` | **ja** — punt ligt 20,6 km van de zeeknoop |

"Aannemelijk": de silo-ligging (b5-einde) en dat al het concentraat dit pad volgt (één bron: OTML-CEO in [3]); dat staat hier, niet in de lijnstijl. b2 en b4 zijn één schip in werkelijkheid (rivier-zeevaartuig, geen overslag in de delta [3][4]).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-oktedi-molen` | mijn / molen | Ok Tedi-molen, Mount Fubilan | -5.2085, 141.1490 | [1] | bron-gelegd (z15 gezien: verwerkingscomplex met gebouwen, schoorstenen en slibvijvers 2,5 km oost van de put). Wikipedia-punt -5.2228,141.1386 en het toets-punt -5.2106,141.1385 liggen in de put zelf (groen meer), niet bij de molen |
| `cu-kiunga-haven` | laadplek / overslag | Kiunga-haven, Fly River | -6.1245, 141.2955 | [1][6] | aannemelijk (z15 gezien: industrieel kadeterrein met witte tank, loodsen en vijvers aan de westoever, het enige industriële waterfront; geen bron met kadecoördinaat) |
| `cu-portmoresby-silo` | losplek (silovaartuig, stoppunt) | silovaartuig-ligplaats, Port Moresby | -9.4640, 147.1400 | [3][4] | **onzeker** (z14/z15 gezien: baai tussen Fairfax Harbour en Napa Napa met twee koopvaarders voor anker; silovaartuig niet te onderscheiden, geen bron met positie). Schematisch ankerpunt, geen vaste ligplaats |
| routeerpunt (geen site) | Fly-delta | einde rivierbeen | -8.6104, 143.4130 | eigen meting | z12 gezien: vertakt estuarium met zandbanken; punt is het uiteinde van het rivierbeen, geen overslag |

Satellietbeelden (prefix `koper-oktedi-portmoresby-`, in `v2/build-cache/satcheck/`): `sat-…-cu-oktedi-molen.png` (z14), `…-molen-z15.png`, `…-cu-kiunga-haven.png` (z15), `…-cu-portmoresby-haven.png` (z14), `…-portmoresby-ankerplaats.png` (z15), `…-cu-flymond-routeerpunt.png` (z12).

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Ok Tedi-molen | -5.2085, 141.1490 | begin (anker) |
| b1 | 2 | Ningerum, Kiunga-Tabubil Highway | -5.6720, 141.1418 | zonder dit punt kiest de router een 148 km-weg die 21 km van Ningerum afligt; de pijp volgt de Highway "through Ningerum" [2] |
| b1 | 3 | Kiunga-haven | -6.1245, 141.2955 | einde (anker) |
Dit is geen wegbeen maar het tracé van een leiding: de weggeometrie dient als schematische stippel. Het wegprofiel staat al in `maak_stroombeen_weg.py`; extract `papoea-nieuw-guinea`. b2 (rivier) en zee hebben geen via-punten.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ok Tedi-molen | Ok Tedi Mining Ltd (OTML) | erts → Cu-Au-Ag-concentraatslurry | 106 kt Cu in 2025 (productie) | [7] |
| Kiunga-haven | OTML | slurry → gedroogd concentraat op schip | niet gevonden | [6][8] |
| silovaartuig Port Moresby | OTML | concentraat → ladingopslag voor overzeese schepen | tot 50.000 t (oktedi.com, silo bij de rivier) [6] | [3][6] |

## 6 · Stoppunt
De brief stopt bij het silovaartuig in Port Moresby: OTML zegt alleen "verkocht aan smelters in Azië en Europa" en geen bron noemt een smelter of overzeese haven [6]; fase D en E vervallen.

## 7 · Open punten
- **Silovaartuig-positie en naam:** alleen een OTML-citaat uit 2022 ("silo vessel in Port Moresby") [3]; ligplaats niet gevonden, punt is schematisch. Oudere bronnen zetten het silo in de riviermond [6][8]: huidige stand onbevestigd.
- **Pijp niet in OSM** (pyosmium-scan: alleen een waterleiding van 2,3 km): b1 is een stippel langs de weg. Wikipedia zegt pijp "tot Bige" [2], OTML tot Kiunga [6]; Bige ligt ~10 km van het tracé, niet gelegd.
- **Fly-delta → zee:** het werkelijke vaarwater (rivier-zee-overgang) is niet gebronnen; het routeerpunt is een meting van het rivierbeen.
- **Afnemer, smelter en aandeel Port Moresby:** niet gevonden; geen volume per been.
- **Sitelaag mist Ok Tedi** (centraal; 106 kt Cu in 2025).
- **Kiunga-kade:** exacte filter- of laadkade niet gebronnen (aannemelijk, z15).
- Laagwater op de Fly onderbreekt de vaart soms (NBC PNG, 2026, zoekresultaat) [9].

## 8 · Bronnen
[1] Wikipedia, "Ok Tedi Mine" (molen naast de put, slurry 137 km langs de Kiunga-Tabubil Highway naar Kiunga, bargevervoer), https://en.wikipedia.org/wiki/Ok_Tedi_Mine
[2] Wikipedia, "Kiunga-Tabubil Highway" (~137 km via Ningerum en Tabubil, pijp langs de hele weg "down to Bige", verhard tot km 25 per 2024-12-17), https://en.wikipedia.org/wiki/Kiunga-Tabubil_Highway
[3] Dry Cargo Magazine, "P&O ML takes possession of new bespoke vessels..." (2022-09-27; Kiunga naar Port Moresby via Fly River en Golf van Papoea, OTML-CEO: silovaartuig in Port Moresby), https://www.drycargomag.com/p-and-oml-takes-possession-of-new-bespoke-vessels-designed-to-support-copper-export-in-papua-new-guinea
[4] P&O Maritime Logistics, zelfde bericht (mv Fly Enterprise en Fly Valiant, 5.400 dwt, OTML-vloot 11), https://pomaritime.com/?p=1748
[5] The National (PNG), 2022-09-14 (mv Fly Enterprise verwelkomd in Port Moresby op 2022-09-13; >17 Mt concentraat verscheept sinds 1984), https://www.thenational.com.pg/?p=406935
[6] OTML, Logistics (via zoekfragment; pagina zelf geeft 403/Cloudflare): pijp 156 km, bargevaart >850 km, silovaartuig 50.000 t, smelters in Azië en Europa, https://oktedi.com/logistics
[7] OTML persberichten (via zoekfragment): 2024 = 103.246 t Cu, https://www.oktedi.com/?p=8156 ; 2025 = 106.018 t Cu, https://www.oktedi.com/?p=9692
[8] rettet-die-elbe.de, "Kiunga River Port" (oudere secundaire bron: bargeladingen 2.500 t naar silo in de riviermond), https://www.rettet-die-elbe.de/oktedi/kiunga.htm
[9] NBC PNG, "Ok Tedi Mine stays fully operational despite dry weather, low Fly River levels" (via zoekfragment), https://www.nbc.com.pg/post/36915/ok-tedi-mine-stays-fully-operational-despite-dry-weather-low-fly-river-levels
[10] OSM/Nominatim (Tabubil -5.2717,141.2256 · Ningerum -5.6720,141.1418 · Kiunga -6.1160,141.2982 · Bige-landingsbaan -5.9451,141.1322), geraadpleegd 2026-11-01
[11] Eigen metingen 2026-11-01: `sat_check.py` (zie §3), `maak_stroombeen_weg.py` (156,6 km), `maak_rivierbeen.py` (803,4 km), `maak_havenaanloop.py` (130,8 en 21,9 km), `hecht_marnet.py` (374,2 km) en de haalbaarheidstoets koper-oktedi-portmoresby

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
Bestand `v2/data/stroomroute-koper-oktedi-portmoresby.json` (128,1 KB, versie 2, lonlat) · functie `bak_koper_oktedi_portmoresby` in `bak_stromen.sh` · register centraal: sleutel `cu-opm`.

| # | modaliteit | km | brief | afwijking | stippel |
|---|---|---|---|---|---|
| 1 | leiding (schematisch langs de Highway) | 156,7 | 156 (OTML), 137 (Wikipedia) | +0,4% / +14% | ja, OSM heeft de pijp niet |
| 2 | binnenvaart (Kiunga, Fly River, delta) | 803,5 | >850 (OTML) | -5,5% (ondergrens) | nee |
| 3 | zee, aanloop Fly-delta naar zeeknoop 2654 | 130,8 | niet gepubliceerd | n.v.t. | ja, MARNET reikt niet (120 km) |
| 4 | zee, zeeknoop 2654 naar zeeknoop 5906 (MARNET) | 374,2 | niet gepubliceerd | n.v.t. | nee |
| 5 | zee, aanloop zeeknoop 5906 naar silo | 21,9 | niet gepubliceerd | n.v.t. | ja, ligplaats onzeker |
Totaal 1.487,1 km, 6.578 punten, 3 markers (molen, Kiunga-haven, silovaartuig-ligplaats); naden 0,33 / 0 / 0 / 0 km (max 0,33 km, b1 naar b2: de rivierroute snapt op de bulklaag); markers 0 m van hun lijn.

**Recept:** b1 = profiel `koper-oktedi-portmoresby-oktedi-kiunga` (`maak_stroombeen_weg.py`, extract papoea-nieuw-guinea) als `--stippel-geojson leiding`; b2 = `maak_rivierbeen.py` `--van=-6.1245,141.2955 --naar=-8.60,143.60` als `--been-geojson binnenvaart`; b3 = `maak_havenaanloop.py` -8.6104,143.413 naar -8.5,144.5 als `--stippel-geojson zee`; b4 = `--been zee` -8.5,144.5 naar -9.6008,147.2662 (zeeknoop-coordinaten); b5 = `maak_havenaanloop.py` silo naar zeeknoop 5906, het geojson omgekeerd naar reisvolgorde (`...-aanloop-portmoresby-heen.geojson`).

**Toelichting stippels:** b1 is schematisch: de weggeometrie van de Kiunga-Tabubil Highway (via Ningerum) staat voor de pijp, die OSM niet kent; de lijn loopt dus niet noodzakelijk exact over de pijp (Wikipedia: pijp tot Bige, OTML: tot Kiunga). b3 en b5 zijn haven-aanlopen over water zonder vaargeul; b5 eindigt op een schematisch ankerpunt, geen vaste ligplaats. Geen vlucht, geen letterlijke kopie.

**Toets:** `toets_knikken` 0 omkeringen en 0 terugloop (68 knikken, vooral meanders van de Fly: echte bochten); `toets_rechte_benen` geen recht been; km binnen de norm waar de brief een waarde geeft (b2 -5,5%; b1 +0,4% t.o.v. OTML). Geen last-mile-been: het landbeen eindigt op het site-anker.

**Lessen:** (1) een aanloop aan het EINDE van een keten moet in reisvolgorde staan (zeeknoop naar kade); de bestaande geojson liep kade naar zeeknoop en is omgedraaid in plaats van opnieuw gerekend (`maak_havenaanloop.py` duurde > 2 min); (2) `maak_havenaanloop.py --van=-9.6,...` vraagt de `=`-vorm bij een negatieve breedtegraad.

