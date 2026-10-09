# Routebrief (licht) · gas — Ras Laffan (Qatar) → Dahej (India)

**stroom-id:** `gas-raslaffan-dahej` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** Aardgas uit het North Field gaat via de offshore verzamelleiding naar Ras Laffan, wordt er
tot LNG verwerkt (QatarEnergy LNG), vaart als LNG-tanker door de Perzische Golf, de Straat van Hormuz, de
Arabische Zee en de Golf van Khambhat naar de Petronet-terminal bij Dahej (Gujarat), waar het wordt hervergast.
**Welke as van het verhaal:** *de structurele Qatar→India-route, op dit moment geblokkeerd* — Petronet heeft
sinds 2004 een langlopend contract met RasGas/QatarEnergy (7,5 Mtpa [3]) en tekende op 6 feb 2024 een vernieuwing
van 7,5 Mtpa voor 2028–2048 [1] ≈ **10,2 bcm/j** (1 Mt LNG ≈ 1,36 bcm; peiljaar contract 2028–2048); Dahej zelf
17,5 Mtpa nominaal ≈ 23,8 bcm/j [1][8]. **Actualiteit:** QatarEnergy heeft sinds maart 2026 force majeure op
LNG (Iran-oorlog, Hormuz), Petronet zag 56 Qatarse ladingen verstoord en had op 13 aug 2026 "geen definitief plan
voor september" [4]. De lijn tekent dus de handelsroute, geen lopende stroom.

## 1 · Ketenkaart
```
North Field (offshore, geen site-anker — §7)
  ──(b1 leiding · offshore verzamelleiding · 84,7 km, stippel — letterlijke kopie van gas-raslaffan-chiba)──►
Ras Laffan LNG-laadkade `gas-raslaffan-kade` (hergebruikt)
  ──(b2 zee · haven-aanloop Ras Laffan · 41,6 km, stippel-geojson — letterlijke kopie van gas-raslaffan-chiba)──►
zeeknoop 4090 (26.3000, 51.6000)
  ──(b3 zee · Golf → Hormuz → Arabische Zee → Golf van Khambhat · MARNET · 2.404,6 km gemeten)──►
zeeknoop 6394 (21.4019, 72.3917)
  ──(b4 zee · haven-aanloop Dahej · ~34,5 km, stippel-geojson)──► Dahej LNG-steiger `gas-dahej-kade`
  ··· trestle ~2,7 km naar het tankpark `gas-dahej-term` (zelfde terminal, geen eigen been) ···
stoppunt: Petronet-terminal Dahej (regas, invoeding GAIL/landelijk net)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | leiding | North Field → Ras Laffan-kade | offshore verzamelleiding (kopie gas-raslaffan-chiba b1) | 84,7 (gemeten in chiba; ontwerp ~80) | letterlijke kopie `--stippel` | ja — subsea, niet gekarteerd |
| b2 | B | zee | Ras Laffan-kade → zeeknoop 4090 | haven-aanloop, kade 41,5 km van de zeeknoop | 41,6 (gemeten in chiba) | letterlijke kopie `gas-raslaffan-chiba-aanloop-raslaffan.geojson` | ja — haven-aanloop |
| b3 | B | zee | zeeknoop 4090 → zeeknoop 6394 | Perzische Golf, Hormuz, Arabische Zee, Golf van Khambhat | 2.404,6 gemeten; geen gepubliceerde zeekm gevonden, hemelsbreed 2.181 km | MARNET | nee; **structurele route, QatarEnergy-force majeure sinds maart 2026** |
| b4 | B | zee | zeeknoop 6394 → Dahej-steiger | haven-aanloop Golf van Khambhat | 34,5 (maak_havenaanloop, 0,00 km over land) | stippel-geojson | ja — haven-aanloop |

Fase C vervalt: tankpark en regas liggen op hetzelfde terrein als de steiger (trestle ~2,7 km), geen OSM-leiding
gevonden/nodig. Fase D/E vervallen: geen bron noemt één specifieke afnemer van deze Qatarse ladingen [1][4].

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gas-raslaffan-kade` | overslag leiding → zee | Ras Laffan LNG-laadsteiger (QatarEnergy) | 25.9265, 51.5955 | **hergebruikt letterlijk** uit `gas-raslaffan-chiba.md` §3 [6] | bron-gelegd (z16 in chiba: kade-eiland met opslagtanks en trestle-wegen) |
| `gas-dahej-kade` | losplek LNG-carrier | Petronet LNG-steiger Dahej, pier-kop | 21.6694, 72.5095 | [2][3][9] | bron-gelegd (z16 gezien: LNG-carrier afgemeerd aan de pier-kop van een ~2 km lange trestle naar het tankpark; tweede steiger 500 m noordelijker) |
| `gas-dahej-term` | regas, stoppunt | Petronet LNG Dahej, tankpark | 21.67498, 72.53532 | **hergebruikt letterlijk** uit sitelaag `w-dahej` [8] | bron-gelegd (z15 gezien: tankpark met ~7 grote cilindrische LNG-tanks, trestles naar zee) |

## 4 · Via-punten
Geen — geen landbeen; de zee loopt kade → kade over MARNET en twee haven-aanlopen.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Ras Laffan LNG-complex | QatarEnergy LNG | pijpleidinggas → LNG | ~77 Mtpa, >126 Mtpa na uitbreiding ≈ 104,7–171,4 bcm/j | [6] |
| Dahej LNG-terminal | Petronet LNG | LNG → hervergast gas → net | 17,5 Mtpa ≈ 23,8 bcm/j; berthing 270 m LOA, 17 m diepgang | [1][2][8] |

## 6 · Stoppunt
De brief stopt bij het tankpark van de Dahej-terminal: geen bron koppelt een Qatarse lading aan één afnemer
stroomafwaarts (hervergast gas gaat het landelijke net in).

## 7 · Open punten
- **Geen site-anker voor het North Field** (offshore, gedeeld met Iran): fase A is gedeeld open punt met chiba/rotterdam.
- **Kade-anker wijkt 310 m af van het toets-kandidaatpunt** 21.6695, 72.5065: dat punt ligt in open water naast de
  pier; het satelliet-gelegde anker is de pier-kop met de carrier. Aanloop gemeten tot dit anker: 34,5 km, 0,00 km over land.
- **Welke van de twee LNG-steigers (jetty 1 of 2) dit is** staat niet in de bronnen; beide liggen < 500 m uit elkaar.
- **Geen gepubliceerde zeekm Ras Laffan→Dahej**: de ±15%-toets is hier een indicatie (hemelsbreed 2.181 km zeeknoop→zeeknoop; gemeten 2.404,6 = +10%).
- **Contractvolume 7,5 Mtpa is contractueel, geen geleverd volume**; actuele leveringen liggen sinds maart 2026 veel lager
  (force majeure, verlengd tot oktober/november 2026 volgens [10], niet zelf kunnen lezen: HTTP 403).
- Dahej wordt ook uit Gorgon, VS, Nigeria en Angola gevuld; dat valt buiten deze keten.
- **Marker `gas-dahej-term` ligt 2,7 km van de lijn** (anker ≠ routeerpunt: de trestle is geen been); bewust zo.

## 8 · Bronnen
[1] Wikipedia, "Petronet LNG" — Dahej 17,5 Mtpa; deal met QatarEnergy 6 feb 2024, 7,5 Mtpa 2028–2048, vernieuwing van het bestaande contract. https://en.wikipedia.org/wiki/Petronet_LNG
[2] Wikipedia, "Dahej" — 21,700 N 72,533 E; Petronet-steiger, berthing 270 m LOA / 38 m breedte / 17 m diepgang. https://en.wikipedia.org/wiki/Dahej
[3] LNG Industry, 3 dec 2014 — eerste Q-Max van Ras Laffan naar Dahej, tweede LNG-steiger; RasGas-contract 7,5 Mtpa (SPA 2004). https://www.lngindustry.com/lng-shipping/03122014/Q-Max-cargo-delivered-to-Dahej-LNG-terminal-1904
[4] Baird Maritime/Reuters, 13 aug 2026 — Qatar-force majeure sinds maart, 56 ladingen verstoord, geen plan voor september. https://www.bairdmaritime.com/shipping/tankers/gas/still-in-limbo-indias-petronet-lng-awaits-clear-gas-supply-commitments-from-qatar
[5] All India Radio, 19 jun 2026 — LNG-tanker Disha (62.370 t) van Ras Laffan door Hormuz naar Dahej. https://newsonair.gov.in/indias-lng-tanker-disha-arrives-at-dahej-port-in-gujarat-after-crossing-strait-of-hormuz/
[6] Routebrief `gas-raslaffan-chiba.md` (+ `gas-raslaffan-rotterdam.md`) — Ras Laffan-anker, kopie-benen b1/b2, zeeknoop 4090.
[7] Haalbaarheidstoets keten (M31 golf 8): zeebeen 2.404,6 km, haven-aanloop Dahej gelukt, kandidaatpunt jetty.
[8] `v2/design/gas-sitelaag.json` — site `w-dahej` 21.67498, 72.53532 (Wikidata Q30972154, z14 gezien).
[9] Esri World Imagery via `v2/tools/sat_check.py` — `sat-gas-raslaffan-dahej-jetty.png` (z14), `-term.png` (z15), `-pier.png` (z16).
[10] GasProcessingNews, jul 2026, "QatarEnergy extends LNG force majeure …" (via haalbaarheidstoets; niet zelf geladen). https://gasprocessingnews.com/news/2026/07/qatarenergy-extends-lng-force-majeure-and-charters-out-tankers-into-october/

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
Functie `bak_gas_raslaffan_dahej` in `v2/tools/bak_stromen.sh`; bestand `v2/data/stroomroute-gas-raslaffan-dahej.json` (7,1 KB, contract versie 2, lonlat). Totaal 2.565,4 km · 4 benen · 326 punten · 3 markers.

| # | modaliteit | km | stippel | wat |
|---|---|---|---|---|
| b1 | leiding | 84,7 | ja | offshore verzamelleiding North Field → Ras Laffan-kade, letterlijke kopie van de stippel in gas-raslaffan-chiba (26.6191,51.9500 → 25.9265,51.5955) |
| b2 | zee | 41,6 | ja | haven-aanloop Ras Laffan, letterlijke kopie `gas-raslaffan-chiba-aanloop-raslaffan.geojson` (20 punten) |
| b3 | zee | 2.404,6 | nee | MARNET zeeknoop 4090 → 6394, 250 punten, snap 0,000 km aan beide kanten |
| b4 | zee | 34,5 | ja | haven-aanloop Dahej, `gas-raslaffan-dahej-aanloop-dahej.geojson` (54 punten, 0,00 km over land), niet opnieuw gedraaid |

**Markers (3):** gas-raslaffan-kade 25.9265,51.5955 · gas-dahej-kade 21.6694,72.5095 · gas-dahej-term 21.67498,72.53532. Kade-markers liggen 0,0 km van de lijn; gas-dahej-term ligt 2,74 km van de lijn (bewust: de trestle is geen been).

**Toets.** Naden alle 0,00 km (geen naad > 5 km). Km-toets: geen gepubliceerde zeekm; gemeten 2.404,6 tegen hemelsbreed 2.181 (+10%), dus een indicatie, geen norm. toets_knikken: 1 knik van 60,9 graden (20.1771,70.8646, krappe bocht bij de Kathiawar-kust, 0 omkeringen, 0 terugloop). toets_rechte_benen: alleen b1 (rechte stippel met reden: subsea) en b2 (aanloop-kopie, omwegfactor 1,002) vallen op, beide stippel met reden. json.load, versie 2, lonlat, modaliteiten geldig, elk been >= 2 punten.

**Toelichting stippels.** b1: subsea, niet gekarteerd, kop is een schematisch veldpunt zonder site-anker (§7). b2 en b4: MARNET reikt niet tot de kade (Ras Laffan 41,5 km van zeeknoop 4090; Dahej-steiger 34,5 km van zeeknoop 6394), kortste pad over water. Het doorgetrokken b3 is een gemeten been; de structurele route (QatarEnergy-force majeure sinds maart 2026) staat in de beennaam, niet in de lijnstijl.

**Lessen.** (1) Twee van de vier benen zijn letterlijke kopieen uit de chiba-stroom: geen tweede versie, de beennaam zegt dat. (2) De bake draaide in 15 s omdat de havenaanloop al klaarstond. (3) Geen register- of bundelwijziging door de bak-agent; centraal registreren met sleutel gas-rd.
