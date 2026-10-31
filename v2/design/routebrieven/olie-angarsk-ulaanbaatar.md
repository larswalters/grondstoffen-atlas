# Routebrief (licht) · olie — Angarsk (Rusland) → Sukhbaatar → Ulaanbaatar (Mongolië), geraffineerd product

**stroom-id:** `olie-angarsk-ulaanbaatar` · **geschreven:** 2026-10-31 · **werkwijze:** licht (M31 golf 17) · **status:** gebakken
**Keten in één zin:** benzine en diesel (GERAFFINEERD product, geen ruwe olie) uit de Rosneft-raffinaderij ANHK in Angarsk per
**spoor** (ketelwagons) over de Trans-Sib (Irkutsk, Ulan-Ude), de Selenga-lijn naar Naushki, grensstation Sukhbaatar en de
Ulaanbaatar Railway (Darkhan) naar een tankenpark aan het spoor in Ulaanbaatar (aannemelijk: één bron, depot niet benoemd).
**Welke as van het verhaal:** *Russische brandstof naar Mongolië in de crisis van 2026.* Mongolië importeert alle geraffineerde
brandstof, 90–97% uit Rusland per spoor [1][2][3]. Volume: Rusland → Mongolië jan–jul 2026 1,05 Mt diesel + 515 kt benzine [3] =
ca. **58 kb/d** (eigen omrekening, 7,46 en 8,45 vat/t); intergouvernementele afspraak 1,8–1,9 Mt/j = ca. 40 kb/d [4]; totaal
verbruik 3 Mt/j ca. 65 kb/d [4]. **Angarsk-aandeel niet gepubliceerd**: Angarsk en Achinsk zijn de hoofdleveranciers [1][2].

## 1 · Ketenkaart
```
ANHK Angarsk `ol-angarsk-ref` ──(b1 spoor · Trans-Sib → Selenga-lijn → grens Naushki/Sukhbaatar → Ulaanbaatar Railway ·
   1.127,5 km eigen router, geen gepubliceerde spoorkm)──► brandstofdepot Ulaanbaatar `ol-ub-depot` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | ANHK Angarsk → tankenpark Ulaanbaatar | Angarsk – Irkutsk – Ulan-Ude (Trans-Sib, deelt ca. 440 km met uranium-priargunsky-seversk, tegengestelde richting) – Naushki/Sukhbaatar – Darkhan – Ulaanbaatar | 1.127,5 [eigen Dijkstra over het 1-op-1-net, 0 omkeringen; geen gepubliceerde spoorkm, de ±15%-toets is hier niet toepasbaar] | toets_spoorroute, een run | nee: doorgetrokken; aannemelijk: één bron staat in de beennaam |

Enige corridor, geen alternatief: een run (niet in drie runs knippen, via Sukhbaatar geeft een omkering van 171 graden).
Indicatie langs het spoor: Angarsk→Irkutsk ca. 34 · Irkutsk→Ulan-Ude ca. 455 · Ulan-Ude→Naushki ca. 242 (Wikipedia-kaartchainage 258 [6]) ·
Naushki→Ulaanbaatar ca. 400 (Wikipedia-chainage grens→Ulaanbaatar 404 [6]) km. De router raakt Ulan-Ude op 0,4 km, Sukhbaatar 0,1 km,
Darkhan 0,4 km, Naushki 2,1 km. Geen haven-aanloop (geen zee).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-angarsk-ref` | laadplek, raffinaderij (fase A) | Angarsk Petrochemical Company (Rosneft ANHK), Irkutsk oblast | 52.5470, 103.9300 | [1][2][7] | bron-gelegd (z15 gezien: tankparken en procesunits in de raffinaderijzone, spoorbundel enkele honderden m west; spoorsnap 0,25 km). Het ontwerpanker 52.5502/103.9195 lag in bos aan de zoom en is verworpen |
| `ol-ub-depot` | losplek, brandstofdepot (fase A, stoppunt) | tankenpark aan het spoor, Ulaanbaatar (zuidkant spoorzone) | 47.9076, 106.8385 | [1][7] | aannemelijk: één bron (z17 gezien: cluster van ca. 10 witte tanks met eigen aftakspoor direct zuid van het rangeeremplacement met kleurige tankwagons; spoorsnap 0,10 km; geen bron noemt een depotnaam of exploitant) |

## 4 · Via-punten
Geen. Enige corridor; het ontwerppunt Ulan-Ude (51.8333, 107.6000, uit uranium-priargunsky-seversk) wordt dus niet als via-punt gebruikt,
alleen als controle (route raakt het op 0,4 km).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| ANHK Angarsk | Rosneft (sinds 2007) | ruwe olie → benzine, diesel, jet | 10,2 Mt/j ontwerpcapaciteit (ca. 205 kb/d), niet allemaal naar Mongolië | [2] |
| tankenpark Ulaanbaatar | onbekend (Petrovis exploiteert 11 depots met 124 miljoen liter, niet gekoppeld aan dit park) | spoor → opslag → tankwagens naar pompstations | niet gepubliceerd | [1] |

## 6 · Stoppunt
Het tankenpark aan het spoor in Ulaanbaatar: de brandstof gaat daar van spoor naar tankwagens en pompstations, en geen bron noemt een
afzonderlijk volgend depot per lading. Fase D/E vervallen (verdeling over ca. 400 pompstations is geen keten met een benoemde fabriek).

## 7 · Open punten
- **Angarsk-aandeel en tonnage per bron niet gepubliceerd**; Achinsk is tweede hoofdleverancier, dus Angarsk-aandeel is een aanname.
- **Depot niet benoemd**: het eindpunt is een door satelliet gevonden tankcluster aan het spoor, geen bevestigde exploitant (Petrovis noemt 11 depots zonder adres).
- **Geen gepubliceerde spoorkilometers** voor Angarsk → Ulaanbaatar; 1.127,5 km is eigen router, de chainage-controle (±6%) is indicatie.
- Volumecijfers komen uit nieuws (Reuters-citaat via The Star) en één blog voor de afspraak van 1,8–1,9 Mt/j [4], niet uit een officiele tekst.
- **Gedeeld spoor** Ulan-Ude–Irkutsk met de uraniumstroom in tegengestelde richting; geen kopie nodig (andere route-uiteinden), alleen naamsvermelding in beennaam.
- TASS-bron (genoemd in het ontwerp) was onbereikbaar en is niet gebruikt.

## 8 · Bronnen
[1] Petrovis Mongolia, "Import" — Angarsk en Achinsk (Rosneft) leveren, spoor via Naushki–Sukhbaatar, 11 depots/124 mln liter, volumes 2021. https://en.petrovis.mn/import
[2] MidstreamIQ, "The Angarsk Vulnerability", juli 2026 — Mongolië 90–95% Russisch, Angarsk 10,2 Mt/j hoofdbron per spoor, niet getroffen (Omsk wel). https://midstreamiq.substack.com/p/the-angarsk-vulnerability
[3] Reuters via The Star, 2026-09-03, "Mongolia bears brunt of Russia's fuel crunch" — diesel 1,05 Mt en benzine 515 kt jan–jul 2026, juli 173 kt. https://www.thestar.com.my/news/world/2026/09/03/mongolia-bears-brunt-of-russia039s-fuel-crunch-official-says
[4] Indrastra, oktober 2026, "Mongolia's Fuel Crisis" — afspraak 2024 1,8–1,9 Mt/j + 60 kt jet; verbruik 3 Mt/j, 97% Russisch (alleen via zoekresultaat gezien, niet geverifieerd). https://www.indrastra.com/2026/10/mongolias-fuel-crisis-when-third.html
[5] Asia News Network, Rusland belooft ononderbroken brandstofleveringen aan Mongolië 2026. https://asianews.network/?p=252999
[6] Wikipedia, "Trans-Mongolian Railway" — kaartchainage Ulan-Ude 5.642, Naushki 5.900, grens→Ulaanbaatar 404 km. https://en.wikipedia.org/wiki/Trans-Mongolian_Railway
[7] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-olie-angarsk-ulaanbaatar-angarsk-anhk.png` (z15), `sat-olie-angarsk-ulaanbaatar-ub-depot.png` (z15), `sat-olie-angarsk-ulaanbaatar-ub-depot-z17.png`; OSM landuse-way 450690704 (ANHK).
[8] Eigen run: `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs --van=52.5470,103.9300 --naar=47.9076,106.8385 --naam=olie-angarsk-ulaanbaatar-angarsk-ulaanbaatar` — 1.127,5 km, 1.139 edges, 3.502 punten, 0 omkeringen, snap 0,25 / 0,10 km; `v2/build-cache/ais/graaf/spoorroute-olie-angarsk-ulaanbaatar-angarsk-ulaanbaatar.geojson`.

## 9 · Gebakken (2026-10-31, lichte werkwijze, M31 golf 17)
`v2/data/stroomroute-olie-angarsk-ulaanbaatar.json` · 65,1 KB · versie 2, lonlat · 1 been · **1.139,6 km** · 3.502 punten · 2 markers.
Recept: `bash v2/tools/bak_stromen.sh olie-angarsk-ulaanbaatar` (functie `bak_olie_angarsk_ulaanbaatar`).

| # | modaliteit | km (gebakken) | km (brief) | stippel | naad |
|---|---|---|---|---|---|
| b1 | spoor | 1.139,6 | 1.127,5 eigen router (geen gepubliceerde spoorkm) | nee, doorgetrokken | n.v.t. |

- **Geometrie:** de tussenuitvoer van de briefagent is hergebruikt (compleet, FeatureCollection, 3.502 punten):
  `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=52.5470,103.9300" "--naar=47.9076,106.8385" "--naam=olie-angarsk-ulaanbaatar-angarsk-ulaanbaatar"`
  → `v2/build-cache/ais/graaf/spoorroute-olie-angarsk-ulaanbaatar-angarsk-ulaanbaatar.geojson`. Eén run, geen via-punten, 0 omkeringen.
- **Km-verschil 1.127,5 → 1.139,6 (+1,1%):** de router telt edge-lengtes, `hecht_marnet` meet de getekende polyline. Binnen de indicatie
  (chainage Angarsk-Irkutsk 34 + Irkutsk-Ulan-Ude 455 + Ulan-Ude-Naushki 258 + grens-Ulaanbaatar 404 = ca. 1.151 km). Geen ±15%-norm: er is geen gepubliceerde spoorkm.
- **Markers:** `ol-angarsk-ref` 0,25 km van de lijn (spoorsnap, bron-gelegd) · `ol-ub-depot` 0,10 km (aannemelijk: één bron, depot niet benoemd). Beide binnen 0,5 km.
- **Toetsen:** `toets_knikken.py` 0 knikken, 0 omkeringen · `toets_rechte_benen.py --min-km 5` meldt de stroom niet · json.load ok, modaliteit alleen `spoor`.
- **Geen stippel, geen haven-aanloop, geen vlucht, geen leiding, geen kopie:** één spoorbeen over het 1-op-1-net.
- **Open (ongewijzigd uit §7):** Angarsk-aandeel per bron, depotnaam/exploitant, gepubliceerde spoorkm, volumes uit nieuws/blog.
- **Lessen:** (1) een `\`+newline in een Python-heredoc via de Bash-tool komt als regelvervolg aan en plakt de functieregels aan elkaar;
  de gebakken functie is daarna herschreven met `chr(92)` en `chr(10)`. (2) een `bash -n`-fout tijdens de bake ("line 15216") kwam van een
  gelijktijdige edit van een andere agent; daarna schoon.
