# Routebrief (licht) · kolen — Taldinsky → Trans-Sib → Vostochny (Rusland)

**stroom-id:** `kolen-taldinsky-vostochny` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** Kuzbass-steenkool (thermisch) van de Taldinsky-dagbouw per spoor over vier opeenvolgende
Trans-Siberische etappes (Taishet → Chita → Khabarovsk, samen ~5.931 km — de langste landcorridor van de atlas)
naar de laadkade van Vostochny Port aan de Stille Oceaan; geen zeebeen getekend — geen bron noemt een specifieke
Aziatische loshaven.
**Welke as van het verhaal:** as 5 — de Russische oost-draai na het EU-kolenembargo van 2022: Rusland exporteerde
198 Mt kolen in 2024, 75 % naar Azië [5]; Vostochny Port (~55 Mt capaciteit, uitbreiding naar ~70 Mt goedgekeurd)
is de belangrijkste Pacific-uitgang, met Kuzbassrazrezugol (KRU/UMMC) als moederbedrijf van de terminal én
hoofdleverancier [2][3][6].

## 1 · Ketenkaart
```
Taldinsky-groeve `kolen-taldinsky-laad` ──(b1 spoor · Kuzbass-net → Trans-Sib → Taishet · ~1.068 km)──►
Taishet (via, BAM-splitsing) ──(b2 spoor · Trans-Sib hoofdlijn · ~1.653 km)──► Chita (via)
──(b3 spoor · Trans-Sib hoofdlijn · ~2.306 km)──► Khabarovsk (via)
──(b4 spoor · Trans-Sib/Ussuri-lijn · ~905 km)──► Vostochny-laadkade `kolen-vostochny-kade` ⏹ stoppunt
   └── vertakking (niet getekend): zeeschip → Japan/Korea/China/Taiwan/India/NL (GEM-bestemmingstypen [2]) —
       geen bron voor één specifieke loshaven
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor (2024; RZD-vervoersquota Oostelijk Polygon maken het jaarvolume volatiel) | `kolen-taldinsky-laad` → Taishet | Kuzbass-net (Artyshta/Novokuznetsk) → Novosibirsk-zuid/Yurga → Krasnoyarsk → Taishet | 1.067,5 [diagnose-meting] | toets_spoorroute (`BAKE_SUFFIX=-raw`, rusland-siberie) | korte stippel bij het emplacement (mijn-eigen railaansluiting ontbreekt in OSM) |
| b2 | A | spoor | Taishet → Chita | Trans-Sib hoofdlijn (boven de BAM-splitsing) | 1.652,9 [diagnose-meting] | toets_spoorroute (rusland-siberie) | nee |
| b3 | A | spoor | Chita → Khabarovsk | Trans-Sib hoofdlijn | 2.305,9 [diagnose-meting] | toets_spoorroute (rusland-siberie + rusland-verrehoosten) | nee |
| b4 | A | spoor | Khabarovsk → `kolen-vostochny-kade` | Trans-Sib/Ussuri-lijn → Nachodka-tak | 904,8 [diagnose-meting] | toets_spoorroute (rusland-verrehoosten) | nee |

Som 5.931,1 km tegen ~5.470 km gepubliceerd (Coal Age: Kemerovo → Vostochny 3.400 mijl) [4] = **+8,4 %**, binnen
de ±15 %-norm. De drie via-punten in §4 zijn niet decoratief maar **verplicht** — zie de gauge-sluipweg-waarschuwing daar.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `kolen-taldinsky-laad` | mijn / laadgebied | Taldinsky open pit (Kuzbassrazrezugol/UMMC), Prokopjevsk-district, Kemerovo | 54.1772, 87.1906 | [1] | bron-gelegd (z15 gezien: dagbouwmijn met meerdere afgravingsbanken en waterplassen op de putbodem, haulwegen eromheen; het GEM-punt ligt in de put zelf — de specifieke railaansluiting/laadstation op de Erunakovo-tak is op dit beeld niet te onderscheiden, vandaar de stippel in b1) |
| `kolen-vostochny-kade` | overslag / laadkade | Vostochny Port JSC kolenterminal, Wrangel-baai, Nachodka | 42.7555, 133.0680 | [2][7] | bron-gelegd (z17 gezien: laadkade met een beladen bulkcarrier langszij, kolenstapels, stacker-reclaimers, transportbanden en een spoorbundel op het achterterrein — ondubbelzinnig de kolenterminal, niet de Wikipedia-centroïde 350 m verderop in de baai) |

## 4 · Via-punten (b1–b4, elk apart geroutet — corridorkeuze is verplicht, geen decoratie)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1/b2 | 1 | Taishet | 55.9500, 98.0167 | pint de Trans-Sib boven de BAM-splitsing; zonder dit punt kan een vrije Dijkstra de BAM-tak nemen |
| b2/b3 | 2 | Chita | 52.0500, 113.4667 | **verplicht**: zonder dit punt geeft een vrije Dijkstra 4.917 km met een omkering in Harbin — de router neemt dan Zabaikalsk–Manzhouli–Harbin–Suifenhe (Chinees 1435 mm-net), want het 1-op-1-spoornet bewaakt geen spoorwijdte |
| b3/b4 | 3 | Khabarovsk | 48.4833, 135.0833 | idem — pint de route op de Trans-Sib/Ussuri-lijn i.p.v. de kortere Chinese sluipweg |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Vostochny Port kolenterminal | Vostochny Port JSC (moederbedrijf Kuzbassrazrezugol JSC/UMMC) | spoor (Kuzbass/Jakoetië/Chakassië) → zeeschip export | ~55 Mt/j (uitbreiding naar ~70 Mt goedgekeurd, 2022); export 25,6 Mt (2022), 13,4 Mt (H1 2024) — "onderbenut" | [2][6][7] |

## 6 · Stoppunt
De brief stopt op de Vostochny-laadkade: geen bron noemt welke Chinese/Aziatische haven de kolen lost, dus het
zeebeen wordt niet getekend — alleen als marker-noot "bestemmingstype: Japan/Korea/China/Taiwan/India/Nederland
(GEM)" [2].

## 7 · Open punten
- Taldinsky-laadstation (de specifieke railaansluiting op de Erunakovo-tak) is niet apart gelegd — het GEM-punt
  ligt in de put zelf; bij het bakken hoort hier een emplacementgat/korte stippel, geen doorgetrokken lijn tot in de put.
- Geen bron voor een specifieke Aziatische loshaven → geen zeebeen getekend (zie §6).
- Taldinsky-jaarproductie voor de huidige periode is niet vastgesteld: GEM geeft 9,1 Mt (2023, raming), eerdere
  piek 13,36 Mt (2017); geen recenter cijfer gevonden.
- Aandeel van Taldinsky/KRU specifiek in de ~55 Mt Vostochny-doorzet is niet gekwantificeerd — KRU is
  moederbedrijf/hoofdleverancier [3][6], niet de enige leverancier (ook Jakoetië, Chakassië) [2].
- RZD-vervoersquota op het Oostelijk Polygon maken het jaarvolume van deze specifieke as volatiel; niet in cijfers gevangen.
- Alternatief met kortere meting maar minder verhaal (niet gekozen): Elga (Jakoetië) → Vanino/Elga-haven.

## 8 · Bronnen
[1] Global Energy Monitor, Taldinsky Coal Mine — coördinaat 54.177222,87.190556 (exact); productie 9,1 Mt (2023, raming), 13,36 Mt (2017); eigenaar Kuzbassrazrezugol JSC (100 %), UMMC 52,7 %. https://www.gem.wiki/Taldinsky_Coal_Mine
[2] Global Energy Monitor, Vostochny Port Coal Terminal — capaciteit 55 Mt/j, export 25,6 Mt (2022), 13,4 Mt (H1 2024), bron Kuzbass/Jakoetië/Chakassië, bestemming Japan/Korea/China/Taiwan/overig Azië-Pacific/India/Nederland. https://www.gem.wiki/Vostochny_Port_Coal_Terminal
[3] Global Energy Monitor, Vostochny Port — eigenaar Vostochny Port JSC (Starlion Limited, Cyprus), moederbedrijf Kuzbassrazrezugol JSC. https://www.gem.wiki/Vostochny_Port
[4] Coal Age, "Russian Coal Exports in the Pacific Rim" — Kemerovo → Vostochny 3.400 mijl (~5.470 km); RZD-investeringsachterstand op de Trans-Sib/BAM; Vostochny 4.000 zeemijl voordeel t.o.v. Noord-Amerikaanse havens. https://www.coalage.com/features/russian-coal-exports-in-the-pacific-rim/
[5] IEA, Coal 2025 — Trade: Rusland 198 Mt kolenexport in 2024, 75 % naar Azië. https://www.iea.org/reports/coal-2025/trade
[6] The Coal Hub, "Vostochny Port to expand its throughput capacity up to 70 mio t" (02-2022) — capaciteit 50 Mt (bereikt 2019), doel ~70 Mt, 2021-doorzet 25 Mt (−7,4 % j/j, spoorbeperkingen als oorzaak). https://thecoalhub.com/vostochny-port-to-expand-its-throughput-capacity-up-to-70-mio-t/
[7] Wikipedia (via MediaWiki API `prop=coordinates`), Vostochny Port — 42.741464,133.079797 (centroïde-vermelding; kade zelf satelliet-gelegd op 42.7555,133.0680, zie §3). https://en.wikipedia.org/wiki/Vostochny_Port
[8] Wikipedia (via MediaWiki API `prop=coordinates`) — Tayshet 55.9500,98.0167 · Chita 52.0500,113.4667 · Khabarovsk 48.4833,135.0833 (via-punten §4, corridorkeuze op de Trans-Sib). https://en.wikipedia.org/wiki/Tayshet · https://en.wikipedia.org/wiki/Chita,_Zabaykalsky_Krai · https://en.wikipedia.org/wiki/Khabarovsk
[9] Sxcoal, "Russian coal freight to China from Vostochny Port hits record" (24-09-2026; kop/datum, volledige tekst achter betaalmuur) — bevestigt doorlopende export Vostochny → China. https://en.sxcoal.com/news/detail/2102948124359675906
[10] Esri World Imagery via `v2/tools/sat_check.py` (z15/z17, live) — `v2/build-cache/satcheck/sat-kolen-taldinsky-vostochny-taldinsky-laadstation.png`, `sat-kolen-taldinsky-vostochny-vostochny-kade.png`.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `kolen-taldinsky-vostochny`** → `v2/data/stroomroute-kolen-taldinsky-vostochny.json` — 5 benen, 5.985,9 km, 2 markers:
spoor (stippel) 9,7 km · spoor 1.069,5 km · spoor 1.667,1 km · spoor 2.323,3 km · spoor 916,3 km.
Recept: `bak_stromen.sh` (functie `bak_kolen_taldinsky_vostochny`).

**Toelichting.** Vier opeenvolgende Trans-Sib-etappes, elk apart geroutet onder `BAKE_SUFFIX=-raw` (het
1-op-1-spoornet, 3.260.717 spoor-edges — console bevestigde dat bij elke run): Taldinsky → Taishet 1.069,5 km
(brief 1.067,5, **+0,2%**) · Taishet → Chita 1.667,1 km (1.652,9, **+0,86%**) · Chita → Khabarovsk 2.323,3 km
(2.305,9, **+0,75%**) · Khabarovsk → Vostochny-laadkade 916,3 km (904,8, **+1,27%**). Totaal 5.985,9 km tegen
Coal Age's ~5.470 km (Kemerovo → Vostochny, 3.400 mijl) = **+9,4%**, ruim binnen de ±15%-norm en dicht bij de
brief-schatting van +8,4%. De drie verplichte via-punten (Taishet, Chita, Khabarovsk) pinden de route op de
Trans-Sib zelf; zónder Chita geeft een vrije Dijkstra op hetzelfde net **4.917,2 km met een omkering in
Harbin** (bewaard als diagnose in `v2/build-cache/ais/graaf/spoorroute-diag-kolen-taldinsky-vostochny.geojson`,
geen onderdeel van deze bake) — de Chinese Oost-spoorweg via Zabaikalsk–Manzhouli–Harbin–Suifenhe, want het
1-op-1-net bewaakt geen spoorwijdte.

**Kop-stippel (b1, 9,7 km).** Het GEM-putpunt van Taldinsky (54,1772/87,1906) ligt in de dagbouwput zelf; de
mijn-eigen railaansluiting op de Erunakovo-tak/het emplacement ontbreekt in OSM. De router snapt 9,72 km
verderop op het hoofdnet (54,1140/87,0875) — rechte stippel ertussen, geen doorgetrokken lijn de put in, exact
zoals brief §7 voorspelde.

**Geen zeebeen.** Zoals brief §6/§7 voorschrijft: geen bron noemt een specifieke Aziatische loshaven, dus de
keten stopt op de Vostochny-laadkade; het bestemmingstype (Japan/Korea/China/Taiwan/India/Nederland, GEM) staat
alleen in de marker-naam, er is geen lijn getekend.

**Gereedschapslessen.**
- `toets_knikken.py` markeert bij b4 (Khabarovsk → Vostochny) één 180°-omkering op 48,49890/135,06490 als
  **TERUGLOOP** (v≈99, boogstraal ~0 m) — dus géén legitieme kopmaak-plek maar een lokale heen-en-weer-zigzag in
  het 1-op-1-net op die precieze coördinaat. De spoorrouter zelf noemde hem neutraler ("OMKERING — alleen echt
  als hier kopgemaakt wordt"); de knikken-toets geeft het scherpere oordeel. Bevinding, niet dichtgetrokken
  (buiten de scope van deze lichte bake — geen shotgun-fix op andermans netgeometrie).
- Bestandsgrootte 355,5 KB ligt boven de indicatieve ~300 KB uit de handleiding — een gevolg van de volle
  1-op-1-spoorgranulariteit over 5.986 km (19.079 punten) zonder simplify; zelfde orde als andere reeds gebakken
  spoor-/kobaltstromen in `v2/data/` (312–688 KB). Bevinding, geen actie.
- Marker-namen met een liggend streepje (—) komen in het geschreven json corrupt terug (`�`) — een bestaand,
  breder pijplijnprobleem in `hecht_marnet.py`'s tekstencoding (ook zichtbaar in eerder gebakken stromen zoals
  `koper-elteniente-rotterdam.json`), niet iets dat deze bake heeft veroorzaakt en niet hier gerepareerd
  (gedeeld gereedschap, buiten scope van één stroom-bake).
- De satelliet-checks voor beide §3-ankers stonden al klaar in `v2/build-cache/satcheck/` (door de briefschrijver
  gemaakt) — geen nieuwe `sat_check.py`-aanroep nodig.

**Open (uit §7, onveranderd door het bakken):** Taldinsky-laadstation blijft ongelegd (het emplacementgat is nu
zichtbaar als de b1-stippel) · geen Aziatische loshaven · Taldinsky-jaarproductie en het KRU-aandeel in de
Vostochny-doorzet blijven ongekwantificeerd · RZD-vervoersquota maken het jaarvolume volatiel, niet in deze
geometrie gevangen.
