# Routebrief (licht) · Uranium · Sint-Petersburg (Rusland) → Baltimore → Westinghouse Columbia (South Carolina, VS)

**stroom-id:** `uranium-stpetersburg-columbia` · **geschreven:** 2026-10-28 · **werkwijze:** licht (M31 golf 10) ·
**status:** gebakken (2026-10-28)
**Keten in één zin:** Russisch verrijkt uranium (UF6 in 30B-cilinders op flatracks, Tenex/Rosatom, fabriek van herkomst onbekend) gaat per
**zeeschip** (Atlantic Ro-Ro Carriers, "Baltic Mercur" in 2005; Atlantic Navigator II in 2025) van de kade van Sint-Petersburg door de Finse Golf,
de Oostzee, de Deense Straten, de Noordzee, het Kanaal en de Atlantische Oceaan naar Baltimore en daarna per **truck** (I-95 · Capital Beltway · I-295 · I-95 ·
I-20 · I-77) naar de Westinghouse Columbia Fuel Fabrication Facility — stoppunt (splijtstoffabricage).
**Welke as van het verhaal:** *Russisch verrijkt uranium naar de VS: de leverlijn onder het importverbod.* Sinds augustus 2024 geldt een Amerikaans
importverbod met uitzonderingen; Tenex leverde 12-02-2025 toch via Baltimore. **Volume (geen jaarvolume per route):** 12-02-2025 één levering van
15 t voor Westinghouse en 85 t voor GNF [4][5]; eenheid (UF6 of U) niet vastgesteld, dus ≈ 15 t/j als indicatie van het Westinghouse-aandeel, peiljaar 2025.
Historische referentie: één zending 2005 = 7 x 30B, max netto 15.420 kg UF6 = 10.425 kg U [1]. Westinghouse Columbia zelf ≈ 1.400 t HM/j (sitelaag).

## 1 · Ketenkaart
```
Russische verrijkingsfabriek (niet gedocumenteerd) ──(trein/truck naar de haven, niet getekend)──►
Sint-Petersburg-kade `u-stpetersburg-kade` ──(b1 zee · Finse Golf, Oostzee, Deense Straten, Noordzee, Kanaal, Atlantische Oceaan · MARNET 8.415,5 km)──►
Baltimore-kade `u-baltimore-kade` ──(b2 truck · I-95 · I-495 · I-295 · I-95 · I-20 · I-77 · hemelsbreed 713 km, geen wegkm · aannemelijk: 2005-notificatie, 2025 modaliteit niet gepubliceerd)──►
Westinghouse Columbia FFF `u-columbia-fabricage` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | Sint-Petersburg-kade → Baltimore-kade (Canton) | Finse Golf, Oostzee, Deense Straten, Noordzee, Kanaal, Atlantische Oceaan | MARNET gemeten 8.415,5 km (zeeknopen 6849 / 4839); grootcirkel 7.139 km; geen gepubliceerde zeekm | MARNET | aanloop: nee (SPb-kade 4,90 km, Baltimore-kade 1,38 km van de zeeknoop) |
| b2 | C | truck | Baltimore-kade → Westinghouse Columbia | I-95 (Baltimore–Capital Beltway–Fredericksburg) → I-295 (Richmond-oost) → I-95 (Rocky Mount, Fayetteville, Florence) → I-20 → I-77 → SC 48 | **hemelsbreed 713 km, geen wegkm**; OSRM-indicatie 856 km direct, 881 km via de zeven via-punten [9] (geen bron; ±15%-toets geldt als indicatie) | maak_stroombeen_weg (extracts us-maryland, us-virginia, us-north-carolina, us-south-carolina) | nee — *aannemelijk: 2005 truck R&R bevestigd [1]; 2025 niet gepubliceerd* |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-stpetersburg-kade` | overslag truck/trein → zee (kop) | Petrolesport, Gutujevski-eiland, Sint-Petersburg | 59.8909, 30.2376 | letterlijk uit `uranium-stpetersburg-pierrelatte.md` §3 (daar uit `uranium-inkai-stpetersburg.md`) [10]; notificatie 2005 noemt alleen "St. Petersburg" [1] | bron-gelegd (hergebruikt: z15 containerstapels, kranen, spoorbundel); of déze kade de nucleaire lading krijgt is niet gepubliceerd |
| `u-baltimore-kade` | overslag zee → truck | Rukert Terminals, Canton, South Clinton Street 2021 (eigen keuze: kadepunt aan de pier met loodsen) | 39.2669, -76.5705 | Baltimore Brew 2013 noemt Rukert (de zending van 2013 ging naar Paducah, niet naar Columbia) [3]; adres [6][7] | **onzeker** (z17 gezien: pier met loodsen en stukgoed-/ro-ro-schepen langs de kade, ten oosten van Clinton Street aan het Noordwest-bekken, Fort McHenry in de verte aan de overkant van het water; geen bron noemt de ligplaats voor déze lading) |
| `u-columbia-fabricage` | splijtstoffabricage (staart, stoppunt) | Westinghouse Columbia Fuel Fabrication Facility, Hopkins (Lower Richland County), SC | 33.8831, -80.9194 | letterlijk uit `uranium-eunice-columbia.md` §3 (`u-columbia-fabricage`) [10]; consignee in [1] | bron-gelegd (hergebruikt: z17 groot hallencomplex met parkeerterreinen, tanks en bufferbekkens aan Bluff Road) |

## 4 · Via-punten b2 (lat, lon; elk een vertex van de OSRM-route, dus op de doorgaande weg, nooit in een stadscentrum; DC bewust gemeden via de Capital Beltway)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | I-95 bij Columbia/Laurel (MD) | 39.1603, -76.8228 | pint I-95 i.p.v. de Baltimore-Washington Parkway (MD 295, voor vrachtverkeer gesloten) en het DC-centrum |
| b2 | 2 | Capital Beltway (I-95/I-495), Virginia-zijde | 38.7967, -77.0646 | omrijden van DC over de beltway i.p.v. door de stad |
| b2 | 3 | I-95 bij Fredericksburg (VA) | 38.3013, -77.5038 | houdt I-95 aan i.p.v. US 1 / US 17 |
| b2 | 4 | I-295 ten oosten van Richmond (VA) | 37.4884, -77.2964 | Richmond-omleiding over I-295 i.p.v. I-95 door het centrum (de keerlus van 10,7 km uit de haalbaarheidstoets) |
| b2 | 5 | I-95 bij Rocky Mount (NC) | 35.9560, -77.8884 | pint I-95 door NC i.p.v. US 301 |
| b2 | 6 | I-95 oost van Fayetteville (NC) | 35.0121, -78.8183 | de Fayetteville-bypass, buiten het centrum |
| b2 | 7 | I-95/I-20 bij Florence (SC) | 34.1930, -79.8461 | hier draait de corridor naar I-20 west richting Columbia |
| b2 | 8 | I-20/I-77 oost van Columbia (SC) | 34.0700, -80.9150 | I-77 zuidwaarts naar Bluff Road/Hopkins (zelfde keuze als `uranium-eunice-columbia`) |

*Refs voor het profiel:* I 95, I 495, I 295, I 20, I 77, SC 48. *Venster:* 40 km (de beltway-lus kan breder; 75 als de snap faalt).

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Russische verrijking (niet aangewezen) | Rosatom/Tenex | verrijkt UF6 → haven | niet gespecificeerd | [1][4] |
| Westinghouse Columbia FFF | Westinghouse Electric Company | verrijkt UF6 (30B) → PWR/BWR-splijtstof | ≈ 1.400–1.700 t HM/j (sitelaag, `uranium-eunice-columbia` §3) | [10] |

## 6 · Stoppunt
De brief stopt bij Westinghouse Columbia: opgedragen eindpunt én de enige consignee die een bron voor een Tenex-zending uit Sint-Petersburg met Baltimore als haven koppelt (NRC-notificatie 21-04-2005: consignor Techsnabexport St. Petersburg, consignee Westinghouse Columbia, vessel Baltic Mercur, overslag Baltimore, R&R-trucks) [1]. Fase D vervalt (geen bron noemt een vervolg); E vervalt.

## 7 · Open punten
- **Baltimore-terminal niet gepubliceerd voor deze lading:** Rukert (Canton) steunt op Baltimore Brew 2013 voor een andere zending (Paducah) [3]; de ARRC-schepen van 2005/2025 kunnen ook een ander terminal (Dundalk) gebruiken; geen coordinaat in OSM onder "Rukert" gevonden. Anker blijft onzeker.
- **Modaliteit na Baltimore alleen voor 2005 bevestigd** (R&R Trucking, 49 CFR 397.101-routering [1]); voor 2025/2026 niet gepubliceerd. Geen wegkm gepubliceerd: hemelsbreed 713 km, OSRM 856-881 km [9] — indicatie, geen norm.
- **CBC-artikel (50.612 kg uranium in 4 containers, 2026) kon niet worden geladen (403)** en is niet gelezen; dat cijfer staat alleen in het ketenontwerp. Idem een EA Daily-bericht (zending 26-04-2026, Atlantic Spirit II) dat alleen als zoekresultaat is gezien (pro-Kremlin bron, niet geopend).
- **2025-levering:** The Insider en Bellona citeren EA Daily/ImportGenius; eenheid (UF6 of U) en vertrekhaven niet genoemd [4][5]. Het Sint-Petersburg-vertrek staat alleen in de notificatie van 2005 [1].
- **Peiljaar wisselt:** NRC 2005 en 2025; sinds aug 2024 een importverbod met uitzonderingen en Russische eenmalige exportlicenties.
- **Capital Beltway bij de Woodrow Wilson-brug:** of die brug in de extracts us-maryland/us-virginia valt (een extract us-district-of-columbia staat niet in `v2/build-cache/geofabrik`) is bij het bakken te controleren; ontbreekt hij, dan is dat centraal werk.
- **Zeecorridor overlapt ca. 27% met `uranium-stpetersburg-pierrelatte`** (Finse Golf tot Noordzee); de Atlantische oversteek is nieuw. Geen letterlijke kopie, want de eindkade verschilt.

## 8 · Bronnen
[1] NRC ADAMS ML052510473 (scan), Transport Logistics International, Notification of Shipment, 21-04-2005 (Revision 1): Techsnabexport St. Petersburg → Westinghouse Columbia SC, 7x30B UF6, Atlantic Ro-Ro Carriers, "Baltic Mercur" naar Baltimore, R&R Trucking. https://www.nrc.gov/docs/ML0525/ML052510473.pdf
[2] NRC ADAMS ML063210493 (scan), idem 12-09-2006 (Tenex → USEC Paducah, ARRC-vessel "Viljandi R6-35", overslag Baltimore; bevestigt het patroon St. Petersburg → Baltimore → truck). https://www.nrc.gov/docs/ML0632/ML063210493.pdf
[3] Baltimore Brew, 10-12-2013 (laatste Megatons-to-Megawatts-zending, vier cilinders, Rukert Terminals tegenover Fort McHenry, daarna naar Paducah). https://baltimorebrew.com/2013/12/10/uranium-converted-from-russian-nuclear-warheads-comes-through-baltimores-port
[4] The Insider, 26-02-2025 (Atlantic Navigator II, 12-02-2025 Baltimore, 15 t Westinghouse en 85 t GNF, Tenex; naar EA Daily/ImportGenius). https://theins.press/en/news/279165
[5] Bellona, Rosatom-levering Baltimore 12-02-2025 (100 t, Atlantic Navigator II, geen vertrekhaven). https://etc.bellona.org/?p=108925
[6] Rukert Terminals Corporation, adres 2021 South Clinton Street, Baltimore MD 21224 (stukgoed, ertsen, project cargo). https://rukert.com/company
[7] OpenStreetMap (Nominatim, ODbL): "2021 South Clinton Street", way 69685106, 39.2678, -76.5684. https://nominatim.openstreetmap.org/search?q=2021+South+Clinton+Street+Baltimore&format=jsonv2
[8] Niet gelezen, alleen genoemd in het ketenontwerp: CBC (russian-enriched-uranium-westinghouse-9.7296239, 403) en World Nuclear News (Centrus import waiver); zie §7.
[9] OSRM (router.project-osrm.org, driving): Baltimore-kade → Columbia 856,5 km direct en 881,1 km via de via-punten van §4 (vertices van de route, geen officiele km); MARNET-meting hecht_marnet route SPb → Baltimore 8.415,5 km (snap 4,903 / 1,375 km).
[10] Eigen briefs: `uranium-stpetersburg-pierrelatte.md` §3/§7, `uranium-inkai-stpetersburg.md` §3, `uranium-eunice-columbia.md` §3; sitelaag `v2/design/uranium-sitelaag.json`. Eigen sat_check-blik: `v2/build-cache/satcheck/sat-uranium-stpetersburg-columbia-baltimore-rukert.png` (z15) en `…-rukert-z17.png`.
[haalbaarheidstoets] Bindend invoerdocument (keten-id `uranium-stpetersburg-columbia`): zee 8.415 km, Rukert proberen en anders Locust Point als onzeker anker, via-punten op doorgaande I-95/I-295, extracts maryland/virginia/north-carolina/south-carolina, bronnen NRC 2005, Baltimore Brew, The Insider — toegepast.

## 9 · Gebakken (2026-10-28, lichte werkwijze, M31 golf 10)
**Bestand:** `v2/data/stroomroute-uranium-stpetersburg-columbia.json` (177,7 KB, versie 2, lonlat, 2 benen, 3 markers, 8.798 punten) · **recept:** `bak_uranium_stpetersburg_columbia()` in `v2/tools/bak_stromen.sh` (LF, 0 CRLF) · **profiel:** `uranium-stpetersburg-columbia-baltimore-columbia` in `maak_stroombeen_weg.py`.

| # | modaliteit | van → naar | km gemeten | km brief | afwijking | punten | stippel |
|---|---|---|---|---|---|---|---|
| b1 | zee | SPb-kade → Baltimore-kade (Rukert) | 8.415,5 | MARNET 8.415,5 (grootcirkel 7.139) | 0,0% | 894 | nee |
| b2 | truck | Baltimore-kade → Westinghouse Columbia FFF | 875,9 | hemelsbreed 713 (geen wegkm); OSRM 856,5-881,1 | +22,8% op hemelsbreed (verwacht), +2,3% / -0,6% t.o.v. OSRM | 7.904 | nee |

**Totaal 9.291,4 km.** Naad b1 -> b2: **1,375 km** (zee eindigt op de zeeknoop, de Baltimore-kade ligt 1,38 km verderop; < 5 km, geen aanloop). Markers: Baltimore 0,0 km en Columbia 0,0 km van de lijn; **SPb-kade 4,90 km** van de lijn (zee-snap op zeeknoop 6849, net onder de aanloopgrens van 5 km: bewust geen aanloop, zoals bij stpetersburg-pierrelatte).

**Recept b2 (wegscan):** `wegscan_puur.py --profiel uranium-stpetersburg-columbia-baltimore-columbia` over us-maryland, us-virginia, us-north-carolina, us-south-carolina; venster 40 km, refs I 95 / I 495 / I 295 / I 20 / I 77 / SC 48; acht via-punten uit §4, alle met snap <= 0,02 km (ankers 0,03 en 0,07 km). Segmenten: Baltimore-Laurel 29,8 · Laurel-Beltway 63,6 · Beltway-Fredericksburg 73,9 · Fredericksburg-Richmond-oost 102,7 · Richmond-Rocky Mount 189,3 · Rocky Mount-Fayetteville 140,4 · Fayetteville-Florence 141,1 · Florence-Columbia-oost 105,6 · Columbia-oost-Hopkins 29,6 km; geen omweg-segment. 2 keerlussen gesnoeid (876,0 -> 875,8 km). Woodrow Wilson-brug: de Beltway-oversteek van de Potomac zit in de extracts (geen "geen wegpad"), dus us-district-of-columbia is niet nodig; DC wordt gemeden. Eerste mijl 0,19 km (service), laatste mijl 1,16 km (residential, service).

**Toets:** `json.load` slaagt, versie 2, `punt_formaat` lonlat, modaliteiten {zee, truck}, elk been >= 2 punten, 177,7 KB. `toets_rechte_benen.py --min-km 5` meldt dit bestand niet. `toets_knikken.py`: zee 3 krappe bochten (<= 78,5 gr, straal >= 6 km); truck 15 knikken, waarvan **2 teruglopen van ~70-100 m** (34.1927,-79.8453 bij het I-95/I-20-knooppunt Florence en 34.0719,-80.9257 bij het I-20/I-77-knooppunt Columbia: uit-en-terug langs een rampstomp) en 4 echte scherpe bochten (Baltimore-start 39.2669,-76.5709; Richmond-oost 37.657,-77.454); rest spikes bij de ankers. Niet bijgeschoven, geen via-punt verplaatst.

**Bevindingen / open:** (1) b2 is geen gemeten wegkm: de +-15%-norm geldt als indicatie; de lijn valt binnen OSRM 856-881. (2) SPb-kade 4,9 km van de lijn (net onder 5 km, geen aanloop); een haven-aanloop zou de marker op de lijn brengen. (3) Baltimore-kade onzeker (Rukert, Dundalk even plausibel); modaliteit na Baltimore alleen 2005 bevestigd. (4) Twee korte rampstomp-teruglopen op knooppunten (zie Toets). (5) Zee overlapt ca. 27% met stpetersburg-pierrelatte, geen letterlijke kopie (eindkade verschilt). (6) Fase D en E vervallen; Russische fabriek niet getekend.

**Lessen:** vier extracts (~0,9 GB pbf) liepen in ~10 minuten door `wegscan_puur.py`; een via-punt op een snelwegknooppunt kan een korte rampstomp-terugloop geven die `keerlussen gesnoeid` niet opruimt (hier 2 x ~70-100 m). De via-punten die uit de OSRM-vertices komen gaven geen enkele snap > 0,03 km.
