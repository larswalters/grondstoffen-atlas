# Routebrief (licht) · Zeldzame aardmetalen · Kuantan (LAMP) → Houston → Pasadena (Verenigde Staten)

**stroom-id:** `ree-kuantan-pasadena` · **geschreven:** 2026-10-29 · **werkwijze:** licht (M31 golf 13) · **status:** gebakken
**Keten in één zin:** Lanthaanoxide van de Lynas Advanced Materials Plant (LAMP) in Gebeng gaat per **truck** naar Westports (Port Klang), per
**zeeschip** (MARNET, via Suez en de Straat van Florida) naar Barbours Cut in Houston en per **truck** naar de Ketjen Bayport Plant (ex-Albemarle) in Pasadena, Texas.
**Welke as van het verhaal:** de niet-magneethelft van REE: lanthaan voor katalysatoren (FCC), uit de enige grote niet-Chinese scheiding. **~1,2 kt/j (indicatie)**
Maleisië → VS in totaal (13% van ~9 kt VS-import compounds en metalen, gem. 2021–24 [2]); het Ketjen-deel is niet apart gepubliceerd (§7).

## 1 · Ketenkaart
```
LAMP Gebeng `ree-lamp-gebeng` (hergebruikt anker, ree-kuantan-japan.md)
  ──(b1 truck · E8 Pantai Timur → Karak Highway → KL–Klang · 336,5 km getekend, LETTERLIJKE KOPIE van ree-kuantan-japan b1)──►
Westports, Port Klang `ree-kuantan-japan-westport-kade` (hergebruikt anker)
  ──(b2 zee · Malakka → Indische Oceaan → Suez → Gibraltar → Atlantisch → Straat van Florida → Golf · 21.437 km, MARNET)──►
Barbours Cut Terminal, Houston `ree-houston-kade` (hergebruikt anker, ree-larochelle-sanmarcos.md; haven = aanname)
  ──(b3 truck, aannemelijk: één bron · E Main St → TX-146 Business → W Fairmont Pkwy → Bay Park Rd · OSRM 10,5 km)──►
Ketjen Bayport Plant, 13000 Bay Park Rd, Pasadena `ree-ketjen-bayport`
  ⏹ stoppunt: de katalysatorfabriek is de afnemer van deze lading
```

## 2 · Benen
| # | fase | modaliteit | van → naar | corridor bij naam | km (bron) | geometrie | stippel? |
|---|---|---|---|---|---|---|---|
| b1 | C | truck | `ree-lamp-gebeng` → `ree-kuantan-japan-westport-kade` | Lebuhraya Pantai Timur (E8) → Karak Highway (E8/E9) → KL–Klang-corridor | hemelsbreed 258 km, geen wegkm; getekend 336,5 km (+16% op de kaartschatting 290, zie ree-kuantan-japan §9) [11] | KOPIE `ree-kuantan-japan-weg-gebeng-westport.geojson` | nee |
| b2 | C | zee | `ree-kuantan-japan-westport-kade` → `ree-houston-kade` | Straat Malakka, Rode Zee/Suez, Straat van Florida (route kiest MARNET) | geen gepubliceerde km; MARNET-test 21.436,8 km (2.274 punten, 164 MARNET- + 16 track-edges) [10] | MARNET | aanloop: nee (Westports 2,34 km, Houston-kade 1,56 km van zeeknoop 6228, router snapt 0,02 km) |
| b3 | D | truck | `ree-houston-kade` → `ree-ketjen-bayport` | George Altvater Blvd → E Barbours Cut Blvd → E Main St → TX-146 Business (Broadway) → W Fairmont Pkwy → Bay Park Rd | hemelsbreed 7,9 km, geen wegkm; OSRM-indicatie 10,5 km (OSM-gebaseerd) [8] | maak_stroombeen_weg (`us-texas`) | nee; site ligt aan Bay Park Rd (0 km last mile) |

## 3 · Ankers (één per site en per overslag)
| id | rol | naam | lat, lon | bron | status |
|---|---|---|---|---|---|
| `ree-lamp-gebeng` | fabriek (start) | Lynas Advanced Materials Plant, Gebeng | 4.0034, 103.3775 | [3] hergebruik `ree-kuantan-japan.md` §3 | bron-gelegd (zie die brief: plantcomplex met procesgebouwen) |
| `ree-kuantan-japan-westport-kade` | overslag truck → zee | Westports Malaysia, Pulau Indah | 2.9498, 101.3076 | hergebruik `ree-kuantan-japan.md` §3 | bron-gelegd (z14 in die brief: kadelijn, containerstapels) |
| `ree-houston-kade` | losplek zee / overslag zee → truck | Barbours Cut Container Terminal, La Porte (Houston) | 29.6819, -94.9983 | hergebruik `ree-larochelle-sanmarcos.md` §3 [12] | aannemelijk (z15 hier gezien: kadefront met ≥5 portaalkranen, containerstapels, afgemeerd schip; welke Houston-terminal ontvangt de lading is een aanname, ImportGenius noemt alleen "Houston") |
| `ree-ketjen-bayport` | afnemer / fabriek | Ketjen Bayport Plant, 13000 Bay Park Rd, Pasadena TX 77507 | 29.6417, -95.0654 | [4] EPA FRS: "KETJEN BAYPORT PLANT" 29.64174, -95.0654; adres bevestigd door [1] | bron-gelegd (z16 gezien, `sat-ree-kuantan-pasadena-ketjen-frs.png`: procescomplex met tanks en een stoompluim, aan weerszijden van Bay Park Road; plant staat niet in OSM) |

## 4 · Via-punten
| been | # | punt | lat, lon | waarom hier |
|---|---|---|---|---|
| b1 | 1–6 | Kuantan · Bentong · Genting Sempah · Gombak-tolplein · Shah Alam · Pulau Indah | LETTERLIJK `ree-kuantan-japan.md` §4 (kopie, geen herberekening) | corridorkeuzes van de bestaande stroom |
| b3 | 1 | E Main St, ten oosten van het centrum van La Porte | 29.6715, -95.0066 | pint E Main St i.p.v. Barbours Cut Blvd/SH-225 westwaarts; bewust niet in het centrum (Main x Broadway, 29.6655, -95.0194) |
| b3 | 2 | TX-146 Business (Broadway) x W Fairmont Pkwy | 29.6529, -95.0190 | corridorkeuze: Fairmont westwaarts, niet door naar Bay Area |
| b3 | 3 | W Fairmont Pkwy, halverwege | 29.6520, -95.0438 | houdt de lijn op de primary i.p.v. de buurtstraten ten noorden |
| b3 | 4 | W Fairmont Pkwy x Bay Park Rd | 29.6520, -95.0654 | afslag zuidwaarts naar de fabriek (1,1 km Bay Park Rd) |

Alle b3-punten komen uit de OSRM-geometrie en liggen dus op de weg; Bay Park Rd (way 15423643, tertiary) bevestigd via Overpass [7].

## 5 · Verwerkingsknopen
| knoop | eigenaar | in → uit | capaciteit | bron |
|---|---|---|---|---|
| LAMP Gebeng | Lynas | Mt Weld-concentraat (via Kalgoorlie) → NdPr-oxide, Ce, LaCe-carbonaat/-oxide, zware REE | NdPr-nameplate 10.500 t/j (ree-sitelaag) | [3] |
| Ketjen Bayport Plant | Ketjen (Albemarle ~49%, KPS controle) | La-oxide → FCC-/ZSM-5-katalysatoren (aannemelijk) | niet gepubliceerd; ZSM-5-capaciteit verdubbeld 2025 | [1][5][6] |

## 6 · Stoppunt
De brief stopt bij de Ketjen-fabriek zelf: het is de op de Bill of Lading genoemde consignee ("Ketjen LLC-Bayport Plant", product "La Oxide") [1]; verdere afzet (raffinaderijen) is niet per lading gebrond. Fase E vervalt.

## 7 · Open punten
- **Haven is een aanname.** ImportGenius noemt Houston als top-poort van Ketjen (13 containers, 239 t, laatste 15 okt 2026), maar het voorbeeld-B/L loopt via Long Beach en de Albemarle-records tot 2022 (101 containers, 1.838 t) via Los Angeles [1]. Barbours Cut is gekozen als bestaand anker; Bayport Container Terminal (ander terrein, ander dan de "Bayport Plant") is even goed mogelijk.
- **Volume per lading niet gepubliceerd.** De ~1,2 kt/j is Maleisië → VS in totaal (USGS [2], gem. 2021–24 gewicht); ImportGenius geeft alleen cumulatieve tonnages zonder startdatum en met betaalmuur [1].
- **Product:** het B/L zegt "La Oxide", Lynas noemt LaCe-carbonaat/-oxide en Ce [3]; of dit zuiver La of LaCe is, is niet te zien. Het is lanthaan voor katalysatoren, geen magneetmetaal.
- **b1 is niet gebrond als route van deze lading**: kopie van een stroom waar alleen Time.com de truckcorridor Gebeng → Port Klang noemt [11]; geen wegkm gepubliceerd (+16% getekend tegen kaartschatting).
- **Zeeroute via Suez** is wat MARNET kiest; of schepen nu via de Kaap varen is niet gemodelleerd.
- **Westports als uitvoerhaven** (en niet Kuantan Port) volgt uit de bestaande brief, niet uit een bron voor deze lading.

**Volume-notitie:** jaarvolume in kt REO per jaar: **~1,2 kt/j (indicatie, bovengrens voor deze as)** = 13% Maleisië-aandeel × ~9 kt VS-import compounds en metalen (USGS MCS 2026, gem. 2021–24) [2]; eigen omrekening. Ketjen: 239 t in 13 containers cumulatief (laatste okt 2026) [1].

## 8 · Bronnen
[1] ImportGenius, "Lynas Malaysia Sdn Bhd" (Ketjen LLC-Bayport Plant, Houston; Albemarle-Bayport, Los Angeles; B/L "La Oxide"), gelezen 2026-10-29. https://www.importgenius.com/suppliers/lynas-malaysia-sdn-bhd
[2] USGS, Mineral Commodity Summaries 2026, Rare Earths (importbronnen 2021–24: China 71%, Maleisië 13%; compounds-import 7.730 / 10.800 / 8.970 / 8.120 t). https://pubs.usgs.gov/periodicals/mcs2026/mcs2026-rare-earths.pdf
[3] Lynas Rare Earths, Kuantan, Malaysia (producten NdPr, Ce, LaCe, zware REE; klanten Oost-Azië, VS, Europa). https://lynasrareearths.com/kuantan-malaysia-2/
[4] US EPA FRS, faciliteit "KETJEN BAYPORT PLANT", 13000 Bay Park Road, Pasadena TX, 29.64174 / -95.0654. https://frs-public.epa.gov/ords/frs_public2/frs_rest_services.get_facilities?facility_name=KETJEN&state_abbr=TX&output=JSON
[5] Ketjen, "Completes Expansion of its Bayport ZSM-5 Facility" (EHCMA, sept 2025; pagina 403 voor WebFetch, gelezen via zoekresultaat). https://www.ehcma.org/news/712075/Ketjen-Completes-Expansion-of-its-Bayport-ZSM-5-Facility.htm
[6] Albemarle verkoopt controlerend belang in Ketjen aan KPS (okt 2025). https://www.indianchemicalnews.com/general/lite/albemarle-sells-controlling-stake-in-ketjen-to-kps-capital-partners-27984
[7] OpenStreetMap (ODbL) via Overpass: Bay Park Road way 15423643 / 15427596 (tertiary), W Fairmont Parkway (primary). https://www.openstreetmap.org
[8] OSRM demo-router (OSM): Barbours Cut → Ketjen 10,5 km, stappen en geometrie voor §4. https://router.project-osrm.org/
[9] Esri World Imagery via `v2/tools/sat_check.py`: `v2/build-cache/satcheck/sat-ree-kuantan-pasadena-{barbours,baypark,ketjen-frs}.png`.
[10] Eigen MARNET-test (`hecht_marnet.py route`, zee Westports → Barbours Cut): 21.436,8 km, snap 2,336 / 0,019 km, via Suez en de Straat van Florida.
[11] `ree-kuantan-japan.md` (b1-kopie, Time.com-bron voor de corridor) en `ree-mtweld-kuantan.md` (LAMP-anker).
[12] `ree-larochelle-sanmarcos.md` (Barbours Cut 29.6819, -94.9983; Wikipedia "Barbours Cut Terminal"). https://en.wikipedia.org/wiki/Barbours_Cut_Terminal
[13] Molycorp 10-Q 2010: lanthaan-concentraat gaat naar de FCC-industrie (achtergrond voor het gebruik). https://www.sec.gov/Archives/edgar/data/0001489137/000095012310083950/c05639e10vq.htm

## 9 · Gebakken (2026-10-29, lichte werkwijze, M31 golf 13)
`bash v2/tools/bak_stromen.sh ree-kuantan-pasadena` (functie `bak_ree_kuantan_pasadena`) → `v2/data/stroomroute-ree-kuantan-pasadena.json`, 136 KB, versie 2, lonlat, 3 benen, 4 markers, totaal 21.783,6 km.

| # | modaliteit | km | brief | naad | beschrijving |
|---|---|---|---|---|---|
| 1 | truck | 336,5 | hemelsbreed 258, geen wegkm; getekend 336,5 | start | LETTERLIJKE KOPIE `ree-kuantan-japan-weg-gebeng-westport.geojson`, 4.673 punten |
| 2 | zee | 21.436,8 | eigen MARNET-test 21.436,8 | 2,34 (snap Westports) | MARNET kade → kade, 16 track- + 164 MARNET-edges, 2.274 punten, geen aanloop |
| 3 | truck | 10,3 | hemelsbreed 7,9, OSRM 10,5; scan 10,2 | 0,02 | profiel `ree-kuantan-pasadena-barbours-ketjen` (wegscan_puur, extract us-texas), 227 punten, 5 via-punten op de weg |

**Markers** (4): alle vier 0,00 km van hun lijn (LAMP, Westports, Barbours Cut, Ketjen).
**Recept:** b1 = voorgebakken kopie; b2 = `--been zee` kade → kade (Westports snapt 2,34 km, Barbours Cut 0,02 km; beide < 5 km dus geen haven-aanloop); b3 = voorgebakken weg uit de wegscan (geen omwegen, alle via-snaps 0,00 km). Geen stippel, lucht, leiding, last mile; fase E vervalt.
**Toets:** naden max 2,34 km (zee-snap Westports, < 5); json.load ok; modaliteiten {truck, zee}; `toets_rechte_benen`: geen recht been. `toets_knikken`: b1 43 knikken en 2 omkeringen (erfenis van de kopie, geen terugloop), zee 6 (krappe bochten R 5-8 km, o.a. Bahama-kanaal en Malakka), b3 9 spikes (R 5-15 m) rond E Main St bij La Porte, geen terugloop.
**Bevindingen/open:** zie §7; Houston-haven is een aanname en b1 is niet gebrond voor deze lading. b3 10,3 km is +-2% van OSRM 10,5, alleen indicatie (geen gepubliceerde wegkm).
**Lessen:** een eerder voorbereid profiel en een gescand b3-geojson hergebruiken scheelde de scan; bij twee hergebruikte havenankers volstaat de MARNET-snap < 5 km zonder aanloop.
