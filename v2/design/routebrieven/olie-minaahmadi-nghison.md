# Routebrief (licht) · olie — Mina al-Ahmadi (Koeweit) → Nghi Son (Vietnam)

**stroom-id:** `olie-minaahmadi-nghison` · **geschreven:** 2026-10-30 · **werkwijze:** licht (M31 golf 16) · **status:** gebakken
**Keten in één zin:** Kuwait Export Crude (KEC) vanaf de exportterminal Mina al-Ahmadi (KOC/KNPC) per **VLCC** door de Perzische Golf, de Straat van
Hormuz, de Arabische Zee, de Straat van Malakka/Singapore, de Zuid-Chinese Zee en de Golf van Tonkin naar de crude-steiger van de Nghi Son-raffinaderij
(NSRP, Thanh Hoa); geen landbenen. Eindpunt = de raffinaderij zelf: dit is het eerste Koeweit-Vietnam-been van de atlas.
**Welke as van het verhaal:** *Hormuz-crisis aan de importkant* — NSRP is gebouwd voor KEC en wordt voor ~35% gehouden door Kuwait Petroleum International
[4][3]. Ontwerpcapaciteit **200 kb/d** (10 Mt/j) [4]; Koeweit leverde **2,8 Mt in jan–aug 2026 (−64% j/j)**, nul van april tot en met juli, ≈ **85 kb/d**
(2,8 Mt × 7,33 bbl/t / 243 d; peiljaar 2026 YTD) [3]. 2025 afgeleid ≈ 235 kb/d (zelfde omrekening op 2,8/0,36 Mt, indicatie). Hervat sep 2026, ~75% van
de nieuwe cargo's, daarna ook andere crudes (Oman, VAE, VS, Irak) [3].

## 1 · Ketenkaart
```
Mina al-Ahmadi-steiger `ol-ahmadi-steiger` (Koeweit) ──(b1 zee · Golf → Hormuz → Arabische Zee → Malakka → Singapore → Zuid-Chinese Zee → Golf
   van Tonkin · MARNET 9.541 km, hemelsbreed 5.888 km)──► zeeknoop Nghi Son (18.9115, 105.9851)
   ──(b2 stippel · haven-aanloop Nghi Son, over water, ~57,7 km)──► NSRP-crude-steiger `ol-nsrp-steiger` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Mina al-Ahmadi-steiger → zeeknoop Nghi Son | Perzische Golf – Hormuz – Arabische Zee – Malakka – Singapore – Zuid-Chinese Zee – Golf van Tonkin (aannemelijk: één bron voor de bestemming) | 9.541 MARNET (haalbaarheidstoets); geen gepubliceerde ladingroute; het ontwerp (10.000–11.000) was een eigen schatting | MARNET, begin 0,5 km van zeeknoop 4091 | nee |
| b2 | B | zee | zeeknoop Nghi Son → NSRP-steiger | Golf van Tonkin | ~57,7 (toets: 0 km over land, scratch olie16) | `maak_havenaanloop.py` | ja — MARNET reikt niet tot de kade (54,6 km) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-ahmadi-steiger` | laadplek / exportterminal | Mina al-Ahmadi-pierencluster (KOC/KNPC), noordelijke pieren | 29.0600, 48.1600 | [5][6][8] | onzeker (z14 gezien, korrelig: pierstructuren met noord-zuid-vingers bij 48.160 en 48.170 vlak bij de kust; Sea Island/SPM zelf niet gelegd: open water heeft geen beeld) |
| `ol-nsrp-steiger` | losplek / crude-steiger NSRP | NSRP crude-oil-jetty, westelijke ligplaats | 19.3640, 105.7925 | [4][8] | bron-gelegd (z17 gezien: trestle vanaf de golfbreker met twee tanker-ligplaatsen, aan beide een tanker afgemeerd; aan land het tankenpark en de procesinstallaties) |

## 4 · Via-punten
Geen. De zeeroute wordt door MARNET zelf gelegd; er is geen landbeen en geen corridorkeuze die een via-punt op zee zou rechtvaardigen.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nghi Son Refinery and Petrochemical (NSRP) | Idemitsu 35,1% · Kuwait Petroleum International 35,1% · Petrovietnam 25,1% · Mitsui Chemicals 4,7% | ruwe olie (KEC + 10 soorten) → brandstoffen, petrochemie | 200 kb/d ontwerp, sinds juli 2026 op 125% | [3][4] |

## 6 · Stoppunt
De brief stopt bij de NSRP-steiger: één bron legt de lading aan deze raffinaderij en de afnemer is de eigenaar; fase D/E (producten naar de Vietnamese markt)
vervalt, geen bron noemt een afzonderlijke fabriek.

## 7 · Open punten
- **Sea Island en SPM bij Mina al-Ahmadi niet gelegd:** het is een kunstmatig eiland (VLCC, ~30 m diepte) met SPM, volgens een zwakke bron [6]; een bron uit 1968 plaatst een
  Sea Island ~10 mijl voor de kust [7]. Op Esri bij z12–z13 niets te zien (open water zonder beeld) en OSM kent hem niet; het anker blijft het pierencluster aan de kust
  (haalbaarheidstoets: berthcluster 29.0414–29.0496 / 48.1548–48.1602 zichtbaar). De laad-ligplaats kan dus 10–15 km zeewaarts liggen.
- **Aandeel Koeweit en exclusiviteit:** langlopend contract ≈ 80% KEC [3] maar NSRP verwerkt nu ook andere crudes; per cargo is Koeweit niet gegarandeerd.
- **Onderbreking:** laatste Koeweit-cargo medio maart 2026 vóór de Hormuz-beperking [2]; nul april–juli; hervat sep 2026 [3].
- **Sitelaag:** geen Koeweit- of Vietnam-site in `olie-sitelaag.json`; v1-knoop `oil-term-kuwait` (29.05, 48.20) ligt in open water en is niet gebruikt.
- **Kilometers:** zeekm 9.541 is een MARNET-meting, geen gepubliceerde waarde; de ±15%-toets is hier indicatief (omwegfactor 1,62 op 5.888 km grootcirkel).
- **Partnernaam KPI:** één bron noemt Kuwait Petroleum Europe, S&P en Wikipedia Kuwait Petroleum International [3][4].

## 8 · Bronnen
[1] NSRP, persbericht mrt 2026 — https://www.nsrp.vn/releases-article/press-release-nghi-son-refinery-sustains-full-performance-and-supply-assurance-through-may-2026/ (niet opgehaald: certificaatfout; inhoud via [2])
[2] Vietnam News, 27-03-2026 — "Nghi Sơn Refinery says crude supply secured": laatste Koeweit-cargo medio maart, Hormuz beperkt leveringen. https://vietnamnews.vn/economy/1778232/nghi-son-refinery-says-crude-supply-secured.html
[3] Hydrocarbon Processing, 02-10-2026 — Koeweit 2,8 Mt jan–aug 2026 (−64%), ~75% van de nieuwe cargo's, 80% in 2025, contract ≈ 80%. https://hydrocarbonprocessing.com/news/2026/10/vietnams-nghi-son-refinery-secures-crude-supplies-through-november-mostly-from-kuwait/
[4] Wikipedia, "Nghi Sơn Refinery" — 19.34222/105.79778, 200 kb/d, aandeelhouders. https://en.wikipedia.org/wiki/Nghi_S%C6%A1n_Refinery
[5] Wikipedia, "Mina Al-Ahmadi refinery" — 29.06000/48.13167, 346 kb/d. https://en.wikipedia.org/wiki/Mina_Al-Ahmadi_refinery
[6] Oil & Gas Storage News, "Kuwait Oil Company pipelines" — zuidpier 8 ligplaatsen, noordpier 4, Sea Island + SPM (zwakke bron). https://oilgasstoragenews.com/kuwait-oil-company-pipelines/
[7] US Minerals Yearbook 1968, p. 476 — Sea Island ~10 mijl uit de kust. https://search.library.wisc.edu/digital/AC7YH2GVPR5IDL8M/text/AVW6MEBUDHT6KJ85
[8] Esri World Imagery via `v2/tools/sat_check.py` — `sat-olie-minaahmadi-nghison-ahmadi-kust.png`, `-ahmadi-wijd.png`, `-ahmadi-pier-n.png`, `-zee13.png`, `-glow.png` (Qaruh-eiland, geen Sea Island), `-nsrp-pier.png`, `-nsrp-steiger.png`.
[9] Eigen MARNET-meting (haalbaarheidstoets 2026-10-30): zeeknoop 4091 (29.0595, 48.1546) op 0,5 km; zeeknoop 5526 (18.9115, 105.9851) op 54,6 km van de steiger.

## 9 · Gebakken
**Gebakken (2026-10-30, lichte werkwijze, M31 golf 16)** — `bash v2/tools/bak_stromen.sh olie-minaahmadi-nghison` → `v2/data/stroomroute-olie-minaahmadi-nghison.json` (18,5 KB, 2 benen, 1.027 punten, 2 markers).

| # | modaliteit | been | km | naad | stippel |
|---|---|---|---|---|---|
| 1 | zee | zeeschip Mina al-Ahmadi → Nghi Son (aannemelijk: één bron), MARNET kade → zeeknoop 5526 | 9.541,3 (MARNET-meting, geen gepubliceerde waarde; brief 9.541) | 0 | nee, doorgetrokken |
| 2 | zee | haven-aanloop Nghi Son (zeeknoop → NSRP-steiger, over water) | 58,1 (brief ~57,7; rechte lijn 54,2 km) | 0,0 km | ja: MARNET reikt niet tot de kade (54,6 km) |

Totaal 9.599,4 km, grootste naad 0,0 km. Markers: `ol-ahmadi-steiger` 29.0600,48.1600 (0,53 km van de lijn: het MARNET-begin snapt op zeeknoop 4091; anker ≠ routeerpunt, onzeker) en `ol-nsrp-steiger` 19.3640,105.7925 (op de lijn).

**Recept:** zeebeen `--been "zee|…|29.0600,48.1600|18.9115,105.9851"`; aanloop met `timeout 600 python v2/tools/maak_havenaanloop.py --naam olie-minaahmadi-nghison-nghison --van 19.3640,105.7925 --naar 18.9115,105.9851` (cel 0,005° gebufferd, 47 punten, 0,00 km over land, omwegfactor 1,072), daarna `--stippel-geojson`. Geen via-punten, geen extract, geen kopie, geen lucht.

**Toelichting en lessen:**
- De aanloop loopt in reisvolgorde zeeknoop → kade. `maak_havenaanloop.py` schrijft in de richting `--van` → `--naar` (hier kade → knoop, bedoeld voor een vertrekhaven); omdat Nghi Son een AANKOMSTHAVEN is, is het bestand omgekeerd (coördinaten gespiegeld, zelfde pad) vóór het bakken. Zonder die omkering ontstond een naad van 54 km tussen zeebeen en stippel. Les: bij een aankomsthaven `--van` de zeeknoop en `--naar` de kade geven, of het geojson omkeren.
- Stippel betekent hier alleen "hier reikt het net niet" (de laatste 54,6 km tot de kade); het zeebeen zelf is gemeten en doorgetrokken. "Aannemelijk: één bron" staat in de beennaam.
- Km-toets: 9.541 is een MARNET-meting (brief §7), geen gepubliceerde ladingroute (omwegfactor 1,62 op 5.888 km hemelsbreed): de toets is indicatief. De ontwerpschatting van 10-11.000 km was onjuist en vervalt.
- toets_knikken: 2 knikken van 61-71 graden (Perzische Golf 29.10,48.30; Zuid-Chinese Zee 16.10,109.00), 0 omkeringen, 0 terugloop. toets_rechte_benen: geen rechte been.
- Open punten blijven §7: Sea Island/SPM niet gelegd (laadplek kan 10-15 km zeewaarts liggen), Koeweit-aandeel per cargo niet exclusief, levering onderbroken apr-jul 2026, geen Koeweit- of Vietnam-site in `olie-sitelaag.json`.
- Titel en eindpunt komen overeen met het id (Nghi Son); geen afwijking van het ontwerp.
