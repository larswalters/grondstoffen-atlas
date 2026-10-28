# Routebrief (licht) · goud — Arezzo (Italpreziosi) → A1/A50/A9 → Valcambi, Balerna (Zwitserland)

**stroom-id:** `goud-arezzo-valcambi` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) ·
**status:** gebakken (2026-10-28)
**Keten in één zin:** goudstaven van de Good Delivery-raffinaderij Italpreziosi (San Zeno, Arezzo) per truck over de
A1 (Variante di Valico), de A50-ring van Milaan en de A9 naar de Ticino-raffinagecluster, aannemelijk Valcambi in Balerna.
**Welke as van het verhaal:** Italiaanse goudstaven (Arezzo-district) naar Zwitserse raffinage/handel, de Italië-Ticino-as.
Jaarvolume **ca 110 t Au/j** (indicatie, peiljaar 2025: Arezzo-baarexport "bijna 11 mld euro" [1], eigen omrekening ÷ ca 97.000 euro/kg
= aanname 2025-goudprijs, niet gebrond, alle bestemmingen; v1-register zegt 120 t, niet geverifieerd) — geen Zwitserland-specifiek tonnage gevonden (§7).
**Herformulering (haalbaarheidstoets, BINDEND):** de ontwerp-premisse "sieradenschroot naar Valcambi" klopt niet. De gebronde
Arezzo-stroom naar Zwitserland is goudstaven van raffinaderijen die zelf recupereren en raffineren (Italpreziosi, Chimet) [1][2][3][5].
Geen sieradenschroot-claim; Valcambi als ontvanger is aannemelijk, niet gebrond.

## 1 · Ketenkaart
```
Italpreziosi, Strada B/A, Zona Industriale San Zeno, Arezzo `au-arezzo-italpreziosi`
  ──(b1 truck · SS679-raccordo → A1 → Variante di Valico → A1 → A50 Milaan-West → A8/A9 → Chiasso · ~428 wegkm, indicatie)──►
Valcambi SA, Balerna `au-ref-valcambi` (hergebruikt uit goud-loulo-ticino.md) ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Italpreziosi, Arezzo → Valcambi, Balerna (aannemelijk: één bron voor Zwitserland, Valcambi niet gebrond) | A1 (Variante di Valico) → A50 → A8 → A9 → Chiasso → Balerna | 428 wegkm [7] (OSRM over OSM = indicatie, geen bedrijfs-/overheidsopgave); hemelsbreed 349 km, geen wegkm | maak_stroombeen_weg (extracts italie + zwitserland) | nee, doorgetrokken |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `au-arezzo-italpreziosi` | raffinaderij / laadplek | Italpreziosi SpA, Zona Industriale San Zeno, Arezzo | 43.4290, 11.8333 | [5][6] | bron-gelegd (z15+z16 gezien: bedrijfsterrein met loodsen in de industriezone San Zeno, groot witdakig magazijn direct ZW van het kruis; het kruis ligt op het gebouwencluster, niet in akker of bos; welk pand de raffinage is, is op deze resolutie niet te zien) |
| `au-ref-valcambi` | losplek / raffinaderij | Valcambi SA, Via Passeggiata 3, Balerna | 45.8385, 9.0051 | [8][9] | bron-gelegd (HERGEBRUIKT letterlijk uit goud-loulo-ticino.md en goud-valcambi-londen.md: bedrijfsgebouw tegen de spoorbundel Balerna-Chiasso, OSM-building "Valcambi SA") |

Het adres op de bedrijfssite is Strada A 32, het OSM-punt (ItalPreziosi, shop=jewelry) ligt aan Strada B, zelfde industriezone [5][6]; verschil 0,2 km, op siteniveau gelijk.

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Alle punten zijn gekozen op de OSRM-routegeometrie (OSM-wegnet) en liggen daardoor per constructie op de doorgaande weg, niet in een stadscentrum [7].
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | A1-oprit Arezzo (einde raccordo SS679) | 43.4414, 11.7738 | pint de toegang tot de A1 bij Arezzo i.p.v. de SR71/E45-sluipweg |
| b1 | 2 | A1 Variante di Valico, Apennijnen | 44.0294, 11.2255 | pint de Variante (A1var) boven de oude Direttissima Firenze-Bologna |
| b1 | 3 | A1 bij Parma | 44.8469, 10.3099 | houdt de route op de A1 over de Via Emilia-vlakte (5,7 km van Parma-centrum, op de snelweg) |
| b1 | 4 | A1 bij Piacenza | 45.0242, 9.7753 | pint de A1 naar Milaan en sluit de A21-afslag naar Brescia uit |
| b1 | 5 | A50 Tangenziale Ovest, Milaan-West | 45.4120, 9.1023 | pint de westelijke ring (A50) i.p.v. de Tangenziale Est of een route door het centrum |
| b1 | 6 | A8/A9-knooppunt Lainate | 45.5725, 9.0148 | splitsing A8 (Varese) / A9 (Como): kiest de A9 |
| b1 | 7 | A9 vóór Chiasso | 45.7968, 9.0496 | A9 Como-Chiasso, enige corridor naar de grens; laatste punt vóór Brogeda |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Italpreziosi (Arezzo) | Italpreziosi SpA | goud-recupero en ruw goud → LBMA Good Delivery-staven | geen capaciteit gepubliceerd; omzet 2025 EUR 5,9 mld [1] | [1][5] |
| Valcambi (Balerna) | Valcambi SA (Rajesh Exports) | goud → LBMA-baren | nameplate ca 2.000 t/j (v1-register / sitelaag) | [9][10] |

## 6 · Stoppunt
Brief stopt bij Valcambi: geen bron noemt een raffinaderij of stad in Zwitserland [4]; Valcambi is aannemelijk als Ticino-cluster-ontvanger. Fase D (afnemer van de baren) en E vervallen.

## 7 · Open punten
- **Valcambi als ontvanger niet gebrond**: Il Sole 24 Ore noemt alleen "Zwitserland" [4]; Chimet levert primair aan Zwitserse banken [1]. Ontvanger kan ook Argor-Heraeus, PAMP, Metalor of een bank/kluis zijn (naam in de beennaam: aannemelijk, één bron voor Zwitserland).
- **Exacte Arezzo-site**: Italpreziosi gekozen (Good Delivery, adres en OSM-punt bevestigd [5][6]); Chimet en Tca zijn andere baarproducenten in dezelfde stroom [1], niet gelegd.
- **Geen Zwitserland-specifiek tonnage**: Zwitserse douane-set "Goldimporte nach Ländern" [11] gaf bij ophalen een 403; eerst daar controleren (Italië 2025), dan het volume bijstellen. Het cijfer ca 110 t is een eigen omrekening van een euro-waarde met een aangenomen prijs (±15%).
- **Sieradenschroot niet gebrond**: de jewelry-export naar Zwitserland (EUR 515 mln in Q1 2026 [3]) is een andere, kleinere stroom en niet getekend.
- **Wegkm is OSRM over OSM**, dezelfde bron als onze extract: de ±15%-toets (428 km) is dus een indicatie, geen onafhankelijke controle. Corridor gedeeld met `goud-valcambi-londen` b1 (A9/A8, omgekeerde richting): geen kopie nodig.

## 8 · Bronnen
[1] Il Sole 24 Ore (EN), 29-08-2026, "The district's new lease of life": Arezzo-baarexport 2025 bijna EUR 11 mld (+128%), Q1 2026 >EUR 6 mld; Italpreziosi, Chimet, Tca, Safimet; Chimet levert primair aan Zwitserse banken. https://en.ilsole24ore.com/art/arezzo-etruscan-jewellery-a-leading-exporter-of-ingots-AJySJgx
[2] La Nazione, Q1 2026: export prov. Arezzo EUR 7,574 mld, edelmetalen bijna EUR 6,1 mld (+237,7%), ca 80% van de provinciale export. https://www.lanazione.it/arezzo/cronaca/lexport-della-provincia-di-arezzo-nel-primo-trimestre-2026-7-miliardi-e-574-milioni-di-euro-ety5101q
[3] Teleborsa, 08-07-2026: Zwitserland weer eerste afzetmarkt voor Italiaanse gouden juwelen, EUR 515 mln Q1 2026 (juwelen, niet de baarstroom). https://www.teleborsa.it/News/2026/07/08/gioielli-in-oro-export-italiano-in-calo-nel-1-trimestre-svizzera-torna-primo-mercato-di-sbocco-145.html
[4] Il Sole 24 Ore (EN), juni 2026, "Tuscany wins silver medal for exports thanks to Arezzo gold": edelmetaalexport Arezzo naar Zwitserland Q1 2026 bijna vertienvoudigd (zonder raffinaderij of stad; zie ook haalbaarheidstoets: EUR 485 mln naar >4 mld). https://en.ilsole24ore.com/art/tuscany-wins-silver-medal-for-exports-thanks-to-arezzo-gold-AI5Q3yhD
[5] Italpreziosi, bedrijfssite: Good Delivery, raffinage goud/zilver/PGM, Strada A 32, San Zeno, Arezzo. https://www.italpreziosi.it/
[6] OpenStreetMap/Nominatim (ODbL), node 5373676912 ItalPreziosi, Strada B, Zona Industriale San Zeno, 43.4290135/11.8332671. https://www.openstreetmap.org/node/5373676912
[7] OSRM (OSM-routing), Arezzo 43.4290,11.8333 → Balerna 45.8385,9.0051: 427,8 km, 4,6 uur, A1/A1var/A50/A8/A9; stappen 28-10-2026. https://router.project-osrm.org/
[8] Eigen briefs `goud-loulo-ticino.md` en `goud-valcambi-londen.md` (M31 golf 3): anker `au-ref-valcambi` 45.8385/9.0051, OSM-building Valcambi SA.
[9] Wikipedia, "Valcambi": raffinaderij in Balerna, onderdeel van Rajesh Exports. https://en.wikipedia.org/wiki/Valcambi
[10] `data/goud.js` en `v2/design/goud-sitelaag.json` (v1/sitelaag): Valcambi cap. ca 2.000 t/j; v1-flow au-rec-italie → au-ref-valcambi 120 t (niet geverifieerd).
[11] Zwitserse douane via opendata.swiss, "Goldimporte nach Ländern" (niet bereikt, 403). https://ckan.opendata.swiss/it/dataset/7181c320-0456-4609-a353-a63044225a38
Satellietblik: `v2/build-cache/satcheck/sat-goud-arezzo-valcambi-italpreziosi.png` (z15) en `…-italpreziosi-z16.png` (z16), Esri, 2026-10-28.

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
**Bestand:** `v2/data/stroomroute-goud-arezzo-valcambi.json` (71,1 KB, versie 2, lonlat) · functie `bak_goud_arezzo_valcambi` in `v2/tools/bak_stromen.sh` · profiel `goud-arezzo-valcambi-arezzo-valcambi` in `v2/tools/maak_stroombeen_weg.py` · tussenuitvoer `v2/build-cache/ais/graaf/goud-arezzo-valcambi-weg-arezzo-valcambi.geojson`.

| # | modaliteit | been | km | naad | stippel |
|---|---|---|---|---|---|
| 1 | truck | Italpreziosi, Arezzo → Valcambi, Balerna (A1 Variante di Valico → A50 Milaan-West → A8/A9 → Chiasso; aannemelijk: één bron voor Zwitserland, Valcambi niet gebrond; 428 wegkm = OSRM-indicatie) | 430,1 | n.v.t. | nee, doorgetrokken |

Totaal 430,1 km · 3.695 punten · 2 markers (`au-arezzo-italpreziosi`, `au-ref-valcambi`), beide 0,0 km van de lijn.

**Recept.** Eén wegprofiel, 9 via-punten (2 ankers + 7 uit §4, letterlijk), extracts italie + zwitserland, refs A1/A50/A8/A9, vensterKm 40, gepubliceerdKm 428. Scan met `wegscan_puur.py` (italie 528 s, weg-slot + reus-slot), daarna `bak_stromen.sh goud-arezzo-valcambi` (geen router: vooraf gebakken lijn). Geen zee, lucht, leiding, haven-aanloop, stippel of kopie.

**Toets.** Lengte 430,1 km tegen 428 = +0,5% (OK), maar 428 is OSRM over OSM, dezelfde bron als onze extract: indicatie, geen onafhankelijke controle. Alle 8 via-snaps ≤ 0,05 km. Anker-verbindingen 0,05 km (plant → weg) en 0,01 km (weg → kade); first mile 3,7 km over kleine klassen (residential/service/unclassified), last mile 0,06 km. Segmentkm: Arezzo-anker → A1-oprit 6,7 · → Variante 102,3 · → Parma 157,8 · → Piacenza 47,2 · → A50 70,9 · → Lainate 21,4 · → Chiasso 25,5 · → Balerna 9,6. 43 keerlussen gesnoeid (441,4 → 430,1 km).

**Bevindingen.** (1) `toets_knikken`: 6 knikken ≥ 60°, 0 terugloop; een omkering van 176° (R 12 m) bij 43,9836 / 11,2110, de aansluiting van de oude A1 op de Variante di Valico bij Barberino di Mugello, ongeveer 1 km lokale lus; geen via-punt verplaatst. De overige knikken zijn spikes van ≤ 0,05 km bij 45,838 / 9,033 (afrit Chiasso/Balerna) en bij 43,985 / 11,211. (2) `toets_rechte_benen`: geen melding voor dit been. (3) Segment Variante → Parma (157,8 km) is 1,34 × hemelsbreed (A1 via Bologna, de corridor zelf), geen omweg door een via-punt.

**Niet veranderd t.o.v. het ontwerp.** Geen afwijkingen: het eindpunt (Valcambi, Balerna) is het werkelijke eindpunt. Open punten uit §7 blijven staan (Valcambi niet gebrond, geen Zwitserland-tonnage, wegkm is OSRM-indicatie, Chimet/Tca niet gelegd).

**Lessen.** Italie (2,2 GB pbf) kost ± 9 minuten scan op één kern; een tweede run met hetzelfde profiel is meteen klaar uit de cache. Profielbestand `maak_stroombeen_weg.py` is CRLF (7.600 regels), `bak_stromen.sh` LF: invoegen via een Python-script dat de regeleinden van het doelbestand behoudt.
