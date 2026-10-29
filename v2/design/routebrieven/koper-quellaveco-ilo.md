# Routebrief (licht) · koper — Quellaveco → Terminal Portuario Engie Ilo (Peru)

**stroom-id:** `koper-quellaveco-ilo` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 12) · **status:** gebakken
**Keten in één zin:** koperconcentraat van de Quellaveco-mijn (Anglo American 60%, Mitsubishi 40%, Moquegua) gaat per **truck** (aannemelijk: één bron) naar het Terminal Portuario Engie in Ilo, waar het in een concentraatloods en over een bandsysteem en pier op zee gaat; de lijn stopt op die kade.
**Welke as van het verhaal:** *Zuid-Peru, de tweede kustuitgang naast Southern Copper* — Quellaveco gebruikt de haven van het Engie-energiecomplex (voorheen Enersur) in plaats van een eigen of SCC-haven. Jaarvolume: **306,3 kt Cu per jaar in 2024** (Anglo American Q4 2024 production report, 100%-basis, contained metal; "Copper Peru" = Quellaveco) [1]. Eerste lading sept. 2022: 35.400 t concentraat naar China en Japan, geen smelter genoemd [2].

## 1 · Ketenkaart
```
Quellaveco-mijn `cu-quellaveco-mijn` ──(b1 truck · hemelsbreed 96 km, geen wegkm · router 160,8 km, aannemelijk: één bron voor truck)──►
Terminal Portuario Engie Ilo `cu-engieilo-kade` ── stoppunt (geen zeebeen: afnemer niet gebrond)
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `cu-quellaveco-mijn` → `cu-engieilo-kade` (**aannemelijk: één bron voor truck**) | OSM-corridor: mijnwegen → TA-105 → MO-107 → TA-100 → PE-1S → PE-36D → kustweg naar de terminal; **geen Moquegua/Torata** (zie §4) | **hemelsbreed 96 km, geen wegkm**; router 160,8 (indicatie); een 2019-rapport noemt 165 (ongecontroleerd) — de ±15%-toets is dus geen norm | maak_stroombeen_weg (extract `peru`) | nee |

Geen zeebeen (bindend, haalbaarheidstoets): geen smelter of afnemer gebrond, en de kade ligt 127,2 km van de dichtstbijzijnde MARNET-zeeknoop (490: -18.9000, -71.0000), dus een zeebeen zonder bestemming zou alleen een haven-aanloop van 127 km zijn. Geen haven-aanloop. Geen stippel: kop snapt op 0,01 km, staart op 0,31 km.

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `cu-quellaveco-mijn` | mijn / laadplek (kop b1) | Quellaveco-mijn (Anglo American / Mitsubishi) | -17.1022, -70.6163 | [3][4] | **aannemelijk** (z14/z15 gezien: grote open pit met gele/blauwe bermen en afvalbergen, installatiestrook met gebouwen langs de zuidrand, tailingsvijvers west; het punt ligt op het OSM-industrieterrein oostelijk in het complex; de concentrator is op deze, oudere opname niet apart aanwijsbaar — `sat-koper-quellaveco-ilo-cu-mijn-z14.png`, `-cu-conc-z15.png`) |
| `cu-engieilo-kade` | overslag / kade (staart b1, stoppunt) | Terminal Portuario Engie, Ilo (voorheen Enersur) | -17.7706, -71.1908 | [2][5][6] | **bron-gelegd** (z15 gezien: tankpark met witte tanks, bandsysteem en gebouwen op het terrein, pier die zuidwestwaarts de zee in loopt met een schip aan het eind, energiecentrale ten zuiden — `sat-koper-quellaveco-ilo-cu-kade-z15.png`) |

Sitelaag `w-quellaveco` staat op -17.1022, -70.6164 (10 m ten westen); zelfde punt, centraal gelijktrekken. Geen anker bestond al voor deze kade (geen andere brief noemt Engie Ilo; Toquepala/Cuajone-ankers liggen bij de SCC-smelter, -17.505, -71.359).

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
Geen (bindend, haalbaarheidstoets): één route zonder via-punten, snap 0,01 en 0,31 km, 160,8 km, eerste mijl 18,6 km tertiary en unclassified, laatste mijl 0,19 km service. De router volgt TA-105 (18,6–55,6 km), MO-107 (55,9–89,7), TA-100 (89,7–104,8), PE-1S (104,8–120,8), PE-36D en daarna unclassified (122,5–159,1).
⚠️ **Corridorkeuze bestaat wél, maar het net kiest voor ons.** De route via Torata en Moquegua (PE-36A, daarna Moquegua–Ilo 91 km) is in OSM niet aan de mijn gekoppeld: de proefrun mijn → Torata gaf 130,7 km (totaal 248,9 km, +51%). Of de werkelijke vrachtwagens de Moquegua-weg of de zuidelijke mijnwegen nemen is niet gebrond; de brief tekent de route die OSM verbindt en zegt dat erbij (§7). Een via-punt bij Torata of Moquegua is bewust niet toegevoegd.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Quellaveco-concentrator | Anglo American | erts → Cu-concentraat | 2024: 306,3 kt Cu in concentraat (recovery 79% in Q4) | [1] |
| Concentraatloods en scheepsbelader Engie Ilo | Engie Energía Perú | concentraat → scheepslading (bandsysteem, 1.200 t/uur) | loods 80.000 t (2022), gepland 65.000 t (2018) | [2][6] |

## 6 · Stoppunt
De brief stopt bij de Engie-kade: de eerste lading ging naar China en Japan zonder genoemde smelter, en geen bron noemt een vervolgbestemming of afnemer voor de lopende volumes (fase B, C, D, E vervallen).

## 7 · Open punten
- **Truckroute niet gebrond:** de modaliteit staat in één bron (NS Energy: concentraat "trucked to the port of Enersur in Ilo") [5]; de wegkilometers niet. 160,8 km is een OSM-routelengte, geen bedrijfscijfer; 165 km uit een 2019-rapport is niet teruggevonden. Wie de werkelijke corridor (Moquegua of zuidelijke mijnwegen) vindt, kan de via-punten later zetten.
- **Mijnweg-toegang:** de eerste 18,6 km zijn tertiary/unclassified, mogelijk deels mijn- of privéweg; niet gecontroleerd.
- **Concentrator niet aanwijsbaar** op de huidige Esri-opname; het anker is het OSM-terrein van de mijn.
- **Pier gedeeld met Engie** (offshore-werk "shared use" [6]): de precieze belading en de plek van de loods op het terrein zijn niet apart gelegd; het kadepunt ligt op ca. 0,6 km van de pierwortel.
- **Afnemer/smelter** (China, Japan) niet genoemd: geen zeebeen.
- Aandeel van het Quellaveco-volume dat via Engie Ilo gaat (i.p.v. andere uitgangen) is niet gekwantificeerd; 306,3 kt is het mijnvolume.

## 8 · Bronnen
[1] Anglo American, Q4 2024 Production Report (29-01-2025): Copper Peru 306.300 t in 2024 (2023: 319.000), Quellaveco Q4 90.200 t, recovery 79%; ownership 60%. https://www.angloamerican.com/~/media/Files/A/Anglo-American-Group-v9/PLC/media/press-release/releases/2025pr/q4-2024-production-report.pdf
[2] Mundo Marítimo, "Terminal Portuario Engie Perú embarca concentrado de cobre del proyecto minero Quellaveco" (2022-09-29): vessel Balabac Island, 35.400 t, China en Japan, loods 80.000 t, band 1.200 t/uur. https://mundomaritimo.cl/noticias/terminal-portuario-engie-peru-embarca-concentrado-de-cobre-del-proyecto-minero-quellaveco
[3] Wikipedia, "Quellaveco mine" (coördinaat -17.1043, -70.6199; Anglo American, productie sinds 2022, 300 kt Cu/jaar). https://en.wikipedia.org/wiki/Quellaveco_mine
[4] OpenStreetMap (ODbL) via Nominatim: way 1200723255 "Quellaveco" (industrial, -17.1021984, -70.6163492); `v2/design/koper-sitelaag.json` w-quellaveco.
[5] NS Energy Business, Quellaveco-projectpagina: "The produced concentrates will be trucked to the port of Enersur in Ilo for shipping to destination smelters." https://www.nsenergybusiness.com/?p=195040
[6] Mundo Marítimo, "Puerto de Engie Perú: Anglo American construirá bodega de concentrados de cobre de la mina Quellaveco" (2018-08-24): loods 65.000 t, gesloten band, scheepsbelader op de Engie-terminal in Ilo. https://mundomaritimo.cl/noticias/puerto-de-engie-peru-angloamerican-construira-bodega-de-concentrados-de-cobre-de-la-mina-quellaveco
[7] Gestión, "Quellaveco: Anglo American se prepara para su segundo embarque de cobre" (2022-10-13): eerste lading naar het terminal portuario in de provincie Ilo. https://gestion.pe/economia/quellaveco-anglo-american-se-prepara-para-su-segundo-embarque-de-cobre-noticia/
[8] Esri World Imagery via `v2/tools/sat_check.py`, 2026-10-29: `v2/build-cache/satcheck/sat-koper-quellaveco-ilo-cu-mijn-z14.png`, `-cu-conc-z15.png`, `-cu-kade-z15.png`.
[9] Proefrunnen `maak_stroombeen_weg` via `wegscan_puur.py` (extract peru, 2026-10-29): 160,8 km (zonder via-punten) en 248,9 km (via Torata en Moquegua); haalbaarheidstoets 170,3 km met dezelfde snaps.

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 12)
**Bestand:** `v2/data/stroomroute-koper-quellaveco-ilo.json` · versie 2, lonlat · 67,7 KB · 1 been, 160,8 km, 3.155 punten, 2 markers. Bakken: `bash v2/tools/bak_stromen.sh koper-quellaveco-ilo` (functie `bak_koper_quellaveco_ilo`).

| # | modaliteit | km | geometrie | stippel |
|---|---|---|---|---|
| b1 | truck | 160,8 | profiel `koper-quellaveco-ilo-quellaveco-engieilo` (extract peru, `wegscan_puur.py`) | nee |

**Recept:** profiel zonder via-punten, refs leeg, gepubliceerdKm 165 (ongecontroleerd), vensterKm 40, eindKlassen incl. track; uit `koper-quellaveco-ilo-weg-quellaveco-engieilo.geojson`. Snap kop 0,01 km, staart 0,31 km; 15 keerlussen gesnoeid (160,6 naar 160,4 km); eerste mijl 18,6 km tertiary/unclassified, laatste mijl 0,19 km service. Markers `Quellaveco-mijn` en `Terminal Portuario Engie Ilo` liggen op 0,0 km van de lijn.

**Toets:** de lengtetoets (160,4 tegen 165) = -2,8%, maar 165 is geen wegkm-bron en hemelsbreed is 96 km: dit is een indicatie, geen norm. Geen naden (1 been). `toets_knikken`: 27 knikken, 0 omkeringen, 0 terugloop; de spikes zijn bochtige mijnweg-serpentines en de ankerrand (R 4 tot 53 m). Rechte-benen-toets: geen melding voor dit been.

**Geen stippel, geen aanloop, geen vlucht, geen leiding:** bewust (brief par.2): geen afnemer gebrond, kade 127 km van MARNET-zeeknoop 490, dus geen zeebeen. De lijn eindigt op de Engie-kade.

**Lessen:** (1) de Moquegua/Torata-route is in OSM niet aan de mijn gekoppeld; het net kiest de zuidelijke mijnwegen (TA-105/MO-107), de werkelijke vrachtroute is niet gebrond. (2) De mijnweg (eerste 18,6 km) kan privé zijn. (3) Het profiel is in een eerdere proefrun al eens gescand (andere cache-hash door eindKlassen); de tweede run kostte 1 minuut.
