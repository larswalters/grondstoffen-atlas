# Routebrief (licht) · Lithium · Salar de Atacama → Antofagasta → Daesan (Zuid-Korea)

**stroom-id:** `lithium-carmen-pohang` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 5) ·
**status:** gebakken (2026-09-28)
**Keten in één zin:** lithiumchloride-oplossing van SQM's Salar de Atacama gaat per tankwagen naar de
Planta Química de Litio Carmen bij Antofagasta, wordt daar tot **lithiumhydroxide** omgezet, gaat in
containers naar de ATI-kade van Puerto Antofagasta en per **containerschip** over de Stille Oceaan naar
**Daesan (Zuid-Korea)**, de haven bij SK On's enige Koreaanse batterijfabriek (Seosan) — getekend tot de
kade, zonder gebronde eindfabriek.
**Welke as van het verhaal:** as 2, Koreaanse tak — SK On tekende in 2023 een eigen LiOH-leveringscontract
met SQM (57 kt over 2023–2027) bovenop het al gemeten China-aandeel van dezelfde Carmen-fabriek [4].

## 1 · Ketenkaart
```
SQM Salar de Atacama `li-atacama-laad` ──(b1 truck · letterlijke kopie · ~232,4 km)──► PQL Carmen `li-carmen-plant`
   ══ knoop: LiCl → LiOH (SQM Carmen, zelfde fabriek als de China-as) ══
   ──(b2 truck · letterlijke kopie · ~21,9 km)──► Puerto Antofagasta, ATI `li-antofagasta-kade`
   ──(b3 zee · haven-aanloop, letterlijke kopie · 97,1 km)──► zeeknoop -23.80,-71.30
   ──(b4 zee · MARNET · hemelsbreed ~17.827 km, geen zeekm-citaat)──► zeeknoop 37.16690,126.41420
   ──(b5 zee · haven-aanloop Daesan, nieuw · ~17,1 km)──► Daesan-kade `li-daesan-kade` ⏹ stoppunt
   └── vertakking (niet getekend): SK On Seosan-batterijfabriek (~15 km landinwaarts, geen bron noemt de kade→fabriek-route)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `li-atacama-laad` → `li-carmen-plant` | Ruta B-39 → Baquedano → Ruta 5 — **identiek aan** `lithium-atacama-antofagasta` been b1 | 232,4 gemeten (letterlijke kopie) | letterlijke kopie van `<stroom-id>-weg-atacama-carmen.geojson` uit `stroomroute-lithium-atacama-antofagasta.json` been 1 | nee |
| b2 | C | truck | `li-carmen-plant` → `li-antofagasta-kade` | Ruta 5 → Ruta 26 — **identiek aan** been b2 | 21,9 gemeten (letterlijke kopie) | letterlijke kopie van been 2 uit dezelfde json | nee |
| b3 | B | zee (haven-aanloop) | `li-antofagasta-kade` → zeeknoop -23.80,-71.30 | over water, MARNET reikt niet tot de kade — **identiek aan** de bestaande aanloop | 97,1 (gemeten, letterlijke kopie) | letterlijke kopie van `aanloop-antofagasta.geojson` (gedeeld met `lithium-atacama-antofagasta`/`koper-aurubis-hamburg`) | ja — haven-aanloop (gedeeld bestand) |
| b4 | B | zee (containerschip) | zeeknoop -23.80,-71.30 → zeeknoop 37.16690,126.41420 | Stille Oceaan, andere lane dan de bestaande Antofagasta→Yangtze-as (geen zeestraat) | hemelsbreed 17.827; geen zeekm-citaat — MARNET bepaalt de route | MARNET (`--been zee`), nieuw zeebeen | nee |
| b5 | B | zee (haven-aanloop) | zeeknoop 37.16690,126.41420 → `li-daesan-kade` | Daesan-havenfront ligt 17,1 km van de dichtstbijzijnde MARNET-zeeknoop (> 5 km ⇒ haven-aanloop, bakhandleiding §2) | 17,1 (hemelsbreed; `maak_havenaanloop.py` bepaalt het gevaren pad) | nieuw, `maak_havenaanloop.py` | ja — haven-aanloop, reden: > 5 km van de zeeknoop |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `li-atacama-laad` | laadplek | SQM Salar de Atacama | -23.5675, -68.4000 | [1][11] hergebruik letterlijk uit `lithium-atacama-antofagasta.md` §3 | bron-gelegd (hergebruikt anker, zie die brief voor het satellietbeeld) |
| `li-carmen-plant` | verwerkingsknoop (LiCl → LiOH/Li2CO3) | SQM Planta Química de Litio Carmen | -23.6335, -70.2600 | [1][11] hergebruik letterlijk | bron-gelegd (hergebruikt anker) |
| `li-antofagasta-kade` | overslag truck → zee | Puerto Antofagasta, ATI | -23.6500, -70.4088 | [11] hergebruik letterlijk | bron-gelegd (hergebruikt anker) |
| `li-daesan-kade` | overslag zee → (niet getekend: land) | Daesan-havenfront, Seosan (충청남도), algemeen-vracht-/containerterminal (2.000 TEU) naast het petrochemische havenbekken | 37.0131, 126.4243 | [2][7][8][10] | bron-gelegd (z15 gezien: loodsen, containerstapels en een kade met kraanportalen direct ten oosten van het grote tankenpark; kruis valt op het vrachtterrein, niet in het water) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
b1 en b2 zijn letterlijke kopieën van `lithium-atacama-antofagasta` — zie die brief §4 voor de via-punten;
hier geen nieuwe via-punten (geen nieuwe corridorkeuze).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| PQL Carmen (hergebruikt, zie `lithium-atacama-antofagasta.md` §5) | SQM / Nova Andino Litio | LiCl-oplossing → Li2CO3 (210 kt/j) + LiOH (40 kt/j) | zie die brief | [1] |

Geen Koreaanse verwerkingsknoop: er wordt geen fabriek getekend (§6).

## 6 · Stoppunt
De brief stopt bij de Daesan-kade: SK On tekende in 2023 een eigen LiOH-leveringscontract met SQM
(57 kt over 2023–2027) en de ondertekening vond plaats bij SK On's **enige** Koreaanse batterijfabriek in
Seosan [2] — Daesan is de haven van dat industriegebied. Geen bron noemt echter dat SQM's lading specifiek
in Daesan wordt gelost of dat de lading van daar naar Seosan rijdt: **fase D (kade → fabriek) vervalt**,
identiek aan hoe `lithium-atacama-antofagasta` bij de Yangtze-monding stopt zonder Chinese fabriek te
noemen. Dit is de bindende uitkomst van de haalbaarheidstoets: het oorspronkelijke ontwerp (POSCO Future M,
Pohang) is geschrapt omdat geen bron Pohang als bestemming voor SQM-materiaal noemt en POSCO's eigen
Pohang-hydroxidevoorraad uit een ander circuit komt (Argentijnse pekel + Pilgangoora, al gemeten als
`lithium-pilgangoora-gwangyang`) [12].

## 7 · Open punten
- **Pohang-fabrieksanker en fase D geschrapt (bindend, haalbaarheidstoets):** geen van de drie Koreaanse
  afnameovereenkomsten (LGES/SK On/Hyundai-Kia) noemt een fabriekslocatie; POSCO Future M's Pohang-lijn
  draait op een eigen, niet-SQM-keten [12].
- **Daesan is een aanname, geen citaat:** de link SQM→SK On→Seosan is gebrond [2], de link Seosan→Daesan
  (nabijheid, algemene-vracht-/containerkade) is geografisch maar niet met een bron die "SQM's lading landt
  in Daesan" zegt.
- **Gwangyang bewust vermeden:** die haven is al de bestaande `lithium-pilgangoora-gwangyang`-as (POSCO);
  deze keten had anders grotendeels op dezelfde haven geconvergeerd.
- **Jaarvolume niet uitgesplitst:** SK On-SQM = 57 kt LiOH over 5 jaar (2023–2027, ≈ 11,4 kt LiOH/j ≈
  10,0 kt LCE/j bij een omrekenfactor ~0,88) [2]; LGES-SQM (~55 kt LCE 2021–2029, ≈ 6–7 kt/j) [3] en
  Hyundai/Kia-SQM [5] zonder gepubliceerd volume — geen van drie is uitgesplitst tegen Carmen's totaal
  233 kt LCE/j (2025); indicatief klein tegenover de al gemeten China-as (72 %).
- **b4-zeebeen is een schatting:** hemelsbreed 17.827 km; de gevaren MARNET-lane (noordelijker dan de
  bestaande Antofagasta→Yangtze-lane) en het exacte kilometer bepaalt de bake.
- **b5-haven-aanloop:** 17,1 km hemelsbreed tot de dichtstbijzijnde zeeknoop; `maak_havenaanloop.py` kan op
  timeout/geen-pad stranden — terugval is een rechte stippel met dezelfde reden (bakhandleiding §2).
- **b1/b2 blijven letterlijke kopieën** van `lithium-atacama-antofagasta`: niet herbakken, geen tweede
  versie van hetzelfde geojson.

## 8 · Bronnen
[1] SQM, Technical Report Summary Salar de Atacama (SEC 20-F FY2023/FY2025) — zie `lithium-atacama-antofagasta.md` [1][2] voor het volledige citaat (255 km B-385/Ruta 5, 210 kt Li2CO3/j + 40 kt LiOH/j Carmen).
[2] SK Innovation/eng.sk.com, "SK On signs lithium hydroxide supply deal with world's leading producer SQM": "up to 57,000 tons of high-quality lithium hydroxide for five years starting in 2023 … enough … for approximately 1.2 million electric vehicles"; SQM-vertegenwoordigers bezochten tijdens de ceremonie SK On's "battery plant in Seosan, South Chungcheong Province" (geen expliciete leverhaven genoemd). https://eng.sk.com/news/sk-on-signs-lithium-hydroxide-supply-deal-with-worlds-leading-producer-sqm
[3] Fastmarkets, "SQM signs lithium supply agreement with LG Energy Solutions" — ~55 kt LCE totaal 2021–2029. https://www.fastmarkets.com/insights/sqm-signs-lithium-supply-agreement-with-lg-energy-solutions/
[4] KED Global, SK On Seosan-uitbreiding (context: Seosan = SK On's enige Koreaanse batterijcelfabriek, $1,1 mld investering). https://www.kedglobal.com/batteries/newsView/ked202308160018
[5] Metal.com, "SQM secures long-term lithium supply agreement with Hyundai and Kia" (geen fabriekslocatie/volume gepubliceerd). https://news.metal.com/newscontent/102811278-sqm-secures-long-term-lithium-supply-agreement-with-hyundai-and-kia
[6] SK Innovation Newsroom (SKinno News), SK On Seosan-investering — "SK On invests up to KRW 1.5 trillion in facility expansion in Seosan City, South Korea". https://skinnonews.com/global/archives/15462
[7] OpenStreetMap (ODbL) via Nominatim: landuse "harbour" 대산항 (Daesan-haven), way/892901810, centroïde 37.01313, 126.42432. https://www.openstreetmap.org
[8] SeaRates / findaport.com, Port of Daesan: algemene-vrachtterminal + containerterminal (1 berth, 2.000 TEU), vloeibare bulk/petrochemie (Hanwha TotalEnergies, Hyundai Oilbank, KNOC). https://www.searates.com/port/daesan_kr
[9] Wikipedia, "List of oil refineries" — Daesan Refinery (Hyundai Oilbank), regionale context van het havencomplex. https://en.wikipedia.org/wiki/List_of_oil_refineries
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15, live): `v2/build-cache/satcheck/sat-lithium-carmen-pohang-daesan-kade.png`.
[11] `v2/design/routebrieven/lithium-atacama-antofagasta.md` §3/§9 — ankers `li-atacama-laad` (-23.5675,-68.4000), `li-carmen-plant` (-23.6335,-70.2600), `li-antofagasta-kade` (-23.6500,-70.4088) en `v2/build-cache/ais/graaf/aanloop-antofagasta.geojson` (97,1 km, zeeknoop -23.80,-71.30), letterlijk hergebruikt.
[12] Haalbaarheidstoets lithium-carmen-pohang (2026-09-28, intern): webcheck newsroom.posco.com/kedglobal.com — P-PLS levert 20–30 kt LiOH/j aan POSCO Future M Pohang uit een Argentijnse zoutmeer- + eigen Australische (Pilgangoora) toevoer; geen bron koppelt SQM aan Pohang. Reden voor het schrappen van het Pohang-fabrieksanker en fase D.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 5)

**Recept:** `bak_lithium_carmen_pohang()` in `v2/tools/bak_stromen.sh` · draai: `bash v2/tools/bak_stromen.sh lithium-carmen-pohang` ·
schrijft `v2/data/stroomroute-lithium-carmen-pohang.json`.

| # | modaliteit | km gebakken | punten | naad | stippel | toelichting |
|---|---|---|---|---|---|---|
| b1 | truck | 240,2 | 2.152 | 0,00 km | nee | **letterlijke kopie** (sha1-identiek) van been 1 uit `stroomroute-lithium-atacama-antofagasta.json`/profiel `lithium-atacama-carmen` — géén eigen wegscan. ⚠️ De brief noemde 232,4 km (oudere meting van die bronstroom); de huidige bronstroom bakt zelf ook op 240,2 km — geen afwijking van dít recept, bevinding voor de bronbrief. |
| b2 | truck | 22,6 | 555 | 0,00 km | nee | letterlijke kopie van been 2 (profiel `lithium-carmen-antofagasta`), zelfde bronstroom. Brief noemde 21,9 km (zelfde kanttekening als b1). |
| b3 | zee | 97,1 | 46 | 0,00 km | ja — haven-aanloop, gedeeld bestand | letterlijke kopie van `v2/build-cache/ais/graaf/aanloop-antofagasta.geojson` (gedeeld met `lithium-atacama-antofagasta` en `koper-aurubis-hamburg`); MARNET reikt hier niet tot de kade. |
| b4 | zee | 18.767,6 | 1.925 | 0,00 km | nee | nieuw MARNET-zeebeen Antofagasta-zeeknoop → Daesan-zeeknoop. Brief schatte hemelsbreed 17.827 km; de **gevaren MARNET-lane is 18.767,6 km** (+5,3% t.o.v. de hemelsbrede schatting, geen wegkm-citaat dus de ±15%-toets geldt hier als indicatie — binnen die marge). Andere lane dan de bestaande Antofagasta→Yangtze-as, zoals de brief voorspelde. |
| b5 | zee | 17,4 | 16 | 0,00 km | ja — haven-aanloop, reden: >5 km van de zeeknoop (LAR-586) | nieuw, `maak_havenaanloop.py --naam lithium-carmen-pohang-daesan --van 37.0131,126.4243 --naar 37.16690,126.41420`: pad over water gevonden (17,4 km, 16 punten, 0,00 km over land, omwegfactor 1,017) — geen terugval-stippel nodig. ⚠️ Het tool bouwt altijd kade→zeeknoop; de punten zijn na het bakken van de aanloop **omgedraaid** zodat de lijn in reisvolgorde (zeeknoop → kade) ligt en de naad niet vals op 17,4 km uitslaat. |

**Totaal:** 19.144,9 km · 4.694 punten · 4 markers (`li-atacama-laad`, `li-carmen-plant`, `li-antofagasta-kade`, `li-daesan-kade`).

**Toets (bakhandleiding §5):**
- Km per been: b1/b2/b3 zijn letterlijke kopieën (per definitie geen eigen lengtetoets — de bronstroom draagt die); b4/b5 hadden geen echte wegkm-citaat, dus de ±15%-toets geldt als indicatie — b4 zit binnen die marge, b5 (17,4 tegen 17,1 hemelsbreed, +1,8%) ruim binnen.
- Naden: **alle vijf op 0,00 km** — geen enkele naad > 5 km.
- `toets_knikken.py`: 3 + 7 + 1 = 11 knikken ≥ 60°, **0 omkeringen ≥ 150°, 0 terugloop** — de gemelde knikken zijn kopmaak-spikes op b1/b2 (gedeeld met de bronstroom, niet hier ontstaan) en één krappe bocht (R 6.263 m) op het MARNET-zeebeen bij Zuid-Korea (normale laankeuze, geen fout).
- `toets_rechte_benen.py --min-km 5`: geen been van deze stroom in de uitslag — b3 (97,1 km, omwegfactor 1,002 impliciet uit de 46 gevaren punten) en b5 (17,4 km, omwegfactor 1,017) zijn beide een gevaren pad, geen kaarsrechte lijn, en worden dus terecht niet gevlagd.
- `json.load` slaagt, `versie` = 2, `punt_formaat` = `lonlat`, modaliteiten ⊂ {zee, truck}, elk been ≥ 2 punten, bestand 98.832 byte (96,5 KB).

**Lessen/toelichting per stippel/aanloop:**
- b3 is bewust géén nieuwe meting: een gedeeld bestand wordt letterlijk hergebruikt, ook al levert dat (net als bij de bronstroom) geen nieuwe informatie op — dat is precies het punt van "gedeeld been = letterlijke kopie".
- b5 is de eerste keer in deze keten dat een `maak_havenaanloop.py`-uitvoer moest worden **omgedraaid** vóór het bakken: het tool neemt altijd `--van` als kade-anker en `--naar` als zeeknoop, en dat is niet per constructie de reisvolgorde. Bij een *aankomende* aanloop (zeeknoop → kade, zoals hier) moet de puntenlijst dus gespiegeld worden — anders meet de naadtoets een vals gat van 17,4 km tussen b4 en b5 in plaats van 0,00 km. Voor een *vertrekkende* aanloop (zoals b3, kade → zeeknoop) is geen spiegeling nodig.
- Geen fase D/E: de keten stopt bij `li-daesan-kade`, precies zoals de brief voorschrijft (bindende uitkomst van de haalbaarheidstoets — geen bron koppelt SQM-lading aan Daesan of aan de Seosan-fabriek).

**Registerregel (centraal, niet door mij gedaan):** `{ sleutel: "li-cp", bestand: "stroomroute-lithium-carmen-pohang.json", grondstof: "lithium", aan: true }`.
Kleur: bestaande lithium-kleur (`#c06bff`), geen nieuwe entry in `stroomstijl.js` nodig.
