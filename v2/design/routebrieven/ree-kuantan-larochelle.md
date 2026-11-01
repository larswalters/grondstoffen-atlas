# Routebrief (licht) · Zeldzame aardmetalen · LAMP Gebeng (Lynas) → Westports → La Pallice → Solvay La Rochelle (Maleisië → Frankrijk)

**stroom-id:** `ree-kuantan-larochelle` · **geschreven:** 2026-11-01 · **werkwijze:** licht (M31 golf 20) · **status:** gebakken
**Titel (bol):** Zeldzame aardmetalen · LAMP Gebeng (Lynas) → Westports → La Pallice → Solvay La Rochelle (Maleisië → Frankrijk; aannemelijk: Eurostat landniveau, ontvanger niet gebronnen)
**Keten in één zin:** Ceriumcarbonaat (Ce-verbindingen, CN 28461000) van de Lynas-plant (LAMP) in Gebeng gaat per **truck** (E8/Karak Highway, 336,5 km) naar Westports in Port Klang, per **zeeschip** (MARNET: Malakka, Indische Oceaan, Suez, Gibraltar, Golf van Biskaje) naar de rede van La Pallice, over een stippel-haven-aanloop naar een kade en over een stippel-last-mile naar Solvay La Rochelle (Chef de Baie). Stoppunt bij de Solvay-poort.
**Welke as van het verhaal:** de nieuwe Atlantische corridor van Lynas naar Europa. Frankrijk importeerde uit Maleisië **0,0033 kt Ce-verbindingen per jaar (2025; productgewicht, geen REO)**, piek 0,0060 kt in 2023 en 0,0025 kt in 2024, EUR 1,8–5,7 mln per jaar [1]. Ter vergelijking: Lynas-NdPr-verkoop 7,3 kt REO/j (FY2026), ander product [13].
**Afwijkingen van het ontwerp (bindend, haalbaarheidstoets):** titel en beennamen dragen "aannemelijk"; b3 en b4 zijn omgekeerde letterlijke kopieën uit `ree-larochelle-sanmarcos`; de zee eindigt op zeeknoop 4239 (geen aanloop bij Westports, snap 2,3 km). Het eindpunt blijft La Rochelle zoals het id belooft.

## 1 · Ketenkaart
```
LAMP Gebeng `ree-lamp-gebeng` (hergebruikt anker)
  ──(b1 truck · E8 Pantai Timur → Karak Highway → KL–Klang · 336,5 km, LETTERLIJKE KOPIE ree-kuantan-japan b1)──►
Westports, Port Klang `ree-kuantan-japan-westport-kade` (hergebruikt anker)
  ──(b2 zee · Malakka → Suez → Gibraltar → Biskaje · 14.432,6 km, MARNET, aannemelijk)──► zeeknoop 4239 (46.2392, -1.2612)
  ╌╌(b3 zee-stippel · haven-aanloop La Pallice · 9,3 km, LETTERLIJKE KOPIE ree-larochelle-sanmarcos b2a, omgekeerd)╌╌► kade La Pallice `ree-larochelle-kade`
  ╌╌(b4 truck-stippel · last mile · 1,8 km, geen net op deze korrel, kopie ree-larochelle-sanmarcos b1 omgekeerd)╌╌► Solvay Chef de Baie `ree-larochelle-site` ⏹ stoppunt
```
Totaal 14.780,2 km (336,5 + 14.432,6 + 9,3 + 1,8).

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-lamp-gebeng` → `ree-kuantan-japan-westport-kade` | Lebuhraya Pantai Timur (E8) → Karak Highway (E8/E9) → KL–Klang-corridor | 336,5 getekend; hemelsbreed 258 km, geen wegkm [7][6] | KOPIE `ree-kuantan-japan-weg-gebeng-westport.geojson` (bak_ree_kuantan_japan / bak_ree_kuantan_narva b1) | nee |
| b2 | B | zee | `ree-kuantan-japan-westport-kade` → zeeknoop 4239 | Malakka, Indische Oceaan, Bab-el-Mandeb, Rode Zee/Suez, Gibraltar, Biskaje (MARNET kiest) — *aannemelijk: haven en route niet gebronnen* | 14.432,6 (eigen MARNET-dry-run 2026-11-01, 93 edges, 1.490 punten, snap 2,336 / 0,000 km [11]); geen gepubliceerde km | MARNET | nee; Westports 2,3 km van zijn knoop (< 5 km), geen aanloop |
| b3 | B | zee | zeeknoop 4239 → `ree-larochelle-kade` | haven-aanloop La Pallice (kade 9,28 km van de zeeknoop, > 5 km) | 9,3 (hemelsbreed, berekend [12]) | KOPIE van de `--stippel`-regel (b2a) in `bak_ree_larochelle_sanmarcos`, punten omgedraaid; `maak_havenaanloop.py` liep daar vast (timeout 300 s) | **ja — hier reikt het net niet** |
| b4 | C | truck | `ree-larochelle-kade` → `ree-larochelle-site` | havenwegen La Pallice → Chef de Baie | 1,8 (hemelsbreed, berekend [12]; geen publicatie) | KOPIE van de `--stippel`-regel b1 in `bak_ree_larochelle_sanmarcos`, punten omgedraaid | **ja — last mile (geen net op deze korrel, < 2 km)** |

## 3 · Ankers (alle hergebruikt; niets nieuw gelegd, dus geen nieuwe satellietblik)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-lamp-gebeng` | fabriek (start) | Lynas Advanced Materials Plant (LAMP), Gebeng | 4.0034, 103.3775 | hergebruik `ree-kuantan-japan.md` §3, `ree-sitelaag.json` w-kuantan-lamp [2] | bron-gelegd (z15 in `sat-ree-mtweld-kuantan-lamp-gebeng.png`: plantcomplex met procesgebouwen en tanks) |
| `ree-kuantan-japan-westport-kade` | overslag truck → zee | Westports Malaysia, Pulau Indah, Port Klang | 2.9498, 101.3076 | hergebruik `ree-kuantan-japan.md` §3 [10] | bron-gelegd (z14 in `sat-ree-kuantan-japan-westport.png`: kadelijn, containerstapels, tankopslag) |
| `ree-larochelle-kade` | overslag zee → truck | La Pallice, kade aan de zuidoostzijde van de noordelijke havenmole | 46.1586, -1.2297 | hergebruik `ree-larochelle-sanmarcos.md` §3 [5][9] | **onzeker** (z16 in `sat-ree-larochelle-sanmarcos-pallice-z16.png`: kades met kranen, loodsen en een schip; geen bron noemt de berth) |
| `ree-larochelle-site` | scheiding / losplek, stoppunt | Solvay La Rochelle, Chef de Baie (40 ha) | 46.1525, -1.2075 | hergebruik `ree-larochelle-sanmarcos.md` §3, `ree-sitelaag.json` w-larochelle [3] | bron-gelegd (z15 in `sat-ree-larochelle-sanmarcos-solvay.png`: industrieel gebouwencomplex met lange hallen tussen havenbekken en kust); Solvay als ontvanger = aanname |

Zeeknoop 4239 (46.2392, -1.2612) is een MARNET-knoop, geen anker. Markers: LAMP, Westports, kade La Pallice, Solvay.

## 4 · Via-punten
Geen eigen: b1 is een letterlijke kopie (via-punten in `ree-kuantan-japan.md` §4: Kuantan, Bentong, Genting Sempah, Gombak, Shah Alam, Pulau Indah); b2 is zee, b3 en b4 zijn stippel. Geen wegprofiel nodig, geen wegscan.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| LAMP Gebeng | Lynas | Mt Weld-concentraat/MREC → NdPr-oxide, Dy, Tb, Ce-carbonaat/-oxide, LaCe | nameplate 10,5 kt NdPr/j; Ce-volume niet gepubliceerd | [2][13] |
| Solvay La Rochelle | Solvay | REE-feed van meerdere leveranciers + recycling → gescheiden oxiden, formuleringen (katalyse, uitlaat, polijsten), magneetlijn | 40 ha; doel 30% van de Europese vraag in 2030; Ce-aandeel niet gepubliceerd | [3][4] |

## 6 · Stoppunt
De brief stopt bij de Solvay-poort: Solvay is de grote Franse REE-verwerker, maar geen bron koppelt Lynas-cerium aan Solvay. Fase D/E vervalt.

## 7 · Open punten
- **Ontvanger niet gebronnen.** Eurostat is landniveau [1]; Solvay noemt Lynas of Maleisië nergens [3]; Lynas noemt klanten alleen als "east Asia, the United States and Europe" [2]; twee zoekopdrachten (Lynas/Solvay/La Rochelle) vonden niets. Een andere Franse Ce-verwerker of afnemer kan het zijn.
- **Haven La Pallice is een aanname** (zelfde zwakte als in `ree-larochelle-sanmarcos`: geen containers genoemd [9]); Le Havre of Antwerpen met landtransport is realistischer en wordt niet getekend. Westports als laadhaven en de zeeroute via Suez zijn ook aannames (Kaaproute niet gemodelleerd).
- **Volume:** productgewicht Ce-verbindingen, REO-gehalte onbekend; 2024 gehalveerd, 2025 0,0033 kt; 2026 jan–aug 3.072 t volgens de haalbaarheidstoets (niet zelf nagekeken). Overige Lynas-bestemmingen niet uitgesplitst; niet alle Ce-import uit Maleisië hoeft van Lynas te komen.
- **Geen gepubliceerde km** voor b1 (hemelsbreed 258 km) en b2: geen ±15%-norm. b1 is niet gebrond als route van deze lading.
- **Kade La Pallice onzeker**; de last mile Solvay ↔ kade (1,8 km) is schematisch.

## 8 · Bronnen
[1] Eurostat Comext DS-045409, FR import uit MY, CN 28461000 (x100 kg, eigen opvraag 2026-11-01): 2021 49.397 (EUR 3,26 mln), 2022 54.080 (5,71), 2023 59.520 (3,38), 2024 24.480 (1,82), 2025 33.002 (2,68). https://ec.europa.eu/eurostat/api/comext/dissemination/statistics/1.0/data/ds-045409?freq=A&reporter=FR&partner=MY&product=28461000&flow=1
[2] Lynas Rare Earths, Kuantan, Malaysia — producten o.a. Ce-carbonaat, Ce-oxide, LaCe; klanten in Oost-Azië, VS en Europa. https://lynasrareearths.com/kuantan-malaysia-2/
[3] Solvay, "Solvay advances European rare earths production through capacity expansion" (2025-04-08) — La Rochelle 40 ha, Chef de Baie, 30% in 2030; geen Lynas, geen Maleisië. https://www.solvay.com/en/press-release/solvay-advances-european-rare-earths-production-through-capacity-expansion
[4] Solvay en Hastings, MoU voor mixed rare earth carbonate (voorbeeld van een andere La Rochelle-leverancier). https://www.solvay.com/en/press-release/solvay-and-hastings-sign-memorandum-understanding-supply-mixed-rare-earth-carbonate
[5] Wikipedia, La Pallice — commerciële diepwaterhaven van La Rochelle. https://en.wikipedia.org/wiki/La_Pallice
[6] Wikipedia, Kuala Lumpur–Karak Expressway (E8, 60 km). https://en.wikipedia.org/wiki/Kuala_Lumpur%E2%80%93Karak_Expressway
[7] Brief `ree-kuantan-japan.md` (Time.com apr 2026: Gebeng → Port Klang per truck; Westports-coördinaat en satellietblik).
[8] Brieven `ree-kuantan-narva.md` en `ree-kuantan-chattanooga.md` — patroon van de b1-kopie en de Westports-zeeroute.
[9] Brief `ree-larochelle-sanmarcos.md` — kade-anker, stippels, Port of La Rochelle (geen containers genoemd). https://www.larochelle.port.fr/en/
[10] Wikipedia, West Port, Malaysia (2.949834, 101.307635). https://en.wikipedia.org/wiki/West_Port,_Malaysia
[11] Eigen MARNET-dry-run (`hecht_marnet.py route`, scratch, 2026-11-01): Westports 2.9498,101.3076 → knoop 4239 14.432,6 km; passeert Sri Lanka, Bab-el-Mandeb, Suez-golf, Gibraltar.
[12] Haversine-berekening (kade ↔ zeeknoop 9,28 km; kade ↔ Solvay 1,84 km).
[13] Discovery Alert, Lynas FY26 (NdPr-verkoop 7.337 t, nameplate 10.500 t), via `ree-kuantan-japan.md` [2]. https://discoveryalert.com/analysis/lynas-rare-earths-investment-analysis/

## 9 · Gebakken (2026-11-01, lichte werkwijze, M31 golf 20)
**Bestand:** `v2/data/stroomroute-ree-kuantan-larochelle.json` (117,5 KB, versie 2, punt_formaat lonlat, 4 benen, 4 markers). **Recept:** functie `bak_ree_kuantan_larochelle` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh ree-kuantan-larochelle`). Geen wegscan, geen profiel, geen via-punten.
| been | modaliteit | km gemeten | brief | punten | stippel |
|---|---|---|---|---|---|
| b1 LAMP Gebeng → Westports | truck | 336,5 | 336,5 (kopie) | 4.673 | nee |
| b2 Westports → zeeknoop 4239 | zee | 14.432,6 | 14.432,6 (dry-run) | 1.490 | nee |
| b3 zeeknoop 4239 → kade La Pallice | zee | 9,3 | 9,3 | 2 | ja (haven-aanloop) |
| b4 kade La Pallice → Solvay | truck | 1,8 | 1,8 | 2 | ja (last mile) |
Totaal 14.780,2 km, 6.167 punten. Naden: Westports → eerste zeepunt 2,34 km (router-snap, < 5 km, in de brief), overige 0,000 km. Markers op 0,000 km van hun lijn.
- **b1** is een letterlijke bestandskopie van `ree-kuantan-japan-weg-gebeng-westport.geojson`; knikken in toets_knikken zijn die van de bron (spikes op de aanloop, niet nieuw).
- **b3** is de omgekeerde kopie van b2a in `bak_ree_larochelle_sanmarcos` (rechte lijn over water, kade 9,28 km van knoop); `maak_havenaanloop.py` niet opnieuw gedraaid (daar timeout 300 s).
- **b4** is de omgekeerde kopie van b1 uit dezelfde functie (geen net op deze korrel, 1,84 km).
- Geen gepubliceerde km voor b1/b2: geen ±15%-norm. Geen vlucht, leiding of spoor. Kaaproute niet gemodelleerd (MARNET kiest Suez).
- **Les:** alle benen waren hergebruik of dry-run; gereedschap, kopieerpatroon (narva b1, sanmarcos b1/b2a) werkte in een run. Eindpunt = La Rochelle, zoals het id belooft.

