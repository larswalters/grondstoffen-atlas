# Routebrief (licht) · Uranium — Metropolis Works → Portsmouth VA → Rotterdam → Urenco Almelo (VS → Nederland)

**stroom-id:** `uranium-metropolis-almelo` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** UF6 in 48Y-cilinders uit de Honeywell/ConverDyn-conversiefabriek Metropolis Works (Illinois) gaat per **truck** over WK/Bluegrass Parkway en I-64 (via Lexington, Charleston WV, Sandstone WV en Richmond) naar de Portsmouth Marine Terminal (Hampton Roads), per **zeeschip** over de Atlantische Oceaan naar Rotterdam RHB (aannemelijk: aanname) en per **truck** (A20/A12/A27/A28/A1/A35) naar de Urenco-verrijkingsfabriek in Almelo — stoppunt.
**Welke as van het verhaal:** *VS-conversie naar Europese verrijking* — de enige VS-UF6-fabriek levert aan Urenco Nederland. Volume: ~1.000 cilinders/j ≈ 8.600 t U/j naar Europese verrijkers (NRC-exportvergunning 2017 volgens het ketenontwerp, via WISE; niet zelf herleid), Almelo-aandeel niet gepubliceerd; nameplate Metropolis ~15.000 t U/j (sitelaag). Het route-bewijs is één zending uit 2009 (§7).

## 1 · Ketenkaart
```
Metropolis Works `u-metropolis-conversie` ──(b1 A truck · I-24/I-69 → WK Pkwy → I-65 → Bluegrass Pkwy → I-64 (Lexington–Sandstone WV–Richmond) → I-295/I-664 · OSRM ~1.393 km, geen wegkm gepubliceerd)──►
  Portsmouth Marine Terminal `u-portsmouth-kade` ──(b2a zee haven-aanloop 16,6 km tot zeeknoop 7797, stippel)──► MARNET-zeeknoop 7797
  ──(b2b zee · Noord-Atlantische Oceaan → Kanaal · 6.496,7 km gemeten MARNET)──► Rotterdam RHB `u-rotterdam-kade` (aannemelijk: aanname)
  ──(b3 C truck · A20→A12→A27→A28→A1→A35 · kopie uranium-porthope-almelo · 191,7 km)──► Urenco Almelo `u-almelo-urenco` ── stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | truck | Metropolis Works → Portsmouth Marine Terminal | US-45 → I-24 → I-69/WK Parkway → I-65 → Bluegrass Parkway → I-64 (Lexington, Charleston WV, **Sandstone WV exit 139**, Richmond) → I-295 → I-664 → US-58 [1][7] | OSRM-wegkm 1.377 (eigen run, via-punten §4) tot 1.409 (haalbaarheidstoets), **geen publicatie**; hemelsbreed 1.106 km. ±15%-toets = indicatie | maak_stroombeen_weg (us-illinois, us-kentucky, us-west-virginia, us-virginia) | nee |
| b2a | B | zee (haven-aanloop) | Portsmouth-kade → MARNET-zeeknoop 7797 (36.9356,-76.4429) | Elizabeth River/Hampton Roads, schematisch over water | 13,5 hemelsbreed [8]; aanloop 16,6 gemeten (eigen run 2026-10-29: cel 0,005 gebufferd, 29 punten, 0,43 km over land aan het uiteinde, 0 km midden) [11] | maak_havenaanloop.py; geojson staat klaar: `uranium-metropolis-almelo-aanloop-portsmouth.geojson` | ja — net reikt niet tot de kade |
| b2b | B | zee | zeeknoop 7797 → Rotterdam RHB | Noord-Atlantische Oceaan, Kanaal; Rotterdam = aanname (zelfde haven als uranium-porthope-almelo) | 6.496,7 [8: MARNET-dry-run kade → kade, snap Portsmouth 13,5 km, snap Rotterdam 0,73 km] | MARNET | nee (aanloop apart in b2a) |
| b3 | C | truck | Rotterdam RHB → Urenco Almelo | A20 → A12 → A27 → A28 → A1 → A35 → N349 | 191,7 getekend (OSRM 189) [9] | **letterlijke kopie** van `uranium-porthope-almelo-weg-rotterdam-almelo.geojson` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `u-metropolis-conversie` | UF6-fabriek (kop, **hergebruikt**) | Honeywell/ConverDyn Metropolis Works, Illinois | 37.1718, -88.7570 | letterlijk uit `uranium-smithranch-metropolis` §3 (= sitelaag `w-metropolis`) [2][10] | bron-gelegd (z16 in die brief: ommuurd fabrieksterrein met tanks en hallen aan de Ohio, 3 km NW van de stad) |
| `u-portsmouth-kade` | overslag truck → zee | Portsmouth Marine Terminal (Virginia Port Authority), Elizabeth River | 36.8575, -76.3270 | [1] noemt alleen "Portsmouth, VA"; terminal = aanname [3]; positie satelliet-gelegd [6] | **aannemelijk** (z16 gezien, 2026-10-29: groot kadeterrein ~219 acre met kranen, containerstapels en een schip aan de noordkade, direct zuid van de Midtown-tunnelbrug; anker ligt op de noordrand van de kade) |
| `u-rotterdam-kade` | overslag zee → truck (**hergebruikt**) | Rotterdam — RHB Stevedoring & Warehousing, Waalhaven Noordzijde 4 | 51.8935, 4.4585 | vast anker uit de kaart (`routebrief-licht.md` §1), letterlijk uit `uranium-porthope-almelo` §3 | hergebruikt; aanname dat deze lading hier losgaat (§7) |
| `u-almelo-urenco` | verrijkingsfabriek (stoppunt, **hergebruikt**) | Urenco Nederland, Drienemansweg, Almelo | 52.3391, 6.6922 | letterlijk uit `uranium-porthope-almelo` §3 [4][9] | bron-gelegd (z15 in die brief: industrieterrein Bavinkel). Sitelaag `w-urenco-almelo` staat op 52.3383, 6.6939 (~0,15 km ernaast, status aannemelijk) — niet gewijzigd, gemeld |

## 4 · Via-punten (alleen b1; (lat, lon) hier, in het profiel (lon, lat); allemaal OSRM-manoeuvrepunten op de doorgaande weg)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Western Kentucky Parkway | 37.2125, -87.4541 | pint de WK-/Bluegrass-route boven Mount Vernon–Louisville |
| b1 | 2 | Bluegrass Parkway | 37.7034, -85.8266 | oostwaarts zonder via Louisville; sluit aan op I-64 bij Lexington |
| b1 | 3 | I-64/I-75 Lexington | 38.0610, -84.4375 | de I-64-corridor naar Charleston WV, niet I-40/I-81 (die OSRM zonder via kiest: 1.378 km) |
| b1 | 4 | I-64 Sandstone WV (exit 139) | 37.7828, -80.8907 | de bron-plek [1]: pint I-64 door West Virginia |
| b1 | 5 | I-295 bij Richmond | 37.6627, -77.5975 | de ringweg om het centrum; pint I-64 → I-295 → I-664 naar Hampton Roads |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Metropolis Works | Honeywell / ConverDyn | U3O8 → UF6 | vergund ~15.000 t U/j; enige VS-fabriek | [2], sitelaag |
| Portsmouth Marine Terminal | Virginia Port Authority | truck → zee | 219 acre, kade 1.080 m, 3 ligplaatsen | [3] |
| Urenco Almelo | Urenco Nederland | UF6 → LEU-UF6 | ~5.200 t U/j voeding-equivalent, SCHATTING (sitelaag, niet gepubliceerd) | sitelaag, [4] |

## 6 · Stoppunt
De brief stopt bij Urenco Almelo (verrijking, het opgegeven eindpunt): de bron noemt "URENCO in the Netherlands" als bestemming en geen vervolgstap; fase D vervalt.

## 7 · Open punten
- **Eén bron, 2009 (17 jaar oud):** WISE/NRC-melding over een UF6-truck op I-64 bij Sandstone WV: 48Y-cilinder (12,7 t UF6) van Metropolis naar Portsmouth VA "for shipment to URENCO in the Netherlands". Of de stroom nog zo loopt is niet gepubliceerd; Metropolis lag stil (2017/18 tot 2023, bronnen verschillen) — actuele stroom onbevestigd.
- **Rotterdam als loshaven is aanname** (de bron noemt alleen Nederland); Antwerpen/Vlissingen zijn niet uit te sluiten. Zelfde aanname als `uranium-porthope-almelo`.
- **Portsmouth-terminal is aanname:** de bron noemt "Portsmouth, VA"; Portsmouth Marine Terminal is de enige Port-of-Virginia-terminal met die naam [3]. Kadepunt alleen via satelliet, geen terminalbron.
- **Kilometers b1:** alleen OSRM-indicatie, geen publicatie (niet de ±15%-norm). Over dezelfde corridor 1.377 (eigen run) versus 1.409 (haalbaarheidstoets); het verschil is niet uitgezocht.
- **Weg-last mile Portsmouth:** het kadeterrein is mogelijk niet (volledig) in OSM bereikbaar; ligt de laatste openbare weg > ~2 km van het anker, dan een stippel "last mile (geen net op deze korrel)".
- **Exporthoeveelheid:** de ~1.000 cilinders/j (≈ 8.600 t U/j, 2017-vergunning) komt uit het ketenontwerp; de NRC-vergunningsdocumenten zijn via de zoekmachine alleen als snippet gezien (nrc.gov gaf 403), exporteur en looptijd onbevestigd.
- Geen spoor (`spoornet_nodig: false`), geen leiding (OSM nvt). b3 is exact `uranium-porthope-almelo` b3: overlap 191,7 van ~8.100 km.

## 8 · Bronnen
[1] WISE Uranium Project, "Enrichment & Fuel Fab. — Issues" (UF6-truck I-64 Exit 139 Sandstone WV, 3 aug 2009; Metropolis → Portsmouth VA → URENCO NL). http://www.wise-uranium.org/etiss.html
[2] Wikipedia (en), "Honeywell Uranium Hexafluoride Processing Facility" — Metropolis Works, herstart 7 nov 2014. https://en.wikipedia.org/wiki/Honeywell_Uranium_Hexafluoride_Processing_Facility
[3] Wikipedia (en), "Virginia Port Authority" — Portsmouth Marine Terminal: 219 acre, wharf 3.540 ft, 3 ligplaatsen, 20.100 ft spoor. https://en.wikipedia.org/wiki/Virginia_Port_Authority
[4] U.S. Federal Register, 3 juli 2013 (FR Doc. 2013-15967) — Almelo als Urenco-verrijkingsbestemming (verwerkt in `uranium-porthope-almelo`). https://www.govinfo.gov/content/pkg/FR-2013-07-03/pdf/2013-15967.pdf
[5] NRC-exportvergunningen met Urenco Nederland (Almelo) als consignee, o.a. https://www.nrc.gov/docs/ML1601/ML16014A279.pdf — alleen als zoekresultaat gezien (403).
[6] Esri World Imagery, `sat_check.py` z15/z16, `v2/build-cache/satcheck/sat-uranium-metropolis-almelo-portsmouth-kade16.png` (2026-10-29).
[7] OSRM publieke demo-server (project-osrm.org): Metropolis → Portsmouth via de vijf via-punten 1.377 km (I-24/I-69/WK/I-65/Bluegrass/I-64/I-295/I-664); zonder via 1.378 km via I-40/I-81 (vermijdt WV).
[8] `hecht_marnet.py route` dry-run 2026-10-29: kade Portsmouth 36.8575,-76.3270 snapt 13,477 km op zeeknoop 7797; MARNET 6.496,7 km naar Rotterdam RHB (snap 0,727 km).
[9] Routebrief `uranium-porthope-almelo.md` §2–§4/§9 — b3 Rotterdam → Almelo, 191,7 km, Rotterdam- en Almelo-anker.
[10] Routebrief `uranium-smithranch-metropolis.md` §3 — Metropolis-anker, satelliet-gelegd.
[11] Haalbaarheidstoets `uranium-metropolis-almelo` (bindend invoerdocument): zeeanker Portsmouth, corridor via Lexington/Charleston WV.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`bash v2/tools/bak_stromen.sh uranium-metropolis-almelo` → `v2/data/stroomroute-uranium-metropolis-almelo.json` (484,3 KB, 24.082 punten, 4 markers, 4 benen, totaal 8.074,6 km). Functie `bak_uranium_metropolis_almelo`, wegprofiel `uranium-metropolis-almelo-metropolis-portsmouth` in `maak_stroombeen_weg.py` (wegscan_puur, 4 extracts, 6 segmenten).

| # | modaliteit | km gemeten | brief | afwijking | naad naar volgend been |
|---|---|---|---|---|---|
| b1 | truck | 1.369,6 | 1.393 (OSRM-indicatie, geen wegkm) | -1,7% (indicatie, geen norm) | 0,00 km |
| b2a | zee, stippel (haven-aanloop) | 16,6 | 16,6 | 0% | 0,00 km |
| b2b | zee (MARNET zeeknoop 7797 → Rotterdam RHB) | 6.496,7 | 6.496,7 | 0% | 0,73 km (snap Rotterdam-kade) |
| b3 | truck (letterlijke kopie uranium-porthope-almelo) | 191,7 | 191,7 | 0% | — |

- **Markers:** 4 (Metropolis, Portsmouth-kade, Rotterdam RHB, Urenco Almelo), alle 0,0 km van hun lijn. Grootste naad 0,73 km (zeeknoop-snap Rotterdam), ruim onder 5 km.
- **Recept b1:** via-punten (lon, lat) Metropolis; -87.4541,37.2125; -85.8266,37.7034; -84.4375,38.0610; -80.8907,37.7828; -77.5975,37.6627; Portsmouth. Alle via-snaps ≤ 0,03 km, kade-snap 0,08 km. Refs I-24 I-69 WK BG I-65 I-64 I-295 I-664, vensterKm 40, eindToegangPrivaat, trimStaart. Segmenten 135,8 / 164,0 / 138,1 / 415,0 / 351,9 / 164,9 km; geen omweg. First mile 0,58 km (residential, service), last mile 0,92 km (service, unclassified): de kade is dus gewoon over OSM-wegen bereikt, geen last-mile-stippel nodig.
- **Haven-aanloop b2a (stippel):** de kade ligt 13,5 km (hemelsbreed) van zeeknoop 7797, dus boven de 5 km-norm; `maak_havenaanloop.py` gaf 16,6 km over water (29 punten, 0,43 km over land aan het uiteinde); het geojson stond klaar en is ongewijzigd gebruikt. Stippel betekent hier "MARNET reikt niet tot de kade".
- **b3:** letterlijke kopie van `uranium-porthope-almelo-weg-rotterdam-almelo.geojson` (191,7 km); in de beennaam genoemd.
- **Toetsen:** `toets_rechte_benen` geen verdenking voor deze stroom; `toets_knikken`: b1 1 omkering (173°, R 34 m op 37.7024,-85.8341, het I-65/Bluegrass Parkway-knooppunt: ~0,6 km overschiet-en-terug op de rampstructuur, scherpe bocht "echt", geen terugloop), de twee terugloopjes zitten in de gekopieerde b3 (52.0551,5.1438 en 52.0909,5.1552, bestond al in uranium-porthope-almelo).
- **Bevinding bestandsgrootte:** 484 KB (b1 alleen is 21.115 punten, wegscan geeft ~65 m puntafstand), boven de ~300 KB-richtlijn; niet herbakken, centraal noteren.
- **Gelaten zoals in de brief:** sitelaag `w-urenco-almelo` (0,15 km naast het anker) niet gewijzigd; route-bewijs blijft één zending uit 2009, Portsmouth-terminal en Rotterdam als loshaven zijn aannames (§7). Eindpunt van het id (Almelo) klopt met het gebakken eindpunt.
- **Lessen:** (1) een wegscan over vier VS-extracts kostte ~7 minuten (Virginia 425 MB en Kentucky domineren), de tweede run is cachegedreven. (2) Een via-punt op een knooppunt (Bluegrass Parkway bij I-65) geeft een overschiet van ~0,6 km zonder dat de km-toets het ziet; hij is niet bijgeschoven (geen shotgun-fix) maar genoteerd. (3) Een 1.370 km-truckbeen komt uit de wegscan als ~500 KB; bij meerdere zulke benen de bundelgrootte in de gaten houden.
