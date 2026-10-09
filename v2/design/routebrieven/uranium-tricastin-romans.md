# Routebrief (licht) · uranium — Orano Tricastin → A7 → Framatome Romans-sur-Isère (Frankrijk)

**stroom-id:** `uranium-tricastin-romans` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken
**Keten in één zin:** verrijkt UF6 (Georges Besse II, Orano Tricastin, Pierrelatte) gaat per **truck** over de
A7 (Rhônevallei) en via de N532/A49 naar Framatome Romans-sur-Isère, waar het tot UO2-poeder, pastilles en
splijtstofassemblages wordt verwerkt — stoppunt; de laatste binnenlandse schakel van de Franse keten.
**Welke as van het verhaal:** Frankrijk, verrijking → splijtstof (reserve-as, prioriteit 3). Volumes: Georges
Besse II ≈ 12% van de wereld-SWU ≈ **~7.800 t U feed-equivalent/j** (sitelaag `w-tricastin-verrijking`, peiljaar
2024, Orano Activity Report [6]); Romans **indicatief ~1.600 t HM/j** (sitelaag `w-framatome-romans`). **Geen bron
noemt een tonnage voor déze relatie.**

## 1 · Ketenkaart
```
Orano Tricastin — Georges Besse II (verrijking), Pierrelatte `u-tricastin`
  ──(b1 D truck · A7 → N7/N532 (Valence-oost) → A49 · hemelsbreed 86,2 km, geen wegkm · aannemelijk: bron-relatie, geen tonnage)──►
Framatome Romans-sur-Isère (UF6 → UO2 → assemblages) `u-framatome-romans` ── stoppunt
```
**Bewijskracht (verbetert de haalbaarheidstoets):** de toets typeerde de relatie als "één bron (Wikipedia)" en
verwees naar `uranium-malvesi-tricastin.md` §7/§8, waar dezelfde claim niet onafhankelijk te bevestigen was. Dit
onderzoek vond **twee aanvullende bronnen**: een SFRP-samenvatting van 1–2 feb. 2023 die in dezelfde keten zegt
dat het (bij Georges Besse II) verrijkte UF6 **per weg** naar Framatome Romans gaat om UO2 te worden [2], en
Reporterre ("een honderdtal km", ouder, ex-Areva/FBFC) [3]. Dat is méér dan één bron maar nog steeds geen
tonnage of datum van een zending → **status blijft "aannemelijk"** (in de beennaam), de lijn is gewoon gemeten
en doorgetrokken. Het §7-incident van `uranium-malvesi-tricastin` (UF6 uit Nederland bij Romans, dec. 2023)
weerlegt dit niet: Romans heeft meerdere toeleveranciers (Urenco én Orano); die brief liet Tricastin→Romans
alleen vervallen bij gebrek aan een bron, en [2] is die bron.

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | D | truck | Orano Tricastin → Framatome Romans-sur-Isère | A7 (Montélimar–Loriol) → N7/N532 Valence-oost → A49 | **hemelsbreed 86,2 km, geen wegkm** (ankers onderling) [indicatie; ±15%-toets geldt niet als norm]; Reporterre "une centaine" [3]; niet-officiële OSRM-voorspelling ~112 km [8] | maak_stroombeen_weg (extract fr-rhone-alpes) | nee — *aannemelijk: bron-relatie, geen tonnage* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-tricastin` | verrijking (kop) | Orano Tricastin — Georges Besse II, Pierrelatte, Drôme | 44.3250, 4.7167 | letterlijk uit `uranium-malvesi-tricastin.md` §3 / sitelaag `w-tricastin-verrijking` [6][7] | bron-gelegd (z14 opnieuw gezien: kruis in het zuidelijke deel van het grote industriecomplex tussen de spoor-/A7-corridor en het Donzère-Mondragon-kanaal; Esri toont het complex vervaagd) |
| `u-framatome-romans` | splijtstoffabricage (staart, stoppunt) | Framatome Romans-sur-Isère (FBFC + CERCA, INB 63-U), Drôme | 45.0512, 5.0982 | OSM way 183695477 (45.0509, 5.0980) [5] + Wikipedia fr "Site nucléaire de Romans" (45.0516, 5.0985, ~30 ha) [4] | bron-gelegd (z15 gezien: omheind compound van ~0,6 × 0,9 km, door Esri vervaagd, in de industriezone aan de oostrand van Romans; kruis in het midden) |

**⚠️ Afwijking t.o.v. de sitelaag:** `w-framatome-romans` staat op 45.0500, 4.9667 (status "onzeker") — dat is
**8,6 km te ver west**, in akkers (z14 gezien: geen terrein). Deze brief gebruikt 45.0512, 5.0982; de sitelaag is
niet aangepast (buiten mijn bestanden) en moet centraal gelijkgetrokken worden (zie §7).

## 4 · Via-punten (b1 — corridorkeuze A7 i.p.v. N7/D-wegen door Montélimar en Valence, ligging op de weg uit OSRM-geometrie)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | A7 bij Montélimar | 44.5795, 4.8057 | op de autoroute; sluit de N7/D-wegen door het centrum van Montélimar uit (ook een toegang via Pierrelatte → Montélimar-Zuid komt hier samen) |
| b1 | 2 | A7 bij Loriol-sur-Drôme/Livron | 44.7602, 4.7956 | houdt de route op de A7-corridor langs de Rhône i.p.v. de Drôme-vallei of de N7 |
| b1 | 3 | N532, Plateau des Couleures (Valence-oost) | 44.9522, 4.9358 | corridorkeuze: Valence **ommeweg langs de oostrand** (N7 → N532) naar de A49, niet door het stadscentrum |
| b1 | 4 | A49 bij Bourg-de-Péage | 45.0164, 5.0282 | A49 Valence → Romans-sur-Isère; pint de snelwegaanvoer naar de fabriek i.p.v. D-wegen door de randgemeenten |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Georges Besse II (Tricastin) | Orano | UF6 (natuurlijk) → verrijkt UF6 | ~12% wereld-SWU ≈ ~7.800 t U feed-eq./j | [6] |
| Romans-sur-Isère | Framatome (FBFC/CERCA) | verrijkt UF6 → UO2-poeder → pastilles → staven → assemblages (≈80% EDF-park) | indicatief ~1.600 t HM/j | [4][6] |

## 6 · Stoppunt
De brief stopt bij Framatome Romans-sur-Isère: dat is het opgedragen eindpunt en de fabriek is zelf de laatste
schakel waarover één bron iets zegt (assemblages gaan daarna naar EDF-reactoren en export, [4]); een tweede
Franse splijtstoflocatie of reactor is niet specifiek aan deze stroom te koppelen. Fase E vervalt.

## 7 · Open punten
- **Geen wegkm gepubliceerd.** Alleen hemelsbreed 86,2 km tussen de ankers; "une centaine de km" [3] is een
  vage, oudere uitspraak. De ±15%-toets geldt hier als indicatie. Voorbereidende meting (Overpass, niet de
  uiteindelijke bake): 106,8 km over A7 → N7/N532 → A49 = +23,8% tegen hemelsbreed, −4,6% tegen de OSRM-schatting
  (~112 km) — een normale omwegfactor voor de Rhônevallei.
- **Sitelaag-anker `w-framatome-romans` ligt 8,6 km te ver west** (45.0500, 4.9667, "onzeker"); centraal
  corrigeren naar 45.0512, 5.0982 (en status bron-gelegd), anders spreekt de gloedlaag de keten tegen.
- **Geen tonnage of zendingsfrequentie** voor Tricastin → Romans; het volume hierboven is fabrieksbreed.
  Romans wordt óók beleverd vanuit Nederland (Urenco, `uranium-malvesi-tricastin.md` §7 [5]); het aandeel
  Tricastin is niet te bepalen.
- **Route is een corridor-aanname**: de A7/A49-aanvoer volgt uit OSM-routering (en past bij "par route" [2]),
  geen bron noemt het traject van de convooien (transporten van splijtbaar materiaal kunnen van de snelste
  route afwijken).
- Het kopanker ligt midden in het complex (z14, vervaagd); de precieze poort/loshal is niet bepaald (brief
  stopt op site-niveau, geen last-mile-been: first mile 4,7 km en last mile 2,3 km over kleine wegklassen
  zijn onderdeel van het wegprofiel).
- Het Wikipedia (en)-artikel "Franco-Belge de Fabrication du Combustible" noemt ook een FBFC-vestiging óp het
  Tricastin-terrein; dat is een andere activiteit en geen alternatief eindpunt.

## 8 · Bronnen
[1] Wikipedia (en), "Nuclear fuel cycle in France" — Georges Besse II verricht de verrijking op de Tricastin-site; verrijkt UF6 wordt bij de FBFC-fabriek op de Romans-site tot UO2 omgezet en de assemblages worden daar vervaardigd. https://en.wikipedia.org/wiki/Nuclear_fuel_cycle_in_France
[2] SFRP, "Au cœur de l'uranium", 1–2 feb. 2023, Paris — samenvatting transport uranium (Darras / De Bastiani): verrijkt UF6 (Georges Besse II) wordt per weg naar Framatome Romans-sur-Isère vervoerd om UO2 te worden; assemblages daarna per weg/trein naar EDF. https://sfrp.asso.fr/wp-content/uploads/2023/02/S6_DARRAS_F-1.pdf
[3] Reporterre, "Pas de frontières pour le nucléaire : le parcours secret de l'uranium en Europe" — verrijkt uranium naar Romans-sur-Isère "à une centaine de kilomètres du Tricastin" (alleen via zoekresultaat gelezen, pagina gaf 403; ouder, noemt nog Areva/FBFC). https://reporterre.net/Pas-de-frontieres-pour-le-nucleaire-le-parcours-secret-de-l-uranium-en-Europe
[4] Wikipedia (fr), "Site nucléaire de Romans" — site van Framatome, ~30 ha, FBFC (INB 98) + CERCA; coördinaat 45.0516, 5.0985; FBFC voedt ~80% van het EDF-park. https://fr.wikipedia.org/wiki/Site_nucl%C3%A9aire_de_Romans
[5] OpenStreetMap (Nominatim), "Framatome, Romans-sur-Isère" — way 183695477, 45.0509, 5.0980 (ODbL). https://nominatim.openstreetmap.org/search?q=Framatome+Romans-sur-Is%C3%A8re&format=jsonv2
[6] `v2/design/uranium-sitelaag.json`/`.md` — `w-tricastin-verrijking` (44.3250, 4.7167, bron-gelegd, ~12% SWU) en `w-framatome-romans` (45.0500, 4.9667, onzeker, ~1.600 t HM/j); bronnen [B17][B19][B29] aldaar.
[7] `v2/design/routebrieven/uranium-malvesi-tricastin.md` §3/§7/§8 — anker `u-tricastin` letterlijk hergebruikt; eerder onderzoek naar dezelfde relatie zonder bevestiging; Nederlandse UF6-aanvoer bij Romans (ASNR/sortirdunucleaire.org).
[8] OSRM (router.project-osrm.org, driving) — niet-officiële routevoorspelling Tricastin → Romans: 112,0 km via A7 → N7 → N532 → A49 (OSRM routeert over OSM; indicatie, geen bron voor km).
[9] Wikipedia (en), "Franco-Belge de Fabrication du Combustible" — FBFC-hoofdkantoor sinds 1977 in Romans-sur-Isère; tweede vestiging op Tricastin. https://en.wikipedia.org/wiki/Franco-Belge_de_Fabrication_du_Combustible
[haalbaarheidstoets] Bindend invoerdocument (keten-id `uranium-tricastin-romans`): risico verzwakt van "stevig gebrond" naar "aannemelijk", verwijzing naar `uranium-malvesi-tricastin.md` §7/§8 — toegepast.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-uranium-tricastin-romans.json` (28,3 KB, contract versie 2, punt_formaat lonlat) ·
functie `bak_uranium_tricastin_romans()` in `v2/tools/bak_stromen.sh` · profiel `uranium-tricastin-romans` in
`v2/tools/maak_stroombeen_weg.py` · tussenuitvoer `v2/build-cache/ais/graaf/uranium-tricastin-romans-weg-tricastin-romans.geojson`.

| been | modaliteit | km gebakken | km brief | punten | doorgetrokken? |
|---|---|---|---|---|---|
| b1 verrijkt UF6 Orano Tricastin → Framatome Romans-sur-Isère (A7 → N532 → A49, aannemelijk: bron-relatie, geen tonnage) | truck | **106,9** | hemelsbreed 86,2 (geen wegkm) | 1.538 | ja |

**Totaal 106,9 km · 1 been · 2 markers** (`u-tricastin` 44.3250,4.7167; `u-framatome-romans` 45.0512,5.0982; beide 0,0 km van de lijn).
Geen naad (één been), geen stippel, geen haven-aanloop, geen zeebeen, geen vlucht, geen leiding, geen gedeelde kopie.

**Recept.** `python v2/tools/maak_stroombeen_weg.py --profiel uranium-tricastin-romans --bron overpass` (extract fr-rhone-alpes;
pyosmium/Geofabrik is op deze machine geblokkeerd, Overpass werkte bij de tweede poging); zes invoerpunten (anker, 4 via-punten
op A7/N532/A49, anker), snaps 0,08/0,00/0,00/0,00/0,00/0,02 km; 68 keerlussen gesnoeid. Daarna
`bash v2/tools/bak_stromen.sh uranium-tricastin-romans` (herbakken in dit rondje bevestigd: 106,9 km, 1.538 punten, ongewijzigd).

**Toets.** Lengte 106,9 km = +23,8% tegen hemelsbreed (86,2 km) en −4,6% tegen de niet-officiële OSRM-voorspelling
(~112 km): de ±15%-toets is hier **indicatie, geen norm** (geen gepubliceerde wegkm), en +24% is een normale omwegfactor
voor de Rhônevallei. `toets_knikken.py`: 12 knikken ≥ 60°, 0 terugloop; de ene omkering (166,8°, R 20 m bij 45.0238,5.0817)
is een echte scherpe bocht (v=1,3), de overige spikes liggen binnen de eerste/laatste 2–5 km op kleine wegklassen in het
fabrieksterrein (first mile 4,7 km, last mile 2,3 km). `toets_rechte_benen.py --min-km 5`: geen treffer voor deze stroom.

**Afwijkingen / lessen.**
- Sitelaag-anker `w-framatome-romans` (45.0500, 4.9667) ligt 8,6 km te ver west; deze stroom gebruikt 45.0512, 5.0982 (OSM way 183695477 + Wikipedia fr). Sitelaag niet gewijzigd, centraal gelijktrekken.
- Het ontwerp ging uit van 83 km (fout sitelaagpunt); gecorrigeerd 86,2 km hemelsbreed.
- Route is een corridoraanname (OSM-routering); geen bron noemt het convooi-traject. Geen tonnage per relatie; Romans krijgt ook Urenco-UF6.
- Slot-hulp: `rm -rf "$d"` en `rmdir "$d"` met een variabele worden door de Claude-Code-veiligheidscheck geblokkeerd; neem een slot met `mkdir` en geef het vrij met een rmdir op een letterlijk pad.
- Tijdens het herbakken gaf `bash v2/tools/bak_stromen.sh` kort een syntaxfout in de functie van een andere agent (`bak_olie_abqaiq_yanbu`, ~regel 7668) na de dispatch; bij herkeuring met `bash -n` was het weg. Mijn bake was ongestoord.

**Registerregel (centraal):** `{ "sleutel": "u-tr", "bestand": "stroomroute-uranium-tricastin-romans.json", "grondstof": "uranium", "label": "Tricastin → Romans", "aan": true, "noot": "M31 · golf 7 (2026-10-09): verrijkt UF6 per truck over A7/N532/A49 van Orano Tricastin naar Framatome Romans-sur-Isère (aannemelijk, geen tonnage)" }`
