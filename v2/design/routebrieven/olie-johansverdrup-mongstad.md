# Routebrief (licht) · olie — Johan Sverdrup-veld (Noordzee) → Mongstad-terminal (Noorwegen)

**stroom-id:** `olie-johansverdrup-mongstad` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 8) ·
**status:** gebakken
**Keten in één zin:** Stabiele ruwe olie van het Johan Sverdrup-veldcentrum (Utsira High, centrale Noordzee) gaat per
**subsea-leiding** (36 inch, Equinor, 283 km gepubliceerd, door de Fensfjord) rechtstreeks naar de ondergrondse
ruwe-olieopslag en exportterminal van Mongstad bij Bergen; daar eindigt het bewijs.
**Welke as van het verhaal:** *Noorwegen als niet-Russische Europese levenslijn* — één veld levert ruwweg een derde van
de Noorse olie; plateau **755 kb/d** (mei 2023, Wikipedia [1]; Equinor spreekt van 755.000 boe/d [3]), dalend sinds begin
2025 (Wikipedia-infobox 2025: 700 kb/d [1]). Peiljaar 2023 (plateau). De eerder afgewezen as (golf 2) bleek OSM-technisch
wél tekenbaar: de leiding staat als doorlopende way in OSM [8].

## 1 · Ketenkaart
```
Johan Sverdrup-veldcentrum `ol-js-veld` (riserplatform, offshore, 58.8373/2.5561)
   ──(b1 leiding · Johan Sverdrup oil transport, 36", Fensfjord · OSM 281,1 km / gepubliceerd 283 · doorgetrokken)──►
Mongstad-ruweolieterminal `ol-mongstad-term` (Equinor, ondergrondse opslag 9,5 mln vaten) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A/B | leiding | veldcentrum → Mongstad-terminal | Johan Sverdrup-exportleiding (Equinor), subsea, diepste punt 537 m, via Fensfjord | 283 [4] (OSM-way 281,1 km = −0,7%) [8] | één OSM-way (`man_made=pipeline`, `substance=oil`, `location=underwater`, naam "Johan Sverdrup oil transport", way 685329866 volgens de ontwerptoets); geen stikken nodig; script `maak_leidingbeen_olie_johansverdrup_mongstad.py` leest hem uit de noorwegen-extract (211 punten, 281,1 km, begin 0,002 en eind 0,005 km van de ankers) | nee — de way loopt van riserplatform tot terminal |

Geen zeebeen, geen afnemer, geen last-mile: de enige schakel is de leiding. De gasleiding van het veld (156 km, 18", naar
Statpipe/Kårstø [5]) is een andere stroom en bewust niet getekend.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ol-js-veld` | kop: veldcentrum / riserplatform (offshore) | Johan Sverdrup-veldcentrum (P1/DP/RP/LQ, plus P2) | 58.8373, 2.5561 | [4][6][8] | aannemelijk (één bron + consistentiecheck; offshore niet satelliet-toetsbaar: Esri heeft daar "Map data not yet available", `sat-olie-johansverdrup-mongstad-veld.png`) |
| `ol-mongstad-term` | overslag leiding → opslag/tanker (stoppunt) | Mongstad-ruweolieterminal (Equinor), noordpunt van het complex | 60.8184, 5.0232 | [2][8][9] | bron-gelegd (z15 gezien: tankparken en procesinstallaties met twee afgemeerde olietankers aan de kade en een steiger naar het noordwesten; kruis ligt op het terrein tussen kade en tankparken) |

*Ankerkeuze.* OSM-beginpunt van de leiding (58.8373/2.5561) tegen Wikipedia-veldcoördinaat (59°13′N 2°29′E = 59.22/2.49) [1]:
40 km verschil. De OSM-ligging wint: de veldpagina van de Noorse overheid zegt "65 km noordoost van Sleipner" [6]; Sleipner ligt
op 58.36/1.91 [7] en het OSM-begin ligt op **64,9 km, peiling 35° (NO)** van Sleipner, de Wikipedia-coördinaat op 101 km. Equinor
meldt dat de laatste pijp "naast het riserplatform" bij het veld ligt [4], dus het leidingbegin is het veldcentrum. Wikipedia-eind
Mongstad (60.8113/5.0330) ligt 0,95 km zuidoostelijker in het raffinaderijdeel (distillatie-eenheden, z15 gezien); het OSM-leidingeind ligt
op de ruweolieterminal zelf en wordt gekozen. De terminal heeft ondergrondse rotskamers (9,5 mln vaten) [2][6]; de tankparken boven
de grond op het beeld zijn aanvullend/product.

## 4 · Via-punten
Niet van toepassing: leidingbeen uit één OSM-way, geen corridorkeuze (zeebodem, geen alternatief).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Johan Sverdrup-veldcentrum | Equinor (42,63%, operator), Aker BP (31,57%), Petoro (17,36%), TotalEnergies (8,44%) | brongas/olie → stabiele ruwe olie via leiding; gas via aparte leiding | fase 1 440 kb/d + fase 2 220 kb/d = 660 kb/d oliebasis-ontwerp; plateau 755 kb/d (boe/d) | [1][3][5] |
| Mongstad-ruweolieterminal + raffinaderij | Equinor (Mongstad Refining 100% sinds 2012) | ruwe olie → ondergrondse opslag → tanker of raffinaderij | opslag 9,5 mln vaten; raffinaderij 12 Mt/j ≈ **230 kb/d** | [2][6] |

## 6 · Stoppunt
De brief stopt op de Mongstad-terminal: de bron noemt alleen "geëxporteerd en geraffineerd bij Mongstad" [1][2], zonder dat één bron
een lading van Johan Sverdrup aan een bestemming of afnemer koppelt (en een deel van de olie wordt in Mongstad zelf geraffineerd).
Geen zeebeen: een bestemming verzinnen is verboden; dit is een bewust dunne, eenbenige reserve-keten.

## 7 · Open punten
- **Veldcoördinaat blijft aannemelijk, één bron:** OSM-begin plus de Sleipner-afstand uit de overheidspagina; platformen zijn offshore niet met
  satelliet te zien. Wikipedia 59.22/2.49 (40 km noordelijker) is waarschijnlijk de Avaldsnes-vondst van Aker BP en wordt niet gebruikt.
- **Gepubliceerde lengte 283 km** staat in de Equinor-nieuwsbrief van 10-09-2018 [4] (leidinglegging); niet apart in een jaarverslag teruggevonden.
- **Actuele 2025/2026-productie niet gevonden:** Wikipedia noemt 700 kb/d als infoboxcijfer voor 2025 en een daling vanaf begin 2025; het
  veld-cijfer is boe/d (incl. gas), de oliestroom door de leiding ligt lager (ontwerp 660 kb/d, OGJ 2018 [5]).
- **Geen afnemer na Mongstad:** een tanker- of raffinaderij-vervolg (Noord-Europa/Azië) heeft geen bron in deze ronde.
- **Zeeknoop Mongstad** (MARNET-knoop 6874, 60.8543/4.7049) ligt 17,7 km van de terminal: pas relevant zodra er een zeebeen komt (dan haven-aanloop, > 5 km).
- OSM-way-id 685329866 komt uit de haalbaarheidstoets; het script vindt de way via naam + substance (1 way) en is niet op het id gefilterd.

## 8 · Bronnen
[1] Wikipedia, "Johan Sverdrup oil field" — plateau 755.000 b/d mei 2023, daling vanaf begin 2025, olie per leiding naar Mongstad, partners, HVDC-stroom van de wal, coördinaat 59°13′N 2°29′E. https://en.wikipedia.org/wiki/Johan_Sverdrup_oil_field
[2] Wikipedia, "Mongstad" — 60°48′41″N 5°01′59″E, ruweolieterminal Equinor 9,5 mln vaten, raffinaderij 12 Mt/j ≈ 230 kb/d, Equinor sinds 2012. https://en.wikipedia.org/wiki/Mongstad
[3] Equinor, "Johan Sverdrup" — partneraandelen (42,6267/31,5733/17,36/8,44%), plateau 755.000 boe/d, ongeveer een derde van de Noorse olie. https://www.equinor.com/energy/johan-sverdrup
[4] Equinor, "Norway's largest oil pipeline now in place" (10-09-2018) — 283 km, 36 inch, Saipem Castorone, begin Mongstad-terminal / einde riserplatform bij het veld, 537 m diepste punt. https://www.equinor.com/news/archive/10sep2018-norways-largest-oil-pipeline
[5] Oil & Gas Journal, "Equinor completes Johan Sverdrup offshore crude pipeline installation" (2018) — 660 kb/d piekcapaciteit in de leiding, gasleiding 156 km/18 inch naar Statpipe/Kårstø (zoekresultaat-samenvatting, pagina niet geopend). https://www.ogj.com/pipelines-transportation/pipelines/article/17296386/equinor-completes-johan-sverdrup-offshore-crude-pipeline-installation
[6] Norwegian Offshore Directorate / norskpetroleum.no, factpagina Johan Sverdrup — Utsira High, 65 km noordoost van Sleipner, 115 m waterdiepte, ontdekt 2010, olie per nieuwe leiding naar bestaande ondergrondse opslagrotsen van Mongstad. https://www.norskpetroleum.no/en/facts/field/johan-sverdrup/
[7] Wikipedia, "Sleipner gas field" — 58°22′N 1°55′E (58.36/1.91), referentie voor de afstandscontrole. https://en.wikipedia.org/wiki/Sleipner_gas_field
[8] OpenStreetMap (ODbL), eigen PBF-scan 2026-10-09 van `noorwegen-latest.osm.pbf`: 1 way `man_made=pipeline` + `substance=oil` + naam "Johan Sverdrup"; kortste pad 281,1 km, 211 punten, begin 58.83731/2.55612, eind 60.81844/5.02321. https://www.openstreetmap.org
[9] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-olie-johansverdrup-mongstad-leidingeinde.png` (z15), `-wikipedia.png` (z15, Wikipedia-eindpunt), `-terminal-z14.png`, `-veld.png` (geen beeld offshore).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 8)
**Bestand:** `v2/data/stroomroute-olie-johansverdrup-mongstad.json` (4,7 KB, contract versie 2, lonlat) · **1 been · 281,1 km · 211 punten · 2 markers.**

| # | modaliteit | van → naar | km gemeten | km brief | afwijking | doorgetrokken/stippel |
|---|---|---|---|---|---|---|
| b1 | leiding | veldcentrum (58.8373, 2.5561) → Mongstad-terminal (60.8184, 5.0232) | 281,1 | 283 (Equinor 2018) | -0,7% | doorgetrokken (OSM-way) |

Naad: n.v.t. (één been). Markers: `ol-js-veld` 0,002 km en `ol-mongstad-term` 0,004 km van de lijn. `toets_knikken.py`: 0 knikken, 0 omkeringen. `toets_rechte_benen.py --min-km 5`: de stroom komt niet in de lijst (geen recht been, geen stippel). json: versie 2, punt_formaat lonlat, modaliteit {leiding}, bestand 4,7 KB.

**Recept.** `python v2/tools/maak_leidingbeen_olie_johansverdrup_mongstad.py --schrijf` (pure-Python-PBF-lezer op `noorwegen-latest.osm.pbf`, selecteert op naam + substance, 1 way) schrijft `v2/build-cache/ais/graaf/olie-johansverdrup-mongstad-leiding-js.geojson` (FeatureCollection, 281,1 km, 211 punten); daarna `bash v2/tools/bak_stromen.sh olie-johansverdrup-mongstad` (functie `bak_olie_johansverdrup_mongstad`, één `--been-geojson "leiding|…"` plus twee `--marker`). Geen extracts nodig bij de bake zelf, geen zeebeen, geen haven-aanloop, geen stippel, geen kopie, geen lucht.

**Toelichting leiding.** De exportleiding staat in OSM als één doorlopende subsea-way van riserplatform tot Mongstad, dus er is geen stikwerk en geen stippel; de afwijking van -0,7% tegen de gepubliceerde 283 km is de enige lengtetoets en klopt binnen de ±15%-norm. De lijn loopt over zee en door de Fensfjord (offshore), niet over een weg: de bol tekent hem als doorgetrokken leidinglijn.

**Beperkingen (eerlijk).** Het veldanker is aannemelijk (één bron, offshore niet satelliet-toetsbaar); het terminalanker is bron-gelegd. Geen zeebeen en geen afnemer na Mongstad: geen bron koppelt een lading aan een bestemming. Mongstad-zeeknoop 6874 ligt 17,7 km van de terminal, dus bij een eventueel latere zeeketen is een haven-aanloop nodig.

**Lessen.** (1) Een leidingbeen uit één OSM-way is in minuten klaar zodra de PBF-lezer de way op naam + substance vindt; het way-id uit de haalbaarheidstoets hoeft niet in het script. (2) Een kale Feature geeft `KeyError: 'features'`: het script schrijft een FeatureCollection. (3) Heb de functie met backslash-vervolgregels, niet op één lange regel, zodat hij leesbaar blijft naast de andere functies.
