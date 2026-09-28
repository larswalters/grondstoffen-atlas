# Routebrief (licht) · PGM — Van → Via → Naar (land)

**stroom-id:** `pgm-norilsk-krasnojarsk` · **geschreven:** 2026-09-28 · **werkwijze:** licht (M31 golf 3) ·
**status:** gebakken
**Keten in één zin:** palladium(-dominant)-concentraat/matte van de Nadezhda-smelter (Nornickel Polar Division,
Norilsk) per **spoor** over het geïsoleerde Norilsk-industrienet naar het vrachtplatform van Alykel (NSK), per
**vrachtvlucht** (grootcirkel) naar het vrachtplatform van Krasnoyarsk Yemelyanovo (KJA), en per **truck** naar de
Krastsvetmet-raffinaderij in Krasnoyarsk — daar tot geregistreerd Pt/Pd/Rh **(stoppunt)**.
**Welke as van het verhaal:** de enige route van Norilsk naar het Russische vasteland die geen zee/rivier gebruikt.
Nornickel produceert wereldwijd (overwegend Norilsk) indicatief **2,6–2,8 Moz palladium/jaar** (peiljaar 2023–2024)
≈ **80,9–87,1 t Pd/jaar** (koz ÷ 32,15 = t; eenheid = 1E, alleen Pd — geen Pt/Rh/Au-mix in deze bron) [1]. Geen
aparte Krastsvetmet-doorvoertonnage gevonden; zie §7. Norilsk heeft aantoonbaar **geen weg- of doorgaande
spoorverbinding met het nationale net** — het lokale Norilsk Railway is geïsoleerd [2] — dus lucht (of rivier,
seizoensgebonden) is de facto de enige route voor hoogwaardige lading. Dit vervangt letterlijk de vermoede
PGM-specifieke bron uit het ontwerp, conform de haalbaarheidstoets (bindend, zie §7).

## 1 · Ketenkaart
```
Nadezhda-smelter `pgm-nadezhda-fabriek` ──(b1 spoor · Norilsk-industrienet, geïsoleerd · ~50 km)──►
Alykel-vrachtplatform `pgm-alykel-vrachtterminal` (NSK)
   ──(b2 lucht · vlucht NSK → KJA, grootcirkel · ~1.484 km)──►
Yemelyanovo-vrachtplatform `pgm-yemelyanovo-vrachtterminal` (KJA)
   ──(b3 truck · R257/Jenisej-oversteek · ~35 km)──►
Krastsvetmet-raffinaderij `pgm-krastsvetmet-raffinaderij`, Krasnoyarsk ── stoppunt (geregistreerd Pt/Pd/Rh)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | spoor | `pgm-nadezhda-fabriek` → `pgm-alykel-vrachtterminal` | Norilsk Railway — geïsoleerd industrieel net, Nadezhda → Kayerkan → Alykel (zelfde net als Nadezhda→Dudinka) [2][8] | ~50 (ontwerp-indicatie); hemelsbreed gemeten 24,5 [9] | `BAKE_SUFFIX=-raw toets_spoorroute.mjs --hoofd-km=50` (rusland-siberie, zelfde drempel als de nikkel-Norilsk-brief) | nee, tenzij het geïsoleerde net Alykel niet blijkt te raken (zie §7) |
| b2 | B | lucht | `pgm-alykel-vrachtterminal` → `pgm-yemelyanovo-vrachtterminal` | vlucht NSK → KJA (vrachtvlucht, grootcirkel) — enige route van Norilsk naar het vasteland zonder rivier/zee | ~1.500 (ontwerp); grootcirkel gemeten 1.484,3 [9] | `maak_luchtbeen.py` | **nee — doorgetrokken** (lucht is nooit stippel, bakhandleiding §2) |
| b3 | C | truck | `pgm-yemelyanovo-vrachtterminal` → `pgm-krastsvetmet-raffinaderij` | luchthaven-toegangsweg → **R257** (Krasnoyarsk–Yeniseysk, "Yeniseysky trakt") zuidwaarts → Jenisej-oversteek → Ленинский район, Транспортный проезд | ~25 (ontwerp); hemelsbreed gemeten 34,5 → herzien richtwaarde ~35–40 [9] | `maak_stroombeen_weg.py` | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `pgm-nadezhda-fabriek` | mijn/smelter (kop spoor) | Nadezhda Metallurgical Plant, Norilsk (Nornickel Polar Division) | 69.3275, 87.9521 | [3], **hergebruikt anker** `ni-nadezhda-fabriek` uit `nikkel-norilsk-monchegorsk.md` | bron-gelegd (z15 gezien in die brief: fabriekscomplex met rookpluim, tankinstallaties, spoorbundel direct ten westen) |
| `pgm-alykel-vrachtterminal` | vrachtplatform (kop lucht) | Alykel International Airport (NSK), Norilsk | 69.3252, 87.3290 | [4][9] | **onzeker** (z17 gezien: klein regionaal vliegveldcomplex met terminal + verwarmings-/technische gebouwen en een asfaltplatform; géén loodsen of vrachttoestellen te onderscheiden die specifiek op cargo wijzen — geen aparte vrachtterminal-bron gevonden) |
| `pgm-yemelyanovo-vrachtterminal` | vrachtplatform (losplek lucht) | Krasnoyarsk International Airport / Yemelyanovo (KJA) | 56.1785, 92.5250 | [5][9] | bron-gelegd (z16 gezien: platform met meerdere geparkeerde vrachttoestellen naast de terminalgebouwen aan de oostzijde van de baan; bron bevestigt een grote Lufthansa Cargo-hub — "second largest after Frankfurt" — en de AirBridgeCargo-basis sinds 2018 [5]) |
| `pgm-krastsvetmet-raffinaderij` | raffinaderij (losplek) | Krastsvetmet (OJSC Gulidov Krasnoyarsk Non-Ferrous Metals Plant), Транспортный проезд 1, Krasnoyarsk | 56.0160, 92.9998 | [6][9] | bron-gelegd (z16 gezien: groot industrieterrein met meerdere hallen direct ten zuiden van de Jenisej-oever; adres komt overeen met het geregistreerde bedrijfsadres [6]; v1-checklist gaf een grovere stadscentroïde 56.01/92.87 — dit anker vervangt die) |

## 4 · Via-punten
Geen — b1 (industrieel spoornet, geen corridorkeuze buiten het enkelvoudige tracé) en b2 (grootcirkel, geen net op
de grond) hebben er per constructie geen. **b3** vraagt ze wel (25–40 km, meerdere kruisingen), maar konden niet
gepind worden: Overpass was tijdens het schrijven van deze brief onbereikbaar (zie §7) — de bak-agent pint 2–4
punten op R257/de Jenisej-brug met OSM tijdens het bakken.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Nadezhda Metallurgical Plant, Norilsk | Nornickel Polar Division | erts/concentraat Talnakh-mijnen → converter-matte/concentraat (Ni-Cu-Pd-Pt-sulfide) | onderdeel van groepscijfer ~2,6–2,8 Moz Pd/j | [1][3] |
| Krastsvetmet, Krasnoyarsk | Krastsvetmet (tolling voor Nornickel) | Norilsk-concentraat/matte → geregistreerd Pt/Pd/Rh (LBMA/LPPM-erkend) | 's werelds grootste PGM-raffinaderij; raffineert ~90% van het Russische Pt/Pd [1][6] | [1][6] |

## 6 · Stoppunt
De brief stopt bij Krastsvetmet: geregistreerd Pt/Pd/Rh is het eindproduct van deze streng (LBMA/LPPM
good-delivery), en Krastsvetmet raffineert de Norilsk-edelmetalen onder tolling voor Nornickel [1][6] — geen bron
koppelt déze specifieke lading aan een volgende, benoemde afnemer/fabriek. Fase D/E vervallen.

## 7 · Open punten
- **Modaliteit Norilsk→Krasnoyarsk niet PGM-specifiek gebrond.** Geen bron bevestigt expliciet dat dít
  PGM-concentraat/deze matte vliegt; de motivering is Norilsk's aantoonbare isolatie (geen weg/doorgaande
  spoorverbinding met het nationale net [2]), zoals de haalbaarheidstoets bindend voorschrijft. Het
  rivier-alternatief (binnenvaart Krasnoyarsk–Dudinka over de Jenisej, seizoensgebonden) is even plausibel en
  blijft expliciet open — niet getekend.
- **b1 op het geïsoleerde net:** de haalbaarheidstoets waarschuwt dat dit been op hetzelfde geïsoleerde
  Norilsk-industrienet ligt als Nadezhda→Dudinka (bevestigd bron-gelegd in `nikkel-norilsk-monchegorsk.md`,
  component ~253 km) — moet bij het bakken met `--hoofd-km=50` op dezelfde OSM-component vallen, anders faalt de
  hoofdnet-drempel en wordt dit onterecht een stippel in plaats van een gemeten been.
- **`pgm-alykel-vrachtterminal` is onzeker:** Alykel is een klein regionaal vliegveld; op het satellietbeeld (z17)
  is geen apart vrachtplatform/loods te onderscheiden van de gewone terminal- en technische gebouwen, en er is
  geen bron gevonden die een specifieke Alykel-vrachtterminal noemt. Mogelijk gaat PGM als bijvracht op
  passagiersvluchten of kleine vrachttoestellen vanaf het bestaande platform.
- **b3 via-punten niet gepind:** Overpass onbereikbaar tijdens het schrijven; corridor (R257/Yeniseysky trakt →
  Jenisej-brug → Ленинский район) is wel bekend. Gepubliceerde km herzien van de ontwerp-indicatie (25) naar
  ~35–40 op basis van de gemeten hemelsbrede afstand (34,5 km) — bij het bakken de werkelijke wegafstand gebruiken.
- **Krastsvetmet-terrein is groot** (meerdere percelen/gebouwen); de exacte aanvoerpoort is niet aangewezen — het
  anker staat op het geregistreerde bedrijfsadres (complex-niveau, conform de lichte werkwijze).
- **Jaarvolume is het Nornickel-groepscijfer voor Pd** (2,6–2,8 Moz/j, overwegend Norilsk); geen aparte
  Krastsvetmet-doorvoertonnage voor déze route gevonden.

## 8 · Bronnen
[1] Nornickel, persbericht productieresultaten (peiljaar 2023–2024; groepscijfer Pd ~2,6–2,8 Moz/jaar;
Krastsvetmet raffineert Norilsk-edelmetalen onder tolling). https://nornickel.com/news-and-media/press-releases-and-news/nornickel-announces-consolidated-production-results-for-2024/
[2] Wikipedia, "Norilsk Railway" — verbindt Talnakh, Norilsk, Kayerkan en Alykel (vliegveld) met de haven Dudinka;
127 km; eigendom van Nornickel, **niet** onderdeel van het Russische nationale spoornet ("does not belong to
Russian Railways"). https://en.wikipedia.org/wiki/Norilsk_Railway
[3] Nornickel, Norilsk Division — bedrijfsprofiel (Nadezhda Metallurgical Plant, Polar Division). https://nornickel.com/business/assets/norilsk-division/
[4] Wikipedia, "Alykel International Airport" — IATA NSK, ICAO UOOO, luchthaven van Norilsk in Krasnoyarsk Krai;
69,310°N/87,333°O. https://en.wikipedia.org/wiki/Alykel_International_Airport
[5] Wikipedia, "Krasnoyarsk International Airport" — IATA KJA; 56,172°N/92,493°O; cargo-sectie: Lufthansa Cargo's
op-één-na-grootste hub na Frankfurt, AirBridgeCargo-basis sinds januari 2018, routes o.a. Amsterdam/Beijing/Hong
Kong/Shanghai. https://en.wikipedia.org/wiki/Krasnoyarsk_International_Airport
[6] Krastsvetmet, bedrijfsgegevens/requisites — statutair adres Транспортный проезд, д. 1, Красноярск, 660123;
's werelds grootste raffinaderij van platinagroepmetalen, raffineert ~90% van het Russische Pt/Pd. https://www.krastsvetmet.ru/about-us/requisites/
[7] v2/data/pgm.js (v1-checklist) — Norilsk→Krastsvetmet-Krasnoyarsk als bestaande stroom (grove stadscentroïde
56,01/92,87, vervangen door het site-niveau-anker in §3).
[8] Interne haalbaarheidstoets `pgm-norilsk-krasnojarsk` (ontwerp-JSON, 2026-09-28, bindend) — aanpassing:
lucht behouden, gemotiveerd met Norilsk's isolatie i.p.v. een vermoede PGM-specifieke bron.
[9] Esri World Imagery via `v2/tools/sat_check.py` (z14–z17) —
`v2/build-cache/satcheck/sat-pgm-norilsk-krasnojarsk-*.png` (alykel-overzicht z14, alykel-terminal z17,
yemelyanovo-overzicht z14, yemelyanovo-oost z16, krastsvetmet z15/z16); grootcirkel- en hemelsbrede afstanden
berekend met dezelfde Vincenty/haversine-methode als `hecht_marnet.py`.

## 9 · Gebakken (2026-09-28, lichte werkwijze, M31 golf 3)

**Stroom `pgm-norilsk-krasnojarsk`** → `v2/data/stroomroute-pgm-norilsk-krasnojarsk.json` — 5 benen (2 spoor
waarvan 1 stippel, 1 lucht, 2 truck waarvan 1 stippel), **1.571,8 km**, 841 punten, 4 markers, 18,0 KB. Recept:
`bak_stromen.sh` (functie `bak_pgm_norilsk_krasnojarsk`); nieuw wegprofiel
`pgm-norilsk-krasnojarsk-yemelyanovo-krastsvetmet` in `maak_stroombeen_weg.py`; spoorbeen met
`toets_spoorroute.mjs --hoofd-km=50`; luchtbeen met `maak_luchtbeen.py`.

**b1 (spoor, `BAKE_SUFFIX=-raw toets_spoorroute.mjs --hoofd-km=50 --max-snap=15`, extract rusland-siberie):**
Nadezhda-smelter → Alykel-vrachtplatform, **27,3 km over 32 edges**, verhouding 1,12 (grootcirkel 24,5 km).
**GEMETEN, geen stippel** — de kandidaat-stippel uit de brief ("component-mismatch") deed zich niet voor: beide
uiteinden snappen op hetzelfde geïsoleerde Norilsk-industrienet-component van **253 km**, exact hetzelfde
component als Nadezhda→Dudinka in `nikkel-norilsk-monchegorsk.md`. Snap van 0,73 km (Nadezhda) en 6,17 km
(Alykel) — dat laatste is de reden voor b2 hieronder.

**b2 (spoor, stippel):** het geometrische spoorbeen eindigt 6,17 km voor het Alykel-vrachtplatform — OSM kent
geen doorgaand zijspoor tot op het platform (`--stippel "spoor|laatste zijspoor naar het Alykel-vrachtplatform
ontbreekt in OSM…"`, 6,2 km, 2 punten). Consistent met de al onzekere Alykel-vrachtterminal-status uit de brief
(§3/§7): geen bron voor een aparte cargofaciliteit, dus geen bron voor een cargo-zijspoor. Naad > 5 km
(bakhandleiding §2 "Emplacementen/havensporen missen vaak") — niet dichtgetrokken, wél als aparte stippel-been
getekend zodat de kaart hem als "hier reikt het net niet" toont in plaats van als een naad die stilzwijgend
verdwijnt.

**b3 (lucht, `maak_luchtbeen.py`):** Alykel (NSK, 69,3252/87,3290) → Yemelyanovo (KJA, 56,1785/92,5250) —
**1.484,3 km** grootcirkel, 61 punten. Doorgetrokken; komt exact overeen met de brief-schatting (1.484,3 km).
Gemotiveerd met Norilsk's aantoonbare isolatie (geen weg/doorgaande spoorverbinding met het nationale net) i.p.v.
een PGM-specifieke bron — de bindende aanpassing uit de haalbaarheidstoets (brief §7/§8[8]).

**b4 (truck, stippel):** Yemelyanovo-vrachtterminal-anker → eerste primary-knoop van 04А-300 — **0,76 km**.
Overpass was onbereikbaar bij het schrijven van de brief; bij het pinnen van via-punten met pyosmium op de
lokale `rusland-siberie`-extract bleek het hele kleine-klasse-wegennet rond de cargoterminal in OSM te bestaan
uit eilandjes van 4-7 knopen zonder gedeelde knoop met het doorgaande net (component-scan op de gescande graaf
— zelfde klasse als `cu-beilun-laadspoor`). Korter dan 2 km → stippel met reden, conform de instructie voor
airside/privéterrein zonder doorlopend net.

**b5 (truck, nieuw profiel `pgm-norilsk-krasnojarsk-yemelyanovo-krastsvetmet`, extract rusland-siberie,
vensterKm 40, `corridorKlassen`/`eindKlassen` tertiary/unclassified/residential/service):**
`maak_stroombeen_weg.py --profiel pgm-norilsk-krasnojarsk-yemelyanovo-krastsvetmet --bron geofabrik` —
**53,2 km** geroute (2 keerlussen gesnoeid, 54,7 → 53,1 km + 0,1 km anker-stukjes). **De brief vermoedde de
verkeerde corridor:** "R257 zuidwaarts" bleek de andere kant van de stad (R-257/Predmostnaya площадь loopt
zuidwestwaarts naar Abakan, niet naar Krastsvetmet). Zelf gepind met pyosmium (Overpass onbereikbaar): de echte
route is de luchthavenweg **R-255 "Sibir"** (niet R257) → **Северное шоссе/Енисейский тракт** (ringwegknoop
noord) → **Октябрьский мост** (Jenisej-oversteek, niet de Коммунальный мост bij Predmostnaya) →
Krastsvetmet-terrein. Anker-verbindingsstukjes plant → weg 0,01 km en weg → kade 0,05 km (beide OK).
Doorgetrokken (geen stippel op het hoofdbeen).

**⚠️ Lengtetoets BUITEN de norm op b5 — bevinding, geen fout:** 53,2 km tegen de door de briefschrijver herziene
toetswaarde ~40 km (zelf al opwaarts bijgesteld van de ontwerp-indicatie 25 km) = **+32,9%**. Verklaring: de
brief nam R257 als corridor-aanname en schatte op die basis; de werkelijke route via twee ringwegen en een
andere Jenisej-brug is een reële stadsroute met bochten om gebouwen/kruispunten, en dat is structureel langer
dan een hemelsbreed-keten van vier via-punten (37,5 km) — laat staan dan de oorspronkelijke 25 km. Geen
via-punt bijgeschoven om het getal te halen (conform de norm); dit vervangt bovendien de corridorbeschrijving
uit de brief met de daadwerkelijk gevonden weg (R-255/Северное шоссе/Октябрьский мост i.p.v. R257).

**Toetsen:** `toets_knikken.py` — b1 0 knikken, b3 (lucht) 0 knikken, b5: **25 knikken ≥60°** (24 spikes bij
kruispunten in Krasnojarsk, R 2–27 m, plus 1 echte scherpe bocht bij Krastsvetmet, 155,2°, R 24 m — geen
terugloop). **Totaal 25 knikken, 1 omkering ≥150°, 0 terugloop** over de hele stroom — geen actie nodig.
`toets_rechte_benen.py --min-km 5` — meldt alleen de b2-stippel (6,2 km, factor 1,005, verwacht: een stippel mag
recht zijn — "hier reikt het net niet"); b4-stippel (0,76 km) blijft onder de 5 km-drempel. Geen doorgetrokken
been staat op de lijst. `json.load` slaagt: versie 2, `punt_formaat` lonlat, modaliteiten `spoor`/`lucht`/`truck`
∈ toegestane set, elk been ≥ 2 punten (2–670), bestandsgrootte 18,0 KB (ruim onder ~300 KB). Naden tussen alle
vijf opeenvolgende benen: **0,000 km** (elk been begint exact waar het vorige eindigt). Markers: 3 van de 4 op
0,00 km van hun been (exact op het ankerpunt, want de stippels zijn zo getekend dat ze er precies op eindigen);
`pgm-nadezhda-fabriek` staat 0,73 km van de spoorlijn — **anker ≠ routeerpunt** (de spoorroute snapt op de
dichtstbijzijnde hoofdnet-knoop, niet op het fabrieksterrein zelf; dezelfde klasse als elders in dit project).

**Toelichting stippels/haven-aanlopen/vluchten:** twee stippels (b2 spoor 6,2 km, b4 truck 0,76 km), beide "hier
reikt het net niet" met een expliciete reden hierboven — geen dichtgetrokken naad. **Eén vlucht** (b3), NSK→KJA,
doorgetrokken grootcirkel tussen twee satelliet-gelegde vrachtplatforms; geen tussenlanding/hub genoemd door een
bron, dus één directe vlucht (aanname al in brief §7). Geen zeebeen in deze keten, dus geen haven-aanloop nodig.

**Gereedschapslessen:** `--hoofd-km=50` op de spoorrouter was inderdaad nodig zoals de brief voorspelde — zonder
die vlag zou het geïsoleerde 253 km-component onder de standaarddrempel vallen en b1 onterecht een stippel
worden. Bij het pinnen van via-punten zonder Overpass bleek een lokale pyosmium-bbox-scan op de geofabrik-extract
(highway=trunk/primary rond de bestemming) een volwaardige vervanging — sneller en preciezer dan de brief kon
voorzien, én het corrigeerde een corridor-aanname (R257 → R-255) die anders stilzwijgend fout was blijven staan.
De component-scan die de b4-stippel opleverde (kleine-klasse-wegennet rond de cargoterminal = losse eilandjes)
is dezelfde klasse als eerdere havenspoor-bevindingen (`cu-beilun-laadspoor`) maar dan op de wegkant — een
nieuwe, nog niet eerder in dit project expliciet benoemde variant: een luchthaven-cargozone kan net zo goed
topologisch geïsoleerd zijn in OSM als een havenspoor.
