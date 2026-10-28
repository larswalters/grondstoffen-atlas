# Routebrief (licht) · uranium — Walvis Bay → Hamburg → Malvési (Namibië → Frankrijk)

**stroom-id:** `uranium-walvisbay-malvesi` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) ·
**status:** gebakken
**Keten in één zin:** Namibisch uraanerts-concentraat (yellowcake, mijn niet genoemd) gaat per containerschip van de
NamPort-kade in Walvis Bay naar de C. Steinweg Süd-West-Terminal in Hamburg en daar per goederentrein (6–14 containers)
via Münster, Köln, Koblenz, Trier, Metz, Dijon, Lyon en Miramas naar Orano Malvési (Narbonne) — **aannemelijk: alleen activistenbronnen 2014–2018**.
**Welke as van het verhaal:** de Hamburger draaischijf naar de Franse conversie. Geen volume voor déze route: zendingen van 6–14 containers
(≈ 33–36 containers per trein [4][5], "mogelijk 150 t" [6]); Malvési verwerkte 12.454 t UF4 in 2013 (output, ≈ 9.400 tU) [3]; nameplate ~15.000 tU/j [8].

## 1 · Ketenkaart
```
Walvis Bay-kade `u-walvisbay-haven` ──(b1a zee haven-aanloop 12,5 km, stippel)──► MARNET-zeeknoop 8084
Walvis Bay-kade ──(b1b zee · MARNET · 10.965 km, Atlantisch → Kanaal → Noordzee → Elbe)──► Hamburg Süd-West-Terminal `u-hamburg-steinweg`
Hamburg Süd-West ──(b2 spoor · Hamburg–Rotenburg–Bohmte–Münster–Hamm–Köln–Koblenz–Trier–Perl–Metz–Dijon–Lyon–Miramas–Narbonne · ~1.750 km)──►
Orano Malvési `u-malvesi` ── stoppunt (b2 sluit af met 7,1 km Malvési-aftakking, kopie)
```
**Afwijking t.o.v. het ketenontwerp:** (a) b1 = zee in twee delen, want Walvis Bay-kade ligt 12,5 km van de MARNET-zeeknoop (haven-aanloop); (b) de Hamburg-kade snapt op 4,14 km
(< 5 km) dus geen tweede aanloop, naad zee→spoor 4,17 km (binnen de norm); (c) het schip "Golden Karoo" is niet teruggevonden, alleen "Green Mountain" (MASC) [4].

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1a | B | zee | `u-walvisbay-haven` → zeeknoop 8084 (-22.8344, 14.4759) | haven-aanloop over de baai | 12,5 (MARNET-snap) | rechte stippel (letterlijke kopie uit `bak_uranium_langerheinrich_metropolis`) | ja — het net reikt niet tot de kade |
| b1b | B | zee | `u-walvisbay-haven` → `u-hamburg-steinweg` | Atlantisch → Kanaal → Noordzee → Elbe; MASC Green Mountain (2014) [4] | hemelsbreed 8.514; gemeten 10.965,5 | MARNET (`--been zee`) | nee — Hamburg snap 4,14 km (zeeknoop 3944) |
| b2 | C | spoor (aannemelijk: één bron per stuk) | `u-hamburg-steinweg` → `u-malvesi` | Rollbahn Hamburg–Rotenburg–Bohmte → Münster–Hamm → Köln → Bonn → Koblenz → Moselstrecke → Perl–Apach–Thionville → Metz → Toul → Dijon → Rhône links → Miramas → Arles → Nîmes-omleiding → Béziers → Narbonne | hemelsbreed 1.255; geen spoorkm gepubliceerd; gemeten 1.749,6 (8 runs + 7,1 kopie) | `toets_spoorroute.mjs` (`BAKE_SUFFIX=-raw`), 8 runs + omgekeerde kopie | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-walvisbay-haven` | laadkade zee | NamPort containerterminal, Walvis Bay | -22.9465, 14.4840 | letterlijk uit `uranium-rossing-walvisbay` §3 [9]; Walvis Bay-laadplek Namibisch uranium [4] | bron-gelegd (z16 gezien in de Rössing-brief: containerterminal met stapels en kade) |
| `u-hamburg-steinweg` | overslag zee → spoor | C. Steinweg Süd-West-Terminal, Kleiner Grasbrook, Hamburg | 53.5335, 9.9868 | [1][3][12] (OSM landuse=industrial "C. Steinweg Süd-West Terminal") | bron-gelegd (z15 gezien: kadeschiereiland met loodsen en spoor, rangeerterrein Hamburg-Süd direct zuidelijk) |
| `u-malvesi` | conversie, stoppunt | Orano Malvési (Comurhex I), Narbonne | 43.2074, 2.9812 | letterlijk `w-malvesi` in `uranium-sitelaag.json` [8] en `uranium-malvesi-tricastin` [10] | bron-gelegd (z15 gezien: industrieel complex met loodsen, verdampingsbekkens NNO; sitelaag had alleen "aannemelijk") |

## 4 · Via-punten (b2, alleen corridorkeuzes en net-artefacten; allemaal OP de doorgaande lijn, kop-via-staart)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Bohmte (station) | 52.3608, 8.3075 | BBU-waarneming 8-4-2014 02:15 [6]; Hamburg–Bohmte rijdt zonder via-punt al over Rotenburg (geen Soltau-omweg), dus dit pint de Bremen–Osnabrück-corridor |
| b2 | 2 | Hamm Hbf (station) | 51.6783, 7.8081 | bron noemt Hamm [6]; zonder dit punt kiest de router Münster–Dortmund en slaat Hamm over |
| b2 | 3 | Bullay (station, Moselstrecke) | 50.0544, 7.1350 | corridorkeuze: Köln–Bonn–Koblenz–Mosel [6][7] i.p.v. de kortere Eifelstrecke (223,7 km tegen 264 km via Koblenz); ná Cochem, dus de Cochem-omkering is met `--keerstraf=150` weggebakken |
| b2 | 4 | Perl (station, grens) | 49.4732, 6.3694 | bron: Perl–Apach [6][7] i.p.v. Luxembourg (de router koos vrij Luxembourg) |
| b2 | 5 | Metz-Ville (station) | 49.1103, 6.1767 | Woippy ligt op de route (0,1 km); via Metz-Ville vermijdt een 1,4 km spoor-uit-en-terug bij Metz-Sablon |
| b2 | 6 | Dijon-Ville (station) | 47.3233, 5.0275 | Dijon staat in de bron [2]; zonder dit punt een 28 m-omkering ten zuiden van Dijon |
| b2 | 7 | Miramas-west (emplacement) | 43.5814, 4.9808 | Miramas [2][7] i.p.v. Avignon–Tarascon–Nîmes direct; punt op de omkering-apex = westkop van het emplacement, geen yard-stub |
| b2 | 8 | Gare de Narbonne | 43.1906, 3.0057 | aansluiting Malvési-aftakking; zelfde punt als b1 van `uranium-malvesi-tricastin` [10] |
Niet als via-punt gebruikt: Sibelin (45.6498, 4.8383) — yard-stub, gaf twee omkeringen; Dijon-Perrigny — geen coördinaat gevonden.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| C. Steinweg Süd-West-Terminal | C. Steinweg Hamburg | containers U3O8 van schip → trein | geen cijfer; 6–14 containers per zending | [1][3][4] |
| Orano Malvési | Orano | U3O8 → UF4 | 12.454 t UF4 (2013, output, ≈ 9.400 tU) [3]; nameplate ~15.000 tU/j [8] | [3][8] |

## 6 · Stoppunt
De brief stopt bij Orano Malvési: het ketenontwerp eindigt daar en de vervolgstap UF4 → Tricastin staat al in `uranium-malvesi-tricastin` (geen dubbel getekend been). Fase D/E vervallen.

## 7 · Open punten
- **Alleen activistenbronnen:** sortirdunucleaire (2015) [1][2], BBU (2014) [6], taz (2014) [4], Freedom Press (2018) [5], Atomdrehscheibe Hamburg [3]; geen operator- of overheidsbron. Daarom aannemelijk: één bron per stuk.
- **Herkomst wisselt:** Namibië (Green Mountain, jan 2015 [1]; 2018 [5]) en Kazachstan (Mikhail Dudin vanuit Sint-Petersburg, sept 2015 [2][4]) per zending; de mijn is nooit genoemd, dus de lijn begint op de kade. Of élke trein Walvis Bay-lading draagt, is niet gepubliceerd.
- **Route Hamburg–Metz is waargenomen, niet gepubliceerd:** BBU zag Maschen en Bohmte, de rest is "vermoed"; Dijon–Lyon–Miramas staat alleen in een lijst van 2015 [2] en in een zoekresultaat van een BBU-bericht van 10-1-2014 (Perrigny, Sibelin; niet zelf gelezen).
- **Hamburg-aanloop niet gedaan:** snap 4,14 km < 5 km; naad zee→spoor 4,17 km blijft staan (norm).
- **Walvis Bay-aanloop = rechte stippel:** `maak_havenaanloop.py` gaf voor exact deze kade twee keer exit 124 (langerheinrich-brief); niet opnieuw geprobeerd.
- **Terugloop bij Narbonne** (43.1870, 3.0011) staat ook in `uranium-malvesi-tricastin`; niet weggeschoven. Cochem-omkering is weg met `--keerstraf=150`.
- **Weg- of spoorkm** niet gepubliceerd; de ±15%-toets geldt niet als norm. Gemeten 1.749,6 km = +39% op hemelsbreed (omweg langs Ruhr, Mosel en Rhône).
- **Overlap (gemeten, punten < 150 m):** 218 km met het spoor van `uranium-malvesi-tricastin` (Narbonne–Nîmes/Avignon-zone) en 381 km met `uranium-tricastin-seversk` (Dijon–Lyon–Rhône), beide in tegengestelde richting; geen kopie, alleen de 7,1 km Malvési-aftakking is een kopie.

## 8 · Bronnen
[1] Sortir du nucléaire, "Un nouveau train de yellow cake en route" (trein Hamburg Süd-West-Terminal C. Steinweg 29-1 → Malvési 2-2-2015, Green Mountain, 6 containers, Namibië) https://www.sortirdunucleaire.org/Un-nouveau-train-de-yellow-cake-en
[2] Sortir du nucléaire, "Transport d'uranium Hambourg-Narbonne" (10-9-2015; Woippy, Dijon, Lyon, Miramas, Montpellier, Béziers, Narbonne; Mikhail Dudin; 14 containers) https://www.sortirdunucleaire.org/Transport-d-uranium-Hambourg-Narbonne
[3] Atomtransporte Hamburg stoppen, "Uranfabrik Narbonne-Malvési" (12.454 t UF4 in 2013; Steinweg Süd-West-Terminal; herkomstlanden) https://www.atomtransporte-hamburg-stoppen.de/wer-ist-an-den-transporten-beteiligt/uranfabrik-narbonne-malvesi/
[4] taz, 18-8-2014 (Green Mountain, 14 containers yellow cake, MASC stopt vaak in Walvis Bay, trein van 36 containers naar Narbonne via Bremen) https://taz.de/!308887
[5] Freedom Press (Freedom News), 3-9-2018 (blokkade bij Koblenz, Namibisch yellowcake, ~33 containers, Hamburg → Malvési) https://freedompress.org.uk/2018/09/03/french-and-german-anti-nuclear-campaigners-block-uranium-transport/
[6] BBU-persbericht 8-4-2014 (Hamburg-Süd 18:05, Maschen, Bohmte 2:15; vermoede route Münster-Hamm-Hagen-Köln-Bonn-Koblenz-Trier-Perl-Apach-Woippy-Miramas-Béziers-Narbonne; mogelijk 150 t) https://bbu-online.de/presseerklaerungen/prmitteilungen/PR%202014/08.04.14.pdf
[7] BBU-persbericht 10-1-2014 (alleen als zoekresultaat gezien: Köln-Gremberg, Apach, Woippy, Perrigny, Sibelin, Miramas) https://bbu-online.de/presseerklaerungen/prmitteilungen/PR%202014/10.01.14.pdf
[8] `v2/design/uranium-sitelaag.json`, `w-malvesi` (43.2074, 2.9812; ~15.000 tU/j indicatief)
[9] `v2/design/routebrieven/uranium-rossing-walvisbay.md` §3 (Walvis Bay-kade); `uranium-langerheinrich-metropolis.md` b2a (aanloop-stippel)
[10] `v2/design/routebrieven/uranium-malvesi-tricastin.md` (Malvési-aftakking b1a, Narbonne-terugloop)
[11] Wikipedia (de/fr) via MediaWiki-API `prop=coordinates`: Bohmte, Hamm Hbf, Bullay, Perl, Apach, Thionville, Woippy, Narbonne
[12] OpenStreetMap via Photon: "C. Steinweg Süd-West Terminal" (landuse=industrial, Kleiner Grasbrook) 53.5335, 9.9868
[sat] Esri World Imagery (`v2/tools/sat_check.py`): `v2/build-cache/satcheck/sat-uranium-walvisbay-malvesi-{steinweg-sw,hamburg-wide,malvesi}.png`
[haalbaarheidstoets] Bindend invoerdocument (zee 10.966 km, Steinweg 53.5335/9.9868, 7–9 runs) — nagevolgd; Koblenz–Trier-omkering als netartefact opgelost met `--keerstraf=150`.

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
**Bestand:** `v2/data/stroomroute-uranium-walvisbay-malvesi.json` (129,2 KB, contract versie 2, lonlat, 11 benen, 7.660 punten, 3 markers). **Functie:** `bak_uranium_walvisbay_malvesi` in `v2/tools/bak_stromen.sh`; `bash v2/tools/bak_stromen.sh uranium-walvisbay-malvesi`. Totaal **12.726,6 km**.

| # | modaliteit | km | naad | opmerking |
|---|---|---|---|---|
| 1 | zee (stippel) | 12,5 | 0 | haven-aanloop Walvis Bay, rechte stippel, letterlijke kopie van de regel in `bak_uranium_langerheinrich_metropolis` |
| 2 | zee | 10.965,5 | 0 | MARNET kade → kade (Walvis Bay → Hamburg Steinweg), doorgetrokken |
| 3 | spoor | 204,3 | 4,17 | Steinweg → Bohmte (Rotenburg-route); naad = Hamburg-zeesnap 4,14 km, binnen de norm |
| 4 | spoor | 110,1 | 0 | Bohmte → Hamm |
| 5 | spoor | 286,9 | 0 | Hamm → Bullay (`--keerstraf=150`) |
| 6 | spoor | 100,1 | 0 | Bullay → Perl |
| 7 | spoor | 56,8 | 0 | Perl → Metz-Ville |
| 8 | spoor | 265,0 | 0 | Metz → Dijon |
| 9 | spoor | 505,2 | 0 | Dijon → Miramas-west |
| 10 | spoor | 213,1 | 0 | Miramas → Narbonne |
| 11 | spoor | 7,1 | 0 | Narbonne → Malvési, omgekeerde kopie van `uranium-malvesi-tricastin` b1a |

**Markers:** `u-walvisbay-haven` 0,00 km van de lijn, `u-hamburg-steinweg` 0,11 km, `u-malvesi` 0,11 km.
**Recept:** de 8 spoorruns (`BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs`, prefix `spoorroute-uranium-walvisbay-malvesi-`) waren al gebakken; de functie plakt ze als `--been-geojson` aan de MARNET-zeeroute. Geen weg-, leiding- of luchtbeen, geen extract nodig.
**Stippel:** alleen de haven-aanloop Walvis Bay (b1a, "hier reikt het net niet"). Hamburg heeft geen aanloop (snap 4,14 km < 5 km).
**Spoorkm:** gemeten som 1.748,6 km (de brief noemde 1.749,6; het totaal 12.726,6 klopt met de dry-run). Geen gepubliceerde spoorkm, +39% op hemelsbreed 1.255; de ±15%-toets is een indicatie.
**Toets:** `toets_knikken` geeft alleen de bekende Narbonne-terugloop (43,1870, 3,0011), ook in `uranium-malvesi-tricastin`; verder één krappe zeebocht (62,5 gr, R 9,5 km) bij 13,81 E voor de kust van Namibië. `toets_rechte_benen`: alleen de aanloop-stippel (bedoeld).
**Lessen:** een vooraf gebakken spoorketen hergebruiken kost één kleine functie en een bake van 16 s; de zware stap zat in de spoorruns zelf.
