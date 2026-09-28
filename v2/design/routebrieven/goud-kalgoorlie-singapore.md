# Routebrief (licht) · goud — Kalgoorlie → Perth → Singapore

**stroom-id:** `goud-kalgoorlie-singapore` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) · **status:** gebakken
**Keten in één zin:** ruwe mijnproductie van de Kalgoorlie Super Pit (KCGM/Northern Star) gaat per **truck** over de Great Eastern Highway naar de **Perth Mint**-raffinage in East Perth, de LBMA-good-delivery-baren rijden per **truck** naar de vrachtterminal van Perth Airport (PER), vliegen als **vrachtvlucht** (grootcirkel) naar de Changi Airfreight Centre in Singapore (SIN), en gaan per **truck** naar het bullion-handelsgebouw GoldSilver Central (International Plaza, Anson Road) — een van de gevestigde Aziatische kluis-/handelsplekken naast Shanghai en Hongkong.
**Welke as van het verhaal:** *Australische downstreaming naar Azië* — vrijwel alle West-Australische mijnproductie wordt bij de eigen LBMA-erkende Perth Mint geraffineerd (geen concentraat-export zoals bij koper); de baren vliegen vervolgens als luchtvracht naar Aziatische bullion-hubs. Deze as kiest Singapore als illustratieve bestemming; Perth Mint's exportverdeling over Singapore/Shanghai/Hongkong is niet per bestemming gepubliceerd (expliciet risico, zie §7).

## BINDENDE aanpassing op het ketenontwerp (haalbaarheidstoets)
De haalbaarheidstoets (orchestrator, BINDEND) meldt: **been C (Changi-vrachtterminal → kluis-/handelszone Singapore, ~20 km) kan met het huidige gereedschap NIET gebakken worden** — er is géén `singapore`-Geofabrik-extract lokaal aanwezig (`ls v2/build-cache/geofabrik/` geeft alleen `maleisie-latest.osm.pbf`, bevestigd opnieuw bij het schrijven van deze brief). Dit is **centraal werk** (bakhandleiding §3: "een ontbrekende extract is centraal werk"), geen taak voor de bak-agent. Tot de extract gedownload is blijft b4 een **stippel** ("geen net op deze korrel" — de weg bestaat fysiek wél, alleen de lokale kaartdata ontbreekt); zie §2/§7/bak-aanwijzingen voor het klaarliggende wegprofiel zodra de extract er is.

## 1 · Ketenkaart
```
Kalgoorlie Super Pit / Fimiston-mill `au-kalgoorlie-mill` ──(b1 truck · Great Eastern Highway · 590 km gepubliceerd)──►
Perth Mint, East Perth `au-ref-perth`
   ═══ knoop: Perth Mint-raffinage (erts/doré → LBMA good-delivery-baren, ~300-400 t Au/j) ═══
   ──(b2 truck · binnenstedelijk Perth, Great Eastern Hwy → Tonkin Hwy · ~10 km)──►
Perth Airport (PER), vrachtterminal `au-per-cargo`
   ──(b3 lucht · vrachtvlucht PER → SIN, grootcirkel · ~3.915 km, DOORGETROKKEN)──►
Singapore Changi (SIN), vrachtterminal `au-sin-cargo`
   ──(b4 truck · East Coast Parkway → Shenton Way · ~20 km, STIPPEL: ontbrekende extract, zie hierboven)──►
GoldSilver Central, International Plaza (Anson Road) `au-sin-vault` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Kalgoorlie Super Pit (Fimiston-mill) → Perth Mint | Great Eastern Highway | 590 gepubliceerd [10]; hemelsbreed 549,8 berekend (ratio 1,07) | maak_stroombeen_weg | nee |
| b2 | A | truck | Perth Mint → Perth Airport (PER), vrachtterminal | binnenstedelijk Perth, Great Eastern Highway → Tonkin Highway | hemelsbreed 10,1 berekend; ontwerp ≈12 [1] | maak_stroombeen_weg | nee |
| b3 | B | lucht | Perth (PER) vrachtterminal → Singapore Changi (SIN) vrachtterminal | vrachtvlucht PER → SIN, grootcirkel | 3.914,5 berekend (grootcirkel); ontwerp ≈3.910 [1] | maak_luchtbeen | nee — doorgetrokken |
| b4 | C | truck | Changi (SIN) vrachtterminal → GoldSilver Central (International Plaza, Anson Road) | East Coast Parkway (ECP) → Nicoll Highway → Shenton Way | hemelsbreed 20,3 berekend; ontwerp ≈20 [1] (bijna exacte match) | maak_stroombeen_weg — **kan nu niet gebakken worden**, zie BINDENDE aanpassing | **ja, tot de `singapore`-extract gedownload is** — "geen net op deze korrel" (centraal werk); via-punten hieronder liggen al klaar voor zodra dat wel kan |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-kalgoorlie-mill` | mijn / mill (kop van b1) | Kalgoorlie Super Pit / KCGM Fimiston-mill-complex, Boulder | -30.7897, 121.4990 | [3][13][14] | bron-gelegd (**hergebruikt** uit de goud-sitelaag-ronde van deze golf, z14 gezien: gebouwencluster direct aan de rand van de open pit, tussen stad en put — `sat-sitelaag-goud-kalgoorlie.png`) |
| `au-ref-perth` | raffinaderij (verwerkingsknoop) | The Perth Mint, 310 Hay Street, East Perth | -31.9550, 115.8700 | [6][7][13][14] | bron-gelegd (**hergebruikt** uit `data/goud.js` v1 (`au-ref-perth`) + de sitelaag-ronde van deze golf, z15 gezien: het karakteristieke koepelgebouw + kantoorcomplex in East Perth — `sat-sitelaag-goud-ref-perth.png`) |
| `au-per-cargo` | vrachtterminal / vertrek luchtvracht | Qantas Freight International Terminal, Affleck Road, Ascot (Perth Airport-terrein) | -31.9460, 115.9764 | [8][9][13] | bron-gelegd (**eigen satcheck deze sessie**, z17 gezien: loods-/kantoorcomplex direct naast de apron van de internationale terminal, met breedrompvliegtuigen aan de gates op ~150 m — `sat-goud-kalgoorlie-singapore-per-affleck.png`; geen "Cargo"-naam-tag in OSM gevonden op dit punt, zie §7) |
| `au-sin-cargo` | vrachtterminal / aankomst luchtvracht | Changi Airfreight Centre / SATS Airfreight Terminal, Singapore Changi Airport | 1.37753, 103.9976 | [11][12][13] | bron-gelegd (**eigen satcheck deze sessie**, z17 gezien: vrachtloodsen + brandstoftanks + meerdere brede-romp vrachttoestellen op het platform, OSM-landuse "Changi Airfreight Centre" — `sat-goud-kalgoorlie-singapore-sin-cargo.png`) |
| `au-sin-vault` | kluis-/handelsgebouw (bestemming) | GoldSilver Central, #23-16 International Plaza, 10 Anson Road | 1.275755, 103.8459 | [11][16] | bron-gelegd (**eigen satcheck deze sessie**, z17 gezien: kantoortoren in het Tanjong Pagar/Anson Road-zakendistrict, adres via OSM "International Plaza" — `sat-goud-kalgoorlie-singapore-goldsilvercentral.png`; het exacte GoldSilver Central-adres is algemeen bekend maar niet apart met een bedrijfseigen bron bevestigd binnen het webbudget, zie §7) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Coolgardie | -30.9530, 121.1640 | eerste stad op de Great Eastern Highway, hier buigt de corridor van Kalgoorlie af naar het westen [10] |
| b1 | 2 | Southern Cross | -31.2306, 119.3278 | doorgaande corridorstad, geen zijtak [10] |
| b1 | 3 | Merredin | -31.4820, 118.2790 | regionale hub op de corridor, kruising met de Merredin-Narembeen-route [10] |
| b1 | 4 | Cunderdin | -31.6600, 117.2400 | doorgaande corridorstad in de Wheatbelt [10] |
| b1 | 5 | Northam | -31.6531, 116.6661 | hier voegt de Great Southern Highway aan en buigt de corridor de Avon-vallei in [10] |
| b1 | 6 | Midland | -31.8880, 116.0100 | rand van de Perth-agglomeratie; hier gaat de corridor over in stedelijke wegen richting East Perth [10] |
| b4 | 1 | Bedok | 1.3241, 103.9284 | East Coast Parkway passeert hier, eerste herkenbare punt na de luchthaven [11] |
| b4 | 2 | Marine Parade | 1.3001, 103.8962 | ECP blijft de kustlijn volgen; geen zijtak richting het binnenland [11] |
| b4 | 3 | Nicoll Highway | 1.2959, 103.8577 | hier buigt de corridor van de ECP het stadscentrum in, richting de Marina/CBD [11] |
| b4 | 4 | Shenton Way | 1.2787, 103.8493 | laatste corridorpunt vóór Anson Road/International Plaza, in het financiële district [11] |

b2 heeft geen via-punten: <15 km binnen Perth, met de Great Eastern Highway → Tonkin Highway als enige voor de hand liggende corridor tussen Perth Mint en de luchthaven — geen aanwijsbare keuze tussen alternatieve routes.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Perth Mint-raffinage | The Perth Mint (West-Australische overheid) | mijnerts/doré → LBMA good-delivery-baren (400 oz) | totale doorvoer ~300-400 t Au/jaar (LBMA-erkend, ook aanvoer uit PNG/NZ/Maleisië/Thailand/Fiji); waarvan 225,4 t specifiek voor mijnbouwklanten (FY2024-25) | [7] |

## 6 · Stoppunt
De brief stopt bij GoldSilver Central: het eindproduct (de LBMA good-delivery-baar) is al bij de Perth Mint gemaakt, en GoldSilver Central is een handels-/opslagpunt (fysieke bullion-dealer met eigen kluis), geen verdere bewerking — fase D/E vervalt.

## 7 · Open punten
- **BINDEND (haalbaarheidstoets): b4 kan niet gebakken worden zonder de `singapore`-Geofabrik-extract** — centraal werk, zie de aanpassing hierboven. De via-punten in §4 liggen al klaar voor een `maak_stroombeen_weg.py`-profiel zodra de extract gedownload is.
- **Ankerkeuze b4 heroverwogen tijdens het schrijven:** Le Freeport (Changi North Crescent, 1.3449/103.9713 — ook genoemd als bron voor luchtvracht in het ketenontwerp) ligt maar 4,7 km van de Changi-vrachtterminal, ver onder de ~20 km uit het ketenontwerp. GoldSilver Central (International Plaza) ligt op 20,3 km — een bijna exacte match met de ontwerpschatting — en is daarom als primair anker gekozen. Le Freeport blijft een plausibel alternatief anker voor een latere correctie.
- **`au-per-cargo` (Qantas Freight International Terminal) heeft geen "Cargo"-naam-tag in OSM** op de satellietpas van deze sessie; het adres (24 Affleck Road, Ascot) komt uit Qantas Freight's eigen website [9], en het gebouw ligt zichtbaar naast de internationale-terminal-apron, maar er is geen bron die specifiek bevestigt dat Perth Mint-baren via déze terminal (i.p.v. bv. dnata) worden verzonden.
- **Geen bron voor een tussenlanding** op b3 — conform bakhandleiding §2 daarom één rechtstreekse vlucht PER→SIN aangenomen; in de praktijk lopen vrachtcombinaties soms via Melbourne, Sydney of een Golf-hub, maar dat is voor déze stroom niet gebrond.
- **Perth Mint's exportverdeling over Singapore/Shanghai/Hongkong is niet per bestemming gepubliceerd** — expliciet risico uit het ketenontwerp én de haalbaarheidstoets; deze as kiest Singapore als illustratieve Aziatische bestemming, een gelijkwaardig alternatief zou Hongkong of Shanghai zijn.
- **GoldSilver Central's exacte adres/coördinaat is algemeen bekend maar niet met een bedrijfseigen bron (website) bevestigd** — het webbudget van deze sessie (max 3 WebSearch) ging naar Perth Mint-volumes en Super Pit-productie; het OSM/Esri-anker (International Plaza) is wel zelf satelliet-gelegd.
- **Jaarvolume specifiek voor déze as** (Kalgoorlie → Perth → Singapore) is niet apart gepubliceerd — alleen de totale Kalgoorlie- en Perth Mint-cijfers zijn gebrond (§8/volumes).

## 8 · Bronnen
[1] Ketenontwerp (JSON, orchestrator-invoer, M31 golf 3) — `goud-kalgoorlie-singapore`, benen A–C met km-indicaties, bronnen_start.
[2] Haalbaarheidstoets (JSON, orchestrator-invoer, BINDEND) — ontbrekende `singapore`-Geofabrik-extract blokkeert been C; aanpassing = centraal werk vóór bakken.
[3] Wikipedia — "Super Pit gold mine" (KCGM, Kalgoorlie, -30.7747/121.5094). https://en.wikipedia.org/wiki/Super_Pit_gold_mine
[4] The Northern Miner, 2024/2025 — KCGM/Super Pit-productie 437.000 oz in het boekjaar tot 30-06-2024; uitbreidingsplan naar 900.000 oz/jaar tegen 2028-29 na de Fimiston Mill-rebuild. https://northernminer.com/news/site-visit-northern-star-to-boost-super-pit-gold-output-to-900000-oz-per-year/1003870807/
[5] Northern Star Resources — KCGM Operations (eigen opgave). https://www.nsrltd.com/our-assets/kcgm-operations/
[6] Wikipedia — "Perth Mint" (-31.9573/115.8692, 310 Hay Street East Perth). https://en.wikipedia.org/wiki/Perth_Mint
[7] The Perth Mint — Gold and silver refinery: LBMA-accreditatie, totale doorvoer 300-400 t Au/jaar (incl. PNG/NZ/Maleisië/Thailand/Fiji), 225,4 t voor mijnbouwklanten FY2024-25, raffinaderij nabij Perth Airport (faciliteert luchtvrachtexport). https://www.perthmint.com/refinery-treasury/refinery/
[8] Wikipedia — "Perth Airport" (-31.94/115.965). https://en.wikipedia.org/wiki/Perth_Airport
[9] Qantas Freight — International freight handling, Perth: Qantas Freight International Terminal, 24 Affleck Road, Ascot. https://freight.qantas.com/au-en/freight-terminals/australia/international/international-handling-perth.html
[10] Wikipedia — "Great Eastern Highway": 590 km-verbinding Perth–Kalgoorlie via Coolgardie, Southern Cross, Merredin, Cunderdin, Northam, Midland. https://en.wikipedia.org/wiki/Great_Eastern_Highway
[11] OpenStreetMap (ODbL) via Photon/Nominatim — Changi Airfreight Centre (landuse=industrial, 103.9976/1.37753), SATS Airfreight Terminals 1-4 (103.9940/1.37445), Le Freeport (shop=storage_rental, Changi North Crescent, 103.9713/1.3449), International Plaza (10 Anson Road, 103.8459/1.27576), dnata Catering nabij Perth Airport (115.9584/-31.9256), Great Eastern Highway-corridorpunten, Singapore ECP-corridorpunten Bedok/Marine Parade/Nicoll Highway/Shenton Way. https://www.openstreetmap.org
[12] Wikipedia — "Changi Airport" (1.35917/103.98944). https://en.wikipedia.org/wiki/Changi_Airport
[13] Esri World Imagery via `v2/tools/sat_check.py` (z14–z17, live) — hergebruikt: `sat-sitelaag-goud-kalgoorlie.png`, `sat-sitelaag-goud-ref-perth.png` (goud-sitelaag-ronde, deze golf); eigen (deze sessie): `sat-goud-kalgoorlie-singapore-per-overview.png`, `-per-t1zoom.png`, `-per-affleck.png`, `-sin-cargo.png`, `-lefreeport.png`, `-goldsilvercentral.png` in `v2/build-cache/satcheck/`.
[14] `data/goud.js` (v1-checklist) — `au-kalgoorlie` (-30.78/121.50), `au-ref-perth` (-31.955/115.87), `au-air-per` (-31.94/115.97), `au-hub-singapore` (1.29/103.85); geraadpleegd voor anker-continuïteit, niet als ankerbron zelf (v1-centroïdes zijn geen ankers, zie routebrief-licht.md §1).
[15] `design/goud.md` — ontwerp-skelet: Perth Mint als Australische raffinagehub ("raffineert vrijwel alle Australische productie"), Singapore als Aziatische kluis-/handelshub.
[16] GoldSilver Central — algemeen bekend vestigingsadres #23-16 International Plaza, 10 Anson Road, Singapore (bullion-dealer); niet apart met een WebFetch van de eigen website bevestigd binnen het webbudget van deze sessie, zie §7.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom:** `goud-kalgoorlie-singapore` · **bestand:** `v2/data/stroomroute-goud-kalgoorlie-singapore.json` (91,7 KB gebakken / 93,9 KB op schijf) · **recept:** `bak_goud_kalgoorlie_singapore()` in `v2/tools/bak_stromen.sh` (draaien: `bash v2/tools/bak_stromen.sh goud-kalgoorlie-singapore`).

| # | modaliteit | km | punten | naad met vorige been |
|---|---|---|---|---|
| b1 | truck | 593,8 | 3.617 | — (eerste been) |
| b2 | truck | 14,9 | 457 | 0,0 km |
| b3 | lucht | 3.914,5 | 158 | 0,0 km |
| b4 | truck (stippel) | 20,3 | 2 | 0,0 km |
| **totaal** | | **4.543,5 km** | **4.234 punten** | |

**Markers:** 5 — alle op ≤ 0,1 m van hun been (`au-kalgoorlie-mill`, `au-ref-perth`, `au-per-cargo`, `au-sin-cargo`, `au-sin-vault`).

**Per been:**
- **b1** (Kalgoorlie Super Pit → Perth Mint, Great Eastern Highway, `maak_stroombeen_weg.py`): 593,8 km tegen 590 km gepubliceerd (Wikipedia) = **+0,6% [OK, ruim binnen ±15%]**. 35 keerlussen gesnoeid (595,7 → 593,7 km voor de gesnoeide lijn; het getekende been incl. anker-aansluitingen komt op 593,8 km).
- **b2** (Perth Mint → PER-vrachtterminal, binnenstedelijk Perth, `maak_stroombeen_weg.py`): 14,9 km tegen ~12 km ontwerp-schatting = **+23,5% [buiten ±15% — bevinding, niet dichtgetrokken]**. De 12 km was een hemelsbreed-afgeleide ontwerpschatting (brief §2/§8[1]), geen gepubliceerde wegbeheerder-lengte; 14,9 km is de gemeten route over Great Eastern Highway → Tonkin Highway inclusief de stedelijke bochten bij Ascot. Geen via-punt bijgeschoven om het getal te halen.
- **b3** (PER-vrachtterminal → SIN-vrachtterminal, `maak_luchtbeen.py`, grootcirkel): 3.914,5 km, exact gelijk aan het ontwerpcijfer (~3.910 km) en de brief-schatting (3.914,5 km berekend). **Doorgetrokken, geen stippel** — geen tussenlanding gebrond (brief §7), één rechtstreekse vlucht PER→SIN aangenomen conform bakhandleiding §2. Eerste luchtbeen van deze sessie dat exact op de vooraf berekende grootcirkel-lengte uitkomt (geen km-toets nodig voor een luchtbeen — km = grootcirkel per constructie).
- **b4** (Changi-vrachtterminal → GoldSilver Central, ~20 km): **STIPPEL, GEEN wegscan** — de `singapore`-Geofabrik-extract ontbreekt lokaal (`v2/build-cache/geofabrik/` heeft alleen `maleisie-latest.osm.pbf`), bevestigd bij het schrijven van de brief én opnieuw bij het bakken. Dit is centraal werk (bakhandleiding §3), geen taak voor deze bak-agent. Getekend als rechte stippellijn Changi (1,37753/103,9976) → GoldSilver Central (1,275755/103,8459), 20,3 km — reden "geen net op deze korrel". De via-punten (Bedok/Marine Parade/Nicoll Highway/Shenton Way, brief §4) liggen al klaar in de brief voor zodra de extract gedownload is: dan is het een `maak_stroombeen_weg.py`-profiel als elk ander wegbeen, geen nieuwe brief nodig.

**Toets (STAP 3):** naden alle 0,00 km · `toets_knikken.py`: 49 knikken ≥60° (allemaal kleine-straal wegbochten "spike", geen enkele omkering ≥150°, geen terugloop) · `toets_rechte_benen.py --min-km 5`: b4 komt terecht op de lijst (omwegfactor 1,000 — verwacht, is een rechte stippel met reden) · `json.load` slaagt, `versie: 2`, `punt_formaat: lonlat`, modaliteiten `{truck, lucht}` ⊂ toegestane set, elk been ≥2 punten, bestandsgrootte 93,9 KB (ruim onder ~300 KB) · markers alle ≤0,1 m van hun lijn.

**Gereedschapslessen:**
- Dit is de eerste bake in deze golf die §2 "Lucht" van de bakhandleiding letterlijk volgt met `maak_luchtbeen.py` als apart, licht tool (geen slot nodig, milliseconden) vóór de zware wegscans en de bake zelf — de volgorde uit STAP 1 (lucht → weg → bake) werkte zonder wrijving.
- De ontwerp-km "~12" voor b2 bleek een zachte hemelsbreed-schatting, geen harde bron; de ±15%-norm hoort dan tegen die zachtheid gelezen te worden — het is een reële bevinding (23,5%) maar geen teken dat de route fout ligt (de weg volgt gewoon de enige beschikbare Great Eastern Hwy → Tonkin Hwy-corridor door de luchthavenomgeving).
- b4 bevestigt de regel uit de bakhandleiding dat een ontbrekende extract nooit lokaal gedownload wordt door de bak-agent: de brief had de via-punten al klaarstaan, dus het enige werk voor een latere centrale download-ronde is de extract zelf plus één `maak_stroombeen_weg.py`-run met het al bestaande brief-recept.
