# Routebrief (licht) · uranium — Orano Tricastin (Frankrijk) → Le Havre → Sint-Petersburg → Seversk (Rusland)

**stroom-id:** `uranium-tricastin-seversk` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) ·
**status:** gebakken
**Keten in één zin:** Frans opgewerkt uranium (RepU) uit de opslag van Orano Tricastin (Pierrelatte) gaat per **spoor**
naar Le Havre, per **zeeschip** door het Kanaal, de Deense Straten en de Oostzee naar Sint-Petersburg (Petrolesport) en
per **spoor** over de Oktjabrskaja- en Trans-Sib-noordroute naar het Siberische Chemische Combinaat (SKhK) in Seversk,
waar RepU wordt geconverteerd en herverrijkt — **stoppunt**.
**Welke as van het verhaal:** *Recycling/herverwerking: de Franse RepU-berg die alleen in Rusland tot splijtstof wordt.* Geen
jaarcijfer gepubliceerd: Orano verkocht eind 2020 "just over 1.000 t" RepU aan Rosatom, in meerdere zendingen (Orano-e-mail
24-02-2021, geciteerd in [1]); zending 12-02-2021 = 11 containers [1]; 28-09-2022 en 15-11-2025 elk "dozens of containers" [2].
Opslag Tricastin 33.000 t (Andra 2021 [1]) resp. 35.000 t (2026 [2]), groeit ~1.000-1.100 t/j. Eenheid t RepU (U-inhoud niet
gespecificeerd), peiljaar 2020-2025.

## 1 · Ketenkaart
```
Orano Tricastin `u-tricastin` ──(b1 spoor · Rhône-corridor Lyon–Dijon–Laroche-Migennes–Parijs-zuidoost–Mantes–Rouen ·
   hemelsbreed 667 km, geen spoorkm · aannemelijk: trein Pierrelatte→Le Havre waargenomen 12-02-2021 [1])──►
Le Havre-kade `u-lehavre-kade` ──(b2 haven-aanloop, stippel, 5,4 km)──(b3 zee · ~2.770 km MARNET · 2021-route)──►
Sint-Petersburg-kade `u-stpetersburg-kade` ──(b4 spoor · Moskou–Kirov–Perm–Jekaterinenburg–Tyumen–Omsk–Novosibirsk–Tayga–Tomsk ·
   hemelsbreed 3.124 km, geen spoorkm · aannemelijk: geografische afleiding)──► Seversk SKhK `u-seversk-skhk` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | spoor | Tricastin → Le Havre-kade | Rhône (Lyon) → Dijon → Laroche-Migennes → Villeneuve-St-Georges → Mantes → Rouen → Le Havre | hemelsbreed 667 km, geen spoorkm; gemeten 976,7 (7 runs) | toets_spoorroute (7 runs) | nee — *aannemelijk: één bron (Greenpeace-waarneming)* |
| b2 | B | zee | haven-aanloop Le Havre (kade → zeeknoop 3956) | Port 2000 → open water | 5,4 [eigen meting] | rechte stippel (maak_havenaanloop hing > 300 s) | **ja — schematisch, kruist de zuiderdijk** |
| b3 | B | zee | Le Havre → Sint-Petersburg | Kanaal, Noordzee, Skagerrak/Kattegat, Deense Straten, Oostzee, Finse Golf | grootcirkel 2.226; MARNET 2.770 (knoop → knoop); geen gepubliceerde zeekm | MARNET | aanloop Le Havre ja (b2); SPb 4,9 km, nee |
| b4 | C | spoor | Sint-Petersburg-kade → Seversk | Oktjabrskaja (Moskou) → Kirov → Perm → Jekaterinenburg → Tyumen → Omsk → Novosibirsk → Tayga → Tomsk | hemelsbreed 3.124 km, geen spoorkm; gemeten 4.267,5 (7 runs + 3 kopieën) | toets_spoorroute + letterlijke kopie priargunsky b8-b10 | nee — *aannemelijk: geografische afleiding* |

**Le Havre (2021-route met waargenomen trein):** de twee latere RepU-zendingen (28-09-2022, 15-11-2025) zijn in **Duinkerken** geladen [2];
de modaliteit Pierrelatte → Duinkerken is niet gedocumenteerd, dus b1/b3 volgen de enige gedocumenteerde treinroute (Le Havre).

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-tricastin` | opslag RepU (kop) | Orano Tricastin, Pierrelatte, Drôme | 44.3250, 4.7167 | letterlijk uit `uranium-malvesi-tricastin.md` / `uranium-tricastin-romans.md` [10] | bron-gelegd (eerder gezien: kruis in het industriecomplex tussen spoor/A7 en het Donzère-Mondragon-kanaal); opslaghal zelf niet apart aangewezen |
| `u-lehavre-kade` | overslag spoor → zee | Port 2000, kade voor Terminal Porte Océane (OSM 49.4611, 0.1548), Le Havre | 49.4580, 0.1619 | eigen keuze [3][4]; **geen bron noemt de kade** | **onzeker** (z16 gezien: containerkade met portaalkranen, een schip langszij en een spoorbundel direct achter het stapelveld; of juist deze terminal is gebruikt is niet bekend) |
| `u-stpetersburg-kade` | overslag zee → spoor | Petrolesport, Gutujevski-eiland, Sint-Petersburg | 59.8909, 30.2376 | letterlijk uit `uranium-inkai-stpetersburg.md` [10] | bron-gelegd (eerder z15 gezien: containerstapels, kranen, spoorbundel aan de landzijde); geen nucleair adres bekend |
| `u-seversk-skhk` | conversie + verrijking (stoppunt) | SKhK (Rosatom/TVEL), Seversk | 56.6180, 84.8580 | letterlijk uit `uranium-priargunsky-seversk.md` [10] | bron-gelegd (eerder z15 gezien: fabriekshallen met spooraansluiting en pluimen NW van de stad) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze; punten op de lijn/het station, niet in een centrum)
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | Lyon | 45.7206, 4.9047 | houdt de Rhône-lijn aan i.p.v. Mâcon-omweg; snapt 2,1 km |
| b1 | 2 | Dijon-Ville | 47.3234, 5.0270 | pint Dijon–Laroche i.p.v. de lijn via Parijs-Lyon |
| b1 | 3 | Laroche-Migennes | 47.9611, 3.5130 | pint de Yonne-lijn (station fr.wikipedia; een gegokt punt 5 km ernaast was fout) [5] |
| b1 | 4 | Villeneuve-Saint-Georges | 48.7330, 2.4490 | vrachtroute ten zuidoosten van Parijs, niet door het centrum [5] |
| b1 | 5 | Mantes-la-Jolie | 48.9897, 1.7033 | zonder dit punt rijdt de router via Creil/Serqueux met 4 omkeringen |
| b1 | 6 | Rouen-Rive-Droite | 49.4490, 1.0941 | pint Rouen–Le Havre; eindpunt b1 = kade (snap 0,5 km) |
| b4 | 1 | Moskou-Yaroslavsky | 55.7761, 37.6573 | knoop tussen SPb-lijn en de oostwaartse hoofdlijn (run SPb→Moskou, juiste richting; geometrisch dezelfde corridor als `uranium-inkai-stpetersburg` b6, omgekeerd) |
| b4 | 2 | Kirov | 58.6036, 49.6680 | corridorkeuze noordroute Kirov–Perm (de router kiest Nizhny Novgorod, niet Yaroslavl) |
| b4 | 3 | Perm | 58.0105, 56.2502 | pint de Oeral-oversteek |
| b4 | 4 | Jekaterinenburg | 56.8356, 60.6128 | hoofdknoop Oeral |
| b4 | 5 | Tyumen-station | 57.1450, 65.5225 | **toegevoegd**: zonder dit punt rijdt de router via Kurgan (162 km zuidelijker); noordroute is 883,6 km tegen 887,8 km [6][7] |
| b4 | 6 | Omsk-Passazhirsky | 54.9396, 73.3866 | stationspunt; de stadscentroïde 54.9885, 73.3242 snapte 4,6 km weg [7] |
| b4 | 7 | Novosibirsk (router-knoop) | 55.0186, 82.9207 | eindpunt van `priargunsky` b7; vanaf hier letterlijke kopieën (Tayga 56.0624, 85.6253 en Tomsk 56.4888, 84.9523 zitten in die geojsons) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Orano Tricastin (RepU-opslag) | Orano | opgewerkt uranium uit La Hague → opslag in hangars | stock 33.000-35.000 t, +1.000-1.100 t/j | [1][2] |
| Seversk SKhK | Rosatom/TVEL | RepU → conversie → herverrijking (verwerkt natuurlijk én opgewerkt uranium) | conversie ~12.000 t U/j, verrijking ~3.900 t U voeding-eq./j (indicatief, sitelaag) | [8][10] |

## 6 · Stoppunt
De brief stopt bij SKhK Seversk: het opgedragen eindpunt en de enige plek die een bron noemt voor de verwerking van deze
lading [1]. Terugvoer van verrijkt RepU naar Cruas-Meysse (EDF-Tenex 2018 [1]) is als afspraak gedocumenteerd, niet als route:
niet getekend. Fase D/E vervallen.

## 7 · Open punten
- **Le Havre-kade niet gepubliceerd** (geen terminalnaam in [1][2][3][4]); Port 2000 (TPO) is een eigen keuze: onzeker.
- **Laatste twee zendingen via Duinkerken** [2]; Pierrelatte → Duinkerken niet gedocumenteerd, niet getekend.
- **Haven-aanloop Le Havre schematisch:** kade ligt 5,4 km van MARNET-zeeknoop 3956 (49.4228, 0.1107, zuid van de zuiderdijk);
  `maak_havenaanloop.py` gaf na 300 s geen pad, dus rechte stippel die de dijk kruist (de echte weg loopt westwaarts om de dijk).
- **Spoor Rouen → Le Havre-kade 120,4 km, met een router-omkering bij Le Havre station** (liever ~87 km tot het station): de
  1-op-1-graaf bereikt Port 2000 alleen langs het station en keert dan terug; keerstraf 100/300 verandert niets. Niet bijgeschoven.
- **Geen spoorkm gepubliceerd** (b1 hemelsbreed 667 km, b4 3.124 km); de ±15%-toets is alleen indicatie. Gemeten 976,7 resp. 4.267,5 km.
- **Spoor Sint-Petersburg → Seversk is geografische afleiding**; geen bron noemt de route [1].
- **Sint-Petersburg-kade 4,9 km van zeeknoop 6849:** net onder de 5 km-grens, geen marge; kade niet als nucleair ladingpunt bevestigd.
- **Bijna al het bewijs is Greenpeace-waarneming**; erkend door Orano per e-mail [1]; scheepsnaam verschilt per bron (Mikhail Lomonosov [1] / Kapitan Lomonosov [9]).
- **"Enige plek die RepU converteert" is te sterk:** WNA noemt ook Elektrostal (700 t/j RepU-capaciteit, uit VVER-440) [8].
- **Politiek:** Franse overheid blokkeerde RepU-export 2022-2025; EU-sancties; zending nov. 2025 hervatte het verkeer [2].

## 8 · Bronnen
[1] Greenpeace France, "French nuclear waste: a one-way ticket to Siberia", 12-10-2021 (Le Havre 20-01/12-02-2021, trein uit Pierrelatte, Orano-citaat, 33.000 t). https://cdn.greenpeace.fr/site/uploads/2021/10/French-nuclear-waste-_-a-one-way-ticket-to-Siberia-_-Briefing-Greenpeace-France-Embargo-12-10-2021.pdf
[2] Greenpeace France, "France-Russia: radioactive trafficking continues", jan. 2026 (Duinkerken 28-09-2022 en 15-11-2025, 35.000 t). https://cdn.greenpeace.fr/site/uploads/2026/02/Greenpeace-investigation-France-Russia-radioactive-trafficking-continues-2026-EN.pdf
[3] Greenpeace France (FR), dossier 12-10-2021, "Déchets nucléaires français: aller simple pour la Sibérie" (zelfde waarneming, geen kade). https://cdn.greenpeace.fr/site/uploads/2021/10/Dechets-nucleaires-francais-_-aller-simple-pour-la-Siberie-_-Dossier-Greenpeace-France-embargo-12-10-2021.pdf
[4] Tendance Ouest, "Le Havre: des déchets radioactifs en transit par le port" (geen terminal; trein SPb → Seversk). https://www.tendanceouest.com/actualite-388974-le-havre-des-dechets-radioactifs-en-transit-par-le-port
[5] Wikipedia (fr/en, MediaWiki API) en OSM Nominatim: Gare du Havre 49.4927/0.1250, Rouen-Rive-Droite 49.4490/1.0941, Villeneuve-St-Georges 48.7299/2.4461; Laroche-Migennes 47.9611/3.5130 (via haalbaarheidstoets). https://fr.wikipedia.org/wiki/Gare_de_Villeneuve-Saint-Georges
[6] Wikipedia, "Tyumen railway station" 57.145/65.5225. https://en.wikipedia.org/wiki/Tyumen_railway_station
[7] OSM Nominatim (ODbL): Omsk-Passazhirsky 54.9396/73.3866, Tyumen 57.1455/65.5221. https://www.openstreetmap.org
[8] World Nuclear Association, "Russia's Nuclear Fuel Cycle" (SCC converteert/verrijkt natuurlijk en opgewerkt uranium; Elektrostal RepU 700 t/j). https://world-nuclear.org/information-library/country-profiles/countries-o-s/russia-nuclear-fuel-cycle
[9] Reporterre, "La France se débarrasse de déchets nucléaires en Russie" (naam Kapitan Lomonosov; pagina 403 voor curl, alleen via zoekresultaat gezien). https://reporterre.net/La-France-se-debarrasse-de-dechets-nucleaires-en-Russie
[10] Eigen briefs: `uranium-malvesi-tricastin.md`, `uranium-tricastin-romans.md`, `uranium-inkai-stpetersburg.md`, `uranium-priargunsky-seversk.md` (ankers letterlijk; geojsons b8-b10).
[11] Lloyd's List 30-10-2009, "Greenpeace blocks collection of nuclear loads at Le Havre" (historische RepU-haven; paywall, geen terminal). https://www.lloydslist.com/LL064513/Greenpeace-blocks-collection-of-nuclear-loads-at-Le-Havre
[sat] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-uranium-tricastin-seversk-lehavre-kade.png` (z16), `…-lehavre-tpo.png`, `…-lehavre-tdf.png`, `…-lehavre-tdn.png`, `…-lehavre-ingang.png` (z15).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-uranium-tricastin-seversk.json` (219,6 KB, versie 2, punt_formaat lonlat) · functie `bak_uranium_tricastin_seversk()` in
`v2/tools/bak_stromen.sh` · `bash v2/tools/bak_stromen.sh uranium-tricastin-seversk` · 19 benen · 12.695 punten · 4 markers · **totaal 8.078,3 km**
(brief: ~8.020; +0,7%). Geen profiel in `maak_stroombeen_weg.py` (geen wegbeen), geen luchtbeen, geen leiding.

| # | modaliteit | been | km (bake) | km (brief) | naad | stippel |
|---|---|---|---|---|---|---|
| 1-7 | spoor | Tricastin → Lyon 177,4 · Lyon → Dijon 210,7 · Dijon → Laroche-Migennes 152,3 · Laroche → Villeneuve-St-Georges 160,7 · Villeneuve → Mantes 89,1 · Mantes → Rouen 82,2 · Rouen → Le Havre kade 122,1 | **994,5** | 976,7 (+1,8%) | 0,00 | nee |
| 8 | zee | haven-aanloop Le Havre Port 2000 (kade → zeeknoop 3956) | 5,4 | 5,4 | 0,52 | **ja**, schematisch |
| 9 | zee | zeeschip Le Havre → Sint-Petersburg (MARNET, 52 edges, 303 punten) | 2.770,4 | 2.770,4 | 0,00 | nee |
| 10-16 | spoor | SPb → Moskou 664,5 · Moskou → Kirov 899,6 · Kirov → Perm 488,9 · Perm → Jekaterinenburg 393,5 · Jek. → Tyumen 320,1 · Tyumen → Omsk 570,7 · Omsk → Novosibirsk 621,6 | 3.958,9 | 3.918,4 | 4,74 (zee-eind zeeknoop 6849 → Petrolesport), daarna 0,00 | nee |
| 17-19 | spoor | letterlijke kopie priargunsky-seversk: Novosibirsk → Tayga 231,3 · Tayga → Tomsk 94,7 · Tomsk → Seversk 23,1 | 349,1 | 349,1 | 0,00 | nee |

Spoor b4 totaal 4.308,0 km (brief 4.267,5; +0,9%). Voor beide spoorbenen is er geen gepubliceerde spoorkm: de ±15%-toets is indicatie en wordt gehaald.
Het verschil met de brief komt doordat `hecht_marnet.py` de lengte uit de getekende polyline herrekent (haversine) i.p.v. de route-km van de spoorrouter te nemen.

**Markers (4, alle ≤ 0,5 km van hun lijn):** `u-tricastin` 0,33 km · `u-lehavre-kade` 0,00 · `u-stpetersburg-kade` 0,37 · `u-seversk-skhk` 0,48.

**Toelichting per stippel/aanloop**
- **b8 haven-aanloop Le Havre:** kade (49.4580, 0.1619) ligt 5,4 km van MARNET-zeeknoop 3956 (49.4228, 0.1107) → aanloop vereist (> 5 km). `maak_havenaanloop.py` is in deze bake
  niet opnieuw gedraaid; de brief meldt > 300 s zonder pad, dus rechte `--stippel` (schematisch, kruist de zuiderdijk van Port 2000), geen tweede poging.
- **Sint-Petersburg:** kade 4,9 km van zeeknoop 6849 (< 5 km), geen aanloop; de naad zee → spoor is 4,74 km: binnen de norm, maar zonder marge (bevinding).
- **Geen leiding, geen lucht, geen weg.** Fase D/E vervallen (stoppunt Seversk).

**Toets**
- json.load OK · versie 2 · punt_formaat lonlat · modaliteiten {spoor, zee} · elk been ≥ 2 punten · 219,6 KB.
- Naden: max 4,74 km (b9 → b10); alle andere ≤ 0,52 km.
- `toets_rechte_benen.py --min-km 5`: alleen b8 (de stippel met reden, omwegfactor 1,002).
- `toets_knikken.py`: 13 knikken ≥ 60 gr, waarvan 10 terugloop-meldingen; allemaal router-artefacten aan via-punt- of kadesnaps, niet bijgeschoven:
  Le Havre station (49.4955, 0.1375, rouen-lehavre) · SPb-begin (59.8728, 30.1949) · Moskou-Kirov / Kirov-Perm bij Kirov (58.6141, 49.6467) · Perm-Jekaterinenburg (58.0096, 56.1217) ·
  Tayga-Tomsk en Tomsk-Seversk bij Tomsk (56.5189, 84.9962; 56.5084, 84.9992; 56.6252, 84.8626 = pal vóór het SKhK-terrein). De laatste drie zitten in de letterlijk gekopieerde
  priargunsky-geojsons en zijn daar al gemeld.

**Recept (kort):** 7 spoorruns b1 en 7 spoorruns b4 met `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs` (vooraf gedraaid, tussenuitvoer
`v2/build-cache/ais/graaf/spoorroute-uranium-tricastin-seversk-*.geojson`), drie letterlijke priargunsky-geojsons, MARNET `--been zee` kade → kade, één `--stippel`
aanloop, vier `--marker`s. Gebakken via het zwaar-slot; één run, rc 0.

**Lessen**
- Het slot-script uit de opdracht (`rm -rf "$d"` met een variabele) wordt door de veiligheidscheck geweigerd; slot nemen met `mkdir` op letterlijke paden en vrijgeven met `rmdir` op een letterlijk pad werkt.
- Alle bevindingen uit §7 blijven staan: Le Havre-kade onzeker, Duinkerken niet getekend, Greenpeace als bijna enige bron, spoor SPb → Seversk is afleiding, terugvoer naar Cruas niet getekend.
- Registerregel (centraal): `{ "sleutel": "u-ts", "bestand": "stroomroute-uranium-tricastin-seversk.json", "grondstof": "uranium", "label": "Tricastin → Seversk", "aan": true, "noot": "M31 · golf 7 (2026-10-09): ..." }`.
