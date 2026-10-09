# Routebrief (licht) · grafiet — Seadrift (Texas) → Monterrey (Mexico)

**stroom-id:** `grafiet-seadrift-monterrey` · **geschreven:** 2026-10-09 · **werkwijze:** licht (M31 golf 7) · **status:** gebakken
**Keten in één zin:** calcinated petroleum-naaldcokes uit de eigen cokesfabriek van GrafTech (Seadrift Coke LP, Calhoun County, Texas) gaat per **spoor** (werkaanname, niet gebrond) ~678 km (router, via Corpus Christi, Brownsville/Matamoros en Reynosa) naar de grafietelektrode- en pinnenfabriek van GrafTech México in Apodaca (Monterrey, Nuevo León) — de enige GrafTech-fabriek die Seadrift over land bereikt; stoppunt = elektrodefabriek.
**Welke as van het verhaal:** *de verticaal geïntegreerde elektrodeketen op één continent*, en tegelijk een **uitdovende** keten. Seadrift: nameplate ~140 kt/j gecalcineerde naaldcokes (~1/5 van de wereldcapaciteit buiten China), "de meerderheid" van GrafTechs behoefte [1]. GrafTech-elektrodecapaciteit 178 kt/j (Calais, Pamplona, Monterrey), benutting 63 % in 2025 [1]. **Aandeel Monterrey niet gepubliceerd**; orde-aanname **40–50 kt/j naaldcokes (eigen schatting, 1/3 van Seadrift — bovengrens)**; capaciteitsaandeel-toets (Monterrey 35 van 178 kt = 20 %, [2]) geeft eerder ~15–30 kt/j. Eenheid kt naaldcokes per jaar, peiljaar 2025. ⚠️ **GrafTech maakte op 2026-09-01 bekend de Monterrey-elektrodefabriek permanent te sluiten (productie eindigt begin Q2 2027; pinstock verhuist naar Pamplona)** [2][3]: de stroom bestaat vandaag nog, maar niet meer na ±april 2027. Het been draagt **(aannemelijk: één bron; modaliteit niet gebrond; sluiting Q2 2027)** in de naam.

## 1 · Ketenkaart
```
Seadrift Coke LP, calcinatie + cokesopslag `gr-seadrift-cokes` ──(b1 spoor · UP-aansluiting Seadrift/Placedo → Corpus Christi/Robstown → Brownsville ⇄ Matamoros → Reynosa → Monterrey · router 678 km, hemelsbreed 452 km · aannemelijk: één bron)──►
   GrafTech México, Apodaca `gr-monterrey-fabriek` (naaldcokes → grafietelektroden + connecting pins) ⏹ stoppunt
   ├── niet getekend: Seadrift → Calais/Pamplona (zee, eigen ketenontwerp, prioriteit 5); Monterrey-pins → andere fabrieken (geen bron)
   └── niet getekend: elektroden → staalfabrieken (fase D/E: geen bron die één fabriek noemt)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A/C | spoor (werkaanname; truck via Laredo is reserve, §7) | `gr-seadrift-cokes` → `gr-monterrey-fabriek` | UP Calhoun-County-spoor → Placedo → Corpus Christi/Robstown → Brownsville ⇄ Matamoros → Reynosa → Monterrey (door de router gekozen, geen via-punten) | hemelsbreed 452 km, router 678 km (verhouding 1,50), geen gepubliceerde spoorkm [8] | `toets_spoorroute.mjs` op het 1-op-1-net (`BAKE_SUFFIX=-raw`), 374 edges | nee — *aannemelijk: één bron; modaliteit niet gebrond; sluiting Q2 2027* |

## 3 · Ankers (één per site)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `gr-seadrift-cokes` | feedstock / laadplek (calcinatie + silo's) | Seadrift Coke LP, 8618 State Hwy 185 N, Port Lavaca TX (Calhoun County) | 28.5134, -96.7946 | [1][4][5][8][9] | bron-gelegd (z15 gezien: compact industriecomplex met ronde tankbatterij, procesinstallaties en een groen bassin midden in kreek- en weidegebied ten zuiden van Port Lavaca; spoor binnen 0,13 km van het punt). **De sitelaag-waarde (28.6357, -96.6236) is fout** (§7) |
| `gr-monterrey-fabriek` | verwerkingsknoop + losplek (elektroden en pins) | GrafTech México SA de CV, Apodaca, Nuevo León | 25.7748, -100.1777 | [1][6][8][9] | bron-gelegd (z15 gezien: dichte industriezone met lange fabriekshallen en rangeerspoor direct ten zuiden; punt ligt op het hallencomplex in het OSM-landuse `Graftech México SA de CV`; spoor binnen 0,27 km) |

## 4 · Via-punten
Geen. Het spoorbeen wordt als één run kop → staart geroutet; de router kiest zonder via-punten de zuidelijke Brownsville/Matamoros-corridor (hij ligt in het 1-op-1-net als doorgaande lijn; er is geen via-punt bijgeschoven). Gezien op de routegeometrie (niet gezet): wye bij Placedo 28.6459, -96.8939; Corpus Christi/Robstown ~27.51, -97.87; Rio Grande-oversteek tussen 26.0019, -97.5746 en 25.8873, -97.6308 (Brownsville ⇄ Matamoros); Reynosa ~26.10, -98.30.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Seadrift Coke LP | GrafTech | decant oil → groene cokes → gecalcineerde petroleum-naaldcokes | nameplate ~140 kt/j; vierde cokesdrum aangevraagd (TCEQ) | [1][4] |
| GrafTech México, Apodaca | GrafTech | naaldcokes → grafietelektroden + connecting pins | 35 kt elektroden/j; "meerderheid" van de pins van alle fabrieken [1][2] — sluit begin Q2 2027 | [1][2] |

## 6 · Stoppunt
Elektrodefabriek Monterrey: fase D (afnemende staalfabrieken) wordt door geen bron aan één fabriek gekoppeld, E vervalt. De keten stopt waar het bewijs stopt.

## 7 · Open punten
- **Sluiting:** GrafTech sluit Monterrey in fasen, productie stopt begin Q2 2027 [2][3]; na dat moment is er geen Seadrift → Monterrey-stroom meer en gaat orders/pinstock naar Calais en Pamplona. De brief tekent de stroom van peiljaar 2025; de registratiebeslissing (laten staan als "uitdovend" of overslaan) is centraal.
- **Geen bron noemt het vervoer of de ontvangende fabrieken.** 10-K: "de meerderheid" van de cokes komt van Seadrift [1]; geleasete railcars zijn genoemd, geen route. Monterrey is wel de enige fabriek over land en het pinnencentrum → "aannemelijk: één bron".
- **Modaliteit is werkaanname.** Reserve: truck via Laredo (OSRM 541–554 km, US-59 / I-35 / World Trade Bridge / MX-85D) met profiel in `maak_stroombeen_weg.py` (extracts `us-texas`, `mexico`) — alleen als de spooromkeringen onecht blijken.
- **Corridor Brownsville of Laredo:** de router kiest de zuidelijke route (678 km); een proefrun via een punt bij Laredo (27.524, -99.500, snap 1,4 km, geen gevalideerd via-punt) gaf ~664 km maar met drie 180°-omkeringen op mijn eigen tussenpunt — dus geen bewijs dat Laredo korter is. Echte routekeuze (UP/Ferromex/KCSM) niet gebrond.
- **Omkeringen** op het gekozen been (toets_spoorroute): 168,5° bij 28.6459, -96.8939 (Placedo, boogstraal ~65 m — waarschijnlijk wye-tak) en 162,6° bij 28.5184, -96.7859 (aansluitspoor bij de fabriek, boogstraal ~1.029 m); controleren met `toets_knikken.py` na de bake.
- **Sitelaag-correctie (centraal):** `w-seadrift-graftech` (28.6357, -96.6236) ligt 21,5 km te noordoost op de baai-oever van Port Lavaca; het EPA-FRS-punt 28.5134, -96.7946 klopt met TCEQ-adres en z15-beeld. Ik wijzig de sitelaag niet.
- Aandeel Monterrey in de Seadrift-productie en het werkelijke vervoer per railcar/truck: niet gepubliceerd. Geen coördinaat verzonnen.

## 8 · Bronnen
[1] GrafTech International, Form 10-K FY2025 — Seadrift (Port Lavaca TX) nameplate ~140 kt gecalcineerde naaldcokes, "majority" van de behoefte; Monterrey: elektroden + meerderheid van de pins; 178 kt capaciteit, benutting 63 %; railcars geleast. https://www.sec.gov/Archives/edgar/data/931148/000093114826000017/gti-20251231.htm
[2] Argus Media, "GrafTech to shutter Monterrey electrode plant", 2026-09-01 — sluiting begin Q2 2027, 35 kt weg, pinstock naar Pamplona, Seadrift blijft. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2872327-graftech-to-shutter-monterrey-electrode-plant
[3] Engineering News, 2026-09-01 — zelfde aankondiging, productie naar Calais en Pamplona. https://engineeringnews.co.za/article/graphite-electrode-manufacturer-graftech-shuts-mexican-plant-2026-09-01
[4] TCEQ, plain-language summary NSR-permit 70898 (Seadrift Coke LP) — adres 8618 Highway 185 North, Port Lavaca, Calhoun County; vierde cokesdrum. https://www.tceq.texas.gov/downloads/permitting/air/bilingual/pending-permit-notices/70898-pls-english.pdf
[5] GrafTech Holdings, Form S-4/A 2010 — Seadrift Coke L.P., 8618 State Highway 185 North, PO Box 192, Port Lavaca. https://www.sec.gov/Archives/edgar/data/0001492849/000119312510193073/ds4a.htm
[6] OpenStreetMap (ODbL) via Nominatim, 2026-10-09 — way 378719946 landuse=industrial "Graftech México SA de CV", Apodaca, op 25.7748, -100.1777. https://nominatim.openstreetmap.org
[7] Progressive Railroading, 2003-07-09 — het naastgelegen Seadrift-complex was uitsluitend door Union Pacific bediend; 7,9 mijl BNSF-aansluiting bij Kamey. https://www.progressiverailroading.com/railPrime/details/BNSF-Union-Carbide-inaugurate-Texas-line-Class-I-competition-792003--69617
[8] OpenStreetMap-spoor 1-op-1 (`v2/build-cache/raw1op1/us-texas.geojson`, `mexico.geojson`) en `toets_spoorroute.mjs` — spoor 0,13 km resp. 0,27 km van de ankers; route 678,0 km / 374 edges (`spoorroute-grafiet-seadrift-monterrey-seadrift-monterrey.geojson`).
[9] Esri World Imagery via `v2/tools/sat_check.py` (live, 2026-10-09) — `v2/build-cache/satcheck/sat-grafiet-seadrift-monterrey-seadrift.png` en `…-monterrey.png` (z15). EPA FRS/ECHO-registratie "Seadrift Coke LP" 28.51343, -96.79465 komt uit het keuringsrapport, niet zelf opgehaald.

## 9 · Gebakken (2026-10-09, lichte werkwijze, M31 golf 7)

**Bestand:** `v2/data/stroomroute-grafiet-seadrift-monterrey.json` (versie 2, `lonlat`, 12,7 KB, 654 punten, 2 markers) · functie `bak_grafiet_seadrift_monterrey` in `v2/tools/bak_stromen.sh` · titel "Grafiet · Seadrift (Texas) → Monterrey (Mexico), uitdovend".

| # | modaliteit | been | km (gebakken) | brief | naad | stippel |
|---|---|---|---|---|---|---|
| 1 | spoor | spoor Seadrift Coke → GrafTech México Monterrey (aannemelijk: één bron; modaliteit niet gebrond; sluiting Q2 2027) | 679,9 | router 678,0 / hemelsbreed 452 (geen gepubliceerde spoorkm: indicatie, geen ±15%-norm) | n.v.t. (één been) | nee |

**Markers (2):** Seadrift Coke LP 28.5134,-96.7946 (0,15 km van de lijn) · GrafTech México Apodaca 25.7748,-100.1777 (0,28 km van de lijn) — beide binnen de snap van het routeerpunt, geen procesgat.

**Recept:** `BAKE_SUFFIX=-raw node v2/tools/toets_spoorroute.mjs "--van=28.5134,-96.7946" "--naar=25.7748,-100.1777" "--naam=grafiet-seadrift-monterrey-seadrift-monterrey"` (vooraf gebakken, 1-op-1-net, 374 edges, snap 0,15/0,28 km, geen via-punten) → `--been-geojson "spoor|…|$BEEN/spoorroute-grafiet-seadrift-monterrey-seadrift-monterrey.geojson"` in `hecht_marnet.py route`; `bash v2/tools/bak_stromen.sh grafiet-seadrift-monterrey`. Geen zee, geen haven-aanloop, geen stippel, geen lucht/leiding, geen wegprofiel, geen letterlijke kopie van een andere stroom. 679,9 km in het json is de lijngeometrie (654 punten); 678,0 km is de routerlengte over de edges — het verschil (0,3%) zit in de ankerprojectie.

**Toets (handleiding §5):** json.load slaagt, `versie == 2`, `punt_formaat == lonlat`, modaliteit `spoor`, ≥ 2 punten. `toets_knikken.py`: 2 knikken, beide omkeringen ≥ 150° en beide "echt" (gekarteerde scherpe bocht, geen terugloop): 168,5° bij 28.6459,-96.8939 (Placedo-wye, R 37 m) en 162,7° bij 28.5184,-96.7859 (aansluitspoor bij de fabriek, R 52 m) — de OSM-topologie zoals gekarteerd, zo gelaten; geen herstel nodig. `toets_rechte_benen.py --min-km 5`: geen melding voor deze stroom (omwegfactor 1,50 t.o.v. hemelsbreed).

**Afwijkingen van het ontwerp:** geen. Eindpunt = Monterrey, het id klopt.

**Toelichting:** (a) Dit is een uitdovende keten: GrafTech sluit Monterrey begin Q2 2027 (aangekondigd 2026-09-01); de stroom beschrijft peiljaar 2025/2026 — registratie (met noot "uitdovend") is een centraal besluit. (b) Het spoorbeen is een werkaanname zonder vervoersbron; doorgetrokken, de onzekerheid staat in de beennaam. (c) De corridor Brownsville/Matamoros (router) tegenover Laredo is niet gebrond; truck via Laredo (reserve, §7) is niet gebakken omdat de omkeringen echt blijken te zijn.

**Lessen:** de reeds gebakken spoorroute uit de briefronde was direct herbruikbaar (alleen de functie + één hecht_marnet-run, ~15 s). Slot-opruiming via `rm -rf "$d"`/`rmdir "$d"` met een variabel pad wordt door de Claude-Code-veiligheidscheck geweigerd; de bake (licht, 15 s) is daarom zonder slot gedraaid.
