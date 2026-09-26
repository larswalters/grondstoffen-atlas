# Routebrief (licht) · nikkel — Ouaco → Téoudié → Gwangyang (Zuid-Korea)

**stroom-id:** `nikkel-ouaco-gwangyang` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** lateriet-erts (~2 % Ni) van het NMC-mijnplateau bij Ouaco (Kaala-Gomen, Nieuw-Caledonië) gaat per truck over een privé-mijnweg naar de laadkade Téoudié, wordt daar op bakken van 250–330 t naar de rede overgeslagen (géén kade voor zeeschepen), vaart per zeeschip (MARNET) ~7.580 km naar Gwangyang, Zuid-Korea, en wordt bij SNNC (SMSP/POSCO-JV) tot ferronikkel verwerkt — dat gaat (aannemelijk, één bron) per truck naar POSCO's roestvrijstaalfabriek in Pohang.
**Welke as van het verhaal:** de shakeout in Nieuw-Caledonië — Koniambo staat sinds aug. 2024 op care & maintenance en SLN draait op een Franse noodlening, maar de NMC/SNNC-as (SMSP/POSCO) blijft varen: 2,9 Mt erts in 2023, doel 3,6 Mt/j [2].

## 1 · Ketenkaart
```
Ouaco-mijnplateau `ni-ouaco-mijn` ──(b1 truck · mijnweg "Mines", privaat/track · stippel)──► Téoudié-laadkade `ni-teoudie-kade`
   ──(b2 zee/bakken · rede, geen kade voor zeeschepen · ~5–6 km, stippel)──► rede Téoudié
   ──(b3 zee · haven-aanloop over het rif · ~102 km, stippel)──► MARNET-zeeknoop 2753 (-20.9000,163.5000)
   ──(b4 zee · MARNET · ~7.578,2 km)──► MARNET-zeeknoop 5615 (34.7100,127.8204)
   ──(b5 zee · haven-aanloop Gwangyang · ~22,1 km, stippel)──► `ni-gwangyang-ertskade`
   ═══ site-anker: SNNC-ferronikkelfabriek `ni-snnc-fabriek` (géén eigen been — kade en fabriek liggen op hetzelfde industrieterrein) ═══
   ──(b7 truck · Zuid-Korea, aannemelijk: één bron · ~250 km)──► POSCO-staalfabriek Pohang `ni-pohang-mill` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ni-ouaco-mijn` → `ni-teoudie-kade` | mijnweg "Mines" (OSM: 348× track, 73× unclassified, 60× primary/RT1 in de Ouaco-bbox) | ~10 [7] | maak_stroombeen_weg (nieuw-caledonie-extract; grotendeels track → stippel, alleen het RT1-stuk meetbaar) | ja — privéweg, net reikt niet |
| b2 | A/B overslag | zee (bakken, 250–330 t, achter sleepboten) | `ni-teoudie-kade` → rede | kade → ankerplaats zeeschip, westkust | 5–6 [1] | stippel "bakken naar rede (geen kade voor zeeschepen)" | ja — geen kade |
| b3 | B | zee | rede Téoudié → MARNET-zeeknoop 2753 | over het barrièrerif, pas onbekend | ~102 [toets] | maak_havenaanloop (schematisch, 1:10M-kust kent het rif niet) | ja — MARNET reikt niet tot de rede |
| b4 | B | zee | zeeknoop 2753 → zeeknoop 5615 | Koraalzee → Salomonszee/Bismarckzee → Filipijnenzee → Oost-Chinese Zee | 7.578,2 [toets] | MARNET | nee |
| b5 | B | zee | zeeknoop 5615 → `ni-gwangyang-ertskade` | havenaanloop Gwangyang-baai | ~22,1 [toets] | maak_havenaanloop | ja — MARNET-knoop ligt net buiten 25 km |
| b7 | D | truck | `ni-snnc-fabriek` → `ni-pohang-mill` | geen gedocumenteerde corridor; bak-agent routeert kop→staart | ~250 (schatting, geen publicatie) [4] | maak_stroombeen_weg (zuid-korea-extract) | nee — *aannemelijk: één bron* |

Geen eigen been C: de erts-losplek en de SNNC-fabriek liggen op hetzelfde industrieterrein (Gwangyang-schiereiland); het procesgat tussen kade en fabriek komt in §9.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-ouaco-mijn` | mijn (kop van b1) | NMC-mijnplateau Ouaco (Kaala-Gomen) | -20.7400, 164.4750 | [2][7][8] | bron-gelegd (z16 gezien: open lateriet-terrassenmijn met haulroads en een mijnkamp, klassiek Nieuw-Caledonisch bulldozer-reliëf) |
| `ni-teoudie-kade` | laadplek/overslag | Téoudié-laadkade, Cotransmine (Kaala-Gomen, westkust) | -20.7566, 164.3822 | [1][7][8] | bron-gelegd (z18 gezien: aangelegde landtong met meerdere bakken (250–330 t-klasse) langszij, exact het beeld dat de bron beschrijft) |
| `ni-snnc-fabriek` | smelter/fabriek | SNNC ferronikkelfabriek, Gwangyang Industrial Complex | 34.9295, 127.7360 | [3][9] | bron-gelegd (adresgebied 금호동/Jecheol-ro; z17 gezien: dichte cluster industriehallen aan de kust binnen het POSCO Gwangyang-complex — het individuele SNNC-gebouw niet te onderscheiden van buurpanden) |
| `ni-gwangyang-ertskade` | overslag/losplek (fase B→C) | bulkkade, POSCO Gwangyang-industriehaven | 34.9095, 127.7280 | [8] | aannemelijk (z17 gezien: bulkcarriers en kranen aan een kade binnen het POSCO Gwangyang-complex; geen bron noemt specifiek welke kade NMC-erts lost) |
| `ni-pohang-mill` | fabriek (fase D) | POSCO geïntegreerd staalcomplex Pohang | 36.0180, 129.3820 | [4][8] | bron-gelegd (z15 gezien: hoogovens/cokesfabrieken op de rivierdelta-oever, het geïntegreerde staalcomplex) |

## 4 · Via-punten
Geen — b1 en b7 hebben geen gedocumenteerde corridorkeuze (b1 is een privé-mijnweg zonder gepubliceerde route, b7 heeft geen enkele bron die de weg noemt). De bak-agent routeert bij b7 kop→staart over het zuid-korea-extract; bij b1 volgt de stippel de hemelsbrede lijn.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| SNNC, Gwangyang | SMSP/POSCO-JV (50/50) | lateriet-erts (~2 % Ni) → ferronikkel (+ vanaf 2023 ook matte) | 54 kt Ni/j in ferronikkel; uitbreidingsdoel 26 kt FeNi + 21 kt matte/j | [3][4] |

## 6 · Stoppunt
De brief stopt bij POSCO Pohang: SNNC verkoopt zijn hele ferronikkelproductie aan POSCO's roestvrijstaalfabrieken en Pohang is "SNNC's main buyer of ferronickel" [4] — één bron, geen fabrieksadres of afnamecontract verder. Fase E (het roestvrijstaal zelf) vervalt.

## 7 · Open punten
- **Rede/ankerplaats Téoudié** heeft geen vaste coördinaat (bron noemt geen positie); b2/b3 zijn daarom volledig stippel zonder tussenanker.
- **b1 grotendeels ongekarteerd als doorgaande weg** (OSM: privé/track); alleen het laatste RT1-stuk richting Téoudié is een meetbare weg. Kan een grotere stippel worden dan de hemelsbrede ~10 km.
- **`ni-gwangyang-ertskade` is niet gebrond**: geen bron zegt welke kade van het POSCO Gwangyang-complex NMC-erts specifiek lost; de gekozen kade is de meest waarschijnlijke bulklosplaats op basis van satellietbeeld.
- **b7 (Gwangyang → Pohang) heeft geen gepubliceerde route of lengte** — ~250 km is een schatting op de kaart, geen bronwaarde; de bak-toets (±15%) kan hier niet tegen een publicatie getoetst worden.
- **Verdeling over de vier NMC-mijncentra**: deze brief tekent alleen Ouaco (50 % van NMC's productie); Poya (15 %), Kouaoua (15 %) en Nakéty (20 %) [2] laden bij hun eigen kades en worden hier niet getekend.
- **Jaarvolume is afgeleid**: NMC verscheepte 2,9 Mt erts in 2023 op ~2 % Ni [2] = ± 58 kt Ni-inhoud totaal; Ouaco's aandeel (50 %) ≈ 1,45 Mt erts ≈ ± 29 kt Ni-inhoud (afleiding, geen bron geeft dit cijfer direct). SNNC's 54 kt Ni/j is wél een direct brongegeven (downstream, niet vergelijkbaar met de ertsvoeding).
- **Koniambo (KNS) en SLN** staan alleen als context (sitelaag-status "care & maintenance" resp. "noodlening") — geen onderdeel van deze keten.

## 8 · Bronnen
[1] SMSP, Cotransmine SAS — vier laadhavens (Téoudié/Kaala-Gomen, Poya, Nakéty, Kouaoua); Téoudié-vloot 3 sleepboten/13 bakken; bakken 250–330 t; westkust kade→rede 5–6 km. https://smsp.nc/en/cotransmine-sas-eng/
[2] SMSP, NMC SAS — 2,9 Mt erts verscheept in 2023, doel 3,6 Mt/j aan SNNC, ~2 % Ni; verdeling Ouaco 50 % · Poya 15 % · Kouaoua 15 % · Nakéty 20 %. https://smsp.nc/en/nmc-sas-eng/
[3] SMSP, SNNC Co. Ltd — Gwangyang Industrial Complex, 54.000 t Ni/j in ferronikkel, 50/50 SMSP/POSCO, "production is entirely sold to POSCO's stainless steel plants", matte-uitbreiding 26 kt FeNi + 21 kt matte/j. https://smsp.nc/en/snnc-co-ltd-eng/
[4] SMSP, "Diversification into matte to remain competitive for SNNC" — Pohang is "SNNC's main buyer of ferronickel"; matte-eenheid bij de Gwangyang-fabriek voor POSCO's nikkelsulfaatfabriek. https://smsp.nc/en/diversification-into-matte-to-remain-competitive-for-snnc/
[5] Glencore, "Koniambo Nickel to Transition to Care and Maintenance" (feb. 2024) — shareholders (SMSP/Glencore 49 %) besluiten KNS naar care & maintenance. https://www.glencore.com/media-and-insights/news/koniambo-nickel-to-transition-to-care-and-maintenance
[6] Nasdaq (Reuters), "France grants loan to Eramet's SLN nickel unit to avert collapse" (feb. 2024) — €40 mln Franse noodlening aan SLN. https://www.nasdaq.com/articles/france-grants-loan-to-eramets-sln-nickel-unit-to-avert-collapse
[7] OpenStreetMap (ODbL) via Nominatim — Ouaco (Wako), Kaala-Gomen -20.83629,164.46952; Kaala-Gomen-centrum -20.66793,164.39600; wegklassen in de Ouaco-bbox (nieuw-caledonie-extract). https://www.openstreetmap.org
[8] Esri World Imagery via `v2/tools/sat_check.py` (z13–z18) — `v2/build-cache/satcheck/sat-ni-ouaco-overzicht.png`, `sat-ni-ouaco-kust.png`, `sat-ni-ouaco-mijn.png`, `sat-ni-ouaco-mijnplateau.png`, `sat-ni-teoudie-kandidaat.png`, `sat-ni-teoudie-kade.png`, `sat-ni-teoudie-kade2.png`, `sat-ni-gwangyang-overzicht.png`, `sat-ni-snnc-zoom.png`, `sat-ni-gwangyang-kade2.png`, `sat-ni-gwangyang-ertskade.png`, `sat-ni-pohang-mill.png`, `sat-ni-pohang-mill2.png`.
[9] POSCO / namu.wiki, SNNC-adres — 전라남도 광양시 제철로 2148-139 (금호동), Gwangyang Industrial Complex. https://www.posco.co.kr/homepage/docs/kor5/jsp/family/snnc.jsp
[toets] Haalbaarheidstoets `nikkel-ouaco-gwangyang.json` (ontwerp+toets, 2026-09-26) — zeeknoop 2753 (-20.9000,163.5000), zeeknoop 5615 (34.7100,127.8204), MARNET-proefroute zeeknoop→Gwangyang 7.578,2 km, aanloop Ouaco ~102 km, aanloop Gwangyang ~22,1 km. `C:/Users/lars/AppData/Local/Temp/claude/C--automation/3990dac9-5d76-4051-8977-ace67e6a8f4a/scratchpad/ontwerp/nikkel-ouaco-gwangyang.json`

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `nikkel-ouaco-gwangyang`** → `v2/data/stroomroute-nikkel-ouaco-gwangyang.json` — 7 benen ·
7.954,7 km · 4.783 punten · 5 markers. Recept: `bak_stromen.sh` (functie `bak_nikkel_ouaco_gwangyang`).

| # | modaliteit | km | stippel? | toelichting |
|---|---|---|---|---|
| 1 | truck | 9,8 | ja | rechte stippel Ouaco-mijnplateau → Téoudié-laadkade — profiel `nikkel-ouaco-gwangyang-ouaco-teoudie` geprobeerd op het nieuw-caledonie-extract, gaf "geen wegpad" (de mijnweg "Mines" is in OSM vrijwel volledig `track`, dat komt de scanner nooit door, ook niet via `corridorKlassen`); geen tweede poging |
| 2 | zee | 0,8 | ja | rechte stippel kade → rede: geen kade voor zeeschepen; het redepunt (-20,760, 164,375) is een schatting ~2-3 km uit de kust op het rif, geen bron geeft een coördinaat |
| 3 | zee | 98,2 | ja | `maak_havenaanloop.py`, kade-aanloop over het barrièrerif (rede → MARNET-zeeknoop 2753); 89 punten, 0 km landkruising midden op de lijn; tegen de brief-schatting van ~102 km = **-3,7%** |
| 4 | zee | 7.578,2 | nee | MARNET, zeeknoop 2753 → zeeknoop 5615; identiek aan de haalbaarheidstoets (7.578,2 km) = **0,0%** |
| 5 | zee | 25,5 | ja | `maak_havenaanloop.py`, aanloop Gwangyang-baai (zeeknoop 5615 → erts­kade); tegen de brief-schatting van ~22,1 km = **+15,4%** — licht buiten de ±15%-norm, maar het is een schematische haven-aanloop (geen gemeten been) en de brief-schatting was zelf al "uit de haalbaarheidstoets", geen publicatie; bevinding, niet dichtgetrokken |
| 6 | truck | 2,3 | ja | kade → SNNC-terrein: geen eigen been in de brief (§2), beide liggen op hetzelfde Gwangyang-industrieterrein; korte stippel toegevoegd voor de continuïteit van de keten (naad zou anders 2,34 km zijn, ruim onder de 5 km-norm, maar zo blijft het procesgat zichtbaar als lijn i.p.v. als onzichtbare sprong) |
| 7 | truck | 239,9 | nee | `maak_stroombeen_weg.py --profiel nikkel-ouaco-gwangyang-snnc-pohang` op het zuid-korea-extract, vrije Dijkstra tussen de twee ankers (geen via-punten, geen gedocumenteerde corridor); tegen de kaart-schatting van ~250 km = **-4,1%** (aannemelijk: één bron voor de afnemer) |

**Toets:** naden tussen alle 7 benen **0,00 km** · markers **0,0–0,1 m** van de lijn (alle 5 uit §3) ·
`toets_knikken.py`: zeebeen 0 omkeringen (3 krappe bochten op de MARNET-route, geen fout); wegbeen b7
1 omkering (153,7°, "scherpe bocht, echt", een rotonde) en 30 kleinere spikes (junctie-ruis op het
zuid-korea-wegnet), **0 terugloop** (de enige klasse die gerepareerd hoort te worden) · `toets_rechte_benen.py
--min-km 5`: alleen been 1 (9,8 km, omwegfactor 0,997) komt boven de 5 km-drempel uit, en dat is al
een stippel — geen probleem · JSON: `versie 2`, `punt_formaat lonlat`, alle modaliteiten in
{zee, truck}, elk been ≥ 2 punten, bestand 99.079 byte (< 300 KB).

**Gereedschapslessen:**
- `maak_havenaanloop.py` accepteert `--van`/`--naar` niet als los argument met een negatief getal
  (argparse leest `-20.760,…` als een optievlag) — gebruik `--van=…`/`--naar=…` met een `=`-teken.
- `track` komt de wegscanner nooit door, ook niet via `corridorKlassen` (staat al als waarschuwing in
  `maak_stroombeen_weg.py` regel 1368) — bevestigd op b1: de Ouaco-mijnweg gaf meteen "geen wegpad"
  zonder dat er iets aan het profiel te verbeteren viel.
- Beide haven-aanlopen (b3, b5) slaagden zonder terugval nodig; b5 zit net (+15,4%) buiten de ±15%-norm
  tegen een brief-schatting die zelf al uit een haalbaarheidstoets kwam — dat is een bevinding over de
  precisie van de brief-schatting, niet over het gereedschap.

**Open na het bakken (ongewijzigd t.o.v. §7):** rede/ankerplaats Téoudié heeft geen vaste bron-coördinaat;
`ni-gwangyang-ertskade` is niet gebrond (aannemelijk); b7 heeft geen gepubliceerde route of lengte.
