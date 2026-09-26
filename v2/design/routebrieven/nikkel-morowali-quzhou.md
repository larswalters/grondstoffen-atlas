# Routebrief (licht) · nikkel — Morowali (IMIP) → Ningbo (Beilun) → Quzhou (China)

**stroom-id:** `nikkel-morowali-quzhou` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) ·
**status:** gebakken
**Keten in één zin:** nikkel-kobalt-tussenproduct (MHP) uit de HPAL-installaties van het Morowali
Industrial Park (IMIP, Bahodopi, Midden-Sulawesi) gaat per **zeeschip** (big bags/containers) naar
Ningbo (hergebruikt anker Beilun), en vandaar (aannemelijk: één bron voor de exacte afnemer) per
**truck** ~300 km naar de nikkelsulfaat-/precursorfabriek van Huayou in Quzhou (Zhejiang) — stoppunt.
**Welke as van het verhaal:** *de omgekeerde trechter* — het erts verlaat Indonesië niet, alleen het
al-verwerkte tussenproduct (MHP) gaat de zee op. Huayue (Huayou/Tsingshan-JV in IMIP) produceerde
**85,0 kt Ni + 8,0 kt Co in MHP in 2024** (nameplate 60 kt; peiljaar 2024) [7][6]; Quzhou's
sulfaatcapaciteit is 29,1 kt Ni/jaar (WoodMac 2021, verouderd — Huayue's huidige output is bijna
3× dat cijfer, dus het merendeel gaat elders) [9].

## 1 · Ketenkaart
```
IMIP-processing (Huayue e.a.) `ni-imip-hpal` ──(eigen terrein, niet getekend)──►
IMIP-jetty `ni-imip-jetty` ──(b1 zee · haven-aanloop ~90 km stippel + MARNET ~4.200 km)──►
Ningbo/Beilun `ni-beilun-losberth` (hergebruikt anker, koper) ──(b2 truck · G60-corridor ·
~300 km, aannemelijk: één bron voor de afnemer)──► Huayou Quzhou-fabriek `ni-quzhou-fabriek` ⏹ stoppunt
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | B | zee | `ni-imip-jetty` → `ni-beilun-losberth` | Golf van Tolo → Bandazee → Straat Makassar/Celebeszee → Zuid-Chinese Zee → Straat Taiwan | haven-aanloop ~90 [16] + zeebeen ~4.200 hemelsbreed (geen publicatie) | MARNET + maak_havenaanloop | aanloop bij IMIP: ja (MARNET reikt niet tot de kust — 1:10M-kust kent de haven niet); bij Beilun: nee (hergebruikt anker, al aangesloten) |
| b2 | C | truck | `ni-beilun-losberth` → `ni-quzhou-fabriek` (aannemelijk: één bron) | G60 Shanghai–Kunming-corridor via Shaoxing–Jinhua | ~300 (geen publicatie; corridorlengte over de kaart) | maak_stroombeen_weg (china-extract) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ni-imip-hpal` | productiesite (HPAL/MHP) | IMIP-verwerkingszone, Bahodopi, Morowali — Huayue Nickel Cobalt (Huayou/Tsingshan) en andere HPAL/smelter-tenants op hetzelfde complex | -2.8250, 122.1600 | [1][2][16] | bron-gelegd (z15 gezien: dicht industrieel complex met grote verwerkingshallen, tanks en schoorstenen aan de kust van IMIP); **onzeker welk gebouw specifiek Huayue is** — IMIP huisvest tientallen tenants zonder naamlabel op de satelliet |
| `ni-imip-jetty` | overslag (zee) | IMIP-exporthaven, oostpunt van het complex, Bahodopi | -2.8480, 122.1980 | [1][16] | bron-gelegd (z16/z17 gezien: pier op een landtong met meerdere ligplaatsen, geladen bulk-/vrachtschepen langszij, opslagloodsen en containeryard erachter) |
| `ni-beilun-losberth` | losplek zee (hergebruikt anker, koperketen) | Ningbo–Zhoushan, Beilun-losberth | 29.9364, 121.883 | [3][koper-sitelaag] | hergebruikt — niet opnieuw satelliet-gelegd (werkwijze §1); kanttekening: dit is een containerterminal/big-bag-lading, de koper-losberth op hetzelfde punt is een bulkkade |
| `ni-quzhou-fabriek` | fabriek (fase C, stoppunt) | Huayou New Energy Technology (Quzhou) — nikkelsulfaat-/precursorfabriek, 念辛路18号, Hi-tech Industrial Park (fase II), Quzhou, Zhejiang | 28.9020, 118.8780 | [4][5][16] | **onzeker** — adres bekend uit twee Huayou-eigen bronnen, maar het exacte perceel niet gelegd: het nationale emissievergunningregister (MEE) was deze sessie onbereikbaar (endpoint opnieuw verplaatst/foutpagina, zie §7), Overpass gaf op elke poging een timeout, en Nominatim/OSM kent 念辛路 niet. Punt ligt in het geïdentificeerde hoogtechnologie-industriepark van Quzhou (z15 gezien: dicht bedrijventerrein met verwerkingshallen), niet op het specifieke kavel |

## 4 · Via-punten (alleen landbenen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b2 | 1 | Shaoxing (stadscentrum, corridor-indicator) | 29.9992, 120.5769 | pint de G60-corridor via Shaoxing i.p.v. rechtstreeks Hangzhou-zuid; **stadscentrum, geen wegvertex** — moet door de bak-agent op de doorgaande G60 geprojecteerd worden |
| b2 | 2 | Jinhua (stadscentrum, corridor-indicator) | 29.1080, 119.6486 | pint de corridor via Jinhua i.p.v. een zuidelijkere S-weg; zelfde voorbehoud als bij Shaoxing |

⚠️ Beide via-punten zijn **stadscentroïdes uit Nominatim**, geen wegvertices — Overpass was deze
sessie onbereikbaar (herhaalde timeouts op overpass-api.de en overpass.kumi.systems) om de echte
G60-op-/afritten te vinden. De bak-agent moet ze bij het wegscannen (§2 van de bakhandleiding)
projecteren op de dichtstbijzijnde G60-vertex; bij >5 km afwijking is het punt fout gelegd.

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| IMIP HPAL-cluster (Huayue e.a.) | Huayou / Tsingshan-JV en andere tenants | lateriet-erts (binnen IMIP, niet getekend) → MHP | Huayue: nameplate 60 kt Ni/j; werkelijk 85,0 kt Ni + 8,0 kt Co in MHP, 2024 | [6][7] |
| Huayou Quzhou-fabriek | Huayou New Energy Technology (Quzhou) | MHP (import) → nikkelsulfaat/precursor | 29,1 kt Ni-sulfaat/j (WoodMac 2021, verouderd — Huayue's huidige MHP-output is ~3× dit cijfer, dus Quzhou verwerkt hooguit een deel) | [9] |

## 6 · Stoppunt
De brief stopt bij de Huayou Quzhou-fabriek: geen bron noemt de volgende schakel (een
batterijcelmaker of precursor-afnemer) met naam en adres — fase D vervalt.

## 7 · Open punten
- **SCM-slurryleiding (SCM-mijn, Konawe → Huayue, IMIP) niet getekend.** Huayou's eigen
  persbericht noemt een leiding van ~62 km (pompstation bij de SCM-veredelingsfabriek op ~530 m,
  Routa-plateau, Zuidoost-Sulawesi → energiedissipatiestation Huayue in IMIP op ~130 m,
  operationeel 11-1-2024) [1][webcheck], maar het pompstation heeft **geen gepubliceerde
  coördinaat** en de SCM-mijn/veredelingsfabriek kon deze sessie niet satelliet-gelegd worden
  (geen Nominatim/Overpass-treffer voor het Routa-plateau-terrein). Conform de bindende
  toets-aanpassing begint de keten daarom bij IMIP; SCM blijft open.
- **Entiteitsverwarring bij de ontvangende HPAL-plant.** Huayou's 2024-jaarverslag noemt de
  ontvanger van de SCM-slurry "Huayue" (IMIP) [1]; een onafhankelijke bron (Merdeka/Argus, over
  dezelfde SCM-mijn) noemt de ontvangende installatie **"SLNC" op IMIP** [10][12]. Mogelijk
  dezelfde installatie onder een andere bedrijfs-/projectnaam — niet gereconcilieerd.
- **Welke kade binnen IMIP Huayue's MHP daadwerkelijk verscheept** is niet bedrijfsniveau
  gebrond; `ni-imip-jetty` is de enige export-pier die op satelliet zichtbaar is op de oostpunt
  van het complex, maar IMIP heeft meerdere bedrijfseigen steigers.
- **Welke Ningbo-terminal precies** (Beilun vs. een andere containerterminal) is niet gebrond —
  alleen "Ningbo port" uit het eerste-ladingbericht [3]. Het hergebruikte Beilun-anker is een
  **containerterminal/big-bag-lading**, terwijl de koper-losberth op hetzelfde punt een bulkkade is.
- **Huayou Quzhou-coördinaat blijft regio-niveau.** Het MEE-emissievergunningregister
  (permit.mee.gov.cn) gaf deze sessie op elk geprobeerd pad óf een foutpagina óf een lege SPA-
  shell; het eerdere werkende pad uit `zoek-chinees-adres-recept.md` (`/perxxgkinfo/syssb/xkgg/…`)
  redirect nu naar `errorinfo.jsp`. Overpass (drie mirrors) gaf alleen timeouts. Volgende stap:
  het register opnieuw proberen met een verse `tempReportKey`-sessie, of Tianditu.
- **Aandeel van Huayue's 85 kt Ni-MHP dat naar Quzhou gaat** (i.p.v. Tongxiang of derde
  afnemers) is niet gepubliceerd — vandaar "aannemelijk: één bron" in de beennaam van b2.
- **Gepubliceerde km voor b2** ontbreekt; de ~300 km is een corridorschatting over de kaart
  (Ningbo–Shaoxing–Jinhua–Quzhou langs G60), geen bronopgave.
- **Fase D** (afnemer van het Quzhou-sulfaat/precursor) niet gevonden — vervalt.

## 8 · Bronnen
[1] Huayou, corporate news — SCM-slurryleiding ~62 km, pompstation 530 m → energiedissipatiestation Huayue in IMIP ~130 m, operationeel 11-1-2024. https://www.huayou.com/en/news/corporate-news/157
[2] Huayou — Indonesia Nickel Industry (Huayue/IMIP-project). https://www.huayou.com/en/products/indonesia-nickel-industry
[3] Nasdaq/Reuters, 14-02-2022 — eerste MHP-lading (~9.500 t) van "Tsingshan Morowali port" naar Ningbo port. https://www.nasdaq.com/articles/chinas-huayou-ships-first-mhp-shipment-from-indonesia-jv
[4] Huayou, "HUAYOU Brand Nickel Cathodes Successfully Registered Again" — adres 念辛路18号, Hi-tech Industrial Park (fase II), Quzhou. https://www.huayou.com/en/news/corporate-news/216.html
[5] Huayou, Report Violations (Quzhou-vestiging) — zelfde adres bevestigd. https://www.huayou.com/en/integrity-building/reporting-of-integrity-violations
[6] Huayou Cobalt, 2024 Annual Report (PDF). https://www.huayou.com/Public/Uploads/uploadfile2/files/20250418/2024AnnualReportofHuayouCobalt.pdf
[7] Nickel Industries, 2025 Annual Report (PDF) — Huayue-productiecijfers 2024 (85,0 kt Ni + 8,0 kt Co in MHP). https://nickelindustries.com/carbon/assets/0007ea/000004/2025-Annual-Report.pdf
[8] Wikipedia — Morowali Industrial Park. https://en.wikipedia.org/wiki/Morowali_Industrial_Park
[9] WoodMac — Quzhou Huayou Cobalt Nickel Sulphate Refinery (2021, capaciteit 29,1 kt Ni/j). https://www.woodmac.com/reports/metals-quzhou-huayou-cobalt-nickel-sulphate-refinery-150004141/
[10] Merdeka Battery Materials — SCM Mine, Konawe, Zuidoost-Sulawesi, 21.100 ha. https://merdekabattery.com/en/business/scm-mine
[11] Argus Media, "Merdeka makes 2Q progress at Indonesian Ni assets" — SCM-veredelingsfabriek + slurryleiding in aanbouw. https://www.argusmedia.com/en/news-and-insights/latest-market-news/2475847-merdeka-makes-2q-progress-at-indonesian-ni-assets
[12] Global Mining Review, "MBMA expands HPAL capacity" — ore-preparation plant bij SCM, pijpleiding naar "SLNC processing plant at IMIP". https://www.globalminingreview.com/mining/27022025/mbma-expands-hpal-capacity/
[13] Indonesiaminer.com — PT SCM opent 60 km Main Hauling Road Konawe–Morowali. https://indonesiaminer.com/news/detail/pt-scm-inaugurates-60-km-mhr-strengthening-nickel-haulage-infrastructure-between-konawe-and-morowali
[14] OpenStreetMap (ODbL) via Nominatim — Indonesia Morowali Industrial Park (landuse-vlak, way/299975400, -2,8368/122,1640), Bandar Udara IMIP (-2,7997/122,1405); 衢州市-centroïde (28,9739/118,8541); 念辛路-zoekopdracht leverde geen treffer op. https://www.openstreetmap.org
[15] Nationaal emissievergunningregister (MEE, permit.mee.gov.cn) — geprobeerd, deze sessie onbereikbaar/verhuisd; zie §7 en `v2/design/zoek-chinees-adres-recept.md`.
[16] Esri World Imagery via `v2/tools/sat_check.py` (z13–z17, live) — `v2/build-cache/satcheck/sat-nikkel-morowali-quzhou-imip-overzicht.png`, `-imip-kade.png`, `-imip-jetty.png/-jetty2.png/-jetty3.png`, `-quzhou-gaoxin-overzicht.png`, `-quzhou-gaoxin-z15.png`.

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `nikkel-morowali-quzhou`** → `v2/data/stroomroute-nikkel-morowali-quzhou.json` — 3 benen.
4.704,1 km. 4 markers: zee (stippel) 95,6 km · zee 4.202,5 km · truck 406,0 km.
Recept: `bak_stromen.sh` (functie `bak_nikkel_morowali_quzhou`). Toelichting: haven-aanloop
IMIP-jetty (Bahodopi) 95,6 km (stippel — de kade ligt 92,9 km van de dichtstbijzijnde
MARNET-zeeknoop, 5491 op −2,03570/122,00170; `maak_havenaanloop.py` vond op de eerste trap
(0,01° gebufferd) een schoon pad, 0% over land); zeebeen MARNET IMIP → Ningbo/Beilun-losberth
4.202,5 km (Beilun is het hergebruikte anker uit de koperketen, al aangesloten — geen tweede
aanloop aan die kant); wegscan (profiel `nikkel-morowali-quzhou-beilun-quzhou` in
`maak_stroombeen_weg.py`, `china`-extract, `--bron geofabrik`) Beilun → Huayou Quzhou-fabriek
406,0 km — beide via-punten (Shaoxing/Jinhua, Nominatim-stadscentroïdes) projecteerden zelf op de
doorgaande G60 met een snap van 0,00–0,16 km (ruim binnen de 5 km-drempel, dus de corridorkeuze
klopt). Tegen de corridorschatting van de brief van ~300 km (§7, geen bronopgave) is dat **+35,2%** —
GEEN ±15%-toets, alleen een referentie voor later gebruik, precies zoals de brief zelf al
aangeeft dat de 300 km een schatting over de kaart is en geen citaat. Naad tussen het zeebeen en
het truckbeen: 1,27 km (Beilun-losberth ligt zelf 1,27 km van het net — dezelfde eigenschap van
dit hergebruikte anker die in de koperketen al is vastgesteld, container-/big-bag-kade in plaats
van bulkkade; bestaand procesgat, niet dichtgetrokken). Fase D vervalt (brief §6, geen afnemer
gevonden). IMIP-processing (Huayue) → IMIP-jetty blijft eigen terrein en ongetekend (ketenkaart
§1, alleen de site-marker staat op de kaart); de SCM-slurryleiding (Konawe → IMIP) blijft volledig
open (brief §7, pompstation niet gelokaliseerd). Toets: `toets_knikken.py` geeft 50 knikken ≥60°
op de truck-geometrie, waarvan 1 omkering ≥150° en **0 terugloop** (spikes/krappe bochten, geen
reparatie nodig); `toets_rechte_benen.py --min-km 5` vindt geen ongeteste rechte lijn voor deze
stroom (omwegfactoren 1,029 / 1,182 / 1,297); json geldig (versie 2, punt_formaat lonlat, alle
modaliteiten in {zee, truck}, elk been ≥ 2 punten, 63,3 KB).

**Gereedschapslessen:**
- Een hergebruikt anker draagt zijn bestaande snap-eigenschappen mee: Beilun-losberth ligt al
  1,27 km van het net (container-/big-bag-kade i.p.v. bulkkade, bekend uit de koperketen) — die
  naad hoort bij het anker, niet bij de nieuwe wegscan die eraan vastknoopt.
- Twee Nominatim-stadscentroïdes als via-punt hoeven niet handmatig op de doorgaande weg
  geprojecteerd te worden: de wegscan snapt ze zelf binnen enkele tientallen meters van de G60,
  zolang het venster (60 km) ruim genoeg is om de corridor niet te missen.
- Een ontbrekende gepubliceerde km (brief §7: "geen publicatie, corridorschatting over de kaart")
  hoort niet als ±15%-bevinding gerapporteerd te worden — de +35,2% tegen zo'n schatting is een
  referentiegetal voor toekomstig gebruik, geen falen van de scan.
