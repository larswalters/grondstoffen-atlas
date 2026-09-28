# Routebrief (licht) · nikkel — Sotkamo (Terrafame) → Kokkola (Finland)

**stroom-id:** `nikkel-sotkamo-kokkola` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) · **status:** gebakken
**Keten in één zin:** nikkelsulfaat (batterijkwaliteit) van Terrafame's bioheap-leaching-mijn + sulfaatfabriek in Sotkamo
(Kainuu) per **spoor** — corridor via Kontiomäki–Iisalmi–Ylivieska (Savonrata/Pohjanmaan rata), aannemelijk — naar de
Kokkolan syväsatama (Port of Kokkola), waar havenoperator Rauanheimo Terrafame's logistiek verzorgt; geen fase B-been
getekend, want geen bron noemt een afnemer/bestemming ná de haven.
**Welke as van het verhaal:** *de resolutie van de eerder afgewezen Oulu-as* (golf 2: `nikkel-sotkamo-oulu`, verworpen
wegens een fictieve marktbestemming zonder coördinaat). Hier eindigt de lijn op een echt, satelliet-gelegd havenanker
(Kokkola, al gelegd voor `kobalt-kcc-kokkola`) — Terrafame battery chemicals plant, nameplate **170 kt
nikkelsulfaat/j ≈ 37,4 kt Ni-inhoud/j** (+ 7,4 kt kobaltsulfaat) [nikkel-sitelaag B24].

## 1 · Ketenkaart
```
Terrafame Sotkamo `ni-sotkamo-terrafame` ──(b1 spoor · via Kontiomäki–Iisalmi–Ylivieska, aannemelijk · ~357 km
    hemelsbreed via-punten-som)──► Kokkolan syväsatama `ni-kokkola-kade` ── stoppunt (fase B: geen been, alleen marker)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `ni-sotkamo-terrafame` → `ni-kokkola-kade` | VR-spoornet via Kontiomäki–Iisalmi–Ylivieska (Savonrata/Pohjanmaan rata), aannemelijk t.o.v. de kortere route via Oulu (Kontiomäki–Oulu–Kokkola, ~360 km hemelsbreed-som — bijna gelijk; de échte spoorkm beslissen, niet de hemelsbrede schatting) | hemelsbreed ~357 km (som via-punten), geen spoorkm gepubliceerd voor déze lading | `toets_spoorroute` (BAKE_SUFFIX=-raw; meerdere runs via de drie via-punten, kop→Kontiomäki, Kontiomäki→Iisalmi, Iisalmi→Ylivieska, Ylivieska→staart) | nee |
| — | B | — | (vervalt) | `ni-kokkola-kade` → stoppunt (geen afnemer gedocumenteerd) | n.v.t. | geen been getekend, alleen marker op `ni-kokkola-kade` | n.v.t. |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-sotkamo-terrafame` | mijn + sulfaatfabriek (kop van het spoor) | Terrafame (bioheap-leaching-mijn + battery chemicals plant), Sotkamo, Kainuu | 63.9782, 27.9998 | [1][2][7] eigen satellietblik (deze sessie) | bron-gelegd (z16 gezien: procesgebouwen, silo's en tanks direct naast een spooremplacement/-siding die vanuit het noordwesten het terrein in loopt — de Wikipedia-coördinaat voor de "Talvivaara mine" (63.9674,28.0179) ligt 1,2 km zuidelijker middenin de bioheap-leachvelden; dit punt is verschoven naar de procesfabriek met directe spooraansluiting) |
| `ni-kokkola-kade` | overslag spoor → zee (havenmarker, geen been getekend erna) | Kokkolan syväsatama / Port of Kokkola | 63.8645, 23.0270 | [4][6][8] — **letterlijk hergebruikt anker** uit `kobalt-kcc-kokkola` (`co-kokkola-kade`) | bron-gelegd (z16 gezien in `kobalt-kcc-kokkola`: pier met kranen, bulklading in hopen, vaartuig(en) aan de kade — niet opnieuw gecheckt deze sessie, letterlijke hergebruik) |

## 4 · Via-punten (alleen b1 — corridorkeuze bij Kontiomäki, Iisalmi en Ylivieska)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Kontiomäki (spoorknoop) | 64.3373, 28.1163 | de corridorkeuze zelf: hier splitst de route naar Iisalmi/Ylivieska (Savonrata-zuidwaarts) versus de kortere aftakking naar Oulu — dezelfde knoop waarover Kostomuksha-ertstreinen naar Kokkola rijden [8][9] |
| b1 | 2 | Iisalmi (spoorknoop) | 63.5603, 27.2003 | pint de route op de Savonrata in plaats van een noordelijke sluipweg via Oulu |
| b1 | 3 | Ylivieska (spoorknoop) | 64.0719, 24.5400 | overstap op de Pohjanmaan rata (kust-hoofdlijn) richting Kokkola-Ykspihlaja |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Terrafame Sotkamo | Terrafame Oy (Finse staat) | nikkel-/kobalthoudend erts (bioheap-leaching) → nikkelsulfaat + kobaltsulfaat | 170 kt nikkelsulfaat/j nameplate ≈ 37,4 kt Ni-inhoud/j + 7,4 kt kobaltsulfaat/j | [1][2][nikkel-sitelaag B24] |
| Kokkolan syväsatama | Port of Kokkola / Rauanheimo (stuwadoor) | nikkelsulfaat (spoor) → bulk-/containerlading (zee) | Rauanheimo verzorgt "logistics of production consumables as well as finished product through the port of Kokkola" voor Terrafame, incl. de battery chemicals plant [4] | [4][6] |

## 6 · Stoppunt
De brief stopt bij de Kokkolan syväsatama: Rauanheimo bevestigt Terrafame's haven-logistiek via Kokkola, maar geen
bron noemt een specifieke afnemer, klantfabriek of vervolgbestemming na de haven — de haven is nu bron-bevestigd,
het "waarheen daarna" blijft een expliciet open punt (geen aangenomen node, conform de haalbaarheidstoets).

## 7 · Open punten
- **Modaliteit/corridor vóór de haven (spoor via Kontiomäki–Iisalmi–Ylivieska vs. de kortere Kontiomäki–Oulu-route)
  is niet bron-bevestigd** — beide sommen hemelsbreed bijna gelijk (~357 vs. ~360 km); `toets_spoorroute` beslist bij
  bake welke corridor het 1-op-1-spoornet daadwerkelijk kiest, en dat blijft "aannemelijk" tot dan (haalbaarheidstoets-aanpassing).
- **Of Terrafame's lading werkelijk via Kokkola gaat i.p.v. via Oulu (dichterbij) is nu wél bron-ondersteund**
  (Rauanheimo: *"the cooperation between Rauanheimo and Terrafame deepens"*, haven-logistiek incl. de nieuwe battery
  chemicals plant [4]) — dit resolueert het eerder open punt uit het ketenontwerp, maar noemt zelf geen spoorlijn.
- **Geen afnemer/bestemming ná Kokkola gedocumenteerd** — fase B blijft bewust een marker zonder been (geen
  aangenomen "Europese afzetmarkt"-node, precies de fout die golf 2 `nikkel-sotkamo-oulu` deed afwijzen).
- **Exacte spoorlijnnaam/-eigenaar van de siding bij het Terrafame-terrein** niet met naam bevestigd (Overpass
  onbereikbaar deze sessie); de satellietblik toont wél een spoorsiding tot op het terrein.
- **b0/last-mile van het terrein-anker naar het hoofdnet** niet vooraf gemeten — bak-agent meet de snap; alleen een
  stippel toevoegen als de afstand > ~2 km blijkt (werkwijze §1).

## 8 · Bronnen
[1] Terrafame, "Battery chemicals". https://www.terrafame.com/offering/battery-chemicals.html
[2] IM-Mining, 25-10-2018, "Terrafame gets go ahead for nickel-cobalt sulphate plant at Sotkamo, Finland". https://im-mining.com/2018/10/25/terrafame-go-ahead-nickel-cobalt-sulphate-plant-sotkamo-finland/
[3] Science|Business, "Business Finland, BASF's new battery materials plant support EU battery value chain". https://sciencebusiness.net/network-updates/business-finland-basfs-new-battery-materials-plant-support-eu-battery-value-chain
[4] Oy M. Rauanheimo Ab, 04-05-2021, "The cooperation between Rauanheimo and Terrafame deepens" — haven-logistiek Kokkola voor productiegrondstoffen én eindproduct, incl. de nieuwe battery chemicals plant. https://www.rauanheimo.com/en/2021/05/04/the-cooperation-between-rauanheimo-and-terrafame-deepens/
[5] Wood Mackenzie, "Sotkamo, Terrafame — Nickel sulphate refinery Report". https://www.woodmac.com/reports/metals-sotkamo-terrafame-nickel-sulphate-refinery-150006792/
[6] Oy M. Rauanheimo Ab, "Port of Kokkola". https://www.rauanheimo.com/en/port-of-kokkola/
[7] Wikipedia (en), "Talvivaara mine" — coördinaat 63.9674,28.0179, eigendom Terrafame sinds 2015, bioheap-leaching. https://en.wikipedia.org/wiki/Talvivaara_mine
[8] Wikipedia (en), "Oulu–Kontiomäki railway" — 166,1 km, verbindingen bij Kontiomäki (Iisalmi–Kontiomäki, Kontiomäki–Vartius), Kostomuksha-taconiettreinen naar Kokkola voor overslag. https://en.wikipedia.org/wiki/Oulu%E2%80%93Kontiomäki_railway
[9] Wikipedia (en), coördinaten via de MediaWiki-API voor "Kontiomäki railway station" (64.3373,28.1163), "Iisalmi railway station" (63.5603,27.2003), "Ylivieska railway station" (64.0719,24.5400), "Kokkola railway station" (63.8347,23.1314). https://en.wikipedia.org
[10] OpenStreetMap/Nominatim (ODbL) — "Terrafame Stadion"/"Talvivaarantie"/"Antell Terrafame" (Talvivaaran kaivos, Sotkamo), controlepunten rond het Terrafame-terrein. https://www.openstreetmap.org
[11] Esri World Imagery via `v2/tools/sat_check.py` (z15–z16) — `sat-nikkel-sotkamo-kokkola-terrafame.png`, `sat-nikkel-sotkamo-kokkola-fabriek.png`, `sat-nikkel-sotkamo-kokkola-fabriek2.png`; havenanker `ni-kokkola-kade` letterlijk hergebruikt (satellietblik zat al in `kobalt-kcc-kokkola` §3/§8).
[12] Interne invoer: ketenontwerp + haalbaarheidstoets `nikkel-sotkamo-kokkola.json` (2026-09-28, M31 golf 6) — Rauanheimo-webcheck, DRC/Kokkola-context, sea-knoop-referentie via `kobalt-kcc-kokkola`.
[B24] `v2/design/nikkel-sitelaag.json`, site `w-terrafame-sotkamo` — 170 kt nikkelsulfaat/j nameplate ≈ 37,4 kt Ni-inhoud/j.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Recept:** `bak_nikkel_sotkamo_kokkola()` in `v2/tools/bak_stromen.sh` (draaien: `bash v2/tools/bak_stromen.sh
nikkel-sotkamo-kokkola`) · **1 keten, 4 benen, alle spoor, geen stippel.**

| # | modaliteit | van → naar | km | punten | naad |
|---|---|---|---|---|---|
| b1a | spoor | Terrafame Sotkamo → Kontiomäki | 67,1 | 154 | — |
| b1b | spoor | Kontiomäki → Iisalmi (Savonrata) | 107,0 | 234 | 0,00 km |
| b1c | spoor | Iisalmi → Ylivieska (Savonrata) | 153,7 | 187 | 0,00 km |
| b1d | spoor | Ylivieska → Kokkolan syväsatama (Pohjanmaan rata) | 85,9 | 223 | 0,00 km |
| **totaal** | | | **413,7 km** | **798 punten** | |

**5 markers** (`ni-sotkamo-terrafame` · Kontiomäki · Iisalmi · Ylivieska · `ni-kokkola-kade`), bestand
`v2/data/stroomroute-nikkel-sotkamo-kokkola.json`, **15,3 KB**.

**Corridorkeuze opgelost (open punt 1):** `BAKE_SUFFIX=-raw toets_spoorroute.mjs` op het 1-op-1-spoornet is vier
keer gedraaid langs de drie via-punten van §4, en apart nog twee keer langs het alternatief via Oulu
(64.3373,28.1163 → 65.0121,25.4651 → 63.8645,23.0270, niet in de bake gebruikt — geojson met suffix `-alt-` in
`v2/build-cache/ais/graaf/`, blijft ter referentie staan). Uitkomst: Kontiomäki→Kokkola via Iisalmi–Ylivieska is
**343,7 km**, via Oulu **367,9 km** — de Savonrata-corridor is 24,2 km korter en dus de daadwerkelijk gekozen
route, precies de "aannemelijk"-corridor van de brief. Alle vier de runs snapten op het Finse hoofdnetcomponent
(1.144.150 km) met snaps van 0,03–0,12 km en **0 bochten ≥60° na de keerstraf** — geen kopmaak-plekken, geen
omwegen.

**Km-toets:** geen gepubliceerde spoorkm voor dit traject (brief §2). Totaal 413,7 km tegen de hemelsbreed-som
van de brief (~357 km, som van de vier via-punt-stukken) = **+15,9%** — net buiten de indicatieve ±15%-marge,
maar die marge geldt hier **als indicatie, niet als norm** (werkwijze: "hemelsbreed X km, geen wegkm"-regel naar
analogie op spoor toegepast). Verklaring: de hemelsbrede som onderschat de echte spoorafstand systematisch,
want elk van de vier stukken volgt een reële boog i.p.v. een rechte lijn (grootcirkel-verhoudingen 1,08–1,65 op
individuele stukken, mediaan ~1,1) — geen bevinding die op fouten wijst, gewoon het verschil tussen hemelsbreed
en spoorgeometrie op vier opeenvolgende stukken.

**Naden:** alle drie de tussen-naden **0,00 km** — elk been-geojson begint exact waar het vorige eindigt (dezelfde
coördinaten als via-punt). `toets_knikken.py`: **0 knikken ≥60°, 0 omkeringen** over alle vier de benen.
`toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom komt in de lijst van rechte lijnen ≥5 km —
alle vier de benen hebben echte spoorkromming (geen doorgetrokken been is een rechte-lijn-aanname).

**Snap/last-mile:** Terrafame-anker (63.9782,27.9998) snapt op 0,12 km, Kokkola-anker (63.8645,23.0270) op
0,10 km — beide ruim onder de 2 km-drempel uit §7 (open punt 5); **geen last-mile-stippel toegevoegd.**

**Stippel/aanloop/vlucht/leiding:** geen — de hele keten is doorgetrokken spoor, geen stippel, geen haven-aanloop
(geen zeebeen), geen luchtbeen, geen leiding.

**Letterlijke kopie:** alleen het anker `ni-kokkola-kade` (63.8645,23.0270) is een letterlijk hergebruikt punt uit
`kobalt-kcc-kokkola` (`co-kokkola-kade`) — geen gedeeld been/geojson.

**Fase B:** vervalt zoals beargumenteerd in §6 — geen been getekend ná `ni-kokkola-kade`, alleen de marker; geen
afnemer/bestemming gedocumenteerd ná de haven.

**Toets-contract:** `versie` 2 · `punt_formaat` `lonlat` · alle modaliteiten `spoor` (in de toegestane set) · elk
been ≥2 punten (min. 154) · bestandsgrootte 15,3 KB (ruim onder de ~300 KB-norm).

**Lessen:**
- De "corridorkeuze niet bron-bevestigd"-onzekerheid uit de brief was met het bestaande gereedschap
  (`toets_spoorroute.mjs`, twee extra runs) in enkele minuten op te lossen — bij een hemelsbreed-bijna-gelijk
  via-puntenpaar loont het om beide corridors gewoon te routeren in plaats van "aannemelijk" te laten staan.
- Vier losse `toets_spoorroute`-runs zonder `--via`-vlag geven bij een schone corridorkeuze (geen kopmaak,
  geen omwegen) een naad van exact 0,00 km tussen de stukken, zolang de eindcoördinaat van run N exact de
  startcoördinaat van run N+1 is.

**Registerregel voor `main.js` (centraal, niet door deze bak-agent):**
`{ sleutel: "ni-sk", bestand: "stroomroute-nikkel-sotkamo-kokkola.json", aan: true }`
