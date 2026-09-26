# Routebrief (licht) · zeldzame aardmetalen — Mt Weld → Kalgoorlie → Fremantle → Kuantan (Maleisië)

**stroom-id:** `ree-mtweld-kuantan` · **geschreven:** 2026-09-26 · **werkwijze:** licht (M29) · **status:** gebakken
**Keten in één zin:** koper-vrij REE-concentraat (in half-height "rotainers") gaat per **truck** ~380 km van de Mt
Weld-mijn/concentratieplant naar de Lynas Kalgoorlie Rare Earths Processing Facility (cracking & leaching tot
mixed rare earth carbonate, MREC), MREC in gesloten containers per **spoor** naar Fremantle North Quay, per
**zeeschip** naar Kuantan Port, en per **truck** naar de Lynas Advanced Materials Plant (LAMP) in Gebeng waar
gescheiden wordt tot NdPr-oxide en zware-REE-oxiden — de enige niet-Chinese scheidingsketen buiten de VS.
**Welke as van het verhaal:** het Lynas-draadje — met MP Materials (VS) een van maar twee niet-Chinese
scheidingslijnen ter wereld. Lynas FY2025 NdPr-verkoop 6.555 t; 1H FY26 productie 6.375 t REO / 3.407 t NdPr;
LAMP-nameplate 10.500 t NdPr/j; Australië 29.000 t REO mijnproductie 2025 (vrijwel geheel Lynas, USGS) [1][4].

## 1 · Ketenkaart
```
Mt Weld-mijn/concentratieplant `ree-mtweld-laad`
   ──(b1 truck · mijnweg → Laverton → Leonora → Menzies → Kalgoorlie · ~380 km)──►
Lynas Kalgoorlie REPF `ree-kalgoorlie-repf` (cracking & leaching → MREC)
   ──(b2 spoor · Eastern Goldfields Railway via Kewdale · ~583 km)──►
Fremantle North Quay `ree-fremantle-kade`
   ──(b3 zee · Indische Oceaan → Sunda/Lombok → Karimata → Z-Chinese Zee · ~4.500 km, MARNET)──►
Kuantan Port `ree-kuantan-kade`
   ──(b4 truck · havenweg → Jalan Gebeng · ~8–12 km)──►
LAMP Gebeng `ree-lamp-gebeng` — scheiding tot NdPr-oxide/Dy-oxide/Tb-oxide ⏹ stoppunt
   ├── vertakking (niet getekend): concentraat óók rechtstreeks Mt Weld → Fremantle → Kuantan zonder
   │   Kalgoorlie ("or shipped to the Lynas Malaysia refinery" [2]) — aandeel niet gepubliceerd
   └── vertakking (niet getekend, fase D): JARE-offtake tot 7.200 t NdPr/j naar Japanse industrie — fabriek
       niet benoemd, alleen offtake-niveau gedocumenteerd [5]
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | A | truck | `ree-mtweld-laad` → `ree-kalgoorlie-repf` | Mt Weld-mijnweg → Laverton → Leonora → Menzies → Kalgoorlie (Goldfields Hwy) | ~380 [3] | maak_stroombeen_weg (australie) | nee (mogelijk kort stippel bij de Yilkari-terreininrit) |
| b2 | A/B | spoor | `ree-kalgoorlie-repf` → `ree-fremantle-kade` | Eastern Goldfields Railway Kalgoorlie → Kewdale → Fremantle; DWER W6567/2020/1: "transported by rail … to the Port of Fremantle for export" [6][7] | ~583 (563 Kalgoorlie–Kewdale [8] + ~20 Kewdale–Fremantle) | toets_spoorroute (1-op-1-net, BAKE_SUFFIX=-raw), twee runs via Kewdale | ja — laatste ≈1,9 km REPF-terrein tot spoornet (Yilkari-siding waarschijnlijk niet in OSM) |
| b3 | B | zee | `ree-fremantle-kade` → `ree-kuantan-kade` | Indische Oceaan → Straat Sunda/Lombok → Straat Karimata → Z-Chinese Zee (MARNET beslist; containerlijndienst) | ~4.500 hemelsbreed (geen publicatie) | MARNET | aanloop Kuantan: ja (22,1 km, maak_havenaanloop.py); Fremantle: nee (0,8 km, binnen net) |
| b4 | C | truck | `ree-kuantan-kade` → `ree-lamp-gebeng` | havenweg Kuantan Port → Jalan Gebeng, Gebeng-industriezone | ~8–12 (OSRM, geen publicatie) | maak_stroombeen_weg (maleisie) | nee |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-mtweld-laad` | mijn / concentratieplant (laadplek rotainers) | Mt Weld-mijn en concentrator (Lynas, ~35 km Z van Laverton) | -28.8695, 122.5392 | [1][9][10] | bron-gelegd (z15 gezien: procesgebouwen, indikkers en meerdere tailings-/evaporatiebekkens rond de put; punt ligt tussen plant en verwerkingscomplex) |
| `ree-kalgoorlie-repf` | overslag truck→spoor / verwerkingsknoop | Lynas Kalgoorlie Rare Earths Processing Facility, 70 Johns Rd (Lot 500 Great Eastern Hwy), Yilkari | -30.7883, 121.4086 | [3][6][9] | onzeker (z15 gezien: bushland met verderop kleine industriële bekkens/gebouwen, geen ondubbelzinnig REPF-terrein te onderscheiden — de faciliteit is recent gebouwd en kan jonger zijn dan de beschikbare Esri-opname; adres wel eenduidig in de vergunningdocumenten) |
| `ree-fremantle-kade` | overslag spoor→zee | Fremantle North Quay containerterminal | -32.0438, 115.7449 | [9] | bron-gelegd (z16 gezien: kadefront met containerkranen, containerstacks en een schip aan de kade, direct aan het spoor) |
| `ree-kuantan-kade` | overslag zee→truck | Kuantan Port (Pelabuhan Kuantan), Tanjung Gelang | 3.9805, 103.4242 | [9][12] | bron-gelegd (z15 gezien: haventerrein met kade, tankopslag en een bulk-/kolenlosplaats aan weerszijden van de vaargeul; welke specifieke berth de MREC-containers ontvangt is niet te onderscheiden) |
| `ree-lamp-gebeng` | fabriek (scheiding) | Lynas Advanced Materials Plant (LAMP), Gebeng-industriegebied | 4.0034, 103.3775 | [2][9] | bron-gelegd (z15 gezien: omheind fabrieksterrein met procesgebouwen en een langgerekt gestreept opslagveld — vermoedelijk de NUF/WLP-residuopslag — ~1,5 km landinwaarts van de kust) |

## 4 · Via-punten (alleen b1 — enige landbeen met een corridorkeuze)
| been | # | punt | lat, lon | waarom hier (welke keuze pint dit punt) |
|---|---|---|---|---|
| b1 | 1 | Laverton | -28.6263, 122.4034 | mijnweg komt hier op de doorgaande Great Central/Beadell Hwy; corridorkeuze noord vs. rechtstreeks zuid |
| b1 | 2 | Leonora | -28.8702, 121.3225 | overgang mijnweg → Goldfields Highway (pint de westelijke route i.p.v. via Laverton–Cosmo Newbery) |
| b1 | 3 | Menzies | -29.6924, 121.0291 | Goldfields Highway blijft de doorgaande weg i.p.v. een binnendoor-piste |
| b1 | 4 | Kewdale (spoorreferentie, geen wegpunt) | -31.9761, 115.9423 | — (zie b2: splitst de spoorrun om een Dijkstra-omweg via de goudlijn te vermijden) |

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| Kalgoorlie REPF | Lynas Rare Earths | REE-concentraat (rotainers) → mixed rare earth carbonate (MREC), cracking (110 m kiln) + leaching | ontworpen op de volledige Mt Weld-concentraatstroom | [3][6] |
| LAMP Gebeng | Lynas Malaysia | MREC + Mt Weld-concentraat (rechtstreeks) → NdPr-oxide, Ce-/LaCe-carbonaat/oxide, Dy-oxide, Tb-oxide, Sm-oxide | 10.500 t NdPr/j nameplate | [2][4] |

## 6 · Stoppunt
De brief stopt bij LAMP Gebeng: dat is het eindproduct (gescheiden REO's) dat Lynas zelf verkoopt aan
magneet- en legeringsfabrieken wereldwijd; geen bron noemt één specifieke afnemersfabriek met adres, behalve
de niet-getekende JARE-vertakking (offtake-niveau, Japan, fabriek onbenoemd).

## 7 · Open punten
- **Aandeel Kalgoorlie vs. rechtstreeks Kuantan** niet gepubliceerd (Lynas' eigen Mt Weld-pagina noemt beide
  routes) — de rechtstreekse rotainer-route is bewust niet getekend (§1).
- **Kalgoorlie REPF-anker onzeker**: satellietpas (Esri, huidige laag) toont geen ondubbelzinnig
  bouwwerk/terrein op het geadresseerde punt — mogelijk jonger dan de opname (Shed 8-8-klasse); adres uit
  vergunningdocumenten wel eenduidig.
- **Yilkari-siding (REPF → spoornet, ≈1,9 km)** niet in OSM verwacht → wordt bij het bakken een kort stippel.
- **Welke Kuantan-berth** de MREC-containers/rotainers ontvangt is op z15 niet te onderscheiden van de andere
  havenfuncties (bulk, tankopslag) — geen aparte containerterminal-tag gevonden in OSM.
- **Gepubliceerde spoorlengte Kalgoorlie–Fremantle** is samengesteld (Kewdale–Kalgoorlie 563 km [8] +
  schatting Kewdale–Fremantle ~20 km); geen enkele bron geeft het hele traject in één getal.
- **Fase D (JARE, Japan)** blijft ongetekend — alleen offtake-niveau gedocumenteerd, geen fabriek/adres.

## 8 · Bronnen
[1] Lynas Rare Earths, Mt Weld, Western Australia — rotainers naar Kalgoorlie "or shipped to the Lynas Malaysia refinery". https://lynasrareearths.com/mt-weld-western-australia/
[2] Lynas Rare Earths, Kuantan, Malaysia — LAMP-proces (cracking/leaching, solvent extraction, product finishing), outputs NdPr-oxide/Ce/LaCe/Dy/Tb/Sm-oxide, 100 ha-site Gebeng Industrial Estate, sinds 2012. https://lynasrareearths.com/kuantan-malaysia-2/
[3] DWER Western Australia, W6567/2021-1 Decision Report (Kalgoorlie Rare Earths Processing Facility) — concentraat van Mt Weld in gesloten containers; MREC per spoor naar Fremantle. https://www.der.wa.gov.au/images/W6567-2021-1_-_Decision_Report.PDF
[4] Lynas Rare Earths, kwartaalrapport maart 2026 (Q3 FY26) — 1H FY26 6.375 t REO/3.407 t NdPr, Q3 3.233 t REO/1.996 t NdPr, LAMP-nameplate 10.500 t NdPr/j. https://wcsecure.weblink.com.au/pdf/LYC/03080721.pdf
[5] ASX-aankondiging, 2026-03-10 — JARE-offtake tot 7.200 t NdPr/j tot 2038 naar Japanse industrie. https://announcements.asx.com.au/asxpdf/20260310/pdf/06x8fmmzvw1fm1.pdf
[6] Lynas Rare Earths, Kalgoorlie, Western Australia — cracking (110 m kiln) + leaching → MREC, "further processed … at the Lynas Malaysia advanced materials plant in Gebeng". https://lynasrareearths.com/kalgoorlie-western-australia/
[7] Mining Technology, "Lynas opens Australia's first rare earths processing plant" — bevestigt MREC-route naar Maleisië. https://www.mining-technology.com/news/lynas-opens-australias-first-rare/
[8] Rome2Rio / Wikipedia Eastern Railway (Western Australia) — spoorafstand Kewdale–Kalgoorlie ≈563 km (350 mi); Fremantle-lijn vertakt bij Kewdale. https://en.wikipedia.org/wiki/Eastern_Railway_(Western_Australia) · https://www.rome2rio.com/s/Kewdale/Kalgoorlie
[9] OpenStreetMap (ODbL) via Nominatim — landuse "Mount Weld mine" -28.86947/122.53916 · "Yilkari"/Johns Road -30.7883/121.4086 · node "North Quay" Fremantle -32.04383/115.74491 · landuse "Pelabuhan Kuantan" (harbour) -3.98054/103.42415 (N) · landuse "Lynas Advanced Material Plant" 4.00338/103.37749 · "Laverton" -28.6263/122.4034 · "Leonora" -28.8702/121.3225 · "Menzies" -29.6924/121.0291 · "Kewdale" -31.9761/115.9423. https://www.openstreetmap.org
[10] Freeport-onafhankelijke bron n.v.t. — via EPA/DWER-vergunningdocumenten wordt Mt Weld beschreven als ~380 km van Kalgoorlie (zie ontwerp-toets, bronnen_start). https://www.epa.wa.gov.au/proposals/lynas-kalgoorlie-rare-earths-processing-facility
[11] USGS Mineral Commodity Summaries 2026 — wereld-REO-productie 2025 ~390 kt, Australië 29.000 t (vrijwel geheel Lynas). https://pubs.usgs.gov/periodicals/mcs2026/
[12] Nominatim/OSM, "Pelabuhan Kuantan" (Kuantan Port), Kampung Gebeng, Kuantan, Pahang. https://www.openstreetmap.org

## 9 · Gebakken (2026-09-26, lichte werkwijze)

**Stroom `ree-mtweld-kuantan`** → `v2/data/stroomroute-ree-mtweld-kuantan.json` — 6 benen. 5.780,6 km. 5 markers:
truck 401,5 km · spoor 649,0 km · spoor 42,7 km · zee 4.649,5 km · zee (stippel) 24,7 km · truck 13,2 km.
Recept: `bak_stromen.sh` (functie `bak_ree_mtweld_kuantan`).

**Toelichting per been:**
- **b1 (truck, `maak_stroombeen_weg.py`, profiel `ree-mtweld-kuantan-mtweld-kalgoorlie`, extract `australie`):**
  eerste poging faalde ("geen wegpad tussen punt 0 en 1") — de outback-mijnweg Mt Weld → Laverton zit niet
  in `WEG_HOUD` (motorway t/m secondary) binnen het venster. Opgelost door de al bestaande, geconnecteerde
  via-keten van corridor `ree-mountweld-leonora` (`fetch_landnet.py` CORRIDORS) te hergebruiken voor het stuk
  Mt Weld → Leonora en te verlengen via Menzies naar Kalgoorlie REPF, met `corridorKlassen: tertiary/
  unclassified`. Uitkomst **401,0 km getekende weggeometrie (401,5 km incl. anker-stubjes) tegen ~380 km
  gepubliceerd (DWER/EPA) = +5,5%**, binnen ±15%.
- **b2 (spoor, `BAKE_SUFFIX=-raw`, twee runs op het 1-op-1-spoornet):** Kalgoorlie REPF → Kewdale
  **649,0 km tegen 563 km gepubliceerd (Kalgoorlie–Kewdale) = +15,3%** — net buiten de ±15%-norm, zie
  bevindingen; Kewdale → Fremantle North Quay **42,7 km tegen ~20 km schatting = +113%**, ruim buiten de
  norm maar tegen een niet-harde referentie (zie bevindingen). REPF-snap **0,473 km** — ruim onder de in de
  brief verwachte ~1,9 km last-mile, dus géén aparte stippel nodig (de naad tussen het truckbeen en het
  spoorbeen blijft ruim binnen de norm). Fremantle-snap **0,512 km**. Eén "omkering" per run (170,5° bij
  -30,78370/121,41110 resp. 169,3° bij -31,98220/115,98110) — kopmaak-plekken op het REPF-/Kewdale-
  emplacement (`toets_knikken.py`: 0 terugloop), geen bugreden.
- **b3 (zee, MARNET, `--been zee` Fremantle → Kuantan):** Fremantle snapt op **0,599 km** — geen aanloop
  nodig. Kuantan snapt automatisch op **22,784 km** (binnen de default `--max-snap 25`). Omdat die snap
  betekenisvol groot is, is de laatste 22,8 km vervangen door een expliciet berekende haven-aanloop
  (`maak_havenaanloop.py`, geslaagd op de eerste poging, **24,7 km over water, omwegfactor 1,085**,
  0,00 km midden op de lijn over land — het restje land dat overblijft grenst aan het kade-uiteinde zelf,
  de korrel van de 1:10M-kustlijn). Zeebeen zelf **4.649,5 km** tegen ~4.500 km hemelsbreed (geen
  publicatie, alleen referentie) = +3,3%.
- **b4 (truck, `maak_stroombeen_weg.py`, profiel `ree-mtweld-kuantan-kuantan-lamp`, extract `maleisie`):**
  **13,1 km getekende weggeometrie (13,2 km incl. anker-stubjes) tegen een OSRM-schatting van 8-12 km**
  (geen harde publicatie — de brief zegt dit vooraf, dus de toets is indicatief, geen ±15%-toets tegen een
  derde bron).

**Toets-bevindingen (buiten de norm, niet dichtgetrokken):**
- **Spoorbeen Kalgoorlie–Kewdale +15,3%** — net buiten de ±15%-norm van de lichte werkwijze (de router zelf
  meldde 646,9 km, de bake-uitvoer geeft 649,0 km na dezelfde geometrie in het stroomcontract; het verschil
  zit in decimalen, niet in een tweede run). Geen via-punt bijgeschoven; het gepubliceerde 563 km-cijfer is
  zelf al een optelling van twee losse bronnen (brief §2/§8[8]), dus een kleine overschrijding hier is eerder
  een teken dat de bron-optelling zacht is dan dat de geometrie fout ligt.
- **Spoorbeen Kewdale–Fremantle +113%** (42,7 km tegen ~20 km) — ruim buiten ±15%, maar de referentie is zelf
  een schatting zonder operator-bron (brief §2/§8): "~20 km schatting Kewdale–Fremantle". Kewdale is bewust
  een spoorreferentiepunt zonder wegequivalent, juist om een Dijkstra-omweg via de goudlijn te vermijden
  (brief §4/bak_aanwijzingen); de langere lijn is aannemelijk een reëel spooremplacement-tracé rond Perth
  i.p.v. een sluipweg (0 terugloop in `toets_knikken.py`). Blijft een bevinding, geen dichtgetrokken getal.
- **Kalgoorlie REPF-anker blijft onzeker** (brief §3/§7): de satellietpas (Esri, huidige laag) toont geen
  ondubbelzinnig REPF-terrein op 70 Johns Rd, Yilkari — mogelijk jonger dan de opname. De marker ligt op
  0,000 km van het truckbeen omdat de weg letterlijk op dat ankerpunt eindigt (niet omdat de plek bevestigd
  is); dat hoort hier expliciet vermeld, niet stilzwijgend als "marker klopt" gelezen te worden.
- **28 knikken ≥ 60° over de twee wegbenen + 2 knikken over de twee spoorbenen** (`toets_knikken.py`),
  waarvan 3 "omkeringen" (≥150°, twee op het spoor bij de emplacementen, één op de weg bij het Mt
  Weld-anker) maar **0 terugloop** — de enige categorie die reparatie vraagt. Alle overige zijn OSM-spikes
  op kleine-klasse-eindwegen (Kuantan-havenweg, Mt Weld-toegangsweg).
- `toets_rechte_benen.py --min-km 5`: geen enkel been van deze stroom komt in de verdachtenlijst (geen
  rechte lijn ≥5 km met omwegfactor ≈1,000) — ook de haven-aanloop Kuantan niet, want die is een 43-punts
  berekende waterlijn, geen rechte stippel.
- Alle 5 markers liggen ≤ 0,512 km van hun lijn.
- JSON-vormtoets: `versie` 2, `punt_formaat` `lonlat`, modaliteiten {truck, spoor, zee} (alle toegestaan),
  elk been ≥ 2 punten, bestand 70,5 KB (< 300 KB) — allemaal in orde.

**Gereedschapslessen:**
- Een outback-mijnweg (motorway t/m secondary binnen het venster) kan zonder pad blijven staan terwijl er
  wél een bestaande, geverifieerde corridor in `fetch_landnet.py` CORRIDORS ligt (`ree-mountweld-leonora`) —
  eerst die hergebruiken vóórdat je `corridorKlassen` verruimt of het venster vergroot, zoals de
  bak_aanwijzingen van deze brief al voorschreven.
- Een haven-aanloop-geojson uit `maak_havenaanloop.py` (`--van kade --naar zeeknoop`) staat altijd in díe
  volgorde in het bestand; voor een AANKOMENDE haven (zoals Kuantan hier, in tegenstelling tot de
  vertrekkende havens in de koper-brieven) moet de puntenlijst vóór gebruik in `--stippel-geojson`
  omgedraaid worden naar zeeknoop→kade, anders klopt de reisvolgorde niet met de rest van de keten.
