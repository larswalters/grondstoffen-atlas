# Routebrief (licht) · koper — Cerro Verde → La Joya → Matarani → Toyo (Japan)

**stroom-id:** `koper-cerroverde-toyo` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** koperconcentraat van de Cerro Verde-concentrator (SMCV, Arequipa; Freeport 55,1 %, SMM 16,8 %, Sumitomo Corp 4,2 %) per **truck** over de mijnweg langs de Quebrada San José naar het PeruRail-transferstation **La Joya**, per **spoor** (Ferrocarril del Sur) naar de Tisur-concentraatpier **Muelle F** in Matarani, per **zeeschip** over de Stille Oceaan naar de Seto-binnenzee en via een haven-aanloop naar de eigen ertslosberth van de **Toyo-smelter van SMM** (Saijo/Niihama, Ehime) — daar stopt deze brief. **Bestemming Toyo = aannemelijk: één bron** (afgeleid uit het 21 %-aandeel, geen afnamebron).
**Welke as van het verhaal:** Peru-concentraat naar een Japanse smelter van de aandeelhouder. Cerro Verde **430,5 kt Cu in concentraat/kathode, 2024** (mining.com-ranking, via koper-sitelaag [8]); SMM-productieplan boekjaar t/m maart 2027: 389 kt [9]. Het deel dat naar Toyo gaat is **niet gepubliceerd** (pro-rata 21 % ≈ 90 kt is een eigen rekensom, geen bron) — geen volumetoewijzing aan Toyo. Toyo-capaciteit 450 kt Cu/j [1].

## 1 · Ketenkaart
```
Cerro Verde-concentrator ──(b1 truck · mijnweg Quebrada San José · OSM-pad 47 km)──► La Joya-station (truck→spoor)
  `cu-cerroverde-laad`                                                                  `cu-lajoya-overslag`
──(b2 spoor · Ferrocarril del Sur La Joya–Matarani · 59 km)──► spooreinde ──(b3 stippel 1,7 km)──► Muelle F `cu-matarani-kade`
──(b4 stippel haven-aanloop 72,1 km)──► zeeknoop 489 ──(b5 zee · MARNET · 17.190 km)──► Niihama-zeeknoop 5746
──(b6 stippel haven-aanloop 23,3 km)──► Toyo-kade `cu-toyo-kade` ⏹ stoppunt (smelter; eigen berth ≤ 30.000 t)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | concentrator → La Joya-station (**openbare-wegbenadering van de 40 km Cerro Verde-privéweg**) | OSM: tertiary (access=private) → secondary (asfalt, 60 km/u) door de Quebrada San José; passeert het station op 40 m [3][11] | **hemelsbreed 36 km, geen gepubliceerde wegkm**; privéweg "40 km" [3] (indicatie); OSM-pad **47,0 km** (40,4 km vanaf de put-snap; eerste 16,3 km = ringweg om de put) | `maak_stroombeen_weg` — nieuw profiel (extract peru), lokaal getest | nee |
| b2 | A | spoor | La Joya → spooreinde Matarani | Ferrocarril del Sur (PeruRail) La Joya–Matarani [4] | **~60** (MINEM-milieudossier, zoekfragment [5]); gemeten **59,0** (−1,7 %) | `toets_spoorroute` (`BAKE_SUFFIX=-raw`, `--hoofd-km=100`) | nee |
| b3 | A | spoor | spooreinde → Muelle F | havenspoor/pier niet in het net | 1,7 (hemelsbreed) | letterlijke kopie lasbambas b4 | **ja** — haventerrein, geen net |
| b4 | B | zee | Muelle F → MARNET-zeeknoop 489 (-17.3000,-72.7000) | — | 72,1 (haven-aanloop; kade 70,6 km van de knoop) | letterlijke kopie `aanloop-matarani.geojson` | **ja** — MARNET reikt niet |
| b5 | B | zee | zeeknoop 489 → Niihama-zeeknoop 5746 (34.0720,133.0479) — **aannemelijk: bestemming Toyo afgeleid uit 21 %-aandeel, geen afnamebron** | Stille Oceaan rechtstreeks (geen kanaal) | MARNET gemeten **17.190,4** (hemelsbreed 16.865, +1,9 %) | MARNET (`--been zee`) | nee |
| b6 | B | zee | zeeknoop 5746 → Toyo-kade (33.9505,133.2295) | — | 23,3 gemeten (kade 21,5 km hemelsbreed van de knoop; omweg 1,08) | `maak_havenaanloop` (**3 min 18 s**, onder timeout 300) | **ja** — Seto-binnenzee buiten het net |

Scratch-keten (hecht_marnet, naar scratchpad, niet geregistreerd): 6 benen, **17.393,7 km**, naden: weg→spoor 0,2 km (snap 0,16 km), spooreinde/aanloop/zeeknoop 0 m.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-cerroverde-laad` | mijn / concentrator | Cerro Verde, concentrator Uchumayo/Yarabamba | -16.5170, -71.5966 | [2][8] | bron-gelegd (z15 gezien: kluster ronde indikkers/tanks en procesgebouwen 1,5 km N van de put, tailingbekken noordelijk; kruis ligt ~1,5 km NNO van de sitelaag-centroïde in de put -16.5300,-71.6000) |
| `cu-lajoya-overslag` | overslag truck→spoor | PeruRail-station La Joya (transfer) | -16.7245, -71.8598 | [3][4] | aannemelijk (z15/z16 gezien: station op de Ferrocarril-lijn met lang laadspoor, wissels en een blauw overdekt gebouw; de concentraattransferbak zelf niet herkend; ontwerp-anker -16.7095,-71.8578 lag op vrije lijn en is verlaten) |
| `cu-matarani-spooreinde` | spooreinde | Matarani, spooreinde | -17.0049, -72.0964 | koper-lasbambas-matarani §3/§9 | bestaand — hergebruikt |
| `cu-matarani-kade` | overslag spoor→zee | Tisur Muelle F, concentraatpier | -17.0044, -72.1124 | [6]; koper-lasbambas-matarani §3 | bestaand — hergebruikt (bron-gelegd, z16) |
| `cu-niihama-zeeknoop` | zee-knoop | MARNET-zeeknoop 5746 | 34.0720, 133.0479 | nikkel-taganito-niihama b3/b4 | bestaand — hergebruikt (knoop, niet de lijn) |
| `cu-toyo-kade` | losplek / smelter | Toyo Smelter & Refinery (SMM), eigen ertslosberth | 33.9505, 133.2295 | [1][10] | aannemelijk (z15/z16 gezien: smelterterrein aan de kust met haventerminals en een bulkcarrier langs de kade; complex-anker 33.9493,133.2305; een lange smalle steiger loopt 0,7 km de baai in, functie niet vastgesteld, niet getekend; dit is een andere kade dan de Niihama Nickel Refinery 33.9669,133.2658) |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Keuze b1: de mijnweg door de Quebrada San José (OSM-pad 47 km) tegenover de openbare omweg via AR-115 → PE-34A → PE-1S (La Joya-stad), die langer is en het station niet raakt. Alle drie op de secondary-way (OSM way 286975126), niet in Arequipa of La Joya-dorp.
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1 | begin secondary, zuid van de put | -16.5681, -71.6494 | dwingt de mijnweg af i.p.v. AR-115/PE-34A; overgang private tertiary → secondary |
| b1 | 2 | km 9 door de Quebrada San José | -16.5958, -71.7226 | houdt de lijn op de kloofweg |
| b1 | 3 | km 19 | -16.6591, -71.7874 | idem; voorkomt afbuigen naar PE-1S |
| b2 | — | geen via nodig | — | één lijn La Joya–Matarani; 1 omkering (162°) aan de La Joya-kop = echte kopmaak op het transferspoor |

Profiel-recept (lon, lat): anker (-71.5966,-16.5170) → via (-71.6494,-16.5681) → (-71.7226,-16.5958) → (-71.7874,-16.6591) → anker (-71.8599,-16.7242); `extracts ["peru"]`, `refs []`, `gepubliceerdKm 40`, `vensterKm 45`, `corridorKlassen ["tertiary"]`, **`eindToegangPrivaat True` (verplicht — zonder faalt de scan)**. pyosmium is geblokkeerd: `--bron overpass`; de standaardspiegels falen, `overpass.private.coffee` werkte.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Cerro Verde-concentrator | SMCV (Freeport 55,1 %) | erts → Cu-concentraat | 430,5 kt Cu/j (2024) | [8] |
| Toyo Smelter & Refinery | SMM | concentraat (20–30 % Cu) → kathode, goud, zilver | 450 kt Cu/j | [1] |

## 6 · Stoppunt
Bij de Toyo-kade: de smelter is het einde van de gedocumenteerde keten; geen bron noemt een afnemer van Toyo-kathode. Fase D/E vervallen.

## 7 · Open punten
1. **Bestemming Toyo niet bevestigd.** SMM noemt Toyo en de Cerro Verde-aandelen, maar geen pagina koppelt Cerro Verde-lading aan Toyo; de claim "twee maanden zeereis naar Toyo" is niet teruggevonden. Een deel gaat naar andere smelters. Eén-bron-aanname staat in de beennaam b5.
2. **Werkelijk truckbeen = privéweg** (~2016 [3]); OSM kent alleen een benadering. Het eerste stuk (16,3 km) is een ringweg om de put; geen gepubliceerde wegkm, de ±15 %-toets (+17 % t.o.v. 40 km) is een indicatie.
3. **La Joya-transferbak niet herkend** op z16; het transfercentrum dat PeruRail nu noemt is Pillones/La Joya [4], de exacte plek niet gepubliceerd.
4. **Spoor 59,0 km** tegen "~60" uit een zoekfragment van het MINEM-dossier; het volledige document niet gelezen.
5. **Volume naar Toyo niet gepubliceerd**; geen volumetoewijzing. Sitelaag-centroïde `w-cerro-verde` ligt 1,5 km van het concentrator-anker (centraal gelijktrekken, zie §3).
6. **Toyo-steiger** (0,7 km de baai in): functie onbekend; kade-anker blijft de kust.

## 8 · Bronnen
[1] SMM, Toyo Smelter & Refinery — eigen berth tot 30.000 t, concentraat uit SMM-belangen in Noord-/Zuid-Amerika en Australië — https://www.smm.co.jp/en/corp_info/location/domestic/toyo/
[2] SMM, overseas locations — Cerro Verde: SMM 16,8 %, Freeport 55,1 %, Sumitomo Corp 4,2 %, overig 23,9 %; producten concentraat + kathode — https://www.smm.co.jp/en/corp_info/location/overseas/
[3] ProActivo, interview Julia Torreblanca (Cerro Verde) — privéweg 40 km langs de Quebrada San José naar het PeruRail-station in La Joya, daar naar de trein naar Matarani — https://proactivo.com.pe/entrevista-exclusiva-julia-torreblanca-cerro-verde-tiene-la-concentradora-mas-grande-construida-en-una-sola-fase/
[4] PeruRail Cargo, operationeel net — Mollendo/Matarani–Arequipa, transfercentra Pillones/La Joya — https://www.perurail.com/cargo/operational-network/
[5] MINEM, milieudossier Cerro Verde-uitbreiding (spoor La Joya–Matarani ~60 km; via zoekfragment, niet volledig gelezen, via haalbaarheidstoets)
[6] MundoMarítimo, 2016-02-15 — eerste verscheping 5.000 t Cerro Verde-concentraat op Muelle F, Tisur — https://www.mundomaritimo.cl/noticias/realizaron-primer-embarque-en-muelle-f-del-puerto-peruano-de-matarani
[7] Freeport-McMoRan Form 10-K FY2025 (sec.gov, fcx-20251231.htm) — concentraat "approximately 70 miles by truck and by rail to the Port of Matarani" (via haalbaarheidstoets)
[8] mining.com, "RANKED: World's biggest copper mines" (2024-data) + FCX 10-K 2024 — https://www.mining.com/featured-article/ranked-worlds-biggest-copper-mines/ · https://s22.q4cdn.com/529358580/files/doc_financials/10-K/10_k2024.pdf
[9] SMM-productieplan boekjaar t/m maart 2027 (389 kt), via ketenontwerp
[10] OSM landuse 住友金属鉱山 東予工場 33.9493/133.2305 (Nominatim), via koper-sitelaag `w-toyo` — v2/design/koper-sitelaag.json
[11] OSM via overpass.private.coffee, 2026-10-09 — way 286975126 (secondary, asfalt, 32,2 km, La Joya-station op 40 m), way 480117520 (tertiary, access=private)
[12] Sumitomo Corporation, copper business — investeert in Cerro Verde, levert concentraat aan smelters in en buiten Japan — https://www.sumitomocorp.com/en/jp/enrich/contents/global_1028
Satellietblik (Esri live, 2026-10-09, `v2/build-cache/satcheck/`): `sat-koper-cerroverde-toyo-cu-cv-put.png` (z14) · `-cu-cv-concentrator.png` (z15) · `-cu-lajoya.png` (z15) · `-cu-lajoya-z16.png` · `-cu-toyo-kade.png` (z15) · `-cu-toyo-steiger.png` (z16).

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)
**Bestand:** `v2/data/stroomroute-koper-cerroverde-toyo.json` (59,6 KB, versie 2, `lonlat`) · **6 benen · 17.393,7 km · 2.986 punten · 4 markers** · recept: `bak_koper_cerroverde_toyo` in `v2/tools/bak_stromen.sh`, weg-profiel `koper-cerroverde-toyo-cerroverde-lajoya` in `v2/tools/maak_stroombeen_weg.py`.

| # | modaliteit | km | naad naar volgend been | stippel | geometrie |
|---|---|---|---|---|---|
| b1 | truck | 47,0 | 133 m (weg→spoor, procesgat bij het transferspoor) | nee | `maak_stroombeen_weg`, extract peru, `--bron overpass` (786 pt) |
| b2 | spoor | 59,2 | 0 | nee | `toets_spoorroute` (`BAKE_SUFFIX=-raw`, `--hoofd-km=100`), 200 edges, 343 pt |
| b3 | spoor | 1,7 | 0 | ja — haventerrein, geen net | letterlijke kopie lasbambas b4 |
| b4 | zee | 72,1 | 0 | ja — MARNET reikt niet (kade 70,6 km van knoop 489) | letterlijke kopie `aanloop-matarani.geojson` (lasbambas b5) |
| b5 | zee | 17.190,4 | 0 | nee (aannemelijk: één bron voor de bestemming, in de beennaam) | MARNET, 72 edges, 1.759 pt, snap 0,000/0,000 |
| b6 | zee | 23,3 | — (stoppunt) | ja — Seto-binnenzee buiten het net | `maak_havenaanloop` (37 pt), kade 21,5 km van zeeknoop 5746 |

**Toets (handleiding §5).** Spoor 59,2 tegen ~60 (−1,3 %) en zee 17.190,4 tegen hemelsbreed 16.865 (+1,9 %) vallen binnen de norm. Truck 47,0 km tegen de privéweg-opgave van 40 km = **+17,5 %, buiten ±15 %**; er is geen gepubliceerde wegkm voor de openbare benadering, dus dit is een indicatie en geen afwijking van een norm (bevinding, geen via-punt bijgeschoven). Geen naad > 5 km (grootste 133 m). Markers 0,0 / 0,035 / 0,0 / 0,0 km van de lijn. `toets_knikken`: 9 knikken ≥ 60° waarvan 1 omkering (spoor, 162° aan de La Joya-kop = echte kopmaak op het transferspoor, geen terugloop) en 7 spikes in het eerste truckstuk (OSM-zigzag/ringweg om de put, R 6–83 m). Geen been ≥ 5 km met omwegfactor 1,000 (b3 is 1,7 km, b4/b6 zijn over-water-routes). `json.load` slaagt, modaliteiten in {zee, truck, spoor}, elk been ≥ 2 punten.

**Toelichting per stippel.** b3 en b4 zijn letterlijke kopieën van koper-lasbambas-tongling (zelfde Muelle F en zelfde aanloop naar zeeknoop 489), geen tweede versie. b6: Toyo-kade 21,5 km van zeeknoop 5746, dus haven-aanloop over water (0 km over land gemeten); stippel omdat MARNET de Seto-binnenzee niet kent.

**Recept en herkomst weg-tussenuitvoer.** `koper-cerroverde-toyo-weg-cerroverde-lajoya.geojson` stond al op schijf uit de scratch-bake (OSM via `overpass.private.coffee`). Bij het bakken is de scan opnieuw geprobeerd met een wrapper die de standaardspiegels naar `overpass.private.coffee` omleidt: alle spiegels gaven die dag HTTP 500, dus het bestaande bestand is **ongewijzigd hergebruikt** (byte-identiek bevestigd). Het profiel is vastgelegd zodat de scan reproduceerbaar is zodra een spiegel weer antwoordt.

**Lessen.** (1) `eindToegangPrivaat True` is voor dit profiel verplicht (mijnweg access=private); zonder faalt de scan. (2) De truck-benadering volgt de OSM-ringweg om de put; de +17,5 % is een eigenschap van de benadering, niet van een via-punt. (3) Bestemming Toyo blijft aannemelijk (§7.1); fase D/E vervallen. (4) De slot-hulpfunctie met `rm -rf "$d"` wordt door de shell-veiligheidscheck geweigerd; neem het slot met een literal pad en geef het vrij met `rmdir`.
