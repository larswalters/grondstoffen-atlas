# Routebrief (licht) · Grafiet · Siviour → Bolivar → Port Adelaide (Australië)

**stroom-id:** `grafiet-siviour-portadelaide` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 11) ·
**status:** gebakken
**Keten in één zin:** Grafietconcentraat van de geplande Siviour-mijn en concentrator (Renascor, Eyre Peninsula, Zuid-Australië)
per **truck** over de Lincoln Highway (via Whyalla) en de Augusta/Princes Highway naar de geplande PSG-fabriek op SA Water-terrein in Bolivar
(Adelaide-noord), daarna per truck naar de exporthaven Port Adelaide (Outer Harbor) — stoppunt, geen bestemmingshaven of -fabriek gedocumenteerd.
**Welke as van het verhaal:** *Australische mijn-naar-anode-keten, nog geen productie.* Plan fase 1: 75 kt/j concentraat en 50 kt/j PSG, fase 2 het
dubbele [2]; 0 kt/j vandaag (alleen een PSG-demonstratiefabriek in Adelaide, 2026 [3][9]). Eenheid kt grafiet/jaar, peiljaar plan 2026+.
Afnemers POSCO, Mitsubishi Chemical, Hanwa e.a. zijn niet-bindend [1][2]; Renascor noemt zelf geen afnemershaven.

## 1 · Ketenkaart
```
Siviour-mijn `gr-siviour-mijn` ──(b1 truck · Siviour Rd → Lincoln Hwy B100 → Augusta/Princes Hwy A1 · ~527 km, aannemelijk)──►
Bolivar PSG-site `gr-bolivar-psg` ──(b2 truck · Port Wakefield Rd → Port Rd · ~26 km, aannemelijk)──►
Port Adelaide, Outer Harbor `gr-portadelaide-outerharbor` ── stoppunt (geen zeebeen)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `gr-siviour-mijn` → `gr-bolivar-psg` | Lincoln Hwy B100 (Arno Bay, Cowell, Whyalla, Port Augusta) → Augusta Hwy / Princes Hwy A1 (Port Wakefield) | 526,8 gemeten; bedrijf ca 500 km tot Port Adelaide, dus A+B ca 553 (+10%) [1]; hemelsbreed 220 km, geen wegkm | maak_stroombeen_weg (profiel `…-siviour-bolivar`) | nee |
| b2 | B | truck | `gr-bolivar-psg` → `gr-portadelaide-outerharbor` | Port Wakefield Rd → Port Rd → Lefevre Peninsula (werkaanname) | 25,9 gemeten; bedrijf: site ca 20 km van Port Adelaide [2] (niet Outer Harbor); hemelsbreed 8,4 km, geen wegkm | maak_stroombeen_weg (profiel `…-bolivar-outerharbor`) | nee |

Geen zeebeen: Renascor noemt Port Adelaide als verschepingshaven [2], geen bestemming. Outer Harbor ligt 16,6 km van MARNET-zeeknoop 6042 (> 5 km):
komt er later een zeebeen, dan is een haven-aanloop verplicht. Eén-bron-status staat in de beennaam; beide benen zijn doorgetrokken.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-siviour-mijn` | mijn + concentrator (kop b1) | Siviour Graphite Project, Siviour Rd, Verran (ML 6495, ca 15 km W van Arno Bay) | -33.8907, 136.4367 | [1][4][5][7], sat | aannemelijk (z14 gezien: akkerland en een N-Z gravelweg, geen mijn — niet gebouwd; punt = OSM-naam Siviour Road, past bij "15 km W van Arno Bay") |
| `gr-bolivar-psg` | PSG-fabriek (staart b1 / kop b2) | Bolivar, SA Water-terrein (optie-to-lease Renascor, 40 jr) | -34.7708, 138.5842 | [2][6][8], sat | aannemelijk (z15 gezien: SA Water-afvalwaterzuivering Bolivar met slibtanks, zonnepanelen en bekkens, naast Port Wakefield Rd; het perceel van Renascor is niet aanwijsbaar) |
| `gr-portadelaide-outerharbor` | losplek / stoppunt | Outer Harbor-terminal, Port of Adelaide — hergebruik `u-portadelaide-outerharbor` uit `uranium-olympicdam-portadelaide.md` | -34.7694, 138.4920 | [2] + bron-brief | aannemelijk (niet opnieuw bekeken; daar z15 gezien: containerstapels en kranen; niet als grafiet-berth bevestigd) |

## 4 · Via-punten (alleen b1; b2 heeft geen corridorkeuze die dit verdient)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Cowell — Lincoln Hwy | -33.6760, 136.9150 | pint de Lincoln Hwy-corridor langs de kust (Arno Bay → Cowell) tegenover de Kimba-route |
| b1 | 2 | Whyalla — Lincoln Hwy (Norrie) | -33.0444, 137.5347 | echte corridorkeuze Whyalla (Lincoln Hwy, 182 km Cowell–Port Augusta) tegenover Kimba–Iron Knob (Eyre Hwy, omweg); op de doorgaande weg, niet in het centrum |
| b1 | 3 | Port Augusta — Augusta Hwy × Lincoln Hwy | -32.4925, 137.7663 | hergebruikt via-punt van de uranium-brief; hier begint de Augusta Hwy naar het zuiden |
| b1 | 4 | Port Wakefield — Augusta/Princes Hwy A1 | -34.1936, 138.1497 | hergebruikt via-punt van de uranium-brief; wegnummerwissel op de doorgaande weg richting Adelaide |
Snaps bij de proefbake: 0,03–0,09 km, behalve Port Wakefield 0,74 km. Extract: `australie`.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Siviour-mijn + concentrator | Renascor | erts (7,0% TGC, reserve 61,8 Mt) → grafietconcentraat | 75 kt/j fase 1, 150 kt/j fase 2 (plan, nog niet gebouwd) | [1][2] |
| PSG-fabriek Bolivar | Renascor | concentraat → gezuiverd bolvormig grafiet (PSG) | 50 kt/j fase 1, 100 kt/j fase 2 (plan; demo-fabriek in Adelaide 2026) | [2][3][9] |

## 6 · Stoppunt
De brief stopt bij Port Adelaide, Outer Harbor: Renascor noemt alleen de haven als verschepingspunt en nergens een anodefabriek of afnemershaven
(POSCO, Mitsubishi Chemical en Hanwa zijn niet-bindend en hebben geen adres in de bron). Fase D/E vervallen; bestemming is een open punt, geen zeebeen.

## 7 · Open punten
- **Geen productie.** Mijn niet gebouwd, afnemers niet-bindend; demo-PSG in Adelaide geopend in 2026 [3][9]. De lijn toont de geplande weg, niet een lading.
- **Ankers aannemelijk.** Siviour = OSM-straatnaam bij "15 km W van Arno Bay" (mijnterrein niet te zien); Bolivar = SA Water-terrein zonder perceel; haven-terminal niet bevestigd.
- **Lucky Bay (ca 60 km van de mijn) is de voorkeurshaven**, Port Adelaide de terugval [1]; Lucky Bay is niet getekend (geen bron-coördinaat in dit budget).
- **Truck als modaliteit is aanname.** [1] noemt ca 500 km "weg" naar Port Adelaide; geen bron beschrijft concentraat per spoor of de exacte route (Cleve of Arno Bay).
- **Overlap met `uranium-olympicdam-portadelaide`**: Port Augusta → Outer Harbor (ca 311 km) valt samen, Bolivar ligt 0,9 km van die lijn. Geen letterlijke kopie: dat been loopt vanaf Olympic Dam (581,9 km) en is niet te knippen; de geometrie volgt dezelfde A1-corridor met eigen profielen.
- **Km-toets:** b1 526,8 tegen ca 500 tot Port Adelaide; A+B 552,9 = +10,6% (norm ±15%, de referentie is een afgeronde bedrijfsopgave). b2 25,9 tegen ca 20 "tot Port Adelaide" (niet Outer Harbor): geen norm, indicatie.
- Mijnanker en omweg: de route verlaat Siviour Rd naar het zuiden en pakt de Arno Bay-weg (13,5 km kleine klassen); een kleine start-omkering (176°) op het ankerpunt is een artefact van de ankerprojectie.

## 8 · Bronnen
[1] Mining Technology, "Siviour Graphite Project, South Australia" — 15 km W van Arno Bay, Lucky Bay ca 60 km voorkeur, terugval Port Adelaide ca 500 km, 75 kt/j concentraat; afnemers. https://www.mining-technology.com/projects/siviour-graphite-project-south-australia/
[2] Renascor Resources, Annual Report 2023 (ASX, 2023-09-29) — Bolivar-optie met SA Water (40 jr), site ca 20 km van Port Adelaide, aan het transportcorridor naar Port Adelaide; 75/150 kt/j concentraat, 50/100 kt/j PSG; POSCO en Mitsubishi niet-bindend. https://announcements.asx.com.au/asxpdf/20230929/pdf/05vjh9jd4h0j6h.pdf
[3] Renascor, Quarterly Activities Report (ASX, 2026-01-30) — PSG-demonstratiefabriek in Adelaide in aanbouw; Siviour ML 6495 (16 km²); cash A$97 mln. https://announcements.asx.com.au/asxpdf/20260130/pdf/06vshd3srsq4b2.pdf
[4] Wikipedia, "Arno Bay, South Australia" — coördinaat -33.9167, 136.5833, op de Lincoln Highway. https://en.wikipedia.org/wiki/Arno_Bay,_South_Australia
[5] Wikipedia, "Lincoln Highway, South Australia" — Port Augusta–Port Lincoln, 315 km, B100 via Whyalla, Cowell en Arno Bay. https://en.wikipedia.org/wiki/Lincoln_Highway,_South_Australia
[6] Wikipedia, "Bolivar, South Australia" (-34.775, 138.589) en "Port Wakefield Highway" (A1, Adelaide–Port Augusta). https://en.wikipedia.org/wiki/Bolivar,_South_Australia
[7] OpenStreetMap via Nominatim — Siviour Road, Verran (way 104527081, -33.8907, 136.4368; unclassified). https://nominatim.openstreetmap.org/search?q=Siviour+Road+Verran&format=json
[8] OpenStreetMap via Nominatim — Cowell -33.6842/136.9237, Lincoln Highway Whyalla Norrie -33.0444/137.5347 (trunk). https://nominatim.openstreetmap.org
[9] Quartr, Renascor Q4 2026 — officiële opening PSG-demonstratiefabriek Adelaide, cash A$94 mln (30 jun 2026); AI-samenvatting. https://quartr.com/events/renascor-resources-limited-rnu-q4-2026-tu_F9IEOf9N
[10] Renascor, Annual Report 2024 (ASX, 2024-09-30) — Bolivar-milieutoetsen afgerond, kaart Mine and Concentrator bij Arno Bay en BAM-plant bij Adelaide. https://announcements.asx.com.au/asxpdf/20240930/pdf/068jxvnk5s2h58.pdf
[sat] Esri World Imagery via `v2/tools/sat_check.py` — `v2/build-cache/satcheck/sat-grafiet-siviour-portadelaide-siviour-mijn.png` (z14), `…-bolivar.png` (z15).

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 11)
**Bestand:** `v2/data/stroomroute-grafiet-siviour-portadelaide.json` (76,4 KB, versie 2, punt_formaat lonlat), 2 benen, 3 markers, totaal 552,9 km, naden 0,0 km.
**Recept:** functie `bak_grafiet_siviour_portadelaide()` in `v2/tools/bak_stromen.sh` (`bash v2/tools/bak_stromen.sh grafiet-siviour-portadelaide`); beide wegbenen als vooraf gebakken lijn uit de profielen `grafiet-siviour-portadelaide-siviour-bolivar` en `...-bolivar-outerharbor` in `maak_stroombeen_weg.py` (wegscan_puur.py, extract australie; geojson in `v2/build-cache/ais/graaf/grafiet-siviour-portadelaide-weg-*.geojson`). Hergebakken en getoetst bij de afronding; geen zee, dus geen MARNET-routing.

| # | modaliteit | been | km gemeten | km brief | stijl |
|---|---|---|---|---|---|
| b1 | truck | Siviour-mijn naar Bolivar PSG-site (Lincoln Hwy B100 via Cowell, Whyalla, Port Augusta, dan Augusta Hwy / Princes Hwy A1 via Port Wakefield) | 526,9 (3.087 punten) | ca 500 tot Port Adelaide (bedrijf); hemelsbreed 220, geen wegkm | doorgetrokken, aannemelijk: één bron in de naam |
| b2 | truck | Bolivar PSG-site naar Outer Harbor, Port of Adelaide (Port Wakefield Rd, Port Rd) | 26,0 (456 punten) | ca 20 tot Port Adelaide (niet Outer Harbor); hemelsbreed 8,4, geen wegkm | doorgetrokken, aannemelijk: één bron in de naam |

**Toets:** A+B 552,9 km tegen ca 500 km tot Port Adelaide = +10,6% (binnen ±15%, maar de referentie is een afgeronde bedrijfsopgave; b2 apart is alleen een indicatie). Naad b1 naar b2 0,0 km. Alle drie de markers liggen op de lijn (0,0 km). `toets_knikken`: 22 knikken van 60 gr of meer over beide benen, 1 omkering (176 gr op het mijnanker, ankerprojectie, geen terugloop), 0 terugloop; de rest zijn spikes in OSM-geometrie bij het Bolivar-terrein en Outer Harbor. `toets_rechte_benen --min-km 5`: geen regel voor deze stroom. Geen stippel nodig.
**Toelichting stippel / aanloop / vlucht / leiding:** geen. Geen stippel (beide ankers liggen op het net), geen haven-aanloop (geen zeebeen; Outer Harbor ligt 16,6 km van MARNET-zeeknoop 6042 en krijgt er een zodra een zeebeen komt), geen vlucht, geen leiding, geen letterlijke kopie (het uranium-been Olympic Dam naar Outer Harbor, 581,9 km, is niet te knippen).
**Lessen:** (1) bij een bedrijfsopgave "tot Port Adelaide" is de km-toets alleen zinvol op A+B samen, niet per been; (2) Port Wakefield snapte 0,74 km van het via-punt, de andere via-punten 0,03 tot 0,09 km, (proefbake); (3) het mijnanker is OSM-straatnaam, geen bevestigde mijn: de 176 gr omkering op het eerste punt komt daar vandaan en hoeft niet gerepareerd; (4) Lucky Bay (ca 60 km, voorkeurshaven volgens Mining Technology) is niet getekend omdat een bron-coordinaat ontbreekt.
