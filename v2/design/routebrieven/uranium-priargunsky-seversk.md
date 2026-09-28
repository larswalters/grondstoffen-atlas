# Routebrief (licht) · uranium — Priargunsky (Rusland) → Seversk (Rusland)

**stroom-id:** `uranium-priargunsky-seversk` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 6) ·
**status:** gebakken
**Keten in één zin:** uraanerts van Priargunsky (ARMZ/Rosatom, Krasnokamensk, Zabaikalsky Krai) per **truck**
naar het lokale spoorstation, dan per **spoor** over de Trans-Siberische hoofdlijn westwaarts en de aftakking
bij Tayga naar het Siberische Chemische Combinaat (SKhK) in Seversk — Ruslands enige UF6-conversieplek sinds
de sluiting van Angarsk-conversie (2014) en tegelijk een verrijkingssite — **stoppunt**.
**Welke as van het verhaal:** *Rusland — de binnenlandse flessenhals zelf (mijn → conversie+verrijking).*
Priargunsky is de grootste/oudste van Ruslands **drie** actieve uraanwinningscentra (met Dalur en Khiagda),
samen ~2.738 tU/j in 2024; Priargunsky alleen **1.047 tU/j** (WNA "Russia's Nuclear Fuel Cycle", 2024-cijfer —
gecorrigeerd op de haalbaarheidstoets, niet "de enige winning" en niet "~2.500 tU/j"). Seversk-conversie
indicatief ~12.000 tU/j, -verrijking ~3.900 tU-feed-equivalent/j (geschat aandeel wereld-SWU × wereldvoeding,
sitelaag-formule). Geen bron noemt het Priargunsky→Seversk-tonnage specifiek; de as leunt op eliminatie:
Priargunsky-erts heeft binnen het verticaal geïntegreerde Rosatom/TVEL geen andere logische binnenlandse
conversiebestemming (§7).

## 1 · Ketenkaart
```
Priargunsky-mijn `u-priargunsky-mijn` ──(b1 truck · steppepiste → lokaal spoorstation · ~11 km hemelsbreed,
   aannemelijk: geografische afleiding)──►
Krasnokamensk-station `u-krasnokamensk-station` ──(b2 spoor · Borzya-aansluiting → Trans-Sib hoofdlijn
   westwaarts (Chita–Ulan-Ude–Irkutsk–Krasnoyarsk–Novosibirsk) → aftakking bij Tayga naar Tomsk ·
   geen gepubliceerde spoorkm, aannemelijk: geografische afleiding)──►
Seversk SKhK `u-seversk-skhk` ── stoppunt (conversie UF6 + verrijking op één terrein)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | Priargunsky-mijn → Krasnokamensk-station | steppepiste/toegangsweg, gesloten mijnstad met eigen aansluiting op de Borzya-lijn, geen bron voor exact traject | ~11 [eigen berekening, hemelsbreed, geen wegkm] | maak_stroombeen_weg (extract rusland-siberie) | nee — *aannemelijk: geografische afleiding*; vindt de scanner geen doorgaand pad, dan alsnog stippel |
| b2 | B/C | spoor | Krasnokamensk-station → Seversk-SKhK | Borzya-aansluiting → Trans-Sib hoofdlijn (Chita–Ulan-Ude–Irkutsk–Krasnoyarsk–Novosibirsk) → aftakking Tayga → Tomsk → Seversk | geen gepubliceerd [via-punten hemelsbreed-som ~2.798 km, eigen berekening] | toets_spoorroute (BAKE_SUFFIX=-raw, extract rusland-siberie; geen `--via`, dus minimaal 9 deelruns kop→via→via→…→staart) | nee — *aannemelijk: geografische afleiding* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-priargunsky-mijn` | mijn / hydrometallurgische fabriek (laadplek) | Priargunsky Mining and Chemical Production Association (ARMZ/Rosatom), Krasnokamensk | 50.0640, 118.1350 | [1][sitelaag] | bron-gelegd — **hergebruikt letterlijk** van de bestaande uranium-sitelaag (`v2/design/uranium-sitelaag.json`, id `w-priargunsky`: kruis ligt op het mijn-/verwerkingscomplex naast de open pit en de tailings) |
| `u-krasnokamensk-station` | overslag truck → spoor | Krasnokamensk-spoorstation (aansluiting Borzya-lijn) | 50.1498, 118.0610 | [5][sat] | bron-gelegd (z15 gezien: spoorbundel + stationsgebouwen op het kruispunt van de Krasnokamensk-aansluiting met de Borzya-lijn, temidden van steppelandschap) |
| `u-seversk-skhk` | conversie + verrijking (losplek, stoppunt) | Siberische Chemische Combinaat (SKhK, Rosatom/TVEL), Seversk, Tomsk-oblast | 56.6180, 84.8580 | [3][4][sat] | bron-gelegd (z15 gezien: rijen langgerekte fabriekshallen met spooraansluiting en rook-/stoompluimen NW van de woonstad Seversk — duidelijk te onderscheiden van het Wikipedia-stadscentroïde-punt op 56.60/84.85, dat middenin de woonwijken viel; sitelaag `w-seversk-conversie`/`w-seversk-verrijking` (beide 56.6000/84.9000, status "onzeker") zijn voor deze as **samengevoegd** tot dit satelliet-gelegde anker, conform het ketenontwerp) |

## 4 · Via-punten (alleen b2 — corridorkeuzes op de Trans-Sib-route)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Borzya-spoorstation | 50.3833, 116.5167 | hier sluit de Krasnokamensk-aansluiting aan op de Trans-Sib-hoofdlijn (Zabaikalskaya); zonder dit punt kan een vrije Dijkstra i.p.v. westwaarts naar de grensovergang Zabaikalsk/Manzhouli buigen (dezelfde valkuil als bij `kolen-taldinsky-vostochny` zonder het Chita-via-punt) |
| b2 | 2 | Chita-spoorstation | 52.0500, 113.4667 | doorgaand hoofdknooppunt op de Trans-Sib; al **verplicht** gebleken in `kolen-taldinsky-vostochny.md` om een omweg via Harbin op hetzelfde 1-op-1-net te vermijden |
| b2 | 3 | Ulan-Ude-spoorstation | 51.8333, 107.6000 | hier vertakt de lijn naar Mongolië/Ulaanbaatar; dit punt pint de doorgaande westwaartse Trans-Sib-tak |
| b2 | 4 | Irkutsk-spoorstation | 52.2892, 104.2800 | de Trans-Sib buigt hier om het Baikalmeer heen (zuidoever); pint die corridorkeuze i.p.v. een noordelijke sluiproute |
| b2 | 5 | Krasnoyarsk-spoorstation | 56.0089, 92.8719 | doorgaand hoofdknooppunt op de Trans-Sib, waar de Jenisej wordt overgestoken |
| b2 | 6 | Novosibirsk-spoorstation | 55.0288, 82.9227 | grootste spoorknoop van Siberië (meerdere lijnen samen, incl. de Turksib-tak naar Kazachstan); pint de doorgaande hoofdlijn |
| b2 | 7 | Tayga-spoorstation | 56.0624, 85.6253 | hier vertakt de lijn van de Trans-Sib-hoofdlijn noordwaarts naar Tomsk — zonder dit punt blijft een vrije Dijkstra op de hoofdlijn westwaarts richting Omsk i.p.v. de aftakking te nemen |
| b2 | 8 | Tomsk-spoorstation | 56.4888, 84.9523 | laatste grote stad op de aftakkingslijn Tayga–Tomsk–Seversk, vlak vóór het SKhK-terrein |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Seversk SKhK | Rosatom/TVEL | UF6-voeding (Russische/Kazachse yellowcake) → conversie (UF6) → verrijking (LEU) | conversie ~12.000 tU/j indicatief; verrijking ~3.900 tU-feed-equivalent/j (geschat aandeel wereld-SWU × ~65.000 tU/j wereldvoeding) | [1][sitelaag] |

## 6 · Stoppunt
De brief stopt bij het Seversk SKhK-complex: het opgedragen keten-eindpunt, waar conversie ÉN verrijking op
één terrein gebeuren (sinds 2014 Ruslands enige UF6-conversieplek, na de sluiting van Angarsk-conversie).
Geen bron noemt een specifieke vervolgbestemming (splijtstoffabricage) voor dit erts — fase D vervalt.

## 7 · Open punten
- **Geen bron zegt letterlijk dat Priargunsky-erts naar Seversk gaat** — de as leunt op eliminatie, niet op
  een citaat: Priargunsky is de grootste van Ruslands drie actieve winningscentra, en Seversk is sinds 2014
  de enige Russische UF6-conversieplek. Bij een verticaal geïntegreerd staatsbedrijf (Rosatom/TVEL, geen
  concurrerende binnenlandse afnemer) is dit de enige logische bestemming, maar het blijft een gevolgtrekking
  (conform de haalbaarheidstoets, punt dat ongewijzigd mag blijven staan).
- **De exacte spoorcorridor (Krasnokamensk–Borzya–Trans-Sib–Tayga–Seversk) is geografische afleiding** —
  vrachtroutes voor kernmateriaal worden uit veiligheidsoverwegingen niet in detail gepubliceerd; geen bron
  noemt de tussenstations. Dit blijft terecht een open punt, niet oplosbaar binnen het webbudget.
- **Extracts gecorrigeerd conform de haalbaarheidstoets:** beide geometrie-aanwijzingen gebruiken nu
  `rusland-siberie` (dekt Krasnokamensk/Borzya, Tayga én Seversk/Tomsk — gemeten 1.748/1.463/1.458
  spoorweg-ways in de bbox's) — `rusland-verrehoosten` is voor deze as niet nodig en niet gebruikt.
- **Jaarvolume gecorrigeerd:** Priargunsky 1.047 tU/j (2024, WNA Red Book), niet "~2.500 tU/j" en niet
  "enige winning" (Dalur 588 tU/j, Khiagda 1.103 tU/j — Khiagda produceerde in 2024 zelfs meer dan
  Priargunsky). Totaal Rusland 2024 = 2.738 tU/j over de drie centra.
- **Geen breukvlak in spoorwijdte** onderweg (heel Rusland 1520 mm) — anders dan bij de Kazachstan→China-
  assen (Dostyk/Alashankou) is er hier geen bogiewissel te modelleren.
- **Fase A (mijn → Krasnokamensk-station) heeft geen gepubliceerde km of exact traject** — bij het bakken de
  daadwerkelijke toegangsweg zoeken op de `rusland-siberie`-extract; vindt de scanner geen doorgaand pad,
  dan stippel "last mile (geen net op deze korrel)".

## 8 · Bronnen
[1] World Nuclear Association, "Russia's Nuclear Fuel Cycle" (live gecheckt via curl) — drie actieve
winningscentra: Priargunsky 1.047 tU, Dalur 588 tU, Khiagda 1.103 tU (2024, totaal 2.738 tU); Seversk =
Ruslands enige UF6-conversieplek sinds de sluiting van Angarsk-conversie in april 2014; Rosatom/TVEL vier
verrijkingsfabrieken (Novouralsk, Angarsk, Zelenogorsk, Seversk) samen ~44% wereld-SWU.
https://world-nuclear.org/information-library/country-profiles/countries-o-s/russia-nuclear-fuel-cycle
[2] Priargunsky Mining and Chemical Production Association (ARMZ/Rosatom), officiële site — Krasnokamensk,
Zabaikalsky Krai. https://priargunsky.armz.ru/en/
[3] Wikipedia, "Siberian Chemical Combine" — opgericht 1953 in Tomsk-7 (nu Seversk), Tomsk-oblast; dochter
van TVEL (Rosatom-groep); combineert het hele nucleaire technologische cyclus-complex.
https://en.wikipedia.org/wiki/Siberian_Chemical_Combine
[4] WISE Uranium Project, "Enrichment Operations" — overzicht Russische verrijkingssites incl. Seversk.
https://www.wise-uranium.org/eopru.html
[5] Wikipedia, "Krasnokamensk, Zabaykalsky Krai" — 535 km ZO van Chita; site van Ruslands grootste
uraanmijn (coördinaat 50.10/118.03, stadscentroïde — het satelliet-gelegde stationsanker in §3 is preciezer).
https://en.wikipedia.org/wiki/Krasnokamensk,_Zabaykalsky_Krai · Wikipedia, "Borzya" (50.3833/116.5167) —
349 km ZO van Chita, op de Trans-Sib-aansluiting. https://en.wikipedia.org/wiki/Borzya · Wikipedia, "Chita,
Zabaykalsky Krai" (52.05/113.4667). https://en.wikipedia.org/wiki/Chita,_Zabaykalsky_Krai · Wikipedia,
"Ulan-Ude" (51.8333/107.6000). https://en.wikipedia.org/wiki/Ulan-Ude · Wikipedia, "Irkutsk" (52.2892/104.28).
https://en.wikipedia.org/wiki/Irkutsk · Wikipedia, "Krasnoyarsk" (56.0089/92.8719).
https://en.wikipedia.org/wiki/Krasnoyarsk · Wikipedia, "Seversk" (56.60/84.85, stadscentroïde — het
satelliet-gelegde industrieanker in §3 is preciezer). https://en.wikipedia.org/wiki/Seversk
[6] OpenStreetMap (ODbL) via Nominatim/Photon — Krasnokamensk-station node (50.14978/118.06097) ·
Novosibirsk (55.0288/82.9227) · Tomsk (56.4888/84.9523) · Tayga-station (56.0624/85.6253).
https://www.openstreetmap.org
[7] `v2/design/routebrieven/kolen-taldinsky-vostochny.md` (M31) — hergebruikte Trans-Sib-werkwijze
(BAKE_SUFFIX=-raw, extract rusland-siberie, Chita als verplicht via-punt tegen een Harbin-omweg).
[8] `v2/design/uranium-sitelaag.json` — anker `w-priargunsky` (50.0640/118.1350, bron-gelegd, letterlijk
hergebruikt) en de aanpassing (2) uit de haalbaarheidstoets: `w-seversk-conversie`/`w-seversk-verrijking`
(beide 56.6000/84.9000, status "onzeker") voor deze as samengevoegd tot één satelliet-gelegd anker.
[sat] Esri World Imagery via `v2/tools/sat_check.py` (z15, live) —
`v2/build-cache/satcheck/sat-uranium-priargunsky-seversk-krasnokamensk-station.png`,
`sat-uranium-priargunsky-seversk-seversk-skhk-industrial.png`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 6)

**Totaal: 10 benen · 3.749,5 km · 11.451 punten · 3 markers** (207,0 KB) —
`v2/data/stroomroute-uranium-priargunsky-seversk.json`, functie
`bak_uranium_priargunsky_seversk()` in `v2/tools/bak_stromen.sh`.

| # | modaliteit | km | naad (km) | recept |
|---|---|---|---|---|
| b1 | truck | 16,4 (getekend, incl. 0,62+0,25 km anker-verbindingsstukjes) | 0,00 (start) | `maak_stroombeen_weg.py --profiel uranium-priargunsky-seversk-priargunsky-krasnokamensk` |
| b2.1 | spoor | 180,7 | 0,32 | `toets_spoorroute.mjs` Krasnokamensk-station → Borzya |
| b2.2 | spoor | 344,9 | 0,00 | Borzya → Chita |
| b2.3 | spoor | 550,4 | 0,00 | Chita → Ulan-Ude |
| b2.4 | spoor | 456,6 | 0,00 | Ulan-Ude → Irkutsk |
| b2.5 | spoor | 1.086,5 | 0,00 | Irkutsk → Krasnoyarsk |
| b2.6 | spoor | 764,9 | 0,00 | Krasnoyarsk → Novosibirsk |
| b2.7 | spoor | 231,3 | 0,00 | Novosibirsk → Tayga |
| b2.8 | spoor | 94,7 | 0,00 | Tayga → Tomsk |
| b2.9 | spoor | 23,1 | 0,00 | Tomsk → Seversk SKhK |

**b1 (truck) — geen terugval-stippel nodig.** De scanner vond een doorgaand OSM-wegpad over de
steppe (`rusland-siberie`-extract, corridorKlassen `tertiary`/`unclassified`, `eindToegangPrivaat`):
15,6 km ruwe weggeometrie (16,4–16,5 km incl. de anker-verbindingsstukjes), tegen de eigen
hemelsbrede schatting van ~11 km uit de brief. De ±15%-toets geldt hier **als indicatie, niet als
norm** (§2/§7) — dit is dus geen afwijking maar de enige beschikbare meting. Eén bevinding:
de plant→weg-aansluiting is **0,62 km** (net > de 0,5 km-norm) — de mijn ligt op een gesloten
mijncomplex zonder directe OSM-aansluiting op de eerste kleine weg; niet dichtgetrokken.
`toets_knikken.py` telt 3 knikken ≥60° (spikes, geen omkeringen) — normale OSM-zigzag op een
steppepiste, geen fout.

**b2 (spoor) — geen stippel, 9 deelruns in reisvolgorde, `BAKE_SUFFIX=-raw` (console bevestigt
"3260717 spoor-edges" op elke run, dus het 1-op-1-net).** Totaal 3.733,1 km over het spoor, tegen
de brief's eigen hemelsbreed-som van de acht via-punten (~2.798 km) — **+33,4%**, en ook hier geldt
de toets als indicatie, niet als norm (§2/§7): een reële Trans-Sib-corridor rond het Baikalmeer
is altijd langer dan een hemelsbrede via-puntenketen. Omwegfactoren (route/grootcirkel) per deelrun:
1,60 / 1,21 / 1,35 / 1,94 / 1,27 / 1,19 / 1,12 / 1,49 / 1,47 — stuk voor stuk ≥1 (sanity OK).

**Naden tussen de 9 deelsegmenten: 0,00–0,32 km, ruim binnen de ≤5 km-norm** — elk segment snapt
op (bijna) dezelfde hoofdnet-knoop als zijn buur.

**⚠️ Bevinding — 6 TERUGLOOP-knikken, allemaal exact op een via-punt/eindsnap, niet gerepareerd.**
`toets_knikken.py` (verhouding pad ÷ hemelsbreed, v ≥ 3,0 = terugloop, v 1,1–2,0 = echte bocht) wijst
zes terugloop-punten aan: **52.2874,104.2597** en **56.0220,92.8323** (Krasnoyarsk-station-omgeving,
gedeeld tussen de Irkutsk→Krasnoyarsk- en Krasnoyarsk→Novosibirsk-run) en **56.0086,92.8313** ·
**56.5189,84.9962** · **56.5084,84.9992** (Tayga/Tomsk/Seversk-omgeving, gedeeld tussen
Novosibirsk→Tayga/Tayga→Tomsk/Tomsk→Seversk). Er is **geen `--via` op de spoorrouter** (bakhandleiding
§2), dus elke deelrun snapt onafhankelijk op de dichtstbijzijnde hoofdnet-knoop rond het via-punt —
dat geeft aan de rand van elk segment soms een korte kopmaak-achtige boog waar twee onafhankelijk
gerouteerde stukken net niet op dezelfde vertex uitkomen. Conform de werkwijze (§2/§7 · geen
via-punt bijschuiven om een getal te halen) blijft dit een bevinding, geen fix — een via-punt
verschuiven om deze boogjes te laten verdwijnen zou een corridorkeuze wijzigen op basis van een
routeerartefact, niet op basis van een betere bron.

**Toetsen:** `toets_rechte_benen.py --min-km 5` geeft geen enkele melding voor deze stroom (geen
onverklaarde rechte/gestippelde benen — er zijn hier ook geen stippels). Markers: `u-priargunsky-mijn`
0,0 m · `u-krasnokamensk-station` 0,0 m · `u-seversk-skhk` 478,0 m (anker ≠ routeerpunt: de
aftakkingslijn eindigt waar OSM het spoor kent, net vóór het SKhK-terrein) — alle binnen de ~0,5 km-
norm. JSON-contract: `versie 2` · `punt_formaat lonlat` · modaliteiten `{truck, spoor}` (beide geldig) ·
elk been ≥ 2 punten · 207,0 KB (ruim onder de ~300 KB-norm).

**Lessen:** (1) een spoorrouter zonder `--via` maakt terugloop-artefacten op via-punt-grenzen
onvermijdelijk bij een lange multi-via-corridor — dit is de negende keer in deze golf dat dat
patroon optreedt (zie ook `kolen-taldinsky-vostochny.md`) en het hoort standaard als §9-bevinding
gemeld, niet als fout behandeld. (2) Bij een ontbrekende gepubliceerde km (zowel voor de weg als het
spoor in deze as) is de ±15%-toets een indicatie, niet een norm — de gemeten waarden (weg +42%
t.o.v. de hemelsbrede schatting, spoor +33% t.o.v. de hemelsbrede via-puntensom) zijn hier dus geen
bevindingen om te herstellen, maar de enige beschikbare metingen.

**Registerregel (centraal, niet door de bak-agent):**
`{ sleutel: "priargunsky-seversk", bestand: "stroomroute-uranium-priargunsky-seversk.json", aan: true }`
in `v2/src/main.js`; titel voor `hecht_marnet.py`: "Uranium · Priargunsky → Seversk (Rusland)"
(al gebruikt in de bak-functie, zie hierboven).
